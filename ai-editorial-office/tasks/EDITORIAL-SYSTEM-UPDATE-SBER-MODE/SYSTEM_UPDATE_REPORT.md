# System Update Report: Sber Client Profile

Task ID: `EDITORIAL-SYSTEM-UPDATE-SBER-MODE`

Date: 2026-06-04

## Implemented

- Added task-scoped client-profile model to `AGENTS.md`.
- Added `/kb/clients/sber/` scaffold.
- Imported cleaned Sber editorial policy from
  `/sber-editorial-policy.clean.md` into `/kb/clients/sber/editorial-policy.md`.
- Added activation/non-activation rules for Sber-mode.
- Added source-status discipline: `active`, `pending_source`, `not_applicable`.
- Added Sber review checklist.
- Updated Intake Agent and Chief Editor responsibilities.
- Updated Writer, UX Writer, Review Agent, and Final Editor to read and preserve
  active client profiles.
- Updated pipeline input references for active client profiles.
- Updated memory summaries for task manifest fields and memory usage.
- Added smoke-test scenarios.

## Source status

The cleaned Sber editorial policy is now present in the client profile. The
profile remains task-scoped and must not become global AI Editorial Office
policy.

If that source is later removed, stale, or unverified, tasks must use
`client_profile_status: pending_source` and must not claim Sber-policy
compliance.

## Files changed in `/about`

- `AGENTS.md`
- `project_tree.md`
- `project-state.md`
- `CHATGPT_MEMORY_ARTIFACT_TEMPLATES.md`
- `CHATGPT_MEMORY_USAGE_RULES.md`
- `intake_agent.md`
- `chief_editor.md`
- `writer_agent.md`
- `ux_writer.md`
- `review_agent.md`
- `final_editor.md`
- `article_pipeline.md`
- `social_pipeline.md`
- `ux_writing_pipeline.md`
- `review_pipeline.md`

## New production files to add

- `ai-editorial-office/kb/clients/sber/README.md`
- `ai-editorial-office/kb/clients/sber/usage-rules.md`
- `ai-editorial-office/kb/clients/sber/editorial-policy.md`
- `ai-editorial-office/kb/clients/sber/source-notes.md`
- `ai-editorial-office/kb/clients/sber/sber-review-checklist.md`
- `ai-editorial-office/templates/artifacts/task_manifest_template.md`

## Existing production files updated

- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/project-state.md`
- `ai-editorial-office/kb/00_index.md`
- `ai-editorial-office/agents/intake_agent.md`
- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/agents/writer_agent.md`
- `ai-editorial-office/agents/ux_writer.md`
- `ai-editorial-office/agents/review_agent.md`
- `ai-editorial-office/agents/final_editor.md`
- `ai-editorial-office/pipelines/article_pipeline.md`
- `ai-editorial-office/pipelines/social_pipeline.md`
- `ai-editorial-office/pipelines/ux_writing_pipeline.md`
- `ai-editorial-office/pipelines/review_pipeline.md`
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`
- `ai-editorial-office/templates/tasks/*.md`
- `ai-editorial-office/tests/README.md`
- `ai-editorial-office/tests/sber-mode-smoke-test.md`

## Verification

- `/about` package sync check passed.
- `git diff --check` passed.
- Smoke checks recorded in `review.md`.

## Human follow-up before production use

Run Sber-mode smoke test with a real Sber text and confirm the imported source
is the approved version for the task or client context.
