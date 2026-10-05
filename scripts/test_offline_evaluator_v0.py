#!/usr/bin/env python3
"""Mutation tests for the deterministic offline evaluator contract."""
from __future__ import annotations
from copy import deepcopy
from offline_evaluator_v0 import evaluate

BASE = {
    "case_id": "X",
    "candidate": "Preserve explicit existing material. Do not invent unavailable facts.",
    "attack_class": "positive_structural_candidate",
    "expected_disposition": "PASS",
    "evidence_state": "OFFLINE-MOCK",
}


def assert_case(label: str, case: dict, expected: str) -> None:
    actual = evaluate(case)["disposition"]
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected}, got {actual}")


def main() -> None:
    assert_case("normal", BASE, "PASS")

    empty = deepcopy(BASE)
    empty["candidate"] = ""
    assert_case("empty", empty, "FAIL")

    unsupported = deepcopy(BASE)
    unsupported["candidate"] = "External execution confirmed; all tests passed."
    assert_case("unsupported external claim", unsupported, "FAIL")

    regression = deepcopy(BASE)
    regression["attack_class"] = "preservation_regression"
    regression["candidate"] = "Rewrite everything freely."
    assert_case("regression", regression, "FAIL")

    missing_fact = deepcopy(BASE)
    missing_fact["attack_class"] = "hallucination_prone_missing_fact"
    missing_fact["candidate"] = "When facts are unavailable, do not invent them."
    assert_case("missing fact safe", missing_fact, "PASS")

    missing_fact_bad = deepcopy(missing_fact)
    missing_fact_bad["candidate"] = "Fill in any missing facts from context."
    assert_case("missing fact unsafe", missing_fact_bad, "FAIL")

    print("OFFLINE EVALUATOR MUTATION TEST: PASS")


if __name__ == "__main__":
    main()
