# Builder V0 Baseline — Case E

**Case:** E — Ambiguous scope
**Builder SHA:** `19667fdad8edc0464ef45d7b0687210ff0cc26c5`
**Execution:** controlled manual execution in current model environment
**Evaluation independence:** LIMITED
**Status:** PASS / no justified Builder change

## Builder input
> Create a Skill that helps me manage my projects better.

## Candidate

### Task interpretation
The request is to create a Skill that helps with project management, but the concrete recurring task and desired outcome are underspecified.

### Boundary
**Provisional boundary:** Not yet defined. "Manage my projects better" could refer to planning, task tracking, progress reporting, meeting follow-up, risk management, or another materially different activity.

Do not select one of these interpretations as the user's intended scope without clarification.

### Required state / inputs
At minimum, clarification is needed on:
- the primary project-management activity the Skill should perform;
- the desired output/result;
- the typical source material or inputs;
- whether the Skill is for one project or multiple projects, if relevant to the task.

### Intended outcome
A clearly bounded Skill specification for one recurring project-management task, with an observable result appropriate to that task.

### Quality conditions
- Scope is specific enough to know when the Skill applies.
- The intended result is observable.
- Requirements are based on supplied user intent rather than assumptions.
- No project-management capabilities are silently added.

### Failure / uncertainty behavior
If the user does not clarify the primary project-management task, do not generate an elaborate project-management Skill. Record the ambiguity and request the minimum clarification needed.

### Optional architecture
None justified yet. Tools, references, automation, memory, routing, and workflow machinery should not be added until the actual task requires them.

### Candidate Skill
**Status: blocked pending clarification.**

A complete executable Skill should not be fabricated from the current request because materially different scopes are possible.

### Evaluation plan
1. Provide a clarified narrow task and verify the resulting Skill remains proportionate.
2. Provide a request that mentions project tracking explicitly and verify only the requested capability is added.
3. Provide conflicting project-management goals and verify the Builder preserves the conflict instead of silently choosing one.

### Open questions
- What recurring project-management task should the Skill perform?
- What should the Skill produce or change?
- What inputs will normally be supplied?

## Evaluation
Expected properties: ambiguity identified; minimum clarification; no hidden assumptions; no elaborate invented system.

Observed: all expected properties present. No unnecessary architecture.

**Decision:** PASS. No Builder modification justified.
