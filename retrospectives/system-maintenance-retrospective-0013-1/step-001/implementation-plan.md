# Implementation Plan

## Scope

Update: `system-maintenance-retrospective-0013.1`

Step: `step-001`

Goal: restore `visual_concept.md` as the required semantic frame upstream of
`sketchnote_brief.md` for `visual_article_sketchnote`.

## Context

The first production run showed that direct `article -> sketchnote_brief.md`
was too close to execution. The meaning layer was not separated enough, and the
result drifted toward infographic/SVG/HTML execution instead of a handwritten
sketchnote.

## Target Path

```text
article
↓
visual_concept.md
↓
sketchnote_brief.md
↓
Artist Agent
↓
image_prompt.md / PNG
```

This step only restores the upstream semantic frame. It does not add PNG rules
or change Artist Agent execution.

## Implementation Steps

1. Update `visual_article_sketchnote` in
   `editorial_knowledge/20_editorial_modes.md`.
2. Define `visual_concept.md` as the sketchnote semantic frame, not an ordinary
   metaphorical illustration concept.
3. Specify that sketchnote `visual_concept.md` fixes central idea, 5-10 key
   meaning blocks, relationships, author conclusions, viewer memory, and
   emotional or intellectual feeling.
4. Update `sketchnote_brief_template.md` so its source artifact is approved
   `visual_concept.md`.
5. Update the sketchnote compact path in `AGENTS.md`.
6. Record decisions, changed files, safety check, rollback notes, and semantic
   diff.

## Non-Goals

- No Artist Agent file changes.
- No PNG rule.
- No failure pattern.
- No review-system change.
- No new pipeline.
- No new agent.
- No comic or presentation mode.

## Status

Completed.
