# Research Repair Handoff

## transfer

- From role: `research_agent`
- To role: `review_agent`
- Reason: CR-01 bounded repair is complete.
- Current state pointer: `task-manifest.md`.

## repair delta

- Added `Factual sensitivity` and `Allowed downstream use` columns to
  `claims_table.md`.
- Added explicit values for C01-C17 consistent with each claim's status,
  confidence, evidence, repository scope, and existing claim limits.
- Added one claim-use note defining the `with caveat` boundary.
- Changed no claim wording, status, evidence, confidence, implementation,
  release, state/memory, scenario, owner, or validation semantics.

## requested re-review

Apply only the exact re-review scope in `review.md`: repaired rows, current
pointers/transitions, bounded changed scope, `git diff --check`, and direct task
lifecycle validation.
