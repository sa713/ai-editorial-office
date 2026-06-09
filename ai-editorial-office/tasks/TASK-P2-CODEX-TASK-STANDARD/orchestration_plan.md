# Orchestration Plan

## task summary

- Task ID: TASK-P2-CODEX-TASK-STANDARD
- User goal: implement P2 Codex Task Standard + Check Pack.
- Deliverable: production markdown patch plus review packet.
- Audience/channel: editorial agents and repository reviewers.
- Current active version: current working tree diff.

## task classification

- Task type: system update / reusable standard
- Risk mode: standard
- Factual sensitivity: low; system-rule accuracy matters
- Human approval likely required: unknown
- Rationale: changes task-generation guidance but not roles, pipelines,
  validators, client profiles, or review-gate.

## process depth

- Depth: compact
- Execution profile: compact
- Rationale: small owner is Chief Editor plus reusable KB standard.
- Forbidden depth shortcuts: no new role, governance layer, capability pack,
  validator, or review-gate change.
- Expanded profile trigger, if any: conflict with `AGENTS.md` or pipeline
  ownership.

## selected pipeline

- Pipeline: compact custom system-update workflow
- Why this pipeline: no existing writing/review pipeline directly owns
  production rule patches.
- Pipeline exceptions or local constraints: review remains pending through
  `check-pack.md` / `chatgpt_p2.md`.

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

- Rationale: requested scope, constraints, acceptance criteria, and source of
  truth are explicit.
- Production may start: yes
- If `constrain`: patch only owner files and task-local review packet.

## owner finding

- Current owner of Codex task generation: Chief Editor, because it owns
  normalized brief routing, scope, preflight strategy, role assignment, and
  execution contracts.
- Reusable standard owner: `kb/codex_task_standard.md`.
- Existing partial standard: `master_backlog.md` section 5.
- Existing helper: `scripts/generate_task_pack.py`, read-only context helper;
  it is not task generation logic.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | intake_agent | yes | Provides normalized brief |
| Orchestration | chief_editor | yes | Owns Codex task/check-pack contract |
| Production patch | Codex under routed task | yes | Updates markdown production files |
| Review | review_agent or external reviewer | yes | Pending; use check-pack/report |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | User request and sources | Compact route | Owner identified |
| 2 | Codex | Owner files and backlog | Production patch | Standard added |
| 3 | Codex | Diff and checks | Notes/check-pack/report | Review packet ready |
| 4 | review_agent / external reviewer | Check-pack/report | Review outcome | Pending |

## completion criteria

- Production files updated: yes
- Backlog status updated: yes
- Review packet complete: pending `chatgpt_p2.md`
- Review outcome acceptable: pending
- Governance fields complete: pending review
