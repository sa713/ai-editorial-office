# Task Manifest

## task identity

- Task ID: `EDITORIAL-SYSTEM-UPDATE-SBER-MODE`
- Task title: Add Sber client-profile mode
- Task type: `editorial system update / process maintenance`
- Owner/current role: none; task finalized
- Created: 2026-06-04
- Last updated: 2026-06-04

## current state

- Current status: `finalized`
- Selected pipeline: `custom workflow mini-contract`
- Risk mode: `standard`
- Process depth: `compact`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `final_decision.md`
- Latest relevant handoff: none
- Next required action: none

## freshness

- Last verified: 2026-06-04
- Verified by: `chief_editor`
- Stale if: Sber client profile, source policy, agent specs, pipelines,
  templates, or `/about` memory files change without updating this task record.

## client profile

Not active for this maintenance task. The task updates the `sber` profile, but
does not itself create a Sber-owned communication.

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved`
- Compact finalization shape allowed: yes
- Human approval required: no for scaffold integration; yes before using any
  changed source version as client-approved policy
- Human approval evidence: user supplied source path
  `/sber-editorial-policy.clean.md`
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Update scope |
| `task-manifest.md` | yes | required | Current state pointer |
| `orchestration_plan.md` | yes | required | Compact maintenance contract |
| `status.md` | yes | required | State history |
| `SYSTEM_UPDATE_REPORT.md` | yes | required | Summary |
| `sber-mode-smoke-test.md` | yes | required | Task-local smoke scenarios |
| `changed-files.md` | yes | required | Change inventory |
| `review.md` | yes | required | Smoke review approved |
| `final_decision.md` | yes | required | Chief Editor final decision |

## active constraints

- Use `ai-editorial-office/` as canonical production tree.
- Treat `/about` as compact ChatGPT memory package.
- Add Sber as isolated client profile, not global editorial policy.
- Do not apply Sber-mode to independent materials where Sber is only mentioned.
- Use source-backed Sber rules only from
  `/kb/clients/sber/editorial-policy.md`.
- If Sber source is missing, stale, or unverified, route as
  `client_profile_status: pending_source` and do not claim Sber-policy
  compliance.

## open questions

- None blocking.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- this manifest;
- `orchestration_plan.md`;
- `status.md`;
- `SYSTEM_UPDATE_REPORT.md`;
- `sber-mode-smoke-test.md`;
- relevant changed system files.

Next action:

- Role: none
- Action: none
- Expected output: none
- Stop conditions: future changes make Sber policy global, hide source status,
  or activate Sber-mode for mere topical mentions

## lifecycle notes

- Legacy task folders consulted: yes, only to identify that `TASK-0031` contains
  historical Sber conversion context; active source for this update is
  `/sber-editorial-policy.clean.md`.
- Old artifact versions consulted: no
- Safe-to-ignore material: unrelated old task content
