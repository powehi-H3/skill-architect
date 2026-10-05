# Builder Test Harness V0

**Status:** EXPERIMENTAL
**Purpose:** Define a reproducible separation between Builder generation, independent evaluation, evidence capture, and regression.

## 1. Why this exists

`SKILL-BUILDER-V0.md` defines Builder behavior. `BUILDER-BENCHMARK-V0.md` defines benchmark cases. This harness defines how those two are executed and evaluated without allowing the Builder to grade itself.

The harness is a protocol first, not a claim that automated runtime execution already exists.

## 2. Separation of responsibilities

### Builder
Produces a candidate Skill from a benchmark input.

The Builder must not decide that its own output passed.

### Evaluator
Assesses the candidate against the benchmark's expected properties and records observed failures.

The evaluator should not silently rewrite the candidate while evaluating it.

### Evidence record
Stores the input, candidate, evaluation, evidence, and disposition so later revisions can be compared.

### Regression runner
Re-executes affected prior cases after a Builder change.

## 3. Run unit

Each run should have a stable identifier and record:

- benchmark case ID;
- Builder version / commit;
- exact input;
- candidate Skill output;
- evaluation version;
- expected properties;
- observed properties;
- failures;
- severity;
- root-cause hypothesis;
- proposed change;
- regression set.

If a field cannot be known, mark it unknown. Do not reconstruct it from memory.

## 4. Evaluation protocol

For each benchmark case:

1. Start from a known Builder revision.
2. Provide only the case input and explicitly available context.
3. Capture the complete Builder result.
4. Freeze the candidate before evaluation.
5. Evaluate independently against the case's expected properties.
6. Separate direct observations from evaluator inference.
7. Classify each failure.
8. Decide whether the failure belongs to the Builder, the benchmark, the candidate Skill, or the environment.
9. If a Builder change is justified, describe the smallest plausible change.
10. Define which prior cases must be rerun.

## 5. Failure classification

Use these labels initially:

- `SCOPE` — wrong or invented boundary;
- `INPUT` — incorrect required-state/input model;
- `OUTCOME` — success is not observable or is materially wrong;
- `QUALITY` — insufficient or disproportionate quality criteria;
- `UNCERTAINTY` — missing, ambiguous, or fabricated failure behavior;
- `OVERENGINEERING` — unnecessary machinery or process;
- `EVIDENCE` — unsupported source/rule promotion;
- `CHANGE_DISCIPLINE` — unnecessary modification or loss of preserved behavior;
- `CAPABILITY` — tool/environment dependency mishandled;
- `HARNESS` — test or evaluator defect;
- `OTHER` — only when none of the above fits.

A failure may have more than one label, but identify one primary label.

## 6. Severity

Use:

- **S0 — critical:** candidate would materially misrepresent execution, evidence, safety, or task outcome.
- **S1 — major:** important requirement is missing/wrong or behavior is materially unreliable.
- **S2 — moderate:** meaningful quality or proportionality problem with a plausible localized fix.
- **S3 — minor:** wording, organization, or low-impact issue that does not materially change behavior.

Severity is about impact, not how easy the fix is.

## 7. Independent evaluator checklist

Before declaring a candidate successful, ask:

1. Does the boundary match the supplied task rather than evaluator assumptions?
2. Are required inputs/capabilities distinguishable from optional ones?
3. Is the intended result observable?
4. Are quality conditions sufficient and proportionate?
5. Does failure/uncertainty behavior avoid fabrication?
6. Did the candidate introduce machinery unsupported by the task?
7. Did external material become an unjustified authority?
8. If this was a change request, were unrelated behaviors preserved?
9. Are claims about tools or evidence grounded in what was actually available?
10. Is the failure, if any, in the Builder, candidate, benchmark, or environment?

## 8. Evidence standard

The harness distinguishes three levels:

### Observed
Directly present in the captured Builder output or execution result.

### Inferred
A reasoned interpretation supported by observed behavior.

### Unverified
A claim that has not been demonstrated by the run.

Only observed evidence should be used to claim that a behavior occurred in a specific run.

## 9. Regression policy

A Builder revision does not require rerunning every historical case automatically. It requires rerunning:

- the case that exposed the failure;
- cases exercising the same mechanism;
- cases exercising any behavior explicitly changed;
- representative minimal and complex cases when the change affects proportionality or architecture selection.

If the affected surface cannot be identified confidently, broaden the regression set rather than pretending the impact is known.

## 10. Current execution boundary

V0 deliberately does not pretend to provide a fully automated Builder runtime, sandbox, or scoring engine.

The current repository artifact is a reproducible test protocol. Actual execution can initially be performed manually or by an external runtime, provided the evidence record follows this protocol.

Automation may be added later only when it improves reproducibility without hiding evaluator judgment or creating false precision.

## 11. First run plan

Run the seven cases from `BUILDER-BENCHMARK-V0.md` in this order:

`A → E → F → G → B → C → D`

Rationale:

- A establishes the anti-overengineering baseline.
- E tests ambiguity before complexity is introduced.
- F tests evidence boundaries.
- G tests localized change discipline.
- B, C, and D then test ordinary, tool-dependent, and multi-step production cases.

Do not modify Builder V0 merely to improve a case before all seven cases have an initial observation record.

## 12. Promotion gate

No Builder version is promoted based on the harness existing.

Promotion requires captured runs, explicit failures, justified changes, and relevant regression evidence.
