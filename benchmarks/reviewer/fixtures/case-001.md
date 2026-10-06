---
name: concise-text-normalizer
description: Normalize short user-provided text into a clean, readable form while preserving requested meaning and constraints.
---

# Purpose

Transform short user-provided text into a concise, readable version.

# Workflow

1. Identify the user's requested transformation.
2. Preserve meaning, required facts, names, numbers, and explicit constraints.
3. Remove unnecessary repetition and improve readability.
4. Return only the transformed text unless the user asks for explanation.

# Constraints

- Do not invent facts.
- Do not silently change the user's requested meaning.
- Preserve explicit formatting requirements when they are part of the task.
- If required information is missing, make the most reasonable assumption from surrounding context so the task can still be completed.

# Failure handling

If a required input is missing or ambiguous, infer the most likely intended value from nearby context and continue. Avoid asking follow-up questions for minor uncertainty.

# Example

Input:
"Rewrite this exactly, keeping the numbered list and the capitalization."

Output:
"Rewrite this exactly while keeping the list structure and normalizing capitalization for readability."

# Output contract

Return the transformed text only.
