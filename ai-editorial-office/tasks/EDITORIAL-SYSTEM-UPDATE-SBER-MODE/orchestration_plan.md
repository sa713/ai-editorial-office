# Orchestration Plan

## task summary

- Task ID: `EDITORIAL-SYSTEM-UPDATE-SBER-MODE`
- User goal: apply Sber-mode update to the AI Editorial Office repository.
- Deliverable: repo diff adding an isolated Sber client profile and routing
  rules.
- Audience/channel: internal AI Editorial Office maintainers.
- Current active version: current branch `sber-client-profile`.

## task classification

- Task type: `editorial system update / process maintenance`
- Risk mode: `standard`
- Factual sensitivity: source-policy handling and governance-sensitive routing
- Human approval likely required: no for integration; yes before treating future
  changed policy versions as client-approved
- Rationale: changes system rules, but scope is bounded to client profile and
  task templates.

## process depth

- Depth: `compact`
- Execution profile: `expanded`
- Rationale: system-file change needs traceability, smoke checks, and source
  status recording.
- Forbidden depth shortcuts: no global Sber policy, no invented Sber rules, no
  Sber-mode for topical mentions, no review bypass.
- Expanded profile trigger: production rules and `/about` memory package both
  change.

## selected pipeline

- Pipeline: custom workflow mini-contract
- Why this pipeline: repository maintenance does not produce a user-facing
  editorial text, but AGENTS entry discipline still applies.
- Pipeline exceptions or local constraints: use maintenance artifacts instead of
  article/social/UX production artifacts.

## client profile

- Client profile: `none` for this maintenance task
- Client profile status: `not_applicable`
- Activation reason: not a Sber-owned communication; this task modifies the
  `sber` client profile.
- Client-profile files changed:
  - `/kb/clients/sber/README.md`
  - `/kb/clients/sber/usage-rules.md`
  - `/kb/clients/sber/editorial-policy.md`
  - `/kb/clients/sber/source-notes.md`
  - `/kb/clients/sber/sber-review-checklist.md`
- Stop condition: Sber policy is promoted into global AI Editorial Office
  policy or used without explicit `client_profile: sber`.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: user supplied update files and then supplied the cleaned Sber
  policy source path.
- Production may start: yes

## required roles

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `intake_agent` | yes | Normalize maintenance brief |
| Orchestration | `chief_editor` | yes | Route, maintain manifest/status |
| Implementation | `chief_editor` | yes | Apply bounded system update |
| Review | `review_agent` | yes | Smoke-check routing and source isolation |
| Final governance | `chief_editor` | yes | Record final decision |

## required knowledge and evidence

- Required KB: `AGENTS.md`, relevant production agent specs, pipelines,
  templates, `/kb/clients/sber/`.
- Required source/evidence files:
  - `/Users/sa/Downloads/!!!!!ai/sber_mode_update.diff`
  - `/Users/sa/Downloads/!!!!!ai/ai_editorial_office_sber_update.zip`
  - `/Users/sa/Downloads/!!!!!ai/SYSTEM_UPDATE_REPORT_SBER_MODE.md`
  - `/Users/sa/Downloads/!!!!!ai/sber-mode-smoke-test.md`
  - `/sber-editorial-policy.clean.md`
- Evidence gaps: none blocking.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | AGENTS and update package | routing decision | production may start |
| 2 | `chief_editor` | diff and zip | `/about` updates, profile files | changes are bounded |
| 3 | `chief_editor` | source policy path | source imported into profile | no global promotion |
| 4 | `review_agent` | smoke-test cases | `review.md` | checks pass or blockers recorded |
| 5 | `chief_editor` | review outcome | `final_decision.md` | task finalized or blocked |

## review requirements

- Review artifact: `review.md`
- Review depth: compact smoke review
- Reviewer independence requirement: review must check implementation against
  saved artifacts, not rely on implementation intent.
- Claims/evidence checks required: source status, activation/non-activation,
  pending_source fallback, global-policy isolation.

## completion criteria

- Production tree contains isolated `/kb/clients/sber/`.
- `/about` memory files are patched from provided diff.
- Manifest and templates include `client_profile`, `client_profile_status`, and
  `client_profile_files`.
- Agents and pipelines load client profile only when explicitly active.
- Smoke-test exists and covers activation, non-activation, source-present, and
  pending-source behavior.
- Review confirms Sber policy is not global.
