# Task Manifest

## task identity

- Task ID: TASK-0031
- Task title: Convert Sber editorial policy PDF to Markdown
- Task type: technical source conversion / external-source transcription
- Owner/current role: chief_editor
- Created: 2026-06-04
- Last updated: 2026-06-04

## current state

- Current status: finalized
- Selected pipeline: compact custom workflow mini-contract
- Risk mode: standard
- Process depth: compact with strict conversion review
- Execution profile: `compact`
- Current working artifact: `sber-editorial-policy.md`
- Latest relevant handoff: none
- Next required action: none; task finalized.

## freshness

- Last verified: 2026-06-04
- Verified by: chief_editor
- Stale if: source PDF changes, another source PDF is added, or the user changes
  output requirements.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set:
  - `Редакционная политика 05.2026.pdf`
  - `sber-editorial-policy.md`
  - `conversion_notes.md`
  - `review.md`
  - `status.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `AGENTS.md`, `project-state.md`, this manifest,
  `brief.md`, `orchestration_plan.md`, `status.md`, and current conversion
  artifacts.
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: yes
- Human approval required: no
- Human approval evidence: not applicable
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Task-local source boundary and conversion rules. |
| `task-manifest.md` | yes | required | Restart pointer and active constraints. |
| `orchestration_plan.md` | yes | required | Compact execution contract. |
| `Редакционная политика 05.2026.pdf` | yes | required source | External source; do not modify. |
| `sber-editorial-policy.md` | yes | required | Converted Markdown output. |
| `conversion_notes.md` | yes | required | Extraction method, cleanup, limits. |
| `review.md` | yes | required | Independent conversion check. |
| `status.md` | yes | required | Lifecycle state and blockers. |
| `final_decision.md` | yes | conditional | Compact Chief Editor final decision after review. |
| `feedback.md` | yes | conditional | Post-delivery feedback and bounded revision boundary. |

## stale or conflicting state

- None.

## active constraints

- User constraints: exact technical conversion; no summary, shortening,
  paraphrase, `/kb` ingestion, or PDF modification.
- Pipeline constraints: editorial entry, preflight decision, role separation,
  review-gate.
- Governance constraints: external source remains external; one task output does
  not become system policy.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- `project-state.md`;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `status.md`;
- current conversion artifacts.

Next action:

- Role: none
- Action: none
- Expected output: task is complete.
- Stop conditions: not applicable.

## lifecycle notes

- Legacy task folders consulted: no; not needed for source conversion.
- Old artifact versions consulted: no; no prior TASK-0031 artifacts exist.
- Safe-to-ignore material: project `/kb` policy files, because the task is
  external-source conversion rather than system rule adoption.
- Post-delivery bounded revision: yes; `Нет` / `Да` and `Хороший пример` /
  `Хороший антипример` blocks were reparsed by OCR word coordinates after user
  feedback.
