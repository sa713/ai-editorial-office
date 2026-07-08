# Task Manifest

## task identity

- Task ID: TASK-EDITORIAL-COMPETENCY-LANDSCAPE
- Task title: Research Editorial Competency Landscape For AI Editorial Office
- Task type: research
- Owner/current role: chief_editor
- Created: 2026-07-08
- Last updated: 2026-07-08

## current state

- Current status: approved
- Selected pipeline: research_pipeline
- Risk mode: standard
- Process depth: full
- Execution profile: expanded
- Client profile: none
- Client profile status: not_applicable
- Current working artifact: `ai-editorial-office/research/editorial_competency_landscape.md`
- Latest relevant handoff: none
- Next required action: run validation and commit only this task's files.

## freshness

- Last verified: 2026-07-08
- Verified by: chief_editor
- Stale if: report, review, or validation results change.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `ai-editorial-office/research/editorial_competency_landscape.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: this manifest, `orchestration_plan.md`,
  `status.md`, report, and `review.md` if present.
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: not applicable
- Human approval required: no
- Human approval evidence: user requested research delivery after validation.
- Final decision artifact: not applicable

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Research goal, scope, constraints. |
| `task-manifest.md` | yes | required | Restart pointer. |
| `orchestration_plan.md` | yes | required | Routing and process contract. |
| `status.md` | yes | required | Current state and transitions. |
| `ai-editorial-office/research/editorial_competency_landscape.md` | yes | required | Main deliverable requested by user. |
| `review.md` | yes | required | Independent review approved. |

## stale or conflicting state

- None.

## active constraints

- User constraints: research only; no canon, agent, pipeline, project-state,
  implementation-task, legacy repo, `/about`, or `diff_intake.md` changes.
- Pipeline constraints: research pipeline; review required before delivery.
- Client-profile constraints: none.
- Governance constraints: preliminary architecture notes only, no decisions.

## open questions

- None.

## next action packet

Minimum restart read set:

- `ai-editorial-office/AGENTS.md` or invariant summary;
- this manifest;
- `orchestration_plan.md`;
- `status.md`;
- active research report, if present;
- `review.md`, if present.

Next action:

- Role: chief_editor
- Action: validate diff scope and commit task files.
- Expected output: clean validation result and commit hash.
- Stop conditions: any need to alter canon, agents, pipelines, project state,
  `/about`, `diff_intake.md`, or legacy repository.

## lifecycle notes

- Legacy task folders consulted: no.
- Old artifact versions consulted: no.
- Safe-to-ignore material: pre-existing unrelated dirty files in `/about` and
  root `diff_intake.md`.
