# Safety Check

## Scope Safety

- [x] Step 3 only.
- [x] Added one failure pattern.
- [x] Changed only `editorial_knowledge/50_editorial_failure_patterns.md`.
- [x] Did not change Artist Agent.
- [x] Did not change `visual_concept.md` rules.
- [x] Did not change `sketchnote_brief.md`.
- [x] Did not change review system.
- [x] Did not create a new mode.
- [x] Did not create a new agent.
- [x] Did not create a new pipeline.
- [x] Did not add comic or presentation mode.

## Pattern Safety

- [x] Pattern is based on the real `TASK-0017` failure.
- [x] Pattern names infographic drift directly.
- [x] Symptoms include grid, cards, alignment, missing handwriting, SVG/HTML,
  and corporate design feeling.
- [x] Causes include designer/marketer thinking, weak semantic layer,
  infographic brief drift, missing constraints, and safe visual-template bias.
- [x] Repair moves restore `visual_concept.md`, sketchnote constraints,
  handwritten note character, and reader-note feeling.
- [x] Detection questions distinguish personal note from infographic,
  one-pager, presentation, report page, and web artifact.

## Ordinary Illustration Safety

- [x] Pattern explicitly applies only to `visual_article_sketchnote`.
- [x] Pattern explicitly does not apply to ordinary meaningful illustration
  tasks.
- [x] No ordinary illustration behavior was changed.

## Readiness Check

- [x] New failure pattern appeared.
- [x] It helps detect sketchnote-to-infographic drift.
- [x] It does not create a new architecture.
