# Handoff

- From: `final_editor`
- To: `chief_editor`
- Reason: the independently approved Release Candidate has a compact final
  deliverable pointer and is ready for final governance

## Delta

- Created `final.md` without changing reviewed implementation meaning.
- Preserved S5.R1 `Review`, pending Project Lead acceptance, S5.R2
  `Not Started`, no push, and all user exclusions.

## Next action

- Chief Editor verifies `review.md`, completes `final_decision.md`, updates
  final status/validation fields, stages only authorized files, runs all
  required checks including `git diff --cached --check`, and commits locally.
- Do not record Project Lead acceptance, start S5.R2, push, or include
  `diff_intake.md`.
