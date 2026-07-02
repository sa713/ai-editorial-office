# Add Sber client profile as an isolated task-scoped mode

## Summary

- Added `/kb/clients/sber` profile with usage rules, source notes, cleaned
  editorial policy, and review checklist.
- Added `client_profile` fields to task manifest and orchestration plan
  templates.
- Wired client profile loading into article, social, UX writing, and review
  pipelines.
- Updated intake, chief editor, writer, UX writer, review agent, and final
  editor role specs.
- Preserved `AGENTS.md` authority: Sber rules cannot bypass review, role
  separation, source discipline, or governance.
- Added and ran smoke tests for active Sber-owned tasks, non-activation for
  independent Sber mentions, `pending_source` fallback, and review-gate conflict.
- Verified `/about` memory package: 20 files and canonical copies match.

## What Changed

### New Sber Client Profile

Added the production profile directory:

```text
ai-editorial-office/kb/clients/sber/
```

Files:

- `README.md`
- `usage-rules.md`
- `editorial-policy.md`
- `source-notes.md`
- `sber-review-checklist.md`

The profile is explicitly task-scoped. It is used only when
`client_profile: sber` is recorded in `task-manifest.md` or
`orchestration_plan.md`.

The cleaned Sber editorial policy source is imported into:

```text
ai-editorial-office/kb/clients/sber/editorial-policy.md
```

The source provenance is recorded in:

```text
ai-editorial-office/kb/clients/sber/source-notes.md
```

### Governance and Memory Rules

Updated `AGENTS.md` to add client profiles as an isolated layer under:

```text
/kb/clients/CLIENT-ID/
```

The authority order preserves project governance:

- `AGENTS.md` and project-level governance stay above all client rules.
- Current user instruction stays below `AGENTS.md`.
- `brief.md` stays below user instruction.
- Selected pipeline and role specs stay above the active client profile.
- Active client profile applies only as task-specific content constraint and
  stays below workflow/governance rules.
- Active client profile can sit above general KB standards for client-specific
  tone, naming, and terminology.

Sber rules cannot cancel or weaken:

- review;
- role separation;
- lifecycle;
- factual verification;
- source discipline;
- safety;
- legal constraints;
- selected pipeline requirements.

Updated `/about` memory package so ChatGPT project memory reflects the new
client-profile layer without becoming canonical policy.

### Templates

Updated:

- `ai-editorial-office/templates/artifacts/task_manifest_template.md`
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`

New fields include:

- `Client profile: none / sber / unknown`
- `Client profile status: not_applicable / active / pending_source`
- `client_profile_files`
- `client_profile_activation_reason`
- `client_profile_source_status`
- `client_profile_stop_condition`

Both templates state that `sber` activates only for Sber-owned,
Sber-product, Sber-communication, or explicit Sber-redpolicy tasks, not for
independent materials where Sber is merely mentioned.

### Roles

Updated:

- `intake_agent`
- `chief_editor`
- `writer_agent`
- `ux_writer`
- `review_agent`
- `final_editor`

Behavior added:

- Intake may propose `client_profile` but cannot finally activate it.
- Chief Editor confirms, rejects, or blocks profile activation before
  production.
- Writer and UX Writer load active client-profile files only when the manifest
  or orchestration plan names them.
- Writer cannot claim client-policy compliance when `client_profile_status` is
  `pending_source` or the source rule has not been checked.
- Review Agent applies `/kb/clients/sber/sber-review-checklist.md` when
  `client_profile: sber` is active.
- Review Agent must not invent client-specific rules when source status is
  `pending_source`.
- Final Editor preserves active client-profile constraints and cannot add or
  preserve client-policy compliance claims unless review verified them against
  the active source.

### Pipelines

Updated:

- `ai-editorial-office/pipelines/article_pipeline.md`
- `ai-editorial-office/pipelines/social_pipeline.md`
- `ai-editorial-office/pipelines/ux_writing_pipeline.md`
- `ai-editorial-office/pipelines/review_pipeline.md`

Pipeline behavior:

- Active client-profile files are loaded only when `client_profile` is set.
- Sber profile is not loaded by default.
- Review Pipeline stops or requests changes if the manifest or orchestration
  plan names an active client profile but required checklist/source files are
  missing.

## Verification

Smoke tests covered:

- Sber-owned push gets `client_profile: sber`,
  `client_profile_status: active`, review required.
- Sber-owned UX gets `client_profile: sber`,
  `client_profile_status: active`, review required.
- Sber-owned post gets `client_profile: sber`,
  `client_profile_status: active`, review required.
- Independent article about Sber gets `client_profile: none`,
  `client_profile_status: not_applicable`.
- Independent comparison Sber vs competitor gets `client_profile: none`,
  `client_profile_status: not_applicable`, unless the task is explicitly
  Sber-owned.
- Mocked missing, stale, or unverified source gets `client_profile: sber`,
  `client_profile_status: pending_source`, and full Sber-policy compliance
  claims are forbidden.
- Request to skip review while `client_profile: sber` is treated as a conflict;
  `AGENTS.md` wins and review remains required.

Additional checks:

```text
./ai-editorial-office/scripts/check_about_memory_package.sh
```

Result:

```text
OK: /about has 20 files and copied files match canonical sources.
```

## Non-Goals

- Do not turn the Sber editorial policy into global AI Editorial Office policy.
- Do not apply Sber-mode to independent materials where Sber is just a topic,
  source, example, competitor, case, or analysis object.
- Do not invent Sber rules from memory, brand impressions, public pages, or old
  examples.
- Do not weaken review-gate.
- Do not add new roles.
- Do not change task lifecycle.
- Do not make `pending_source` a default blocker for the whole task:
  it blocks full Sber-policy compliance claims, while safe work may continue
  under general rules and explicit task constraints.

## Acceptance Criteria

- Sber profile exists under `ai-editorial-office/kb/clients/sber/`.
- Source status is active and provenance is recorded.
- Templates contain client-profile fields.
- Roles and pipelines mention active client profile where relevant.
- Sber-mode is not global.
- Non-activation rules are explicit.
- `pending_source` fallback is preserved.
- Review remains mandatory.
- Smoke tests pass.
- `/about` package remains valid.

## Final Status

Sber-mode update accepted and ready to merge.
