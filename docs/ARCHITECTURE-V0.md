# Skill Architect — Architecture V0

**Status:** CORE CANDIDATE — PROVISIONALLY PROMOTED

## 1. Purpose

Skill Architect is a meta-skill engineering system for designing, generating, testing, reviewing, refactoring, versioning, and composing AI Skills.

It is not itself a domain Skill. It is the engineering layer used to create and maintain domain Skills.

## 2. Core principles

1. Define the task boundary before writing a Skill.
2. Specify the Skill's semantic contract, but do not force a universal document template.
3. Separate knowledge, procedure, constraints, expected results, and evaluation criteria where those concerns are meaningfully distinct.
4. A documented rule is not automatically a validated rule.
5. Meaningful Skill revisions should be testable and evaluated for unintended effects.
6. Prefer the smallest justified change when a localized failure has a localized cause; broader redesign is allowed when evidence shows the architecture itself is inadequate.
7. External material is evidence/reference, not automatically authoritative project rules.
8. Experimental behavior must not silently become stable behavior.
9. A Skill should define how it handles relevant uncertainty and missing information rather than silently inventing facts.
10. Responsibilities should have clear ownership; avoid multiple conflicting authoritative definitions of the same rule.
11. Skills should be composable without requiring one giant universal Skill.
12. Architecture rules must earn their place through general applicability, evidence, or clearly stated design necessity. A rule is not included merely because it was useful in one domain project.
13. Complexity should be proportional to the Skill's actual behavior, risk, dependencies, and maintenance needs.

## 3. Core Skill Contract

A Skill must specify the following semantically, in whatever representation is appropriate for that Skill and host:

### 3.1 Boundary / Purpose
What the Skill is for, what task or state it is responsible for, and any meaningful activation or scope limits.

### 3.2 Inputs / Required State
What information, state, context, resources, or capabilities the Skill relies on. This does not imply that the user must provide explicit input fields.

### 3.3 Intended Outcome / Observable Result
What successful execution is intended to accomplish. For artifact-producing Skills this may be an output; for action or routing Skills it may be a state change, action, or correct dispatch.

### 3.4 Quality / Success Conditions
What makes the result acceptable, correct, or fit for purpose. The level of detail should be proportional to the task.

### 3.5 Failure / Uncertainty Behavior
What the Skill should do when information, capability, context, or confidence is insufficient. It must not silently fabricate successful completion.

These are semantic requirements, not mandatory Markdown headings.

## 4. Optional capabilities

The following may be added when justified by the Skill:

- Evidence / provenance
- Tools / environment / capability requirements
- Intermediate state or artifacts
- Routing / composition
- External references or resources
- Validation / regression mechanisms
- Specialized constraints or policies

An optional capability becomes part of a Skill's effective contract when that Skill depends on it. Optional does not mean informal; a dependency that materially affects execution should be specified clearly.

## 5. Lifecycle

`DRAFT → EXPERIMENTAL → TESTING → REVIEW → REGRESSION → STABLE`

This is a reference lifecycle, not an obligatory bureaucracy for every Skill. The amount of process should scale with complexity, risk, change magnitude, and evidence needs.

Material changes to a stable Skill should produce a distinguishable candidate version and preserve the recoverability of the prior stable version until the new candidate is accepted.

## 6. Evaluation model

Evaluation should be designed around the Skill's actual behavior and claims.

Possible evaluation classes include:

- normal expected use;
- edge or ambiguity cases;
- demanding/stress cases;
- previously successful cases rerun after meaningful changes;
- capability/tool failure cases;
- domain-specific adversarial or safety cases where relevant.

No fixed number or universal set of tests is required. The Skill's claims and risk should justify its evaluation coverage.

A useful evaluation record distinguishes, where applicable:

- expected behavior;
- observed behavior;
- evidence;
- judgment;
- remediation or next experiment.

## 7. Failure model

The architecture provides categories as a starting vocabulary, not a permanent universal taxonomy:

- wrong trigger / scope;
- incorrect task interpretation;
- unsupported factual claims or fabrication;
- omitted requirements;
- expected-result violation;
- quality/success-condition violation;
- constraint conflict;
- unnecessary rule expansion / redundancy;
- tool or dependency failure;
- input/context capacity problems;
- unstable behavior across repeated runs.

Skill-specific failure modes may be added when justified.

## 8. Change discipline

For a demonstrated failure, when practical:

1. reproduce or document the failure;
2. identify the smallest plausible root cause;
3. choose the narrowest justified change;
4. rerun the relevant evaluation;
5. evaluate relevant prior behavior for regression;
6. record the change and evidence.

A broader redesign is appropriate when evidence shows that a localized fix would not address the underlying problem.

## 9. Evidence boundary

Sources may include user workflows, successful outputs, failed outputs, external repositories, documentation, experiments, and expert guidance.

Source material must not be promoted directly into authoritative rules. Promotion requires an explicit design decision and, where practical, validation evidence.

Domain-specific lessons may be retained as case studies without becoming universal architecture rules.

## 10. Architecture responsibilities

The architecture distinguishes these responsibilities conceptually:

- Intent: what the user wants.
- Control: boundaries, priorities, constraints, and change policy.
- Knowledge: reusable domain knowledge and references.
- Execution: the Skill procedure.
- Evaluation: tests, quality criteria, and failure analysis.
- Registry: version, status, dependencies, and discoverability.
- Composition: routing and workflow across multiple Skills.

These are conceptual responsibilities. A particular Skill or repository does not need seven separate files, sections, or runtime layers.

## 11. Architecture admission rule

Before adding a new core architecture rule, ask:

1. Is the problem cross-domain rather than domain-specific?
2. Does the rule have independent evidence, clear design necessity, or repeated observations across different Skill types?
3. Can its benefit or necessity be evaluated?
4. Is there a simpler existing mechanism that already covers it?
5. Would removing it create a meaningful capability or reliability loss?
6. Does the rule impose complexity disproportionate to the problem it solves?

If the answer is unclear, keep the idea as an experiment, case study, or open design question rather than promoting it to a core rule.

## 12. Evidence basis for this revision

This revision is based on:

- cross-domain conceptual tests covering writing, code review, information synthesis, tool-using work, and multi-step transformation;
- examination of real Skill artifacts from independent public ecosystems;
- explicit counterexample/falsification attempts against the candidate core;
- the finding that semantic requirements generalize better than fixed document structures, universal workflows, or universal test suites.

This evidence is still limited and does not constitute a statistical survey of all Skills. The status is therefore provisionally promoted, not final or immutable.

## 13. Current scope

This version defines the core semantic contract and architectural boundaries. It does not yet define production implementations of Builder, Reviewer, Tester, or Orchestrator.

The next work should test this provisionally promoted core against additional real Skill artifacts and platform-specific Skill specifications, then refine only where new evidence exposes a weakness.
