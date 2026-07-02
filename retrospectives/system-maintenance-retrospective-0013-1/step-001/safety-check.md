# Safety Check

## Scope Safety

- [x] Step 1 only.
- [x] `visual_article_sketchnote` now requires upstream `visual_concept.md`.
- [x] `sketchnote_brief.md` is built from approved `visual_concept.md`.
- [x] `AGENTS.md` compact path was updated.
- [x] Artist Agent file was not changed.
- [x] Review system was not changed.
- [x] Failure patterns were not changed.
- [x] PNG rule was not added.
- [x] No new pipeline added.
- [x] No new agent added.
- [x] No comic or presentation mode added.

## Semantic Safety

- [x] The article remains the source of truth.
- [x] `visual_concept.md` is the required semantic frame.
- [x] `sketchnote_brief.md` does not rebuild article meaning from scratch.
- [x] The sketchnote visual concept is distinguished from a normal
  metaphorical illustration concept.
- [x] Required sketchnote concept contents are explicit: central idea, 5-10
  meaning blocks, relationships, author conclusions, viewer memory, and
  emotional or intellectual feeling.

## Ordinary Illustration Safety

- [x] The existing `visual_illustration_brief` mode was not edited.
- [x] The ordinary path still remains:
  `text -> visual_concept.md -> illustration_brief.md -> Artist Agent`.
- [x] No ordinary illustration artifact was renamed or removed.

## Readiness Check

- [x] `visual_article_sketchnote` no longer jumps directly from article to
  `sketchnote_brief.md`.
- [x] `visual_concept.md` is mandatory as the meaning layer.
- [x] `sketchnote_brief_template.md` names `visual_concept.md` as source.
- [x] Compact path in `AGENTS.md` includes `visual_concept.md`.
