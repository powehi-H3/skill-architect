#!/usr/bin/env python3
"""Validate the offline Reviewer blind-test materials without executing a model."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "benchmarks" / "reviewer" / "fixtures" / "case-001.md"
PROMPT = ROOT / "benchmarks" / "reviewer" / "BLIND-PROMPT-001.md"

FORBIDDEN = [
    "seeded defect",
    "exact defect",
    "hidden defect",
    "defect category",
    "expected verdict",
    "NEEDS REVISION because",
    "FAIL because",
]


def die(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if FIXTURE.name != "case-001.md":
        die("Fixture filename is not neutral.")

    fixture = FIXTURE.read_text(encoding="utf-8")
    prompt = PROMPT.read_text(encoding="utf-8")

    if "name:" not in fixture or "description:" not in fixture:
        die("Fixture lacks basic Skill frontmatter.")
    if "# Purpose" not in fixture or "# Workflow" not in fixture or "# Constraints" not in fixture:
        die("Fixture is not structurally realistic enough for a blind review.")
    if "# Failure handling" not in fixture or "# Example" not in fixture:
        die("Fixture does not exercise the intended review surfaces.")

    lower_prompt = prompt.lower()
    for token in FORBIDDEN:
        if token.lower() in lower_prompt:
            die(f"Blind prompt leaks benchmark information: {token}")

    if re.search(r"case[-_ ]?001", lower_prompt):
        die("Blind prompt leaks the fixture identifier.")

    print("PASS: Reviewer blind-test pack is structurally valid and does not expose the seeded defect category.")
    print("EVIDENCE: offline material validation only; no Reviewer model execution was performed.")


if __name__ == "__main__":
    main()
