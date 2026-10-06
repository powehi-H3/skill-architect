# Skill-under-test targets

This directory defines external or repository-local Skills that Skill Architect evaluates.

A target profile records identity, source location, version semantics, and evidence policy.
It does not copy the target Skill into Skill Architect.

Current first target:
- MiniMax H3 active Skill V0.3
- source: `powehi-H3/minimax-h3-NSFW-skill`
- current executable mirror: `PROJECT/ACTIVE-SKILL/h3-nsfw-unified-experimental/SKILL.md`

Evidence levels remain separate:
- STATIC-AUDIT: repository-visible inspection only
- REAL-LLM: actual model execution
- HUMAN-VERIFIED: human verification
- UNKNOWN: insufficient evidence
