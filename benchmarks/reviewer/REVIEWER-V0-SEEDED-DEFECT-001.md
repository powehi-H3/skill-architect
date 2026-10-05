# Reviewer V0 — Seeded Defect Test 001

## Purpose
Test whether Reviewer V0 can disagree with a superficially compliant Skill instead of echoing a checklist.

## Seed Skill characteristics
The fixture to be supplied to the Reviewer should:

- have a valid frontmatter name and description;
- contain all common sections expected by a simple Skill template;
- appear concise and professional;
- contain one hidden semantic defect in failure handling;
- contain one example that silently contradicts the stated preservation rule;
- contain no explicit benchmark labels.

## Expected invariant
A Reviewer should identify the semantic defect even though the Skill satisfies superficial structural checks.

## Anti-gaming requirement
Do not expose the exact defect category in the fixture filename or review prompt during the blind run. This document is the test specification, not the blind input.

## Pass condition
Reviewer returns NEEDS REVISION or FAIL with evidence that points to the actual semantic defect, rather than merely complaining about missing sections.

## Evidence boundary
Until a real blind execution is performed, this is only a test design artifact.
