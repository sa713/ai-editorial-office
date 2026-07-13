# Task Manifest

## task identity

- Task ID: `TASK-OUTCOME-FIRST-DELIVERABLE-SELECTION`
- Task title: Add Outcome-First Deliverable Selection
- Task type: canonical system capability update
- Owner/current role: `chief_editor`
- Created: 2026-07-13
- Last updated: 2026-07-13

## current state

- Current status: `finalized`
- Selected deliverable: bounded canonical patch, synthetic test, implementation
  report, and complete diff
- Selected pipeline: `review_pipeline`
- Risk mode: `standard`
- Process depth: `normal`
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `final.md`
- Latest relevant handoff: `handoff-finalization-final-editor-to-chief-editor.md`
- Next required action: deliver package to user

## artifact inventory

| Artifact | Required | State | Purpose |
| --- | --- | --- | --- |
| `brief.md` | yes | current | Scope and acceptance contract |
| `orchestration_plan.md` | yes | current | Deliverable-first route and execution contract |
| `status.md` | yes | current | Lifecycle and blocker state |
| `implementation-report.md` | yes | current | User-requested implementation report |
| `complete-diff.md` | yes | current after final mechanical generation | User-requested complete patch record |
| `review.md` | yes | current: approved | Independent review verdict |
| `handoff-implementation-writer-agent-to-review-agent.md` | yes | current | Review scope and independence boundary |
| `handoff-review-review-agent-to-writer-agent.md` | yes | current | Bounded OFD-001 repair contract |
| `handoff-repair-writer-agent-to-review-agent.md` | yes | current | Repair evidence and bounded re-review scope |
| `handoff-review-approval-review-agent-to-final-editor.md` | yes | current | Approved-scope finalization contract |
| `handoff-finalization-final-editor-to-chief-editor.md` | yes | current | Finalization delta and closeout action |
| `final.md` | yes | current | Final delivery pointer |
| `final_decision.md` | yes | current | Chief Editor governance decision |

## runtime execution

| Stream ID | Canonical function | Scope | Artifacts/packages | Boundary |
| --- | --- | --- | --- | --- |
| `implementation-main` | Writer / implementation function | Canonical owner edits, templates, tests, report, diff | repository patch and task-local package | Does not independently review or approve |
| `review-independent` | Review Agent | Patch, tests, architecture constraints, scope | `review.md` and bounded findings | Must be a separate role instance |

Model/mode metadata: not recorded; no runtime nickname is used as process
identity.
