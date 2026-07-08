# Orchestration Plan

## task summary

- Task ID: `TASK-ROADMAP-V1-FINALIZE`
- User goal: finalize `ROADMAP.md` as the stable long-term strategic document.
- Deliverable: narrow ROADMAP v1.0 stabilization patch, review, validation, and
  commit.
- Audience/channel: Project Lead and future roadmap readers.
- Current active version: `../../ROADMAP.md`.

## task classification

- Task type: roadmap stabilization
- Risk mode: `low`
- Factual sensitivity: low; work applies explicit review comments.
- Human approval likely required: no before local commit.
- Rationale: user provided exact required changes and validation expectations.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: bounded documentation-only finalization.
- Forbidden depth shortcuts: no review bypass; no changes to excluded files.

## selected pipeline

- Pipeline: `review`
- Why this pipeline: final roadmap text needs independent review before
  finalization.
- Pipeline exceptions or local constraints: no research or architecture design
  work required.

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

- Rationale: user supplied required edits, constraints, validation, and delivery
  requirements.
- Production may start: yes.

## editorial decision frame

- Chosen editorial route: apply only requested review comments to `ROADMAP.md`
  and record compact task trace.
- Why this route serves the task: the mission is finalization, not redesign.
- Alternatives considered:
  - Update `project-state.md` to mirror the rename.
    - Rejected because the user explicitly forbade project-state changes.
  - Sync `/about`.
    - Rejected because the user explicitly forbade `/about` changes.
  - Rework roadmap stage strategy.
    - Rejected because the user forbade strategy and stage changes.
- Writer contract:
  - Result type: narrow roadmap patch.
  - Scope boundary: the five required review comments only.
  - Must include: Project Operating Model, Professional Capability Model rename,
    no framework encouragement, release-first rule, stronger success criterion.
  - Must not include: architecture changes, capability-definition changes,
    project-state changes, `/about` changes, or roadmap redesign.
- Review focus: all required comments applied, no excluded files modified, no
  strategy drift.
- Reroute triggers: conflict with canonical architecture or validation failure.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `chief_editor` | yes | Route and constraints |
| Writing | `writer_agent` | yes | Roadmap patch |
| Review | `review_agent` | yes | Independent check |
| Final governance | `chief_editor` | yes | Closure |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Scope |
| `task-manifest.md` | required | all roles | Restart |
| `status.md` | required | all roles | State history |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `../../ROADMAP.md` | required | project | Finalized roadmap |
| `review.md` | required | Chief Editor | Review gate |
| `final.md` | required | user | Deliverable pointer |
| `final_decision.md` | required | governance | Closure |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | User request and `AGENTS.md` | Task route | Scope bounded |
| 2 | `writer_agent` | `ROADMAP.md` and review comments | Roadmap patch | Required edits applied |
| 3 | `review_agent` | Patch and constraints | `review.md` | Approved or changes requested |
| 4 | `chief_editor` | Review and validation | `final_decision.md` | Ready to commit |

## review requirements

- Review artifact: `review.md`
- Review depth: compact roadmap-finalization review.
- Reviewer independence requirement: reviewer separate from writer role.
- Claims/evidence checks required: required comments applied, excluded files
  untouched, roadmap remains strategic.
