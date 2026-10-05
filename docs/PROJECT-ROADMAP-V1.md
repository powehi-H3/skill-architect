# Skill Architect Roadmap V1

## Completed foundations

- Builder V0 baseline
- Manual Runner V0
- Normal benchmark baseline A–G
- Adversarial pressure P1–P7
- Targeted countertests C1–C3 / R1–R3
- V0.1 Candidate
- V0.2 Candidate
- Project Definition of Done
- Failure Library contract
- Promotion Protocol
- Unknown-task blind-test protocol

## Autonomous next sequence

1. Run V0.2 against the complete normal baseline.
2. Run V0.2 against P1–P7.
3. Run R1–R3.
4. Protect AP5 as a negative control.
5. Perform a V0.1 → V0.2 differential review.
6. Record any reproducible regressions.
7. If clean, run a second adversarial wave focused on authority, semantic impact, and context contamination.
8. If a new failure reproduces, classify it before changing V0.2.
9. If stable, prepare Reviewer V0 as a separate component rather than expanding Builder indefinitely.
10. Before final promotion, execute the sealed unknown-task blind test.

## Stop conditions requiring human participation

- A test requires access to a runtime, model, credential, or tool unavailable to the current environment.
- A destructive repository operation is proposed.
- A new external service or permission must be connected.
- A blind test requires the user to supply or approve secret/unseen test material.
- A promotion decision has consequences outside this repository.
- The evidence is ambiguous enough that choosing a branch would encode a user preference rather than an engineering conclusion.

Until one of these conditions occurs, continue with the documented sequence without waiting for routine approval.
