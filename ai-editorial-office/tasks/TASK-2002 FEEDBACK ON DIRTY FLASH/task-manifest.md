# Task Manifest

## task identity

- Task ID: `TASK-2002 FEEDBACK ON DIRTY FLASH`
- Task title: Feedback classification for Dirty Flash
- Task type: customer feedback classification / post-delivery governance
- Owner/current role: Chief Editor
- Created: 2026-06-12
- Last updated: 2026-06-12

## current state

- Current status: finalized
- Selected pipeline: review_pipeline
- Risk mode: standard
- Process depth: compact
- Execution profile: compact
- Client profile: none
- Client profile status: not_applicable
- Current working artifact: `feedback.md`
- Latest relevant handoff: not used; compact Chief Editor classification with independent review recorded in `review.md`
- Next required action: no system action; optional future bounded revision only if user requests it

## freshness

- Last verified: 2026-06-12
- Verified by: Chief Editor
- Stale if: additional similar feedback appears across other tasks, or user requests a TASK-2001 revision.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `feedback.md`, `review.md`, `final_decision.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, `feedback.md`, `review.md`, `final_decision.md`, and the four TASK-2001 source artifacts named in `brief.md`
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
| `brief.md` | yes | required | Normalized feedback task |
| `task-manifest.md` | yes | required | Restart pointer |
| `orchestration_plan.md` | yes | required | Feedback-loop routing |
| `status.md` | yes | required | Lifecycle record |
| `feedback.md` | yes | required | Main classification and decision |
| `review.md` | yes | required | Independent compact review |
| `final_decision.md` | yes | required | Chief Editor governance decision |
| `system_change_proposal.md` | no | omitted | Insufficient evidence; explicitly not created |

## active constraints

- User constraints: apply feedback process; classify type/significance/signal/system-change need; do not change system without sufficient grounds; do not create system update proposal if insufficient data.
- Pipeline constraints: preserve review gate; keep feedback task local; do not turn one feedback item into a global rule.
- Client-profile constraints: none.
- Governance constraints: no KB/watchlist/backlog/system changes without Chief Editor decision and stronger evidence.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `feedback.md`;
- `review.md`;
- `final_decision.md`;
- TASK-2001 source artifacts named in `brief.md`.

Next action:

- Role: Chief Editor
- Action: wait for user decision on whether to request a bounded TASK-2001 revision
- Expected output: no action unless requested
- Stop conditions: user asks to treat this single signal as a system rule without additional evidence

## lifecycle notes

- Legacy task folders consulted: yes, `TASK-2001 DIRTY FLASH` as the delivered source task under feedback.
- Old artifact versions consulted: no.
- Safe-to-ignore material: unrelated task folders and system backlog.
