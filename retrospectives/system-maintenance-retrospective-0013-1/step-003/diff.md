# Diff

The project files are currently untracked in git, so `git diff` cannot show a
tracked baseline for this file. This file records the Step 3 semantic diff.

## `editorial_knowledge/50_editorial_failure_patterns.md`

```diff
diff --git a/editorial_knowledge/50_editorial_failure_patterns.md b/editorial_knowledge/50_editorial_failure_patterns.md
@@
+ ### Pattern: Sketchnote → Infographic Drift
+
+ #### Description
+
+ The editorial system formally creates a sketchnote, but the actual result
+ becomes an infographic, presentation slide, corporate one-pager, UI-like
+ scheme, or other designed visualization instead of a handwritten reader's note
+ sheet.
+
+ This pattern was added after the first production sketchnote run in
+ `TASK-0017`, where a visual article sketchnote request drifted into
+ infographic/SVG/HTML output.
+
+ This pattern belongs only to `visual_article_sketchnote`. It does not apply to
+ ordinary meaningful illustration tasks.
+
+ #### Symptoms
+
+ - Strict grid.
+ - Identical cards or blocks.
+ - Perfect alignment.
+ - Symmetrical structure.
+ - Presentation-slide feeling.
+ - Corporate one-pager feeling.
+ - No visible handwriting.
+ - No loose liner drawings.
+ - No sense of visual thinking in progress.
+ - Weak or absent paper-sheet feeling.
+ - SVG, HTML, web page, or interactive artifact treated as the main result.
+ - The image looks designed for a report instead of noted by a reader.
+
+ #### Causes
+
+ - Artist Agent starts thinking like a designer, analyst, or marketer instead
+   of a reader.
+ - The semantic layer is too weak or not anchored in approved
+   `visual_concept.md`.
+ - `sketchnote_brief.md` turns into an infographic brief.
+ - Sketchnote genre constraints are missing, weak, or ignored during prompt
+   execution.
+ - Visual constraints against grids, cards, corporate layout, SVG/HTML, and
+   one-pager output are not enforced.
+ - The model chooses the safest familiar visual template: clean blocks, icons,
+   hierarchy, and alignment.
+
+ #### Risks
+
+ - The result loses the feeling of a live handwritten article note.
+ - The image no longer creates the right kind of interest in the article.
+ - The reader perceives the output as an infographic or presentation asset.
+ - The visual branch stops doing the sketchnote job and becomes generic design
+   production.
+ - Article meaning may survive as content, but the genre no longer matches the
+   reader request.
+
+ #### Repair moves
+
+ - Return to the approved `visual_concept.md` and check whether the semantic
+   frame is clear enough.
+ - Check the sketchnote genre constraints in `sketchnote_brief.md` and
+   `image_prompt.md`.
+ - Remove strict grid behavior.
+ - Remove identical cards or modular blocks.
+ - Remove corporate one-pager, presentation, UI, or web-page language.
+ - Strengthen the handwritten note character: paper sheet, liner drawings,
+   uneven spacing, arrows, labels, and reader-like visual thinking.
+ - Reframe the output as "notes made by an attentive reader", not "designed
+   explanation".
+ - Treat SVG or HTML only as an internal intermediate if necessary; the final
+   sketchnote result should be image output.
+
+ #### Detection questions
+
+ - Does the result look like a personal article note?
+ - Could an attentive reader plausibly have drawn this in a notebook?
+ - Does it look like an infographic, one-pager, report page, or presentation
+   slide?
+ - Are there identical cards, perfect alignment, or a strict grid?
+ - Has the feeling of paper disappeared?
+ - Has handwriting been replaced by clean typographic labels?
+ - Are the visual relationships loose and reader-like, or designed and
+   corporate?
+ - Is SVG/HTML/web output being treated as the final result?
+
+ #### Do not over-correct
+
+ Do not apply this pattern to ordinary illustration tasks. Some visual
+ assignments may legitimately be infographics, slides, diagrams, or structured
+ visuals when the user asks for those formats. The failure appears when a
+ `visual_article_sketchnote` request loses its handwritten reader-note genre.
```

## Boundary Confirmation

```diff
+ Added one new failure pattern based on `TASK-0017`.
+ Scoped the pattern only to `visual_article_sketchnote`.
+ Added detection questions and repair moves for infographic drift.
- Changed no Artist Agent file.
- Changed no `visual_concept.md` rules.
- Changed no `sketchnote_brief.md`.
- Changed no review system.
- Created no new mode, agent, pipeline, comic, or presentation path.
```
