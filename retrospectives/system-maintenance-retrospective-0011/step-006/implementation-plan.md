# Step 6 Implementation Plan

## Scope

Step: `system-maintenance-retrospective-0011 / step-006`

Focus: add Artist Agent as an execution role and add the `image_prompt.md`
template.

Goal: let an executor convert approved `illustration_brief.md` into
`image_prompt.md` or an image when the environment allows, without taking over
semantic ownership from editorial artifacts.

## Context

Existing visual branch layers:

- `visual_illustration_brief` mode;
- visual meaning extraction;
- `visual_concept.md`;
- visual concept review;
- `illustration_brief.md`.

Step 6 adds:

- Artist Agent;
- `image_prompt.md` template.

## Implementation Steps

1. Create `ai-editorial-office/agents/artist_agent.md`.
2. Define Artist Agent as an execution role, not a semantic editor.
3. Require approved `visual_concept.md` and approved `illustration_brief.md`.
4. Define allowed outputs: `image_prompt.md` and optionally an image when the
   environment supports image creation.
5. Add forbidden actions against source-text analysis, meaning changes, comic
   drift, presentation drift, pipeline creation, and review-system ownership.
6. Create `ai-editorial-office/templates/artifacts/image_prompt_template.md`.
7. Define `image_prompt.md` as an Artist Agent execution artifact built on
   `illustration_brief.md`.
8. Leave pipelines, review system, `visual_concept_template.md`, and
   `illustration_brief_template.md` unchanged.

## Non-Goals

- No new pipeline.
- No review-system change.
- No change to `visual_concept_template.md`.
- No change to `illustration_brief_template.md`.
- No comics.
- No presentations.
- No Step 7 work.

## Status

Completed.
