# Orchestration Plan

## task summary

- Task ID: `TASK-MASTER-BACKLOG-REPO-PLACEMENT`
- User goal: place the current master backlog into the repo as the main planning artifact.
- Deliverable: `../../ideas/master_backlog.md`
- Audience/channel: AI editorial office planning and ChatGPT/Codex synchronization.
- Current active version: `../../ideas/master_backlog.md`

## task classification

- Task type: system planning artifact placement.
- Risk mode: `low`.
- Factual sensitivity: low; the task uses a provided local source file.
- Human approval likely required: no.
- Rationale: the user specified exact placement and one status-line update.

## process depth

- Depth: `compact`.
- Execution profile: `compact`.
- Rationale: this is repo placement of an existing backlog, not creation of new editorial material.
- Forbidden depth shortcuts: do not alter production files or move this into `/about`.
- Expanded profile trigger, if any: user asks to redesign backlog governance or change production rules.

## selected pipeline

- Pipeline/mode: `compact_maintenance_mode`.
- Why this mode: no standard article/social/UX production pipeline is needed for placing a provided planning artifact.
- Pipeline exceptions or local constraints: content changes are limited to the requested document status update.

## client profile

- Client profile: `none`.
- Client profile status: `not_applicable`.
- Activation reason: not applicable.
- Stop condition: none.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: the local source file exists at `/ideas/master_backlog.md`, the target path is clear, and the only requested text change is explicit.
- Production may start: yes.
- Scope boundary: place backlog as planning artifact; do not edit editorial production system.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Orchestration | Chief Editor | yes | Route task and enforce boundaries |
| File placement | Chief Editor | yes | Copy provided artifact and update requested status line |
| Review | Review Agent | no | Not required because no new editorial content is produced |
| Final governance | Chief Editor | yes | Confirm placement and state |

## required knowledge and evidence

- Required source/evidence files:
  - `/ideas/master_backlog.md`
  - `AGENTS.md`
- Evidence gaps: none blocking.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | restart / governance | Compact state pointer |
| `status.md` | required | restart / governance | State history |
| `orchestration_plan.md` | required | restart / governance | Execution boundary |
| `../../ideas/master_backlog.md` | required | user / planning | Requested artifact |
| `review.md` | omitted | not applicable | No new draft material to review |
| `final_decision.md` | omitted | not applicable | Compact task state is sufficient |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Chief Editor | user request, `AGENTS.md` | route recorded | compact maintenance mode selected |
| 2 | Chief Editor | `/ideas/master_backlog.md` | `../../ideas/master_backlog.md` | file placed |
| 3 | Chief Editor | placed file | updated status line | status reads `active draft / placed in repo` |
| 4 | Chief Editor | git/status checks | final confirmation | production files unchanged |

## review requirements

- Review artifact: not required.
- Review depth: compact placement verification.
- Reviewer independence requirement: not applicable.
- Claims/evidence checks required: verify source file was copied and requested status line changed.

## completion criteria

- `../../ideas/master_backlog.md` exists.
- Document status is `active draft / placed in repo`.
- `/about` remains untouched.
- Production files listed by the user remain untouched.
