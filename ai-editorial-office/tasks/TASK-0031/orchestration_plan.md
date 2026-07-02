# Orchestration Plan

## task summary

- Task ID: TASK-0031
- User goal: convert the Sber editorial policy PDF into a faithful Markdown
  text source.
- Deliverable: `sber-editorial-policy.md` plus conversion notes, review, and
  status update.
- Audience/channel: task-local Markdown source for later use as text.
- Current active version: source PDF `Редакционная политика 05.2026.pdf`.

## task classification

- Task type: technical source conversion / external-source transcription
- Risk mode: `standard`
- Factual sensitivity: high for transcription fidelity; low for interpretation
  because no analysis or policy adoption is requested.
- Human approval likely required: no
- Rationale: the output must preserve an external source exactly enough for
  downstream use, while avoiding any change to AI-editorial-office rules.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: one source PDF, one target Markdown file, clear acceptance
  criteria, and no new editorial judgment needed.
- Forbidden depth shortcuts: silent PDF-to-Markdown without editorial routing;
  paraphrase; summary; `/kb` ingestion; skipping review.
- Expanded profile trigger, if any: unreadable pages, multiple candidate PDFs,
  OCR uncertainty, complex tables that cannot be verified textually.

## selected pipeline

- Pipeline: compact custom workflow mini-contract
- Why this pipeline: existing pipelines are heavier than needed for a technical
  conversion, but AGENTS requires routing, role assignment, preflight, status,
  and review.
- Pipeline exceptions or local constraints: no visual branch; no research
  branch; no governance change.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | `confirmed` |
| Channel or context | `confirmed` |
| Deliverable | `defined` |
| Source boundary | `defined` |
| Success criterion | `defined` |
| Approval boundary | `defined` |
| Missing data strategy | `proceed` |

- Rationale: the user identified the task folder, source type, output path,
  forbidden actions, conversion method boundaries, and review criteria. Exactly
  one candidate PDF is present.
- Production may start: yes
- If `ask`: not applicable
- If `constrain`: not applicable
- If `block`: not applicable

## custom workflow mini-contract

- Deviation: use a technical conversion path rather than research/writing
  production.
- Reason: the task asks for faithful transfer of an existing source, not new
  editorial material.
- Owner: chief_editor
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake/routing | Chief Editor | yes | Route task, confirm source boundary, run preflight. |
| Research | omitted | no | No new research; source is the PDF only. |
| Writing/technical transfer | Writer Agent | yes | Produce Markdown without paraphrase or new claims. |
| Review | Review Agent | yes | Check completeness, order, tables/lists/examples/notes, and extraction cleanup. |
| Finalization | Final Editor | conditional | Only if review requests bounded formatting fixes after conversion. |
| Final governance | Chief Editor | yes | Update status after review. |

## required knowledge and evidence

- Required KB: none.
- Required source/evidence files: `Редакционная политика 05.2026.pdf`.
- Evidence gaps: none known.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | Writer Agent / Review Agent | Holds task-local conversion contract. |
| `task-manifest.md` | required | all roles | Restart pointer and current state. |
| `orchestration_plan.md` | required | all roles | Compact execution contract. |
| `sber-editorial-policy.md` | required | user / downstream readers | Converted source text. |
| `conversion_notes.md` | required | reviewer / downstream readers | Method, cleanup, limitations. |
| `review.md` | required | Chief Editor | Review-gate evidence. |
| `status.md` | required | all roles | Lifecycle status and blockers. |
| `finalization-notes.md` | omitted | n/a | Not needed unless review requests bounded finalization fixes. |
| `qa-checklist.md` | omitted | n/a | Review artifact covers required checks. |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| Route | Chief Editor | user request, AGENTS, project state, task folder | manifest, plan, status | Preflight decision is `proceed`. |
| Extract | Writer Agent | source PDF | extracted text / page metadata | All pages have extractable text or OCR fallback decision is recorded. |
| Convert | Writer Agent | extracted text | `sber-editorial-policy.md`, `conversion_notes.md` | Markdown preserves wording, structure, tables/lists/examples/notes as far as technically possible. |
| Review | Review Agent | PDF, Markdown, notes | `review.md` | Completeness and non-paraphrase checks are complete. |
| Close | Chief Editor | review, artifacts | updated `status.md` | No blockers remain. |

## status transitions

- Starting status: writing
- Next expected status: review, then finalized if review passes
- Status owner: Chief Editor
- Status update trigger: conversion created, review completed, blocker found, or
  task completed.

## review requirements

- Review artifact: `review.md`
- Review depth: full-page coverage check plus structural/content spot checks.
- Reviewer independence requirement: Review Agent must verify the converted
  artifact against extraction/page metadata and not rewrite the document.
- Claims/evidence checks required: no new claims; no paraphrase; no source
  adoption into `/kb`.
- Optional review artifacts justified: no.

## human approval requirements

- Required: no
- Approval owner: not applicable
- Evidence needed: not applicable
- Cannot proceed past: review-gate if conversion is incomplete or blocked.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Hidden OCR/image-only pages | Missing content | Writer Agent | Check extraction coverage and record OCR decision. |
| Complex tables lose structure | Reduced usability | Writer Agent / Review Agent | Prefer Markdown tables; otherwise readable text plus note. |
| PDF extraction artifacts remain | Noisy output | Writer Agent | Technical cleanup and review. |
| Source policy treated as system rule | Governance breach | Chief Editor | Keep source task-local and out of `/kb`. |

## unresolved questions

- None.

## escalation conditions

- Stop or escalate if the PDF cannot be extracted reliably, page coverage cannot
  be verified, or a conversion choice would require semantic rewriting.

## completion criteria

- Required artifacts complete: yes.
- Review outcome acceptable: `approved`.
- Blockers resolved: yes.
- Governance fields complete: source remains external and task-local.

## finalization conditions

- Finalization may start when: `sber-editorial-policy.md` and
  `conversion_notes.md` exist and `review.md` is approved.
- Finalization must stop when: review is `blocked` or `changes_requested`.
- Compact finalization shape allowed: yes, because this is a technical transfer.
- Conditional finalization artifacts needed: no.

## restart notes

- Minimum read set: `AGENTS.md`, `project-state.md`, `brief.md`,
  `task-manifest.md`, `orchestration_plan.md`, `status.md`, current conversion
  artifacts.
- Current active version: `Редакционная политика 05.2026.pdf`.
- Deprecated/previous versions: none.
- Latest relevant handoff: none.
- Directly relevant pipeline/KB: none.
