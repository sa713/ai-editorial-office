# Task Manifest

## task identity

- Task ID: `SYSTEM-MAINTENANCE-0022`
- Task title: GitHub private publishing preflight
- Task type: `editorial system maintenance / publication safety audit`
- Owner/current role: none; task finalized
- Created: 2026-06-04
- Last updated: 2026-06-04

## current state

- Current status: `finalized`
- Selected workflow: `custom workflow mini-contract`
- Risk mode: `high-governance`
- Process depth: `compact`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `final_decision.md`
- Latest relevant handoff: none
- Next required action: none for this step; future publication cleanup requires
  separate human approval

## freshness

- Last verified: 2026-06-04
- Verified by: `chief_editor`
- Stale if: repository structure, tracked binary/source files, `.gitignore`, or
  publishing constraints change before GitHub publication.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: root publishing preflight files and
  this task-local routing package
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `PUBLISHING_AUDIT.md`, `.gitignore`,
  `GITHUB_PUBLISHING_CHECKLIST.md`, `README.md`, this manifest,
  `orchestration_plan.md`, `status.md`
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: `approved_with_risks`
- Compact finalization shape allowed: yes, after review because no final
  editorial copy is being published
- Human approval required: yes before any GitHub push or repository publication
- Human approval evidence: not present
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `task-manifest.md` | yes | required | Current task state |
| `orchestration_plan.md` | yes | required | Publishing-preflight route and boundaries |
| `status.md` | yes | required | Status and transitions |
| `README.md` | yes | user-required | Root service file |
| `.gitignore` | yes | user-required | Publishing safety ignore rules |
| `GITHUB_PUBLISHING_CHECKLIST.md` | yes | user-required | Manual pre-push checklist |
| `PUBLISHING_AUDIT.md` | yes | user-required | Main audit result |
| `review.md` | yes | required | Independent review of safety scope |
| `final_decision.md` | yes | required | Chief Editor final governance note |

## active constraints

- Do not change `AGENTS.md`.
- Do not change agents, pipelines, templates, review-gate, roles, or editorial
  rules.
- Do not delete task folders or source materials.
- Do not push, create a GitHub repository, or publish anything.
- Treat real task materials, client-specific policy, binary/source files, and
  possible personal/internal data as publication risks.

## open questions

- Which tracked source/binary files should be removed from the Git index before
  private GitHub publication: requires human decision in a later step.
- Whether Sber/client-specific materials may be stored in a private GitHub repo:
  requires human approval.

## next action packet

Minimum restart read set:

- `AGENTS.md`;
- `ai-editorial-office/AGENTS.md`;
- this manifest;
- `orchestration_plan.md`;
- `status.md`;
- root publishing preflight files.

Next action:

- Role: none
- Action: no further action in this step
- Expected output: none
- Stop conditions: any request to push, create GitHub repo, delete working
  materials, alter review-gate, or change canonical editorial rules

## lifecycle notes

- Legacy task folders consulted: yes, only by file path and selected metadata to
  identify publication risks.
- Old artifact versions consulted: no.
- Safe-to-ignore material: task content not needed for publication-risk
  classification.
