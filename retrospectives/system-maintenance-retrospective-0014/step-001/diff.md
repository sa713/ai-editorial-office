# Diff

The project files are currently untracked in git, so `git diff` cannot show a
tracked baseline for this file. This file records the Step 1 semantic diff.

## `ai-editorial-office/AGENTS.md`

```diff
diff --git a/ai-editorial-office/AGENTS.md b/ai-editorial-office/AGENTS.md
@@ Главные инварианты
+ 9. Если задача поставлена как редакционная задача, редакция должна быть
+    активирована до производства результата.

@@
+ ## Editorial entry discipline
+
+ This charter is the canonical owner for editorial entry discipline because it
+ governs system invariants, role assignment, orchestration, and governance
+ boundaries.
+
+ When the user works through a `TASK-ID` folder, the editorial project, or an
+ existing editorial workflow, direct-production execution is forbidden unless
+ the user explicitly asks to bypass the editorial process.
+
+ Before production starts, Chief Editor must route the task editorially:
+
+ - determine the task type;
+ - choose the relevant pipeline or editorial mode;
+ - activate the visual branch when the selected task requires it;
+ - determine the required roles and bounded extension roles;
+ - record the routing decision in `orchestration_plan.md`,
+   `task-manifest.md`, or `status.md`.
+
+ Technical actions are not substitutes for editorial routing. SVG, PNG, HTML,
+ image generation, PDF extraction, OCR, parsing, conversion, scraping,
+ rendering, or other tool work may support a task only after the editorial
+ route is known. They must not become a silent replacement for the editorial
+ process.
+
+ Exception: direct-production execution is allowed when the user explicitly
+ asks to do the work directly, skip the editorial process, bypass the process,
+ not use the editorial system, or handle the request as an ordinary
+ non-editorial task.
+
+ After routing, the result must stay within the selected pipeline or mode. For
+ example, when `visual_article_sketchnote` is selected, execution must not
+ silently drift into an infographic, web page, SVG summary, corporate
+ one-pager, or other output genre that contradicts the selected mode.
```

## Boundary Confirmation

```diff
+ Added editorial entry discipline to the canonical charter.
+ Required Chief Editor routing before production for editorial tasks.
+ Stated that technical actions are not substitutes for editorial process.
+ Added explicit direct-production exception.
+ Required selected-mode fidelity.
- Changed no pipelines.
- Changed no Artist Agent.
- Changed no visual modes.
- Changed no review system.
- Added no new architecture.
```
