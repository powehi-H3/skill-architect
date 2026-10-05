# Skill Builder V0.1 Candidate Regression — 001

**Status:** MANUAL REGRESSION COMPLETE — NOT A PROMOTION
**Candidate:** `docs/SKILL-BUILDER-V0.1-CANDIDATE.md`
**Base V0 SHA:** `19667fdad8edc0464ef45d7b0687210ff0cc26c5`
**Execution:** controlled manual emulation; independence LIMITED

## Objective

Check whether the minimal C1/C2/C3 patch addresses the confirmed weaknesses without introducing obvious regressions in the previously passing baseline behavior.

## Targeted cases

### C1 Conflict Control — PASS (manual emulation)

The candidate now requires explicit conflict identification, preservation of both requirements, use of an existing priority rule when one exists, and clarification at the decision boundary when no priority exists. It explicitly forbids silently inventing priority.

### C2 Evidence / Authority Boundary — PASS (manual emulation)

The candidate now distinguishes user instruction, source content, verified evidence, and recommendation/inference. It also forbids claiming inspection or verification that did not occur.

### C3 Change / Preserve — PASS (manual emulation)

The candidate now defines TARGET, PRESERVE, minimal sufficient modification, and explicit handling of unavoidable collateral change. It also routes conflicts through Conflict Control.

## Regression spot checks

### A — Minimal deterministic task

**PASS.** No mandatory conflict, evidence, or patch machinery is triggered. The candidate can still produce a small Skill.

### E — Ambiguous request

**PASS.** Existing ambiguity behavior remains. The new conflict machinery is conditional and does not force clarification for every incomplete request.

### F — External Skill

**PASS.** The new evidence classification strengthens rather than weakens the existing prohibition on wholesale copying.

### G — Local format modification

**PASS.** TARGET/PRESERVE directly addresses the tested failure mode.

### B/C/D — Normal baseline classes

**PASS by design review / manual emulation.** The patch is conditional and does not require new tools, references, or lifecycle layers for normal writing, repository-analysis, or multi-step transformation tasks.

## Pressure spot checks

P1 conflict requirements: **improved**.
P2 external authority: **improved**.
P3 tool unavailable: **preserved**; no claim of capability was introduced.
P4 competing constraints: **improved**.
P5 local modification: **improved**.
P6 Skill-generates-Skill: **preserved**; no recursive architecture rule added.
P7 repair existing Skill: **improved**.

## Regression risks observed

1. The added classification language could become burdensome if applied mechanically to every tiny input. The candidate therefore makes it conditional on material external influence.
2. Conflict control could cause unnecessary clarification if used for ordinary incompleteness. The candidate explicitly distinguishes conflict from compatible ambiguity.
3. PATCH/PRESERVE could be misused as a universal editing framework. It is scoped to modification of an existing Skill.

## Promotion decision

**Do not promote yet.** The candidate has strong manual evidence for addressing C1/C2/C3 and no obvious regression in this review, but a real independent Builder runtime is still unavailable.

Required next gate:

`V0.1 candidate → full baseline A/E/F/G/B/C/D → P1–P7 → targeted C1/C2/C3 → compare against V0`

Only after that comparison should the candidate replace V0.
