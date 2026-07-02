# Step 5 Implementation Plan

## Scope

Step: `system-maintenance-retrospective-0011 / step-005`

Focus: create the `illustration_brief.md` artifact template.

Goal: add a document that translates `visual_concept.md` into a clear editorial assignment for an illustrator without becoming a prompt, image-generation workflow, design document, or drawing methodology.

## Context

Existing layers:

- `visual_illustration_brief` mode;
- visual meaning extraction;
- `visual_concept.md`;
- visual concept review.

Step 5 adds the next layer:

`visual_concept.md` -> `illustration_brief.md` -> illustrator

## Implementation Steps

1. Create `ai-editorial-office/templates/artifacts/illustration_brief_template.md`.
2. Define the output artifact as `illustration_brief.md`.
3. Link the brief to `visual_illustration_brief`.
4. Set `visual_concept.md` as the source artifact.
5. Define ownership: created by editorial work, used by an illustrator, not replacing `visual_concept.md`.
6. Add the requested structure:
   - illustration goal;
   - main meaning;
   - viewer takeaway;
   - emotional tone;
   - visual metaphor;
   - required elements;
   - forbidden distortions;
   - misreading risks;
   - notes for illustrator.
7. Add explicit exclusions for prompt, model instruction, design document, composition, colors, technique, style, generation settings, and prompt wording.

## Non-Goals

- No Artist Agent.
- No `image_prompt.md`.
- No image generation workflow.
- No composition methodology.
- No drawing rules.
- No storyboard, comic artifact, or presentation artifact.
- No Step 6+ work.

## Status

Completed.
