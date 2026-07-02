# Orchestration Plan

## task summary

Task ID: `TASK-0002`

Task title: `AI tools getting in the way of team work`

Requested output: article draft, after downstream stages

Audience: `unknown`

Primary goal: Explain why AI tools can start interfering with teams instead of helping, without alarmism or hype.

Quality bar: calm, practical, source-aware article; no invented claims, examples, audience, or publication context.

Current task status: `writing`

Brief source: `/tasks/TASK-0002/brief.md`

Current status source: `/tasks/TASK-0002/status.md`

Last updated by: `chief_editor`

## post-research planning update

Updated at: `2026-05-18 02:15:15 MSK`

Decision: proceed to constrained writing without asking the user now.

Why clarification is not required before drafting:

- The user requested an article and supplied a clear tone constraint.
- Research provides enough safe claim boundaries for a cautious first draft.
- Audience, publication channel, exact length, and real examples can be constrained without pretending they are known.

Constrained writing scope:

- Russian-language draft.
- General professional readers who work in or with teams; no narrower audience assumption.
- Publication channel unknown; do not imply internal/external/official publication.
- Generic hypothetical workflow scenarios only.
- No internal examples, vendor claims, legal/compliance/security/HR claims, or broad numeric productivity claims.
- Use only allowed or caveated claims from `claims_table.md`; blocked claims are forbidden.

## decisions

| Decision | Outcome | Rationale |
| --- | --- | --- |
| Task type | `article` | User explicitly requested "статья"; Article Pipeline fits explanatory editorial work. |
| Pipeline | `/pipelines/article_pipeline.md` with `/pipelines/research_pipeline.md` upstream | The article is likely to use factual or causal claims about AI tools and team workflows. |
| Risk mode | `standard` | Normal article task with material factual sensitivity; `low-risk` is not justified while publication, audience, examples, and factual scope are unresolved. `high-governance` is not triggered yet because no external publication, internal claims, numeric claims, legal/compliance/security/HR claims, vendor claims, or required human approval were specified. |
| Clarification before production | Required before writing, not before research | Research can map safe claim boundaries and options without selecting audience or inventing examples. Writing would need unresolved choices to be settled or explicitly constrained. |
| Research before writing | `yes` | Direct writing would require unsupported causal claims or generic examples without evidence guidance. |
| Direct writing now | `no` | Audience, publication scope, example type, and claim boundaries remain unresolved. |

## selected pipeline

Pipeline file: `/pipelines/article_pipeline.md`

Upstream research context: `/pipelines/research_pipeline.md`

Pipeline constraints:

- Research is separate from writing.
- Writer must use only the brief, orchestration plan, approved KB context, research artifacts, and latest handoff.
- Review is mandatory before finalization.
- Finalization is not governance approval.
- Publication or delivery approval must not be inferred.

Pipeline conflicts: none identified.

## required agents

| Stage | Required agent | Agent spec | Responsibility | Handoff required |
| --- | --- | --- | --- | --- |
| intake | `intake_agent` | `/agents/intake_agent.md` | normalize raw task package | done |
| orchestration | `chief_editor` | `/agents/chief_editor.md` | select pipeline, risk mode, next route, artifact scope | done |
| research | `research_agent` | `/agents/research_agent.md` | create evidence base and claim-use guidance | yes |
| planning after research | `chief_editor` | `/agents/chief_editor.md` | decide whether research is sufficient and whether clarification is needed before writing | yes |
| writing | `writer_agent` | `/agents/writer_agent.md` | create outline, draft, writer notes, claims-used if claims are used | yes |
| review | `review_agent` | `/agents/review_agent.md` | independent review | yes |
| finalization | `final_editor` | `/agents/final_editor.md` | controlled finalization after approved review | yes |
| final governance | `chief_editor` | `/agents/chief_editor.md` | final decision without implying publication approval | yes |

## required KB

| KB file | Required for | Loaded before stage | Notes |
| --- | --- | --- | --- |
| `/kb/task_statuses.md` | status governance | orchestration | loaded |
| `/kb/editorial_policy.md` | factual discipline and artifact minimalism | orchestration | loaded |
| `/kb/tone_of_voice.md` | writing and review tone | orchestration/writing | loaded for orchestration; writer should reread before drafting |
| `/kb/forbidden_patterns.md` | quality and anti-hype checks | review or writing | load before writing/review if assigned |

## artifact scope

| Artifact | Class | Owner | Stage | Status | Rationale |
| --- | --- | --- | --- | --- | --- |
| `/tasks/TASK-0002/brief.md` | required | `intake_agent` | intake | present | Source of task intent and uncertainty. |
| `/tasks/TASK-0002/task-manifest.md` | required | current owner | all | updated | Compact state and restart anchor. |
| `/tasks/TASK-0002/status.md` | required | current owner | all | updated | Detailed status/history. |
| `/tasks/TASK-0002/orchestration_plan.md` | required | `chief_editor` | orchestration | present | Execution contract. |
| `/tasks/TASK-0002/open-questions.md` | required | current owner | intake onward | present | Tracks uncertainties; no duplicate question artifact needed. |
| `/tasks/TASK-0002/research.md` | required | `research_agent` | research | present | Separates facts, interpretations, assumptions, risks, and gaps. |
| `/tasks/TASK-0002/sources.md` | required | `research_agent` | research | present | Source traceability. |
| `/tasks/TASK-0002/facts.md` | required | `research_agent` | research | present | Reusable factual base. |
| `/tasks/TASK-0002/claims_table.md` | required | `research_agent` | research | present | Marks allowed, caveated, and blocked claims. |
| `/tasks/TASK-0002/planning-notes.md` | required | `chief_editor` | planning | present | Records constrained-writing decision. |
| `/tasks/TASK-0002/outline.md` | required now | `writer_agent` | writing | missing | Required for article drafting. |
| `/tasks/TASK-0002/draft.md` | required now | `writer_agent` | writing | missing | Required for article drafting. |
| `/tasks/TASK-0002/writer-notes.md` | required now | `writer_agent` | writing | missing | Required to record assumptions and caveats. |
| `/tasks/TASK-0002/claims-used.md` | required now | `writer_agent` | writing | missing | Required because factual claims are expected. |
| `/tasks/TASK-0002/review.md` | required before finalization | `review_agent` | review | not_applicable now | Review gate preserved; not created early. |
| `/tasks/TASK-0002/qa-checklist.md` | conditional | `review_agent` | review | not_applicable now | Standard mode likely requires separate checklist at review. |
| `/tasks/TASK-0002/review-summary.md` | conditional | `review_agent` | review | not_applicable now | Create if needed for concise transfer. |
| `/tasks/TASK-0002/final.md` | conditional | `final_editor` | finalization | not_applicable now | Only after approved review. |
| `/tasks/TASK-0002/finalization-notes.md` | conditional | `final_editor` | finalization | not_applicable now | Create if controlled changes or risks need recording. |
| `/tasks/TASK-0002/final_decision.md` | conditional | `chief_editor` | governance | not_applicable now | Only after finalization. |

No `context-summary.md` is needed: `task-manifest.md`, `status.md`, `brief.md`, `open-questions.md`, this plan, and handoff are sufficient restart anchors.

## research assignment

Status after orchestration: `research`

Next role: `research_agent`

Research scope:

- Map the main evidence-backed ways AI tools may interfere with team workflows.
- Separate verified claims, interpretations, assumptions, generic scenarios, unsupported claims, and open questions.
- Identify safe generic workflow example patterns without presenting invented scenarios as real cases.
- Flag claims that would require stronger evidence, user-supplied internal context, or human approval.
- Avoid numeric productivity claims unless strongly sourced and marked with limits.
- Avoid vendor-specific, internal-practice, legal/compliance/security/HR, or policy claims unless evidence supports them and risk is escalated.

Expected research outputs:

- `/tasks/TASK-0002/research.md`;
- `/tasks/TASK-0002/sources.md`;
- `/tasks/TASK-0002/facts.md`;
- `/tasks/TASK-0002/claims_table.md`;
- updated `/tasks/TASK-0002/open-questions.md`, if research changes blocking/deferred questions;
- updated `/tasks/TASK-0002/task-manifest.md`;
- updated `/tasks/TASK-0002/status.md`;
- research handoff to `chief_editor`, not directly to `writer_agent`, unless the plan is updated.

## uncertainty handling

No longer blocks constrained writing:

- exact audience, because writing is constrained to general professional readers;
- publication channel, because the draft must not imply a channel or approval;
- real examples, because only generic hypothetical scenarios are allowed;
- exact length, because Writer Agent may choose a practical draft length and note the assumption.

Still blocks later stages or scope expansion:

- finalization/publication approval;
- official internal/external publication scope;
- real organization-specific examples;
- vendor, legal, compliance, security, HR, policy, or broad numeric productivity claims.

Writer must not resolve these by invention.

## planned transitions

| From | To | Trigger | Responsible role | Required artifact |
| --- | --- | --- | --- | --- |
| `intake` | `research` | Article Pipeline confirmed; research required before safe writing | `chief_editor` | `orchestration_plan.md`, `handoff-orchestration-chief-editor-to-next-role.md`, `status.md` |
| `research` | `planning` | Research scope completed or needs routing decision | `research_agent` recommends; `chief_editor` records | research artifacts and research handoff |
| `planning` | `writing` | Chief Editor confirms research sufficiency and resolves or safely constrains writing blockers | `chief_editor` | updated plan/status and handoff to `writer_agent` |
| `writing` | `review` | Writer creates required writing artifacts | `writer_agent` | `outline.md`, `draft.md`, `writer-notes.md`, `claims-used.md` if needed, handoff |
| `review` | `approved` or `changes_requested` or `blocked` | Independent review verdict | `review_agent` | `review.md` and required review artifacts |

## review and governance requirements

Independent review required: `yes`

Reviewer: `review_agent`

Review must check:

- compliance with brief, orchestration plan, and Article Pipeline;
- no invented facts, examples, sources, audience, or publication context;
- factual traceability through research and claims-used artifacts;
- caveats for uncertain claims;
- role separation and review-gate integrity;
- whether unresolved audience/publication questions block approval or finalization.

Human approval required: `unknown`

Human approval must be reassessed before finalization or publication if the article becomes external-facing, uses internal examples, makes sensitive claims, or review requests a human decision.

## risk controls

| Risk | Severity | Stage affected | Mitigation | Owner |
| --- | --- | --- | --- | --- |
| Unsupported causal claims about AI tools harming teams | medium | research/writing/review | Require claim table and caveats; block unsupported claims from draft. | `research_agent`, then `writer_agent` |
| Invented workflow examples | medium | writing/review | Allow only generic hypothetical scenarios clearly marked, or sourced/supplied examples. | `writer_agent` |
| Silent audience or publication assumption | medium | planning/writing/finalization | Chief Editor must resolve, ask, or constrain before writing/finalization. | `chief_editor` |
| Bureaucracy drift | medium | all | Use only listed artifacts; no speculative notes or placeholder files. | current owner |

## completion condition for this orchestration stage

Orchestration is complete when:

- Article Pipeline and upstream Research Pipeline are recorded;
- `standard` risk mode is confirmed;
- task status is moved to `research`;
- next role is `research_agent`;
- no writing, review, finalization, or governance artifacts are created.
