# Skill Architect — Skill Lifecycle V0.2

**Status:** DESIGN BASELINE
**Parent:** `docs/ARCHITECTURE-V0.md`
**Contract:** `contracts/SKILL-CONTRACT-V0.1.md`

## 1. Purpose

This document defines the lifecycle states of a Skill, permitted transitions, promotion evidence, and conditions for rollback or retirement.

The lifecycle is evidence-driven. Documentation alone cannot promote a Skill to `STABLE`.

## 2. State model

```text
DRAFT → EXPERIMENTAL → TESTING → REVIEW → REGRESSION → STABLE
                                      ↑                    │
                                      └── ITERATE ←────────┘

Any active state may move toward DEPRECATED → RETIRED.
```

A transition must be explicit. An AI must not silently treat draft or experimental behavior as stable.

## 3. DRAFT

The Skill is being designed and its contract or architecture is incomplete or changing.

Allowed activity: define scope, analyze inputs/outputs, gather references, draft procedures, create initial tests.

Promotion to `EXPERIMENTAL` requires:
- identity and trigger boundary;
- purpose and non-goals;
- preliminary input/output contracts;
- initial failure handling;
- an executable or reviewable Skill artifact.

Draft behavior must not be presented as validated behavior.

## 4. EXPERIMENTAL

A runnable or otherwise testable Skill exists, but evidence is insufficient for reliability claims.

Required records: version, assumptions, initial test plan, known limitations.

Promotion to `TESTING` occurs when the Skill is ready for structured evaluation.

## 5. TESTING

The Skill is under structured evaluation.

Minimum evaluation:
- Normal test;
- Edge test;
- Stress test.

Regression tests are required after meaningful revisions and before stable promotion when applicable.

Each test result should separate:
1. observed output;
2. expected behavior;
3. pass/fail judgment;
4. failure classification;
5. suspected root cause;
6. proposed change.

A failed test does not automatically justify a broad rewrite. Target the smallest demonstrated failure mechanism.

Promotion to `REVIEW` occurs when sufficient planned evidence exists for a review decision.

## 6. REVIEW

A reviewer evaluates whether evidence supports the Skill's claims and whether failures are properly handled.

Review checks:
- scope and trigger are usable;
- requirements are covered;
- output contract is satisfied;
- quality criteria are meaningful;
- failure handling is safe;
- test evidence is credible;
- external knowledge has not been promoted without justification;
- no duplicated authoritative rule source exists;
- unresolved critical failures are disclosed.

Outcomes:
- `REVIEW → REGRESSION` when ready for compatibility testing;
- `REVIEW → EXPERIMENTAL` when changes are required;
- `REVIEW → DEPRECATED` when the design should no longer be used.

## 7. REGRESSION

A revised Skill is checked against previously passing behavior and important known failure cases.

A fix for one failure must not silently reintroduce a previously fixed failure.

Promotion to `STABLE` requires relevant regression tests to pass, known limitations to be documented, no hidden critical defect, contract compliance, and updated version/status metadata.

If regression fails, return to `EXPERIMENTAL` or `TESTING` according to the failure.

## 8. STABLE

The Skill has sufficient evidence for normal use within its declared boundary.

`STABLE` does not mean perfect, universal, or permanently frozen.

Stable obligations:
- preserve the declared contract;
- maintain version history;
- retain relevant regression cases;
- record meaningful changes;
- re-enter the lifecycle for material behavior changes.

## 9. ITERATE

`STABLE → ITERATE` is a conceptual maintenance event rather than a required persistent state. A material improvement or defect fix creates a new candidate version that enters `EXPERIMENTAL` while the previous stable version remains recoverable.

## 10. DEPRECATED

The Skill remains identifiable for compatibility or migration but should no longer be selected for new work.

Possible reasons: superseded implementation, obsolete assumptions, unsafe/unreliable behavior, incompatible dependencies, or replacement by a better Skill.

A deprecated Skill should point to its replacement when one exists.

## 11. RETIRED

The Skill is no longer an active execution candidate. Historical metadata and the reason for retirement should remain recoverable.

## 12. Transition authority

The system distinguishes:
- **Builder:** creates or modifies a candidate;
- **Tester:** produces test evidence;
- **Reviewer:** evaluates evidence and recommends promotion/rejection;
- **Registry:** records authoritative status;
- **User/project owner:** may approve high-impact promotion where required.

No generation step may self-certify its output as `STABLE` without the required evaluation evidence.

## 13. Version rule

A material behavior change creates a new candidate version. The previous stable version remains recoverable until the candidate is accepted.

Documentation-only changes may not require a behavioral version bump, but must be recorded when they affect interpretation or execution.

## 14. Minimum promotion gate

Before `STABLE`:

- [ ] Trigger boundary works.
- [ ] Input contract works.
- [ ] Execution procedure is sufficiently reproducible.
- [ ] Output contract passes.
- [ ] Quality criteria pass.
- [ ] Failure handling does not fabricate missing facts.
- [ ] Normal test passes.
- [ ] Edge test passes or limitations are explicitly accepted.
- [ ] Stress test passes or limitations are explicitly accepted.
- [ ] Relevant regression tests pass.
- [ ] Known failures are recorded.
- [ ] Version and provenance are recorded.

## 15. V0.2 boundary

This is a design baseline, not a fully automated state machine. Exact quantitative thresholds, scoring, quorum rules, and automated promotion are deferred until real Skill test data exists.
