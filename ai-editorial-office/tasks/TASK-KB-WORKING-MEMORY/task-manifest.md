# Task Manifest

## task identity

- Task ID: `TASK-KB-WORKING-MEMORY`
- Task title: Knowledge Base as Working Memory
- Task type: high-governance KB/system documentation update
- Owner/current role: `chief_editor`
- Created: 2026-07-02
- Last updated: 2026-07-02

## current state

- Current status: `finalized`
- Selected pipeline: `/pipelines/research_pipeline.md` with custom KB update mini-contract, then writing, review, finalization, and Chief Editor governance
- Risk mode: `high-governance`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: finalized KB working-memory update
- Latest relevant handoff: `handoff-final-editor-to-chief-editor.md`
- Next required action: report completion to user

## freshness

- Last verified: 2026-07-02
- Verified by: `chief_editor`
- Stale if: KB schema, AGENTS/project-state governance, or active KB record structure changes before finalization.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: KB application model v1 and task-local support artifacts
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, this manifest, `status.md`, `orchestration_plan.md`, KB `schema.md`, KB `application-model.md` if present, and changed KB records.
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: no
- Human approval required: no for local artifact creation; yes for any later adoption as binding Studio policy beyond the KB documentation.
- Human approval evidence: not applicable
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Normalized user request. |
| `task-manifest.md` | yes | required | Current state pointer. |
| `status.md` | yes | required | State and transition history. |
| `orchestration_plan.md` | yes | required | Route and KB update contract. |
| `context-study.md` | yes | required | Local context studied before edits. |
| `implementation-report.md` | yes | required | Summary of KB changes and representative records. |
| `handoff-writing-writer-agent-to-review-agent.md` | yes | required | Role transition to review. |
| `review.md` | yes | required | Independent review before finalization; outcome approved. |
| `handoff-review-review-agent-to-final-editor.md` | yes | required | Role transition to finalization. |
| `changed-files.md` | yes | required | Created and changed file list. |
| `final.md` | yes | required after approved review | Final delivery summary. |
| `handoff-final-editor-to-chief-editor.md` | yes | required | Role transition to final governance. |
| `final_decision.md` | yes | required | Chief Editor final governance decision; task finalized. |

## stale or conflicting state

- None.

## active constraints

- User constraints: preserve existing KB structure, readability, and non-journal nature.
- Pipeline constraints: review required before finalization.
- Client-profile constraints: none.
- Governance constraints: do not treat missing BRD Governance/Historian files as invented policy.

## open questions

- BRD Governance and Historian source files were requested but not found by filename search; this will be documented as a source gap, not invented.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `status.md`;
- `orchestration_plan.md`;
- KB `schema.md`, `index.md`, `navigation.md`, `application-model.md` if present;
- changed representative records.

Next action:

- Role: `chief_editor`
- Action: report finalized artifact locations and verification results to the user.
- Expected output: KB model files, schema updates, representative record updates, and task-local report.
- Stop conditions: conflict with AGENTS canonical ownership, unclear BRD/Historian source requirement, or requested change that turns KB into a development journal.

## lifecycle notes

- Legacy task folders consulted: no; current task can be handled from active KB and governance files.
- Old artifact versions consulted: no.
- Safe-to-ignore material: pre-existing unrelated modified files in the worktree.
