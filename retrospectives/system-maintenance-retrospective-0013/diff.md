# Diff Summary

The local repository exposes project files as untracked, so tracked `git diff`
is not a reliable baseline. This file records the semantic diff for
`system-maintenance-retrospective-0013`.

## Added

```diff
+ ai-editorial-office/templates/artifacts/sketchnote_brief_template.md
+ retrospectives/system-maintenance-retrospective-0013/implementation-plan.md
+ retrospectives/system-maintenance-retrospective-0013/changed-files.md
+ retrospectives/system-maintenance-retrospective-0013/sketchnote-mode-decisions.md
+ retrospectives/system-maintenance-retrospective-0013/sketchnote-brief-decisions.md
+ retrospectives/system-maintenance-retrospective-0013/review-decisions.md
+ retrospectives/system-maintenance-retrospective-0013/safety-check.md
+ retrospectives/system-maintenance-retrospective-0013/rollback-notes.md
+ retrospectives/system-maintenance-retrospective-0013/diff.md
```

## Updated

```diff
M editorial_knowledge/20_editorial_modes.md
M editorial_knowledge/40_editorial_review_system.md
M ai-editorial-office/AGENTS.md
M ai-editorial-office/agents/artist_agent.md
M ai-editorial-office/templates/artifacts/image_prompt_template.md
```

## Semantic Changes

```diff
+ Added editorial mode `visual_article_sketchnote`.
+ Defined sketchnote reader goal, useful outcome, reader state, output
+ character, boundaries, expected artifact, and anti-patterns.
+ Added `sketchnote_brief.md` template with article meaning, key points,
+ author conclusions, visual hierarchy, suggested layout, handwritten content,
+ drawing elements, do-not-show constraints, and style constraints.
+ Updated visual branch activation so sketchnote requests route to
+ `visual_article_sketchnote`, including Russian triggers such as
+ "визуальный конспект статьи", "рукописный конспект", and "конспект на
+ листе".
+ Allowed Artist Agent to use approved `sketchnote_brief.md` as a source for
+ `image_prompt.md`.
+ Updated `image_prompt.md` template to support either `illustration_brief.md`
+ or `sketchnote_brief.md`.
+ Added review checks for sketchnote meaning fidelity, invented theses,
+ one-sheet discipline, readability of main phrases, genre drift, and prompt
+ drift from `sketchnote_brief.md` to `image_prompt.md`.
- Added no new agent.
- Added no new pipeline.
- Added no comic, presentation, OCR, artistic scoring, or design-system layer.
- Did not rewrite the existing ordinary illustration branch beyond the minimal
- Artist Agent and image-prompt bridge needed for the new artifact.
```
