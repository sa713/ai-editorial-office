# Handoff: Review Agent to Final Editor

## Transfer

- From role: `review_agent`
- To role: `final_editor`
- Status: `approved`
- Review outcome: `approved`
- Reason: complete S5.R2 change set passed independent high-governance review
  with no critical or non-critical issues.

## Approved finalization scope

- Update release report/pack status from review-pending to internally approved
  and Release Candidate ready.
- Change validation wording only as supported by the approved review and final
  checks.
- Create `final.md` as the final deliverable pointer and summary.
- Preserve state as S5.R2 `Review`, Project Lead acceptance pending.
- Preserve all evidence limitations, optionality, qualitative judgments,
  existing-owner boundaries, and explicit non-decisions.

## Do not change

- Canonical signal contract or architecture synthesis.
- Scenario logic or research claims.
- Role, pipeline, lifecycle, gate, owner, capability, or task-object shape.
- S5.R2 to `Done`, Project Lead verdict, or S5.R3 state.
- Root `diff_intake.md` or legacy archive.

## Remaining validation

After finalization, Chief Editor must run final diff, memory, lifecycle,
task-pack, direct task, and staged-diff checks before committing.

## Escalate if

Finalization would change meaning, evidence confidence, architecture, Project
Lead authority, or any reviewed boundary.
