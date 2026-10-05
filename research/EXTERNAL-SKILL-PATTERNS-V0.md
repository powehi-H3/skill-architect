# External Skill Patterns V0

**Status:** RESEARCH ONLY — NOT CORE ARCHITECTURE

## Purpose

This document records observations from external Skill systems supplied for this project. These observations are deliberately kept outside the core architecture until they are shown to generalize across unrelated Skill types.

## Sources reviewed

- dontbesilent2025/dbskill
- alchaincyf/nuwa-skill
- mattpocock/skills
- gnipbao/dao-skill
- YouMind 元提示词架构师

## Observations

### 1. A Skill can be a system, not merely a prompt

The reviewed projects use combinations of SKILL.md, references, scripts, examples, tests, setup/configuration, and generated artifacts. This supports treating a Skill as a potentially packaged capability rather than assuming every Skill is one prompt file.

**Status:** strong observation; not yet a mandatory architecture rule.

### 2. Clear trigger boundaries matter

Examples use explicit descriptions, trigger signals, non-use boundaries, and routing. Nuwa has explicit triggers and a routing path for vague versus explicit requests. dbskill provides a general entry point plus narrower Skills. Matt Pocock's setup Skill explicitly disables automatic invocation for a setup action and describes when it should run.

**Candidate general principle:** a Skill needs a discoverable invocation boundary appropriate to its environment.

### 3. Routing/composition is a real capability

Dbskill can decide whether one Skill is enough or whether a small combination is needed. Dao has explicit mode routing and handoff to specialized Skills. Matt Pocock's repository organizes Skills into composable engineering capabilities.

**Candidate general principle:** Skill systems may need routing/composition rather than one universal Skill.

### 4. References should be loaded selectively

Dao explicitly uses a resource guide and mode-specific references rather than loading every reference for every request. This is a useful pattern for controlling context and separating core instructions from deeper material.

**Status:** promising pattern; requires cross-domain validation before becoming core architecture.

### 5. Evidence and evaluation are treated as first-class concerns

Dao separates structural checks from runtime behavior evidence and uses explicit evidence levels. Nuwa reports a fidelity scorecard and documents methodology. Matt Pocock keeps in-progress Skills separate from stable public Skills. These are materially different implementations of the same broader concern: do not equate a complete document with validated behavior.

**Candidate general principle:** validation status should be distinguishable from documentation status.

### 6. Experimental/stable separation appears independently useful

Matt Pocock explicitly separates in-progress Skills from stable Skills. Dao has provisional/accepted/quarantined/rejected deployment concepts. Nuwa has ongoing optimization and fidelity evaluation.

**Candidate general principle:** systems that evolve Skills benefit from explicit maturity/evidence status.

### 7. Failure feedback can become durable assets

Dao explicitly turns feedback into rules, references, examples, tests, scripts, or rubric changes and has an evolution protocol. This is more than prompt editing: it treats observed failures as inputs to system improvement.

**Status:** promising, but the exact evolution mechanism should not be copied into core architecture without testing.

### 8. Setup and runtime state should be distinguished

Matt Pocock's setup Skill creates repository-specific configuration. Dao explicitly separates source repository, installation, runtime state, and generated child Skills. Dbskill maintains local records separately from its distributable Skills.

**Candidate general principle:** reusable Skill artifacts and user/runtime state are distinct concerns.

### 9. Self-containedness is a design choice, not a universal rule

Dbskill's content-system Skill explicitly requires self-containment, while Dao uses external references selectively. Therefore “every Skill must be self-contained” is not a safe universal rule.

**Important negative finding:** do not promote self-containedness to a core requirement.

### 10. Large Skills are not automatically better

The reviewed projects range from compact procedural Skills to large systems with references and scripts. Their value comes from appropriate structure, routing, resources, and validation—not raw line count.

**Candidate general principle:** optimize for capability and maintainability, not prompt length.

## What we deliberately do NOT adopt yet

- Any fixed universal number of Skill sections.
- Any universal requirement that every Skill have scripts/references/tests.
- Any particular scoring formula (including 80/100 or other numeric gates).
- Dao's philosophical vocabulary as architecture.
- Any project's exact lifecycle names as mandatory.
- Any domain-specific H3 rule.
- “Self-contained SKILL.md” as a universal requirement.
- Any claim that one repository's runtime behavior proves another Skill's reliability.

## Next validation experiment

Build or inspect three unrelated prototype Skills:

1. text transformation / article polishing;
2. code review;
3. meeting-note synthesis.

For each, ask whether the candidate principles above improve design clarity or reliability without imposing irrelevant machinery. Promote only principles that survive this cross-domain check.

## Evidence boundary

This file records interpretation of public sources, not a claim that the source authors endorse this architecture. Source-specific implementation details remain source-specific unless independently validated.
