# Step 1 Diff Summary

The local repository state exposes these project files as untracked, so `git diff` does not provide a reliable tracked baseline. This file records the semantic diff applied in Step 1.

## AGENTS.md Diff

`ai-editorial-office/AGENTS.md`

```diff
diff --git a/ai-editorial-office/AGENTS.md b/ai-editorial-office/AGENTS.md
--- a/ai-editorial-office/AGENTS.md
+++ b/ai-editorial-office/AGENTS.md
@@
-В MVP активными production roles являются только эти канонические роли и файлы:
+В MVP активными production roles для обычных текстовых задач являются эти канонические роли и файлы:
@@
-Только канонические agent files из `/agents/*.md` должны использоваться как активные спецификации. Дубликаты и экспортированные копии, например `chief_editor(1).md`, не считаются активными agent specs.
+Только канонические agent files из `/agents/*.md` должны использоваться как активные спецификации для MVP-ролей и явно легализованных extension-ролей. Дубликаты и экспортированные копии, например `chief_editor(1).md`, не считаются активными agent specs.
+
+Non-MVP extension roles are forbidden by default unless this charter explicitly legalizes them.
+
+Currently legalized extension:
+
+- Artist Agent — `artist_agent` — `/agents/artist_agent.md`.
+
+Artist Agent is allowed only for illustration-to-text tasks when the task explicitly requires an illustration and the task already has approved:
+
+- `visual_concept.md`;
+- `illustration_brief.md`.
+
+Artist Agent may prepare `image_prompt.md` or an image when the environment allows, but it is not a semantic editor, reviewer, writer, designer, comic artist, or presentation designer. It must not reinterpret the source text, replace `visual_concept.md`, change `illustration_brief.md`, invent new meaning, create comics, create presentations, or become part of ordinary text tasks.
+
+The MVP agent set remains unchanged for ordinary text tasks. Artist Agent is a bounded visual-branch extension, not a universal production role.
@@
-   `chief_editor` выбирает pipeline, назначает MVP-роли, фиксирует план в `orchestration_plan.md` и поддерживает `task-manifest.md` и `status.md`.
+   `chief_editor` выбирает pipeline, назначает MVP-роли или явно легализованные extension-роли только когда их условия выполнены, фиксирует план в `orchestration_plan.md` и поддерживает `task-manifest.md` и `status.md`.
```

## Pipeline Guardrail Diff Summary

Affected files:

- `ai-editorial-office/pipelines/article_pipeline.md`
- `ai-editorial-office/pipelines/social_pipeline.md`
- `ai-editorial-office/pipelines/ux_writing_pipeline.md`
- `ai-editorial-office/pipelines/research_pipeline.md`
- `ai-editorial-office/pipelines/review_pipeline.md`

Pattern changed:

```diff
- Only MVP agents may be used...
+ By default, only MVP agents may be used...
+ Explicitly legalized non-MVP extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.

- This pipeline must not assign work to any non-MVP role.
+ This pipeline must not assign work to non-MVP extension roles by default.
+ Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions.

- task requires a non-MVP production role;
+ task requires a non-MVP production role that is not explicitly legalized in `AGENTS.md`,
+ or uses a legalized extension role outside its allowed scope;

- request to use a non-MVP role;
+ request to use a non-MVP role that is not explicitly legalized in `AGENTS.md`,
+ or to use a legalized extension role outside its allowed scope;

- confirm current owner role and next role are valid MVP roles;
+ confirm current owner role and next role are valid MVP roles or explicitly legalized
+ extension roles whose `AGENTS.md` conditions apply;
```

## Boundary Confirmation

```diff
+ Legalized Artist Agent only as bounded non-MVP visual extension.
+ Kept MVP agent set unchanged for ordinary text tasks.
+ Kept Artist Agent out of semantic editing, review, writing, design, comics, and presentations.
- Created no new agents.
- Changed no Artist Agent file.
- Created no new pipeline.
- Changed no review system.
- Added no comics.
- Added no presentations.
```
