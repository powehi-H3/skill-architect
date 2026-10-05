#!/usr/bin/env python3
"""Run deterministic evaluator cases and mutation tests as one local gate."""
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "benchmarks/fixtures/offline-builder-v0"
EVAL = ROOT / "scripts/evaluate_offline_candidate_v1.py"
MUT = ROOT / "scripts/mutation_test_offline_v1.py"
CASES = ["A", "D2", "E", "H", "I", "J"]

failed=[]
for c in CASES:
    p=subprocess.run(["python3",str(EVAL),str(FIX/f"case-{c}.json")],capture_output=True,text=True)
    print(p.stdout,end="")
    try:
        result=json.loads(p.stdout)
    except json.JSONDecodeError:
        failed.append(f"{c}: invalid evaluator output")
        continue
    if p.returncode != 0 and result.get("actual_disposition") != result.get("expected_disposition"):
        failed.append(c)
    # UNKNOWN is a valid evaluator result only when it is explicitly expected;
    # it is never promoted to PASS by this suite.
    if result.get("actual_disposition") == "UNKNOWN" and result.get("expected_disposition") != "UNKNOWN":
        failed.append(f"{c}: UNKNOWN mismatch")

m=subprocess.run(["python3",str(MUT)],capture_output=True,text=True)
print(m.stdout,end="")
if m.returncode != 0: failed.append("MUTATION")

if failed:
    print(json.dumps({"status":"FAIL","failed":failed}))
    sys.exit(1)
print(json.dumps({"status":"PASS","cases":CASES,"unknown_non_promotable":True,"mutation_test":"PASS"}))
