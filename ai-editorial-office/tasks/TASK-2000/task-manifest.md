# Task Manifest

## Task Identity

- Task ID: TASK-2000
- Task title: Business requirements for "Dashboard of Employee Hobbies"
- Task type: business requirements synthesis
- Owner/current role: `chief_editor`
- Created: 2026-06-10
- Last updated: 2026-06-10

## Current State

- Current status: `finalized`
- Selected pipeline: `article_pipeline`
- Risk mode: `high-governance`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `business-requirements.md`
- Latest relevant handoff: `handoff-writing-writer-agent-to-review-agent-round-2.md`
- Next required action: user/business owner review of the revised finalized
  deliverable.

## Freshness

- Last verified: 2026-06-10
- Verified by: `chief_editor`
- Stale if: source drafts change, new source files are added, or review changes
  the required deliverable scope.

## Current Version Pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `business-requirements.md` plus
  source and evidence artifacts
- Replaces: not applicable
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, `orchestration_plan.md`, `status.md`,
  source drafts, and completed research/writing/review artifacts.
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## Governance State

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Compact finalization shape allowed: no
- Human approval required: yes, after delivery for business/product acceptance
- Human approval evidence: pending user/business owner approval
- Final decision artifact: `final_decision.md`

## Artifact Inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | User request normalized. |
| `orchestration_plan.md` | yes | required | Pipeline and preflight recorded. |
| `status.md` | yes | required | Current status is `writing`. |
| `БТ дашборд хобби.md` | yes | source | Must be read. |
| `БТ календарь.md` | yes | source | Must be read. |
| `БТ хобби.md` | yes | source | Must be read. |
| `research.md` | yes | required | Source synthesis complete. |
| `sources.md` | yes | required | Source list complete. |
| `facts.md` | yes | required | Source-backed requirements extracted. |
| `claims_table.md` | yes | required | Claim traceability complete. |
| `outline.md` | yes | required | Structure created. |
| `business-requirements.md` | yes | required | Revised deliverable approved by review. |
| `writer-notes.md` | yes | required | Consolidation notes created. |
| `claims-used.md` | yes | required | Final claims mapped to source evidence. |
| `review.md` | yes | required | Review outcome: `approved` after bounded revision. |
| `final_decision.md` | yes | required | Governance decision recorded. |

## Stale or Conflicting State

- None.

## Active Constraints

- User constraints: produce one coherent Russian BRD; follow the requested
  14-section structure; describe functionality through roles and user stories;
  do not invent unsupported functionality.
- Pipeline constraints: review is mandatory before final governance.
- Client-profile constraints: none.
- Governance constraints: high-governance source traceability; personal-data and
  HR-related uncertainties must not be hidden.

## Open Questions

- None blocking production. Source-level ambiguities are captured in
  `research.md` and should be carried into the final document.

## Next Action Packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `status.md`;
- latest relevant handoff;
- the three source drafts;
- `sources.md`;
- `facts.md`;
- `research.md`;
- `claims_table.md`.

Next action:

- Role: user / business owner
- Action: review `business-requirements.md` and answer open questions as needed.
- Expected output: approval, requested revisions, or decisions on open questions.
- Stop conditions: implementation planning should not treat open questions as
  resolved requirements.

## Lifecycle Notes

- Legacy task folders consulted: no; not needed.
- Old artifact versions consulted: no; none exist.
- Safe-to-ignore material: unrelated repository files outside TASK-2000.
