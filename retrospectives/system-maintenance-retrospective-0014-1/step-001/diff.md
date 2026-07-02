# Diff

The project files are currently untracked in git, so `git diff` cannot show a
tracked baseline for these files. This file records the Step 1 semantic diff.

## `ai-editorial-office/kb/canonical_sketchnote_prompt.md`

```diff
diff --git a/ai-editorial-office/kb/canonical_sketchnote_prompt.md b/ai-editorial-office/kb/canonical_sketchnote_prompt.md
new file mode 100644
--- /dev/null
+++ b/ai-editorial-office/kb/canonical_sketchnote_prompt.md
@@
+ # CANONICAL SKETCHNOTE PROMPT
+
+ This file is intentionally left blank.
+
+ The prompt will be supplied and maintained manually.
+
+ Do not replace, summarize, optimize, rewrite, or reinterpret its contents.
```

## `ai-editorial-office/agents/artist_agent.md`

```diff
diff --git a/ai-editorial-office/agents/artist_agent.md b/ai-editorial-office/agents/artist_agent.md
@@ Primary Responsibilities
-   - for `visual_article_sketchnote`: `sketchnote_brief.md`;
+   - for `visual_article_sketchnote`: approved `visual_concept.md`, approved
+     `sketchnote_brief.md`, and `kb/canonical_sketchnote_prompt.md`;

@@ Inputs
-   - `sketchnote_brief.md` for `visual_article_sketchnote`;
+   - `visual_concept.md`, `sketchnote_brief.md`, and
+     `kb/canonical_sketchnote_prompt.md` for `visual_article_sketchnote`;

@@ Execution Mode: visual_article_sketchnote
- Use this execution mode only when the active visual mode is
- `visual_article_sketchnote` and an approved `sketchnote_brief.md` exists.
+ Use this execution mode only when the active visual mode is
+ `visual_article_sketchnote`, an approved `visual_concept.md`, an approved
+ `sketchnote_brief.md`, and `kb/canonical_sketchnote_prompt.md` exist.

+ For this mode, `kb/canonical_sketchnote_prompt.md` is the canonical source for
+ genre and visual execution. If the canonical prompt exists and is not empty
+ with manually supplied prompt content beyond the placeholder, it has priority
+ over generic sketchnote generation logic. Artist Agent must not replace,
+ summarize, optimize, rewrite, reinterpret, or reinvent the canonical prompt's
+ execution style.

@@ Forbidden Actions
+ - replace, summarize, optimize, rewrite, reinterpret, or reinvent
+   `kb/canonical_sketchnote_prompt.md`;

@@ Stop Conditions
+ - approved `visual_concept.md` is missing for `visual_article_sketchnote`;
+ - `kb/canonical_sketchnote_prompt.md` is missing for
+   `visual_article_sketchnote`;

@@ Role-Specific Quality Checks
+ - meaning remains owned by `visual_concept.md` and `illustration_brief.md`, or
+   by `visual_concept.md` and `sketchnote_brief.md` for
+   `visual_article_sketchnote`;
+ - `visual_article_sketchnote` prompt uses
+   `kb/canonical_sketchnote_prompt.md` as the source of genre and visual
+   execution when the canonical prompt exists and is not empty with manually
+   supplied prompt content beyond the placeholder;
```

## `ai-editorial-office/templates/artifacts/image_prompt_template.md`

```diff
diff --git a/ai-editorial-office/templates/artifacts/image_prompt_template.md b/ai-editorial-office/templates/artifacts/image_prompt_template.md
@@ source brief
+ - Source `visual_concept.md`, if applicable; required for
+   `visual_article_sketchnote`:
+ - Source `kb/canonical_sketchnote_prompt.md`, required for
+   `visual_article_sketchnote`:
+ - Canonical sketchnote prompt status: missing / placeholder only / manually
+   supplied:

@@ sketchnote genre constraints
+ - Canonical source:
+   `ai-editorial-office/kb/canonical_sketchnote_prompt.md`.
+ - If canonical prompt exists and is not empty with manually supplied prompt
+   content beyond the placeholder, it has priority over generic sketchnote
+   generation logic.
+ - Do not replace, summarize, optimize, rewrite, or reinterpret the canonical
+   prompt contents.
```

## Boundary Confirmation

```diff
+ Added canonical sketchnote prompt placeholder.
+ Integrated canonical prompt as a required source for `visual_article_sketchnote`.
+ Added priority rule over generic sketchnote generation logic when manually
+ supplied prompt content exists.
+ Protected canonical prompt from replacement, summary, optimization, rewrite,
+ or reinterpretation.
- Did not fill the canonical prompt.
- Did not change `visual_concept`.
- Did not change `sketchnote_brief`.
- Did not change review system, pipelines, visual modes, or ordinary
- illustration branch.
```
