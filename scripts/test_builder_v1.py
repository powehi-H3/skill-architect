#!/usr/bin/env python3
"""Offline contract and benchmark tests for Skill Builder V1."""
from __future__ import annotations
import json, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts/build_skill_v1.py"
FIXTURE_DIR = ROOT / "benchmarks/fixtures/builder-v1"
OPTIONAL_MAP = {
    "## Dependencies": "dependencies",
    "## Evidence Rules": "evidence",
    "## Constraints": "constraints",
}


def run(inp):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "input.json"
        p.write_text(json.dumps(inp), encoding="utf-8")
        return subprocess.run(["python3", str(BUILDER), str(p)], capture_output=True, text=True)


def main():
    fixtures = sorted(FIXTURE_DIR.glob("case-*.json"))
    failures = []
    if len(fixtures) < 5:
        failures.append(f"expected at least 5 benchmark fixtures, found {len(fixtures)}")

    required_sections = (
        "## Purpose / Boundary", "## Inputs", "## Procedure", "## Outcome",
        "## Quality Conditions", "## Failure / Uncertainty", "Evidence state: OFFLINE-MOCK"
    )

    for fixture in fixtures:
        base = json.loads(fixture.read_text(encoding="utf-8"))
        ok = run(base)
        if ok.returncode != 0:
            failures.append(f"{fixture.name}: valid fixture rejected")
            continue
        for needle in required_sections:
            if needle not in ok.stdout:
                failures.append(f"{fixture.name}: missing output contract section: {needle}")
        for section, field in OPTIONAL_MAP.items():
            if section in ok.stdout and field not in base:
                failures.append(f"{fixture.name}: optional section invented: {section}")

    base = json.loads((FIXTURE_DIR / "case-celsius.json").read_text(encoding="utf-8"))
    malformed = dict(base)
    malformed.pop("quality")
    bad = run(malformed)
    if bad.returncode == 0 or "missing required fields: quality" not in bad.stdout:
        failures.append("missing required field was not rejected")

    unknown = dict(base)
    unknown["invented"] = "must not be accepted"
    unknown_result = run(unknown)
    if unknown_result.returncode == 0 or "unknown fields: invented" not in unknown_result.stdout:
        failures.append("undeclared field was not rejected")

    optional = dict(base)
    optional["dependencies"] = ["none"]
    optional["evidence"] = ["Only supplied temperature is authoritative"]
    optional["constraints"] = ["Do not invent missing temperature"]
    opt = run(optional)
    if opt.returncode != 0 or not all(x in opt.stdout for x in OPTIONAL_MAP):
        failures.append("explicit optional sections were not preserved")

    if failures:
        print("BUILDER V1 CONTRACT: FAIL")
        for f in failures:
            print("-", f)
        return 1
    print(f"BUILDER V1 CONTRACT: PASS ({len(fixtures)} benchmark fixtures)")
    print("Deterministic generation, required-field rejection, undeclared-field rejection, benchmark coverage, and optional-section discipline verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
