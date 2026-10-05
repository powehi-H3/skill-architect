# Builder V0 — Case G Retest

**Status:** RETEST READY — FIXTURE ESTABLISHED / BUILDER RUNTIME LIMIT REMAINS
**Builder under test:** `docs/SKILL-BUILDER-V0.md`
**Builder baseline:** `19667fdad8edc0464ef45d7b0687210ff0cc26c5`
**Benchmark:** `benchmarks/BUILDER-BENCHMARK-V0.md`
**Fixture:** `benchmarks/fixtures/case-g-existing-skill.md`
**Harness:** `benchmarks/BUILDER-TEST-HARNESS-V0.md`
**Execution protocol:** `benchmarks/BUILDER-EXECUTION-PROTOCOL-V0.md`

## 1. Why the fixture was added

The original Case G was not executable as a controlled test because it referred to an existing Skill without supplying a fixed existing Skill artifact. Using an arbitrary Skill would have changed the test input and contaminated the result.

A fixed fixture has now been added. It is intentionally small but complete enough to test preservation.

## 2. Exact requested change

The only requested change for the candidate is:

> Change the Output Contract from a bullet list to a table.

The request does **not** authorize changes to scope, inputs, core behavior, quality criteria, failure handling, or capabilities.

## 3. Evaluation target

The candidate should preserve all unrelated behavior while changing only the requested presentation contract.

### Must preserve

- Scope and non-invention boundary.
- Input requirements.
- Decision extraction behavior.
- Action-item extraction behavior.
- Uncertainty preservation.
- Separation of factual extraction from optional wording cleanup.
- Quality criteria.
- Failure handling.
- Preservation constraint itself.

### May change

- The Output Contract's representation from bullet list to table.
- Wording strictly necessary to make that table contract coherent.

### Must not appear without authorization

- New tools.
- Memory systems.
- Automation.
- Routing.
- New extraction categories.
- New quality requirements unrelated to the format change.
- Removal of existing behavior.

## 4. Runtime evidence boundary

This fixture repair makes the case executable in principle. It does **not** create an independent Builder runtime.

Therefore a genuine Candidate output still requires an actual Builder execution. Until such an execution is captured, the retest cannot honestly be marked PASS or FAIL.

## 5. Retest gate

When a valid Builder runtime is available, execute exactly this sequence:

1. Load Builder baseline `19667fdad8edc0464ef45d7b0687210ff0cc26c5`.
2. Load the fixed fixture.
3. Supply only the authorized format-change request.
4. Capture the complete Candidate.
5. Freeze Candidate.
6. Compare Candidate against the fixture section-by-section.
7. Classify any unrelated modification as `CHANGE_DISCIPLINE`.
8. Classify unnecessary new machinery as `OVERENGINEERING`.
9. Record severity and evidence.
10. Do not modify Builder V0 based on this single case.

## 6. Current decision

**Fixture problem: RESOLVED.**

**Builder result: RUNTIME-PENDING.**

The correct next action is to perform the controlled Builder execution, not to infer a result from the fixture itself.
