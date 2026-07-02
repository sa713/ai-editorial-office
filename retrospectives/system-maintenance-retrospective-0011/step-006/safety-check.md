# Safety Check

## Scope Safety

- [x] Step 6 only.
- [x] No Step 7 implementation started.
- [x] Artist Agent file created.
- [x] `image_prompt_template.md` created.
- [x] No pipeline created or changed.
- [x] Review system not changed.
- [x] `visual_concept_template.md` not changed.
- [x] `illustration_brief_template.md` not changed.

## Artist Agent Safety

- [x] Artist Agent requires approved `visual_concept.md`.
- [x] Artist Agent requires approved `illustration_brief.md`.
- [x] Artist Agent works as executor, not semantic editor.
- [x] Artist Agent does not analyze source text as the primary input.
- [x] Artist Agent does not replace `visual_concept.md`.
- [x] Artist Agent does not change `illustration_brief.md`.
- [x] Artist Agent does not invent new meaning.
- [x] Artist Agent does not change tone.
- [x] Artist Agent records insufficient briefs as blockers.

## Image Prompt Safety

- [x] `image_prompt.md` is defined as an Artist Agent execution artifact.
- [x] `image_prompt.md` is built on `illustration_brief.md`.
- [x] Template includes source brief.
- [x] Template includes illustration goal.
- [x] Template includes prompt.
- [x] Template includes required elements.
- [x] Template includes forbidden distortions.
- [x] Template includes text-on-image rules.
- [x] Template includes format/aspect ratio.
- [x] Template includes style constraints only if given.
- [x] Template includes unresolved questions.

## Boundary Safety

- [x] Comics not added.
- [x] Presentations not added.
- [x] No image generation workflow added.
- [x] No new pipeline added.
- [x] No review-system update added.
- [x] No previous visual templates changed.

## Readiness Check

- [x] Artist Agent exists.
- [x] `image_prompt.md` exists as an artifact type through its template.
- [x] Artist Agent is executor, not meaning owner.
- [x] Meaning remains owned by `visual_concept.md` and `illustration_brief.md`.
- [x] Comics and presentations remain untouched.
- [x] No new pipeline exists.
