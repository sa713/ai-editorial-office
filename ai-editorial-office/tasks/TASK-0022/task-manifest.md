# Task Manifest

## task identity

- Task ID: TASK-0022
- Task title: Переписать ответ ответственному подразделению
- Task type: compact editorial rewrite
- Owner/current role: chief_editor
- Created: 2026-06-03
- Last updated: 2026-06-03

## current state

- Current status: finalized
- Selected pipeline: Article Pipeline lifecycle, compact editorial rewrite mode
- Risk mode: standard
- Process depth: compact
- Execution profile: compact
- Current working artifact: `task.md`
- Latest relevant handoff: `handoff-finalization-final-editor-to-chief-editor.md`
- Next required action: none; task ready for user review/use.

## freshness

- Last verified: 2026-06-03
- Verified by: chief_editor
- Stale if: user changes the question, asks to add new facts, or requires publication approval.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `task.md`, `final.md`, `editorial-note.md`
- Replaces: original answer in `task.md`
- Deprecated/previous versions: original answer before rewrite
- Versions no longer working artifacts: original answer
- Version conflict state: none
- What to read on restart: `brief.md`, `orchestration_plan.md`, `source-snapshot.md`, `task.md`, `review.md`, `final.md`
- Old versions read only for: comparison / reviewer-governance traceability
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: yes
- Human approval required: unknown for external publication; not required for editorial completion
- Human approval evidence: none
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `task.md` | yes | required | User-facing file updated; question preserved. |
| `source-snapshot.md` | yes | required | Original question and answer captured before rewrite for review traceability. |
| `brief.md` | yes | required | Scope and source boundary. |
| `orchestration_plan.md` | yes | required | Compact route and role assignment. |
| `status.md` | yes | required | Lifecycle and review state. |
| `draft.md` | yes | required | Reviewed rewrite candidate. |
| `writer-notes.md` | yes | required | Writer constraints and source-boundary notes. |
| `review.md` | yes | required | Independent compact review. |
| `final.md` | yes | required | Controlled final version. |
| `editorial-note.md` | yes | required by user | Short improvement note. |
| Handoffs | yes | required for role transitions | Compact role transfers. |

## stale or conflicting state

- None.

## active constraints

- User constraints: change only the answer; do not change the question; preserve facts and meaning; add no new promises, timelines, decisions, or obligations.
- Pipeline constraints: review required; role separation preserved.
- Governance constraints: final readiness is editorial, not publication approval.

## open questions

- None for the editorial rewrite.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `brief.md`;
- `source-snapshot.md`;
- `task.md`;
- `review.md`;
- `final.md`.

Next action:

- Role: none
- Action: none
- Expected output: none
- Stop conditions: any request to add new facts or approve publication requires new routing.

## lifecycle notes

- Legacy task folders consulted: no.
- Old artifact versions consulted: original task content captured in `source-snapshot.md`.
- Safe-to-ignore material: research, sources, claims table, separate QA checklist, and review summary are intentionally omitted.
