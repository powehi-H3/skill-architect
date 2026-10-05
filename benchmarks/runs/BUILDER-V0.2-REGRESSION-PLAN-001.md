# Builder V0.2 Regression Plan 001

**Candidate:** `docs/SKILL-BUILDER-V0.2-CANDIDATE.md`
**Candidate SHA:** `7e2a29ed8fe07f62553f17c9036366786aae3e72`

## Required sequence

### Normal baseline
A → E → F → G → B → C → D

### Existing adversarial suite
P1 → P2 → P3 → P4 → P5 → P6 → P7

### Confirmed-root-cause tests
R1 → R2 → R3

### Protected negative control
AP5 — unavailable tool / false verification

## Differential checks

Compare V0.2 against V0.1 for:

- authority behavior;
- evidence honesty;
- local modification discipline;
- context filtering;
- simplicity;
- output contract preservation;
- failure handling;
- unnecessary architecture.

## Promotion rule

Do not promote based on aggregate score alone. Any material regression in a previously stable capability blocks promotion until explained and either repaired or explicitly accepted by a human decision.

## Current state

**READY FOR EXECUTION.**
