# Task Manifest

## task identity

- Task ID: TASK-0021
- Task title: Письмо участникам встречи УЭК
- Task type: short internal announcement / follow-up email
- Owner/current role: Chief Editor
- Created: 2026-06-02
- Last updated: 2026-06-02

## current state

- Current status: `finalized`
- Selected pipeline: `social_pipeline`
- Risk mode: `low-risk`
- Process depth: `compact`
- Execution profile: `compact`
- Current working artifact: `final.md`
- Latest relevant handoff: `handoff-review-review-agent-to-final-editor.md`
- Next required action: user adds links manually before sending.

## freshness

- Last verified: 2026-06-02
- Verified by: Chief Editor
- Stale if: user changes audience, access instructions, required links, or tone constraints.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `final.md`
- Replaces: `draft.md`
- Deprecated/previous versions: none
- Versions no longer working artifacts: `draft.md` after finalization
- Version conflict state: none
- What to read on restart: `brief.md`, `orchestration_plan.md`, `review.md`, `final.md`, `final_decision.md`
- Old versions read only for: reviewer-governance traceability
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Compact finalization shape allowed: yes
- Human approval required: no for editorial completion; actual sending not assessed.
- Human approval evidence: not applicable
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | normalized request |
| `orchestration_plan.md` | yes | required | compact route |
| `status.md` | yes | required | finalized |
| `draft.md` | no | required | reviewed draft, replaced by final |
| `writer-notes.md` | yes | required | compact rationale |
| `review.md` | yes | required | approved |
| `final.md` | yes | required | final deliverable |
| `final_decision.md` | yes | required | governance decision |
| `claims-used.md` | no | omitted | no separate traceability need |
| `research.md` / `sources.md` / `facts.md` / `claims_table.md` | no | omitted | no research required |
| `qa-checklist.md` / `review-summary.md` | no | omitted | embedded in review |
| `finalization-notes.md` | no | omitted | no controlled changes needing separate notes |

## stale or conflicting state

- None.

## active constraints

- User constraints: short, useful, no recap, links added manually, ordinary working tone, include access and troubleshooting instructions.
- Pipeline constraints: Social Pipeline compact announcement route, review gate preserved.
- Governance constraints: final text cannot be delivered as reviewed without `review.md`; actual sending approval is outside task.

## open questions

- None.

## next action packet

Minimum restart read set:

- `AGENTS.md` invariant summary;
- this manifest;
- `review.md`;
- `final.md`;
- `final_decision.md`;
- `social_pipeline.md` if route needs revalidation.

Next action:

- Role: user
- Action: add actual links manually before sending.
- Expected output: sent email, outside editorial artifact scope.
- Stop conditions: access instructions or audience changes; route back to writing/review.

## lifecycle notes

- Legacy task folders consulted: no
- Old artifact versions consulted: no
- Safe-to-ignore material: UX pipeline after route rejected as non-fitting; article pipeline as heavier fallback.
