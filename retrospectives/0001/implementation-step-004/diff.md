# Step 4 diff

## `ai-editorial-office/AGENTS.md`

```diff
@@
 - длинные источники и черновики нужно сводить в краткие task-local summaries перед передачей следующей роли;
 - решения, допущения и открытые вопросы фиксируются в файлах, а не только в сообщениях;
-- если контекст фрагментирован между несколькими файлами, агент создаёт или обновляет `context-summary.md`;
+- если контекст фрагментирован, long-running work затрудняет restart или обычных manifest/status/handoff недостаточно, агент может создать или обновить `context-summary.md`;
 - перед review агент проверяет не только текущий черновик, но и brief, research, sources и последние handoff-заметки;
 - если агент не уверен, что видит актуальную версию артефакта, он перечитывает файл из `/tasks/TASK-ID/`.
@@
-Handoff не заменяет основные артефакты этапа. Он является короткой delta-запиской, которая ссылается на `task-manifest.md` вместо повторения полного состояния задачи. Handoff должен содержать только то, что изменилось, созданные или обновлённые артефакты, изменившиеся ограничения, blockers, next role, next action, expected outputs и escalation conditions.
+Handoff не заменяет основные артефакты этапа. Он является короткой role-to-role delta-запиской, которая ссылается на `task-manifest.md` вместо повторения полного состояния задачи. Handoff должен содержать только то, что изменилось, созданные или обновлённые артефакты, изменившиеся ограничения, blockers, next role, next action, expected outputs и escalation conditions.
+
+`compact-handoff.md` не является role-to-role handoff. Это final/user-facing transfer summary: что сделано, где лежат итоговые артефакты, что остаётся за human owner и какие approval/send caveats важны.
+
+`context-summary.md` не является обычным handoff или status update. Это recovery artifact после context fragmentation, long-running work или handoff failure, когда `task-manifest.md`, `status.md` и последний handoff недостаточны для безопасного restart. Он остаётся optional.
@@
 | `orchestration_plan.md` | selected pipeline, roles, artifact scope, gates | narrative status log or handoff delta |
 | handoff files | short delta-transfer between roles | manifest, status, orchestration plan, full artifact lists |
+| `compact-handoff.md` | final/user-facing transfer summary | role-to-role transfer, status history, full review |
+| `context-summary.md` | recovery after context fragmentation or long-running work | normal status update, final handoff, routine role transfer |
 | `writer-notes.md` / `ux-writer-notes.md` | production-role assumptions, caveats, decisions for review | review findings or finalization notes |
```

## `ai-editorial-office/templates/artifacts/handoff_template.md`

```diff
@@
 Use one receiving role in the filename. If routing is uncertain, choose the immediate receiving role and describe alternate routes inside the handoff body, not in the filename.
 
-Handoff files describe what changed since the previous task state and what the next agent should do. They must not repeat the full `status.md`, `task-manifest.md`, `orchestration_plan.md`, task artifact inventory, KB list, restart checklist, or lifecycle history.
+Handoff files are role-to-role delta transfers. They describe what changed since the previous task state and what the next agent should do. They must not repeat the full `status.md`, `task-manifest.md`, `orchestration_plan.md`, task artifact inventory, KB list, restart checklist, or lifecycle history.
 
 Artifact minimalism: create a handoff only for an actual role transfer or escalation. Handoff is delta-transfer, not a restart encyclopedia or duplicate status log.
+
+Do not use this template for `compact-handoff.md` or `context-summary.md`. `compact-handoff.md` is a final/user-facing transfer summary. `context-summary.md` is an optional recovery artifact after context fragmentation, long-running work, or handoff failure.
```

## `ai-editorial-office/agents/chief_editor.md`

```diff
@@
-The handoff must follow `/templates/artifacts/handoff_template.md`. It must reference `task-manifest.md`, summarize only what changed, name the next role and action, list expected and forbidden outputs, and include escalation conditions.
+The handoff must follow `/templates/artifacts/handoff_template.md`. It is a role-to-role delta transfer: reference `task-manifest.md`, summarize only what changed, name the next role and action, list expected and forbidden outputs, and include escalation conditions.
 
 The handoff must not repeat the full manifest, status history, orchestration plan, KB list, restart checklist, or task artifact inventory.
+
+Do not use `compact-handoff.md` for role routing. Use it only as a final/user-facing transfer summary when the user needs a compact closeout. Use `context-summary.md` only when context fragmentation, long-running work, or handoff failure makes normal restart files insufficient.
@@
 If the context is too large:
 
-- create or update `context-summary.md`;
+- create or update `context-summary.md` only when it is needed for recovery;
 - preserve references to source files;
 - record what was omitted;
 - avoid making decisions from omitted material.
```

## `ai-editorial-office/project-state.md`

```diff
@@
 - If task-manifest.md conflicts with status.md, latest handoff, or orchestration_plan.md, stop and escalate to chief_editor.
 - Latest handoff is delta-based and should reference task-manifest.md instead of repeating manifest, status, orchestration, KB, restart notes, or full task state.
 - Handoff filenames use one receiving role; route ambiguity belongs inside the handoff body.
+- compact-handoff.md is final/user-facing transfer summary, not role-to-role handoff.
+- context-summary.md is optional recovery after fragmentation or long-running work, not a routine status update.
 - Late-stage task-manifest next action packets should list only files the next role truly needs.
```
