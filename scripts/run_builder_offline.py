#!/usr/bin/env python3
"""Deterministic offline harness for the canonical Skill Builder fixture pipeline.

This does NOT execute an LLM. It validates offline evidence plumbing against
the current canonical fixture schema and preserves the legacy D alias.
It is not evidence of Builder semantic quality.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "offline-harness"
FIXTURES = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"

CANONICAL_CASES = ["A", "E", "F", "G", "B", "C", "D2", "H", "I", "J"]
LEGACY_CASE = "D"
REQUIRED_FIELDS = ["case_id", "candidate", "expected_disposition", "evidence_state"]
ALLOWED_DISPOSITIONS = {"PASS", "FAIL", "UNKNOWN"}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    run_id = datetime.now(timezone.utc).strftime("OFFLINE-V1-%Y%m%dT%H%M%SZ")
    run_dir = OUT / run_id
    run_dir.mkdir()
    results = []

    for case in CANONICAL_CASES:
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
        if data["evidence_state"] != "OFFLINE-MOCK":
            results.append({"case": case, "status": "FAIL", "reason": "fixture must declare OFFLINE-MOCK evidence state"})
            continue
        if data["expected_disposition"] not in ALLOWED_DISPOSITIONS:
            results.append({"case": case, "status": "FAIL", "reason": "invalid expected disposition"})
            continue
        if not isinstance(data["candidate"], str):
            results.append({"case": case, "status": "FAIL", "reason": "candidate must be a string"})
            continue

        results.append({
            "case": case,
            "status": "PASS",
            "evidence_state": "OFFLINE-MOCK",
            "expected_disposition": data["expected_disposition"],
        })

    legacy_path = FIXTURES / f"case-{LEGACY_CASE}.json"
    if not legacy_path.exists():
        results.append({"case": LEGACY_CASE, "status": "FAIL", "reason": f"missing legacy fixture: {legacy_path}"})
    else:
        legacy = json.loads(legacy_path.read_text(encoding="utf-8"))
        if (
            legacy.get("case_id") != LEGACY_CASE
            or legacy.get("source") != "FIXTURE"
            or legacy.get("expected_evidence_state") != "OFFLINE-MOCK"
        ):
            results.append({"case": LEGACY_CASE, "status": "FAIL", "reason": "legacy fixture markers invalid"})
        else:
            results.append({
                "case": LEGACY_CASE,
                "status": "PASS",
                "evidence_state": "OFFLINE-MOCK",
                "legacy": True,
            })

    summary = {
        "run_id": run_id,
        "status": "PASS" if all(r["status"] == "PASS" for r in results) else "FAIL",
        "evidence_state": "OFFLINE-MOCK",
        "llm_executed": False,
        "cases": results,
        "canonical_cases": CANONICAL_CASES,
        "legacy_case": LEGACY_CASE,
        "purpose": "Validate offline harness/evidence plumbing; not evidence of Builder semantic quality.",
    }
    (run_dir / "SUMMARY.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    raise SystemExit(0 if summary["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
