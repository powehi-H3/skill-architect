# Skill Architect — Skill Lifecycle V0.2

**Status:** DESIGN BASELINE
**Parent:** `docs/ARCHITECTURE-V0.md`
**Contract:** `contracts/SKILL-CONTRACT-V0.1.md`

## 1. Purpose

This document defines lifecycle states, permitted transitions, promotion evidence, and conditions for rollback or retirement.

The lifecycle is evidence-driven. Documentation alone cannot promote a Skill to `STABLE`.

## 2. State model

```text
DRAFT → EXPERIMENTAL → TESTING → REVIEW → REGRESSION → STABLE
                                           ↑                 │
                                           └── new candidate ─┘

Any active state may move toward DEPRECATED → RETIRED.
```

A transition must be explicit. An AI must not silently treat draft or experimental behavior as stable.

## 3. DRAFT

The Skill is being designed and its contract or architecture is incomplete or changing.

Allowed activity: define scope, analyze inputs/outputs, gather references, draft procedures, create initial evaluation cases.

Promotion to `EXPERIMENTAL` requires enough definition for the Skill to be meaningfully tried, including its purpose, boundary, expected inputs/outputs, and initial failure handling appropriate to the task.

Draft behavior must not be presented as validated behavior.

## 4. EXPERIMENTAL

A runnable or otherwise testable Skill exists, but evidence is insufficient for reliability claims.

Required records should include version, assumptions, evaluation plan, and known limitations appropriate to the task.

Promotion to `TESTING` occurs when the Skill is ready for structured evaluation.

## 5. TESTING

The Skill is under structured evaluation.

The evaluation suite should be appropriate to the Skill's behavior and risk. Common cases include Normal, Edge, Stress, and Regression tests; not every Skill requires identical cases.

Each test result should separate:
1. observed output;
2. expected behavior;
3. pass/fail or graded judgment;
4. failure classification where applicable;
5. suspected root cause;
6. proposed change.

A failed test does not automatically justify a broad rewrite. Target the smallest justified change when the evidence supports a localized cause.

Promotion to `REVIEW` occurs when sufficient planned evidence exists for a review decision.

## 6. REVIEW

A reviewer evaluates whether evidence supports the Skill's claims and whether failures are properly handled.

Review checks should include, as relevant:
- scope and trigger are usable;
- requirements are covered;
- output contract is satisfied;
- quality criteria are meaningful;
- failure handling is appropriate;
- test evidence is credible;
- external knowledge has not been promoted without justification;
- conflicting authoritative definitions are absent;
- unresolved important failures are disclosed.

Outcomes:
- `REVIEW → REGRESSION` when ready for compatibility testing;
- `REVIEW → EXPERIMENTAL` when changes are required;
- `REVIEW → DEPRECATED` when the design should no longer be used.

## 7. REGRESSION

A revised Skill is checked against previously important behavior and known failure cases that should remain fixed.

A fix for one failure should not silently reintroduce a previously fixed failure.

Promotion to `STABLE` requires sufficient relevant regression evidence, documented limitations, contract compliance, and updated version/status metadata.

If regression fails, return to `EXPERIMENTAL` or `TESTING` according to the failure.

## 8. STABLE

The Skill has sufficient evidence for normal use within its declared boundary.

`STABLE` does not mean perfect, universal, or permanently frozen.

Stable obligations:
- preserve the declared contract;
- maintain version history;
- retain relevant evaluation evidence;
- record meaningful changes;
- re-enter the lifecycle for material behavior changes.

## 9. New candidate from STABLE

A material improvement or defect fix creates a new candidate version that enters `EXPERIMENTAL` while the previous stable version remains recoverable.

The previous stable version must not be overwritten merely because a candidate exists.

## 10. DEPRECATED

The Skill remains identifiable for compatibility or migration but should no longer be selected for new work.

Possible reasons: superseded implementation, obsolete assumptions, unsafe/unreliable behavior, incompatible dependencies, or replacement by a better Skill.

A deprecated Skill should point to its replacement when one exists.

## 11. RETIRED

The Skill is no longer an active execution candidate. Historical metadata and the reason for retirement should remain recoverable.

## 12. Transition authority

The system distinguishes:
- **Builder:** creates or modifies a candidate;
- **Tester:** produces evaluation evidence;
- **Reviewer:** evaluates evidence and recommends promotion/rejection;
- **Registry:** records authoritative status;
- **User/project owner:** may approve high-impact promotion where required.

No generation step may self-certify its output as `STABLE` without the required evaluation evidence.

## 13. Version rule

A material behavior change creates a new candidate version. The previous stable version remains recoverable until the candidate is accepted.

Documentation-only changes may not require a behavioral version bump, but must be recorded when they affect interpretation or execution.

## 14. Promotion gate

Before `STABLE`, confirm that the evidence appropriate to this Skill supports:

- [ ] Trigger boundary works.
- [ ] Required input handling works.
- [ ] Execution is sufficiently reproducible for the claimed use.
- [ ] Output contract is satisfied.
- [ ] Quality criteria are supported.
- [ ] Failure handling is appropriate.
- [ ] Relevant evaluation cases have passed or accepted limitations are recorded.
- [ ] Relevant regression checks pass after meaningful changes.
- [ ] Known failures and limitations are recorded.
- [ ] Version and provenance are recorded.

There is intentionally no universal numeric score or mandatory test count in V0.2. Those rules must be derived from evidence and Skill class rather than copied from a single domain.

## 15. V0.2 boundary

This is a design baseline, not a fully automated state machine. Exact scoring, quorum rules, automated promotion, and class-specific gates are deferred until the system is tested on multiple unrelated Skills.
