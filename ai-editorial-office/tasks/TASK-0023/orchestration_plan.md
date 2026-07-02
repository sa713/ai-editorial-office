# Orchestration Plan

## task summary

- Task ID: TASK-0023
- User goal: prepare a raw interview transcript for publication.
- Deliverable: `analysis.md`, `final.md`, `review.md`.
- Audience/channel: assumed internal/publication-style readers interested in a vivid professional-personal portrait.
- Current active version: `source-transcript.md`

## task classification

- Task type: interview adaptation / editorial article
- Risk mode: standard
- Factual sensitivity: low to medium; source is the interview itself, not external factual research.
- Human approval likely required: no
- Rationale: the task is about faithful literary editing of provided source material, not external claims research.

## process depth

- Depth: compact
- Execution profile: compact
- Rationale: source is self-contained, user explicitly asks for editorial transformation and three deliverables.
- Forbidden depth shortcuts: no final material without review; no Q&A invention; no external facts added.
- Expanded profile trigger, if any: unresolved factual contradiction, missing source section, or review finding requiring major rewrite.

## selected pipeline

- Pipeline: `article_pipeline.md`
- Why this pipeline: the output is a publishable article/interview text requiring structure, writing, review, and finalization.
- Pipeline exceptions or local constraints: separate research artifacts are omitted because the source interview is sufficient and no external evidence is needed.

## custom workflow mini-contract

- Deviation: use `analysis.md` as both user-required analysis and compact writer-facing editorial rationale.
- Reason: the user explicitly requested `analysis.md`; duplicating the same content in extra research artifacts would not improve quality.
- Owner: chief_editor / writer_agent
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | intake_agent / chief_editor | yes | Normalize request into `brief.md` |
| Research | research_agent | no | Source-contained interview; no external research |
| Writing | writer_agent | yes | Prepare analysis, outline, and draft |
| Review | review_agent | yes | `review.md` required before finalization |
| Finalization | final_editor | yes | Produce `final.md` after review |
| Final governance | chief_editor | compact | Record readiness in status/review |

## required knowledge and evidence

- Required KB: none beyond `AGENTS.md` and `article_pipeline.md`.
- Required source/evidence files: `source-transcript.md`.
- Evidence gaps: none blocking.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | all roles | Restart anchor |
| `brief.md` | required | all roles | Normalized task |
| `status.md` | required | all roles | Status and review state |
| `analysis.md` | required | user / writer / reviewer | Format and editorial decisions |
| `outline.md` | required | writer / reviewer | Structure-before-writing |
| `draft.md` | required | reviewer / final editor | Review target |
| `review.md` | required | Chief Editor / Final Editor | Independent review gate |
| `final.md` | required | user | Publication-ready deliverable |
| `review-summary.md` | omitted | none | `review.md` is sufficient |
| `qa-checklist.md` | omitted | none | Checklist embedded in `review.md` |
| `finalization-notes.md` | omitted | none | Compact finalization is enough |

## structure-before-writing plan

- Reader path: role in УЭК -> route into profession -> work style and team -> hobbies/travel/home -> values and final punchline.
- Section roles: keep lively portrait sections; use subheads as navigation rather than artificial questions.
- Required structure: interview-article in first person with editor's compact lead.
- Duplication risks: repeated self-irony about chaos/rest/travel; repeated team warmth; long oral paragraphs.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | user request, AGENTS, pipeline | brief, manifest, plan, status | route recorded |
| 2 | writer_agent | source transcript | analysis, outline, draft | draft preserves voice and improves readability |
| 3 | review_agent | draft, source | review | approved or changes requested |
| 4 | final_editor | approved review, draft | final | final aligns with review |
| 5 | chief_editor | final, review | status update | task ready |

## status transitions

- Starting status: intake
- Next expected status: writing
- Status owner: chief_editor, then writer_agent
- Status update trigger: stage transitions and review outcome

## review requirements

- Review artifact: `review.md`
- Review depth: compact but source-aware
- Reviewer independence requirement: reviewer checks draft against source and user constraints after writing
- Claims/evidence checks required: source fidelity and no invented claims
- Optional review artifacts justified: no

## human approval requirements

- Required: no
- Approval owner: not applicable
- Evidence needed: not applicable
- Cannot proceed past: finalization may proceed after approved review

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Over-polishing | Loss of voice | writer/reviewer | Preserve first-person jokes and characteristic turns |
| Under-editing | Reads like transcript | writer | Rebuild rhythm and section flow |
| Artificial Q&A | Invented interviewer voice | writer | Use interview-article format |
| Context opacity | Readers may not know УЭК acronyms | writer | Add light editorial lead without overexplaining |

## unresolved questions

- None blocking.

## escalation conditions

- Stop or escalate if source meaning is unclear in a way that affects publication claims.

## completion criteria

- Required artifacts complete: `analysis.md`, `draft.md`, `review.md`, `final.md`
- Review outcome acceptable: approved
- Blockers resolved: yes
- Governance fields complete: status updated

## finalization conditions

- Finalization may start when: `review.md` approves `draft.md`.
- Finalization must stop when: review requests changes or finds source distortion.
- Compact finalization shape allowed: yes; user requested three concise deliverables and no separate approval workflow.
- Conditional finalization artifacts needed: no.

## restart notes

- Minimum read set: `brief.md`, `task-manifest.md`, `orchestration_plan.md`, `status.md`, `source-transcript.md`.
- Current active version: `source-transcript.md`.
- Deprecated/previous versions: none.
- Latest relevant handoff: none yet.
- Directly relevant pipeline/KB: `article_pipeline.md`.
