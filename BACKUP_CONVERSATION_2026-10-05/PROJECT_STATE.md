# Skill Architect — Project State Backup

## Repository

`powehi-H3/skill-architect`

## Runtime state

### OpenAI runtime

BLOCKED by API billing status:

`billing_not_active`

No payment/credit action is currently available to the user, so this path is intentionally paused.

### Offline runtime

Operational and previously successful.

## Implemented components

- Offline Builder harness
- Offline evidence artifact generation
- Offline Harness Audit V0/V1 direction
- deterministic candidate evaluator
- mutation testing
- unified evaluator suite
- GitHub Actions workflows for the above

## Important quality boundary

Offline/mock execution is infrastructure evidence only. It must not be represented as evidence that an LLM actually executed or that the Builder has passed semantic quality evaluation.

## Current next engineering target

Strengthen the deterministic evaluator so that its assertions are substantive rather than merely fixture-schema checks. Expand mutation testing and verify that intentionally weakened/incorrect candidates are rejected.

After the offline evaluator is trustworthy, the real OpenAI runtime can be re-enabled when billing becomes available.

## Repository history

Use Git history as the authoritative record of actual code/config changes.
