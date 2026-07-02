# Orchestration Plan

## task summary

- Task ID: `SYSTEM-MAINTENANCE-0022`
- User goal: prepare the local AI editorial office project for safe future
  publication to a private GitHub repository, without publishing now.
- Deliverable: root `.gitignore`, `README.md`,
  `GITHUB_PUBLISHING_CHECKLIST.md`, `PUBLISHING_AUDIT.md`, and a short list of
  publication risks.
- Audience/channel: single local project owner; no external publication in this
  step.
- Current active version: repository state on 2026-06-04.

## task classification

- Task type: `editorial system maintenance / publication safety audit`
- Risk mode: `high-governance`
- Rationale: the work concerns potential GitHub publication, sensitive working
  materials, client-specific policy, secrets, binaries, and corporate-boundary
  risk.
- Human approval likely required: yes before any push, publication, deletion,
  or index cleanup.

## selected workflow

- Workflow: `custom workflow mini-contract`
- Why this workflow: no dedicated publishing-preflight pipeline exists; article,
  social, UX, and research pipelines do not fit this service task.
- Review gate preserved: yes.
- Governance model unchanged: yes.

## assigned roles

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Entry/routing | `chief_editor` | yes | Activate editorial entry, classify risk, set boundaries |
| Inventory/audit | `chief_editor` | yes | Inspect file structure and produce root audit files |
| Review | `review_agent` | yes | Check scope, risks, and forbidden changes |
| Final governance | `chief_editor` | yes | Record final decision and remaining human approval needs |

No new roles are added. Visual subsystem is not activated.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | restart / governance | Editorial entry discipline |
| `orchestration_plan.md` | required | restart / governance | Route and constraints |
| `status.md` | required | restart / governance | State transitions |
| `.gitignore` | required by user | repository owner | Publishing safety defaults |
| `README.md` | required by user if missing | repository owner | Minimal project description |
| `GITHUB_PUBLISHING_CHECKLIST.md` | required by user | repository owner | Manual pre-push controls |
| `PUBLISHING_AUDIT.md` | required by user | repository owner | Main audit result |
| `review.md` | required | Chief Editor | High-governance safety review |
| `final_decision.md` | required | user / restart | Final governance note |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | user request, AGENTS | route and task artifacts | boundaries recorded |
| 2 | `chief_editor` | filesystem, Git status, Git index | risk inventory | risky paths classified |
| 3 | `chief_editor` | existing `.gitignore` and missing root docs | service files | requested files exist |
| 4 | `review_agent` | changed files and audit | `review.md` | verdict recorded |
| 5 | `chief_editor` | `review.md` | `final_decision.md`, status update | no publication performed |

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | confirmed: local project owner |
| Channel/context | confirmed: local preflight before possible private GitHub repo |
| Deliverable | defined: service files and audit |
| Source boundary | defined: local filesystem and Git index only |
| Success criterion | defined by user criteria |
| Approval boundary | defined: no push/repo creation; human approval required later |
| Missing data strategy | constrain: flag risky files rather than delete or publish |

## review requirements

- Review artifact: `review.md`.
- Review focus: requested files exist, risks are explicit, no forbidden system
  files changed, no GitHub publication occurred.
- Reviewer independence: `review_agent` reviews the package after
  `chief_editor` creates it.

## stop conditions

- Stop before any GitHub push or repository creation.
- Stop before deleting or untracking task/source materials.
- Stop if a required change would alter `AGENTS.md`, roles, pipelines,
  review-gate, templates, or editorial rules.
