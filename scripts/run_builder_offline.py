#!/usr/bin/env python3
"""Deterministic offline harness for the Skill Builder evaluation pipeline.

This does NOT execute an LLM. It consumes fixed candidate fixtures and runs the
same evidence/evaluator-contract checks that must hold before a real runtime can
be trusted. Its purpose is to validate the harness itself while API billing is
unavailable.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "offline-harness"
FIXTURES = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"

CASES = ["A", "E", "F", "G", "B", "C", "D"]
REQUIRED_FIELDS = ["case_id", "candidate", "source", "expected_evidence_state"]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    run_id = datetime.now(timezone.utc).strftime("OFFLINE-V0-%Y%m%dT%H%M%SZ")
    run_dir = OUT / run_id
    run_dir.mkdir()
    results = []

    for case in CASES:
        path = FIXTURES / f"case-{case}.json"
        if not path.exists():
            results.append({"case": case, "status": "FAIL", "reason": f"missing fixture: {path}"})
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        missing = [k for k in REQUIRED_FIELDS if k not in data]
        if missing:
            results.append({"case": case, "status": "FAIL", "reason": f"missing fields: {missing}"})
            continue
        if data["case_id"] != case:
            results.append({"case": case, "status": "FAIL", "reason": "case_id mismatch"})
            continue
        if data["expected_evidence_state"] != "OFFLINE-MOCK":
            results.append({"case": case, "status": "FAIL", "reason": "fixture must declare OFFLINE-MOCK evidence state"})
            continue
        if not isinstance(data["candidate"], str) or not data["candidate"].strip():
            results.append({"case": case, "status": "FAIL", "reason": "candidate is empty"})
            continue
        results.append({"case": case, "status": "PASS", "evidence_state": "OFFLINE-MOCK", "source": data["source"]})

    summary = {
        "run_id": run_id,
        "status": "PASS" if all(r["status"] == "PASS" for r in results) else "FAIL",
        "evidence_state": "OFFLINE-MOCK",
        "llm_executed": False,
        "cases": results,
        "purpose": "Validate offline harness/evidence plumbing; not evidence of Builder semantic quality.",
    }
    (run_dir / "SUMMARY.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    raise SystemExit(0 if summary["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
