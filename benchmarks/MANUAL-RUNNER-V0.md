# Manual Runner V0

**Status:** EXPERIMENTAL / CONTROLLED MANUAL EXECUTION
**Purpose:** Provide a reproducible procedure for executing Builder V0 when an independent automated Builder runtime is unavailable.

## 1. Non-negotiable evidence rule

A manual run is a real run only if the operator captures the complete Builder interaction needed to audit it. Analysis, prediction, or a reconstructed answer is not a run.

This procedure does not create runtime independence. It creates execution discipline and evidence integrity.

## 2. Immutable inputs

Before starting a case, record:

- Builder commit SHA;
- benchmark version;
- case ID;
- fixture path/version when applicable;
- execution model/runtime;
- date/time;
- any explicitly permitted supporting references.

Do not modify Builder, benchmark, or fixture during the baseline sequence.

## 3. Blind Builder phase

The operator must prepare a Builder-only packet containing:

1. the exact Builder specification at the locked SHA;
2. the exact case input;
3. only the context explicitly permitted by the case.

Do not include:

- expected answer;
- evaluator rubric beyond what the Builder specification itself requires;
- hidden failure labels;
- evaluator notes;
- predicted weaknesses;
- proposed fixes.

Run the Builder once.

## 4. Candidate capture

Capture the Builder output exactly as returned.

Do not edit, shorten, correct, reorganize, or merge it with commentary.

Assign a Candidate ID and freeze the text.

If the output is truncated, tool access fails, or the response is otherwise incomplete, record the run as `INCOMPLETE` rather than reconstructing the missing content.

## 5. Evaluation phase

Only after the Candidate is frozen may the evaluator load:

- the Candidate;
- the benchmark case;
- the applicable evaluation criteria;
- the original fixture where relevant.

The evaluator records observations before proposing any fix.

## 6. Independence limitation

Manual execution in the same model/session family does not establish statistical or model-level independence between Builder and Evaluator.

Therefore every manual run must expose:

`evaluation_independence: LIMITED`

unless a genuinely separate evaluator runtime is used.

This limitation does not invalidate the evidence; it limits the strength of claims made from it.

## 7. Baseline sequence

Run the baseline in this order:

`A → E → F → G → B → C → D`

The Builder version must remain identical throughout the baseline.

A failure in one case must not trigger a Builder edit before the remaining baseline cases are completed.

## 8. Case record template

Every run must save:

### Metadata
- Run ID
- Case ID
- Builder SHA
- Benchmark version
- Fixture/version
- Model/runtime
- Date/time
- execution_independence
- status

### Builder packet
- exact input/context supplied

### Candidate
- complete unedited output
- Candidate ID

### Evaluation
- observed strengths
- observed failures
- failure labels
- severity
- evidence

### Diagnosis
- primary failure
- root-cause hypothesis
- confidence

### Decision
- no change / change candidate / blocked
- reason
- affected regression cases

## 9. Operator contamination controls

The operator must not:

- silently improve the Builder prompt while running it;
- provide a better example after seeing the Candidate;
- retry a poor Candidate and keep only the best result without recording all attempts;
- select favorable outputs from multiple runs;
- edit the Candidate before evaluation;
- tell the evaluator which result is expected;
- turn an inference into an observed fact.

If a retry is necessary because of a genuine execution failure, record the failed attempt and the reason for retry.

## 10. Retry policy

A substantive Builder failure is not a reason for retrying merely to obtain a better result.

Only execution failures justify retrying, such as:

- transport failure;
- truncated response;
- unavailable required tool;
- invalid session state;
- accidental contamination before Candidate capture.

The original failed attempt must remain in the evidence record.

## 11. Promotion gate

A manual baseline does not authorize Builder modification by itself.

After A–G are complete, aggregate failures and identify common root causes. Only then may the project propose a minimal Builder revision and define regression cases.

## 12. Final honesty rule

If evidence is missing, say `UNKNOWN`, `INCOMPLETE`, or `RUNTIME-PENDING`.

Never convert a plausible analysis into an executed result.
