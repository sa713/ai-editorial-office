# Orchestration Plan

## task summary

- Task ID: `TASK-BUILD-PROJECT-BACKLOG`
- User goal: create the operational implementation backlog from the current
  roadmap.
- Deliverable: `../../BACKLOG.md`, review, validation, and commit.
- Audience/channel: Project Lead and future release execution.
- Current active version: `../../BACKLOG.md`.

## task classification

- Task type: operational planning
- Risk mode: `low`
- Factual sensitivity: low; work translates current roadmap structure.
- Human approval likely required: no before local commit.
- Rationale: user provided structure, allowed statuses, constraints, and
  validation expectations.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: documentation-only planning artifact with constrained structure.
- Forbidden depth shortcuts: no review bypass; no changes to excluded files.

## selected pipeline

- Pipeline: `review`
- Why this pipeline: the backlog is a planning artifact that needs independent
  review for structure, completeness, and boundary preservation.
- Pipeline exceptions or local constraints: no research or capability
  implementation required.

## client profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: not applicable.
- Non-activation reason: no client-owned content.
- Client-profile files: none.
- Stop condition: any attempt to apply client-specific policy.

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

- Rationale: current roadmap and user constraints are sufficient to create the
  backlog.
- Production may start: yes.

## editorial decision frame

- Chosen editorial route: create one backlog document using Stage -> Release ->
  Task hierarchy and task tables with only the allowed fields.
- Why this route serves the task: it translates strategy into executable work
  without duplicating roadmap narrative or changing architecture.
- Alternatives considered:
  - Add backlog status to roadmap.
    - Rejected because roadmap and backlog have separate purposes.
  - Update project-state or capability files.
    - Rejected because the user forbade architecture and capability changes.
  - Create a detailed issue-style tracker.
    - Rejected because the user specified the exact task field set.
- Writer contract:
  - Result type: operational backlog.
  - Scope boundary: releases and executable tasks derived from `ROADMAP.md`.
  - Must include: completed work as Done, Engineering Review as Done, current
    active work, ordered dependencies, objective success criteria.
  - Must not include: architecture changes, governance rules, capability
    definitions, pipeline changes, or roles.
- Review focus: every roadmap stage represented, releases executable, task
  fields limited to the allowed set, status values valid.
- Reroute triggers: missing roadmap stage, invalid task status, or excluded-file
  modification.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `chief_editor` | yes | Route and constraints |
| Writing | `writer_agent` | yes | Backlog creation |
| Review | `review_agent` | yes | Independent check |
| Final governance | `chief_editor` | yes | Closure |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Scope |
| `task-manifest.md` | required | all roles | Restart |
| `status.md` | required | all roles | State history |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `../../BACKLOG.md` | required | project | Operational execution plan |
| `review.md` | required | Chief Editor | Review gate |
| `final.md` | required | user | Deliverable pointer |
| `final_decision.md` | required | governance | Closure |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | User request and `AGENTS.md` | Task route | Scope bounded |
| 2 | `writer_agent` | `ROADMAP.md` | `BACKLOG.md` | Stages, releases, and tasks mapped |
| 3 | `review_agent` | Backlog and constraints | `review.md` | Approved or changes requested |
| 4 | `chief_editor` | Review and validation | `final_decision.md` | Ready to commit |

## review requirements

- Review artifact: `review.md`
- Review depth: compact planning-artifact review.
- Reviewer independence requirement: reviewer separate from writer role.
- Claims/evidence checks required: roadmap coverage, task field compliance,
  status value compliance, current active release, no excluded-file changes.
