# Failure Pattern: Duplicated Authority Chains

## Pattern
A Skill contains more than one precedence/authority ladder that is individually reasonable but not formally identical.

## Why it matters
Long-context models may select different ladders depending on where they encounter the conflict. This can cause:
- current user instruction to lose to source conventions;
- historical approved prompts to override current instructions;
- project overrides to be inconsistently applied;
- source observations to be promoted into requirements.

## Detection
Search the active Skill for multiple normative phrases such as:
- priority
- precedence
- authority
- higher-priority
- conflict resolution
- source wins
- user wins

Then compare the ladders semantically, not only lexically.

## Expected remediation
Create one canonical authority ladder in the active execution section.
Historical sections may remain as documentation only if they are clearly non-normative and point to the canonical SSOT.

## Evidence classification
This pattern was found in H3 V0.3 during CHATGPT-SEMANTIC-EXECUTION audit.
It is not MiniMax H3 runtime evidence.
