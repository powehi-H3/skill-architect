# Builder V0 — Run 001 / Case F

**Status:** MANUAL TWO-PHASE ANALYSIS — RUNTIME INDEPENDENCE LIMITED
**Date:** 2026-10-05
**Builder under test:** `docs/SKILL-BUILDER-V0.md`
**Builder SHA:** `19667fdad8edc0464ef45d7b0687210ff0cc26c5`
**Benchmark:** `benchmarks/BUILDER-BENCHMARK-V0.md`
**Benchmark SHA:** `176a56c5b694fa8810d8c7b577c53d31a37f5a66`
**Harness:** `benchmarks/BUILDER-TEST-HARNESS-V0.md`
**Execution protocol:** `benchmarks/BUILDER-EXECUTION-PROTOCOL-V0.md`
**Execution surface:** ChatGPT manual execution
**Model:** GPT-5.6 Luna

## 1. Evidence boundary

This record is a controlled manual two-phase analysis of Case F. It is not an independently hosted Builder runtime. The Builder specification was read first; the Case F benchmark requirements were not treated as Builder instructions during candidate generation. The resulting candidate is frozen conceptually before evaluation.

Because generation and evaluation occur in the same model/runtime, evaluator independence is LIMITED. This record is valid for baseline observation but must not be represented as independent-runtime validation.

## 2. Exact benchmark input

> I found an existing public Skill that uses a ten-section template. Create my own Skill for a simple recurring task using whatever parts of that Skill are genuinely useful, but do not copy requirements merely because the external Skill contains them.

## 3. Builder generation phase

### Task interpretation
Create a Skill for a simple recurring task using only those mechanisms from an external ten-section Skill template that are justified by the actual task. The external template is reference material, not an authority.

### Boundary
The Builder can use the external Skill as design evidence, but must determine the candidate Skill's scope from the actual recurring task. Because the benchmark input does not identify what the simple recurring task is, the exact task boundary remains materially unspecified.

### Required state / inputs
- The actual recurring task must be supplied or identified before a task-specific Skill can be responsibly specified.
- The external Skill/template may be supplied as reference material if the user wants its mechanisms considered.
- No requirement is established merely by the external template's ten-section structure.

### Intended outcome
A small, task-specific Skill whose mechanisms are justified by the recurring task, with irrelevant external requirements excluded.

### Quality conditions
- External material is treated as reference/evidence rather than automatic authority.
- Only mechanisms that solve an actual task need are retained.
- The candidate does not claim the external ten-section structure is universally required.
- Missing task information is surfaced rather than silently invented.
- The resulting Skill is proportionate to the actual task once that task is known.

### Failure / uncertainty behavior
If the recurring task is not supplied, do not invent one. Ask for or record the minimum clarification needed to identify the task before producing a fully task-specific Skill.

If the external Skill is unavailable, do not pretend to have inspected it; the Builder can still describe the selection principle at a general level.

### Optional architecture
No tools, references, scripts, routing, or workflow machinery are automatically justified. The external Skill may be consulted as reference material, but its architecture must earn inclusion mechanism by mechanism.

### Candidate Skill
Because the benchmark omits the actual recurring task, a fully task-specific Skill would require invented requirements. The responsible candidate is therefore a minimum intake/selection contract rather than a fabricated task Skill:

```markdown
---
name: task-specific-skill-builder-input
# The final name and description should be chosen after the actual recurring task is supplied.
---

## Goal
Define a small Skill for the user's actual recurring task, using external Skill material only where it is genuinely useful.

## Required input
- The actual recurring task and desired result.
- Optional external Skill/template supplied as reference material.

## Selection rule
Treat external material as reference, not authority. Keep only mechanisms justified by the actual task, its risks, dependencies, and quality requirements.

## Output
A task-specific Skill whose scope, inputs, outcome, quality conditions, and failure behavior are derived from the actual task rather than copied from the external template.

## Failure handling
If the actual recurring task is not specified well enough to determine the Skill boundary, request the minimum clarification needed. Do not invent the task or silently adopt the external template's assumptions.
```

### Evaluation ideas proposed during Builder generation
1. Supply a simple deterministic task and a bloated ten-section external template; check whether irrelevant architecture is rejected.
2. Supply a task that genuinely benefits from one mechanism in the external Skill; check whether that mechanism is adapted without importing unrelated requirements.
3. Supply the external template but omit the actual recurring task; check whether the Builder asks for clarification rather than inventing a task.

### Open questions
The actual recurring task is missing from the benchmark input. A final task-specific Skill cannot be judged for proportionality until that missing input is supplied.

## 4. Candidate freeze

The candidate above is treated as immutable evidence for this run. No evaluator correction has been applied to it.

## 5. Evaluation phase

### Expected properties from Case F
- external material treated as reference/evidence;
- useful mechanisms may be adapted;
- unsupported external requirements not promoted automatically;
- resulting Skill sized to the actual task.

### Observed properties

**Boundary — 2/2**
The candidate explicitly refuses to invent the missing recurring task and treats the external template as reference material rather than the task boundary.

**Input/state — 2/2**
It correctly identifies the actual recurring task as required state and distinguishes the optional external template from the task itself.

**Outcome — 2/2**
The intended result is observable: a task-specific Skill whose mechanisms are justified by the actual task.

**Quality — 2/2**
The candidate gives concrete criteria for rejecting irrelevant external machinery and preserving proportionality.

**Failure/uncertainty — 2/2**
It explicitly refuses to fabricate the missing task and distinguishes an unavailable external source from an inspected source.

**Proportionality / non-overengineering — 2/2**
It does not reproduce a ten-section template merely because it exists. It adds no tools, routing, scripts, or lifecycle machinery without justification.

**Evidence discipline — 2/2**
This is the strongest part of the result: the external Skill is explicitly treated as reference/evidence, not authority, and the candidate makes no claim to have inspected unavailable material.

**Change/preservation discipline — N/A**
Case F is not a localized change request.

### Observed failure signals
None in this manual run.

### Primary failure label
None.

### Severity
None.

## 6. Diagnosis

**Result:** Case F shows the intended Builder behavior under the available manual execution conditions.

The critical behavior is that the Builder did not allow the external ten-section template to define the Skill automatically. It also recognized a second-order ambiguity that the benchmark itself contains: the benchmark says "a simple recurring task" but does not identify that task. Rather than inventing a task, the candidate converts the missing information into an explicit input requirement.

This is preferable to manufacturing a generic Skill and pretending that its architecture was derived from the user's needs.

### Confidence
Moderate. The observed candidate strongly satisfies the benchmark properties, but evaluator independence remains limited because generation and evaluation use the same model/runtime.

## 7. Builder change decision

**No Builder change proposed from Case F.**

No observed failure justifies a patch. In particular, the candidate's refusal to copy the external ten-section template is evidence that the existing anti-copy constraint in Builder V0 is functioning as intended.

Do not weaken or broaden the Builder merely to force a more elaborate candidate from an intentionally underspecified benchmark.

## 8. Benchmark quality note

Case F contains a useful stress property but also an intentional ambiguity: it does not identify the "simple recurring task." This is valuable because it simultaneously tests evidence discipline and missing-input handling. It should remain as a baseline case unless later runs show that it fails to discriminate Builder versions.

## 9. Regression implications

No regression run is triggered because no Builder behavior was changed.

Remaining baseline cases should continue against Builder SHA `19667fdad8edc0464ef45d7b0687210ff0cc26c5`.

## 10. Next baseline case

Proceed to **Case G — Localized Change Request** without modifying Builder V0.
