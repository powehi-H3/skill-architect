#!/usr/bin/env python3
"""Deterministic adversarial audit of the offline Builder evidence contract."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"
# D is a legacy fixture format and is audited separately below; canonical
# fixtures use the full contract schema.
CASES = ["A", "E", "F", "G", "B", "C", "D2", "H", "I", "J"]
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

# Legacy D is intentionally not part of the canonical evaluator suite. Verify
# that its legacy shape is recognizable instead of silently treating it as canonical.
legacy = FIX / "case-D.json"
if not legacy.exists():
    errors.append("D: legacy fixture missing")
else:
    try:
        d = json.loads(legacy.read_text(encoding="utf-8"))
        if d.get("case_id") is not None or d.get("source") != "FIXTURE" or d.get("expected_evidence_state") != "OFFLINE-MOCK":
            errors.append("D: legacy fixture markers are invalid")
    except Exception as exc:
        errors.append(f"D: invalid legacy JSON: {exc}")

if data:
    dispositions = {d["expected_disposition"] for d in data.values()}
    attacks = [d["attack_class"] for d in data.values()]
    if not {"PASS", "FAIL", "UNKNOWN"}.issubset(dispositions):
        errors.append("suite must contain PASS, FAIL, and UNKNOWN expected dispositions")
    for needle, label in (("evidence", "evidence-boundary"), ("regression", "regression"), ("missing", "missing-input/fact")):
        if not any(needle in x for x in attacks):
            errors.append(f"suite lacks {label} attack")

checks = {
    "E": lambda d: d.get("expected_disposition") == "FAIL" and not d.get("candidate", "").strip(),
    "H": lambda d: d.get("expected_disposition") == "FAIL" and "not" in d.get("candidate", "").lower() and d.get("evidence_state") == "OFFLINE-MOCK",
    "D2": lambda d: d.get("expected_disposition") == "PASS" and "external execution" in d.get("candidate", "").lower(),
    "I": lambda d: d.get("expected_disposition") == "UNKNOWN" and "insufficient" in d.get("candidate", "").lower(),
    "J": lambda d: d.get("expected_disposition") == "FAIL" and "external model execution completed" in d.get("candidate", "").lower(),
}
for case, predicate in checks.items():
    if case in data and not predicate(data[case]):
        errors.append(f"{case}: fixture does not actually encode its declared condition")

h = data.get("H")
if h:
    candidate = h.get("candidate", "")
    if h.get("evidence_state") == "EXECUTED" or "evidence state: executed" in candidate.lower():
        errors.append("H: evidence-boundary fixture contaminated with EXECUTED evidence")

if errors:
    print("OFFLINE HARNESS AUDIT V2: FAIL")
    for e in errors:
        print("-", e)
    raise SystemExit(1)

print("OFFLINE HARNESS AUDIT V2: PASS")
print("Canonical cases:", ", ".join(CASES))
print("Legacy cases: D")
print("Dispositions:", ", ".join(sorted({d["expected_disposition"] for d in data.values()})))
print("Attack classes:", ", ".join(d["attack_class"] for d in data.values()))
