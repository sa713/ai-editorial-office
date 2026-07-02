# Safety Check

## Scope Safety

- [x] Added `visual_article_sketchnote`.
- [x] Added `sketchnote_brief.md` artifact template.
- [x] Updated visual activation rules in `AGENTS.md`.
- [x] Updated Artist Agent only enough to accept `sketchnote_brief.md`.
- [x] Updated `image_prompt.md` template only enough to support the new source
  brief.
- [x] Added compact review checks.
- [x] No new pipeline added.
- [x] No new agent added.
- [x] No ordinary text pipeline changed.

## Meaning Safety

- [x] The mode distinguishes sketchnote from ordinary illustration.
- [x] The brief requires article meaning.
- [x] The brief requires 4-7 key points.
- [x] The brief requires author conclusions.
- [x] The brief requires controlled handwritten phrases.
- [x] Artist Agent must not change key points or author conclusions.
- [x] Review checks for invented theses and prompt drift.

## Genre Safety

- [x] The mode rejects corporate infographic drift.
- [x] The mode rejects poster and ad drift.
- [x] The mode rejects comic and presentation drift.
- [x] The mode rejects photorealistic scene drift.
- [x] The mode rejects AI-collage feeling.
- [x] The mode rejects unreadable "map of everything" behavior.

## Constraint Safety

- [x] No comic system added.
- [x] No presentation system added.
- [x] No OCR requirement added.
- [x] No artistic quality scoring added.
- [x] No complex sketchnote methodology added.
- [x] No separate design system added.

## Readiness Check

- [x] Future user can ask: "Prepare a visual sketchnote of the article from
  TASK-0017."
- [x] Future user can ask: "Подготовь визуальный конспект статьи из TASK-0017."
- [x] The system can route the request to `visual_article_sketchnote`.
- [x] The system can create `sketchnote_brief.md`.
- [x] Artist Agent can prepare `image_prompt.md` from `sketchnote_brief.md`.
- [x] Review can check semantic fidelity and prompt drift.
