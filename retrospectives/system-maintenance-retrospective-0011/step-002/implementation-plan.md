# Step 2 Implementation Plan

## Scope

Step: `system-maintenance-retrospective-0011 / step-002`

Focus: visual meaning extraction for the existing `visual_illustration_brief` mode.

Goal: teach the editorial system to extract the visual meaning of a text before any illustrator, image-generation workflow, or prompt appears.

## Discovery

Step 1 added `visual_illustration_brief` to:

- `editorial_knowledge/20_editorial_modes.md`

The Step 2 change belongs in the same mode because it clarifies how the mode reads the text before moving toward any future illustration brief.

## Implementation Steps

1. Add visual meaning extraction guidance inside `visual_illustration_brief`.
2. Distinguish main meaning from topic and retelling.
3. Define viewer takeaway as a 3-5 second understanding.
4. Add emotional tone extraction tied to the text.
5. Add visual metaphor selection with a check against obvious, distorting metaphors.
6. Add distortion risks.
7. Add visual anti-patterns.
8. Keep the guidance away from artist instructions, composition, color, style, and final prompt wording.

## Non-Goals

- No Artist Agent.
- No Visual Editor Agent.
- No image generation workflow.
- No `image_prompt.md`.
- No production artifacts.
- No review heuristics.
- No Step 3+ work.
- No composition, color, style, or design methodology.

## Status

Completed.
