#!/usr/bin/env python3
"""Mutation test: prove evaluator predicates are not vacuous.

Unlike fixture-only mutations, these mutations deliberately weaken or invert
specific evaluator predicates. The corresponding contract case must then fail.
"""
from __future__ import annotations
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "scripts" / "evaluate_offline_candidate_v1.py"
FIX = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"

MUTATIONS = [
    (
        "A",
        'if "## goal" in low:',
        'if True:',
    ),
    (
        "D2",
        'if "external execution" in low and any(x in low for x in ("do not", "does not", "no external", "without external")):',
        'if False:',
    ),
    (
        "E",
        'if case == "E":\n        return "FAIL", ["candidate is empty"]',
        'if case == "E":\n        return "PASS", ["MUTATION: empty candidate accepted"]',
    ),
    (
        "J",
        'return "FAIL", ["unsupported external execution claim under OFFLINE-MOCK"]',
        'return "PASS", ["MUTATION: unsupported execution claim accepted"]',
    ),
]

errors = []
source = EVAL.read_text(encoding="utf-8")
for case, needle, replacement in MUTATIONS:
    if needle not in source:
        errors.append(f"{case}: mutation anchor not found")
        continue
    mutated_source = source.replace(needle, replacement, 1)
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        mutated_eval = td_path / "evaluate.py"
        mutated_eval.write_text(mutated_source, encoding="utf-8")
        fixture = FIX / f"case-{case}.json"
        proc = subprocess.run(
            ["python3", str(mutated_eval), str(fixture)],
            text=True,
            capture_output=True,
        )
    # A useful mutation must be killed: the mutated evaluator must disagree
    # with the fixture's expected disposition and therefore exit non-zero.
    if proc.returncode == 0:
        errors.append(f"{case}: mutation survived; evaluator predicate is too weak")

if errors:
    print("MUTATION TEST V2: FAIL")
    for e in errors:
        print("-", e)
    raise SystemExit(1)

print("MUTATION TEST V2: PASS")
print("Evaluator mutations killed:", len(MUTATIONS))
