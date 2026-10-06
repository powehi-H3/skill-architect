#!/usr/bin/env python3
"""Generic static contract auditor for a Skill under test.

This audit never claims LLM execution. It checks repository-visible structure,
identity metadata, and evidence-boundary markers.
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

SEMANTIC_GROUPS = {
    "boundary": [r"purpose", r"scope", r"trigger", r"boundary"],
    "inputs": [r"input", r"required", r"context", r"reference"],
    "outcome": [r"output", r"result", r"outcome", r"payload"],
    "quality": [r"quality", r"success", r"validation", r"constraint"],
    "failure": [r"failure", r"uncertain", r"ambigu", r"missing", r"error"],
    "evidence": [r"evidence", r"verified", r"baseline", r"provenance"],
}

REQUIRED_IDENTITY = {"skill_id", "display_name", "declared_version", "source"}
REQUIRED_SOURCE = {"repository", "ref", "skill_path", "active_pointer", "artifact_filename"}

def group_hit(text: str, patterns: list[str]) -> bool:
    return any(re.search(p, text, re.I) for p in patterns)

def validate_identity(manifest: dict) -> list[dict]:
    findings = []
    missing = sorted(REQUIRED_IDENTITY - set(manifest))
    if missing:
        findings.append({"id":"STATIC-IDENTITY-MISSING","severity":"critical","status":"FAIL",
                         "message":f"missing identity fields: {', '.join(missing)}"})
    source = manifest.get("source")
    if not isinstance(source, dict):
        findings.append({"id":"STATIC-SOURCE-MISSING","severity":"critical","status":"FAIL",
                         "message":"source must be an object containing repository/ref/path metadata"})
        return findings
    missing_source = sorted(REQUIRED_SOURCE - set(source))
    if missing_source:
        findings.append({"id":"STATIC-SOURCE-METADATA-MISSING","severity":"critical","status":"FAIL",
                         "message":f"missing source fields: {', '.join(missing_source)}"})
    if not isinstance(manifest.get("skill_id"), str) or not manifest["skill_id"].strip():
        findings.append({"id":"STATIC-SKILL-ID-INVALID","severity":"critical","status":"FAIL",
                         "message":"skill_id must be a non-empty permanent identity"})
    if not isinstance(manifest.get("declared_version"), str) or not re.fullmatch(r"V\d+(?:\.\d+)+", manifest["declared_version"].strip()):
        findings.append({"id":"STATIC-VERSION-INVALID","severity":"major","status":"FAIL",
                         "message":"declared_version must use V<major>.<minor> form"})
    return findings

def audit(skill_path: Path, manifest: dict) -> dict:
    text = skill_path.read_text(encoding="utf-8")
    findings = validate_identity(manifest)
    groups = {}
    for name, patterns in SEMANTIC_GROUPS.items():
        hit = group_hit(text, patterns)
        groups[name] = hit
        if not hit:
            findings.append({"id":f"STATIC-{name.upper()}","severity":"major","status":"FAIL",
                             "message":f"no recognizable {name} contract marker found"})
    size = len(text)
    if size < manifest.get("min_chars", 1000):
        findings.append({"id":"STATIC-SIZE","severity":"major","status":"FAIL",
                         "message":f"skill is unexpectedly small: {size} chars"})
    execution_claims = re.findall(r"(?:real|actual|successfully|completed).{0,80}(?:execution|run|test)", text, flags=re.I)
    if execution_claims and not re.search(r"(?:execution evidence|run id|trace id|recorded run|REAL-LLM)", text, re.I):
        findings.append({"id":"STATIC-EVIDENCE-CLAIM","severity":"critical","status":"FAIL",
                         "message":"possible execution claim without recognizable execution evidence marker"})
    result = {
        "identity":{"skill_id":manifest.get("skill_id"),"display_name":manifest.get("display_name"),
                    "declared_version":manifest.get("declared_version")},
        "target":manifest.get("skill_id", skill_path.name),
        "skill_path":str(skill_path),
        "skill_sha256":hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "chars":size,"evidence_state":"STATIC-AUDIT","llm_executed":False,
        "groups":groups,"findings":findings,
        "status":"FAIL" if any(f["status"]=="FAIL" for f in findings) else "PASS",
    }
    return result

def main() -> int:
    if len(sys.argv) != 3:
        print("usage: audit_skill_static_v1.py <skill.md> <manifest.json>", file=sys.stderr); return 2
    skill = Path(sys.argv[1])
    manifest = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    if not skill.exists():
        print(json.dumps({"status":"FAIL","error":"skill file not found"})); return 1
    result = audit(skill, manifest)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
