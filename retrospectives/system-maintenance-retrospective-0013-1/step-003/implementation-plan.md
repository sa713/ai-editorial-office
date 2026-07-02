# Implementation Plan

## Scope

Update: `system-maintenance-retrospective-0013.1`

Step: `step-003`

Goal: add a new editorial failure pattern named
`Sketchnote → Infographic Drift`.

## Context

The first production run for `TASK-0017` showed a repeatable failure: a user
asked for a visual article sketchnote, but execution produced an infographic,
SVG/HTML artifact, and corporate one-pager feeling instead of a handwritten
reader's note sheet.

This step adds the failure pattern to editorial knowledge so future work can
name, detect, and repair the drift.

## Implementation Steps

1. Update `editorial_knowledge/50_editorial_failure_patterns.md`.
2. Add pattern `Sketchnote → Infographic Drift`.
3. Describe the failure as sketchnote work turning into infographic,
   presentation slide, corporate one-pager, UI-like scheme, or designed
   visualization.
4. Add symptoms, causes, risks, repair moves, and detection questions.
5. Scope the pattern only to `visual_article_sketchnote`.
6. Record changed files, decisions, safety check, rollback notes, and semantic
   diff.

## Non-Goals

- No Artist Agent changes.
- No `visual_concept.md` changes.
- No `sketchnote_brief.md` changes.
- No review-system changes.
- No new modes.
- No new agents.
- No new pipeline.
- No comic or presentation mode.

## Status

Completed.
