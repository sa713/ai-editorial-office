# Task Manifest

## task identity

- Task ID: TASK-P15-RAW-BRIEF-NORMALIZATION
- Task title: P1.5 raw brief normalization system update
- Task type: system update / governance patch
- Owner/current role: chief_editor
- Created: 2026-06-09
- Last updated: 2026-06-09

## current state

- Current status: review
- Selected pipeline: compact custom system-update workflow
- Risk mode: standard
- Process depth: compact
- Execution profile: compact
- Client profile: none
- Client profile status: not_applicable
- Current working artifact: production diff for `intake_agent.md` and
  `master_backlog.md`
- Latest relevant handoff: `check-pack.md`
- Next required action: independent review of the patch packet

## freshness

- Last verified: 2026-06-09
- Verified by: Codex
- Stale if: production files change after `chatgpt_report.md` is generated.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: production diff plus
  `chatgpt_report.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, this manifest, `status.md`,
  `orchestration_plan.md`, `implementation-notes.md`, `check-pack.md`,
  `chatgpt_report.md`, and changed production files.
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: pending external/manual review using
  `check-pack.md` and `chatgpt_report.md`
- Review outcome: pending
- Compact finalization shape allowed: not applicable
- Human approval required: unknown
- Human approval evidence: none
- Final decision artifact: not created

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Task-local normalized brief |
| `task-manifest.md` | yes | required | Current restart pointer |
| `status.md` | yes | required | Current lifecycle state |
| `orchestration_plan.md` | yes | required | Compact routing contract |
| `implementation-notes.md` | yes | required by user | Review support |
| `check-pack.md` | yes | required by user | Review support |
| `chatgpt_report.md` | yes | required by user | Generated after checks |

## stale or conflicting state

- None known.

## active constraints

- User constraints: minimal patch; no new roles, pipelines, mandatory artifacts,
  capabilities, validator, visual subsystem, or client-profile changes.
- Pipeline constraints: custom workflow must not weaken review-gate.
- Client-profile constraints: none.
- Governance constraints: no final approval without independent review.

## open questions

- `/about` package is absent in this checkout; sync check fails before content
  comparison.

## next action packet

Minimum restart read set:

- root `AGENTS.md`;
- `ai-editorial-office/AGENTS.md`;
- this manifest;
- `check-pack.md`;
- `chatgpt_report.md`;
- changed production files.

Next action:

- Role: review_agent or external reviewer
- Action: review production patch against acceptance criteria
- Expected output: approve, request changes, or block with specific findings
- Stop conditions: review-gate conflict, source-status rule regression, or
  accidental architecture expansion.

## lifecycle notes

- Legacy task folders consulted: no
- Old artifact versions consulted: no
- Safe-to-ignore material: unrelated untracked task folders.
