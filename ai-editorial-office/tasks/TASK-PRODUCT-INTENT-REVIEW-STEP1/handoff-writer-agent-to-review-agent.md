# Handoff — Writer Agent to Review Agent

- Task: `TASK-PRODUCT-INTENT-REVIEW-STEP1`
- From: `writer_agent`
- To: `review_agent`
- Date: 2026-07-29

## review set

- `brief.md`
- `baseline-report.md`
- `../../kb/product_intent_review.md`
- `../../kb/capability_registry.md`
- `../../AGENTS.md`
- `../../kb/professional_analysis.md`
- `specification-report.md`
- `implementation-report.md`
- `change-summary.md`
- scoped canonical diff and validation evidence

## required review

Independently verify:

1. all twenty Step 1 acceptance criteria;
2. one sole full owner and no duplicated full contract;
3. multi-signal activation and explicit non-activation;
4. all seven model elements and four checks;
5. evidence, owner, finding/verdict, and adjacent-capability boundaries;
6. explicit Problem Hypothesis disposition;
7. unchanged Professional Analysis release status and `project-state.md`;
8. absence of new role, pipeline, stage, gate, status, review outcome, task
   object, mandatory artifact, runtime, production behavior, or Step 2 work;
9. current lifecycle, link, `/about`, and diff checks.

## producer assertion

No Review Agent verdict has been preselected. The reviewer must return
`approved`, `changes_requested`, or `blocked` through the existing gate.
