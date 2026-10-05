#!/usr/bin/env python3
"""Mutation tests proving Builder V1 contract tests can detect regressions."""
from __future__ import annotations
import shutil, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts/build_skill_v1.py"
TEST = ROOT / "scripts/test_builder_v1.py"
FIXTURES = ROOT / "benchmarks/fixtures/builder-v1"

MUTATIONS = {
    "remove-quality-requirement": (
        'REQUIRED = ["task_id", "task", "inputs", "outcome", "quality", "failure"]',
        'REQUIRED = ["task_id", "task", "inputs", "outcome", "failure"]',
    ),
    "drop-unknown-field-rejection": (
        '    unknown = sorted(set(spec) - ALLOWED)\n    if unknown:\n        raise ValueError(f"unknown fields: {\', \'.join(unknown)}")\n',
        '',
    ),
    "drop-offline-evidence": (
        'Evidence state: OFFLINE-MOCK. This candidate has not been externally executed.',
        'Evidence state: PASS. This candidate has been externally executed.',
    ),
    "skip-failure-section": (
        '        "## Failure / Uncertainty",\n        bullets(failure),',
        '        "## Outcome",\n        spec["outcome"].strip(),',
    ),
}


def run_mutation(name, old, new):
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        scripts = root / "scripts"
        fixtures = root / "benchmarks/fixtures/builder-v1"
        scripts.mkdir(parents=True)
        fixtures.mkdir(parents=True)
        source = BUILDER.read_text(encoding="utf-8")
        if old not in source:
            return False, f"mutation anchor missing: {name}"
        (scripts / "build_skill_v1.py").write_text(source.replace(old, new, 1), encoding="utf-8")
        shutil.copy2(TEST, scripts / "test_builder_v1.py")
        for fixture in FIXTURES.glob("*.json"):
            shutil.copy2(fixture, fixtures / fixture.name)
        result = subprocess.run(["python3", str(scripts / "test_builder_v1.py")], capture_output=True, text=True)
        if result.returncode == 0:
            return False, f"mutation survived: {name}"
        return True, f"mutation killed: {name}"


def main():
    failures = []
    for name, (old, new) in MUTATIONS.items():
        ok, message = run_mutation(name, old, new)
        print(message)
        if not ok:
            failures.append(message)
    if failures:
        print("BUILDER V1 MUTATION TEST: FAIL")
        return 1
    print(f"BUILDER V1 MUTATION TEST: PASS ({len(MUTATIONS)} mutations killed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
