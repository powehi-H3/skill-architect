# Skill Builder Benchmark V0

**Status:** EXPERIMENTAL
**Purpose:** Black-box benchmark for Skill Builder V0. This benchmark evaluates generated Skills, not how polished the Builder instructions look.

## 1. Evaluation rule

For each case, record:

- Input given to Builder
- Candidate Skill produced
- Expected properties
- Observed properties
- Failures / unnecessary additions
- Root-cause hypothesis
- Smallest justified Builder change
- Regression cases to rerun

Do not award credit merely because the candidate contains familiar headings.

## 2. Case A — Minimal deterministic task

**Prompt:**

> Create a Skill that converts a user-provided Celsius temperature into Fahrenheit. The user supplies one temperature. Return the converted value and unit. If the temperature is missing or not interpretable as a number, say what is missing instead of inventing it.

**Purpose:** Detect over-engineering.

**Expected properties:**
- narrow boundary;
- one clear input;
- deterministic outcome;
- simple quality condition (correct conversion/unit);
- explicit missing/invalid input behavior;
- no unnecessary tools, references, routing, memory, automation, registry, or complex lifecycle.

**Failure signals:**
- large architecture for a tiny task;
- invented requirements;
- unnecessary external dependencies;
- vague success criteria.

## 3. Case B — Writing transformation

**Prompt:**

> Create a Skill that polishes a user-provided business email. Preserve the user's factual meaning and requested intent, improve clarity and professionalism, and do not invent facts. The user may specify a desired tone.

**Purpose:** Test a common artifact-producing Skill without tool dependencies.

**Expected properties:**
- clear scope;
- source email and optional tone as inputs;
- observable polished email as result;
- meaning/fact preservation as quality condition;
- sensible handling of missing source text;
- no forced tools or references.

**Failure signals:**
- rewriting the task into a generic writing agent;
- adding unsupported facts;
- mandatory complex QA infrastructure;
- failure behavior missing.

## 4. Case C — Tool-dependent repository analysis

**Prompt:**

> Create a Skill for reviewing a GitHub repository for a named bug. It should inspect relevant repository files, identify evidence supporting or contradicting the suspected cause, and return a concise diagnosis with file references. If the repository or relevant files cannot be accessed, report that limitation rather than pretending the investigation happened.

**Purpose:** Test capability/environment representation and evidence grounding.

**Expected properties:**
- repository/tool access represented as a real dependency;
- evidence-based diagnosis;
- clear distinction between observed evidence and inference;
- explicit inaccessible-source failure behavior;
- no claim of tool execution when no tool was actually used.

**Failure signals:**
- pretending to inspect files;
- treating GitHub access as universal Skill infrastructure;
- no evidence boundary;
- confusing diagnosis with guaranteed root cause.

## 5. Case D — Multi-step transformation

**Prompt:**

> Create a Skill that turns a long meeting transcript into an action-oriented project brief. It should identify decisions, unresolved questions, owners when explicitly stated, deadlines when explicitly stated, and concrete next actions. It should distinguish stated facts from inferred suggestions and should not invent owners or dates.

**Purpose:** Test whether intermediate structure is added only because it helps reliability.

**Expected properties:**
- source transcript as input;
- observable project brief as outcome;
- extraction/organization logic appropriate to the task;
- explicit fact-vs-inference boundary;
- missing owner/date behavior;
- intermediate state may be represented if useful, but should not become generic architecture boilerplate.

**Failure signals:**
- fabricated owners/dates;
- no uncertainty handling;
- unnecessary agent/workflow machinery;
- treating every inference as a fact.

## 6. Case E — Ambiguous scope

**Prompt:**

> Create a Skill that helps me manage my projects better.

**Purpose:** Test whether Builder recognizes material ambiguity rather than inventing a large system.

**Expected properties:**
- identify that purpose and boundary are materially underspecified;
- ask for or clearly record minimum clarification needed;
- avoid generating an elaborate project-management Skill from assumptions;
- if offering a provisional candidate, label assumptions explicitly.

**Failure signals:**
- silently choosing project tracking, planning, reminders, reporting, or automation as the user's intent;
- generating a large Skill while hiding assumptions.

## 7. Case F — External Skill as evidence, not authority

**Prompt:**

> I found an existing public Skill that uses a ten-section template. Create my own Skill for a simple recurring task using whatever parts of that Skill are genuinely useful, but do not copy requirements merely because the external Skill contains them.

**Purpose:** Test evidence-boundary behavior.

**Expected properties:**
- external material treated as reference/evidence;
- useful mechanisms may be adapted;
- unsupported external requirements not promoted automatically;
- resulting Skill sized to the actual task.

**Failure signals:**
- wholesale copying;
- claiming external structure is universally required;
- inability to reject irrelevant machinery.

## 8. Case G — Localized change request

**Prompt:**

> Here is an existing Skill that already works. Change only its output so that it returns a table instead of a bullet list. Preserve its scope, inputs, core behavior, quality conditions, and failure handling unless the requested format change makes one of them genuinely inconsistent.

**Purpose:** Test change discipline and preservation.

**Expected properties:**
- targeted modification;
- preservation of unrelated behavior;
- no unnecessary rewrite;
- explicit identification of any genuinely affected contract element.

**Failure signals:**
- rewriting the whole Skill;
- deleting unrelated constraints;
- adding new behavior under the guise of formatting;
- changing semantics without evidence.

## 9. Scoring dimensions

Score each dimension 0–2:

- Boundary correctness
- Input/state correctness
- Outcome observability
- Quality adequacy
- Failure/uncertainty handling
- Proportionality / non-overengineering
- Evidence discipline
- Change/preservation discipline when applicable

`0 = absent or materially wrong`
`1 = partially correct / unnecessary complexity`
`2 = correct and proportionate`

Do not use the total score as a substitute for qualitative failure analysis. A catastrophic failure in one dimension may matter more than several minor strengths.

## 10. Promotion / regression rule

Builder V0 is not promoted based on benchmark design alone.

After actual black-box runs, promote only evidence-backed changes. Every Builder revision should rerun all cases that could plausibly regress, not merely the case that exposed the original failure.

The benchmark itself may be revised when a case becomes redundant, unrealistic, or unable to discriminate between Builder versions. Such changes must be recorded.
