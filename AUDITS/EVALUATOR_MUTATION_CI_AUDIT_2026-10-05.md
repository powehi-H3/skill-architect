# Evaluator / Mutation / CI Evidence Audit — 2026-10-05

## Scope
Audit the real evidence chain for the current offline evaluator, mutation test, and GitHub Actions suite. This audit does not claim semantic Skill quality.

## Evidence inspected

- `PROJECT_MASTER_SPEC.md`
- `scripts/evaluate_offline_candidate_v1.py`
- `scripts/mutation_test_offline_v1.py`
- `scripts/run_evaluator_suite_v1.py`
- `.github/workflows/offline-evaluator-suite-v1.yml`
- `benchmarks/fixtures/offline-builder-v0/case-{A,D2,E,H,I,J}.json`
- GitHub Actions run `37298560758` for commit `d8bea1e0a3cc1722ba8fa86644d81a6336943c9f`
- GitHub Actions run `37298560556` for the mutation workflow

## Findings

### 1. Evaluator execution: REAL evidence
The evaluator suite was actually executed by GitHub Actions. Run `37298560758` checked out commit `d8bea1e0...` and ran `python3 scripts/run_evaluator_suite_v1.py`.

Observed evaluator results:
- A: PASS = expected PASS
- D2: PASS = expected PASS
- E: FAIL = expected FAIL
- H: FAIL = expected FAIL
- I: UNKNOWN = expected UNKNOWN
- J: FAIL = expected FAIL
- Mutation V3: PASS; 4 mutations killed

### 2. CI result: FAILED for a harness bug
The workflow itself failed with `failed: ["I"]`. The failure was not caused by an evaluator disposition mismatch. The evaluator correctly returned UNKNOWN for I. The suite incorrectly expected the evaluator process to exit 1 for a matching UNKNOWN result.

This is a genuine test-harness defect: the suite conflated "UNKNOWN must not be promoted" with "UNKNOWN must make the process fail".

### 3. Mutation workflow: REAL evidence and PASS
Run `37298560556` completed successfully for the same commit. The mutation workflow therefore provides real CI evidence that the four current evaluator mutations are rejected.

### 4. Offline evaluator limitation
Case H is currently a weak semantic rule because the evaluator has a case-specific deterministic FAIL branch rather than deriving the disposition entirely from the candidate content. This is acceptable as a fixture-specific contract for the current gate, but it is not yet a general-purpose semantic evaluator.

### 5. Legacy fixture boundary
`case-D.json` uses an older fixture schema and is not canonical. The audit now treats it as a legacy alias and validates its legacy markers rather than pretending it is a canonical evaluator case.

## Repairs made after this audit

1. Fixed `scripts/run_evaluator_suite_v1.py` so a matching UNKNOWN result is accepted while remaining explicitly non-promotable.
2. Upgraded `scripts/audit_offline_harness_v1.py` to V2:
   - covers I and J;
   - explicitly validates the legacy D boundary;
   - requires PASS, FAIL, and UNKNOWN coverage;
   - adds semantic sanity checks for I and J.

## Current evidence status

- Evaluator implementation: **IMPLEMENTED**
- Mutation implementation: **IMPLEMENTED**
- Mutation CI: **VERIFIED PASS**
- Evaluator suite CI at audited commit: **VERIFIED FAILURE, defect identified**
- Evaluator suite after repair: **NOT YET VERIFIED**
- Real LLM runtime: **BLOCKED by billing status**

## Gate decision

**DO NOT promote Level 1 yet.**

The next required evidence is a fresh GitHub Actions run after commit `23cba510...` / subsequent audit commit. It must show:

1. evaluator suite PASS;
2. UNKNOWN case remains UNKNOWN without being promoted;
3. mutation suite PASS;
4. harness audit V2 PASS.

Only after those are observed should the offline evaluator integrity gate be considered genuinely green.
