# Implementation Plan

## Scope

Update: `system-maintenance-retrospective-0014.1`

Step: `step-001`

Name: Canonical Sketchnote Prompt Integration

Goal: prepare the system to use a manually maintained canonical generation
prompt for `visual_article_sketchnote`.

## Context

Several `visual_article_sketchnote` runs drifted into infographic, SVG scheme,
or corporate one-pager outputs. A user-maintained canonical sketchnote prompt
will become the genre and visual-execution source for this mode.

This step creates the placeholder and integrates it. It does not create or edit
the real prompt content.

## Implementation Steps

1. Create `ai-editorial-office/kb/canonical_sketchnote_prompt.md` as a
   placeholder.
2. Update `ai-editorial-office/agents/artist_agent.md` so
   `visual_article_sketchnote` uses approved `visual_concept.md`, approved
   `sketchnote_brief.md`, and `kb/canonical_sketchnote_prompt.md`.
3. State that the canonical sketchnote prompt is the source of genre and visual
   execution.
4. State that when the canonical prompt exists and is not empty with manually
   supplied prompt content beyond the placeholder, it has priority over generic
   sketchnote generation logic.
5. Update `image_prompt_template.md` so it references
   `canonical_sketchnote_prompt.md` as a required source for
   `visual_article_sketchnote`.
6. Record changed files, decisions, safety check, rollback notes, and semantic
   diff.

## Non-Goals

- Do not create, fill, optimize, summarize, or rewrite the canonical prompt.
- Do not change `visual_concept`.
- Do not change `sketchnote_brief`.
- Do not change review system.
- Do not change pipelines.
- Do not change visual modes.
- Do not change ordinary illustration branch.

## Status

Completed.
