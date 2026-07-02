# Task Manifest

## Task Identity

- Task ID: `TASK-PORTAL-AS-QUESTIONNAIRE`
- Task title: Помочь составить опросник защищённости автоматизированных систем
- Task type: portal task publication
- Owner/current role: Chief Editor
- Created: 2026-06-10
- Last updated: 2026-06-10

## Current State

- Current status: `human_approval_required`
- Selected pipeline: `article_pipeline`
- Risk mode: `standard`
- Process depth: `compact`
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `portal_task_draft.md`; controlled final copy also in `final.md`
- Latest relevant handoff: none; compact execution state is captured in `task_analysis.md`, `review.md`, and this manifest.
- Next required action: human owner approves or revises before portal publication.

## Freshness

- Last verified: 2026-06-10
- Verified by: Chief Editor
- Stale if: source brief changes, author clarifies CIA(T)/КА ФО in a way that changes wording, or portal owner requests a different format.

## Current Version Pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `portal_task_draft.md`, `final.md`, `review.md`, `final_decision.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, `task_analysis.md`, `portal_task_draft.md`, `review.md`, `final_decision.md`
- Do not use latest modified as source of truth: yes

## Governance State

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Compact finalization shape allowed: yes
- Human approval required: yes, before actual portal publication
- Human approval evidence: not provided
- Final decision artifact: `final_decision.md`

## Artifact Inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Source input and done criteria. |
| `orchestration_plan.md` | yes | required | Pipeline and compact routing. |
| `task_analysis.md` | yes | required by user | Problem, result, competencies, uncertainties. |
| `portal_task_draft.md` | yes | required by user | Ready portal publication. |
| `review.md` | yes | required | Approved. |
| `final.md` | yes | required by pipeline | Controlled final copy. |
| `final_decision.md` | yes | required | Approved for next step; human publication approval pending. |
| `status.md` | yes | required | Current state and history. |

## Stale Or Conflicting State

- None.

## Active Constraints

- User constraints: final text must be understandable without context, useful, practical, clear about contribution, and not invent facts.
- Pipeline constraints: review required before finalization; writer/reviewer/final governance separated.
- Client-profile constraints: none.
- Governance constraints: publication requires human approval.

## Open Questions

- What exactly does `CIA(T)` mean?
- What does `КА ФО` mean and should it appear in public-facing task text?
- What format should the final questionnaire have for model ingestion?
- Do existing materials include questions, weights, answer scales, or only conceptual notes?

## Next Action Packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `brief.md`;
- `portal_task_draft.md`;
- `review.md`;
- `final_decision.md`.

Next action:

- Role: human owner
- Action: approve publication or request a bounded revision.
- Expected output: approval decision or specific revision comments.
- Stop conditions: do not publish if human approval is missing or if clarified terms materially change the draft.

## Lifecycle Notes

- Legacy task folders consulted: no; no need for historical examples.
- Old artifact versions consulted: no; none exist.
- Safe-to-ignore material: no external source artifacts.
