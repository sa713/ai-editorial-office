# Safety Check

## Scope Safety

- [x] Step 1 only.
- [x] Created `canonical_sketchnote_prompt.md`.
- [x] Left the canonical prompt as a placeholder.
- [x] Updated Artist Agent only to recognize and prioritize the canonical
  prompt source.
- [x] Updated `image_prompt_template.md` only to reference the canonical prompt.
- [x] Did not change `visual_concept`.
- [x] Did not change `sketchnote_brief`.
- [x] Did not change review system.
- [x] Did not change pipelines.
- [x] Did not change visual modes.
- [x] Did not change ordinary illustration branch.

## Integration Safety

- [x] Artist Agent knows the canonical prompt exists.
- [x] `image_prompt_template.md` knows the canonical prompt exists.
- [x] The canonical prompt is named as the source of sketchnote genre and visual
  execution.
- [x] Priority over generic sketchnote generation logic is conditional on a
  manually supplied prompt beyond the placeholder.
- [x] Artist Agent is forbidden from replacing, summarizing, optimizing,
  rewriting, reinterpreting, or reinventing the canonical prompt.

## Readiness Check

- [x] User can manually paste the working prompt later.
- [x] The placeholder does not contain executable prompt content.
- [x] Future `visual_article_sketchnote` prompt work can cite the canonical
  prompt source.
