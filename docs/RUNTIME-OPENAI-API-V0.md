# OpenAI API Runtime — Builder V0.2

**Status:** EXPERIMENTAL RUNTIME — NOT A PROMOTION

## Purpose

This document records the automated runtime path for executing the Skill Builder V0.2 candidate against the existing V0 benchmark.

The runtime exists to establish real execution evidence. It does not promote V0.2 and it does not replace the project evidence contract.

## Runtime architecture

`GitHub Actions → fixed repository checkout → Builder V0.2 Candidate + benchmark case → OpenAI Responses API → frozen candidate → separate evaluator API call → artifact evidence`

The Builder and evaluator are separate API calls. The evaluator receives the frozen Builder candidate only after capture.

## Secret

The workflow expects a repository Actions secret named `OPENAI_API_KEY`.

The key is never stored in the repository and must not be printed into logs. GitHub Actions secrets are the intended mechanism for sensitive API credentials.

## Model

The workflow does **not** assume a default model identifier. The exact model identifier must be supplied explicitly at manual dispatch time and is recorded in run metadata.

This is intentional: an unverified model alias must never be treated as a valid runtime dependency.

## Execution scope

The first automated baseline runs the seven normal benchmark cases in the protocol order:

`A → E → F → G → B → C → D`

Case G also receives the repository's explicit existing-Skill fixture because the case itself requires that context.

## Evidence rules

Every case preserves:

- exact case input supplied to the Builder;
- complete Builder candidate as captured;
- separate evaluator result;
- run ID;
- Builder commit;
- benchmark identifier;
- model identifier;
- execution status;
- runtime/evidence boundary.

The workflow must not claim PASS merely because the workflow completed. Evaluation remains evidence that must be inspected.

## Deliberate limitations

- The evaluator is an automated model-based evaluator, not an independent human or independently trained gold-standard judge.
- The Builder and evaluator currently use the same API provider and configurable model family; this is an independence limitation that must be recorded, not hidden.
- No Builder revision is changed automatically by this workflow.
- No promotion occurs automatically.
- Adversarial and unknown-task runs remain separate gates.

## Acceptance boundary

A successful workflow run establishes **EXECUTED runtime evidence** for the tested cases. It does not by itself establish that V0.2 is Stable or that the overall Skill Architect project is complete.
