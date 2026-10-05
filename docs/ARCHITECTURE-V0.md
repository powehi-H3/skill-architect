# Skill Architect — Architecture V0

**Status:** DESIGN BASELINE

## 1. Purpose

Skill Architect is a meta-skill engineering system for designing, generating, testing, reviewing, refactoring, versioning, and composing AI Skills.

It is not itself a domain Skill. It is the engineering layer used to create and maintain domain Skills.

## 2. Core principles

1. Define the task boundary before writing a Skill.
2. Separate knowledge, procedure, constraints, output contract, and evaluation criteria where those concerns are meaningfully distinct.
3. A documented rule is not automatically a validated rule.
4. Meaningful Skill revisions should be testable and evaluated for unintended effects.
5. Prefer the smallest justified change when a localized failure has a localized cause; broader redesign is allowed when evidence shows the architecture itself is inadequate.
6. External material is evidence/reference, not automatically authoritative project rules.
7. Experimental behavior must not silently become stable behavior.
8. A Skill should define how it handles relevant uncertainty and missing information rather than silently inventing facts.
9. Responsibilities should have clear ownership; avoid multiple conflicting authoritative definitions of the same rule.
10. Skills should be composable without requiring one giant universal Skill.
11. Architecture rules must earn their place through general applicability, evidence, or clearly stated design necessity. A rule is not included merely because it was useful in one domain project.

## 3. Skill lifecycle

`DRAFT → EXPERIMENTAL → TESTING → REVIEW → REGRESSION → STABLE`

Material changes to a stable Skill create a new candidate version; the prior stable version remains recoverable until the candidate is accepted.

A Skill may remain Experimental when evidence is insufficient for Stable status.

## 4. Core system roles

### Analyst
Determines whether a repeated task is suitable for Skill化 and defines its boundary, inputs, outputs, and recurring failure modes.

### Distiller
Extracts reusable knowledge, procedures, constraints, examples, evidence, and failure patterns from source material.

### Architect
Designs the Skill contract, execution model, dependencies, references, tests, and quality criteria before implementation.

### Builder
Produces the Skill package from an approved architecture. Builder is not the final quality authority.

### Tester
Runs the defined evaluation suite against a Skill and records observable evidence.

### Reviewer
Evaluates evidence and determines whether the Skill's claims, boundaries, and quality criteria are supported.

### Refactorer
Applies justified changes based on requirements or evidence while preserving unaffected behavior where preservation is appropriate.

### Registry / Orchestrator
Tracks versions, status, dependencies, capabilities, known limitations, and selects or composes Skills for larger workflows.

## 5. Skill contract — preliminary

A Skill should define, at minimum:

- identity and trigger boundary
- purpose
- expected inputs
- execution procedure
- output contract
- quality criteria
- failure handling
- an appropriate test plan

The exact contract may vary by Skill type; the architecture must not force irrelevant fields merely for uniformity.

## 6. Evaluation model

A Skill's evaluation suite should include test types appropriate to its risk and behavior. Common classes include:

- Normal: expected valid task.
- Edge: missing, ambiguous, conflicting, or unusual input.
- Stress: complex, long, multi-constraint, or otherwise demanding input.
- Regression: previously passing cases rerun after a meaningful change.

Not every Skill requires identical tests or identical quantities. The Skill's contract should justify the tests needed to support its claims.

A test result should distinguish observed behavior, expected behavior, judgment, and proposed remediation.

## 7. Failure model

Initial cross-domain failure categories include:

- wrong trigger / wrong scope
- missing or incorrect task interpretation
- unsupported factual claims or fabrication
- omitted requirements
- output contract violation
- quality-criteria violation
- constraint conflict
- unnecessary rule expansion / redundancy
- tool or dependency failure
- input/context capacity problems
- unstable behavior across repeated runs

The taxonomy is intentionally V0 and must evolve from evidence rather than speculation.

## 8. Change discipline

For a demonstrated failure:

1. reproduce or document the failure;
2. identify the smallest plausible root cause;
3. choose the narrowest justified change when practical;
4. rerun the relevant evaluation;
5. evaluate relevant prior behavior for regression;
6. record the change and its evidence.

A broad redesign is appropriate when evidence shows that a localized fix would not address the underlying problem.

## 9. Evidence boundary

Sources may include user workflows, successful outputs, failed outputs, external repositories, documentation, experiments, and expert guidance.

Source material must not be promoted directly into authoritative rules. Promotion requires an explicit design decision and, where practical, validation evidence.

Domain-specific lessons may be retained as case studies without becoming universal architecture rules.

## 10. Architecture layers

- Intent: what the user wants.
- Control: boundaries, priorities, constraints, and change policy.
- Knowledge: reusable domain knowledge and references.
- Execution: the Skill procedure.
- Evaluation: tests, quality criteria, and failure analysis.
- Registry: version, status, dependencies, and discoverability.
- Composition: routing and workflow across multiple Skills.

These are conceptual responsibilities, not a requirement that every Skill or repository contain seven separate runtime layers.

## 11. Architecture admission rule

Before adding a new core architecture rule, ask:

1. Is the problem cross-domain rather than domain-specific?
2. Does the rule have independent evidence, clear design necessity, or repeated observations across different Skill types?
3. Can its benefit or necessity be evaluated?
4. Is there a simpler existing mechanism that already covers it?
5. Would removing it create a meaningful capability or reliability loss?

If the answer is unclear, keep the idea as an experiment, case study, or open design question rather than promoting it to a core rule.

## 12. Current scope

V0 defines architecture and contracts only. It does not yet define the final Builder, Reviewer, Tester, or Orchestrator implementations.

The next design work should formalize test evidence and evaluation records, then validate the architecture against multiple unrelated Skill types before creating production Meta-Skills.
