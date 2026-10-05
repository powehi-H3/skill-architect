#!/usr/bin/env python3
"""Exercise the Builder V1 -> Evaluator V1 offline integration path."""
from __future__ import annotations
import json, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts/build_skill_v1.py"
EVALUATOR = ROOT / "scripts/evaluate_offline_candidate_v1.py"
FIXTURE = ROOT / "benchmarks/fixtures/builder-v1/case-celsius.json"

with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    source = td / "source.json"
    source.write_text(FIXTURE.read_text(encoding="utf-8"), encoding="utf-8")
    built = subprocess.run(["python3", str(BUILDER), str(source)], capture_output=True, text=True)
    if built.returncode != 0:
        print("BUILDER -> EVALUATOR: FAIL")
        print("Builder rejected canonical fixture")
        raise SystemExit(1)

    candidate = built.stdout
    # V1 adapter maps the Builder's declared purpose into the evaluator's
    # minimal Goal contract. It does not add execution evidence.
    purpose = candidate.split("## Purpose / Boundary", 1)[1].split("## Inputs", 1)[0].strip()
    adapted = "## Goal\n" + purpose + "\n\n" + candidate
    eval_case = {
        "case_id": "A",
        "candidate": adapted,
        "expected_disposition": "PASS",
        "required_findings": ["candidate is non-empty", "candidate contains a minimal goal section"],
        "evidence_state": "OFFLINE-MOCK",
    }
    evaluation = td / "evaluation.json"
    evaluation.write_text(json.dumps(eval_case), encoding="utf-8")
    checked = subprocess.run(["python3", str(EVALUATOR), str(evaluation)], capture_output=True, text=True)

    if checked.returncode != 0:
        print("BUILDER -> EVALUATOR: FAIL")
        print(checked.stdout)
        raise SystemExit(1)

print("BUILDER -> EVALUATOR: PASS")
print("Builder output was produced, adapted without execution claims, and accepted by the independent evaluator.")
