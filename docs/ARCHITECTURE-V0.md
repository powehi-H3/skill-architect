# Skill Architect — Architecture V0

**Status:** DESIGN BASELINE

## 1. Purpose

Skill Architect is a meta-skill engineering system for designing, generating, testing, reviewing, refactoring, versioning, and composing AI Skills.

It is not itself a domain Skill. It is the engineering layer used to create and maintain domain Skills.

## 2. Core principles

1. Define the task boundary before writing a Skill.
2. Separate knowledge, procedure, constraints, output contract, and evaluation criteria.
3. A documented rule is not automatically a validated rule.
4. Every meaningful Skill revision should be testable and regression-aware.
5. Prefer the smallest change that fixes a demonstrated failure.
6. External material is evidence/reference, not automatically authoritative project rules.
7. Experimental behavior must not silently become stable behavior.
8. A Skill must have explicit failure handling rather than inventing missing information.
9. Roles and responsibilities must have single ownership; avoid duplicated authority.
10. Skills should be composable without requiring one giant universal Skill.

## 3. Skill lifecycle

Draft → Test → Review → Refactor → Regression Test → Stable → Iterate

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
Runs normal, edge, stress, and later regression cases against a Skill.

### Reviewer
Evaluates observed failures and determines whether the root cause is scope, trigger, procedure, output contract, quality criteria, failure handling, knowledge, or model variance.

### Refactorer
Applies the minimum justified change and preserves unaffected behavior.

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
- test cases

Advanced Skills may additionally define examples, references, scripts, tools, dependencies, evidence, version history, and regression suites.

## 6. Testing model

Minimum test classes:

- Normal: expected valid input.
- Edge: missing, ambiguous, conflicting, or unusual input.
- Stress: long, complex, multi-constraint, or adversarial workload.
- Regression: previously passing cases rerun after a change.

A test result should distinguish observed behavior from interpretation and from proposed remediation.

## 7. Failure model

Initial failure categories:

- wrong trigger / wrong scope
- missing or incorrect task interpretation
- fabricated information under insufficient input
- omitted requirements
- output contract violation
- quality-criteria violation
- constraint conflict
- unnecessary rule expansion / redundancy
- tool or dependency failure
- context-length degradation
- unstable behavior / model variance

The taxonomy is intentionally V0 and must evolve from evidence rather than speculation.

## 8. Change discipline

For a demonstrated failure:

1. reproduce or document the failure;
2. identify the smallest plausible root cause;
3. change one primary mechanism where practical;
4. rerun the failing test;
5. run relevant regression tests;
6. record the change and its evidence.

Do not rewrite a whole Skill merely because one test failed.

## 9. Evidence boundary

Sources may include user workflows, successful outputs, failed outputs, external repositories, documentation, experiments, and expert guidance.

Source material must not be promoted directly into authoritative rules. Promotion requires an explicit decision and, where practical, validation evidence.

## 10. Architecture layers

- Intent: what the user wants.
- Control: boundaries, priorities, constraints, and change policy.
- Knowledge: reusable domain knowledge and references.
- Execution: the Skill procedure.
- Evaluation: tests, quality criteria, and failure analysis.
- Registry: version, status, dependencies, and discoverability.
- Composition: routing and workflow across multiple Skills.

## 11. Current scope

V0 defines architecture and contracts only. It does not yet define the final Builder, Reviewer, Tester, or Orchestrator implementations.

Next design work should formalize the Skill Contract, lifecycle state transitions, test schema, failure schema, and evidence/promotion model before creating production Meta-Skills.
