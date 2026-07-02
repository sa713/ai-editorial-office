# Step 7 Implementation Plan

## Scope

Step: `system-maintenance-retrospective-0011 / step-007`

Focus: bounded meaning-preservation review across the visual artifact chain.

Goal: let editorial review verify that meaning survives the transition from `visual_concept.md` to `illustration_brief.md` to `image_prompt.md` without reviewing image quality or becoming art direction.

## Context

Existing visual branch layers:

- `visual_concept.md`;
- `illustration_brief.md`;
- `image_prompt.md`.

Step 7 adds review guidance for the transition chain:

`visual_concept.md` -> `illustration_brief.md` -> `image_prompt.md`

## Implementation Steps

1. Add bounded meaning-preservation chain guidance to `editorial_knowledge/40_editorial_review_system.md`.
2. Check main meaning continuity.
3. Check viewer takeaway continuity.
4. Check visual metaphor continuity.
5. Check whether new meanings were introduced downstream.
6. Check preservation of required elements, forbidden distortions, and misreading protections.
7. Check prompt drift.
8. Add boundary protection against image quality review, art direction, Artist QA, composition review, color review, style review, drawing review, comics, and presentations.
9. State that downstream drift is fixed in `illustration_brief.md` or `image_prompt.md`, not by changing `visual_concept.md`.

## Non-Goals

- No image review.
- No image quality review.
- No artistic expertise or art direction.
- No composition, color, style, or drawing-quality review.
- No Artist QA pipeline.
- No comics.
- No presentations.

## Status

Completed.
