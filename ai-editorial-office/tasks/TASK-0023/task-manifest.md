# Task Manifest

## task identity

- Task ID: TASK-0023
- Task title: Подготовка интервью Дарины к публикации
- Task type: editorial article / interview adaptation
- Owner/current role: chief_editor
- Created: 2026-06-03
- Last updated: 2026-06-03

## current state

- Current status: finalized
- Selected pipeline: article_pipeline
- Risk mode: standard
- Process depth: compact editorial pipeline
- Execution profile: compact
- Current working artifact: `final.md`
- Latest relevant handoff: `handoff-finalization-final-editor-to-chief-editor.md`
- Next required action: deliver completed artifacts to user

## freshness

- Last verified: 2026-06-03
- Verified by: chief_editor
- Stale if: source transcript, requested deliverables, or chosen format changes

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `source-transcript.md`, then `analysis.md`, `draft.md`, `review.md`, `final.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, this manifest, `orchestration_plan.md`, `status.md`, `source-transcript.md`
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: yes
- Human approval required: no
- Human approval evidence: not required by task
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Normalized task brief |
| `source-transcript.md` | yes | conditional | Technical extraction from provided `.docx` |
| `orchestration_plan.md` | yes | required | Compact execution contract |
| `status.md` | yes | required | Current task state |
| `analysis.md` | yes | user-required | Editorial analysis and format rationale |
| `outline.md` | yes | pipeline-required | Compact structure before draft |
| `draft.md` | yes | pipeline-required | Review target |
| `review.md` | yes | user-required / pipeline-required | Independent editorial self-check |
| `final.md` | yes | user-required / pipeline-required | Publication-ready material |
| `final_decision.md` | yes | governance | Chief Editor readiness decision |

## stale or conflicting state

- None.

## active constraints

- User constraints: preserve voice, personality, meaning, emotional tone; improve readability and structure.
- Pipeline constraints: review required before finalization; writer and reviewer roles must remain separated.
- Governance constraints: no publication claim without final reviewed artifact.

## open questions

- None blocking. Exact publication venue is not specified; assume internal editorial publication for readers familiar with УЭК/Sber context.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `orchestration_plan.md`;
- `status.md`;
- `source-transcript.md`;
- `article_pipeline.md`.

Next action:

- Role: chief_editor
- Action: deliver `analysis.md`, `final.md`, and `review.md`
- Expected output: completed task response
- Stop conditions: none

## lifecycle notes

- Legacy task folders consulted: no
- Old artifact versions consulted: no
- Safe-to-ignore material: unrelated tasks and retrospectives
