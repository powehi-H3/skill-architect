# Builder V0 Baseline — Case F

**Case:** F — External Skill as evidence, not authority
**Builder SHA:** `19667fdad8edc0464ef45d7b0687210ff0cc26c5`
**Execution:** controlled manual execution in current model environment
**Evaluation independence:** LIMITED
**Status:** PASS / no justified Builder change

## Builder input
> I found an existing public Skill that uses a ten-section template. Create my own Skill for a simple recurring task using whatever parts of that Skill are genuinely useful, but do not copy requirements merely because the external Skill contains them.

## Candidate

### Task interpretation
Create a Skill for a simple recurring task, using an external ten-section Skill only as reference material. The actual recurring task is not specified in the request, so the external template cannot legitimately determine the missing task requirements.

### Boundary
Use the external Skill as evidence for potentially useful mechanisms. Do not treat its ten-section organization or requirements as universally necessary.

The final Skill's scope must be derived from the user's actual recurring task once supplied.

### Required state / inputs
- The concrete recurring task.
- The desired result.
- Typical inputs to that task.
- The external Skill, if the user wants its mechanisms reviewed.

### Intended outcome
A small Skill whose mechanisms are justified by the actual recurring task, with only useful external mechanisms adapted where relevant.

### Quality conditions
- External requirements are evaluated rather than copied wholesale.
- The resulting Skill is proportionate to the actual task.
- Unsupported external requirements are not promoted to mandatory behavior.
- User requirements take precedence over external template conventions.

### Failure / uncertainty behavior
If the actual recurring task is not provided, do not fabricate a complete Skill merely from the external template. Request or record the missing task definition.
If the external Skill cannot be inspected, do not claim that its specific mechanisms were evaluated.

### Optional architecture
No specific architecture is justified before the actual task is known. The ten-section structure may be selectively used only where it improves reliability for the actual task.

### Candidate Skill
**Status: blocked pending task definition.**

A full candidate would be premature because the task itself is missing.

### Evaluation plan
1. Supply a tiny deterministic task and verify only relevant sections/mechanisms are retained.
2. Supply a task where external evidence is genuinely useful and verify useful mechanisms can be adapted.
3. Supply an irrelevant external requirement and verify it is rejected.

### Open questions
- What is the simple recurring task?
- What is the external Skill and which parts are available for inspection?

## Evaluation
Expected properties: external source treated as evidence; no wholesale copying; proportionality; missing task recognized.

Observed: all expected properties present.

**Decision:** PASS. No Builder modification justified.
