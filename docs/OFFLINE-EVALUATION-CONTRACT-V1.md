# Offline Evaluation Contract V1

## Scope

This contract defines what the offline suite may and may not conclude. It is deliberately narrower than a semantic evaluation of a real LLM-produced Skill.

## Dispositions

- `PASS`: the fixture's required property is demonstrably satisfied by deterministic checks.
- `FAIL`: the fixture contains a deterministic violation that the harness is required to detect.
- `UNKNOWN`: available evidence is insufficient to decide the semantic property. `UNKNOWN` must never be silently promoted to `PASS`.

## Evidence states

- `OFFLINE-MOCK`: no external LLM execution occurred.
- `EXECUTED`: reserved for real runtime evidence. Offline fixtures must never claim this state.

## Non-claims

A passing offline audit does not prove:

- semantic quality of Builder V0.2;
- quality of an LLM-generated Skill;
- model instruction following;
- robustness against novel prompts;
- production readiness.

## Required attack families

The suite must retain coverage for:

1. missing-input/fact handling;
2. output-contract violations;
3. evidence-boundary violations;
4. regression/preservation failures;
5. UNKNOWN propagation;
6. empty or malformed candidates.

## Promotion rule

No offline PASS may promote a Builder or Skill to Stable. Real runtime evidence and separate review remain mandatory whenever the claim concerns actual model execution or semantic quality.
