#!/usr/bin/env python3
"""Detect potentially duplicated normative authority/priority ladders."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

KEYWORDS = re.compile(r"\b(priority|precedence|authority|higher[- ]priority|conflict resolution|source[s]? conflict)\b", re.I)
ARROW = re.compile(r"(?:→|->|=>)")
CHAIN_HINT = re.compile(r"(user|source|project|skill|H3|reference|prompt|knowledge|default|approved|historical)", re.I)

def normalize(line: str) -> str:
    line = re.sub(r"[*_#]+", "", line)
    line = re.sub(r"\s+", " ", line).strip()
    return line

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: audit_authority_consistency_v1.py <skill.md>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(json.dumps({"status":"FAIL","error":"skill file not found"}))
        return 1
    text = path.read_text(encoding="utf-8")
    candidates = []
    for raw in text.splitlines():
        line = normalize(raw)
        if KEYWORDS.search(line) and ARROW.search(line) and CHAIN_HINT.search(line):
            candidates.append(line)
    distinct = list(dict.fromkeys(candidates))
    result = {
        "skill_path": str(path),
        "evidence_state": "STATIC-AUTHORITY-HEURISTIC",
        "llm_executed": False,
        "candidate_ladders": distinct,
        "candidate_count": len(distinct),
        "status": "NEEDS_REVIEW" if len(distinct) > 1 else "PASS",
        "message": (
            "multiple distinct authority/priority ladders detected; compare them against one canonical SSOT"
            if len(distinct) > 1 else
            "no duplicated arrow-style authority ladder detected"
        )
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
