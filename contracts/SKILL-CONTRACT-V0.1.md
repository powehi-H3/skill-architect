# Skill Contract V0.1

**Status:** DESIGN BASELINE
**Parent:** `docs/ARCHITECTURE-V0.md`

## 1. Purpose

The Skill Contract defines the minimum information a Skill must declare so that its scope, execution, output, failure behavior, and testability are explicit.

This is a contract for Skill design, not a universal requirement that every field must appear verbatim inside a runtime `SKILL.md`.

## 2. Identity

Every Skill MUST have:

- `name`: stable unique identifier within the Skill library.
- `version`: explicit version using the project's chosen versioning scheme.
- `status`: one of `DRAFT`, `EXPERIMENTAL`, `TESTING`, `STABLE`, `DEPRECATED`, `RETIRED`.
- `description`: concise statement of what the Skill does and its intended trigger boundary.

## 3. Trigger and boundary

A Skill MUST define:

- when it SHOULD be invoked;
- when it SHOULD NOT be invoked;
- the minimum conditions required to begin execution;
- any known ambiguity that requires clarification or a safe fallback.

A description is not sufficient if it only names the task. It must establish a usable boundary.

## 4. Purpose and success condition

A Skill MUST state:

- the task outcome it is responsible for;
- what counts as successful completion;
- important non-goals.

Success must be observable or testable where practical.

## 5. Input contract

A Skill MUST define:

- accepted input types/materials;
- required inputs;
- optional inputs;
- how missing information is handled;
- whether external tools, files, references, or prior state are required.

A Skill MUST NOT silently invent missing facts merely to satisfy an output format.

## 6. Execution contract

A Skill MUST define the procedure needed to transform valid inputs into the intended output.

The procedure should identify, where relevant:

1. intake / interpretation;
2. input validation;
3. task decomposition;
4. core processing;
5. internal checks;
6. output construction.

Internal control terminology may be used by the engineering system but should not be leaked into a domain Skill's user-facing output unless required by that Skill.

## 7. Output contract

A Skill MUST define:

- output type or structure;
- required sections/fields when applicable;
- formatting constraints;
- what must not appear in the output;
- whether uncertainty or missing information must be surfaced.

The output contract should be specific enough to test.

## 8. Quality contract

A Skill MUST define the principal quality criteria that distinguish a successful result from a merely plausible result.

Criteria should be prioritized when they can conflict, for example:

- correctness;
- requirement coverage;
- factual grounding;
- consistency;
- format compliance;
- minimality / non-redundancy;
- robustness.

Do not create a long checklist unless each item has a meaningful evaluation purpose.

## 9. Failure contract

A Skill MUST define expected handling for relevant failure classes, including as applicable:

- insufficient input;
- ambiguous input;
- conflicting requirements;
- uncertain facts;
- unavailable tools/dependencies;
- oversized input/context;
- failed execution;
- output validation failure.

Failure handling should prefer explicit uncertainty, clarification, partial completion, or safe fallback over fabrication.

## 10. Test contract

A Skill MUST have a minimal test set before it can be promoted to `STABLE`.

The minimum test classes are:

- `NORMAL`: expected valid task;
- `EDGE`: missing, ambiguous, conflicting, or unusual input;
- `STRESS`: complex, long, multi-constraint, or otherwise demanding input;
- `REGRESSION`: previously passing cases rerun after a meaningful change.

Each test should specify expected observable behavior rather than merely asserting that the output “looks good.”

## 11. Evidence and provenance

A Skill may use:

- user-provided requirements;
- observed successful/failed outputs;
- project knowledge;
- external documentation or repositories;
- experiments;
- expert guidance.

External material is not automatically authoritative. A promoted rule should record its source and, where practical, validation evidence.

## 12. Version and change requirements

A meaningful Skill change MUST identify:

- what changed;
- why it changed;
- which failure, requirement, or evidence motivated it;
- which tests were rerun;
- whether previously passing behavior was preserved.

A broad rewrite should not be used as the default response to a localized failure.

## 13. Promotion gate

A Skill SHOULD NOT enter `STABLE` merely because its document is complete.

Minimum promotion evidence:

1. trigger boundary is usable;
2. required inputs and failure handling are defined;
3. output contract is testable;
4. normal, edge, and stress tests have been executed;
5. known failures are recorded;
6. relevant regression tests pass after the latest change;
7. no unresolved critical defect is being hidden by documentation.

Exact quantitative thresholds remain V0.1 design work and must be defined after real test data exists.

## 14. Separation of concerns

The following responsibilities should not have duplicate authoritative owners:

- Skill definition;
- domain knowledge;
- execution procedure;
- testing;
- review/judgment;
- version/status management.

Supporting references may duplicate information for usability, but only one source should be authoritative for a given rule.

## 15. Contract status

This contract is `DESIGN BASELINE` and is not yet a finalized universal schema. It should be validated against the first real Meta-Skills before V1.
