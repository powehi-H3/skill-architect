# Skill Builder V0

**Status:** EXPERIMENTAL
**Role:** First implementation experiment built on the provisionally promoted Skill Architect core.

## 1. Purpose

Skill Builder turns a user's concrete task description into a candidate Skill specification that can be tested and revised.

It is a builder, not an authority. It must not invent requirements merely to make a Skill look complete.

## 2. Builder contract

The Builder must establish, explicitly or by careful inference from supplied material:

- Boundary / Purpose
- Inputs / Required State
- Intended Outcome / Observable Result
- Quality / Success Conditions
- Failure / Uncertainty Behavior

It may propose optional capabilities only when the task actually appears to require them:

- tools / environment
- evidence / provenance
- intermediate state
- routing / composition
- external references
- validation / regression
- specialized constraints

## 3. Operating procedure

### Step 1 — Understand the task

Extract the actual recurring task, desired result, user/operator, and important constraints.

Do not prematurely turn every sentence into a rule.

### Step 2 — Determine the boundary

State what the Skill does and, where useful, what it does not do.

If the boundary is materially ambiguous, preserve the ambiguity as an open question rather than fabricating a scope.

### Step 3 — Determine required state and inputs

Identify information and capabilities required for reliable execution.

Distinguish:

- user-provided inputs;
- contextual state;
- optional information;
- external capabilities or tools.

### Step 4 — Define observable success

Describe what a successful run produces or changes.

Prefer observable results over vague goals such as "do it well".

### Step 5 — Define quality conditions

Add the smallest set of criteria that can distinguish acceptable from unacceptable results.

Do not create a large checklist without evidence that it is useful.

### Step 6 — Define failure and uncertainty behavior

Specify what happens when required information, capability, or confidence is missing.

The Builder must not make up facts, tool results, source material, or successful completion.

### Step 7 — Select optional architecture

Only add references, scripts, tools, intermediate artifacts, routing, validation, or other machinery when justified by the task's behavior, dependencies, risk, or maintenance needs.

### Step 8 — Produce a candidate Skill

Generate the smallest candidate that can plausibly perform the task while preserving the semantic contract.

The candidate's document organization should suit the host environment and task. The Builder must not force a universal section template.

### Step 9 — Generate evaluation ideas

Propose evaluation cases based on the Skill's actual claims and risks. Do not force a fixed number or universal test taxonomy.

### Step 10 — Mark uncertainty

Clearly separate:

- supplied facts;
- inferred design choices;
- assumptions;
- open questions.

## 4. Output contract

A normal Builder result should contain:

1. **Task interpretation** — concise statement of what is being built.
2. **Boundary** — scope and meaningful exclusions.
3. **Required state / inputs** — including capability dependencies when relevant.
4. **Intended outcome** — observable success.
5. **Quality conditions** — minimum meaningful acceptance criteria.
6. **Failure / uncertainty behavior** — what the candidate does when it cannot reliably proceed.
7. **Optional architecture** — only justified additions.
8. **Candidate Skill** — a complete draft suitable for testing.
9. **Evaluation plan** — cases tied to the candidate's claims.
10. **Open questions** — unresolved items that could materially affect behavior.

For very simple tasks, the Builder may compress the presentation while preserving the underlying contract.

## 5. Builder constraints

The Builder must not:

- treat its own generated text as validated merely because it is detailed;
- turn examples into universal rules without justification;
- add tools because tools are available;
- add references because references are fashionable;
- add lifecycle bureaucracy to a simple Skill;
- claim testing was performed when it was only proposed;
- silently resolve a material user ambiguity by inventing requirements;
- copy an external Skill wholesale and call it architecture.

## 6. Self-review before output

Before presenting a candidate, check:

- Is the boundary clear enough to know when the Skill applies?
- Are required inputs/capabilities distinguishable from optional ones?
- Is success observable?
- Are quality conditions actionable and proportionate?
- Is uncertainty handled without fabrication?
- Did optional machinery earn its place?
- Did any inferred rule get mistaken for a user requirement?
- Is the candidate smaller than or comparable to the complexity justified by the task?

## 7. Evaluation protocol for Builder V0

The Builder itself must now be tested rather than declared successful.

### Test A — Simple writing Skill

Input: recurring article-polishing task with style requirements.

Expected: a small candidate with clear scope, source text as input, observable revised-text result, style/meaning preservation criteria, and sensible ambiguity handling. It should not invent a tool or complex file structure.

### Test B — Tool-dependent Skill

Input: task that requires inspecting a repository and reporting evidence-grounded findings.

Expected: capability/environment requirements are represented explicitly, while the Builder does not assume every Skill needs tools.

### Test C — Multi-step transformation Skill

Input: source material that must become a structured deliverable through analysis, drafting, and checking.

Expected: intermediate state may be represented because it affects reliability, but it is not imposed as a universal requirement.

### Test D — Ambiguous request

Input: an underspecified request where multiple materially different Skills could satisfy it.

Expected: the Builder identifies the ambiguity and asks for or records the minimum clarification instead of silently choosing a large set of assumptions.

### Test E — Minimal task

Input: a tiny deterministic task.

Expected: the Builder does not manufacture a large lifecycle, test suite, reference tree, or multi-layer architecture.

## 8. Promotion rule

Skill Builder V0 remains EXPERIMENTAL until these tests are run against actual generated candidates and the observed failures are recorded.

A future version should change the Builder only in response to evidence from these tests or clearly justified architecture changes.

## 9. Relationship to the architecture

This document implements the current architecture; it does not redefine it.

If Builder behavior conflicts with the core architecture, the conflict must be recorded and resolved explicitly rather than silently changing the architecture.
