# Orchestration Plan

## task summary

- Task ID: TASK-P15-RAW-BRIEF-NORMALIZATION
- User goal: add raw brief normalization to the editorial intake system.
- Deliverable: production markdown patch plus review packet.
- Audience/channel: editorial agents and repository reviewers.
- Current active version: current working tree diff.

## task classification

- Task type: system update / governance patch
- Risk mode: standard
- Factual sensitivity: low; system-rule accuracy matters
- Human approval likely required: unknown
- Rationale: changes role behavior but not review-gate, roles, client profiles,
  validators, or external artifacts.

## process depth

- Depth: compact
- Execution profile: compact
- Rationale: narrow production owner is `intake_agent.md`; backlog update is
  required by user.
- Forbidden depth shortcuts: no bypass of Chief Editor routing, no fake
  independent review, no new architecture layer.
- Expanded profile trigger, if any: conflict with `AGENTS.md` or broader
  pipeline implications.

## selected pipeline

- Pipeline: compact custom system-update workflow
- Why this pipeline: no existing writing/review pipeline directly owns
  production rule patches.
- Pipeline exceptions or local constraints: review remains pending through
  `check-pack.md` / `chatgpt_report.md`.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `unclear` |
| Missing data strategy | `proceed` |

- Rationale: requested files, constraints, acceptance criteria, and source of
  truth are explicit.
- Production may start: yes
- If `ask`: not applicable
- If `constrain`: patch only listed production areas and task-local review
  packet
- If `block`: not applicable

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | intake_agent | yes | Normalize user request into task brief |
| Orchestration | chief_editor | yes | Route compact system update |
| Production patch | Codex acting under routed task | yes | Update markdown production files |
| Review | review_agent or external reviewer | yes | Pending; use check-pack/report |
| Final governance | chief_editor | if applicable | Only after review approval |

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | restart/review | Editorial entry discipline |
| `status.md` | required | restart/review | State tracking |
| `orchestration_plan.md` | required | restart/review | Routing contract |
| `implementation-notes.md` | required by user | reviewer | Explain patch scope |
| `check-pack.md` | required by user | reviewer | Review packet |
| `review.md` | omitted for now | reviewer/chief_editor | No independent review has been performed yet |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | intake_agent | Raw user request | `brief.md` | Task normalized |
| 2 | chief_editor | Brief and source-of-truth files | This plan and manifest | Route confirmed |
| 3 | Codex | Current intake/backlog files | Production diff | Patch complete |
| 4 | Codex | Diff and checks | Notes, check-pack, report | Review packet ready |
| 5 | review_agent / external reviewer | Check-pack/report | Review outcome | Pending |

## review requirements

- Review artifact: pending
- Review depth: compact system-patch review
- Reviewer independence requirement: required before final governance
- Claims/evidence checks required: verify patch matches source-of-truth files
  and user acceptance criteria
- Optional review artifacts justified: no

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Guidance bloat | Intake becomes harder to scan | reviewer | Check compactness |
| Fantasy normalization | Raw request still invites invented fields | reviewer | Check hard limits and examples |
| `/about` absent | Memory sync check cannot pass | chief_editor | Record failure; do not invent package |

## completion criteria

- Production files updated: yes
- Backlog status updated: yes
- Review packet complete: yes
- Review outcome acceptable: pending
- Governance fields complete: pending review
