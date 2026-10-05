# Skill Architect — Project Master Specification

**Status:** REBASELINE / ACTIVE
**Purpose:** establish a verifiable completion contract for the Skill Architect project after the initial implementation exposed gaps between implementation, testing, evidence, and completion claims.

## 1. Final objective

Build a reusable, testable Skill-architecture system that can help create, evaluate, improve, and regression-test Skills without confusing documentation with execution evidence.

The project is not complete merely because SKILL.md files, scripts, or workflows exist. Completion requires evidence that the system behaves according to its declared contracts.

## 2. Non-negotiable principles

1. **Implementation is not evidence.** A file existing in GitHub is not proof that it works.
2. **Workflow success is not semantic quality.** A green CI run proves only what that workflow actually asserts.
3. **Mock evidence must never be represented as real model execution.** `OFFLINE-MOCK` and real execution remain distinct evidence states.
4. **UNKNOWN is not PASS.** Missing or unverifiable evidence must remain unknown unless a deterministic rule establishes a result.
5. **Tests must be attackable.** Mutation tests must demonstrate that meaningful test failures can actually be triggered.
6. **Regression is mandatory.** An improvement must not silently remove an existing required behavior.
7. **No completion claim without an acceptance gate.** Every milestone needs explicit pass criteria and evidence.
8. **No invented capability.** If a dependency, API, connector, or source is unavailable, record the limitation instead of simulating success.

## 3. Evidence states

- `OFFLINE-MOCK`: deterministic local fixture; no LLM execution.
- `REAL-LLM`: a real model/API call was performed and the run is traceable.
- `HUMAN-VERIFIED`: a human verified the relevant output.
- `UNKNOWN`: evidence is insufficient.

Evidence states are metadata, not quality scores.

## 4. Completion levels

### Level 0 — Repository integrity

Required:
- repository structure is coherent;
- canonical entry points are identified;
- legacy aliases are explicitly marked;
- no duplicate workflow is silently treated as authoritative.

### Level 1 — Offline evaluator integrity

Required:
- deterministic evaluator exists;
- normal, failure, missing-input, evidence-boundary, and regression cases exist;
- evaluator compares actual disposition against expected disposition;
- mutation tests prove predicates are non-vacuous;
- workflow produces inspectable evidence.

### Level 2 — Builder contract

Required:
- Builder input/output contract is explicit;
- structural validation is deterministic where possible;
- failure handling is explicit;
- evaluator distinguishes structural validity from semantic quality;
- no unsupported semantic claims are promoted to PASS.

### Level 3 — Real runtime

Required:
- real model execution is available;
- request/response evidence is retained in a safe, reproducible form;
- runtime failures are distinguishable from Builder failures;
- real execution is never inferred from a green offline run.

### Level 4 — Regression and adversarial validation

Required:
- baseline candidates exist;
- deliberate regressions are detected;
- adversarial cases cover misleading, incomplete, contradictory, and evidence-invalid outputs;
- evaluator mutation tests remain green;
- failures produce actionable evidence.

### Level 5 — Release candidate

Required:
- all lower levels pass;
- known limitations are documented;
- no unresolved critical test-system defect remains;
- release artifact and verification report are reproducible from Git history.

## 5. Current state

- GitHub repository: active.
- Offline Harness: previously demonstrated a successful deterministic run.
- OpenAI runtime: blocked by API billing status; this is an external dependency limitation, not proof of Builder failure.
- Deterministic evaluator and mutation-test work: implemented but must be executed and audited before promotion.
- Full conversational transcript backup: **not available from the GitHub connector or current Project file surface**. Existing backup summaries must not be described as a verbatim transcript.

## 6. Current next gate

Do not add more arbitrary fixtures until the evaluator suite has been executed and its results inspected.

Acceptance sequence:

1. Run evaluator suite.
2. Verify expected PASS/FAIL dispositions.
3. Run mutation suite.
4. Verify every intended mutation is rejected.
5. Inspect workflow logs/artifacts.
6. Fix any evaluator weakness.
7. Repeat until the gate is genuinely green.
8. Only then expand coverage.

## 7. Definition of done

The project is complete only when a release-candidate report can answer YES to all of the following:

- Can we state exactly what the Skill Architect is supposed to do?
- Can we distinguish documentation from actual execution?
- Can the offline evaluator detect deliberately injected failures?
- Can mutation tests demonstrate that the evaluator is not vacuous?
- Can regression tests detect loss of required behavior?
- Can we distinguish OFFLINE-MOCK from REAL-LLM evidence?
- Does UNKNOWN remain UNKNOWN instead of being promoted to PASS?
- Can a failed run be reproduced from the repository?
- Are all known limitations explicitly recorded?
- Has the final artifact passed the same acceptance gates used to evaluate it?

If any answer is NO or UNKNOWN, the project is not complete.

## 8. Operating rule for future work

Work in closed loops, not open-ended file accumulation:

`implement → run → inspect → find defect → fix → rerun → record evidence → promote`

A status update is not a completion signal. Evidence is.
