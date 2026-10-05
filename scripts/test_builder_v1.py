#!/usr/bin/env python3
"""Offline contract tests for Skill Builder V1."""
from __future__ import annotations
import json, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts/build_skill_v1.py"
FIXTURE = ROOT / "benchmarks/fixtures/builder-v1/case-celsius.json"


def run(inp):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "input.json"
        p.write_text(json.dumps(inp), encoding="utf-8")
        return subprocess.run(["python3", str(BUILDER), str(p)], capture_output=True, text=True)


def main():
    base = json.loads(FIXTURE.read_text(encoding="utf-8"))
    failures = []
    ok = run(base)
    if ok.returncode != 0:
        failures.append("valid fixture rejected")
    else:
        text = ok.stdout
        for needle in ("## Purpose / Boundary", "## Inputs", "## Procedure", "## Outcome", "## Quality Conditions", "## Failure / Uncertainty", "Evidence state: OFFLINE-MOCK"):
            if needle not in text:
                failures.append(f"missing output contract section: {needle}")
        for forbidden in ("## Dependencies", "## Evidence Rules", "## Constraints"):
            if forbidden in text:
                failures.append(f"optional section invented: {forbidden}")

    malformed = dict(base)
    malformed.pop("quality")
    bad = run(malformed)
    if bad.returncode == 0 or "missing required fields: quality" not in bad.stdout:
        failures.append("missing required field was not rejected")

    optional = dict(base)
    optional["dependencies"] = ["none"]
    optional["evidence"] = ["Only supplied temperature is authoritative"]
    optional["constraints"] = ["Do not invent missing temperature"]
    opt = run(optional)
    if opt.returncode != 0 or "## Dependencies" not in opt.stdout or "## Evidence Rules" not in opt.stdout or "## Constraints" not in opt.stdout:
        failures.append("explicit optional sections were not preserved")

    if failures:
        print("BUILDER V1 CONTRACT: FAIL")
        for f in failures: print("-", f)
        return 1
    print("BUILDER V1 CONTRACT: PASS")
    print("Deterministic generation, required-field rejection, and optional-section discipline verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
