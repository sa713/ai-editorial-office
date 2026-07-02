# MVP replacement decisions

## Core model

`AGENTS.md` now defines the replacement model directly:

- Core roles are the primary production roles for ordinary text tasks.
- Extension roles are additional roles outside the core role set.
- Unauthorized extension roles are roles not explicitly legalized by `AGENTS.md`, or legalized extension roles used outside their bounded scope.
- Current operating model is the active lifecycle, status, handoff, artifact, review-gate, governance, and role-assignment system.

## Role decisions

- The core role list was not changed.
- No role was added.
- No role was removed.
- Artist Agent remains a legalized extension role.
- Artist Agent remains bounded to illustration-to-text work with approved `visual_concept.md` and `illustration_brief.md`.
- Future style/editor/fact-check roles remain future extensions and are not current core roles.

## Governance decisions

- Chief Editor still selects pipeline, assigns valid roles, maintains `orchestration_plan.md`, `task-manifest.md`, and `status.md`.
- Governance wording now says Chief Editor assigns core roles or explicitly legalized extension roles only when their conditions apply.
- No final governance decision rule changed.
- Human approval semantics were not changed.

## Pipeline decisions

- Pipeline role-admissibility language now says core roles are used by default.
- Legalized extension roles remain assignable only under `AGENTS.md` conditions and only within bounded scope.
- Unauthorized extension roles are blocked/escalated.
- Handoff validity checks now refer to core roles or explicitly legalized extension roles.
- Production and review sequences were renamed from old terminology to default sequences without changing order.

## Review and status decisions

- Direct `writing` -> `review` remains valid after required artifacts and handoff.
- Direct `ux-writing` -> `review` remains valid under the same UX conditions.
- `editing` remains optional only as a revision checkpoint/status bridge.
- No separate Editor Agent was introduced.
- Review-gate behavior was not changed.

## Artifact decisions

- `edited.md`, `editor-notes.md`, and `revision-requests.md` are now described as not required production artifacts.
- Their future optional status remains unchanged.
- No artifact requirement was added or removed.

## Wording choices

- `MVP agent set` became `core role set`.
- `MVP agents` / `MVP roles` became `core roles` where role admissibility was meant.
- `non-MVP extension roles` became `unauthorized extension roles` where a ban/escalation was meant.
- `MVP default workflow` and sequence headings became default operating/production/review wording.
- `valid in MVP` became valid in the current operating model.
