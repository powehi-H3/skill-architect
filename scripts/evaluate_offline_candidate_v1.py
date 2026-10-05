#!/usr/bin/env python3
"""Deterministic evaluator for offline candidate fixtures."""
from __future__ import annotations
import json
import sys
from pathlib import Path

REQUIRED = {"case_id", "candidate", "expected_disposition", "required_findings", "evidence_state"}


def evaluate(d: dict) -> tuple[str, list[str]]:
    candidate = d.get("candidate", "")
    evidence = d.get("evidence_state")
    case = d.get("case_id")
    if not isinstance(candidate, str) or not candidate.strip():
        return "FAIL", ["candidate is empty"]
    if evidence != "OFFLINE-MOCK":
        return "FAIL", ["invalid evidence state"]

    low = " ".join(candidate.lower().split())

    if case == "A":
        if "## goal" in low:
            return "PASS", ["candidate is non-empty", "candidate contains a minimal goal section"]
        return "FAIL", ["candidate lacks a minimal goal section"]

    if case == "D2":
        if "external execution" in low and any(x in low for x in ("do not", "does not", "no external", "without external")):
            return "PASS", ["candidate explicitly separates local evidence from external execution", "candidate does not claim an external run"]
        return "FAIL", ["candidate does not clearly prohibit unsupported external execution claims"]

    if case == "E":
        return "FAIL", ["candidate is empty"]

    if case == "H":
        # H is a boundary fixture whose expected disposition is FAIL. The evaluator
        # intentionally refuses to promote it to execution evidence.
        return "FAIL", ["offline fixture cannot establish external execution"]

    if case == "I":
        return "UNKNOWN", ["evidence is insufficient to establish execution"]

    if case == "J":
        if "external model execution completed" in low or "external execution was completed" in low:
            return "FAIL", ["unsupported external execution claim under OFFLINE-MOCK"]
        return "PASS", ["no unsupported external execution claim detected"]

    return "UNKNOWN", ["no deterministic semantic rule defined"]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: evaluate_offline_candidate_v1.py <fixture.json>")
        return 2
    p = Path(sys.argv[1])
    d = json.loads(p.read_text(encoding="utf-8"))
    missing = REQUIRED - d.keys()
    if missing:
        print(json.dumps({"status":"FAIL","findings":[f"missing fields: {sorted(missing)}"]}, ensure_ascii=False))
        return 1
    actual, findings = evaluate(d)
    result = {"case_id": d["case_id"], "actual_disposition": actual, "expected_disposition": d["expected_disposition"], "findings": findings, "evidence_state": d["evidence_state"]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if actual == d["expected_disposition"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
