# Task Manifest

## task identity

- Task ID: TASK-0024
- Task title: Behavioral audit of the editorial system
- Task type: research / behavioral audit
- Owner/current role: chief_editor
- Created: 2026-06-04
- Last updated: 2026-06-04

## current state

- Current status: finalized
- Selected pipeline: research_pipeline with audit/report deliverables and review gate
- Risk mode: standard
- Process depth: full
- Execution profile: expanded
- Current working artifact: `final_decision.md`
- Latest relevant handoff: `handoff-research-research-agent-to-review-agent.md`
- Next required action: none; audit complete

## freshness

- Last verified: 2026-06-04
- Verified by: chief_editor
- Stale if: review outcome changes, final decision changes, or audit artifacts are revised

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `executive-summary.md`, `behavioral-audit.md`, `systemic-errors.md`, `useful-mechanisms.md`, `top-3-improvements.md`, `final_decision.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: this manifest, `executive-summary.md`, `behavioral-audit.md`, `systemic-errors.md`, `useful-mechanisms.md`, `top-3-improvements.md`, `review.md`, `final_decision.md`
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: no
- Human approval required: no
- Human approval evidence: not applicable
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Normalized user request and constraints |
| `task-manifest.md` | yes | required | Current task pointer |
| `status.md` | yes | required | State history |
| `orchestration_plan.md` | yes | required | Audit routing and scope |
| `sources.md` | yes | required | Task artifact sample and source classes |
| `research.md` | yes | required | Evidence base and findings |
| `executive-summary.md` | yes | required | Executive summary |
| `behavioral-audit.md` | yes | required | Stage-by-stage behavioral audit |
| `systemic-errors.md` | yes | required | Error catalog |
| `useful-mechanisms.md` | yes | required | Strong solution catalog |
| `top-3-improvements.md` | yes | required | Prioritized recommendations |
| `handoff-research-research-agent-to-review-agent.md` | yes | conditional | Role transfer to review |
| `review.md` | yes | required | Independent review approved audit package |
| `final_decision.md` | yes | required | Chief Editor governance conclusion |

## stale or conflicting state

- None.

## active constraints

- User constraints: recommendations only; do not change existing system files or completed task artifacts.
- Pipeline constraints: research separated from review and final governance.
- Governance constraints: final decision requires review.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `status.md`;
- `review.md`, `final_decision.md`, and the requested audit artifacts.

Next action:

- Role: none
- Action: none
- Expected output: none
- Stop conditions: not applicable

## lifecycle notes

- Legacy task folders consulted: yes, because the audit requires historical behavior evidence.
- Old artifact versions consulted: yes, only as evidence of behavior, not as active task state.
- Safe-to-ignore material: extracted images, binary source files, generated media, and non-editorial assets unless needed to explain process behavior.
