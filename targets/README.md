# Skill-under-test targets

Skill Architect separates permanent Skill identity from mutable display name, version, and source location.

A target profile records:
- `skill_id`: permanent identity
- `display_name`: current human-facing name
- `declared_version`: current executable version
- `source`: repository, ref, active pointer, stable current mirror, and current artifact filename
- evidence policy and runtime state

The current mirror path is intentionally version-independent:
`PROJECT/ACTIVE-SKILL/h3-prompt-skill-current/SKILL.md`

Current first target:
- skill_id: `minimax-h3-prompt-skill`
- display name: `H3提示词技能 Skill`
- version: `V0.3`
- source: `powehi-H3/minimax-h3-NSFW-skill`

A future rename or version bump does not require a new target file. Only an explicit identity-breaking decision creates a new `skill_id`.

Evidence levels remain separate:
- STATIC-AUDIT: repository-visible inspection only
- REAL-LLM: actual model execution
- HUMAN-VERIFIED: human verification
- UNKNOWN: insufficient evidence

See `TARGET-IDENTITY-SCHEMA-V1.md` for the identity contract.
