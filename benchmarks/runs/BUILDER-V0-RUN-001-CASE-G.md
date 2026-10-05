# Builder V0 — Case G Run Record

**Status:** BLOCKED BY BENCHMARK FIXTURE — NOT A BUILDER FAILURE
**Builder baseline:** V0
**Benchmark:** `benchmarks/BUILDER-BENCHMARK-V0.md`
**Case:** G — Localized change request
**Date:** 2026-10-05

## 1. Intended test

Case G is intended to test whether Builder makes a localized change to an already-working Skill while preserving unrelated behavior.

The supplied benchmark prompt says:

> Here is an existing Skill that already works. Change only its output so that it returns a table instead of a bullet list. Preserve its scope, inputs, core behavior, quality conditions, and failure handling unless the requested format change makes one of them genuinely inconsistent.

Expected behavior includes targeted modification, preservation of unrelated behavior, no unnecessary rewrite, and explicit identification of any genuinely affected contract element.

## 2. Execution finding

The benchmark prompt references an "existing Skill" but the V0 benchmark does not provide the actual Skill fixture.

A repository search did not locate a dedicated fixture for Case G. Without the source Skill, there is no valid way to produce or evaluate the requested localized modification.

Creating an invented source Skill would change the test. It could accidentally make the case easier or harder and would therefore contaminate the benchmark.

## 3. Evidence classification

- **Observed:** Case G has no supplied existing-Skill fixture in the benchmark artifact.
- **Observed:** No dedicated Case G fixture was found in the repository search performed for this run.
- **Unverified:** Whether Builder V0 would preserve unrelated behavior when given a real existing Skill.
- **Unverified:** Whether Builder V0 would unnecessarily rewrite the Skill.

## 4. Failure classification

Primary label: `HARNESS`

Severity: **S1 — major** for the validity of this benchmark case, because the missing fixture prevents the intended behavior from being tested.

This is **not** currently classified as a Builder failure.

## 5. Why we stop here

Do not fabricate the missing Skill.

Do not use an arbitrary existing repository Skill as a substitute.

Do not score Builder V0 on a different task and call it Case G.

Do not modify Builder V0 to compensate for a benchmark defect.

## 6. Required correction

Add a stable fixture such as:

`benchmarks/fixtures/case-g-existing-skill.md`

The fixture should be intentionally small but contain enough independent behavior to detect destructive rewriting, for example:

- a narrow scope;
- at least two input requirements;
- a core transformation;
- at least one quality condition;
- explicit missing-input behavior;
- bullet-list output contract.

The benchmark should then provide that fixture to Builder as part of Case G input while keeping the preservation requirements outside the Builder's hidden evaluation rubric.

## 7. Regression implication

After the fixture is added, Case G must be rerun against the unchanged Builder V0 baseline before any Builder modification is proposed.

## 8. Decision

**Do not patch Builder V0.**

The correct action is to repair the benchmark fixture, record the benchmark revision, then rerun Case G.
