#!/usr/bin/env python3
"""Generic real-LLM runner for a Skill under test.

The Skill is frozen before the evaluator sees any output. Builder/Skill execution
and evaluation are separate API calls. This runner requires OPENAI_API_KEY and
an explicit OPENAI_MODEL; it never supplies a model default.
"""
from __future__ import annotations
import hashlib, json, os, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

def api_call(model: str, instructions: str, user_input: str) -> dict:
    key=os.environ.get("OPENAI_API_KEY","")
    if not key: raise RuntimeError("OPENAI_API_KEY is not available")
    payload={"model":model,"instructions":instructions,"input":user_input,"store":False,"max_output_tokens":8000}
    req=Request("https://api.openai.com/v1/responses",data=json.dumps(payload).encode(),
                headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},method="POST")
    try:
        with urlopen(req,timeout=180) as r: return json.loads(r.read().decode())
    except HTTPError as e: raise RuntimeError(f"OpenAI API HTTP {e.code}: {e.read().decode(errors='replace')[:2000]}")
    except URLError as e: raise RuntimeError(f"OpenAI API network error: {e}")

def output_text(r:dict)->str:
    out=[]
    for item in r.get("output",[]):
        for c in item.get("content",[]) or []:
            if c.get("type")=="output_text" and isinstance(c.get("text"),str): out.append(c["text"])
    text="\n".join(out).strip()
    if not text: raise RuntimeError("model returned no output_text")
    return text

def main()->int:
    if len(sys.argv)!=5:
        print("usage: run_skill_under_test_openai_v1.py <skill.md> <cases.json> <output-dir> <manifest.json>",file=sys.stderr); return 2
    skill=Path(sys.argv[1])
    cases=json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    manifest=json.loads(Path(sys.argv[4]).read_text(encoding="utf-8"))
    model=os.environ.get("OPENAI_MODEL","").strip()
    if not model: print("ERROR: OPENAI_MODEL is required",file=sys.stderr); return 2
    text=skill.read_text(encoding="utf-8")
    out=Path(sys.argv[3]); out.mkdir(parents=True,exist_ok=True)
    run_id=datetime.now(timezone.utc).strftime("SKILL-UT-OPENAI-%Y%m%dT%H%M%SZ")
    run=out/run_id; run.mkdir()
    skill_sha=hashlib.sha256(text.encode()).hexdigest()
    (run/"skill.sha256").write_text(skill_sha+"\n")
    meta={"run_id":run_id,"evidence_state":"REAL-LLM","llm_executed":True,"model":model,
          "skill_id":manifest.get("skill_id"),"display_name":manifest.get("display_name"),
          "declared_version":manifest.get("declared_version"),
          "skill_path":str(skill),"skill_sha256":skill_sha,
          "started_at":datetime.now(timezone.utc).isoformat(),"case_count":len(cases)}
    (run/"run-metadata.json").write_text(json.dumps(meta,indent=2,ensure_ascii=False),encoding="utf-8")
    evaluator_instructions="""You are an independent evaluator. The candidate output below was produced by a separate model call using a frozen Skill. Judge only the supplied task and output. Do not rewrite it.
Return:
## Verdict
PASS / NEEDS REVISION / FAIL / UNKNOWN
## Findings
Concrete observed defects or strengths.
## Evidence boundary
What was directly observed versus inferred.
"""
    for case in cases:
        cid=case["case_id"]; prompt=case["prompt"]; expected=case.get("expected_invariants",[])
        exec_input=f"""TASK:
{prompt}

Produce the requested result using the supplied Skill. Do not discuss this evaluation harness."""
        t=time.time()
        raw=api_call(model,text,exec_input); candidate=output_text(raw)
        (run/f"case-{cid}-candidate.txt").write_text(candidate,encoding="utf-8")
        eval_input=f"""TASK:
{prompt}

EXPECTED INVARIANTS:
{json.dumps(expected,ensure_ascii=False,indent=2)}

FROZEN CANDIDATE:
---
{candidate}
---
"""
        ev=output_text(api_call(model,evaluator_instructions,eval_input))
        (run/f"case-{cid}-evaluation.md").write_text(ev,encoding="utf-8")
        (run/f"case-{cid}-record.json").write_text(json.dumps({
            "case_id":cid,"status":"EXECUTED","duration_seconds":round(time.time()-t,2),
            "candidate":f"case-{cid}-candidate.txt","evaluation":f"case-{cid}-evaluation.md",
            "expected_invariants":expected
        },indent=2,ensure_ascii=False),encoding="utf-8")
    meta["completed_at"]=datetime.now(timezone.utc).isoformat()
    (run/"run-metadata.json").write_text(json.dumps(meta,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps({"status":"PASS","run_id":run_id,"evidence_state":"REAL-LLM","model":model,
                      "skill_id":manifest.get("skill_id"),"declared_version":manifest.get("declared_version")},ensure_ascii=False))
    return 0

if __name__=="__main__": raise SystemExit(main())
