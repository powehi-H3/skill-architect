#!/usr/bin/env python3
"""Generic static contract auditor for a Skill under test.

This audit never claims LLM execution. It checks only repository-visible
structure and evidence-boundary markers.
"""
from __future__ import annotations
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

def lower(s: str) -> str:
    return s.lower()

def group_hit(text: str, patterns: list[str]) -> bool:
    return any(re.search(p, text, re.I) for p in patterns)

def audit(skill_path: Path, manifest: dict) -> dict:
    text = skill_path.read_text(encoding="utf-8")
    low = lower(text)
    findings = []
    groups = {}
    for name, patterns in SEMANTIC_GROUPS.items():
        hit = group_hit(text, patterns)
        groups[name] = hit
        if not hit:
            findings.append({
                "id": f"STATIC-{name.upper()}",
                "severity": "major",
                "status": "FAIL",
                "message": f"no recognizable {name} contract marker found",
            })

    size = len(text)
    if size < manifest.get("min_chars", 1000):
        findings.append({
            "id": "STATIC-SIZE",
            "severity": "major",
            "status": "FAIL",
            "message": f"skill is unexpectedly small: {size} chars",
        })

    # Explicitly reject evidence inflation if the document claims actual
    # execution without a matching execution-evidence marker in the same file.
    execution_claims = re.findall(
        r"(?:real|actual|successfully|completed).{0,80}(?:execution|run|test)",
        text,
        flags=re.I,
    )
    if execution_claims and not re.search(r"(?:execution evidence|run id|trace id|recorded run|REAL-LLM)", text, re.I):
        findings.append({
            "id": "STATIC-EVIDENCE-CLAIM",
            "severity": "critical",
            "status": "FAIL",
            "message": "possible execution claim without recognizable execution evidence marker",
        })

    result = {
        "target": manifest.get("target_id", skill_path.name),
        "skill_path": str(skill_path),
        "skill_sha256": __import__("hashlib").sha256(text.encode("utf-8")).hexdigest(),
        "chars": size,
        "evidence_state": "STATIC-AUDIT",
        "llm_executed": False,
        "groups": groups,
        "findings": findings,
        "status": "FAIL" if any(f["status"] == "FAIL" for f in findings) else "PASS",
    }
    return result

def main() -> int:
    if len(sys.argv) != 3:
        print("usage: audit_skill_static_v1.py <skill.md> <manifest.json>", file=sys.stderr)
        return 2
    skill = Path(sys.argv[1])
    manifest = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    if not skill.exists():
        print(json.dumps({"status":"FAIL","error":"skill file not found"}))
        return 1
    result = audit(skill, manifest)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
