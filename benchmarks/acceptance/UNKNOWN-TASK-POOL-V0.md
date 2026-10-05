# Unknown Task Blind-Test Pool V0

## Purpose

This pool is reserved for final generalization testing. Cases must not be used to tune the Builder before the blind run.

## Construction rules

- Tasks must come from domains not represented by the existing A–G baseline vocabulary.
- Cases must be written independently of the Builder's known failure taxonomy where practical.
- Expected invariants must be defined before execution.
- Builder must not receive labels such as "test", "benchmark", or the intended failure mode.
- At least one case must be a create-from-scratch task.
- At least one case must modify an existing Skill.
- At least one case must contain external reference material.
- At least one case must contain incomplete information.
- At least one case must contain a legitimate conflict requiring clarification.
- At least one case must tempt unnecessary architecture.

## Acceptance rule

The pool is not a benchmark for perfect output. It tests whether the Builder applies its engineering discipline to unseen task structures.

No case may be promoted into the tuning set after seeing a failure without being marked as contaminated and removed from the blind pool.

## Current status

**SEALED FOR DESIGN / NOT YET POPULATED WITH SECRET CASE CONTENT.**

The actual blind cases must be authored outside the Builder's active context before execution.
