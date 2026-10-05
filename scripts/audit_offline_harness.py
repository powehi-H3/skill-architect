#!/usr/bin/env python3
"""Audit the offline fixture contract without an LLM.

This intentionally tests the test data and evidence boundary, not Skill quality.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"
CASES = ["A", "E", "F", "G", "B", "C", "D"]
REQUIRED = ["case_id", "attack_class", "candidate", "expected_disposition", "required_findings", "evidence_state"]

errors = []
for case in CASES:
    p = FIX / f"case-{case}.json"
    if not p.exists():
        errors.append(f"{case}: missing fixture")
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    for key in REQUIRED:
        if key not in d:
            errors.append(f"{case}: missing {key}")
    if d.get("case_id") != case:
        errors.append(f"{case}: case_id mismatch")
    if d.get("evidence_state") != "OFFLINE-MOCK":
        errors.append(f"{case}: evidence_state must be OFFLINE-MOCK")
    if not isinstance(d.get("required_findings"), list) or not d["required_findings"]:
        errors.append(f"{case}: required_findings must be non-empty list")
    if not isinstance(d.get("expected_disposition"), str):
        errors.append(f"{case}: expected_disposition missing/invalid")

# The suite must contain both positive and negative dispositions and at least
# one fixture that explicitly tests an evidence-boundary failure.
dispositions = {json.loads((FIX / f"case-{c}.json").read_text())["expected_disposition"] for c in CASES if (FIX / f"case-{c}.json").exists()}
if not {"PASS", "FAIL"}.issubset(dispositions):
    errors.append("suite must contain both PASS and FAIL expected dispositions")
attack_classes = [json.loads((FIX / f"case-{c}.json").read_text())["attack_class"] for c in CASES if (FIX / f"case-{c}.json").exists()]
if not any("evidence" in x for x in attack_classes):
    errors.append("suite lacks an explicit evidence-boundary attack")

if errors:
    print("OFFLINE HARNESS AUDIT: FAIL")
    for e in errors:
        print("-", e)
    raise SystemExit(1)
print("OFFLINE HARNESS AUDIT: PASS")
print("Cases:", ", ".join(CASES))
print("Dispositions:", ", ".join(sorted(dispositions)))
print("Attack classes:", ", ".join(attack_classes))
