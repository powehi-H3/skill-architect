#!/usr/bin/env python3
"""Deterministic semantic sanity gate for offline benchmark fixtures.

This validates that the fixture metadata and its actual candidate text agree.
It is deliberately conservative: it does not attempt to judge the quality of
natural language. It only prevents vacuous or mislabeled benchmark cases.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"
CASES = ["A", "E", "F", "G", "B", "C", "D", "D2", "H"]
errors: list[str] = []

for case in CASES:
    p = FIX / f"case-{case}.json"
    if not p.exists():
        errors.append(f"{case}: missing")
        continue
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{case}: invalid JSON ({exc})")
        continue
    text = d.get("candidate", "").lower()
    attack = d.get("attack_class", "").lower()
    disposition = d.get("expected_disposition")

    if d.get("evidence_state") != "OFFLINE-MOCK":
        errors.append(f"{case}: evidence_state is not OFFLINE-MOCK")
    if disposition not in {"PASS", "FAIL", "UNKNOWN"}:
        errors.append(f"{case}: invalid expected_disposition")

    if case == "A" and not (disposition == "PASS" and "## goal" in text and text.strip()):
        errors.append("A: positive structural candidate is not encoded as declared")
    if case == "E" and not (disposition == "FAIL" and text.strip() == ""):
        errors.append("E: empty-candidate failure is not encoded as declared")
    if case == "F" and not ("missing" in attack and "do not invent" in text):
        errors.append("F: hallucination/missing-fact condition is absent")
    if case == "G" and not ("regression" in attack and "preserve" in text and "authorization" in text):
        errors.append("G: preservation/regression condition is absent")
    if case == "B" and not ("missing" in attack and "missing" in text):
        errors.append("B: missing-input condition is absent")
    if case == "C" and not ("quality" in attack and "quality" in text):
        errors.append("C: quality-gate condition is absent")
    if case == "D" and not (disposition == "PASS" and "offline-mock" in d.get("evidence_state", "").lower()):
        errors.append("D: evidence baseline condition is absent")
    if case == "D2" and not (disposition == "PASS" and "external execution" in text and "do not claim" in text):
        errors.append("D2: evidence-boundary positive condition is absent")
    if case == "H" and not (disposition == "FAIL" and "not" in text and "executed" not in text):
        errors.append("H: negative evidence-boundary condition is absent or contaminated")

if errors:
    print("OFFLINE FIXTURE SEMANTICS V2: FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("OFFLINE FIXTURE SEMANTICS V2: PASS")
print("Validated cases:", ", ".join(CASES))
