# Builder V0 Baseline Summary 001

**Builder SHA:** `19667fdad8edc0464ef45d7b0687210ff0cc26c5`
**Benchmark:** `BUILDER-BENCHMARK-V0.md` SHA `176a56c5b694fa8810d8c7b577c53d31a37f5a66`
**Execution mode:** controlled manual execution in current model environment
**Evaluation independence:** LIMITED
**Builder modifications during baseline:** NONE

## Results

| Case | Theme | Result | Builder change justified? |
|---|---|---|---|
| A | Minimal deterministic task | PASS | No |
| E | Ambiguous scope | PASS | No |
| F | External Skill as evidence | PASS | No |
| G | Localized change / preservation | PASS | No |
| B | Writing transformation | PASS | No |
| C | Tool-dependent repository analysis | PASS | No |
| D | Multi-step transformation | PASS | No |

## Interpretation

No substantive Builder failure was observed in this controlled manual baseline. The candidates remain proportionate to their tasks, preserve uncertainty, avoid invented requirements, represent genuine capability dependencies where needed, and preserve unrelated content in the localized-change case.

The ordering used for execution follows the project protocol: A → E → F → G → B → C → D.

## Evidence limitation

These are controlled manual executions, not independent black-box executions in a separate Builder runtime. The same model family performed Builder and evaluation roles. Therefore `evaluation_independence = LIMITED` and the results should be treated as engineering evidence, not as proof of statistical or model-level independence.

## Important consequence

Because no substantive failure was observed, there is currently no evidence-based reason to create Builder V0.1. Do not modify Builder merely to create a new version.

## Next stage

The project should now perform adversarial/pressure testing beyond the current seven baseline cases before promotion. Candidate additions should target failure modes not discriminated by V0:

1. conflicting user requirements;
2. deliberately misleading external reference;
3. missing/partially accessible tool capability;
4. very long input with competing constraints;
5. localized change combined with a semantic conflict;
6. request for a Skill that itself should use another Skill;
7. repeated iteration where previous candidate mistakes are supplied as context.

Any new test must be added to the benchmark with a fixed input and explicit expected properties before it is used to justify a Builder change.
