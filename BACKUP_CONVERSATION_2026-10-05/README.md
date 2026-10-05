# Skill Architect — Conversation Backup

Backup created at the user's request on 2026-10-05.

## Important scope note

This folder is a **conversation-recovery backup**, not a byte-for-byte export of the private ChatGPT transcript.

The GitHub connector can write files to this repository, but it does not expose the complete hidden conversation transcript, including every skipped/compacted message. Therefore it would be incorrect to claim that this folder contains every message verbatim.

This backup contains the project context and the conversation-derived decisions that are currently available to the assistant, plus the current implementation state. It is intended to make the project recoverable if the chat becomes too long.

## Files

- `CHAT_RECOVERY.md` — consolidated conversation/project decisions available from the current context.
- `PROJECT_STATE.md` — current technical state and known blockers.

## Preservation rule

Do not treat this backup as a replacement for the Git history. The repository commits remain the authoritative record of actual project-file changes.
