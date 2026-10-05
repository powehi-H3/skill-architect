# Cross-Domain Validation V1

**Status:** EXPERIMENTAL RESEARCH
**Purpose:** Extend cross-domain validation to tool-using and multi-step Skills before promoting any principle to core architecture.

## D — Tool-using Skill

Representative task: inspect a repository, locate relevant files, analyze evidence, and return a grounded change recommendation.

### What the architecture must express
- scope/boundary: what sources and operations are in scope;
- inputs: user goal plus available repository/tool context;
- intended outcome: an evidence-grounded result;
- output: findings/recommendations with source references when relevant;
- quality: correctness, evidence grounding, and clear separation between observed facts and inference;
- failure: unavailable tool, inaccessible source, incomplete context, conflicting evidence, or operation failure.

### Result
The core contract still fits.

### New requirement revealed
A Skill may depend on **capabilities/environment** that are neither ordinary user inputs nor part of the Skill's text. Therefore capability requirements should be representable as an optional contract component.

This does not justify making tools mandatory for Skills generally.

## E — Multi-step transformation Skill

Representative task: source material → analysis → structured plan → draft → quality check → final artifact.

### What the architecture must express
- scope and desired final outcome;
- source/input requirements;
- intermediate transformations where they materially affect correctness;
- final output contract;
- quality checks appropriate to the artifact;
- failure handling at the point where an intermediate step lacks sufficient information.

### Result
The core contract still fits.

### New requirement revealed
A Skill may have meaningful **intermediate artifacts/state**. The architecture should allow them when needed, but must not force every Skill to expose or persist intermediate stages.

## Cross-domain result

The five validation domains now cover:

1. writing;
2. code review;
3. information synthesis;
4. tool-using work;
5. multi-step transformation.

The same small conceptual core remains usable:

```text
Boundary / purpose
Input expectations
Intended outcome
Output expectations
Quality criteria
Failure / uncertainty handling
Evidence where relevant
Optional capabilities / environment
Optional intermediate state
```

## What still should NOT become universal

- mandatory tools;
- mandatory intermediate stages;
- one universal execution pipeline;
- one universal output schema;
- one fixed testing recipe;
- lifecycle overhead unrelated to the Skill's complexity or risk.

## Current confidence

**Provisional:** the contract core appears broadly applicable across the tested task families.

This is not yet sufficient to declare a final architecture. The next step should test the proposed core against real Skill artifacts from independent ecosystems and record concrete friction points rather than relying only on abstract examples.

## Promotion rule

No finding in this document is automatically promoted to CORE ARCHITECTURE. Promotion requires evidence that the concept is useful across multiple independent Skill implementations and does not introduce disproportionate complexity.
