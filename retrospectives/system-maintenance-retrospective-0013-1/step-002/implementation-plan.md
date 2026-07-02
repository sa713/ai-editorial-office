# Implementation Plan

## Scope

Update: `system-maintenance-retrospective-0013.1`

Step: `step-002`

Goal: add sketchnote execution discipline so Artist Agent treats
`visual_article_sketchnote` as a distinct visual genre instead of drifting into
infographic, SVG, HTML, or corporate one-pager execution.

## Context

The first production run for `TASK-0017` selected the sketchnote mode but
failed at execution: the output became an infographic/SVG/HTML-style corporate
one-pager rather than a handwritten reader's note sheet.

This step addresses execution behavior only.

## Implementation Steps

1. Update `ai-editorial-office/agents/artist_agent.md`.
2. Add execution mode `visual_article_sketchnote`.
3. Define required sketchnote signals: one sheet of paper, coherent spread,
   handwritten notes, liner drawings, arrows, labels, relationships, small
   visual metaphors, and live thinking-process feeling.
4. Define genre prohibitions: infographic, slide, poster, ad, corporate
   one-pager, UI mockup, card set, digital scheme, web page, and interactive
   artifact.
5. Define visual prohibitions: strict grid, perfect alignment, symmetry,
   identical blocks, presentation feeling, corporate design feeling, and
   AI-collage feeling.
6. Set PNG as the standard final image result for `visual_article_sketchnote`.
7. Update `image_prompt_template.md` with sketchnote-specific prompt fields:
   genre constraints, handwritten note constraints, one-sheet constraints, and
   anti-infographic constraints.
8. Record changed files, decisions, safety check, rollback notes, and semantic
   diff.

## Non-Goals

- No `visual_concept.md` changes.
- No `sketchnote_brief.md` changes.
- No ordinary illustration branch changes.
- No new agent.
- No new pipeline.
- No review-system change.
- No comic mode.
- No presentation mode.

## Status

Completed.
