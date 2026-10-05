# Offline Harness Audit V0

## Purpose

The successful Offline Harness run proves only that deterministic fixtures, the runner, and artifact upload execute successfully. It does **not** establish semantic quality of Skill Builder V0.2.

This audit defines the next offline gate: test whether the harness can distinguish good, bad, incomplete, misleading, and evidence-invalid candidates.

## Threat model

A weak harness can report PASS when:

1. a candidate is merely non-empty;
2. required headings exist but instructions are contradictory;
3. failure handling is absent or unsafe;
4. examples contradict the stated quality standard;
5. the candidate claims execution evidence it never received;
6. a regression fixture is silently ignored;
7. evaluator output is malformed but still accepted;
8. all fixtures are happy-path and never exercise adversarial behavior.

## Offline gate

The next harness must include deterministic fixtures for:

- structurally valid candidate;
- empty/minimal candidate;
- contradictory quality requirements;
- hallucination-prone missing-input case;
- output-format violation;
- unsafe automatic-claim/evidence-boundary violation;
- regression candidate that is superficially better but removes a required behavior;
- evaluator result with UNKNOWN evidence state.

## Required assertion style

A fixture passes only when the harness detects the property it was designed to test. A green workflow with fixtures that cannot fail is not evidence of evaluator quality.

Each fixture must declare:

- `case_id`
- `attack_class`
- `candidate`
- `expected_disposition`
- `required_findings`
- `evidence_state`

## Promotion boundary

This audit is itself an infrastructure test. It cannot promote Builder V0.2. Promotion still requires real LLM execution plus independent review of evidence.
