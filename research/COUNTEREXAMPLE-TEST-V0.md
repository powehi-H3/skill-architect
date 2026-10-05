# Counterexample Test V0

**Status:** EXPERIMENTAL RESEARCH
**Purpose:** Try to falsify the current candidate Core Contract rather than merely confirm it.

## Candidate Core under test

1. Boundary / purpose
2. Input expectations
3. Intended outcome
4. Output expectations
5. Quality expectations
6. Failure / uncertainty handling

Evidence/provenance, capabilities/environment, intermediate state, routing/composition, external resources, and validation remain optional candidates.

## Falsification questions

A concept should NOT become core merely because it is common. We ask whether a real Skill can be useful while lacking that concept, or whether forcing it causes distortion.

### 1. Boundary / purpose

Counterexample attempt: a tiny utility Skill whose invocation itself fully defines the task.

Result: Even when the Skill is tiny, there remains an implicit purpose and scope. The concept may be extremely short, but removing it entirely makes activation and expected behavior ambiguous.

Status: **Survives, but must allow minimal expression.**

### 2. Input expectations

Counterexample attempt: a Skill that requires no user-provided input and operates only from fixed environment state.

Result: A conventional "input" section may be unnecessary. However, the Skill still has an effective input/environment contract. Therefore the core concept should mean "what information/state the Skill relies on", not "the user must provide fields".

Status: **Survives after generalization.**

### 3. Intended outcome

Counterexample attempt: a routing/dispatcher Skill whose immediate job is to select another Skill rather than produce a final artifact.

Result: It still has an intended outcome: selecting/dispatching appropriately.

Status: **Survives.**

### 4. Output expectations

Counterexample attempt: a Skill whose purpose is an action rather than a user-visible artifact, such as changing a configuration or invoking a tool.

Result: A conventional output format may not exist, but there is still an expected result/state change and success condition. Therefore "output expectations" must be generalized to "expected observable result".

Status: **Survives after generalization.**

### 5. Quality expectations

Counterexample attempt: a deterministic wrapper around one exact command where correctness is almost entirely delegated to the underlying tool.

Result: Quality may be represented as a simple success/failure condition rather than a rich rubric. The concept remains useful, but must not require a lengthy quality section.

Status: **Survives, with minimality requirement.**

### 6. Failure / uncertainty handling

Counterexample attempt: a trivial deterministic Skill with no meaningful ambiguity or known failure branch beyond the underlying tool's normal error.

Result: The Skill does not need elaborate failure prose. But it still needs a behavior when required capability is unavailable or execution fails, even if that behavior is simply to report the failure rather than fabricate success.

Status: **Survives as a minimal failure contract, not a mandatory error catalogue.**

## Strongest falsification result

The test did NOT find a convincing counterexample that eliminates the six concepts entirely.

However, it found a more important constraint:

> **The Core Contract must describe semantics, not force document sections.**

For example:

- "Input expectations" does not require an `## Input` heading.
- "Output expectations" does not require a textual output format.
- "Quality expectations" does not require a checklist.
- "Failure handling" does not require a troubleshooting table.

The architecture defines what a Skill needs to specify, while leaving the representation proportional to the Skill.

## Current verdict

**Candidate Core survives this falsification round, but only in generalized semantic form.**

No promotion to final/core architecture is made by this document alone. The finding should be compared against independent real Skill artifacts and platform specifications before promotion.

## Anti-overfitting rule

Do not convert the six semantic concepts into six mandatory Markdown headings unless independent evidence demonstrates that a fixed document structure materially improves interoperability or reliability.
