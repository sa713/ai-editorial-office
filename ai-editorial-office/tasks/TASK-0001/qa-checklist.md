# QA Checklist

Task ID: `TASK-0001`

Owner: `review_agent`

Review outcome: `approved`

| Checklist item | Status | Evidence | Notes |
| --- | --- | --- | --- |
| Review readiness gate | `pass` | `draft.md`; `handoff-writing-writer-agent-to-review-agent.md`; `status.md` | Draft and latest handoff exist; current status is `review`. |
| Reviewer independence | `pass` | `draft.md` owner is `writer_agent`; review artifacts owned by `review_agent` | Review Agent did not write or rewrite the draft. |
| Required artifact completeness | `pass` | `status.md` artifact list; task folder file list | All required research and writing artifacts are present. |
| Brief compliance | `pass` | `brief.md`; `draft.md` | Draft addresses editors, UX writers, and product teams; internal-portal tone is practical. |
| Article Pipeline compliance | `pass` | `article_pipeline.md`; `orchestration_plan.md`; `status.md` | Research, writing, and review remain separate; finalization not started. |
| Review Pipeline compliance | `pass` | `review_pipeline.md`; this checklist; `review.md` | Review outcome is explicit and mapped to operational status. |
| Factual traceability | `pass` | `claims-used.md`; `claims_table.md`; `facts.md`; `research.md` | Material factual claims are traceable. |
| Caveated claims preserved | `pass` | `claims-used.md`; `draft.md` | C1, C3, C4, and C7 remain caveated. |
| Blocked claims excluded | `pass` | `claims-used.md`; `draft.md`; `claims_table.md` | C8, C9, C10, and C11 are not used as factual claims. |
| Unsupported productivity claims | `pass` | `draft.md` lines 17, 36 | No numeric or absolute productivity claims; draft explicitly avoids guaranteed time savings. |
| Replacement rhetoric | `pass` | `draft.md` lines 13, 29 | Draft says AI is not a replacement and keeps responsibility with humans. |
| No invented internal practices | `pass` | `draft.md`; `writer-notes.md`; `claims-used.md` | Examples are generic and do not claim internal practice. |
| Tone of voice | `pass` | `tone_of_voice.md`; `draft.md` | Calm, practical, direct, non-hype. |
| Forbidden patterns | `pass` | `forbidden_patterns.md`; `draft.md` | No generic AI opening, clickbait certainty, or corporate motivational filler found. |
| UX writing constraints | `pass` | `ux_writing_guidelines.md`; `draft.md` line 21 | UX examples remind reader to verify product state and avoid unsupported behavior. |
| Glossary consistency | `pass` | `glossary.md`; task artifacts | Terms such as draft, review, finalization, traceability are used consistently. |
| Role boundaries | `pass` | `AGENTS.md`; `status.md`; review artifacts | Review Agent did not create `final.md`, `final_decision.md`, or rewrite draft. |
| Governance discipline | `pass` | `status.md`; `review.md` | Review outcome maps to `approved`; finalization must be performed by `final_editor`. |
| Status consistency | `pass` | `status.md`; `task_statuses.md`; `article_pipeline.md` | Current status `review` is valid and can map to `approved`. Prior direct `writing` -> `review` is noted as a non-blocking process note. |
| Human approval requirement | `not_applicable` | `open-questions.md`; `orchestration_plan.md` | Human approval is unknown and belongs to later final governance, not current review approval. |
| Final artifacts absent before finalization | `pass` | task folder file list | `final.md`, `final_decision.md`, and `approval.md` are absent. |
