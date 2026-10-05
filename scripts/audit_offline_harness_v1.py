#!/usr/bin/env python3
"""Deterministic adversarial audit of the offline Builder evidence contract.

This is intentionally independent of an LLM. It verifies that the offline suite
contains both positive and negative cases and that each attack fixture actually
contains the condition it claims to test. A passing audit is evidence about the
TEST HARNESS, not about Builder semantic quality.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"
CASES = ["A", "E", "F", "G", "B", "C", "D", "D2", "H"]
REQUIRED = ["case_id", "attack_class", "candidate", "expected_disposition", "required_findings", "evidence_state"]
errors: list[str] = []
data: dict[str, dict] = {}

for case in CASES:
    p = FIX / f"case-{case}.json"
    if not p.exists():
        errors.append(f"{case}: missing fixture")
        continue
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{case}: invalid JSON: {exc}")
        continue
    data[case] = d
    for key in REQUIRED:
        if key not in d:
            errors.append(f"{case}: missing {key}")
    if d.get("case_id") != case:
        errors.append(f"{case}: case_id mismatch")
    if d.get("evidence_state") != "OFFLINE-MOCK":
        errors.append(f"{case}: evidence_state must be OFFLINE-MOCK")
    if not isinstance(d.get("candidate"), str):
        errors.append(f"{case}: candidate must be string")
    if not isinstance(d.get("required_findings"), list) or not d["required_findings"]:
        errors.append(f"{case}: required_findings must be non-empty list")
    if d.get("expected_disposition") not in {"PASS", "FAIL", "UNKNOWN"}:
        errors.append(f"{case}: expected_disposition must be PASS, FAIL, or UNKNOWN")

if data:
    dispositions = {d["expected_disposition"] for d in data.values()}
    attacks = [d["attack_class"] for d in data.values()]
    if not {"PASS", "FAIL"}.issubset(dispositions):
        errors.append("suite must contain both PASS and FAIL expected dispositions")
    for needle, label in (("evidence", "evidence-boundary"), ("regression", "regression"), ("missing", "missing-input/fact")):
        if not any(needle in x for x in attacks):
            errors.append(f"suite lacks {label} attack")

# Semantic sanity checks: a fixture must actually contain the failure/condition
# it claims to exercise. This prevents vacuous tests that always PASS.
checks = {
    "E": lambda d: d.get("expected_disposition") == "FAIL" and not d.get("candidate", "").strip(),
    "H": lambda d: d.get("expected_disposition") == "FAIL" and "not" in d.get("candidate", "").lower() and d.get("evidence_state") == "OFFLINE-MOCK",
    "D2": lambda d: d.get("expected_disposition") == "PASS" and "external execution" in d.get("candidate", "").lower(),
}
for case, predicate in checks.items():
    if case in data and not predicate(data[case]):
        errors.append(f"{case}: fixture does not actually encode its declared condition")

# Explicitly ensure the negative evidence case cannot be promoted by metadata.
h = data.get("H")
if h:
    candidate = h.get("candidate", "")
    if h.get("evidence_state") == "EXECUTED" or "evidence state: executed" in candidate.lower():
        errors.append("H: evidence-boundary fixture contaminated with EXECUTED evidence")

if errors:
    print("OFFLINE HARNESS AUDIT V1: FAIL")
    for e in errors:
        print("-", e)
    raise SystemExit(1)

print("OFFLINE HARNESS AUDIT V1: PASS")
print("Cases:", ", ".join(CASES))
print("Dispositions:", ", ".join(sorted({d["expected_disposition"] for d in data.values()})))
print("Attack classes:", ", ".join(d["attack_class"] for d in data.values()))
