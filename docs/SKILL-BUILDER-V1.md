# Skill Builder V1

**Status:** IMPLEMENTATION BASELINE — NOT PROMOTED

## Purpose

Skill Builder V1 is the first concrete Builder implementation contract. It turns a structured task specification into a minimal, testable Skill candidate without requiring an LLM.

V1 is deliberately deterministic. It is a compiler-like baseline, not a claim that language models can be replaced by templates.

## Input contract

The Builder accepts JSON with:

- `task_id` — stable identifier;
- `task` — concrete recurring task description;
- `inputs` — required user-provided inputs;
- `outcome` — observable result;
- `quality` — minimum acceptance conditions;
- `failure` — missing/invalid/uncertain behavior;
- `dependencies` — optional tools/environment dependencies;
- `evidence` — optional evidence/provenance rules;
- `constraints` — optional task-specific constraints.

The Builder must reject missing `task_id`, `task`, `inputs`, `outcome`, `quality`, or `failure` rather than inventing them.

## Output contract

The output is a complete Markdown Skill candidate containing only justified sections:

1. Purpose / Boundary
2. Inputs
3. Procedure
4. Outcome
5. Quality Conditions
6. Failure / Uncertainty
7. Dependencies, only when supplied
8. Evidence Rules, only when supplied
9. Constraints, only when supplied

The Builder must not add tools, memory, routing, lifecycle, registry, or automation unless explicitly represented by the input.

## Evidence boundary

The output is `OFFLINE-MOCK` evidence. It demonstrates deterministic generation only. It does not demonstrate semantic quality of an arbitrary natural-language task and must never claim external execution.

## Relationship to existing safety net

Every V1 candidate remains subject to the existing Evaluator, Mutation Test, fixture semantics, and CI gates. Builder success is never equivalent to evaluator PASS.

## Promotion gate

V1 is promoted only after:

1. deterministic fixture generation succeeds;
2. malformed-input rejection is tested;
3. optional sections are shown to be non-invasive;
4. generated candidates pass the existing offline contract/evaluator suite where applicable;
5. regression evidence is recorded;
6. real LLM comparison is performed later when runtime access is available.
