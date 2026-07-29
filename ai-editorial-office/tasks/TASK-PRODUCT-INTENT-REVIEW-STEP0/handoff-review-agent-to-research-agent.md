# Handoff

## metadata

- Task ID: `TASK-PRODUCT-INTENT-REVIEW-STEP0`
- From role: `review_agent`
- To role: `research_agent`
- Date: 2026-07-29
- Current status: `research`
- Risk mode: `standard`
- Process depth: `full`
- Current active version: bounded F1/F2 repair

## reason for handoff

- Review repair.

## delta summary

- Review outcome: `changes_requested`.
- F1: make the open Professional Analysis release-candidate and no-future-stage
  governance dependency explicit.
- F2: satisfy the selected Research Pipeline contract with a compact evidence
  index.

## active constraints for next role

- Do not alter the core architecture recommendation.
- Do not add implementation.
- Do not expand review scope beyond F1/F2 and task-state consistency.

## next action

- Required next role action: update the two named reports, create `research.md`,
  align plan/manifest/status, and hand only that scope back to Review Agent.
- Expected output: bounded repair ready for re-review.
- What not to change: responsibility map unless the repair invalidates it.

## validation before proceeding

- Check `project-state.md` wording.
- Check that `research.md` is a process artifact and not a fourth selected
  deliverable.
- Run scoped `git diff --check`.
