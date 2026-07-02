# Implementation Plan

## Scope

Update: `system-maintenance-retrospective-0015`

Step: `step-001`

Name: Visual Subsystem Freeze

Goal: preserve the visual subsystem in the repository while making it inactive
by default and experimental/frozen for ordinary editorial work.

## Context

The editorial system contains a visual subsystem:

- `visual_illustration_brief`;
- `visual_article_sketchnote`;
- Artist Agent;
- `visual_concept.md`;
- `illustration_brief.md`;
- `sketchnote_brief.md`;
- `image_prompt.md`;
- `canonical_sketchnote_prompt.md`;
- visual failure patterns.

After production tests, visual quality is considered unstable and not reliable
enough for active production use. Editorial focus returns to text tasks.

## Implementation Steps

1. Update `ai-editorial-office/AGENTS.md` with visual subsystem status:
   frozen / experimental.
2. State that visual modes, visual branch routing, Artist Agent, visual
   artifacts, canonical visual prompts, and visual failure patterns are
   preserved but inactive by default.
3. Replace automatic visual branch activation with explicit activation only:
   user must ask to use the visual subsystem, use Artist Agent, launch the
   visual branch, activate a visual mode, or otherwise clearly run the frozen
   visual subsystem.
4. Preserve existing mode-specific activation rules only for cases after
   explicit visual-subsystem activation.
5. Mark Artist Agent as frozen / experimental without deleting or rewriting its
   execution behavior.
6. Mark visual modes as inactive by default without deleting their knowledge.
7. Record changed files, decisions, safety check, rollback notes, and semantic
   diff.

## Non-Goals

- Do not delete visual subsystem files.
- Do not delete visual modes.
- Do not delete Artist Agent.
- Do not delete visual failure patterns.
- Do not change text modes.
- Do not change diagnostic analysis.
- Do not change author diagnostics.
- Do not change review system.
- Do not change pipelines.
- Do not change text roles.

## Status

Completed.
