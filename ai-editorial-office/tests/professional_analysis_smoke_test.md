# Professional Analysis Smoke Test

Status: manual smoke-test / synthetic examples only.

Purpose: check whether Professional Analysis activates only when analytical
product quality is material and remains inactive for ordinary summaries,
copyediting, Architecture Review, and Engineering Review.

This file is not a canonical rule owner. Canonical guidance lives in
`/kb/professional_analysis.md`.

## Expected Classification Labels

- `activate`: Professional Analysis should be selected.
- `do_not_activate`: Professional Analysis should not be selected.
- `activate_with_other_capability`: Professional Analysis should be selected
  and another capability should also be considered.

## Cases

| Case | Scenario | Expected | Lenses |
| --- | --- | --- | --- |
| PA-01 | A Project Lead asks for a decision brief comparing three roadmap release options. | `activate` | options and recommendation; executive decision brief |
| PA-02 | A task asks for synthesis of stakeholder notes into product opportunities and risks. | `activate` | synthesis brief; product discovery analysis |
| PA-03 | A policy memo needs impacts, tradeoffs, assumptions, and a recommended path. | `activate` | policy or impact analysis; options and recommendation |
| PA-04 | A technology assessment compares adopting a future AI evaluation tool against the current process. | `activate_with_other_capability` | technology assessment; options and recommendation; Architecture Review or Engineering Review if system shape or implementation safety is material |
| PA-05 | A research summary only lists facts from one source and no decision or recommendation is requested. | `do_not_activate` | none |
| PA-06 | A writer edits tone and clarity in an already approved draft. | `do_not_activate` | none |
| PA-07 | A system change alters lifecycle or canonical ownership. | `activate_with_other_capability` | situation assessment or options and recommendation only if a decision brief is needed; Architecture Review owns design fitness |
| PA-08 | Codex changes a validator script and reports tests. | `do_not_activate` | none; Engineering Review owns change safety |
| PA-09 | A user asks for a recommendation but available evidence supports only caveated findings. | `activate` | options and recommendation; executive decision brief with constrained recommendation or no-recommendation rationale |
| PA-10 | A task asks for a product discovery note before implementation. | `activate` | product discovery analysis; business or needs analysis |

## Pass Criteria

- Positive cases select only relevant lenses.
- Negative cases do not activate Professional Analysis.
- Architecture-sensitive cases also consider Architecture Review.
- Implementation-sensitive cases route change-safety concerns to Engineering
  Review.
- Recommendations stay within evidence confidence and expose uncertainty.
- No case creates a new role, pipeline, lifecycle stage, review gate,
  consulting framework, or mandatory artifact.
