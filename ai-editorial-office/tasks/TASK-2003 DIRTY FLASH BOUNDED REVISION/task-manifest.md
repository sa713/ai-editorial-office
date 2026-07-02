# Task Manifest

## task identity

- Task ID: `TASK-2003 DIRTY FLASH BOUNDED REVISION`
- Task title: Dirty Flash bounded revision
- Task type: bounded revision / creative editorial update
- Owner/current role: Chief Editor
- Created: 2026-06-12
- Last updated: 2026-06-12

## current state

- Current status: finalized
- Selected pipeline: article_pipeline
- Risk mode: standard
- Process depth: compact
- Execution profile: compact
- Client profile: none
- Client profile status: not_applicable
- Current working artifact: `photo_concept_v2.md`, `model_brief_v2.md`, `photographer_cheatsheet_v2.md`, `revision_notes.md`
- Latest relevant handoff: not used; compact bounded revision with review recorded in `review.md`
- Next required action: user review

## freshness

- Last verified: 2026-06-12
- Verified by: Chief Editor
- Stale if: user requests a different direction, broader rewrite, or system-level change.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: v2 artifact set listed above
- Replaces: TASK-2001 working set for revised use, while v1 remains historical.
- Deprecated/previous versions: TASK-2001 `photo_concept.md`, `model_brief.md`, `photographer_cheatsheet.md`
- Versions no longer working artifacts: none deleted; v1 should be treated as previous, not current, for this revision.
- Version conflict state: none
- What to read on restart: `brief.md`, this manifest, `orchestration_plan.md`, v2 artifact set, `revision_notes.md`, `review.md`, `final_decision.md`, TASK-2002 `feedback.md`
- Old versions read only for: comparison / reviewer-governance traceability
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
| `brief.md` | yes | required | Normalized revision scope |
| `task-manifest.md` | yes | required | Current version pointer |
| `orchestration_plan.md` | yes | required | Revision routing |
| `status.md` | yes | required | Lifecycle record |
| `photo_concept_v2.md` | yes | required | Revised concept |
| `model_brief_v2.md` | yes | required | Revised model-facing brief |
| `photographer_cheatsheet_v2.md` | yes | required | Revised on-shoot tool |
| `revision_notes.md` | yes | required | Revision explanation |
| `review.md` | yes | required | Independent review |
| `final_decision.md` | yes | required | Governance closure |

## active constraints

- User constraints: bounded revision only; shift center to loss of propriety without loss of control; preserve Dirty Flash atmosphere and visual language.
- Pipeline constraints: review gate preserved; no system changes.
- Client-profile constraints: none.
- Governance constraints: v2 must be reviewed before final decision.

## open questions

- None.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- TASK-2002 `feedback.md`;
- v2 artifact set;
- `revision_notes.md`;
- `review.md`;
- `final_decision.md`.

Next action:

- Role: Chief Editor
- Action: deliver v2 for user review
- Expected output: optional bounded revision if requested
- Stop conditions: user asks to change the core concept beyond bounded revision.

## lifecycle notes

- Legacy task folders consulted: yes, TASK-2001 and TASK-2002 are direct inputs.
- Old artifact versions consulted: yes, TASK-2001 v1 files for bounded revision.
- Safe-to-ignore material: unrelated task folders.
