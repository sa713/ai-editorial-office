# Orchestration Plan

## task summary

- Task ID: `TASK-PROJECT-ROADMAP`
- User goal: introduce the project roadmap as the strategic document for AI
  Editorial Office.
- Deliverable: `ai-editorial-office/ROADMAP.md` plus lightweight navigation.
- Audience/channel: repository maintainers and future Codex/editorial-system
  work.
- Current active version: `../../ROADMAP.md`

## task classification

- Task type: documentation-only system strategy update
- Risk mode: `standard`
- Factual sensitivity: low; source-bound to existing project roadmap/backlog
  and user constraints
- Human approval likely required: no
- Rationale: the change is documentation-only but strategy-adjacent, so review
  must verify ownership boundaries and non-goals.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: no architecture, behavior, lifecycle, role, pipeline, review-gate,
  capability registry, or framework-boundary changes are allowed.
- Forbidden depth shortcuts: no review bypass; no silent promotion of roadmap
  to canonical operational owner.
- Expanded profile trigger, if any: instruction conflict, canonical ownership
  conflict, or discovery that the roadmap source is insufficient.

## selected pipeline

- Pipeline: `review`
- Why this pipeline: the task requires independent validation before
  finalization of a repository document.
- Pipeline exceptions or local constraints: Writer creates the strategy
  document candidate directly as `ROADMAP.md`; review checks that the candidate
  preserves meaning and does not become operational canon.

## client profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: not applicable
- Non-activation reason, if considered and rejected: no Sber-owned or
  Sber-policy task.
- Client-profile files: none
- Stop condition: any attempt to apply client policy.

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

- Rationale: user supplied clear goal, constraints, deliverables, forbidden
  areas, validation commands, and deliver-back requirements.
- Production may start: yes
- If `ask`: not applicable
- If `constrain`: constrain to documentation and discoverability updates only.
- If `block`: not applicable

## editorial decision frame

- Chosen editorial route: create a strategic roadmap document from the
  consolidated roadmap/backlog content and add minimal navigation.
- Why this route serves the task: it makes strategy discoverable while keeping
  operational ownership in canonical files.
- Alternatives considered:
  - Alternative route, one line: add roadmap text into `AGENTS.md`.
    - Why rejected, one line: would make strategy look like canonical
      operational policy.
  - Alternative route, one line: update only `ideas/master_backlog.md`.
    - Why rejected, one line: user explicitly requested `ROADMAP.md` as the
      strategic document.
  - Alternative route, one line: reference roadmap broadly across many files.
    - Why rejected, one line: user requested lightweight navigation only.
- Writer contract:
  - Result type: strategic roadmap document and light navigation.
  - Angle or reader path: document role, principles, roadmap phases, strategic
    fit check, maintenance.
  - Scope boundary: preserve existing roadmap meaning and user constraints.
  - Must include: strategic/non-canonical boundary; P0-P10 roadmap phases;
    future work fit check; conflict rule that canonical architecture wins.
  - Must not include: new roadmap items, architecture changes, governance
    changes, lifecycle changes, capability ownership changes, implementation
    checklist behavior, `/about` sync.
  - Source boundary and confidence: high confidence from current task plus
    `ideas/master_backlog.md`; no external research.
- Review focus: meaning preservation, no operational ownership drift,
  forbidden-file compliance, and navigation minimalism.
- Reroute triggers: roadmap conflicts with canonical files, omits roadmap
  items, invents items, or requires architecture changes.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `chief_editor` | yes | User request sufficient |
| Research | `research_agent` | no | Source is local project roadmap/backlog |
| Writing | `writer_agent` | yes | Create roadmap candidate |
| Review | `review_agent` | yes | `review.md` required |
| Finalization | `final_editor` | yes | Finalize reviewed candidate |
| Final governance | `chief_editor` | yes | `final_decision.md` |

## required knowledge and evidence

- Required KB: `AGENTS.md` ownership map and review-gate rules.
- Required source/evidence files:
  - `ideas/master_backlog.md`
  - current user task
  - root `README.md`
  - `project-state.md`
- Evidence gaps: none known.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Scope and constraints |
| `task-manifest.md` | required | all roles | Restart and current state |
| `status.md` | required | all roles | Status history |
| `orchestration_plan.md` | required | all roles | Routing contract |
| `../../ROADMAP.md` | required | maintainers | Requested deliverable |
| root `../../../README.md` | conditional | maintainers | Lightweight navigation |
| `../../project-state.md` | conditional | maintainers | Current strategic state note |
| `review.md` | required | final editor, chief editor | Review gate |
| `final.md` | required after review | chief editor | Compact finalization pointer |
| `final_decision.md` | required after finalization | maintainers | Governance closure |
| `qa-checklist.md` | omitted | none | Review checklist fits in `review.md` |
| `review-summary.md` | omitted | none | `review.md` is sufficient |
| `open-questions.md` | omitted | none | No open questions |
| `finalization-notes.md` | omitted | none | No controlled meaning changes after review |
| `finalization-checklist.md` | omitted | none | Compact finalization is sufficient |

## structure-before-writing plan

- Reader path: role of roadmap -> strategic context -> principles -> phases ->
  fit check -> maintenance.
- Section roles: keep strategy separate from operational ownership.
- Required structure: explicit authority boundary; P0-P10 phases; non-goals;
  future-work screening questions.
- Duplication risks: avoid copying canonical ownership details beyond a short
  boundary statement.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | User task, `AGENTS.md`, project state | Routing artifacts | Review-ready route selected |
| 2 | `writer_agent` | Source roadmap/backlog and constraints | `ROADMAP.md`, nav edits | Candidate ready for review |
| 3 | `review_agent` | Candidate and task artifacts | `review.md` | Verdict recorded |
| 4 | `final_editor` | Approved review | `final.md` | Final deliverable recorded |
| 5 | `chief_editor` | Finalized artifacts | `final_decision.md` | Governance closure recorded |

## status transitions

- Starting status: `intake`
- Next expected status: `review`
- Status owner: `chief_editor`
- Status update trigger: candidate roadmap and navigation edits created.

## review requirements

- Review artifact: `review.md`
- Review depth: compact standard review
- Reviewer independence requirement: reviewer must not be `writer_agent`
- Claims/evidence checks required: source preservation and canonical
  ownership boundary
- Optional review artifacts justified: no
