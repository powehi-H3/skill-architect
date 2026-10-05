# Failure Library

Stable failure records belong here once a failure is reproduced and classified.

## Required record fields

- Failure ID
- First detected version
- Minimal reproduction
- Observed behavior
- Expected invariant
- Root-cause hypothesis
- Confirmation evidence
- Repair version
- Regression cases
- Current status

## Rules

Do not create a failure record merely because an output is aesthetically different. Record reproducible engineering failures with observable impact.

Do not merge unrelated failures simply because they look similar. Cluster by demonstrated root cause.

Do not delete historical failures after repair. Mark them resolved and retain their regression coverage.
