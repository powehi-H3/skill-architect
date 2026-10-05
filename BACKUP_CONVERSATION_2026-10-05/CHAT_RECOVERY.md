# Conversation Recovery — Skill Architect Project

## 1. Project start and objective

The user created a new GitHub repository specifically for a new Skill/Skill-Architect project:

- Repository: `powehi-H3/skill-architect`
- Goal: build a general-purpose Skill architecture / Skill Builder / Skill Reviewer system.
- Explicit constraint: do **not** simply copy or generalize the user's previous Minimax H3 skill experience unless there is strong evidence it is genuinely useful.
- The user wants professional, rigorous engineering rather than superficial agreement.

## 2. Source material reviewed / supplied by the user

The user supplied or referenced multiple Skill-related projects and articles, including:

- `https://github.com/dontbesilent2025/dbskill`
- `https://github.com/alchaincyf/nuwa-skill`
- `https://github.com/mattpocock/skills`
- `https://github.com/gnipbao/dao-skill`
- `https://youmind.com/zh-CN/skills/meta-prompt-architect-ZB8wDKV9edDPbf`
- X/Twitter material from GeekCatX, including status IDs:
  - `2084866403635810523`
  - `2054830389123059990`
  - `2094292719049068783`

The user also supplied extensive excerpts describing a Skill methodology:

- A Skill should specify what to do, how to do it, how to judge quality, and what to do when it cannot complete the task.
- Minimal structure:
  - frontmatter `name` / `description`
  - Goal
  - Input
  - Execution Steps
  - Output Format
  - Quality Standards
  - Failure Handling
- Test normal, edge, and pressure scenarios.
- Iterate from failure results, changing one problem at a time.
- Build a Skill library only after repeated tests.
- Workflow = multiple Skills composed into a pipeline.
- Agent systems add planning, tools, memory, and fallback.
- Meta-Skill = a Skill that produces, reviews, and upgrades Skills.

## 3. Design direction agreed in conversation

The project is not intended to be an H3-specific prompt optimizer. It is intended to become a general Skill architecture system.

The user asked for a system that can eventually support:

- Skill Builder
- Skill Reviewer / Evaluator
- testing and regression
- adversarial / pressure testing
- evidence boundaries
- iterative improvement
- eventual LLM runtime
- eventually workflows / automation if justified

The user wants the project to be robust enough that it does not simply declare its own work successful.

## 4. GitHub / access setup

The user created and connected the repository through the ChatGPT/Codex GitHub connector flow.

The repository is accessible for GitHub file and workflow operations.

## 5. OpenAI API runtime

The user created an OpenAI API key and stored the required GitHub Secret.

The OpenAI baseline workflow was actually run.

The workflow reached the Python Builder and then the OpenAI API, but the API returned:

`HTTP 429`

with:

`billing_not_active`

and:

`Your account is not active, please check your billing details on our website.`

Therefore:

- GitHub Actions: working
- Secret injection: working
- Python runner: working
- API request path: working
- OpenAI billing: unavailable

The user currently cannot add billing/credits, so the project was explicitly switched to an offline/mock path rather than requiring payment.

Important: the OpenAI runtime failure must not be represented as a Builder-quality failure. It is an external billing blocker.

## 6. Offline Harness

An offline deterministic harness was added and successfully run.

The first successful run demonstrated that:

- workflow executes
- fixtures are loaded
- offline runner executes
- evidence is generated
- artifact upload works

The offline run was explicitly defined as `OFFLINE-MOCK` evidence and must never be presented as proof of real LLM execution or semantic Builder quality.

## 7. Audit problem discovered

A major design concern was identified:

A test system can produce green results while merely checking fixture metadata, rather than actually evaluating whether a Skill candidate is good.

The user strongly objected to superficial progress and asked for real engineering work rather than repeated status messages.

The correct project standard became:

> Do not count adding files/fixtures as progress unless the new code can detect a real failure, produce evidence, or close a real architectural gap.

## 8. Offline Harness Audit

An Offline Harness Audit V1 was introduced.

The audit checks fixture structure and required attack classes, including:

- missing-input / fact attack
- evidence-boundary attack
- regression attack
- PASS/FAIL/UNKNOWN disposition handling

There were initially two audit workflows. This was recognized as an ambiguity. The old workflow was retained as a legacy alias while the V1 implementation became the intended authoritative audit logic.

## 9. Deterministic Evaluator upgrade

A deterministic evaluator was added:

`scripts/evaluate_offline_candidate_v1.py`

It intentionally does not claim to judge open-ended Skill quality. It evaluates explicit, machine-checkable contract properties.

A mutation tester was added:

`scripts/mutation_test_offline_v1.py`

The purpose is to deliberately alter cases that should fail and require the evaluator to reject those mutations. This prevents a vacuous evaluator from receiving green status merely because fixtures exist.

A unified evaluator suite was then added:

`scripts/run_evaluator_suite_v1.py`

and workflow:

`.github/workflows/offline-evaluator-suite-v1.yml`

The suite currently exercises deterministic cases E/H/D2 and the mutation test.

## 10. Current principle for evaluation

The project should move toward this evidence chain:

Fixture → deterministic evaluator → expected disposition → actual disposition → assertion → evidence

The evaluator must be capable of failing deliberately mutated cases.

The system must distinguish:

- PASS
- FAIL
- UNKNOWN

and must not convert lack of evidence into PASS.

## 11. User communication preference

The user explicitly asked that when no participation is needed:

- do not repeatedly report trivial progress
- do not stop merely to say “continuing”
- do not repeatedly explain architecture that has already been explained
- only interrupt when user action/confirmation is genuinely required
- when reporting, report concrete results rather than filler

## 12. Current backup request

On 2026-10-05 the user requested that the project's conversations be backed up into a dedicated folder in this GitHub repository.

This folder is that backup.

Because the complete private ChatGPT transcript is not exposed through the GitHub connector, this is a recovery/context backup rather than a verbatim transcript export. The repository Git history remains the authoritative record of code/config changes.
