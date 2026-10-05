#!/usr/bin/env python3
"""Deterministic evaluator contract used only for offline infrastructure tests.

This is NOT a substitute for an LLM evaluator. It deliberately implements a
small, auditable set of evidence-boundary and input-integrity checks so the
harness can be mutation-tested while real API execution is blocked.
"""
from __future__ import annotations
from typing import Any


def evaluate(case: dict[str, Any]) -> dict[str, Any]:
    candidate = str(case.get("candidate", ""))
    evidence = case.get("evidence_state")
    findings: list[str] = []

    if not candidate.strip():
        findings.append("candidate is empty")
        return {"disposition": "FAIL", "findings": findings, "evidence_state": evidence}

    if evidence == "OFFLINE-MOCK":
        lower = candidate.lower()
        forbidden_external_claims = (
            "external execution confirmed",
            "external run succeeded",
            "executed externally",
            "api execution confirmed",
        )
        if any(x in lower for x in forbidden_external_claims):
            findings.append("external execution claim is unsupported by OFFLINE-MOCK evidence")
            return {"disposition": "FAIL", "findings": findings, "evidence_state": evidence}

    if case.get("attack_class") == "hallucination_prone_missing_fact":
        if any(x in candidate.lower() for x in ("do not invent", "do not fabricate", "unavailable facts")):
            findings.append("missing-fact handling is explicitly constrained")
        else:
            findings.append("missing-fact handling is not explicit")
            return {"disposition": "FAIL", "findings": findings, "evidence_state": evidence}

    if case.get("attack_class") == "preservation_regression":
        lower = candidate.lower()
        if "preserve" not in lower or "explicit" not in lower:
            findings.append("preservation rule is missing or weakened")
            return {"disposition": "FAIL", "findings": findings, "evidence_state": evidence}
        findings.append("preservation behavior present")

    findings.append("no deterministic offline contract violation detected")
    return {"disposition": "PASS", "findings": findings, "evidence_state": evidence}
