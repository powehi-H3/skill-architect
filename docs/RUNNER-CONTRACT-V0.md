# Reproducible Runner Contract V0

## Goal
Provide a repeatable execution record for a fixed Builder version against a fixed benchmark case.

## Required inputs
- Builder commit SHA;
- benchmark/case identifier and SHA;
- exact Builder input;
- runtime/model identifier when available;
- tool/capability configuration;
- evaluator configuration;
- timestamp;
- execution status.

## Required outputs
- exact candidate produced by the Builder;
- evaluator result;
- structured findings;
- evidence references;
- runtime/tool failures;
- reproducibility metadata.

## Evidence states

`EXECUTED` — actual runtime execution occurred and evidence is preserved.

`STATIC-AUDIT` — repository artifacts were inspected but the Builder was not executed.

`MANUAL-EMULATION` — procedure was manually applied in the current model environment.

`UNKNOWN` — evidence is insufficient to determine execution state.

## Hard rule
Never convert STATIC-AUDIT or MANUAL-EMULATION into EXECUTED by wording alone.

## Determinism target
A later run with the same declared inputs should be able to identify whether differences came from Builder version, benchmark version, runtime/model variation, tool availability, or evaluator variation.

## Current project limitation
The repository currently contains controlled manual and static evidence but does not yet contain a proven independent runtime harness for executing Builder V0.2. This is an explicit project gate, not a reason to manufacture a PASS.
