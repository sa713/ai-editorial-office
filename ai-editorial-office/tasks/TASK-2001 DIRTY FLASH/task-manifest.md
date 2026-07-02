# Task Manifest

## task identity

- Task ID: `TASK-2001 DIRTY FLASH`
- Task title: Dirty Flash photoshoot concept
- Task type: editorial brief normalization / creative production pack
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
- Current working artifact: `photo_concept.md`, `model_brief.md`, `photographer_cheatsheet.md`, `editorial_decision.md`
- Latest relevant handoff: not used; compact single-turn task, role separation recorded in `orchestration_plan.md` and `review.md`
- Next required action: user review / optional revision request

## freshness

- Last verified: 2026-06-12
- Verified by: Chief Editor
- Stale if: source brief changes, user changes concept direction, or new mandatory references are added

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: final working set listed above
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, `Dirty Flash.md`, `orchestration_plan.md`, `status.md`, current active artifact set, `review.md`, `final_decision.md`
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: yes
- Human approval required: no
- Human approval evidence: not required for local draft pack
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `Dirty Flash.md` | yes | source | Raw consultant text |
| `brief.md` | yes | required | Normalized task brief |
| `task-manifest.md` | yes | required | Current task pointer |
| `orchestration_plan.md` | yes | required | Compact routing contract |
| `status.md` | yes | required | Lifecycle record |
| `photo_concept.md` | yes | required | Concept artifact |
| `model_brief.md` | yes | required | Model-facing brief |
| `photographer_cheatsheet.md` | yes | required | On-shoot cheat sheet |
| `editorial_decision.md` | yes | required | Editorial rationale |
| `review.md` | yes | required | Independent compact review |
| `final_decision.md` | yes | required | Chief Editor governance decision |

## active constraints

- User constraints: preserve source idea; remove repeats, contradictions, noise; produce four named files; living language; no corporate style; no camera settings unless conceptually necessary.
- Pipeline constraints: `article_pipeline` governs lifecycle and review gate; local artifact names replace generic article draft/final outputs by user request; roles recorded; all artifacts stay in task folder.
- Client-profile constraints: none.
- Governance constraints: final decision only after `review.md`.

## open questions

- None.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `brief.md`;
- `Dirty Flash.md`;
- current active artifact set;
- `review.md`;
- `final_decision.md`.

Next action:

- Role: Chief Editor
- Action: receive user feedback or archive after user acceptance
- Expected output: optional bounded revision or no action
- Stop conditions: user asks to change concept direction beyond source boundary

## lifecycle notes

- Legacy task folders consulted: no
- Old artifact versions consulted: no
- Safe-to-ignore material: unrelated task folders
