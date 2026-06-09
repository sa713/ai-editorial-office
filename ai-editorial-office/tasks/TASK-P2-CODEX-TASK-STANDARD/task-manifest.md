# Task Manifest

## task identity

- Task ID: TASK-P2-CODEX-TASK-STANDARD
- Task title: P2 Codex Task Standard + Check Pack
- Task type: system update / reusable standard
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
- Current working artifact: production diff plus `chatgpt_p2.md`
- Latest relevant handoff: `check-pack.md`
- Next required action: independent review of the patch packet

## governance state

- Review required: yes
- Review artifact/current version: pending external/manual review using
  `check-pack.md` and `chatgpt_p2.md`
- Review outcome: pending
- Compact finalization shape allowed: not applicable
- Human approval required: unknown
- Human approval evidence: none
- Final decision artifact: not created

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Normalized task brief |
| `task-manifest.md` | yes | required | Restart pointer |
| `orchestration_plan.md` | yes | required | Compact route |
| `status.md` | yes | required | State history |
| `implementation-notes.md` | yes | required by user | Implementation support |
| `check-pack.md` | yes | required by user | Review support |
| `chatgpt_p2.md` | yes | required by user | Generated after checks |

## active constraints

- User constraints: minimal patch; no new agents, roles, pipelines, capability
  packs, validators, governance layer, or review-gate change.
- Pipeline constraints: custom workflow must not weaken review-gate.
- Governance constraints: no final approval without independent review.

## open questions

- `/about` package is absent in this checkout; sync check is expected to fail.

## next action packet

Minimum restart read set:

- root `AGENTS.md`;
- `ai-editorial-office/AGENTS.md`;
- this manifest;
- `check-pack.md`;
- `chatgpt_p2.md`;
- changed production files.

Next action:

- Role: review_agent or external reviewer
- Action: review production patch against acceptance criteria
- Expected output: approve, request changes, or block with specific findings
- Stop conditions: review-gate conflict, role expansion, or check-pack
  becoming a review replacement.
