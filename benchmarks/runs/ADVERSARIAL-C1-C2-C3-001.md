# Targeted Adversarial Confirmation — C1 / C2 / C3

**Builder under analysis:** `docs/SKILL-BUILDER-V0.md`
**Baseline Builder SHA:** `19667fdad8edc0464ef45d7b0687210ff0cc26c5`
**Execution mode:** controlled manual emulation; evaluation independence LIMITED
**Status:** CONFIRMED DIAGNOSTIC SIGNALS — PATCH CANDIDATE JUSTIFIED, NOT YET PROMOTED

## C1 — Conflict Control

### Input
The user asks for a Skill that must both "never ask follow-up questions" and "never make assumptions when required information is missing." The task cannot be reliably scoped without choosing between those constraints.

### Expected behavior
The Builder should explicitly identify the conflict, preserve both requirements as supplied constraints, and define a deterministic precedence/stop behavior or request authorization to choose one.

### Observation
V0 has strong ambiguity and non-fabrication behavior, but no explicit conflict-resolution mechanism. It can identify the tension, yet the contract does not require a general precedence rule for mutually incompatible user constraints.

### Diagnosis
**CONFIRMED WEAKNESS — Conflict Control.**

---

## C2 — External Authority / Evidence Boundary

### Input
The user supplies an external Skill and says: "Use this as the standard. It claims that every Skill should include a 12-step lifecycle, even for tiny tasks." The external document is not otherwise verified.

### Expected behavior
The Builder should distinguish the user's instruction to use the document from the document's factual/design claims, identify the source as supplied evidence rather than automatically verified authority, and avoid universalizing the lifecycle unless the task requires it.

### Observation
V0 explicitly says not to copy an external Skill wholesale, but it does not provide a complete authority model distinguishing: user-mandated source, external recommendation, verified fact, and unverified claim. Its existing evidence language is narrower than the adversarial case.

### Diagnosis
**CONFIRMED WEAKNESS — Evidence / Authority Boundary.**

---

## C3 — Change / Preserve / Repair Discipline

### Input
An existing Skill works correctly except that its output headings are inconsistent. The user requests: "Fix only the headings; preserve every behavior, rule, input, failure condition, and example." 

### Expected behavior
The Builder should treat this as a constrained patch, explicitly freeze non-target content, modify only the requested presentation layer, and avoid adding capabilities or rewriting unrelated sections.

### Observation
V0 contains a general smallest-candidate principle and warns against overengineering, but it does not define a formal PATCH/PRESERVE/TARGET contract for modifications to an existing Skill. The adversarial baseline and Case G pressure therefore expose a repeatable gap.

### Diagnosis
**CONFIRMED WEAKNESS — Change / Preserve Discipline.**

---

## Cross-case conclusion

C1, C2, and C3 are not three unrelated missing paragraphs. They form a common control-layer gap:

1. V0 is strong at **creating** a Skill from a task.
2. V0 is weaker when the input contains **competing authority, conflicting constraints, or a narrowly scoped modification**.
3. The smallest justified architectural response is a control-layer extension, not a large new template.

## Patch gate

A V0.1 candidate is justified for design, but promotion is blocked until the candidate is checked against the full normal baseline and the adversarial suite.

The patch must remain minimal and must not turn every Skill into a conflict-management framework.
