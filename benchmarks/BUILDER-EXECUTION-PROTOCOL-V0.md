# Builder Execution Protocol V0

**Status:** EXPERIMENTAL
**Purpose:** Define what counts as a valid execution of Skill Builder V0 and how to capture a reproducible evidence record.

## 1. Scope

This protocol sits between the Builder specification and the benchmark/harness. It does not change Builder behavior. It defines the conditions under which a Builder run may be called an actual run.

A run is valid only when the complete Builder input and complete Builder output are captured, the Builder version is identifiable, and evaluation is performed after the candidate output is frozen.

## 2. Required run identity

Every run must record:

- Run ID
- date/time
- Builder version or commit
- benchmark case ID and version
- execution surface/runtime
- model identifier when known
- relevant configuration when known
- evaluator version

Unknown metadata must be marked `UNKNOWN`; it must never be reconstructed from memory.

## 3. Input isolation

The Builder receives:

1. the benchmark case input;
2. only context explicitly permitted by the case;
3. the Builder specification and any dependencies that are part of the declared Builder environment.

Do not leak the benchmark's expected properties, failure signals, scoring rubric, or evaluator notes into the Builder prompt unless the case explicitly tests behavior with such information.

The Builder must not be told what result would earn a passing score.

## 4. Candidate capture

Capture the Builder's complete response exactly as produced.

Do not:

- clean it up before evaluation;
- remove unwanted sections;
- correct wording;
- merge it with evaluator comments;
- silently fill missing sections.

The captured candidate becomes immutable evidence for that run.

## 5. Evaluation isolation

After candidate capture:

1. freeze the candidate;
2. provide the candidate and the applicable benchmark expectations to the evaluator;
3. keep Builder self-assessment separate from evaluator judgment;
4. record observations before proposing fixes.

The evaluator may explain why a behavior is good or bad, but must not silently edit the candidate and then evaluate the edited version.

## 6. Evidence hierarchy

For every substantive claim, classify it as:

- **Observed:** directly visible in the captured execution;
- **Inferred:** reasoned from observed evidence;
- **Unverified:** not demonstrated by this run.

Only Observed claims can establish that a particular Builder output contained or omitted something.

## 7. Valid run gate

A run may be marked `VALID` only if all are present:

- complete benchmark input;
- complete Builder output;
- identifiable Builder version;
- identifiable benchmark case;
- post-capture evaluation;
- evidence-backed findings.

If any required element is absent, mark the run `INVALID` or `INCOMPLETE` rather than manufacturing the missing evidence.

## 8. Manual execution mode

A manual run is permitted when no automated Builder runtime exists, provided the operator follows this protocol exactly.

Manual execution must identify the model/runtime used and preserve the complete interaction needed to reproduce or audit the result.

The operator must not switch models, alter hidden instructions, add benchmark expectations, or rewrite the Builder specification mid-run without recording that as an environment change.

## 9. Runtime execution mode

An automated runtime may be used when it can:

- load a known Builder version;
- provide controlled case input;
- capture complete output;
- persist run metadata;
- prevent evaluator contamination;
- produce an auditable evidence record.

Automation is not required for V0 validity. Reproducibility and evidence integrity are required.

## 10. Case execution order

For the first baseline run, execute:

`A → E → F → G → B → C → D`

Do not modify Builder V0 between these baseline cases solely because one case looks weak. The purpose of the baseline is to observe the unmodified Builder across the full test surface.

If an environmental failure prevents a case from running, record the failure and continue only where doing so does not contaminate the remaining cases.

## 11. Evaluation record

Each case record must contain:

### Metadata
- Run ID
- Case ID
- Builder version
- Runtime/model
- Status

### Input
- exact prompt/context supplied

### Candidate
- complete Builder output

### Evaluation
- expected properties
- observed properties
- failure labels
- severity
- evidence

### Diagnosis
- primary failure
- root-cause hypothesis
- confidence

### Change proposal
- smallest justified Builder change
- why it addresses the root cause
- what it intentionally does not change

### Regression
- cases required for rerun
- reason for each case

## 12. Prohibited shortcuts

Do not:

- invent candidate outputs;
- claim a case passed without an actual run;
- use the benchmark expectations as hidden Builder instructions;
- let the Builder grade itself;
- change Builder V0 after each case and call the sequence a baseline;
- infer tool execution from the mere presence of tool instructions;
- treat a proposed test as an executed test;
- turn evaluator suggestions into observed facts.

## 13. First baseline objective

The first objective is not to obtain a high score. It is to obtain a trustworthy baseline that reveals where Builder V0 succeeds, fails, over-engineers, or remains uncertain.

Only after all seven baseline cases have valid evidence should the project select the smallest justified Builder change.

## 14. Relationship to promotion

A Builder revision may be proposed after baseline analysis, but it is not promoted merely because it fixes one case.

Promotion requires:

1. a documented failure;
2. a justified minimal change;
3. affected regression runs;
4. evidence that the change improves the intended behavior without unacceptable regression.
