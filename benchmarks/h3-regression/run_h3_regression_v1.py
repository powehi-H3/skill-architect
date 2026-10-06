#!/usr/bin/env python3
"""Deterministic/static H3 Skill regression contract. Never calls an LLM or H3."""
import json, hashlib, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CASES=ROOT/"benchmarks/h3-regression/cases.json"
def main():
    cases=json.loads(CASES.read_text(encoding="utf-8"))
    if len(sys.argv)!=2:
        print(json.dumps({"status":"BLOCKED","reason":"local frozen Skill input required","evidence_state":"OFFLINE-STATIC","llm_executed":False},ensure_ascii=False)); return 2
    skill_path=Path(sys.argv[1])
    if not skill_path.exists():
        print(json.dumps({"status":"BLOCKED","reason":"Skill input not found","evidence_state":"OFFLINE-STATIC","llm_executed":False},ensure_ascii=False)); return 2
    skill=skill_path.read_text(encoding="utf-8")
    globals_=["Universal H3 Output Contract","Output-Type Gate","H3 Schema Lock","Experience Reference Check","H3 Payload Contract","Final H3 Output Gate"]
    results=[]
    for case in cases["cases"]:
        missing=[x for x in case["requirements"] if x.lower() not in skill.lower()]
        results.append({"case_id":case["case_id"],"status":"PASS" if not missing else "FAIL","missing":missing})
    gm=[x for x in globals_ if x.lower() not in skill.lower()]
    out={"suite":cases["suite"],"status":"PASS" if not gm and all(x["status"]=="PASS" for x in results) else "FAIL","evidence_state":"OFFLINE-STATIC","llm_executed":False,"semantic_quality_proven":False,"skill_sha256":hashlib.sha256(skill.encode()).hexdigest(),"global_missing":gm,"cases":results}
    print(json.dumps(out,ensure_ascii=False,indent=2)); return 0 if out["status"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
