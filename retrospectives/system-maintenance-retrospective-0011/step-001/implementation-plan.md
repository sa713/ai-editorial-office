# Step 1 Implementation Plan

## Scope

Step: `system-maintenance-retrospective-0011 / step-001`

Focus: add one editorial mode for preparing a meaning-based illustration brief from a text.

Goal: let the editorial system treat a text as a source of meaning for a future illustration without adding drawing, prompt-generation, comics, presentation, artist-agent, pipeline, template, or review-heuristic behavior.

## Discovery

The canonical place for editorial modes is:

- `editorial_knowledge/20_editorial_modes.md`

The file already contains named editorial modes such as `diagnostic_analysis` and `author_concept_diagnosis`, so the new mode was added as another named mode in the same knowledge file.

No pipeline, template, role, agent, or task scaffold needed changes for Step 1.

## Implementation Steps

1. Add `visual_illustration_brief` to `editorial_knowledge/20_editorial_modes.md`.
2. Define the reader goal around understanding the visual task of an illustration.
3. Define the useful outcome as a meaning brief: main meaning, 3-5 second viewer takeaway, mood, metaphor, required elements, constraints, and non-distortion rules.
4. Define structure behavior from text meaning to illustration task, viewer perception, visual image, constraints, and only then a possible illustrator assignment.
5. Add boundaries against rewriting, inventing meaning, infographic drift, banal metaphor selection, presentation/comic drift, and prompt-first behavior.
6. Add common anti-patterns tied to meaning drift and prompt-first work.

## Non-Goals

- No comics.
- No presentations.
- No artist or Artist Agent.
- No pipeline changes.
- No template changes.
- No production artifact changes.
- No review heuristics.
- No Step 2+ work.
- No design-system or prompt-generator behavior.

## Status

Completed.
