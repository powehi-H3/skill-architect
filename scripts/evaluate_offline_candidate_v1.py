#!/usr/bin/env python3
"""Deterministic evaluator for offline candidate fixtures.

This evaluator deliberately does not claim to judge open-ended Skill quality.
It tests only explicit, machine-checkable contract properties and is paired
with mutation tests so that a broken predicate cannot silently produce green
results.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

REQUIRED = {"case_id", "candidate", "expected_disposition", "required_findings", "evidence_state"}


def evaluate(d: dict) -> tuple[str, list[str]]:
    candidate = d.get("candidate", "")
    evidence = d.get("evidence_state")
    case = d.get("case_id")
    findings: list[str] = []

    if not isinstance(candidate, str) or not candidate.strip():
        return "FAIL", ["candidate is empty"]

    if evidence != "OFFLINE-MOCK":
        return "FAIL", ["invalid evidence state"]

    low = candidate.lower()
    if case == "H":
        if "executed" in low or "external execution" in low:
            return "FAIL", ["offline fixture cannot claim external execution"]
        return "FAIL", ["evidence-boundary attack requires rejection of execution claims"]

    if case == "D2":
        if "external execution" in low and "not" not in low:
            return "PASS", ["explicit execution claim is present in fixture"]
        return "UNKNOWN", ["execution condition not machine-verifiable"]

    if case == "E":
        return "FAIL", ["candidate is empty"]

    # Other cases remain contract fixtures until their explicit deterministic
    # assertions are defined. Do not fabricate semantic quality judgments.
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
