# Builder V0.2 — Static Regression Audit 001

**Candidate:** `docs/SKILL-BUILDER-V0.2-CANDIDATE.md`
**Candidate SHA:** `7e2a29ed8fe07f62553f17c9036366786aae3e72`
**Evidence mode:** repository artifact audit / manual contract simulation
**Runtime independence:** LIMITED
**Important:** This record is NOT a runtime execution of V0.2. Existing A–G/P/R/AP artifacts were produced against earlier Builder versions. This audit checks whether V0.2's written contract addresses their documented invariants. It must not be labeled as a successful V0.2 runtime regression run.

## A–G contract audit

| Case | V0.2 contract coverage | Static result |
|---|---|---|
| A — deterministic task | Minimal candidate, observable success, non-fabrication, proportionality retained | PASS* |
| B — writing transformation | Semantic contract preservation and no unsupported additions retained | PASS* |
| C — tool-dependent analysis | Evidence honesty and capability boundary explicitly retained | PASS* |
| D — multi-step transformation | Minimal architecture and fact/inference separation retained | PASS* |
| E — ambiguous scope | Source/task filtering plus explicit uncertainty/clarification behavior retained from V0.1 | PASS* |
| F — external Skill as evidence | Authority/source classification is materially strengthened | PASS* |
| G — localized change | TARGET/PRESERVE/semantic-impact/PATCH procedure directly addresses the prior weakness | PASS* |

`* PASS = contract-level coverage only; not a runtime execution result.`

## R1–R3 contract audit

### R1 Authority resolution
**Coverage:** Strong. V0.2 explicitly classifies sources, identifies conflicts, separates reference instructions from executable authority, and requires clarification when user-level constraints conflict without established priority.

**Static result:** PASS*

### R2 Semantic impact
**Coverage:** Strong. V0.2 explicitly checks whether a target edit carries implicit behavior and requires semantic-impact handling before applying a local patch.

**Static result:** PASS*

### R3 Context contamination
**Coverage:** Strong but potentially high-risk. V0.2 introduces explicit stale/irrelevant-context filtering and deduplication.

**Static result:** PASS WITH DESIGN NOTE*

**Design note:** “Remove irrelevant material from the active reasoning set” should not be interpreted as deleting provenance or destroying potentially relevant context before authority classification. A future runtime test must verify that filtering reduces contamination without causing evidence loss.

## AP5 protected negative control

V0.2 explicitly retains the capability/evidence honesty requirement: it must not claim a tool was used, a test was executed, or an output was verified without evidence.

**Static result:** PASS*

## Differential review: V0.1 → V0.2

### Improvements directly justified by evidence
- procedural source/authority classification;
- explicit conflict resolution boundary;
- stale-context filtering;
- semantic-impact inspection for local changes;
- explicit TARGET/PRESERVE/PATCH flow.

### Existing safeguards retained
- non-fabrication;
- evidence honesty;
- proportionality / anti-overengineering;
- ambiguity handling;
- observable success;
- failure handling.

### No evidence for adding
- generic agents;
- memory;
- MCP;
- automation;
- large universal templates;
- domain-specific rules unrelated to the Builder task.

## Decision

**V0.2 is not promoted.**

The static contract audit finds no immediate textual regression that justifies reverting the candidate, but it cannot substitute for execution. The next valid milestone is a reproducible or independently controlled runtime that actually applies V0.2 to A–G, P1–P7, R1–R3, and AP5.

Until that exists, the correct evidence label remains **LIMITED / STATIC-AUDIT**, not PASSED.
