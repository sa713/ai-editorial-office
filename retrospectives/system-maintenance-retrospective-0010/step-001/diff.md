# Step 1 Diff Summary

The local repository state exposes these project files as untracked, so `git diff` does not provide a reliable tracked baseline. This file records the semantic diff applied in Step 1.

## Global Artifact Rule

`ai-editorial-office/AGENTS.md`

```diff
+ For low-risk and simple standard tasks, the primary review artifact is one `review.md`.
+ `review-summary.md`, `qa-checklist.md`, `finalization-checklist.md`,
+ `open-questions.md`, and `finalization-notes.md` are conditional.
+ `compact-handoff.md` is not created automatically.
+ Legacy task folders are history, not templates.
```

## Orchestration Template

`ai-editorial-office/templates/artifacts/orchestration_plan_template.md`

```diff
+ Artifact scope must classify support artifacts as conditional unless justified.
+ Low-risk/simple standard review uses `review.md` as primary artifact.
+ Legacy task folders must not be copied into new plans as templates.
```

## Review Artifacts

Pipelines and review role specs now use:

```diff
- `qa-checklist.md` required for standard/high-governance review.
+ `qa-checklist.md` required only for high-governance, downstream consumer,
+ task-specific requirement, blocker/open-question state, or traceability need.

- `review-summary.md` required when concise transfer is useful.
+ `review-summary.md` created only when a separate concise transfer is consumed downstream.
```

## Finalization Artifacts

Pipelines and final editor specs now use:

```diff
- `finalization-checklist.md` required for standard/high-governance finalization.
+ `finalization-checklist.md` required only for high-governance,
+ downstream governance, task-specific requirement, or traceability proof need.

- `finalization-notes.md` expected after approved review when changes are applied.
+ `finalization-notes.md` created only for controlled changes, unresolved risks/blockers,
+ downstream governance, high-governance, task requirement, or traceability need.
```

## Open Questions

Research, intake, and task scaffolds now use:

```diff
- Create `open-questions.md`, even if it initially says `None`.
+ Create `open-questions.md` only when real questions, blockers,
+ deferred decisions, or traceability gaps exist.
```

## Compact Handoff

Chief Editor and global handoff policy now use:

```diff
- `compact-handoff.md` treated as a common closeout artifact.
+ `compact-handoff.md` is not automatic and is never role-to-role routing.
+ It is only for final/user-facing transfer or explicit context transfer need.
```
