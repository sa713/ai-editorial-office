# Orchestration Plan

## task summary

- Task ID: SYSTEM-MAINTENANCE-0017
- User goal: выполнить все рекомендации по актуализации memory package, кроме наполнения пустых examples-файлов.
- Deliverable: updated project state, memory package references, archive path references, and package sync/check mechanism.
- Audience/channel: local editorial system maintenance.
- Current active version: current repository files.

## task classification

- Task type: editorial system update / memory package maintenance
- Risk mode: low-risk
- Factual sensitivity: low
- Human approval likely required: no
- Rationale: requested changes are housekeeping and navigation alignment, not policy redesign.

## selected workflow

- Pipeline: custom workflow mini-contract
- Why this workflow: no standard production content pipeline is needed; work updates system documentation and support script.
- Review gate preserved: compact verification through file count, copied-file comparison, and reference search.
- Governance model unchanged: yes.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Orchestration | Chief Editor | yes | Route and constrain update |
| Implementation | Chief Editor | yes | Maintenance edit under user instruction |
| Verification | Chief Editor | yes | Check package count, sync, and references |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | restart | Entry discipline |
| `orchestration_plan.md` | required | governance | Documents compact maintenance route |
| `status.md` | required | restart | Records state and completion |
| `review.md` | omitted | none | User asked direct update; verification is mechanical and compact |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| Route | Chief Editor | user request, AGENTS.md | task artifacts | compact route recorded |
| Update | Chief Editor | recommendations | edited files | requested scope complete |
| Verify | Chief Editor | changed files | check results | no count or sync failures |

## escalation conditions

- Stop if `/about` exceeds 20 files.
- Stop if copied files diverge after sync.
- Stop if a recommendation would require changing examples files.
- Stop if updating archive references would change active policy semantics.

## completion criteria

- `project-state.md` no longer claims pipeline materialization as active next task.
- `/about` is documented as ChatGPT memory package.
- historical references to the retired `ai-editorial-office/project_tree.md` path are updated or clearly redirected.
- a check mechanism exists outside `/about`.
- `/about` remains exactly 20 files.
