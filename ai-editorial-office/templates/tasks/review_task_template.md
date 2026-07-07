# Review Task Template

## template purpose

Use when the task is primarily independent review of an existing artifact or
artifact set. Review is never optional; `review.md` is the primary review
artifact.

## when to use

- A draft, research package, UX copy, finalization candidate, or governance
  packet needs independent validation.
- The task outcome is approval, changes requested, or blocked.
- Separate `qa-checklist.md` or `review-summary.md` is needed only for
  downstream, high-governance, task-specific, blocker, or traceability reasons.

## folder shape

```text
tasks/TASK-ID/
  brief.md
  task-manifest.md
  status.md
  reviewed-material.md
  review.md
```

Conditional files:

- `orchestration_plan.md`
- `qa-checklist.md`
- `review-summary.md`
- `reviewer-notes.md`
- `handoff-*.md`

## bootstrap steps

1. Identify artifact/version under review.
2. Create or update `task-manifest.md` with current-version pointer and
   `client_profile` fields when a client profile is active for the reviewed
   material.
3. Record review target and status.
4. Produce `review.md`.
5. Create optional review artifacts only when justified.

## brief.md scaffold

```markdown
# Brief

## review goal

## artifact under review

## expected standard

## audience or downstream consumer

## risk mode

## process depth

## constraints

## client profile

## evidence available

## success criteria
```

## reviewed material scaffold

```markdown
## reviewed material

- Artifact path:
- Version/currentness:
- Producer role:
- Known dependencies:
```

## review.md scaffold

```markdown
# Review

## review metadata

- Reviewer:
- Reviewed artifact/version:
- Review date:
- Risk mode:
- Process depth:

## reviewer independence

- Producer role:
- Reviewer role:
- Independence confirmed: yes/no

## validation summary

- Brief compliance:
- Evidence/claims validation:
- Tone/glossary/policy validation:
- Structure/usefulness validation:
- Governance validation:

## editorial challenge

- Decision under challenge:
- Chosen route remains valid while:
  - Assumption:
  - Assumption:
  - Assumption:
- Challenge conditions:
  - If ..., then ... route would become stronger.
  - If ..., then ... route would become stronger.
- Assumption check: `holds` / `partially_changed` / `changed`
- Evidence:
- Required action:

## findings

| Severity | Finding | Evidence | Required action | Owner |
| --- | --- | --- | --- | --- |

## blockers

- None / list blockers.

## required changes

- None / list bounded changes.

## review outcome

approved / changes_requested / blocked

## reviewer confidence

- High / medium / low:
- Reason:

## next action
```

## qa-checklist.md scaffold

Create only when separate checklist depth is justified.

```markdown
# QA Checklist

| Check | Pass/Fail/N/A | Evidence | Notes |
| --- | --- | --- | --- |
```

## review-summary.md scaffold

Create only when a downstream consumer needs a separate concise transfer.

```markdown
# Review Summary

## outcome

## biggest blockers or risks

## required next action
```

## reviewer-notes.md scaffold

Use only for reasoning that should remain separate from `review.md`.

```markdown
# Reviewer Notes

## detailed reasoning

## caveats

## borderline decisions
```

## handoff scaffold

Use `handoff_template.md`. Include outcome, repair owner, exact re-review scope,
blockers, and next action.

## completion check

- `review.md` exists.
- Reviewed artifact/version is current.
- Independence is recorded.
- Outcome is deterministic.
- Optional review artifacts are justified.
