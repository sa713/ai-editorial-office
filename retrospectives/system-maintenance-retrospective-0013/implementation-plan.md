# Implementation Plan

## Scope

Update: `system-maintenance-retrospective-0013`

Goal: add `visual_article_sketchnote` as a separate visual editorial mode for
handwritten article sketchnotes, without changing ordinary text pipelines or
turning the illustration branch into a broader design system.

## Implementation Steps

1. Add `visual_article_sketchnote` to `editorial_knowledge/20_editorial_modes.md`.
2. Define the reader goal, useful outcome, reader state, output character,
   boundaries, and anti-patterns for article sketchnotes.
3. Create `ai-editorial-office/templates/artifacts/sketchnote_brief_template.md`
   with `sketchnote_brief.md` as the output artifact.
4. Update `AGENTS.md` so the visual branch activates this mode when the user
   asks for a visual article sketchnote, handwritten summary, one-sheet note, or
   similar phrasing.
5. Minimally update Artist Agent so it may use an approved
   `sketchnote_brief.md` to prepare `image_prompt.md`.
6. Update `image_prompt_template.md` so `image_prompt.md` can be sourced from
   either `illustration_brief.md` or `sketchnote_brief.md`.
7. Add compact review checks for `visual_article_sketchnote` and
   `sketchnote_brief.md` -> `image_prompt.md` prompt drift.
8. Record decisions, changed files, safety checks, rollback notes, and semantic
   diff in this retrospective folder.

## Non-Goals

- No new agent.
- No new pipeline.
- No comic mode.
- No presentation mode.
- No separate design system.
- No complex sketchnote methodology.
- No OCR requirements.
- No artistic quality scoring.
- No broad rewrite of `visual_illustration_brief`.
- No changes to ordinary text pipelines.

## Status

Completed.
