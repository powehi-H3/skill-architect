#!/usr/bin/env python3
"""Mutation test: prove evaluator predicates are not vacuous."""
from __future__ import annotations
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "scripts" / "evaluate_offline_candidate_v1.py"
FIX = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"

# Each mutation deliberately changes a correct evaluator rule into an incorrect
# one. The corresponding contract fixture must then be rejected.
MUTATIONS = [
    ("A", 'if "## goal" in low:', "if False:"),
    (
        "D2",
        'if "external execution" in low and any(x in low for x in ("do not", "does not", "no external", "without external")):',
        "if False:",
    ),
    (
        "E",
        'return "FAIL", ["candidate is empty"]',
        'return "PASS", ["MUTATION: empty candidate accepted"]',
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
        mutated_eval = Path(td) / "evaluate.py"
        mutated_eval.write_text(mutated_source, encoding="utf-8")
        fixture = FIX / f"case-{case}.json"
        proc = subprocess.run(
            ["python3", str(mutated_eval), str(fixture)],
            text=True,
            capture_output=True,
        )
    if proc.returncode == 0:
        errors.append(f"{case}: mutation survived; evaluator predicate is too weak")

if errors:
    print("MUTATION TEST V3: FAIL")
    for e in errors:
        print("-", e)
    raise SystemExit(1)

print("MUTATION TEST V3: PASS")
print("Evaluator mutations killed:", len(MUTATIONS))
