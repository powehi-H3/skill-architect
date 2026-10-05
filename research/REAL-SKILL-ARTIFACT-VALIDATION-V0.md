# Real Skill Artifact Validation V0

**Status:** EXPERIMENTAL RESEARCH
**Purpose:** Test the current Skill Architect concepts against real Skill artifacts from independent ecosystems.

## Sources examined

### dbskill
- `dbs/SKILL.md`: router/orchestrator behavior, update check, downstream Skill delegation, explicit scope.
- `dbs-content-system/SKILL.md`: deliberately self-contained heavy Skill; explicit non-goals and local resources.
- `dbs-learning/SKILL.md`: adaptive multi-turn teaching Skill with explicit trigger signals and boundaries.
- `dbs-knowledge/SKILL.md`: knowledge-base Skill with navigation, source-of-truth handling, version/conflict checks.

### Matt Pocock skills
- `engineering/research/SKILL.md`: research Skill with primary-source requirement and cited Markdown output.
- `engineering/setup-matt-pocock-skills/SKILL.md`: environment-aware setup Skill with explicit exploration before writing.
- `engineering/to-spec/SKILL.md`: conversation-to-spec transformation with repository context and project conventions.
- `engineering/writing-shape/SKILL.md`: staged transformation Skill with read-only source-material handling.

### dao-skill
- repository `SKILL.md`: meta-Skill architecture with routing, generation, validation, workspace resolution, references, scripts, examples, and regression prompts.
- `examples/usage-verification.md`: behavior-oriented verification examples for generation and installation boundaries.

## Findings

### 1. Boundary / purpose generalizes strongly
Real Skills consistently state what they are for and/or what they are not for. dbskill's router delegates concrete work rather than performing every downstream task; dbs-learning explicitly separates teaching from diagnosis; writing-shape distinguishes exploration from exploitation. This supports Boundary/Purpose as a core concept. citeturn0search7turn0search5turn0search9

### 2. Trigger/selection is important, but not identical to purpose
Descriptions are used as invocation/selection signals. Matt's `research` explicitly describes when to use it; `ask-matt` is itself a router; dbskill uses descriptions to select capabilities. This suggests trigger/selection metadata should be a core interface concern, while exact trigger syntax remains host-dependent. citeturn0search1turn0search4turn0search0

### 3. Input and environment are separate concepts
Real Skills show both ordinary inputs and environmental prerequisites. `setup-matt-pocock-skills` inspects repository configuration before writing; `to-spec` depends on project context; dbs-knowledge depends on filesystem/source-of-truth structures. This validates optional capability/environment requirements, but not as a universal mandatory section. citeturn0search2turn0search13turn0search8

### 4. Output contracts are real, but task-specific
Research requires a cited Markdown artifact; dbs-knowledge has concrete navigation and knowledge-base outputs; to-spec produces a project spec. These outputs differ substantially. A universal output schema would be harmful. citeturn0search1turn0search8turn0search13

### 5. Execution procedures vary substantially
The real artifacts use direct procedures, staged loops, repository exploration, routing, scripts, and delegated sub-Skills. There is no credible basis for one universal execution pipeline. citeturn0search2turn0search4turn0search10

### 6. Self-contained vs modular is a genuine architectural choice
`dbs-content-system` explicitly requires self-containment, while dao-skill uses references, examples, scripts, and dynamically created child Skills. Therefore self-containment cannot be a universal Skill rule. The architecture should support both packaging strategies. citeturn0search3turn0search10

### 7. Evidence/provenance matters where claims depend on sources
The research Skill explicitly requires primary sources and citations. dbs-knowledge requires following navigation to original files rather than answering from summaries alone. This supports evidence/provenance as a conditional core capability, not a mandatory behavior for every Skill. citeturn0search1turn0search8

### 8. Routing/composition is a capability, not a universal requirement
`ask-matt`, dbskill's main entry, and dao-skill demonstrate routing/composition. Simple Skills need not have a router. Therefore routing should be modeled as an optional capability. citeturn0search4turn0search7turn0search10

### 9. Validation exists at different scales
Dao-skill includes regression prompts and verification examples, while individual Skills may have much lighter instructions. This supports validation as an architectural capability, but does not justify one fixed test suite or lifecycle burden for every Skill. citeturn0search10turn0search12

## Cross-check against current proposed core

| Concept | Real-artifact evidence | Current disposition |
|---|---|---|
| Boundary / purpose | Strong | Keep as core candidate |
| Trigger / selection | Strong | Keep as core interface candidate |
| Input expectations | Strong | Keep as core candidate |
| Intended outcome | Strong | Keep as core candidate |
| Output expectations | Strong but variable | Keep as core, task-specific |
| Quality criteria | Present, often implicit | Keep as candidate; refine later |
| Failure / uncertainty | Present unevenly | Keep as candidate; require proportionality |
| Evidence / provenance | Strong where source claims matter | Conditional capability |
| Environment / capabilities | Strong in tool-oriented Skills | Optional capability |
| Intermediate state | Present in staged workflows | Optional capability |
| Routing / composition | Strong in meta/router Skills | Optional capability |
| External references/resources | Common | Packaging choice, not universal |
| Self-contained package | Used by some | Packaging choice, not universal |
| Fixed universal workflow | No | Reject as core |
| Fixed universal test suite | No | Reject as core |

## Important limitation

This is evidence from selected public repositories, not a statistical survey of all Skills. The findings therefore support provisional architectural hypotheses only. They do not establish universal laws.

## Provisional conclusion

The real artifacts strengthen the case for a **small core contract + optional capabilities + host/package-specific mechanisms**.

The strongest current core candidate is:

```text
Identity / Trigger boundary
Purpose / intended outcome
Input expectations
Output expectations
Quality expectations
Failure / uncertainty handling
```

Conditional capabilities include:

```text
Evidence / provenance
Environment / tools
Intermediate state
Routing / composition
External resources
Validation / regression
```

The distinction between **core contract**, **optional capability**, and **implementation/host mechanism** should now become the central architectural question for the next revision.

## Promotion status

No automatic promotion to CORE. This document records evidence and provisional conclusions only.
