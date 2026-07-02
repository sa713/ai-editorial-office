# Diff

The project files are currently untracked in git, so `git diff` cannot show a
tracked baseline for these files. This file records the Step 2 semantic diff
by requested file.

## `ai-editorial-office/agents/artist_agent.md`

```diff
diff --git a/ai-editorial-office/agents/artist_agent.md b/ai-editorial-office/agents/artist_agent.md
@@ Outputs
+ For `visual_article_sketchnote`, the standard final image result is PNG.
+ HTML, SVG, web page, and interactive artifact are not final results for this
+ mode. SVG may be used only as an internal intermediate format if the
+ environment requires it, but the final result must be treated as PNG.

+ ## Execution Mode: visual_article_sketchnote
+ Use this execution mode only when the active visual mode is
+ `visual_article_sketchnote` and an approved `sketchnote_brief.md` exists.
+
+ The result must look as if an intelligent, attentive reader read the article
+ and summarized it for themselves in a notebook. It should feel made by a
+ reader, not by a designer, analyst, marketer, product team, or presentation
+ author.
+
+ Required sketchnote signals:
+ - one sheet of paper;
+ - one coherent spread, not separate slides or screens;
+ - handwritten notes;
+ - liner drawings;
+ - arrows;
+ - labels;
+ - visible relationships between ideas;
+ - small visual metaphors;
+ - a live thinking-process feeling.
+
+ Genre prohibitions:
+ - infographic;
+ - presentation slide;
+ - poster;
+ - advertising image;
+ - corporate one-pager;
+ - UI mockup;
+ - set of cards;
+ - digital scheme;
+ - web page;
+ - interactive artifact.
+
+ Visual prohibitions:
+ - strict grid;
+ - perfect alignment;
+ - symmetrical structure;
+ - identical repeated blocks;
+ - presentation feeling;
+ - corporate design feeling;
+ - AI-collage feeling.
+
+ For `visual_article_sketchnote`, the default final result is PNG. Do not
+ deliver HTML, SVG, web page, or interactive artifact as the final result.

@@ Forbidden Actions
+ - turn a sketchnote into a presentation slide, advertising image, corporate
+   one-pager, UI mockup, set of cards, digital scheme, web page, or interactive
+   artifact;
+ - deliver HTML or SVG as the final result for `visual_article_sketchnote`;

@@ Stop Conditions
+ - `visual_article_sketchnote` execution would require delivering a final HTML,
+   SVG, web page, interactive artifact, infographic, presentation slide, poster,
+   corporate one-pager, UI mockup, set of cards, or digital scheme;

@@ Role-Specific Quality Checks
+ - `visual_article_sketchnote` output reads as one handwritten note sheet made
+   by an attentive reader, not as an infographic, slide, poster, one-pager, UI
+   mockup, card set, digital scheme, web page, or interactive artifact;
+ - `visual_article_sketchnote` final image target is PNG, with SVG allowed only
+   as an internal intermediate when required by the environment;
```

## `ai-editorial-office/templates/artifacts/image_prompt_template.md`

```diff
diff --git a/ai-editorial-office/templates/artifacts/image_prompt_template.md b/ai-editorial-office/templates/artifacts/image_prompt_template.md
@@ format/aspect ratio
+ - For `visual_article_sketchnote`, standard final result: PNG.
+ - For `visual_article_sketchnote`, not final output: HTML, SVG, web page,
+   interactive artifact.
+ - SVG intermediate allowed only if the environment requires it: yes / no / not
+   applicable.

+ ## sketchnote genre constraints
+ Fill when active visual mode is `visual_article_sketchnote`.
+ - Must look like one handwritten article sketchnote:
+ - Must feel like notes made by an attentive reader:
+ - Must not feel like work by a designer, analyst, marketer, product team, or
+   presentation author:

+ ## handwritten note constraints
+ Fill when active visual mode is `visual_article_sketchnote`.
+ - Handwritten note qualities to preserve:
+ - Liner drawing qualities to preserve:
+ - Required controlled handwritten phrases:
+ - Fake handwriting or filler text to avoid:

+ ## one-sheet constraints
+ Fill when active visual mode is `visual_article_sketchnote`.
+ - One sheet of paper:
+ - One coherent spread:
+ - Arrows, labels, and relationships between ideas:
+ - Small visual metaphors:
+ - Live thinking-process feeling:

+ ## anti-infographic constraints
+ Fill when active visual mode is `visual_article_sketchnote`.
+ - Do not make an infographic:
+ - Do not make a presentation slide:
+ - Do not make a poster, ad, or corporate one-pager:
+ - Do not make a UI mockup, card set, digital scheme, web page, or interactive
+   artifact:
+ - Avoid strict grid, perfect alignment, symmetry, identical blocks, corporate
+   design feeling, and AI-collage feeling:
```

## Boundary Confirmation

```diff
+ Added sketchnote execution discipline.
+ Set PNG as standard final result for `visual_article_sketchnote`.
+ Prohibited infographic, SVG/HTML final output, web page, interactive artifact,
+ corporate one-pager, UI mockup, card set, and digital scheme drift.
- Changed no `visual_concept.md` rules.
- Changed no `sketchnote_brief.md`.
- Changed no ordinary illustration branch.
- Created no new agent.
- Created no new pipeline.
- Changed no review system.
- Added no comic or presentation mode.
```
