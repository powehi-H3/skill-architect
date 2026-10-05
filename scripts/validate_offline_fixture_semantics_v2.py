#!/usr/bin/env python3
"""Deterministic semantic sanity gate for offline benchmark fixtures."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "benchmarks" / "fixtures" / "offline-builder-v0"
# Canonical fixtures use the full contract. D is a legacy alias and is checked separately.
CASES = ["A", "E", "F", "G", "B", "C", "D2", "H", "I", "J"]
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
    text = " ".join(d.get("candidate", "").lower().split())
    attack = d.get("attack_class", "").lower()
    disposition = d.get("expected_disposition")

    if d.get("case_id") != case:
        errors.append(f"{case}: case_id mismatch")
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
    if case == "D2" and not (disposition == "PASS" and "external execution" in text and "do not claim" in text):
        errors.append("D2: evidence-boundary positive condition is absent")
    if case == "H" and not (disposition == "FAIL" and "not executed" in text and "external execution evidence" in text):
        errors.append("H: negative evidence-boundary condition is absent")
    if case == "I" and not (disposition == "UNKNOWN" and "insufficient" in text):
        errors.append("I: UNKNOWN propagation condition is absent")
    if case == "J" and not (disposition == "FAIL" and "external model execution completed" in text):
        errors.append("J: false external-execution claim is absent")

legacy = FIX / "case-D.json"
if not legacy.exists():
    errors.append("D: legacy fixture missing")
else:
    try:
        d = json.loads(legacy.read_text(encoding="utf-8"))
        if d.get("case_id") != "D" or d.get("source") != "FIXTURE" or d.get("expected_evidence_state") != "OFFLINE-MOCK":
            errors.append("D: legacy fixture markers invalid")
    except Exception as exc:
        errors.append(f"D: invalid legacy JSON ({exc})")

if errors:
    print("OFFLINE FIXTURE SEMANTICS V3: FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("OFFLINE FIXTURE SEMANTICS V3: PASS")
print("Validated canonical cases:", ", ".join(CASES))
print("Validated legacy alias: D")
