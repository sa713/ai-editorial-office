# Diff

The project files are currently untracked in git, so `git diff` cannot show a
tracked baseline for these files. This file records the Step 1 semantic diff,
separated by requested file.

## `editorial_knowledge/20_editorial_modes.md`

```diff
@@ visual_article_sketchnote / Useful outcome
- The editorial team can read the article, identify its main meaning, extract
- 4-7 key points, determine relationships between those points, identify the
- author's conclusions, suggest a one-sheet visual structure, and prepare a
- sketchnote brief for an artist.
+ The editorial team can read the article, prepare `visual_concept.md` as the
+ semantic frame for the sketchnote, identify the article's central idea, map
+ 5-10 key meaning blocks, determine relationships between ideas, identify the
+ author's conclusions, define what the viewer should remember, capture the
+ emotional or intellectual feeling of the material, and then prepare a
+ sketchnote brief for an artist.

@@ visual_article_sketchnote / Preferred structure behavior
- Start with the article's main meaning, then select the key points,
- relationships, and author conclusions that must appear on the sheet.
+ Start by creating `visual_concept.md` from the article. For
+ `visual_article_sketchnote`, `visual_concept.md` is the semantic frame of the
+ article, not an ordinary metaphorical illustration concept.
+
+ The sketchnote `visual_concept.md` should fix:
+ - central idea;
+ - 5-10 key meaning blocks;
+ - relationships between ideas;
+ - author conclusions;
+ - what the viewer should remember;
+ - emotional or intellectual feeling of the material.
+
+ Only after this meaning layer is approved, translate it into
+ `sketchnote_brief.md`.

@@ visual_article_sketchnote / Expected outputs
- Primary artifact: `sketchnote_brief.md`.
+ Primary upstream artifact: `visual_concept.md`.
+ Execution brief artifact: `sketchnote_brief.md`.
+ `sketchnote_brief.md` must be built from approved `visual_concept.md`, not
+ directly from the article.
```

## `ai-editorial-office/templates/artifacts/sketchnote_brief_template.md`

```diff
@@ header
- Purpose: translate an article into an editorial assignment for a visual
- handwritten sketchnote that can be published next to the article.
+ Purpose: translate an approved `visual_concept.md` into an editorial
+ assignment for a visual handwritten sketchnote that can be published next to
+ the article.

- Source artifact: article or article draft supplied in the task.
+ Source artifact: `visual_concept.md`.

@@ ownership
- This brief owns the meaning layer for the sketchnote.
+ This brief translates the approved meaning layer into a handwritten
+ sketchnote format. The article remains the source of truth, but this brief
+ must not rebuild the article's meaning from scratch or bypass the approved
+ `visual_concept.md`.

@@ required upstream
+ Required upstream: approved `visual_concept.md` for
+ `visual_article_sketchnote`. In this mode, `visual_concept.md` is not an
+ ordinary metaphorical illustration concept; it is the semantic frame of the
+ article: central idea, 5-10 key meaning blocks, relationships, author
+ conclusions, viewer memory, and emotional/intellectual feeling.

@@ artifact fields
- Main thought of the article:
+ Main thought from approved `visual_concept.md`:

- 4-7 key theses that must appear on the sheet:
+ 4-7 visible key theses selected from the approved meaning blocks:

- Main conclusions the author reaches:
+ Main author conclusions from approved `visual_concept.md`:
```

## `ai-editorial-office/AGENTS.md`

```diff
@@ Artist Agent prerequisites
 For `visual_article_sketchnote` tasks, Artist Agent requires:

++ `visual_concept.md`;
 - `sketchnote_brief.md`.

@@ compact path
- article -> `sketchnote_brief.md` -> Artist Agent
+ article -> `visual_concept.md` -> `sketchnote_brief.md` -> Artist Agent
```

## Boundary Confirmation

```diff
+ Restored `visual_concept.md` as mandatory upstream semantic frame.
+ Kept the ordinary `visual_illustration_brief` branch intact.
+ Created no new pipeline.
+ Created no new agent.
+ Added no PNG rule.
+ Added no failure pattern.
+ Changed no review-system file.
+ Changed no Artist Agent file.
```
