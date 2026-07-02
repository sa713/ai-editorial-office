# Artifact Depth Decisions

## Primary Decision

For low-risk and simple standard tasks, the primary review artifact is one `review.md`.

`review.md` remains mandatory before finalization. It must carry:

- verdict;
- reviewed scope;
- reviewer independence check;
- findings or pass rationale;
- blockers or open questions;
- next action.

## Conditional Support Artifacts

These artifacts are conditional, not default:

- `review-summary.md`;
- `qa-checklist.md`;
- `finalization-checklist.md`;
- `open-questions.md`;
- `finalization-notes.md`.

Create them only when at least one condition is true:

- there is an explicit downstream consumer;
- high-governance mode applies;
- the task separately requires the artifact;
- there are real open questions, blockers, unresolved risks, or deferred decisions;
- there is a traceability need that cannot be safely carried inside the primary artifact.

## Compact Handoff

`compact-handoff.md` is not created automatically.

It is only for:

- final/user-facing transfer of the result;
- explicit context transfer when `task-manifest.md`, `status.md`, and ordinary handoff files are not enough.

It is not a role-to-role handoff and must not replace `handoff-*.md`.

## Legacy Folders

Legacy task folders are history, not templates.

The heavier artifact structures in folders such as `TASK-0009` and `TASK-0010` must not be copied into new work only because they exist. Current risk mode, selected pipeline, downstream needs, and artifact minimalism decide artifact depth.

## High-Governance Preservation

High-governance work still requires full traceability where needed:

- review remains mandatory;
- claim/source/fact artifacts remain required when sensitivity or claims require them;
- final governance remains with Chief Editor;
- human approval remains explicit when required;
- optional artifacts become mandatory only when a real governance, traceability, blocker, or downstream need exists.
