# Promotion Protocol V0

## States

`EXPERIMENTAL → CANDIDATE → STABLE`

## Candidate requirements

- Targeted failure has reproduced at least once when proposing a fix.
- The proposed change is minimal and traceable to evidence.
- Existing baseline and relevant pressure tests have been rerun.
- Known limitations are recorded.

## Stable requirements

- Definition-of-Done gates applicable to the component are satisfied.
- No unresolved critical regression exists.
- Evidence level is explicitly recorded.
- Tested commit SHA is recorded.
- Benchmark set and runtime limitations are recorded.
- A rollback point exists.

## Promotion rule

A component must not be promoted because it "looks better" or because a single test improved. Promotion requires evidence that the intended defect improved without unacceptable regression.

## Demotion rule

A Stable component may be returned to Candidate when a reproducible critical failure is discovered or when its evidence basis is found to be invalid.
