# Diff

The project files are currently untracked in git, so `git diff` cannot show a
tracked baseline for these files. This file records the Step 1 semantic diff.

## `ai-editorial-office/AGENTS.md`

```diff
diff --git a/ai-editorial-office/AGENTS.md b/ai-editorial-office/AGENTS.md
@@ Core roles and extension roles
+ Visual subsystem status: frozen / experimental.
+
+ The visual subsystem is preserved in the repository as accumulated knowledge,
+ but it is inactive by default. Visual modes, visual branch routing, Artist
+ Agent, visual artifacts, canonical visual prompts, and visual failure patterns
+ must not participate in ordinary editorial work unless the user explicitly
+ asks to activate the visual subsystem.
+
+ Artist Agent is preserved as a legalized extension role, but it is frozen and
+ must not be assigned by default.

- Artist Agent is allowed only for visual-branch tasks when the task explicitly
- requires a visual output for a text and the task already has the approved
- source artifacts required by the active visual mode.
+ Artist Agent is allowed only for explicitly activated visual-branch tasks when
+ the task explicitly requires use of the visual subsystem and the task already
+ has the approved source artifacts required by the active visual mode.

@@ Visual branch activation
- Activate the visual branch in mode `visual_illustration_brief` when the task
- requires a meaningful illustration for a text.
+ While the visual subsystem is frozen, do not activate the visual branch merely
+ because the user asks for an illustration, visual article sketchnote, visual
+ summary, image, handwritten note, or similar visual output.
+
+ The visual branch may be activated only when the user explicitly asks to use
+ the visual subsystem, use Artist Agent, launch the visual branch, activate a
+ visual mode, or otherwise clearly asks to run the frozen visual subsystem
+ despite its inactive default status.

- Activate the visual branch in mode `visual_article_sketchnote` when the user
- asks for a visual article sketchnote, sketchnote, handwritten article notes,
- handwritten summary, one-sheet notes, a note sheet, or an image as if an
- attentive reader had summarized the article on one sheet.
+ If the user explicitly activates the frozen visual subsystem, use mode
+ `visual_article_sketchnote` when the user asks for a visual article
+ sketchnote, sketchnote, handwritten article notes, handwritten summary,
+ one-sheet notes, a note sheet, or an image as if an attentive reader had
+ summarized the article on one sheet.

@@ Do not activate
+ Do not activate the visual branch for ordinary editorial work where the user
+ did not explicitly ask to use the frozen visual subsystem.

@@ Compact path
- For low-risk or simple visual tasks, `chief_editor` may choose a compact
- visual path without creating a new pipeline.
+ After explicit frozen-subsystem activation, `chief_editor` may choose a
+ compact visual path without creating a new pipeline for low-risk or simple
+ visual tasks.

@@ Artist Agent assignment
- If the visual branch is not activated, Artist Agent must not be assigned.
+ If the visual branch is not explicitly activated under the frozen-subsystem
+ rule, Artist Agent must not be assigned.
```

## `ai-editorial-office/agents/artist_agent.md`

```diff
diff --git a/ai-editorial-office/agents/artist_agent.md b/ai-editorial-office/agents/artist_agent.md
@@
+ Status: frozen / experimental. This role is preserved for possible future
+ visual-subsystem reactivation, but it is inactive by default. Assign it only
+ when `AGENTS.md` explicitly allows visual subsystem activation for the task.
```

## `editorial_knowledge/20_editorial_modes.md`

```diff
diff --git a/editorial_knowledge/20_editorial_modes.md b/editorial_knowledge/20_editorial_modes.md
@@ visual_illustration_brief
+ Status: inactive by default while the visual subsystem is frozen. Preserve this
+ mode as visual knowledge; use it only when `AGENTS.md` explicitly allows
+ visual subsystem activation for the task.

@@ visual_article_sketchnote
+ Status: inactive by default while the visual subsystem is frozen. Preserve this
+ mode as visual knowledge; use it only when `AGENTS.md` explicitly allows
+ visual subsystem activation for the task.
```

## Boundary Confirmation

```diff
+ Marked visual subsystem frozen / experimental.
+ Disabled automatic visual branch activation.
+ Required explicit user activation for visual subsystem use.
+ Preserved Artist Agent and visual modes.
+ Preserved visual failure patterns.
- Deleted no visual knowledge.
- Changed no review system.
- Changed no pipelines.
- Changed no text modes or text roles.
```
