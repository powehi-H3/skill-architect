---
name: meeting-notes
version: 0.1
---

# Meeting Notes Skill

## 1. Scope
Turn a user's raw meeting notes into a concise, factual meeting record.
Do not invent decisions, owners, deadlines, or facts that are not present in the input.

## 2. Inputs
- Raw meeting notes or transcript excerpts.
- Optional meeting title and date.

## 3. Core Behavior
1. Extract decisions explicitly stated in the input.
2. Extract action items explicitly stated in the input.
3. Preserve uncertainty when ownership or deadlines are unclear.
4. Separate factual extraction from optional wording cleanup.

## 4. Output Contract
Return a bullet list with these sections, in this order:
- Decisions
- Action Items
- Open Questions

Each item must remain traceable to the supplied meeting material.

## 5. Quality Criteria
- No invented facts.
- No omitted explicit decisions.
- Unclear ownership remains marked as unclear.
- Output stays concise.

## 6. Failure Handling
If the notes are missing or empty, state that the required meeting material was not provided.
If the notes contain contradictions, preserve the contradiction and flag it rather than resolving it by invention.

## 7. Preservation Constraint
This Skill is already working. A requested change to one section must not silently rewrite unrelated sections or add new capabilities.
