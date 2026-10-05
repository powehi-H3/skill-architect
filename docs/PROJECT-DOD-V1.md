# Skill Architect — Definition of Done V1

This is the promotion contract. No single green workflow may override it.

## Gate 0 — Repository integrity

- Canonical Skill Builder candidate is versioned.
- Offline fixtures and audit scripts are versioned.
- Runtime configuration never contains a plaintext API key.
- Experimental artifacts are clearly labeled.

## Gate 1 — Harness validity

- Offline harness executes deterministically.
- Evidence artifact is produced.
- Audit suite contains both PASS and FAIL expectations.
- Suite contains missing-input, evidence-boundary, and regression attacks.
- Negative fixtures are semantically non-vacuous.

## Gate 2 — Builder execution

Required before any quality promotion:

- Real LLM execution completed.
- Model identifier and repository revision recorded.
- Every benchmark case has captured raw Builder output.
- Failed/blocked calls are retained as evidence.
- API billing/runtime blocks are reported as BLOCKED, never PASS.

## Gate 3 — Evaluation independence

- Builder output is frozen before evaluation.
- Evaluator input is exactly the captured candidate plus the declared evaluation context.
- Evaluator result is stored separately from Builder output.
- UNKNOWN remains UNKNOWN when evidence is insufficient.

## Gate 4 — Regression

A candidate cannot be promoted solely because it improves a new benchmark. Existing required behavior must remain intact across the regression suite.

## Gate 5 — Adversarial robustness

At minimum, test:

- underspecified request;
- contradictory requirements;
- missing facts;
- malformed input;
- excessive input;
- prompt injection inside source material;
- evidence spoofing;
- output-format attack;
- regression that removes an existing behavior.

## Gate 6 — Human promotion decision

Automation may collect and classify evidence, but promotion to Stable requires an explicit human decision after reviewing the evidence bundle.

## Status vocabulary

- `PASS`: the required evidence exists and the tested assertion passed.
- `FAIL`: the tested assertion failed.
- `UNKNOWN`: evidence is insufficient to decide.
- `BLOCKED`: execution could not occur for an external prerequisite.
- `EXPERIMENTAL`: implementation exists but has not met promotion gates.

`BLOCKED` and `UNKNOWN` must never be silently converted to `PASS`.
