# Finalization Handoff

## transfer

- From role: `final_editor`
- To role: `chief_editor`
- Reason: the independently approved package has been finalized without
  semantic change.
- Current state pointer: `task-manifest.md`.

## delta

- Added `final.md` as the controlled pointer to the approved S5.R5 package.
- Preserved the Round 1 CR-01 repair and Round 2 approval history.
- Changed no contract, evidence, architecture, scenario, release, state, or
  memory semantic.

## chief editor actions

- Verify finalization against `review.md` and the Release Pack.
- Create `final_decision.md` for Release Candidate readiness only.
- Move release-level S5.R5 from `In Progress` to `Review`; do not use `Done`.
- Refresh state and mapped memory exact copy, then run the complete final
  validation set.
- Stage only the authorized S5.R5 scope, commit locally, and do not push.

## constraints

- Project Lead acceptance remains pending.
- Stage 5 remains active and no future stage starts.
- Preserve `diff_intake.md` and do not touch the legacy redaction path.
