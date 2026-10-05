#!/usr/bin/env python3
"""Run the deterministic offline contract suite, including adversarial cases.

This suite validates the harness/evidence contract only. It does not execute an LLM
and must never be interpreted as semantic quality evidence for Skill Builder.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"
CASES = ["A", "E", "F", "G", "B", "C", "D", "D2", "H"]
REQUIRED = ["case_id", "attack_class", "candidate", "expected_disposition", "required_findings", "evidence_state"]


def load(case: str) -> dict:
    return json.loads((FIX / f"case-{case}.json").read_text(encoding="utf-8"))


def check(case: str, d: dict) -> tuple[bool, str]:
    missing = [k for k in REQUIRED if k not in d]
    if missing:
        return False, f"missing fields: {missing}"
    if d["case_id"] != case:
        return False, "case_id mismatch"
    if d["evidence_state"] != "OFFLINE-MOCK":
        return False, "evidence_state is not OFFLINE-MOCK"
    if d["expected_disposition"] not in {"PASS", "FAIL", "UNKNOWN"}:
        return False, "invalid expected disposition"
    if not isinstance(d["required_findings"], list) or not d["required_findings"]:
        return False, "required_findings empty"
    if not isinstance(d["candidate"], str):
        return False, "candidate is not string"
    if case == "E" and (d["expected_disposition"] != "FAIL" or d["candidate"].strip()):
        return False, "E must be an empty-candidate FAIL fixture"
    if case == "H" and (d["expected_disposition"] != "FAIL" or "not executed" not in d["candidate"].lower()):
        return False, "H must encode the offline evidence boundary attack"
    if case == "D2" and (d["expected_disposition"] != "PASS" or "external execution" not in d["candidate"].lower()):
        return False, "D2 must encode the non-claiming evidence-boundary PASS case"
    return True, "ok"


def main() -> int:
    results = []
    for case in CASES:
        path = FIX / f"case-{case}.json"
        if not path.exists():
            results.append({"case": case, "status": "FAIL", "reason": "missing fixture"})
            continue
        try:
            ok, reason = check(case, load(case))
        except Exception as exc:
            ok, reason = False, f"invalid fixture: {exc}"
        results.append({"case": case, "status": "PASS" if ok else "FAIL", "reason": reason})
    summary = {
        "suite": "offline-contract-v1",
        "status": "PASS" if all(x["status"] == "PASS" for x in results) else "FAIL",
        "llm_executed": False,
        "evidence_state": "OFFLINE-MOCK",
        "semantic_quality_proven": False,
        "cases": results,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
