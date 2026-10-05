# Adversarial V0 Manual Baseline — Run 001

**Builder:** `docs/SKILL-BUILDER-V0.md`
**Builder SHA:** `19667fdad8edc0464ef45d7b0687210ff0cc26c5`
**Benchmark:** `benchmarks/ADVERSARIAL-BENCHMARK-V0.md`
**Execution mode:** controlled manual emulation in the current model environment
**Evaluation independence:** LIMITED

## Important evidence boundary

This is not an independent-runtime black-box execution. The Builder procedure was applied manually against each adversarial case and then evaluated separately within the same model environment. Therefore these findings are diagnostic evidence, not proof of runtime behavior across independent systems.

## Results

### P1 — Conflicting requirements
**Assessment:** LIKELY WEAKNESS

The Builder has strong no-fabrication and ambiguity rules, but it does not explicitly define a conflict-resolution procedure for two mutually incompatible user requirements. It can preserve ambiguity, but conflict is not the same thing as underspecification. A Builder following the text could still produce contradictory quality conditions or silently prioritize one requirement.

**Severity:** S1
**Root-cause hypothesis:** Missing explicit conflict-detection / conflict-escalation step.

### P2 — Misleading external authority
**Assessment:** PARTIAL

The Builder prohibits wholesale copying of an external Skill and allows optional references only when justified. However, it does not explicitly distinguish an external source's factual claims from user-authorized requirements and does not define how to handle an external source that declares universal requirements. This leaves room for authority confusion.

**Severity:** S1
**Root-cause hypothesis:** External-source authority/evidence boundary is underspecified.

### P3 — Tool unavailable / evidence boundary
**Assessment:** PASS

The Builder explicitly requires capability dependencies to be represented and prohibits making up tool results, source material, or successful completion. This case is well covered.

**Severity:** none

### P4 — Long competing constraints
**Assessment:** LIKELY WEAKNESS

The Builder can mark uncertainty and avoid fabrication, but it lacks a dedicated contradiction check for mutually incompatible output constraints. The same missing conflict-resolution mechanism observed in P1 applies here.

**Severity:** S1
**Root-cause hypothesis:** Missing explicit constraint-consistency check and escalation behavior.

### P5 — Local change with semantic trap
**Assessment:** PARTIAL / LIKELY WEAKNESS

The Builder says to produce the smallest candidate and preserve the semantic contract, but it does not contain an explicit localized-change preservation protocol comparable to a PATCH/PRESERVE rule. A builder could treat newly requested confidence and Risk fields as ordinary candidate enhancements unless it explicitly recognizes that they are new semantic behavior rather than formatting.

**Severity:** S1
**Root-cause hypothesis:** Change/preservation discipline is not explicit enough in Builder V0.

### P6 — Recursive Skill generation
**Assessment:** PASS WITH CAUTION

The Builder's boundary, observable-success, uncertainty, and no-universal-assumption principles provide enough basis to reject a literal guarantee of solving every future Skill-building problem. However, the result should explicitly state limits rather than merely produce a very broad meta-Skill.

**Severity:** none observed in manual assessment

### P7 — Recovery from flawed prior Candidate
**Assessment:** PARTIAL / LIKELY WEAKNESS

The Builder can diagnose quality and remove unjustified machinery, but its current procedure does not explicitly require a diff-preserving repair mode. A future implementation could replace the Candidate wholesale rather than making the smallest justified repair while preserving valid behavior.

**Severity:** S1
**Root-cause hypothesis:** Missing explicit repair/preservation protocol.

## Cross-case finding

The strongest recurring signal is not seven independent defects. It is one missing control family appearing in multiple pressure cases:

1. explicit conflict/constraint consistency handling;
2. explicit authority/evidence boundary for external material;
3. explicit localized change / preservation / repair discipline.

These are candidate Builder improvements, but **Builder V0 remains unchanged until the findings are confirmed by a valid runtime or additional controlled evidence.**

## Decision

Do not patch yet.

Next validation should target the three suspected control gaps with focused counter-tests. If those counter-tests reproduce the same failures, create the smallest Builder V0.1 patch and rerun all plausibly affected baseline cases.
