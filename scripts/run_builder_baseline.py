#!/usr/bin/env python3
"""Run Skill Builder V0.2 against the frozen V0 benchmark and independently evaluate each candidate.

This is an evidence runner, not a promotion engine. It preserves the raw Builder response and the
separate evaluator response for every case. It intentionally uses the OpenAI Responses API directly
so the runtime has minimal dependencies.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("RUN_OUTPUT_DIR", ROOT / "artifacts" / "builder-baseline"))
MODEL = os.environ.get("OPENAI_MODEL", "").strip()
ORDER = ["A", "E", "F", "G", "B", "C", "D"]
BUILDER_PATH = ROOT / "docs" / "SKILL-BUILDER-V0.2-CANDIDATE.md"
BENCHMARK_PATH = ROOT / "benchmarks" / "BUILDER-BENCHMARK-V0.md"
FIXTURE_G = ROOT / "benchmarks" / "fixtures" / "case-g-existing-skill.md"


def die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def api_call(instructions: str, user_input: str) -> dict:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        die("OPENAI_API_KEY is not available. Add it as a repository Actions secret.")
    if not MODEL:
        die("OPENAI_MODEL is required. Supply the exact model identifier at workflow dispatch.")
    payload = {
        "model": MODEL,
        "instructions": instructions,
        "input": user_input,
        "max_output_tokens": 7000,
        "store": False,
    }
    req = Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=180) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        die(f"OpenAI API HTTP {e.code}: {body[:2000]}")
    except URLError as e:
        die(f"OpenAI API network error: {e}")


def output_text(response: dict) -> str:
    chunks: list[str] = []
    for item in response.get("output", []):
        for content in item.get("content", []) or []:
            if content.get("type") == "output_text" and isinstance(content.get("text"), str):
                chunks.append(content["text"])
    text = "\n".join(chunks).strip()
    if not text:
        die("OpenAI response contained no output_text.")
    return text


def parse_cases(markdown: str) -> dict[str, dict[str, str]]:
    pattern = re.compile(r"^## \d+\. Case ([A-G]) — (.+)$", re.M)
    matches = list(pattern.finditer(markdown))
    cases: dict[str, dict[str, str]] = {}
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else markdown.find("## 9. Scoring dimensions")
        block = markdown[m.end():end].strip()
        prompt_match = re.search(r"\*\*Prompt:\*\*\s*\n\s*>\s*(.*?)(?=\n\s*\*\*Purpose:\*\*)", block, re.S)
        expected_match = re.search(r"\*\*Expected properties:\*\*\s*\n(.*?)(?=\n\s*\*\*Failure signals:\*\*)", block, re.S)
        if not prompt_match or not expected_match:
            die(f"Could not parse benchmark case {m.group(1)}")
        prompt = re.sub(r"\n\s*>\s*", " ", prompt_match.group(1)).strip()
        expected = expected_match.group(1).strip()
        cases[m.group(1)] = {"title": m.group(2).strip(), "prompt": prompt, "expected": expected}
    return cases


def builder_instructions(builder_spec: str) -> str:
    return f"""You are the Skill Builder under test. Follow ONLY the Builder specification below plus the case input supplied by the harness.

BUILDER SPECIFICATION (authoritative runtime dependency):
---
{builder_spec}
---

This is a black-box benchmark. Do not mention the benchmark rubric, expected properties, scoring, evaluator, or hidden test logic. Do not claim that you tested or verified anything unless the case input itself supplies evidence of such execution. Produce the complete candidate Builder result requested by the task."""


def evaluator_instructions() -> str:
    return """You are an independent evaluator for a Skill Builder benchmark. You did NOT generate the candidate. Evaluate the frozen candidate against the supplied case prompt and expected properties. Do not rewrite the candidate. Distinguish direct observations from inference. Never claim that an event occurred unless it is visible in the supplied evidence.

Return a concise but complete evaluation with exactly these headings:
## Verdict
## Score
## Observed
## Failures
## Root-cause hypothesis
## Smallest justified Builder change
## Regression cases
## Evidence boundary

For Score, give each applicable dimension 0-2 and a total, but do not let the total replace qualitative severity. Use PASS / NEEDS REVISION / FAIL only as an evaluator disposition, not as proof of execution."""


def main() -> None:
    if not MODEL:
        die("OPENAI_MODEL is required. Supply the exact model identifier at workflow dispatch.")

    OUT.mkdir(parents=True, exist_ok=True)
    builder_spec = BUILDER_PATH.read_text(encoding="utf-8")
    benchmark = BENCHMARK_PATH.read_text(encoding="utf-8")
    cases = parse_cases(benchmark)
    missing = [c for c in ORDER if c not in cases]
    if missing:
        die(f"Missing benchmark cases: {missing}")

    run_id = datetime.now(timezone.utc).strftime("BUILDER-V0.2-OPENAI-%Y%m%dT%H%M%SZ")
    run_dir = OUT / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    metadata = {
        "run_id": run_id,
        "evidence_state": "EXECUTED",
        "builder_version": os.environ.get("BUILDER_VERSION", "UNKNOWN"),
        "benchmark_version": "BUILDER-BENCHMARK-V0",
        "model": MODEL,
        "execution_surface": "GitHub Actions + OpenAI Responses API",
        "evaluator_version": "OPENAI-AUTOMATED-EVALUATOR-V0",
        "started_at": datetime.now(timezone.utc).isoformat(),
        "case_order": ORDER,
    }
    (run_dir / "run-metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    summary = []
    for case_id in ORDER:
        case = cases[case_id]
        context = f"CASE {case_id} — {case['title']}\n\nTASK INPUT:\n{case['prompt']}"
        if case_id == "G":
            context += "\n\nEXPLICITLY PROVIDED EXISTING SKILL FIXTURE:\n" + FIXTURE_G.read_text(encoding="utf-8")
        print(f"[Builder] Case {case_id} ...", flush=True)
        started = time.time()
        builder_response = api_call(builder_instructions(builder_spec), context)
        candidate = output_text(builder_response)
        frozen_path = run_dir / f"case-{case_id}-candidate.txt"
        frozen_path.write_text(candidate, encoding="utf-8")

        evaluator_input = f"""CASE {case_id} — {case['title']}

CASE PROMPT:
{case['prompt']}

EXPECTED PROPERTIES:
{case['expected']}

FROZEN BUILDER CANDIDATE (evaluate exactly as captured; do not edit):
---
{candidate}
---

Benchmark rule: the candidate must be judged on behavior, not on the presence of familiar headings."""
        print(f"[Evaluator] Case {case_id} ...", flush=True)
        evaluator_response = api_call(evaluator_instructions(), evaluator_input)
        evaluation = output_text(evaluator_response)
        (run_dir / f"case-{case_id}-evaluation.md").write_text(evaluation, encoding="utf-8")

        record = {
            "run_id": run_id,
            "case_id": case_id,
            "title": case["title"],
            "builder_version": metadata["builder_version"],
            "benchmark_version": metadata["benchmark_version"],
            "model": MODEL,
            "status": "EXECUTED",
            "duration_seconds": round(time.time() - started, 2),
            "input": context,
            "candidate_file": frozen_path.name,
            "evaluation_file": f"case-{case_id}-evaluation.md",
            "evidence_boundary": "Builder and evaluator were separate API calls; evaluator received the frozen candidate after capture.",
        }
        (run_dir / f"case-{case_id}-record.json").write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
        summary.append({"case": case_id, "status": "EXECUTED", "candidate": frozen_path.name, "evaluation": f"case-{case_id}-evaluation.md"})

    metadata["completed_at"] = datetime.now(timezone.utc).isoformat()
    metadata["cases_completed"] = len(summary)
    (run_dir / "run-metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (run_dir / "SUMMARY.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({"run_id": run_id, "cases": summary}, indent=2), flush=True)


if __name__ == "__main__":
    main()
