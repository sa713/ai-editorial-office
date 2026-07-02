# Step 2 diff

Requested diff scope:

- `AGENTS.md`
- `project-state.md`
- all changed `pipelines/*.md`

## AGENTS.md

```diff
--- /private/tmp/system-maintenance-retrospective-0012-step-002-before/ai-editorial-office/AGENTS.md	2026-05-30 19:47:04
+++ ai-editorial-office/AGENTS.md	2026-05-30 19:48:03
@@ -70,9 +70,10 @@
 7. Агент не должен скрывать неопределённость, пробелы в источниках или спорные допущения.
 8. Если данных недостаточно для уверенного вывода, это должно быть явно указано.
 
-## MVP agent set
+## Core roles and extension roles
 
-В MVP активными production roles для обычных текстовых задач являются эти канонические роли и файлы:
+Core roles are the primary production roles for ordinary text tasks in the
+current operating model:
 
 - Chief Editor / Orchestrator — `chief_editor` — `/agents/chief_editor.md`;
 - Intake Agent — `intake_agent` — `/agents/intake_agent.md`;
@@ -82,12 +83,22 @@
 - Review Agent — `review_agent` — `/agents/review_agent.md`;
 - Final Editor — `final_editor` — `/agents/final_editor.md`.
 
-Только канонические agent files из `/agents/*.md` должны использоваться как активные спецификации для MVP-ролей и явно легализованных extension-ролей. Дубликаты и экспортированные копии, например `chief_editor(1).md`, не считаются активными agent specs.
+Current operating model means the active lifecycle, status, handoff, artifact,
+review-gate, governance, and role-assignment rules in this charter and the
+selected pipeline.
 
-Non-MVP extension roles are forbidden by default unless this charter explicitly legalizes them.
+Extension roles are additional roles outside the core role set. They may be
+assigned only when this charter explicitly legalizes them and their bounded
+scope conditions are met.
 
-Currently legalized extension:
+Unauthorized extension roles are forbidden by default. An extension role is
+unauthorized when this charter has not explicitly legalized it, or when a
+legalized extension role is used outside its bounded scope.
 
+Только канонические agent files из `/agents/*.md` должны использоваться как активные спецификации для core roles и явно легализованных extension roles. Дубликаты и экспортированные копии, например `chief_editor(1).md`, не считаются активными agent specs.
+
+Currently legalized extension role:
+
 - Artist Agent — `artist_agent` — `/agents/artist_agent.md`.
 
 Artist Agent is allowed only for illustration-to-text tasks when the task explicitly requires an illustration and the task already has approved:
@@ -107,16 +118,16 @@
 
 If the visual branch is not activated, Artist Agent must not be assigned.
 
-The MVP agent set remains unchanged for ordinary text tasks. Artist Agent is a bounded visual-branch extension, not a universal production role.
+The core role set remains unchanged for ordinary text tasks. Artist Agent is a bounded visual-branch extension, not a universal production role.
 
-В MVP нет обязательной роли `Editor`. Если нужна редакторская доработка, она выполняется через:
+В текущей рабочей модели нет обязательной роли `Editor`. Если нужна редакторская доработка, она выполняется через:
 
 - `writer_agent` — для доработки `draft.md`;
 - `ux_writer` — для доработки `ux-copy.md`;
 - `review_agent` — для независимой проверки;
 - `final_editor` — только для controlled finalization после review-gate.
 
-Отдельные роли `future_style_editor`, `future_structural_editor`, `future_terminology_reviewer` и `future_fact_checker` могут быть добавлены только как future extensions после явного обновления этого устава, agent specs и pipeline contracts. Они не являются текущими MVP-ролями и не могут быть обязательными участниками task flow.
+Отдельные роли `future_style_editor`, `future_structural_editor`, `future_terminology_reviewer` и `future_fact_checker` могут быть добавлены только как future extensions после явного обновления этого устава, agent specs и pipeline contracts. Они не являются текущими core roles и не могут быть обязательными участниками task flow.
 
 ## Authority hierarchy
 
@@ -300,7 +311,7 @@
 
 ## Стандартный жизненный цикл задачи
 
-MVP default workflow:
+Default operating workflow:
 
 ```text
 intake -> orchestration -> research if needed -> writing or ux-writing -> review -> finalization -> chief_editor final governance decision
@@ -441,7 +452,7 @@
 
 2. Orchestration
 
-   `chief_editor` выбирает pipeline, назначает MVP-роли или явно легализованные extension-роли только когда их условия выполнены, фиксирует план в `orchestration_plan.md` и поддерживает `task-manifest.md` и `status.md`.
+   `chief_editor` выбирает pipeline, назначает core roles или явно легализованные extension roles только когда их условия выполнены, фиксирует план в `orchestration_plan.md` и поддерживает `task-manifest.md` и `status.md`.
 
 3. Research if needed
 
@@ -463,7 +474,7 @@
 
    `chief_editor` валидирует finalization, создаёт `final_decision.md` и обновляет или рекомендует статус `finalized`. Publication или delivery всё равно требуют human approval, если оно нужно по задаче.
 
-В MVP прямой переход `writing` -> `review` валиден после создания обязательных writing artifacts и handoff от `writer_agent` или `ux_writer` к `review_agent`. Если локальный UX pipeline или handoff использует метку `ux-writing`, переход `ux-writing` -> `review` валиден на тех же условиях. `editing` может использоваться только как optional status-model bridge или revision checkpoint. В MVP `editing` не является обязательным этапом и не означает наличие отдельного Editor Agent: доработка текста выполняется `writer_agent`, доработка UX copy выполняется `ux_writer`, evidence gaps возвращаются к `research_agent`.
+В текущей рабочей модели прямой переход `writing` -> `review` валиден после создания обязательных writing artifacts и handoff от `writer_agent` или `ux_writer` к `review_agent`. Если локальный UX pipeline или handoff использует метку `ux-writing`, переход `ux-writing` -> `review` валиден на тех же условиях. `editing` может использоваться только как optional status-model bridge или revision checkpoint. В текущей рабочей модели `editing` не является обязательным этапом и не означает наличие отдельного Editor Agent: доработка текста выполняется `writer_agent`, доработка UX copy выполняется `ux_writer`, evidence gaps возвращаются к `research_agent`.
 
 ## Handoff protocol
 
@@ -573,7 +584,7 @@
 - `planning` — формируется структура и редакционный план;
 - `writing` — создаётся черновик;
 - `ux-writing` — optional explicit UX writing status для product-facing copy, если выбранный pipeline использует отдельную метку;
-- `editing` — optional revision checkpoint/status bridge; в MVP доработка возвращается к `writer_agent` или `ux_writer` и не означает отдельный Editor Agent;
+- `editing` — optional revision checkpoint/status bridge; в текущей рабочей модели доработка возвращается к `writer_agent` или `ux_writer` и не означает отдельный Editor Agent;
 - `review` — идёт независимая проверка;
 - `changes_requested` — review потребовал доработки;
 - `approved` — review пройден, материал можно финализировать;
@@ -627,7 +638,7 @@
 
 Legacy task folders are history, not templates. Do not copy the heavier artifact structure from earlier folders such as `TASK-0009` or `TASK-0010` only because it exists there. Use the current risk mode, selected pipeline, and artifact minimalism rules instead.
 
-`edited.md`, `editor-notes.md` и `revision-requests.md` не являются обязательными MVP-артефактами. Они допустимы только как future optional artifacts, если позже будут введены `future_style_editor`, `future_structural_editor`, `future_terminology_reviewer` или `future_fact_checker`.
+`edited.md`, `editor-notes.md` и `revision-requests.md` не являются обязательными production artifacts. Они допустимы только как future optional artifacts, если позже будут введены `future_style_editor`, `future_structural_editor`, `future_terminology_reviewer` или `future_fact_checker`.
 
 Файл `final.md` разрешён только после review со статусом `approved`.
```

## project-state.md

```diff
--- /private/tmp/system-maintenance-retrospective-0012-step-002-before/ai-editorial-office/project-state.md	2026-05-30 19:47:04
+++ ai-editorial-office/project-state.md	2026-05-30 19:48:10
@@ -6,7 +6,7 @@
 ## Completed
 - governance layer;
 - AGENTS.md;
-- MVP agent set;
+- core role set;
 - artifact templates;
 - task-manifest model;
 - orchestration model;
@@ -15,7 +15,7 @@
 - canonical ownership map;
 - repository-first memory approach.
 
-## Current MVP agents
+## Current core roles
 - chief_editor
 - intake_agent
 - research_agent
@@ -46,7 +46,7 @@
 ## Architecture principles
 Current architecture principles are owned by `AGENTS.md`. Project state may record active constraints, but permanent invariants should be changed in `AGENTS.md` first.
 
-## MVP workflow default
+## Default operating workflow
 Owned by `AGENTS.md`. Current default remains intake -> chief_editor orchestration -> research if needed -> writing or ux-writing -> review -> finalization -> chief_editor final governance decision.
 
 ## Risk modes
@@ -62,8 +62,8 @@
 - /kb/task_statuses.md
 
 ## Known normalization decisions
-- MVP does not include separate editor_agent.
-- Direct writing -> review is valid in MVP after required writing artifacts and handoff to review_agent exist.
+- The current operating model does not include separate editor_agent.
+- Direct writing -> review is valid in the current operating model after required writing artifacts and handoff to review_agent exist.
 - Direct ux-writing -> review is valid when that local stage label is used and required UX writing artifacts and handoff to review_agent exist.
 - editing is optional only as a revision checkpoint or status bridge and does not imply a separate Editor Agent.
 - Writer should not hand off to a non-existing Editor by default.
```

## pipelines/article_pipeline.md

```diff
--- /private/tmp/system-maintenance-retrospective-0012-step-002-before/ai-editorial-office/pipelines/article_pipeline.md	2026-05-30 19:47:04
+++ ai-editorial-office/pipelines/article_pipeline.md	2026-05-30 19:50:36
@@ -44,7 +44,7 @@
 
 ## required agents
 
-By default, only MVP agents may be used for this pipeline. Explicitly legalized non-MVP extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
+By default, only core roles may be used for this pipeline. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
 
 | Stage | Required role | Agent spec | Responsibility |
 | --- | --- | --- | --- |
@@ -55,7 +55,7 @@
 | Review | `review_agent` | `/agents/review_agent.md` | Independently validate draft and artifacts |
 | Finalization | `final_editor` | `/agents/final_editor.md` | Create final deliverable after approved review |
 
-This pipeline must not assign work to non-MVP extension roles by default. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions; revision in MVP is handled by `writer_agent`, not by a separate Editor role.
+This pipeline must not assign work to unauthorized extension roles. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions; revision in the current operating model is handled by `writer_agent`, not by a separate Editor role.
 
 ## required inputs
 
@@ -166,7 +166,7 @@
 
 ## stage sequence
 
-MVP default production sequence:
+Default production sequence:
 
 ```text
 intake -> chief_editor orchestration -> research if needed -> writing -> review -> finalization -> chief_editor final governance decision
@@ -186,7 +186,7 @@
 | 8 | `approved` | `final_editor` | Produce controlled final deliverable | `final.md`, conditional finalization notes/checklist, finalization handoff | `approved` |
 | 9 | `approved` | `chief_editor` | Validate finalization and make governance decision | `final_decision.md`, updated `status.md` | `finalized` or `human_approval_required` |
 
-Direct `writing` -> `review` handoff is valid in MVP after required writing artifacts exist and the latest handoff from `writer_agent` to `review_agent` is recorded. `editing` may be used only as an optional Writer Agent revision or ready-for-review bridge. It must not assign work to a separate Editor role.
+Direct `writing` -> `review` handoff is valid in the current operating model after required writing artifacts exist and the latest handoff from `writer_agent` to `review_agent` is recorded. `editing` may be used only as an optional Writer Agent revision or ready-for-review bridge. It must not assign work to a separate Editor role.
 
 ## status transitions
 
@@ -464,7 +464,7 @@
 - missing `brief.md`, `status.md`, or `orchestration_plan.md`;
 - selected pipeline conflicts with `AGENTS.md`;
 - required agent spec, KB file, or pipeline file is unavailable;
-- task requires a non-MVP production role that is not explicitly legalized in `AGENTS.md`, or uses a legalized extension role outside its allowed scope;
+- task requires an unauthorized extension role, or uses a legalized extension role outside its allowed scope;
 - research is required but research artifacts are missing or insufficient;
 - factual claims are required but `sources.md`, `facts.md`, or `claims_table.md` is missing;
 - Writer Agent would need to invent facts to continue;
@@ -497,7 +497,7 @@
 - impossible factual requirement;
 - missing human decision;
 - request to bypass review;
-- request to use a non-MVP role that is not explicitly legalized in `AGENTS.md`, or to use a legalized extension role outside its allowed scope;
+- request to use an unauthorized extension role, or to use a legalized extension role outside its allowed scope;
 - repeated failure caused by unclear brief;
 - review-gate failure that requires a governance decision.
 
@@ -554,7 +554,7 @@
 - stop and ask Chief Editor if current version state is unclear;
 - confirm current status is valid under `/kb/task_statuses.md`;
 - confirm the selected pipeline is Article Pipeline;
-- confirm current owner role and next role are valid MVP roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
+- confirm current owner role and next role are valid core roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
 - compare `task-manifest.md`, `status.md`, `orchestration_plan.md`, and latest handoff for conflicts;
 - identify the last completed quality gate;
 - verify required artifacts for that gate;
```

## pipelines/social_pipeline.md

```diff
--- /private/tmp/system-maintenance-retrospective-0012-step-002-before/ai-editorial-office/pipelines/social_pipeline.md	2026-05-30 19:47:04
+++ ai-editorial-office/pipelines/social_pipeline.md	2026-05-30 19:50:36
@@ -42,7 +42,7 @@
 
 ## required agents
 
-By default, only MVP agents may be used for this pipeline. Explicitly legalized non-MVP extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
+By default, only core roles may be used for this pipeline. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
 
 | Stage | Required role | Agent spec | Responsibility |
 | --- | --- | --- | --- |
@@ -53,7 +53,7 @@
 | Review | `review_agent` | `/agents/review_agent.md` | Independently validate copy, artifacts, tone, traceability, and governance compliance |
 | Finalization | `final_editor` | `/agents/final_editor.md` | Create final deliverable after approved review |
 
-This pipeline must not assign work to non-MVP extension roles by default. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions; revision in MVP is handled by `writer_agent` for copy changes or `research_agent` for evidence gaps, not by a separate editing role.
+This pipeline must not assign work to unauthorized extension roles. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions; revision in the current operating model is handled by `writer_agent` for copy changes or `research_agent` for evidence gaps, not by a separate editing role.
 
 ## required inputs
 
@@ -166,7 +166,7 @@
 
 ## stage sequence
 
-MVP default production sequence:
+Default production sequence:
 
 ```text
 intake -> chief_editor orchestration -> research if needed -> writing -> review -> finalization -> chief_editor final governance decision
@@ -186,7 +186,7 @@
 | 8 | `approved` | `final_editor` | Produce controlled final deliverable | `final.md`, conditional finalization notes/checklist, finalization handoff | `approved` |
 | 9 | `approved` | `chief_editor` | Validate finalization and make governance decision | `final_decision.md`, updated `status.md` | `finalized` or `human_approval_required` |
 
-Direct `writing` -> `review` handoff is valid in MVP after required writing artifacts exist and the latest handoff from `writer_agent` to `review_agent` is recorded. `editing` may be used only as an optional Writer Agent revision or ready-for-review bridge. It must not assign work to a separate editing role.
+Direct `writing` -> `review` handoff is valid in the current operating model after required writing artifacts exist and the latest handoff from `writer_agent` to `review_agent` is recorded. `editing` may be used only as an optional Writer Agent revision or ready-for-review bridge. It must not assign work to a separate editing role.
 
 ## status transitions
 
@@ -549,7 +549,7 @@
 - missing `brief.md`, `status.md`, or `orchestration_plan.md`;
 - selected pipeline conflicts with `AGENTS.md`;
 - required agent spec, KB file, tone file, or pipeline file is unavailable;
-- task requires a non-MVP production role that is not explicitly legalized in `AGENTS.md`, or uses a legalized extension role outside its allowed scope;
+- task requires an unauthorized extension role, or uses a legalized extension role outside its allowed scope;
 - platform constraints are missing and materially affect copy;
 - tone requirements conflict and cannot be resolved by the current role;
 - platform adaptation would create clickbait drift, factual distortion, or misleading compression;
@@ -588,7 +588,7 @@
 - impossible factual requirement;
 - missing human decision;
 - request to bypass review;
-- request to use a non-MVP role that is not explicitly legalized in `AGENTS.md`, or to use a legalized extension role outside its allowed scope;
+- request to use an unauthorized extension role, or to use a legalized extension role outside its allowed scope;
 - repeated failure caused by unclear platform constraints;
 - review-gate failure that requires a governance decision.
 
@@ -645,7 +645,7 @@
 - stop and ask Chief Editor if current version state is unclear;
 - confirm current status is valid under `/kb/task_statuses.md`;
 - confirm the selected pipeline is Social Pipeline;
-- confirm current owner role and next role are valid MVP roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
+- confirm current owner role and next role are valid core roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
 - compare `task-manifest.md`, `status.md`, `orchestration_plan.md`, and latest handoff for conflicts;
 - identify the last completed quality gate;
 - verify required artifacts for that gate;
```

## pipelines/ux_writing_pipeline.md

```diff
--- /private/tmp/system-maintenance-retrospective-0012-step-002-before/ai-editorial-office/pipelines/ux_writing_pipeline.md	2026-05-30 19:47:04
+++ ai-editorial-office/pipelines/ux_writing_pipeline.md	2026-05-30 19:50:36
@@ -48,7 +48,7 @@
 
 ## required agents
 
-By default, only MVP agents may be used for this pipeline. Explicitly legalized non-MVP extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
+By default, only core roles may be used for this pipeline. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
 
 | Stage | Required role | Agent spec | Responsibility |
 | --- | --- | --- | --- |
@@ -59,7 +59,7 @@
 | Review | `review_agent` | `/agents/review_agent.md` | Independently validate UX copy and artifacts |
 | Finalization | `final_editor` | `/agents/final_editor.md` | Create final deliverable after approved review |
 
-This pipeline must not assign work to non-MVP extension roles by default. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions; revision in MVP is handled by `ux_writer` for UX copy or `research_agent` for evidence gaps, not by a separate Editor role.
+This pipeline must not assign work to unauthorized extension roles. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions; revision in the current operating model is handled by `ux_writer` for UX copy or `research_agent` for evidence gaps, not by a separate Editor role.
 
 ## required inputs
 
@@ -175,7 +175,7 @@
 
 ## stage sequence
 
-MVP default production sequence:
+Default production sequence:
 
 ```text
 intake -> chief_editor orchestration -> research if needed -> ux-writing -> review -> finalization -> chief_editor final governance decision
@@ -195,7 +195,7 @@
 | 8 | `approved` | `final_editor` | Produce controlled final deliverable | `final.md`, conditional finalization notes/checklist, finalization handoff | `approved` |
 | 9 | `approved` | `chief_editor` | Validate finalization and make governance decision | `final_decision.md`, updated `status.md` | `finalized` or `human_approval_required` |
 
-Direct `writing` -> `review` handoff is valid in MVP after required UX writing artifacts exist and the latest handoff from `ux_writer` to `review_agent` is recorded. If a local handoff or orchestration note uses `ux-writing` as the stage label, `ux-writing` -> `review` is valid under the same conditions. `editing` may be used only as an optional UX Writer revision or ready-for-review bridge. It must not assign work to a separate Editor role.
+Direct `writing` -> `review` handoff is valid in the current operating model after required UX writing artifacts exist and the latest handoff from `ux_writer` to `review_agent` is recorded. If a local handoff or orchestration note uses `ux-writing` as the stage label, `ux-writing` -> `review` is valid under the same conditions. `editing` may be used only as an optional UX Writer revision or ready-for-review bridge. It must not assign work to a separate Editor role.
 
 ## status transitions
 
@@ -517,7 +517,7 @@
 - missing `brief.md`, `status.md`, or `orchestration_plan.md`;
 - selected pipeline conflicts with `AGENTS.md`;
 - required agent spec, KB file, glossary, UX guidelines, or pipeline file is unavailable;
-- task requires a non-MVP production role that is not explicitly legalized in `AGENTS.md`, or uses a legalized extension role outside its allowed scope;
+- task requires an unauthorized extension role, or uses a legalized extension role outside its allowed scope;
 - product context is missing or too ambiguous for safe UX writing;
 - UI states, triggers, validation rules, or fallback behavior are missing and affect copy;
 - terminology sources conflict on a product-critical term;
@@ -553,7 +553,7 @@
 - impossible product requirement;
 - missing product owner or human decision;
 - request to bypass review;
-- request to use a non-MVP role that is not explicitly legalized in `AGENTS.md`, or to use a legalized extension role outside its allowed scope;
+- request to use an unauthorized extension role, or to use a legalized extension role outside its allowed scope;
 - repeated failure caused by unclear brief or missing product context;
 - review-gate failure that requires a governance decision.
 
@@ -610,7 +610,7 @@
 - stop and ask Chief Editor if current version state is unclear;
 - confirm current status is valid under `/kb/task_statuses.md`;
 - confirm the selected pipeline is UX Writing Pipeline;
-- confirm current owner role and next role are valid MVP roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
+- confirm current owner role and next role are valid core roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
 - compare `task-manifest.md`, `status.md`, `orchestration_plan.md`, and latest handoff for conflicts;
 - identify the last completed quality gate;
 - verify required artifacts for that gate;
```

## pipelines/review_pipeline.md

```diff
--- /private/tmp/system-maintenance-retrospective-0012-step-002-before/ai-editorial-office/pipelines/review_pipeline.md	2026-05-30 19:47:04
+++ ai-editorial-office/pipelines/review_pipeline.md	2026-05-30 19:49:14
@@ -47,7 +47,7 @@
 
 ## required agents
 
-By default, only MVP agents may be used for this pipeline. Explicitly legalized non-MVP extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
+By default, only core roles may be used for this pipeline. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
 
 | Responsibility | Required role | Agent spec |
 | --- | --- | --- |
@@ -58,7 +58,7 @@
 | Evidence repair, when review finds factual or product evidence gaps | `research_agent` | `/agents/research_agent.md` |
 | Finalization after approved review | `final_editor` | `/agents/final_editor.md` |
 
-This pipeline must not assign review, editing, writing, finalization, or governance work to non-MVP extension roles by default. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
+This pipeline must not assign review, editing, writing, finalization, or governance work to unauthorized extension roles. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
 
 ## required inputs
 
@@ -94,7 +94,7 @@
 
 If required inputs are missing, Review Agent must stop, record the missing input, and recommend `blocked` or `changes_requested` according to `/kb/task_statuses.md`.
 
-Review may start from `review` status or from a direct handoff by `writer_agent` or `ux_writer` when the required artifacts exist and review is required. Missing `editing` status is not a blocker in MVP.
+Review may start from `review` status or from a direct handoff by `writer_agent` or `ux_writer` when the required artifacts exist and review is required. Missing `editing` status is not a blocker in the current operating model.
 
 `task-manifest.md` must be updated at every stage transition, status transition, owner change, blocker change, review outcome change, review artifact state change, and handoff creation. Review cannot be considered complete if `task-manifest.md` is stale. If `task-manifest.md`, `status.md`, latest handoff, and `orchestration_plan.md` conflict, stop and escalate to `chief_editor`.
 
@@ -121,7 +121,7 @@
 | `/tasks/TASK-ID/reviewer-notes.md` | extra reviewer reasoning or caveats needed | `review_agent` |
 | `/tasks/TASK-ID/handoff-review-review-agent-to-TO.md` | always when handing off | `review_agent` |
 
-`TO` must be replaced with the receiving MVP role, or an explicitly legalized extension role whose `AGENTS.md` conditions apply, as a filename slug, for example `chief-editor`, `writer-agent`, `ux-writer`, `research-agent`, or `artist-agent` when visual-extension conditions apply. These slugs are not separate agent names.
+`TO` must be replaced with the receiving core role, or an explicitly legalized extension role whose `AGENTS.md` conditions apply, as a filename slug, for example `chief-editor`, `writer-agent`, `ux-writer`, `research-agent`, or `artist-agent` when visual-extension conditions apply. These slugs are not separate agent names.
 
 ## artifact creation policy
 
@@ -178,7 +178,7 @@
 
 ## stage sequence
 
-MVP default review sequence:
+Default review sequence:
 
 ```text
 writing or ux-writing -> review -> changes if needed -> review -> finalization -> chief_editor governance decision
@@ -196,7 +196,7 @@
 | 6 | `approved` | `final_editor` | Finalize only after approved review | `final.md`, conditional finalization notes/checklist, finalization handoff unless compact finalization is fully traceable through `review.md`, `final.md`, and current `task-manifest.md` | `approved` |
 | 7 | `approved` | `chief_editor` | Make governance decision after finalization | `final_decision.md`, updated `status.md` | `finalized` or `human_approval_required` |
 
-Direct `writing` -> `review` handoff is valid in MVP after required writing artifacts exist and the latest handoff from `writer_agent` or `ux_writer` to `review_agent` is recorded. If a local handoff or orchestration note uses `ux-writing` as the stage label, `ux-writing` -> `review` is valid under the same conditions. Review Agent must not treat a missing `editing` stage as a blocker in MVP. `editing` may be used only as a ready-for-review or revision bridge owned by the production role. It must not assign work to a separate Editor role.
+Direct `writing` -> `review` handoff is valid in the current operating model after required writing artifacts exist and the latest handoff from `writer_agent` or `ux_writer` to `review_agent` is recorded. If a local handoff or orchestration note uses `ux-writing` as the stage label, `ux-writing` -> `review` is valid under the same conditions. Review Agent must not treat a missing `editing` stage as a blocker in the current operating model. `editing` may be used only as a ready-for-review or revision bridge owned by the production role. It must not assign work to a separate Editor role.
 
 ## status transitions
 
@@ -295,7 +295,7 @@
 - `reviewer-notes.md` exists when extra caveats or borderline reasoning do not fit in `review.md`;
 - review outcome is exactly `approved`, `changes_requested`, or `blocked`;
 - review outcome maps to a valid operational status under `/kb/task_statuses.md`;
-- handoff exists to the correct next MVP role or explicitly legalized extension role whose `AGENTS.md` conditions apply;
+- handoff exists to the correct next core role or explicitly legalized extension role whose `AGENTS.md` conditions apply;
 - all review-critical decisions cite artifacts;
 - if outcome is `approved`, finalization can proceed without bypassing review-gate;
 - if outcome is not `approved`, the task is not handed off as ready for finalization.
```

## pipelines/research_pipeline.md

```diff
--- /private/tmp/system-maintenance-retrospective-0012-step-002-before/ai-editorial-office/pipelines/research_pipeline.md	2026-05-30 19:47:04
+++ ai-editorial-office/pipelines/research_pipeline.md	2026-05-30 19:49:14
@@ -35,7 +35,7 @@
 
 ## required agents
 
-By default, only MVP agents may be used. Explicitly legalized non-MVP extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
+By default, only core roles may be used. Explicitly legalized extension roles may be assigned only under `AGENTS.md` conditions and only for their bounded extension scope.
 
 | Stage responsibility | Required role | Agent spec |
 | --- | --- | --- |
@@ -47,7 +47,7 @@
 | Downstream independent verification of drafted material | `review_agent` | `/agents/review_agent.md` |
 | Downstream controlled finalization after approved review | `final_editor` | `/agents/final_editor.md` |
 
-This pipeline does not introduce any additional roles. It must not refer work to non-MVP extension roles by default; explicitly legalized extension roles may be referenced only under `AGENTS.md` conditions.
+This pipeline does not introduce any additional roles. It must not refer work to unauthorized extension roles; explicitly legalized extension roles may be referenced only under `AGENTS.md` conditions.
 
 ## required inputs
 
@@ -81,7 +81,7 @@
 - `/tasks/TASK-ID/open-questions.md`, when questions exist or are deferred;
 - `/tasks/TASK-ID/handoff-research-research-agent-to-TO.md`.
 
-`TO` must be replaced with the receiving MVP role, or an explicitly legalized extension role whose `AGENTS.md` conditions apply, as a filename slug. These slugs are not separate agent names:
+`TO` must be replaced with the receiving core role, or an explicitly legalized extension role whose `AGENTS.md` conditions apply, as a filename slug. These slugs are not separate agent names:
 
 - `writer-agent` for `writer_agent`;
 - `ux-writer` for `ux_writer`;
@@ -344,7 +344,7 @@
 - required facts are unverifiable;
 - high or critical factual sensitivity cannot be supported by adequate evidence;
 - required KB, agent spec, or template is unavailable;
-- handoff cannot identify a valid MVP receiving role or an explicitly legalized extension role whose `AGENTS.md` conditions apply;
+- handoff cannot identify a valid core receiving role or an explicitly legalized extension role whose `AGENTS.md` conditions apply;
 - downstream work would require inventing facts;
 - context is too fragmented to continue and cannot be repaired with `context-summary.md`.
 
@@ -388,7 +388,7 @@
 - each required artifact follows the structure required by `/agents/research_agent.md` or this pipeline;
 - `claims_table.md` clearly states which claims are safe, unsafe, or caveated for drafting;
 - `open-questions.md` clearly marks whether each question blocks downstream work, when real questions exist;
-- `handoff-research-research-agent-to-TO.md` exists with `TO` replaced by a valid MVP receiving role or an explicitly legalized extension role whose `AGENTS.md` conditions apply;
+- `handoff-research-research-agent-to-TO.md` exists with `TO` replaced by a valid core receiving role or an explicitly legalized extension role whose `AGENTS.md` conditions apply;
 - `status.md` records the current status, previous status, responsible role, next action, key artifacts, and blockers;
 - the recommended next status is valid under `/kb/task_statuses.md`;
 - if the recommended downstream stage is `writing` or `review`, all sufficiency criteria are met;
@@ -420,7 +420,7 @@
 - stop and ask Chief Editor if current version state is unclear;
 - confirm current status is valid under `/kb/task_statuses.md`;
 - confirm the selected pipeline is still this pipeline or research is still the active upstream stage;
-- confirm the current owner role and next required role are valid MVP roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
+- confirm the current owner role and next required role are valid core roles or explicitly legalized extension roles whose `AGENTS.md` conditions apply;
 - compare `task-manifest.md`, `status.md`, `orchestration_plan.md`, and the latest handoff for conflicts;
 - check whether required research artifacts are present and current;
 - identify missing, stale, or contradictory artifacts;
```
