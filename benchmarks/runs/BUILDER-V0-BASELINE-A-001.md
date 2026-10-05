# Builder V0 Baseline — Case A

**Run ID:** BUILDER-V0-BASELINE-A-001
**Case:** A — Minimal deterministic task
**Status:** COMPLETED / MANUAL CONTROLLED RUN
**Builder SHA:** `19667fdad8edc0464ef45d7b0687210ff0cc26c5`
**Benchmark SHA:** `176a56c5b694fa8810d8c7b577c53d31a37f5a66`
**Evaluation independence:** LIMITED

## 1. Blind Builder input

Create a Skill that converts a user-provided Celsius temperature into Fahrenheit. The user supplies one temperature. Return the converted value and unit. If the temperature is missing or not interpretable as a number, say what is missing instead of inventing it.

No expected properties, failure labels, or evaluator notes were supplied in the Builder packet.

## 2. Candidate Skill

---
name: celsius-to-fahrenheit
description: Use when a user provides one Celsius temperature and wants it converted to Fahrenheit. Do not use when the input temperature is missing or cannot be interpreted as a number; in that case report the missing or invalid input.
---

# Celsius to Fahrenheit

## Goal
Convert one user-provided Celsius temperature to Fahrenheit.

## Input
- One Celsius temperature supplied by the user.

## Execution
1. Check that exactly one temperature value is available and interpretable as a number.
2. Convert using `F = (C × 9/5) + 32`.
3. Return the converted value with the Fahrenheit unit.

## Output
Return the converted Fahrenheit value and unit.

## Quality criteria
- The calculation is mathematically correct.
- The output identifies the result as Fahrenheit.
- No value is invented when the input is missing or invalid.

## Failure handling
- If the temperature is missing, state that a Celsius temperature is required.
- If the supplied temperature is not interpretable as a number, state that the input is invalid instead of inventing a value.

## Evaluation ideas
- A normal numeric Celsius input.
- A missing input.
- A non-numeric input.

## Open questions
None for the stated task.

## 3. Evaluation

### Boundary correctness — 2/2
Narrowly scoped to one Celsius-to-Fahrenheit conversion.

### Input/state correctness — 2/2
Requires one user-provided Celsius temperature and validates interpretability.

### Outcome observability — 2/2
Defines a concrete Fahrenheit result and unit.

### Quality adequacy — 2/2
Correct formula, unit identification, and non-invention are explicit.

### Failure/uncertainty handling — 2/2
Missing and invalid inputs have explicit behavior.

### Proportionality / non-overengineering — 2/2
No tools, references, memory, routing, automation, registry, or complex lifecycle were introduced.

### Evidence discipline — 2/2
No external execution or evidence was falsely claimed.

### Change/preservation discipline — N/A
Not applicable to Case A.

## 4. Observed unnecessary additions

None material.

## 5. Failure classification

No substantive Builder failure observed in this controlled manual run.

## 6. Root-cause hypothesis

Not applicable.

## 7. Builder change decision

**NO CHANGE.**

There is no evidence from Case A that justifies modifying Builder V0.

## 8. Regression cases

No new regression case is justified from this result.

## 9. Evidence limitation

This is a controlled manual execution performed in the same model/session family used for evaluation. It is therefore not an independent-runtime black-box result. The candidate and evaluation are preserved here to maintain auditability, but `evaluation_independence` remains `LIMITED`.
