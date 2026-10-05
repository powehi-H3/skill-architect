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

MUTATIONS = [
    ("E", lambda d: {**d, "candidate": "non-empty candidate"}),
    ("H", lambda d: {**d, "candidate": "The external execution was completed successfully."}),
    ("D2", lambda d: {**d, "candidate": "No external execution evidence is present."}),
]

errors = []
for case, mutate in MUTATIONS:
    original = json.loads((FIX / f"case-{case}.json").read_text(encoding="utf-8"))
    mutated = mutate(original)
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / f"case-{case}.json"
        p.write_text(json.dumps(mutated, ensure_ascii=False), encoding="utf-8")
        proc = subprocess.run(["python3", str(EVAL), str(p)], text=True, capture_output=True)
    # A mutation test succeeds only if the mutation is rejected by the evaluator.
    if proc.returncode == 0:
        errors.append(f"{case}: mutation survived; evaluator predicate is too weak")

if errors:
    print("MUTATION TEST V1: FAIL")
    for e in errors:
        print("-", e)
    raise SystemExit(1)

print("MUTATION TEST V1: PASS")
print("Mutations rejected:", len(MUTATIONS))
