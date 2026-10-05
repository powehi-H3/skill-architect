# Skill Reviewer V0

**Status:** DESIGN / CANDIDATE
**Independence requirement:** Reviewer must not merely echo Builder rules.

## Purpose
Evaluate an existing or newly generated Skill against its stated task contract and observable evidence. The Reviewer judges the Skill; it does not rewrite it automatically.

## Review protocol

### 1. Establish the review target
Identify:
- Skill version / commit when available;
- stated purpose and trigger;
- intended task;
- inputs and expected outputs;
- explicit constraints;
- available evidence.

If the target cannot be identified, return NEEDS REVISION rather than inventing scope.

### 2. Reconstruct the Skill contract
Extract what the Skill actually claims to do. Do not assume a generic Skill template is required.

### 3. Check six independent dimensions
1. **Scope integrity** — trigger and boundary are specific enough to distinguish intended use from unrelated use.
2. **Execution adequacy** — instructions are sufficient to perform the stated task.
3. **Output contract** — result format and observable success are defined where needed.
4. **Failure / uncertainty** — missing, conflicting, unsupported, or unavailable inputs have honest behavior.
5. **Preservation / semantic integrity** — requested behavior is not silently altered by examples, formatting, or local edits.
6. **Proportionality** — architecture and rules are justified by task complexity, risk, and maintenance needs.

### 4. Evidence discipline
For every material finding, distinguish:
- directly observed text;
- verified execution evidence;
- logical implication;
- reviewer inference;
- unresolved uncertainty.

Never claim runtime success from static inspection alone.

### 5. Adversarial review
Attempt to falsify the Skill using at least:
- missing required input;
- ambiguous request;
- conflicting constraints;
- misleading reference material;
- unavailable capability;
- local-change semantic trap;
- excessive or irrelevant context when applicable.

### 6. Decision
Return exactly one primary status:

- **PASS** — no material defect established under the tested evidence level.
- **NEEDS REVISION** — one or more material weaknesses are identified, but the Skill remains structurally salvageable.
- **FAIL** — the Skill cannot reliably satisfy its stated contract or violates a critical evidence/safety/integrity boundary.
- **UNKNOWN** — evidence is insufficient to make a defensible judgment.

### 7. Findings
Every finding should contain:
- Finding ID;
- severity: critical / major / minor / informational;
- observed evidence;
- violated invariant;
- impact;
- confidence;
- minimal recommended repair direction.

The Reviewer must not silently implement the repair unless explicitly asked.

## Anti-echo requirements
The Reviewer must:

- test the Skill against its own claims, not against the Builder's preferred wording;
- permit a well-designed Skill to differ from Builder templates;
- identify when a Builder rule is unnecessary for the reviewed task;
- reject unsupported claims even if they match project terminology;
- preserve UNKNOWN when evidence is inadequate.

## Reviewer test contract
Before Reviewer V0 can become Stable, test it against:

1. clearly good small Skill;
2. good complex Skill;
3. ambiguous Skill;
4. overengineered Skill;
5. hallucination-prone Skill;
6. local-edit regression;
7. evidence-boundary violation;
8. intentionally misleading Skill that matches superficial checklist terms.

## Promotion gate
Reviewer V0 remains a candidate until it demonstrates that it can disagree with the Builder and correctly identify a seeded defect without relying on Builder-generated labels.
