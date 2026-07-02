This is a task-local analysis packet for P1. It does not contain real task
materials.

# P1 Case Comparison

## Cases Found

Case 1: `ai-editorial-office/tests/end_to_end_cases/access_pass_security_task/`

Case 2: `ai-editorial-office/tests/end_to_end_cases/cybersecurity_toolkit_feedback/`

Case 3: `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task/`

The case reports are real repository artifacts under
`ai-editorial-office/tests/end_to_end_cases/`. They are synthetic/sanitized
E2E cases, not real task folders.

## Files Used

- `ai-editorial-office/tests/README.md`
- `ai-editorial-office/tests/end_to_end_cases/access_pass_security_task/brief.md`
- `ai-editorial-office/tests/end_to_end_cases/access_pass_security_task/case_report.md`
- `ai-editorial-office/tests/end_to_end_cases/access_pass_security_task/orchestration_plan.md`
- `ai-editorial-office/tests/end_to_end_cases/access_pass_security_task/review.md`
- `ai-editorial-office/tests/end_to_end_cases/access_pass_security_task/task-manifest.md`
- `ai-editorial-office/tests/end_to_end_cases/access_pass_security_task/task_pack_writer.md`
- `ai-editorial-office/tests/end_to_end_cases/access_pass_security_task/task_pack_review_agent.md`
- `ai-editorial-office/tests/end_to_end_cases/cybersecurity_toolkit_feedback/brief.md`
- `ai-editorial-office/tests/end_to_end_cases/cybersecurity_toolkit_feedback/case_report.md`
- `ai-editorial-office/tests/end_to_end_cases/cybersecurity_toolkit_feedback/orchestration_plan.md`
- `ai-editorial-office/tests/end_to_end_cases/cybersecurity_toolkit_feedback/review.md`
- `ai-editorial-office/tests/end_to_end_cases/cybersecurity_toolkit_feedback/task-manifest.md`
- `ai-editorial-office/tests/end_to_end_cases/cybersecurity_toolkit_feedback/task_pack_writer.md`
- `ai-editorial-office/tests/end_to_end_cases/cybersecurity_toolkit_feedback/task_pack_review_agent.md`
- `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task/brief.md`
- `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task/case_report.md`
- `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task/orchestration_plan.md`
- `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task/review.md`
- `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task/source_summary.md`
- `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task/task-manifest.md`
- `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task/task_pack_writer.md`
- `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task/task_pack_review_agent.md`
- `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task/final_decision.md`

## Side-by-Side Comparison

| Dimension | Case 1: access pass security | Case 2: toolkit feedback | Case 3: system thinking course |
| --- | --- | --- | --- |
| Task type | Internal task/post wording for sanctioned test-pass security testing | Internal task/post wording for expert feedback on MVP toolkit | Internal task/post wording for source-based course-development task |
| Routing | `social`, compact, `constrain` | `social`, compact, `proceed` | `social`, compact with source summary, `constrain` |
| Source status | Sanitized raw brief only; no external source import | Sanitized raw brief only; no external source import or source notes | Task-local supplied source; original source not committed; sanitized `source_summary.md` used |
| Evidence mode | `no-research` | `no-research` | `compact-evidence` |
| Compact execution | Worked; complete lifecycle and review-gated finalization | Worked; complete lifecycle and review-gated finalization | Worked with one extra evidence artifact: `source_summary.md` |
| Task pack/context selection | Writer and review packs passed; both warned about missing handoff | Writer and review packs passed; both warned about missing handoff | Writer and review packs passed; both warned about missing handoff, but did not include `source_summary.md` |
| Review-gate | Preserved; `final.md` only after approved `review.md` | Preserved; `final.md` only after approved `review.md` | Preserved; `final.md` only after approved `review.md` |
| Finalization | Approved sanitized final task/post | Approved sanitized final task/post | Approved sanitized final task/post; source boundary recorded in final decision |
| Successful decision | `constrain` converted risky exploit-like wording into sanctioned internal testing | `proceed` was correct because the raw brief was sufficient and safe | `constrain` prevented invented course content while allowing a source-bound task |
| Main problem | Non-blocking missing handoff warning | Non-blocking missing handoff warning | Non-blocking missing handoff warning; missing `source_summary.md` in task packs |

## One-Off Observations

- Case 1 keeps both `draft.md` and `final.md` even when review requests no
  changes. This is slightly extra, but useful because the case tests
  review-gate sequencing.
- Case 3 depends on an attached source that is not committed. This is a
  source-bound scenario, not a problem by itself; `source_summary.md` preserves
  safe provenance.

## Repeated Patterns

Repeated successful patterns:

- Compact execution worked in all three cases.
- Review-gated finalization worked in all three cases.
- Task packs were useful as read-set checks for writer and review roles.
- Source/provenance stayed clean: no unsafe source import happened.
- `proceed` and `constrain` were applied differently and appropriately.

Repeated problem pattern:

- Task pack generator warns about missing handoff files in all three compact
  cases. This is repeated but non-blocking. It should be treated as compact
  case convention noise for now, not as a system fix.

Actionable narrow issue:

- In the source-based compact-evidence case, the writer and review task packs
  did not include `source_summary.md`, even though the case explicitly uses it
  as the task-local evidence artifact. This is not a broad routing failure, but
  it is the clearest small fix candidate and matches the existing P5 concern.

## Decision

`fix needed`

One small system fix is needed for P5/task pack generator follow-up:

```text
When a compact-evidence or source-based task declares a task-local evidence
summary such as source_summary.md, source_notes.md, or an equivalent source
artifact, task pack generator should include it in writer and review_agent read
sets.
```

No broader refactor is justified. Do not add roles, pipelines, mandatory
artifacts, validators, or review-gate changes for P1.
