# Sources

## coverage

Audit date: 2026-06-04.

The audit inspected the task folders available under
`ai-editorial-office/tasks/` before `TASK-0024` was created.

Scope counted:

- 25 `TASK-*` folders: `TASK-0001` through `TASK-0023`, including `TASK-0003B`
  and `TASK-0004B`.
- Supporting evidence from `SYSTEM-MAINTENANCE-*` folders was used only to
  understand why some current safeguards exist.
- Binary source files, extracted images, generated media, and spreadsheets were
  not evaluated for content quality unless their task-local markdown artifacts
  described system behavior.

## artifact coverage snapshot

| Metric | Count | Notes |
| --- | ---: | --- |
| Total pre-audit `TASK-*` folders inspected | 25 | Excludes `TASK-0024` |
| Tasks with `brief.md` | 13 | Stronger in mature tasks |
| Tasks with `task-manifest.md` | 13 | Becomes normal after early runs |
| Tasks with `status.md` | 14 | Some early/direct tasks lack lifecycle state |
| Tasks with `orchestration_plan.md` | 14 | Mature tasks route explicitly |
| Tasks with review artifact | 15 | Includes less formal `review-v2.md` style in `TASK-0009` |
| Tasks with final decision artifact | 14 | Most mature tasks separate editorial readiness from publication approval |
| Tasks without review | 10 | Mostly direct/sparse or visual precursor tasks: `TASK-0010` to `TASK-0019` except none reviewed |
| Full formal cycle | 11 | `TASK-0003`, `TASK-0003B`, `TASK-0004`, `TASK-0004B`, `TASK-0005`, `TASK-0006`, `TASK-0007`, `TASK-0008`, `TASK-0021`, `TASK-0022`, `TASK-0023` |

## primary evidence sample

| Task | Evidence used | Behavioral relevance |
| --- | --- | --- |
| `TASK-0001` | `brief.md`, `orchestration_plan.md`, `research.md`, `claims_table.md`, `review.md`, `review-summary.md`, `final_decision.md` | First full lifecycle validation; shows strong research/review discipline and heavy artifact depth. |
| `TASK-0002` | `brief.md`, `research.md`, `orchestration_plan.md`, `review.md`, `retrospective.md` | Best evidence for incomplete intake handled safely: unknown audience/channel preserved, research used before writing, review catches unsupported certainty. |
| `TASK-0003` | `brief.md`, `orchestration_plan.md`, `draft.md`, `review.md`, `review-summary.md`, `final_decision.md` | Social pipeline with variant selection; later follow-up shows first choice was editorially plausible but too synthetic for user taste. |
| `TASK-0003B` | `brief.md`, `orchestration_plan.md`, `review.md`, `review-summary.md`, `final_decision.md` | Strong evidence that user feedback and bounded experimentation improve tone and anti-genericity. |
| `TASK-0004` | `brief.md`, `orchestration_plan.md`, `review.md`, `qa-checklist.md`, `final_decision.md` | Operational instruction revision; review catches answer delay, sequence ambiguity, ownership, and unsupported terms. |
| `TASK-0004B` | `brief.md`, `orchestration_plan.md`, `review.md`, `comparison-with-task-0004.md` | Evidence that structure-before-writing improved selective reading, role paths, and repetition. |
| `TASK-0005` | `brief.md`, `orchestration_plan.md`, `writer-notes.md`, `review.md`, `qa-checklist.md`, `final_decision.md` | Good source-boundary task; turns abstract HR-like source into concrete orientation material. |
| `TASK-0006` | `brief.md`, `orchestration_plan.md`, `writer-notes.md`, `review.md`, `qa-checklist.md`, `final_decision.md` | Launch communication with canonical task-local sources; shows channel differentiation and publication-boundary discipline. |
| `TASK-0007` | `brief.md`, `orchestration_plan.md`, `writer-notes.md`, `review.md`, `review-summary.md`, `final_decision.md` | Reusable editorial guide; shows high value of reader-state and platform-specific opening patterns. |
| `TASK-0008` | `brief.md`, `diagnosis.md`, `audience-analysis.md`, `communication-failures.md`, `rewrite-strategy.md`, `review.md`, `final_decision.md` | Strongest evidence that the system can diagnose communication architecture, not only rewrite text. |
| `TASK-0009` | `editorial_diagnosis.md`, `communication_strategy.md`, `review.md`, `review-v2.md`, `final_decision.md`, `final-decision-v2.md` | Strong editorial work but weaker formal lifecycle; useful transition evidence. |
| `TASK-0010` | `recommendations.md`, `recommendations-v4.md`, `comparison-review-v3.md` | Evidence for readiness logic and premature transition risk, but lacks full task scaffolding. |
| `TASK-0011` to `TASK-0019` | Sparse task-local files, visual summaries, direct outputs | Evidence of direct-production mode and inconsistent editorial entry before current governance normalized it. |
| `TASK-0020` | `orchestration_plan.md`, `visual_concept.md`, `sketchnote_brief.md`, `image_prompt.md`, `review.md`, `final_decision.md` | Mature visual-branch example with semantic frame, brief, prompt, and review. |
| `TASK-0021` | `brief.md`, `orchestration_plan.md`, handoffs, `review.md`, `final_decision.md` | Compact mature task; shows artifact minimalism and useful embedded checklist. |
| `TASK-0022` | `brief.md`, `source-snapshot.md`, `orchestration_plan.md`, `review.md`, `final_decision.md` | Compact source-boundary rewrite; good protection against adding commitments. |
| `TASK-0023` | `brief.md`, `analysis.md`, `orchestration_plan.md`, `review.md`, `final_decision.md` | Interview adaptation; good source-contained routing, weaker review framing because review is titled as self-check. |

## supporting system-evolution evidence

| Task | Evidence used | Why it matters |
| --- | --- | --- |
| `SYSTEM-MAINTENANCE-0001` | `final_decision.md`, `status.md` | Added relevance, replaceability, and release-specific angle pressure after social copy risk. |
| `SYSTEM-MAINTENANCE-0002` | `final_decision.md`, `status.md` | Added instructional architecture checks: reading path, section roles, duplication, selective reading. |
| `SYSTEM-MAINTENANCE-0003` | `final_decision.md`, `status.md` | Compressed review-system redundancy; evidence that artifact/policy bloat was recognized. |
| `SYSTEM-MAINTENANCE-0004` | `final_decision.md`, `status.md` | Added structure-before-writing pressure, later validated by `TASK-0004B`. |
| `SYSTEM-MAINTENANCE-0016` | `normalized-brief-contract-decisions.md`, `safety-check.md` | Added distinction between confirmed, inferred, and unknown brief context. |
| `SYSTEM-MAINTENANCE-0018` | `structure-cleanup-report.md` | Shows project had accumulated structural noise and task-location ambiguity. |

## limitations

- The audit uses saved task-local artifacts, not chat history.
- Frequency labels are approximate behavioral frequencies over the inspected
  corpus, not statistical measurements.
- Older direct tasks are useful evidence of historical behavior, but they should
  not be treated as representative of the current mature process.
- The audit evaluates system behavior, not the publishable quality of individual
  final texts.
