# Builder V0 Baseline — Case B

**Case:** B — Writing transformation
**Builder SHA:** `19667fdad8edc0464ef45d7b0687210ff0cc26c5`
**Execution:** controlled manual execution in current model environment
**Evaluation independence:** LIMITED
**Status:** PASS / no justified Builder change

## Builder input
> Create a Skill that polishes a user-provided business email. Preserve the user's factual meaning and requested intent, improve clarity and professionalism, and do not invent facts. The user may specify a desired tone.

## Candidate

### Task interpretation
Create a Skill that edits a supplied business email for clarity and professionalism while preserving factual meaning and intent. Tone is optional user input.

### Boundary
The Skill rewrites provided business email text. It does not invent facts, change the user's intended request, or add unsupported content. It does not require external tools.

### Required state / inputs
- Source business email text.
- Optional desired tone.

### Intended outcome
A polished business email that is clearer and more professional while preserving the source's factual content and requested intent.

### Quality conditions
- Facts are preserved.
- User intent is preserved.
- Requested tone is followed when supplied.
- Clarity and professionalism improve without changing meaning.
- No unsupported facts are added.

### Failure / uncertainty behavior
If source email text is missing, state that the source email is required and do not fabricate an email.
If the requested tone conflicts with preserving factual meaning or intent, preserve meaning/intent and flag the conflict rather than inventing content.

### Optional architecture
None. No tools, references, routing, memory, or automation are justified for this transformation.

### Candidate Skill
When the user provides a business email, rewrite it for clarity and professionalism. Preserve every factual claim and the user's requested intent. Apply the user's requested tone when supplied. Do not add facts or unsupported commitments. If the source email is missing, ask for it rather than generating one.

### Evaluation plan
1. Polish a normal business email and compare factual claims.
2. Supply a tone request and verify only style changes.
3. Omit the source email and verify no invented email is produced.

### Open questions
None material for the stated task.

## Evaluation
Expected properties all observed. Candidate is small, tool-free, and preserves the requested semantic contract.

**Decision:** PASS. No Builder modification justified.
