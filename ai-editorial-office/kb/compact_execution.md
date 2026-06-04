# Compact Execution

This is practical guidance for applying compact execution and artifact
minimalism. It does not override `AGENTS.md`, the selected pipeline, or
task-local governance artifacts.

## Purpose

Compact execution reduces service weight for simple tasks: fewer duplicated
notes, fewer placeholder files, and a shorter restart path. It is valid only
when the task remains reviewable, restartable, and traceable.

Compact execution is not a shortcut around review, evidence, governance, or
current-version discipline.

## Non-negotiables

Do not compress away:

- `brief.md` or a clearly normalized brief;
- `task-manifest.md`;
- `status.md`;
- selected pipeline and process-depth rationale;
- the current working artifact;
- `review.md` before any finalization;
- `final.md` when a final deliverable exists;
- `final_decision.md` for Chief Editor governance closure;
- review-gate independence and an explicit review outcome;
- a current-version pointer when multiple artifact versions exist.

If any of these are missing or stale, compact execution should stop until the
state is repaired or explicitly blocked.

## Risk Modes

### Low-risk task

Use the smallest safe task package:

- brief or normalized brief;
- current `task-manifest.md` and `status.md`;
- compact orchestration/process-depth rationale;
- one current working artifact;
- `review.md` with verdict, checked scope, independence check, and next action;
- `final.md` after approved review;
- `final_decision.md` after finalization;
- handoff only when the next role cannot recover delta context from the core
  files.

No research or claim artifacts are needed when the task has no factual,
product, policy, numeric, legal, financial, HR, security, regulatory, medical,
or reputational claims.

### Standard task

Use compact execution only for simple, source-light standard tasks. Keep the
core package above, then add only the artifacts the selected pipeline needs for
review: for example research notes, source pointers, claims used, UX state
notes, or a handoff when the next role needs delta context.

If review cannot validate the work from the compact package, expand the task.

### High-governance task

Do not over-compress. Use the expanded artifact set required by `AGENTS.md` and
the selected pipeline. High-governance tasks need explicit evidence, review
depth, human approval assessment when relevant, and a Chief Editor final
governance decision.

## Optional Artifacts

These files are conditional or optional. Do not create them automatically:

- `qa-checklist.md`;
- `review-summary.md`;
- `reviewer-notes.md`;
- `finalization-notes.md`;
- `finalization-checklist.md`;
- `open-questions.md`;
- `claims_table.md`;
- `sources.md`;
- `context-summary.md`;
- `compact-handoff.md`;
- handoff files beyond what is needed for role transfer or restart.

Create one only when it has a real consumer, blocker, governance need,
traceability need, explicit task requirement, or restartability purpose.

## Chief Editor Rationale

When Chief Editor chooses compact execution, record a short rationale in
`orchestration_plan.md`, `task-manifest.md`, or `status.md`:

- risk mode and why compact is safe;
- selected review target;
- artifacts intentionally omitted;
- why omitted artifacts are not needed for review, restart, or governance;
- trigger that would require switching to expanded execution.

The rationale should be brief. It should make the omission visible, not create
another long artifact.

## Review Agent Expectations

Review Agent should review the compact task against its approved scope, not
against an expanded artifact package by default.

For compact tasks, Review Agent checks:

- core required artifacts are present and current;
- reviewed artifact is clear;
- reviewer independence is explicit;
- skipped artifacts are justified by risk and scope;
- factual or product claims have enough evidence for the selected risk mode;
- finalization is not allowed without `review.md` outcome `approved`.

Review Agent should not require optional artifacts solely because they exist in
templates or legacy tasks. Missing optional artifacts become findings only when
their absence blocks review, traceability, restart, governance, or an explicit
task requirement.

## Examples

Compact: low-risk messenger post with no factual claims uses brief, manifest,
status, compact orchestration rationale, draft, review, final, and final
decision. `qa-checklist.md`, `sources.md`, and `review-summary.md` are omitted
with rationale.

Expanded: external communication with product behavior claims uses research,
sources, facts or claims table, claims-used, full review evidence, finalization
notes or checklist when needed, human approval assessment, and final decision.
