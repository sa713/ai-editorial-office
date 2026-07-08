# Orchestration Plan

## task summary

- Task ID: `TASK-ROADMAP-REWRITE`
- User goal: completely replace the project roadmap with a timeless long-term
  strategy document.
- Deliverable: rewritten `ROADMAP.md`, lightweight reference updates, review,
  validation, and commit.
- Audience/channel: Project Lead and future roadmap readers.
- Current active version: `../../ROADMAP.md`.

## task classification

- Task type: roadmap strategy rewrite
- Risk mode: `standard`
- Factual sensitivity: low; work reflects current repository state and user
  direction.
- Human approval likely required: no before local commit.
- Rationale: user explicitly requested the rewrite and final commit hash.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: documentation-only strategy rewrite with bounded integration.
- Forbidden depth shortcuts: no review bypass; no canonical architecture edits.

## selected pipeline

- Pipeline: `review`
- Why this pipeline: the output is a strategic document that needs independent
  review for scope, structure, and boundary preservation.
- Pipeline exceptions or local constraints: no external research required.

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

- Rationale: user supplied structure, constraints, validation, and delivery
  requirements.
- Production may start: yes.

## editorial decision frame

- Chosen editorial route: replace `ROADMAP.md` completely and update only
  lightweight navigation/current-state references that would otherwise conflict.
- Why this route serves the task: the mission says the old roadmap is obsolete
  and should not be merged forward.
- Alternatives considered:
  - Preserve old P0-P10 material in an appendix.
    - Rejected because the user forbade old phases, history, backlog, and
      retrospective notes.
  - Update capability definitions to match the new roadmap.
    - Rejected because capability definitions are out of scope.
  - Sync `/about`.
    - Rejected because the user explicitly said not to sync `/about` if only
      roadmap drift is created.
- Writer contract:
  - Result type: concise strategic roadmap.
  - Scope boundary: vision, philosophy, stable foundation, evolution model,
    major stages, current stage, architectural rules, success criteria.
  - Must include: Professional Competency Model as active stage, Engineering
    Review complete, Professional Analysis next planned release.
  - Must not include: old P0-P10 phases, backlog detail, implementation
    history, architecture specification, release notes, or task tracker detail.
- Review focus: complete replacement, readability, timelessness, no architecture
  changes, no canonical ownership changes.
- Reroute triggers: conflict with `AGENTS.md`, accidental canonical behavior
  change, or validation failure.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `chief_editor` | yes | Route and constraints |
| Writing | `writer_agent` | yes | Roadmap rewrite |
| Review | `review_agent` | yes | Independent check |
| Final governance | `chief_editor` | yes | Closure |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Scope |
| `task-manifest.md` | required | all roles | Restart |
| `status.md` | required | all roles | State history |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `../../ROADMAP.md` | required | project | Strategic roadmap |
| `../../../README.md` | conditional | project readers | Lightweight navigation |
| `../../project-state.md` | conditional | project state readers | Current stage alignment |
| `review.md` | required | Chief Editor | Review gate |
| `final.md` | required | user | Deliverable pointer |
| `final_decision.md` | required | governance | Closure |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | User request and `AGENTS.md` | Task route | Scope bounded |
| 2 | `writer_agent` | Current state and user structure | New roadmap | Old roadmap replaced |
| 3 | `writer_agent` | Navigation/state references | Lightweight updates | References aligned |
| 4 | `review_agent` | Rewritten docs | `review.md` | Approved or changes requested |
| 5 | `chief_editor` | Review and validation | `final_decision.md` | Ready to commit |

## review requirements

- Review artifact: `review.md`
- Review depth: compact strategic-document review.
- Reviewer independence requirement: reviewer separate from writer role.
- Claims/evidence checks required: current stage, next release, no old roadmap
  structure, no architecture change, no `/about` sync.
