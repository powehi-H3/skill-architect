# Cross-Domain Validation V0

**Status:** EXPERIMENTAL RESEARCH
**Purpose:** Test whether the current Skill Architect concepts generalize across unrelated Skill types.

## Method

We test three intentionally different tasks against the current architecture:

- A — Article polishing
- B — Code review
- C — Meeting-note synthesis

The goal is not to prove the architecture correct. The goal is to find where it breaks, becomes unnecessary, or imposes needless complexity.

## Evaluation dimensions

For each task, ask:

1. Can the task be described without distorting its nature?
2. Can trigger/boundary be stated usefully?
3. Can required and optional inputs be distinguished?
4. Can execution be described without prescribing one universal procedure?
5. Can output expectations be made testable?
6. Can quality be evaluated with task-appropriate criteria?
7. Can uncertainty, missing information, and conflicts be handled without fabrication?
8. Can the Skill evolve without making the lifecycle burdensome?

A concept fails generalization if it is only useful because of one domain's peculiarities, or if enforcing it adds more complexity than value for ordinary Skills.

## A — Article polishing

### Natural contract
- Input: source text + requested style/constraints.
- Boundary: improve the supplied text rather than inventing substantive claims.
- Output: revised text matching the requested purpose and constraints.
- Quality: preservation of intended meaning, clarity, style compliance, grammar, and appropriate completeness.
- Failure: ambiguous target audience/style, missing source text, or requests that conflict with preservation requirements.

### Architecture result
The general contract fits naturally.

### Important qualification
A fixed execution sequence is unnecessary. Different writing tasks may require different procedures. The architecture should specify required outcomes and constraints rather than force every Skill through identical steps.

### Evidence status
PASS for general contract concepts; no evidence yet that a dedicated lifecycle is necessary for every simple writing Skill.

## B — Code review

### Natural contract
- Input: code/diff + relevant project context + review criteria.
- Boundary: identify defects, risks, maintainability issues, and requirement violations; do not silently rewrite unrelated code.
- Output: findings with evidence, severity/relevance, and actionable recommendations.
- Quality: technical correctness, evidence grounding, coverage of important issues, avoidance of fabricated project facts.
- Failure: incomplete diff/context, unavailable dependency information, or uncertainty about intended behavior.

### Architecture result
The general contract fits, but input dependencies are materially more important than in article polishing.

### Important qualification
Tool availability and repository context may be part of the Skill's operating environment rather than ordinary user input. The architecture must allow environment/dependency contracts without making them mandatory for every Skill.

### Evidence status
PASS for general contract concepts; environment-aware execution should remain optional/capability-dependent.

## C — Meeting-note synthesis

### Natural contract
- Input: transcript/notes + requested format/audience.
- Boundary: summarize and organize supplied information; distinguish stated facts from interpretation.
- Output: structured minutes, decisions, actions, open questions, and unresolved items when requested.
- Quality: source fidelity, coverage of material decisions/actions, clear attribution where available, and no invented commitments.
- Failure: incomplete transcript, unclear speaker attribution, contradictory source material, or missing context.

### Architecture result
The general contract fits naturally.

### Important qualification
Different meeting outputs may legitimately omit sections. Therefore a universal output schema would be over-prescriptive; the output contract should be task-specific.

### Evidence status
PASS for general contract concepts; fixed universal output sections should be rejected.

## Cross-domain findings

### Concepts that currently generalize

1. **Explicit scope/boundary** — useful in all three tasks.
2. **Input expectations** — useful, but environment/dependency inputs must remain optional where appropriate.
3. **Output contract** — useful when defined per task, not as a universal format.
4. **Quality criteria** — useful and necessarily domain-specific.
5. **Failure handling** — useful, especially for missing/ambiguous information and uncertainty.
6. **Evidence/provenance awareness** — useful whenever claims or source material matter.

### Concepts that require qualification

1. **Universal execution steps** — should not be mandatory. Skills need a procedure sufficient for reproducibility, not an identical pipeline.
2. **Universal test categories** — should be selected according to task behavior and risk.
3. **Lifecycle overhead** — should scale with complexity/risk; a tiny Skill should not require a bureaucratic process designed for a complex system.
4. **Environment/dependency contracts** — should be available as an optional contract component.
5. **Universal output sections** — should not exist at the architecture level.

### Concepts rejected as core rules at this stage

- Rules justified only by the H3 project.
- Rules requiring every Skill to have the same number or type of tests.
- Rules requiring every Skill to expose identical internal phases.
- Rules requiring every Skill to use the same output structure.

## Current conclusion

The strongest candidate for a general Skill architecture is a **small contract core plus optional capability-specific components**, not a large universal rule stack.

Candidate core:

```text
Identity / Boundary
Input expectations
Intended outcome
Output expectations
Quality criteria
Failure / uncertainty handling
Evidence where relevant
```

Everything else should earn its place by demonstrating usefulness across multiple Skill types.

## Next experiment

Before promoting any of these findings to CORE ARCHITECTURE, test the architecture against at least one tool-using Skill and one multi-step transformation Skill. Record failures rather than forcing the architecture to fit.
