# Skill Contract V0.1

**Status:** DESIGN BASELINE
**Parent:** `docs/ARCHITECTURE-V0.md`

## 1. Purpose

The Skill Contract defines the minimum information a Skill should declare so that its scope, execution, output, failure behavior, and evaluation are explicit.

This is a design contract, not a requirement that every field appear verbatim inside a runtime `SKILL.md`.

## 2. Identity

A Skill SHOULD have:

- `name`: stable identifier within its Skill library.
- `version`: explicit version using the project's chosen scheme.
- `status`: lifecycle state recorded by the project registry.
- `description`: concise statement of what the Skill does and its intended trigger boundary.

The exact metadata schema may evolve with the registry design.

## 3. Trigger and boundary

A Skill SHOULD define:

- when it should be invoked;
- when it should not be invoked;
- the minimum conditions required to begin execution;
- known ambiguity that requires clarification or a safe fallback.

A description is insufficient if it only names the task; it should establish a usable boundary.

## 4. Purpose and success condition

A Skill SHOULD state:

- the task outcome it is responsible for;
- what counts as successful completion;
- important non-goals.

Success should be observable or testable where practical.

## 5. Input contract

A Skill SHOULD define:

- accepted input types/materials;
- required inputs;
- optional inputs;
- how missing information is handled;
- whether external tools, files, references, or prior state are required.

A Skill should not silently invent missing facts merely to satisfy an output format.

## 6. Execution contract

A Skill SHOULD define the procedure needed to transform valid inputs into the intended output.

The procedure may identify, where relevant:

1. intake / interpretation;
2. input validation;
3. task decomposition;
4. core processing;
5. internal checks;
6. output construction.

The exact procedure should fit the task. Irrelevant stages should not be added merely to satisfy a template.

## 7. Output contract

A Skill SHOULD define:

- output type or structure;
- required sections/fields when applicable;
- formatting constraints;
- what must not appear in the output;
- whether uncertainty or missing information must be surfaced.

The output contract should be specific enough to evaluate.

## 8. Quality contract

A Skill SHOULD define the principal quality criteria that distinguish a successful result from a merely plausible result.

Criteria may include, when relevant:

- correctness;
- requirement coverage;
- factual grounding;
- consistency;
- format compliance;
- minimality / non-redundancy;
- robustness.

Do not create a long checklist unless each item has a meaningful evaluation purpose.

## 9. Failure contract

A Skill SHOULD define handling for failure classes relevant to its task, such as:

- insufficient input;
- ambiguous input;
- conflicting requirements;
- uncertain facts;
- unavailable tools/dependencies;
- oversized input/context;
- failed execution;
- output validation failure.

Failure handling should prefer explicit uncertainty, clarification, partial completion, or a safe fallback over fabrication when those are appropriate to the task.

## 10. Test contract

A Skill must have an evaluation plan sufficient to support its claims before it can be promoted to `STABLE`.

Common test classes are:

- `NORMAL`: expected valid task;
- `EDGE`: missing, ambiguous, conflicting, or unusual input;
- `STRESS`: complex, long, multi-constraint, or otherwise demanding input;
- `REGRESSION`: previously passing cases rerun after a meaningful change.

Not every Skill requires all four classes in identical form. The test plan should justify which cases are necessary for that Skill's behavior and risk.

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

A domain-specific lesson may remain a case study without becoming a universal architecture rule.

## 12. Version and change requirements

A meaningful Skill change SHOULD identify:

- what changed;
- why it changed;
- which failure, requirement, or evidence motivated it;
- which relevant tests were rerun;
- whether important prior behavior was preserved or intentionally changed.

A broad rewrite should not be the default response to a localized failure, but the contract must allow redesign when evidence shows that a local fix is inadequate.

## 13. Promotion gate

A Skill SHOULD NOT enter `STABLE` merely because its document is complete.

Promotion evidence should establish, as appropriate to the Skill:

1. trigger boundary is usable;
2. required inputs and failure handling are defined;
3. output contract is evaluable;
4. relevant evaluation cases have been executed;
5. known failures and limitations are recorded;
6. relevant regression checks pass after meaningful changes;
7. no unresolved critical defect is being hidden by documentation.

There are no universal numeric pass thresholds in V0.1; those must be justified by Skill class and real evidence.

## 14. Separation of concerns

The following responsibilities should have clear ownership:

- Skill definition;
- domain knowledge;
- execution procedure;
- testing;
- review/judgment;
- version/status management.

Supporting references may repeat information for usability, but conflicting authoritative definitions should be avoided.

## 15. Contract status

This contract is `DESIGN BASELINE` and is not a finalized universal schema. It must be validated against multiple unrelated Skill types before V1.
