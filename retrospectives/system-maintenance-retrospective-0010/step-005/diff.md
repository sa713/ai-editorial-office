# Step 5 Diff Summary

The local repository exposes project files as untracked, so tracked `git diff`
does not provide a reliable baseline. This file records the semantic diff
applied in Step 5.

## Global Execution Profile

`ai-editorial-office/AGENTS.md`

```diff
+ Added `Execution profiles` section.
+ Defined `compact` as an official bounded operating mode.
+ Defined `expanded` as the profile required when compact safety conditions fail.
+ Stated compact execution is not a new pipeline, workflow, agent, status model,
+ automation, or governance model.
+ Stated compact execution is not lower quality, weaker review, skipped evidence,
+ skipped review, skipped governance, or minimalism at any cost.
+ Added non-automatic exclusions and expansion triggers.
+ Added compact finalization shape.
```

## Handoff And Finalization

`AGENTS.md`
`article_pipeline.md`
`social_pipeline.md`
`ux_writing_pipeline.md`
`review_pipeline.md`

```diff
- Finalization handoff and finalization proof wording could read as always
- requiring a fixed support-artifact bundle.
+ Compact finalization may rely on approved `review.md`, `final.md`, current
+ `task-manifest.md`, and optional short handoff only if needed.
+ Conditional notes/checklists remain required when high-governance, downstream,
+ blocker, task-specific, or traceability needs exist.
+ Finalization and governance gates still require approved review and
+ artifact-backed final decision.
```

## Templates

`orchestration_plan_template.md`
`task_manifest_template.md`
`final_decision_template.md`

```diff
+ Added explicit execution-profile fields.
+ Added expanded-profile trigger field to orchestration plan.
+ Added compact finalization shape fields to manifest and final decision.
+ Preserved risk mode, process depth, review required, human approval, and final
+ decision fields.
```

## Explicit Non-Changes

```diff
  No new pipeline.
  No new agent.
  No automation.
  No Step 6 work.
  No governance model change.
  Review remains mandatory.
  High-governance remains expanded/full-depth.
```
