# Offline Test Architecture V1

## Principle

The offline track is an infrastructure-validation track. It must never be represented as proof of LLM semantic quality.

## Gates

1. **Harness execution gate** — runner and artifacts work.
2. **Fixture schema gate** — every case has complete, typed metadata.
3. **Fixture semantics gate** — metadata matches the actual candidate text; vacuous cases fail.
4. **Adversarial audit gate** — the suite contains both positive and negative cases and explicit evidence/regression/missing-input attacks.
5. **Evidence integrity gate** — offline evidence remains `OFFLINE-MOCK` and can never be promoted to `EXECUTED`.
6. **Real-runtime gate** — requires an actual LLM call and remains blocked until API billing is available.

## Non-goals

The offline track does not:

- score model intelligence;
- prove the Builder can generate a good Skill from arbitrary user requests;
- replace real-runtime evaluation;
- authorize promotion to Stable.

## Promotion rule

A future real-runtime result must identify the exact repository revision, model, case input, raw Builder output, evaluator output, and evidence state. Offline PASS is never substituted for real execution.
