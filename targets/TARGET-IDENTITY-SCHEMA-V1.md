# Target Identity Schema V1

Skill Architect separates identity, name, version, and location.

## Permanent identity

skill_id is the stable identity of a Skill.
It must not change merely because the Skill display name, version, ZIP filename, or current mirror contents change.

## Mutable metadata

display_name is the current human-facing Skill name.
declared_version is the current executable Skill version, using V<major>.<minor>.
source.artifact_filename is the current published ZIP filename.

These may change independently.

## Stable source path

The active readable mirror must use:

PROJECT/ACTIVE-SKILL/h3-prompt-skill-current/SKILL.md

The mirror directory is not a version identifier.

## Historical evidence

Every evidence record should preserve skill_id, display_name, declared_version, skill_sha256, source repository/ref, evidence state, and a run identifier when applicable.

## Version changes

V0.3 -> V0.4 keeps the same skill_id, changes declared_version and artifact_filename, and keeps the current mirror path.

## Name changes

A name-only change keeps the same skill_id and changes display_name. Version changes independently.

## Breaking identity change

Only an explicit project decision creates a new skill_id. A renamed Skill is not automatically a new Skill.