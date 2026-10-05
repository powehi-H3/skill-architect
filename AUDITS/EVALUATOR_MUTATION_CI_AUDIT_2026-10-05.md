# Evaluator / Mutation / CI Evidence Audit — 2026-10-05

## Scope
Audit the real evidence chain for the current offline evaluator, mutation test, fixture semantics, and GitHub Actions gates. This audit does not claim semantic Skill quality.

## Evidence inspected

- `PROJECT_MASTER_SPEC.md`
- `scripts/evaluate_offline_candidate_v1.py`
- `scripts/mutation_test_offline_v1.py`
- `scripts/run_evaluator_suite_v1.py`
- `scripts/audit_offline_harness_v1.py`
- `scripts/validate_offline_fixture_semantics_v2.py`
- `.github/workflows/offline-evaluator-suite-v1.yml`
- `.github/workflows/offline-harness-audit-v1.yml`
- `.github/workflows/offline-gates-v1.yml`
- canonical fixtures A/B/C/D2/E/F/G/H/I/J and legacy D
- GitHub Actions run `37299276049` for commit `23cba510...`
- GitHub Actions run `37299365320` for the canonical harness audit
- GitHub Actions run `37299365321` for the legacy-alias audit
- GitHub Actions run `37299290750` showing the older combined-gates failure
- GitHub Actions run `37299487136` showing the first repaired fixture-semantics attempt

## Findings

### 1. Evaluator suite: REAL PASS evidence
Run `37299276049` checked out commit `23cba5102171618a238b49e491b5a727982cf1fd` and completed successfully.

The suite exercised A, D2, E, H, I, and J and also ran the mutation test. The repaired suite correctly accepts a matching UNKNOWN result without promoting UNKNOWN to PASS.

### 2. Mutation testing: included in the passing suite
The mutation test is executed by `run_evaluator_suite_v1.py`. Therefore the successful run above is direct CI evidence that the current four evaluator mutations were rejected.

An earlier standalone mutation workflow also passed on the same evaluator generation.

### 3. Canonical harness audit: REAL PASS evidence
Run `37299365320` completed successfully and executed `audit_offline_harness_v1.py` against the canonical fixture set.

Run `37299365321` also completed successfully for the legacy-alias audit workflow.

### 4. A separate stale/combined CI gate exposed another defect
Run `37299290750` failed in `validate_offline_fixture_semantics_v2.py` because that older validator still treated legacy D as canonical and had stale semantic assumptions for G and H.

This is important: the failure is evidence of a **real duplicate/stale CI contract**, not an evaluator failure.

### 5. Repairs to the stale gate
`validate_offline_fixture_semantics_v2.py` has now been upgraded to V4:
- canonical cases are A/B/C/D2/E/F/G/H/I/J;
- legacy D is validated separately;
- H checks the actual phrase `not executed` plus the absence boundary;
- I and J have explicit semantic checks;
- G accepts the actual fixture wording `authorizes` as well as `authorization`.

The corresponding combined Offline Gates workflow is currently running for the repair commit `88fdba7c457b941a445e53165f9451cc6122c8f1`; its final result is not yet available at the time of this audit.

## Important evaluator limitation
Case H remains a fixture-specific deterministic boundary rule rather than a general semantic inference rule. This is acceptable for the current contract gate, but it is not evidence that the evaluator can generally understand arbitrary Skill semantics.

## Current evidence status

- Evaluator implementation: **IMPLEMENTED**
- Evaluator suite: **VERIFIED PASS on commit `23cba510...`**
- Mutation testing: **VERIFIED PASS as part of that suite**
- Canonical harness audit: **VERIFIED PASS**
- Legacy-alias audit: **VERIFIED PASS**
- Combined Offline Gates after V4 repair: **RUNNING / NOT YET VERIFIED**
- Real LLM runtime: **BLOCKED by billing status**

## Gate decision

**Level 1 is not promoted yet.**

The remaining required evidence is the final result of the combined Offline Gates run for `88fdba7...`. If it passes, the offline evidence chain will have a materially stronger closed loop; if it fails, the failure must be repaired before promotion.
