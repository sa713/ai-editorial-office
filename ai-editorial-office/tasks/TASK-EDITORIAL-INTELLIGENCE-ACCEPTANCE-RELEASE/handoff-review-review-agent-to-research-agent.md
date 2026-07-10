# Review Repair Handoff

## transfer

- From role: `review_agent`
- To role: `research_agent`
- Outcome: `changes_requested`
- Current state pointer: `task-manifest.md`.

## blocking issue

CR-01: `claims_table.md` lacks `Factual sensitivity` and `Allowed downstream
use` for C01-C17 under the selected high-governance Research Pipeline.

## bounded repair

- Add the two fields and explicit row values only.
- Preserve claim wording, status, evidence, confidence, review-use notes, and
  every release/contract semantic.
- Do not change any template, report, Release Pack, scenario, state/memory,
  accepted release, role, pipeline, lifecycle, capability, pack, or validator.

## return condition

Return the repaired claim table plus current manifest/status/handoff pointers
to the same Review Agent for the exact re-review in `review.md`.
