# Handoff — Research Agent to Writer Agent

- Task: `TASK-PRODUCT-INTENT-REVIEW-STEP2`
- From: `research_agent`
- To: `writer_agent` with implementation capabilities
- Date: 2026-07-29

## approved implementation design

- Extend existing TNR; do not create a classifier.
- Preserve separate advisory recommendation and Chief Editor decision.
- Store full routing state in orchestration and only restart-critical
  `limited`/`full` state in manifest.
- Parse explicit decision labels in generator; never parse request keywords.
- Load `kb/product_intent_review.md` only for `limited`/`full`.
- Add manual recommendation scenarios and executable generator/restart tests.

## authorized surface

- Task Need Recognition and task-object canon.
- Intake and Chief Editor role contracts plus required `/about` copies.
- Orchestration and manifest templates.
- Minimal task-pack generator change.
- Related fixtures, shell/manual smoke tests, and test documentation.
- Step 2 task reports.
