# Evaluator / Mutation / CI Evidence Audit — 2026-10-05

## Scope
Audit the current deterministic evaluator, mutation test, unified suite, and GitHub Actions evidence chain without promoting any result beyond the evidence actually observed.

## Evidence inspected
- `PROJECT_MASTER_SPEC.md`
- `scripts/evaluate_offline_candidate_v1.py`
- `scripts/mutation_test_offline_v1.py`
- `scripts/run_evaluator_suite_v1.py`
- `.github/workflows/offline-evaluator-suite-v1.yml`
- `benchmarks/fixtures/offline-builder-v0/case-H.json`
- GitHub Actions run `37298560758`, head `d8bea1e0a3cc1722ba8fa86644d81a6336943c9f`
- Job `111725543126` and its decoded log

## Findings

### 1. CI evidence is REAL and traceable
The V1 suite workflow actually executed on GitHub Actions against commit `d8bea1e0a3cc1722ba8fa86644d81a6336943c9f`.
Conclusion: `REAL-CI-EVIDENCE = PASS`.

### 2. Individual evaluator cases A/D2/E/H/I/J produced the expected dispositions
The CI log shows:
- A PASS/PASS
- D2 PASS/PASS
- E FAIL/FAIL
- H FAIL/FAIL
- I UNKNOWN/UNKNOWN
- J FAIL/FAIL
The evaluator itself therefore produced contract-aligned dispositions for all six cases in this run.

### 3. Mutation testing genuinely ran and passed
The CI log reports `MUTATION TEST V3: PASS` and `Evaluator mutations killed: 4`.
Conclusion: the four current evaluator mutations were killed in the real CI run.

### 4. Unified suite has a logic defect
`run_evaluator_suite_v1.py` explicitly sets `EXPECTED_EXIT = {"I": 1}` while the evaluator exits with code 0 whenever `actual == expected_disposition`.
Because case I is `UNKNOWN/UNKNOWN`, the evaluator correctly exits 0, but the suite expects 1 and therefore reports `failed: ["I"]`.
Conclusion: `SUITE_GATE = FAIL` due to a test-harness defect, not an evaluator-case mismatch.

### 5. H remains a weak semantic test
The evaluator's H branch unconditionally returns FAIL for `case == "H"`, regardless of candidate content. This means H demonstrates the evidence boundary as a fixed fixture contract, but it does not test whether the evaluator can detect a misleading H candidate.
Conclusion: `H_SEMANTIC_STRENGTH = INSUFFICIENT`.

### 6. CI warnings are non-blocking
The run completed on Ubuntu 24.04. The only observed workflow warning was the Node.js 20 deprecation warning for `actions/checkout@v4`. It did not cause the failure.

## Overall verdict
`AUDIT STATUS = FAIL / REPAIR REQUIRED`

The evidence chain is substantially real: the workflow executed, all six evaluator cases emitted expected dispositions, and all four current mutations were killed. However, the unified suite itself is currently red because of an incorrect exit-code expectation for the intentionally non-promotable UNKNOWN case, and H needs a stronger semantic predicate.

No release or completion claim is justified from this audit.

## Required repairs before promotion
1. Fix the suite's case-I exit expectation so a correctly classified UNKNOWN does not fail the gate.
2. Replace H's unconditional FAIL with a deterministic predicate that distinguishes a valid evidence-boundary fixture from an unsupported execution claim.
3. Re-run the full GitHub Actions suite and inspect the resulting log.
4. Only promote Level 1 after the repaired run is green and mutation tests remain green.
