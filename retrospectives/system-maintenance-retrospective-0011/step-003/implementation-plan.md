# Step 3 Implementation Plan

## Scope

Step: `system-maintenance-retrospective-0011 / step-003`

Focus: create the first independent visual editorial output: `visual_concept.md`.

Goal: add a template that lets the editorial system turn a text into a meaning-only visual concept that can later inform an illustrator brief or prompt preparation without becoming either of those things.

## Discovery

Existing artifact templates live in:

- `ai-editorial-office/templates/artifacts/`

The user-facing logical path `templates/artifacts/visual_concept_template.md` maps to this canonical project folder.

The existing mode is:

- `visual_illustration_brief` in `editorial_knowledge/20_editorial_modes.md`

## Implementation Steps

1. Create `ai-editorial-office/templates/artifacts/visual_concept_template.md`.
2. Define the output artifact as `visual_concept.md`.
3. Bind the artifact to `visual_illustration_brief`.
4. Record ownership as editorial.
5. Include only meaning-layer sections:
   - main meaning;
   - viewer takeaway;
   - emotional tone;
   - visual metaphor;
   - required elements;
   - distortion risks;
   - misreading risks;
   - notes for a future illustration brief.
6. Add explicit exclusions for prompt, artist instruction, composition, color, style, technique, and design-document behavior.

## Non-Goals

- No Artist Agent.
- No Visual Editor Agent.
- No `image_prompt.md`.
- No image generation workflow.
- No review heuristics.
- No composition, color, style, or drawing technique guidance.
- No storyboard, comic artifact, or presentation artifact.
- No Step 4+ work.

## Status

Completed.
