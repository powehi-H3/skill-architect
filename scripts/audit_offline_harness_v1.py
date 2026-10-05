#!/usr/bin/env python3
"""V1 audit of offline fixture/evidence contracts without an LLM."""
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"
CASES = ["A", "E", "F", "G", "B", "C", "D2", "H"]
REQUIRED = ["case_id", "attack_class", "candidate", "expected_disposition", "required_findings", "evidence_state"]
errors=[]; data={}
for case in CASES:
    p=FIX/f"case-{case}.json"
    if not p.exists(): errors.append(f"{case}: missing fixture"); continue
    try: d=json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc: errors.append(f"{case}: invalid JSON: {exc}"); continue
    data[case]=d
    for key in REQUIRED:
        if key not in d: errors.append(f"{case}: missing {key}")
    if d.get("case_id") != case: errors.append(f"{case}: case_id mismatch")
    if d.get("evidence_state") != "OFFLINE-MOCK": errors.append(f"{case}: evidence_state must be OFFLINE-MOCK")
    if not isinstance(d.get("required_findings"),list) or not d["required_findings"]: errors.append(f"{case}: required_findings must be non-empty list")
    if d.get("expected_disposition") not in {"PASS","FAIL","UNKNOWN"}: errors.append(f"{case}: invalid expected_disposition")
if data:
    dispositions={d["expected_disposition"] for d in data.values()}
    attacks=[d["attack_class"] for d in data.values()]
    if not {"PASS","FAIL"}.issubset(dispositions): errors.append("suite must contain PASS and FAIL")
    if not any("evidence" in x for x in attacks): errors.append("suite lacks evidence-boundary attack")
    if not any("regression" in x for x in attacks): errors.append("suite lacks regression attack")
    if not any("missing" in x for x in attacks): errors.append("suite lacks missing-input/fact attack")
    if data["H"].get("evidence_state") != "OFFLINE-MOCK": errors.append("H evidence state contaminated")
if errors:
    print("OFFLINE HARNESS AUDIT V1: FAIL")
    print("\n".join(f"- {e}" for e in errors)); raise SystemExit(1)
print("OFFLINE HARNESS AUDIT V1: PASS")
print("Cases:",", ".join(CASES))
print("Dispositions:",", ".join(sorted({d["expected_disposition"] for d in data.values()})))
