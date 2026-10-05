#!/usr/bin/env python3
"""Mutation test: prove evaluator predicates are not vacuous."""
from __future__ import annotations
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "scripts" / "evaluate_offline_candidate_v1.py"
FIX = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"

# Each mutation intentionally changes a fixture into a state that should flip
# its expected disposition. A surviving mutation means the evaluator failed
# to detect a deliberately injected defect.
MUTATIONS = [
    ("A", lambda d: {**d, "candidate": "# Offline candidate A\n\nNo goal section here."}),
    ("D2", lambda d: {**d, "candidate": "External execution completed successfully."}),
    ("E", lambda d: {**d, "candidate": "non-empty candidate"}),
    ("J", lambda d: {**d, "candidate": "The external execution was completed successfully."}),
]

errors = []
for case, mutate in MUTATIONS:
    original = json.loads((FIX / f"case-{case}.json").read_text(encoding="utf-8"))
    mutated = mutate(original)
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / f"case-{case}.json"
        p.write_text(json.dumps(mutated, ensure_ascii=False), encoding="utf-8")
        proc = subprocess.run(["python3", str(EVAL), str(p)], text=True, capture_output=True)
    if proc.returncode == 0:
        errors.append(f"{case}: mutation survived; evaluator predicate is too weak")

if errors:
    print("MUTATION TEST V1: FAIL")
    for e in errors:
        print("-", e)
    raise SystemExit(1)

print("MUTATION TEST V1: PASS")
print("Mutations rejected:", len(MUTATIONS))
