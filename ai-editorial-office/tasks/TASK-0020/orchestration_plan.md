# Orchestration Plan

## task summary

- Task ID: TASK-0020
- User goal: Prepare a visual summary of the article for blog publication.
- Deliverable: one horizontal PNG sketchnote-style visual article summary.
- Audience/channel: blog readers.
- Current active version: source PDF in `TASK-0020`.

## task classification

- Task type: visual_article_sketchnote
- Risk mode: `standard`
- Factual sensitivity: moderate; the source discusses enterprise AI security and security controls, so the visual must not invent claims.
- Human approval likely required: no for preparation; yes before external publication.
- Rationale: user requested a visual article summary, which `AGENTS.md` maps to `visual_article_sketchnote`.

## process depth

- Depth: `compact`
- Execution profile: `compact`
- Rationale: the task has one clear source file, one requested visual deliverable, and no multi-version conflict.
- Forbidden depth shortcuts: no direct PDF-to-image/HTML/SVG/MD production as a substitute for editorial routing; no final delivery without review.
- Expanded profile trigger, if any: unreadable PDF, contradictory source content, request for platform-specific design variants, or review finding requiring semantic revision.

## selected pipeline

- Pipeline: compact visual branch, mode `visual_article_sketchnote`
- Why this pipeline: the request is for a visual article sketchnote rather than an ordinary illustration, article rewrite, social post, or research report.
- Pipeline exceptions or local constraints: no separate full article pipeline; create only the artifacts required for safe visual production and review.

## custom workflow mini-contract

- Deviation: use compact visual path instead of a full article pipeline.
- Reason: output is a sketchnote image, not a new text article.
- Owner: chief_editor
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake / routing | chief_editor | yes | Select visual mode and keep task state aligned. |
| Source reading / semantic frame | research_agent | yes | Extract article meaning from source without creating final visual. |
| Brief writing | writer_agent | yes | Convert approved meaning into `visual_concept.md` and `sketchnote_brief.md`. |
| Visual execution | artist_agent | yes | Prepare `image_prompt.md` and PNG from approved brief. |
| Review | review_agent | yes | Review prompt/image against source and brief in `review.md`. |
| Final governance | chief_editor | if review passes | Record `final_decision.md`. |

## required knowledge and evidence

- Required KB: `kb/canonical_sketchnote_prompt.md`; active invariants from `AGENTS.md`.
- Required source/evidence files: `/ai-editorial-office/kb/sources/CSA_+_Zenity_Enterprise_AI_Security_Starts_with_AI_Agents.pdf`; extracted text may be used as a support artifact.
- Evidence gaps: none known before source extraction.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | all roles | Restart and current-state pointer. |
| `orchestration_plan.md` | required | all roles | Visual branch routing and boundaries. |
| `status.md` | required | all roles | State history and review readiness. |
| `article-source.txt` | conditional | research_agent / review_agent | Support source reading if PDF text extraction succeeds. |
| `visual_concept.md` | required | writer_agent / artist_agent / review_agent | Approved meaning frame. |
| `sketchnote_brief.md` | required | artist_agent / review_agent | Visual sketchnote assignment. |
| `image_prompt.md` | required | artist_agent / review_agent | Execution prompt and constraints. |
| `visual-conspect-blog.png` | required | user / review_agent | Final PNG deliverable. |
| `review.md` | required before finalization | chief_editor | Independent review gate. |
| `final_decision.md` | conditional | user / archive | Needed if review approves the final PNG. |

## structure-before-writing plan

- Reader path: central thesis -> agentic AI risk shift -> why legacy controls fail -> three-layer defensive model -> governance and operating takeaway.
- Section roles: summarize concepts visually, not rewrite article as text.
- Required structure: one-sheet sketchnote with 4-7 key thesis clusters, arrows, relationships, and short handwritten labels.
- Duplication risks: repeating vendor/product language or overloading the image with text.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | user request, AGENTS | routing artifacts | Visual branch activated and state recorded. |
| 2 | research_agent | source PDF | source understanding / optional `article-source.txt` | Main arguments and evidence are readable. |
| 3 | writer_agent | source understanding | `visual_concept.md`, `sketchnote_brief.md` | Brief contains central idea, key points, conclusions, layout, text rules. |
| 4 | artist_agent | approved visual artifacts and KB prompt | `image_prompt.md`, PNG | PNG exists and follows sketchnote mode. |
| 5 | review_agent | source, briefs, PNG | `review.md` | Verdict recorded. |
| 6 | chief_editor | review | `final_decision.md` if approved | Final readiness recorded. |

## status transitions

- Starting status: planning
- Next expected status: writing
- Status owner: chief_editor
- Status update trigger: each stage transition and review verdict.

## review requirements

- Review artifact: `review.md`
- Review depth: compact but source-aware.
- Reviewer independence requirement: reviewer must not be the same role as visual execution.
- Claims/evidence checks required: visual claims and handwritten phrases must be grounded in source/brief.
- Optional review artifacts justified: no.

## human approval requirements

- Required: no for preparation.
- Approval owner: user for actual blog publication.
- Evidence needed: explicit user approval only if asked to publish externally.
- Cannot proceed past: external publication.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Text extraction misses article nuance | Visual summary may distort source | research_agent | Use PDF text extraction and review against source. |
| Output becomes infographic/slide | Violates active visual mode | artist_agent / review_agent | Use canonical sketchnote prompt and review genre constraints. |
| Too much text in image | Blog visual becomes unreadable | artist_agent | Keep controlled short phrases only. |
| Invented security claims | Misleads readers | writer_agent / review_agent | Use only source-grounded claims. |

## unresolved questions

- None blocking.

## escalation conditions

- Stop or escalate if: PDF cannot be read; source and user goal conflict; requested output drifts into infographic/slide/poster; review blocks the deliverable.

## completion criteria

- Required artifacts complete: `visual_concept.md`, `sketchnote_brief.md`, `image_prompt.md`, `visual-conspect-blog.png`, `review.md`.
- Review outcome acceptable: `approved`.
- Blockers resolved: yes.
- Governance fields complete: yes.

## finalization conditions

- Finalization may start when: `review.md` approves `visual-conspect-blog.png`.
- Finalization must stop when: review requests changes or blocks on factual/genre issues.
- Compact finalization shape allowed: yes; final deliverable is a single PNG plus recorded decision.
- Conditional finalization artifacts needed: `final_decision.md` if approved.

## restart notes

- Minimum read set: `AGENTS.md`, `task-manifest.md`, `orchestration_plan.md`, `status.md`, current working artifact, `kb/canonical_sketchnote_prompt.md`.
- Current active version: source PDF and latest generated PNG in this task folder.
- Deprecated/previous versions: none.
- Latest relevant handoff: none yet.
- Directly relevant pipeline/KB: compact visual branch rules in `AGENTS.md`, `kb/canonical_sketchnote_prompt.md`.
