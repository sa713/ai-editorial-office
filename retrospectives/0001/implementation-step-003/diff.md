# Step 3 diff

## `ai-editorial-office/templates/artifacts/task_manifest_template.md`

```diff
@@
 Current blockers: `{none_or_short_blocker_list}`
 
+## freshness
+
+Last updated by: `{role}`
+
+Last updated stage: `{stage}`
+
+Latest artifact changes: `{short_list_or_none}`
+
+Known stale risk: `{none_or_short_reason}`
+
+Keep this block operational. It should tell the next role whether the manifest can be trusted for restart; it must not become an audit log.
+
 ## governance state
 
 Review required: `{yes | no | unknown}`
@@
 Human approval required: `{yes | no | unknown}`
 
 Publication/delivery approval: `{not_started | required | granted | not_required | unknown}`
+
+These fields are visibility fields, not a separate status system. Operational task status still comes from `status.md` and `/kb/task_statuses.md`.
+
+Finalization, final governance, and publication/delivery approval are separate. `finalized` does not mean published, delivered, or human-approved unless that approval is explicitly recorded.
 
 ## artifact inventory
@@
 | `status.md` | `{role}` | all | `{missing | present | stale | not_applicable}` | yes | detailed status/history |
 | `orchestration_plan.md` | `chief_editor` | planning | `{missing | present | stale | not_applicable}` | `{yes | no}` | `{notes}` |
 | `{artifact}.md` | `{role}` | `{stage}` | `{missing | present | stale | not_applicable}` | `{yes | no}` | `{notes}` |
 
+## stale or conflicting state
+
+If this manifest conflicts with `status.md`, latest handoff, or `orchestration_plan.md`, stop production work and route to `chief_editor`.
+
+Conflict summary: `{none_or_short_conflict}`
+
+Smallest repair needed: `{none_or_short_repair}`
+
 ## active constraints
```

## `ai-editorial-office/AGENTS.md`

```diff
@@
 `orchestration_plan.md` является execution plan: выбранный pipeline, роли, порядок работ, gates и task-specific contract. Handoff не должен дублировать `task-manifest.md`, `status.md` или `orchestration_plan.md`.
 
-Агент обязан обновлять `task-manifest.md` при stage transition, status transition, owner change, blocker change, handoff creation, review outcome change, finalization status change и final governance status change.
+Агент обязан обновлять `task-manifest.md` при stage transition, status transition, owner change, blocker change, handoff creation, review outcome change, finalization status change и final governance status change. Manifest должен содержать compact freshness и governance visibility, но не должен становиться audit log, approval matrix или вторым `status.md`.
 
 Если `task-manifest.md` конфликтует с `status.md`, latest handoff или `orchestration_plan.md`, агент должен остановиться и escalate to `chief_editor` до продолжения production work.
```

## `ai-editorial-office/agents/chief_editor.md`

```diff
@@
-The Chief Editor must use `task-manifest.md` for routing and must update it on stage completion, status transition, owner change, blocker change, handoff creation, and final governance status change. Keep the manifest compact; put longer rationale in `status.md`, `orchestration_plan.md`, handoffs, or `final_decision.md`.
+The Chief Editor must use `task-manifest.md` for routing and must update it on stage completion, status transition, owner change, blocker change, handoff creation, review outcome change, finalization status change, and final governance status change. Keep freshness and governance visibility compact; put longer rationale in `status.md`, `orchestration_plan.md`, handoffs, or `final_decision.md`.
```

## `ai-editorial-office/project-state.md`

```diff
@@
 - Operational task statuses must come from /kb/task_statuses.md.
 - Local role outcomes must not be treated as operational statuses unless mapped through /kb/task_statuses.md.
 - task-manifest.md is the compact operational source of truth and first task-local restart file.
 - status.md remains detailed status/history.
 - orchestration_plan.md remains the execution plan.
+- task-manifest.md carries compact freshness and governance visibility, not a second status system or audit log.
 - If task-manifest.md conflicts with status.md, latest handoff, or orchestration_plan.md, stop and escalate to chief_editor.
```
