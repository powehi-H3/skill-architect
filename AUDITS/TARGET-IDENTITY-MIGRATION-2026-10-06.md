# TARGET IDENTITY MIGRATION AUDIT — 2026-10-06

## Scope

Normalized Skill Architect's H3 target identity/version/name model and removed version-coupled active target paths.

## Canonical identity

- skill_id: `minimax-h3-prompt-skill`
- current display_name: `H3提示词技能 Skill`
- current declared_version: `V0.3`
- source repository: `powehi-H3/minimax-h3-NSFW-skill`
- stable active mirror:
  `PROJECT/ACTIVE-SKILL/h3-prompt-skill-current/SKILL.md`

## Changes

1. Added `targets/TARGET-IDENTITY-SCHEMA-V1.md`.
2. Replaced version-coupled `targets/h3-v0.3.json` with `targets/h3-active.json`.
3. Replaced version-coupled `targets/h3-v0.3/cases.json` with `targets/h3-active/cases.json`.
4. Updated static audit workflow to the stable target manifest/path.
5. Updated real-runtime workflow to the stable target manifest/path.
6. Updated the real-runtime runner so evidence records carry:
   - skill_id
   - display_name
   - declared_version
   - skill_sha256
7. Updated the static auditor so missing/invalid identity metadata is a hard finding.
8. Removed the old version-coupled target manifest and case path.

## H3 repository verification

Current active mirror:
`PROJECT/ACTIVE-SKILL/h3-prompt-skill-current/`

The repository tree contains no active path named:
- `h3-nsfw-unified-experimental`
- `README-UNIFIED-EXPERIMENTAL.md`

The active pointer and sync workflow both use the stable mirror path.

## Version/name behavior

### Version bump
V0.3 → V0.4:
- same skill_id
- new declared_version
- new artifact filename
- same current mirror path

### Name change
`H3提示词技能 Skill` → another display name:
- same skill_id
- new display_name
- version changes independently

### Identity-breaking change
Only an explicit project decision creates a new skill_id.

## Evidence boundary

No real LLM or MiniMax H3 execution was performed by this migration.

The local container could not resolve `raw.githubusercontent.com`, so no local runtime test is claimed from that environment.

Repository-level verification completed:
- current H3 mirror path exists and `SKILL.md` is readable
- Skill Architect current target manifest exists
- old version-coupled target files are removed
- old H3 active directory name is absent from the repository tree
- current static/runtime workflow definitions reference the stable path
- historical V0.3 audit filenames remain as historical evidence only
