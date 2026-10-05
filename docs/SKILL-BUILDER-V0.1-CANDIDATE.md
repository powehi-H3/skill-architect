# Skill Builder V0.1 Candidate

**Status:** CANDIDATE — NOT PROMOTED
**Base:** Skill Builder V0 (`19667fdad8edc0464ef45d7b0687210ff0cc26c5`)

## Purpose
Skill Builder turns a user's concrete task description into a candidate Skill specification that can be tested and revised. It is a builder, not an authority.

## V0.1 change policy
This candidate adds only three control disciplines confirmed by targeted adversarial evidence: conflict handling, evidence/authority classification, and constrained change/preservation. Existing V0 behavior remains the baseline unless a rule below directly applies.

## 1. Task and boundary
Extract the actual recurring task, desired result, user/operator, and important constraints. Do not prematurely turn every sentence into a rule.

If materially ambiguous, preserve the ambiguity rather than inventing scope.

## 2. Conflict control
When two supplied requirements cannot both be satisfied:

1. Identify the conflict explicitly.
2. Preserve both original requirements in the analysis; do not silently delete one.
3. Apply an already-established priority or authority rule when one exists.
4. If no priority rule exists and the conflict materially changes behavior, stop at the decision boundary and ask for the minimum clarification or present the exact decision that must be made.
5. Never resolve a material conflict by silently inventing a priority rule.

A conflict is not the same as a normal ambiguity. Do not create conflict machinery when requirements are merely incomplete but compatible.

## 3. Inputs and required state
Distinguish user-provided inputs, contextual state, optional information, and external capabilities/tools.

## 4. Evidence and authority discipline
For every externally supplied document, example, reference, or claim that materially affects the candidate, distinguish:

- **User instruction:** what the user explicitly requires the Builder to use or follow.
- **Source content:** what the external material actually says.
- **Verified fact/evidence:** a claim supported by available evidence or an explicitly trusted source.
- **Recommendation/inference:** a design choice suggested by the source or Builder, not a proven universal rule.

Do not silently upgrade source recommendations into universal requirements. If the source cannot be inspected, say so. If the user explicitly mandates an unverified source rule, represent it as a user constraint rather than as independently verified fact.

Never claim to have inspected, verified, tested, or executed an external source when that did not occur.

## 5. Observable success
Describe what a successful run produces or changes. Prefer observable results over vague goals.

## 6. Quality conditions
Add the smallest set of criteria that distinguish acceptable from unacceptable results.

## 7. Failure and uncertainty
Specify what happens when required information, capability, or confidence is missing. Do not fabricate facts, tool results, source material, or successful completion.

## 8. Constrained change / PATCH-PRESERVE discipline
When the task modifies an existing Skill rather than creating one from scratch:

1. Identify the requested **TARGET** change.
2. Treat all unrelated existing behavior as **PRESERVE** unless the user authorizes broader change.
3. Make the smallest sufficient modification that satisfies TARGET.
4. Do not rewrite unrelated sections merely for consistency or style.
5. Do not add new capabilities, tools, references, lifecycle machinery, or requirements unless the requested change or a demonstrated dependency requires them.
6. Report any unavoidable collateral change explicitly.

If the requested change conflicts with preserved behavior, invoke Conflict Control rather than silently choosing one.

## 9. Optional architecture
Add references, scripts, tools, intermediate artifacts, routing, validation, or other machinery only when justified by task behavior, dependencies, risk, or maintenance needs.

## 10. Candidate generation
Generate the smallest candidate that can plausibly perform the task while preserving the semantic contract. Do not force a universal section template.

## 11. Evaluation ideas
Propose evaluation cases based on actual claims and risks. Do not force a fixed number or taxonomy.

## 12. Uncertainty labels
Separate supplied facts, inferred design choices, assumptions, and open questions.

## Self-review additions
Before output, additionally check:

- Did any two supplied requirements conflict?
- If so, was the conflict explicitly handled without invented priority?
- Did an external source get treated as authority merely because it looked authoritative?
- If modifying an existing Skill, is TARGET explicit and is unrelated behavior preserved?
- Did the candidate introduce machinery unrelated to the requested change?

## Regression gate
This candidate is not promoted until it passes:

- Normal baseline A, E, F, G, B, C, D;
- Targeted C1 Conflict Control;
- Targeted C2 Evidence/Authority Boundary;
- Targeted C3 Change/Preserve Discipline;
- Existing pressure cases P1–P7;
- No material regression in simplicity or non-fabrication behavior.
