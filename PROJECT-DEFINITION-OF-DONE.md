# Skill Architect — Definition of Done

**Status:** Project acceptance contract
**Version:** 1.0

## Project completion definition

Skill Architect is complete only when it functions as an auditable Skill Engineering System, not merely as a Skill Builder prompt.

## Ten mandatory gates

### 1. Stable Skill Builder
A versioned Builder reaches Stable status with documented scope, inputs, execution rules, outputs, quality criteria, failure handling, and evidence boundaries.

### 2. Skill Reviewer
A separate Reviewer can evaluate candidate Skills against explicit criteria and produce evidence-backed PASS / NEEDS REVISION / FAIL decisions. Reviewer logic must not simply echo Builder instructions.

### 3. Benchmark system
Benchmarks cover normal, edge, pressure, modification, evidence, conflict, preservation, and unknown-task behavior. Each benchmark has a stable case definition and expected invariants.

### 4. Reproducible execution
A documented Runner can execute a fixed Builder against a fixed case and preserve the complete candidate and evaluation evidence. Manual execution may be used only with explicit limitations; final acceptance requires a credible path to reproducibility.

### 5. Failure taxonomy and library
Observed failures have stable identifiers, minimal reproductions, evidence, root-cause classification, repair history, and regression coverage.

### 6. Regression system
Every Builder revision must be tested against prior capabilities as well as the newly targeted failure. A targeted improvement cannot be promoted if it causes material regression without explicit acceptance.

### 7. Version and promotion system
Experimental → Candidate → Stable transitions are explicit. Every promotion identifies the tested commit, benchmark set, evidence level, known limitations, and reason for promotion.

### 8. Independence / contamination controls
Builder, Reviewer, benchmark authoring, and evaluation evidence must have clearly stated independence limits. The system must not claim stronger evidence than the runtime supports.

### 9. Unknown-task blind test
The Builder must perform acceptably on previously unseen tasks not designed around its known benchmark vocabulary. The purpose is to test generalization rather than benchmark memorization.

### 10. Closed engineering loop
The repository must demonstrate a repeatable loop:

`Task → Build → Test → Observe → Classify Failure → Root Cause → Minimal Patch → Regression → Promote`

The loop must be executable without rewriting the methodology from scratch for each new Skill.

## Non-goals

The project is not complete merely because:

- SKILL.md is long;
- the Builder has many rules;
- every benchmark says PASS without evidence;
- an automated tool was added without proving reproducibility;
- MCP, memory, agents, or automation were added for appearance rather than demonstrated need;
- the system copies domain-specific rules from an unrelated project without independent evidence.

## Final acceptance principle

When evidence is unavailable, the project must report UNKNOWN or LIMITED rather than manufacture completion. A smaller system with reproducible evidence is preferable to a larger system with unverifiable claims.
