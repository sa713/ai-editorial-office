# Orchestration Plan

## task summary

- Task ID: `GLOBAL_RESEARCH_INTELLIGENT_PRODUCTION_SYSTEMS`
- User goal: conduct global critical research and create Knowledge Base AI Software Studio v1.
- Deliverable: research artifacts plus independent permanent KB directory.
- Audience/channel: internal Studio roles and future research/governance work.
- Current active version: v1 working artifact set.

## task classification

- Task type: high-governance research and reusable knowledge extraction.
- Risk mode: `high-governance`
- Factual sensitivity: high; claims concern engineering, AI, product, quality, governance, and source-backed methods.
- Human approval likely required: no for local artifact creation; yes for later policy adoption or publication.
- Rationale: the task uses external factual claims, source evaluation, and long-lived KB artifacts.

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: source-heavy, cross-domain, high factual sensitivity, and long-term reuse.
- Forbidden depth shortcuts: no source-light summary, no unsupported claims, no finalization without review.
- Expanded profile trigger, if any: active by default due to high-governance scope.

## selected pipeline

- Pipeline: `/pipelines/research_pipeline.md`
- Why this pipeline: the primary work is evidence collection, critical comparison, and reusable knowledge extraction.
- Pipeline exceptions or local constraints: downstream `writer_agent` may produce requested research deliverables and KB records after research sufficiency; review and finalization remain mandatory.

## client profile

- Client profile: `none`
- Client profile status: `not_applicable`
- Activation reason: n/a
- Non-activation reason, if considered and rejected: the work is not Sber-owned and does not request Sber redpolicy.
- Client-profile files: none
- Stop condition: activate no client profile unless user explicitly changes scope.

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

- Rationale: user supplied extensive scope, constraints, and acceptance criteria; missing details can be safely handled by marking KB v1 as non-exhaustive.
- Production may start: yes
- If `ask`: n/a
- If `constrain`: v1 source corpus is public and source-backed; no audit or Studio redesign.
- If `block`: n/a

## editorial decision frame

- Chosen editorial route: research corpus -> evidence artifacts -> atomic KB records -> extraction report -> review -> final delivery.
- Why this route serves the task: it separates research from writing while producing reusable knowledge instead of a literature essay.
- Alternatives considered:
  - Write one long analytical report.
    - Rejected because the user requested atomic reusable KB knowledge, not a literature review.
  - Create only KB records without research artifacts.
    - Rejected because high-governance source traceability and extraction rationale are required.
  - Audit the current Studio against the research.
    - Rejected because the user explicitly forbids auditing or proposing Studio changes in this task.
- Writer/UX Writer contract:
  - Result type: structured research deliverables and KB v1 records.
  - Angle or reader path: reusable production-system knowledge for future Studio roles.
  - Scope boundary: general global research only; no current Studio evaluation.
  - Must include: source annotations, patterns, anti-patterns, contradictions, freshness policy, and relationships.
  - Must not include: Studio audit, BRD, audit framework design, or Codex tasks.
  - Source boundary and confidence: use checked public sources and clearly label limitations.
- Review focus: coverage, source quality, atomicity of KB records, required fields, contradictions, no forbidden Studio audit content.
- Reroute triggers: material source contradiction, insufficient evidence, user changes scope, or KB records cannot be made traceable.

## custom workflow mini-contract

- Deviation: permanent KB artifacts are created under `/kb/ai-software-studio-knowledge-base/` while task research artifacts remain under `/tasks/GLOBAL_RESEARCH_INTELLIGENT_PRODUCTION_SYSTEMS/`.
- Reason: user requested Knowledge Base as a standalone long-term Studio artifact; `AGENTS.md` assigns global reusable knowledge to `/kb`.
- Owner: `chief_editor`
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `chief_editor` | yes | User request is sufficiently complete. |
| Research | `research_agent` | yes | Full evidence mode. |
| Writing/UX writing | `writer_agent` | yes | Produce structured research deliverables and KB records from evidence. |
| Review | `review_agent` | yes | `review.md` required. |
| Finalization | `final_editor` | yes | Create `final.md` after approved review. |
| Final governance | `chief_editor` | yes | Create `final_decision.md`. |

## required knowledge and evidence

- Required KB: `/kb/research_evidence.md`, `/kb/task_statuses.md` as needed.
- Required source/evidence files: public sources listed in `sources.md`; user brief in `brief.md`.
- Evidence gaps: none blocking at preflight; emerging gaps must be marked in research artifacts.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | all roles | Current state and restart pointer. |
| `brief.md` | required | all roles | Normalized scope and constraints. |
| `research.md` | required | writer, reviewer | Research synthesis and contradictions. |
| `sources.md` | required | writer, reviewer | Source traceability. |
| `facts.md` | required | writer, reviewer | Fact-level extraction. |
| `claims_table.md` | required | writer, reviewer | Claim-level validation. |
| requested research artifacts | required | user, reviewer | Explicit user deliverables. |
| KB directory | required | future Studio roles | Permanent knowledge asset. |
| `claims-used.md` | required | reviewer | Trace final claims to evidence. |
| `review.md` | required before finalization | Chief Editor / Final Editor | Review gate. |
| `review-summary.md` | omitted | n/a | `review.md` will include enough summary. |
| `qa-checklist.md` | omitted | n/a | Checklist embedded in `review.md`. |
| `open-questions.md` | conditional | Chief Editor | Create only if real blocking questions appear. |
| `finalization-notes.md` | conditional | Chief Editor | Create only if review requires controlled final changes. |
| `finalization-checklist.md` | omitted unless review requires it | Chief Editor | Not needed if `review.md`, `final.md`, and manifest suffice. |

## structure-before-writing plan

- Reader path: overview -> map -> source register -> durable principles -> practices/patterns -> anti-patterns -> atomic KB -> extraction report.
- Section roles: each file has a distinct consumer and avoids duplicating the KB records.
- Required structure: atomic IDs, source IDs, relationships, confidence, freshness.
- Duplication risks: long report sections copying KB entries; mitigate by summarizing and linking.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | user request, AGENTS, pipeline | brief, manifest, status, plan, handoff | task routed to research |
| 2 | `research_agent` | plan, sources | research, sources, facts, claims table | research sufficient for writing |
| 3 | `writer_agent` | evidence artifacts | requested research deliverables, KB v1, claims-used | draft artifacts ready for review |
| 4 | `review_agent` | brief, evidence, KB, deliverables | review.md | approved or bounded repair requested |
| 5 | `final_editor` | approved review | final.md and any needed notes | finalization complete |
| 6 | `chief_editor` | final.md, review.md | final_decision.md | task governance complete |

## status transitions

- Starting status: `intake`
- Next expected status: `research`
- Status owner: `chief_editor`, then current stage owner
- Status update trigger: role transition, artifact completion, review outcome, final decision.

## review requirements

- Review artifact: `review.md`
- Review depth: high-governance deterministic review with embedded checklist.
- Reviewer independence requirement: review by `review_agent`, not `writer_agent`.
- Claims/evidence checks required: yes; source and claim traceability must be checked.
- Optional review artifacts justified: no; `review.md` is sufficient unless a blocker appears.

## human approval requirements

- Required: no for local artifact creation.
- Approval owner: user for later adoption, publication, or policy changes.
- Evidence needed: explicit user decision in a later task.
- Cannot proceed past: no publication/adoption as Studio policy in this task.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Source corpus cannot be exhaustive | KB may miss niche practices | `research_agent` | Mark v1 scope and further research areas. |
| AI-agent practices change rapidly | Some entries stale quickly | `writer_agent` | Freshness policy per entry. |
| Research turns into Studio audit | Violates user constraint | all roles | Explicitly exclude current Studio evaluation. |
| Long artifacts become hard to reuse | KB loses atomicity | `writer_agent` | One record per knowledge entity. |
| Metrics become prescriptive targets | Gaming risk | `review_agent` | Capture metric anti-patterns and limitations. |

## unresolved questions

- None blocking.

## escalation conditions

- Stop or escalate if sources conflict on material claims, critical sources cannot be accessed, or the task scope shifts toward Studio audit/design.

## completion criteria

- Required artifacts complete: research deliverables, evidence files, KB v1, review, final, final decision.
- Review outcome acceptable: `approved`.
- Blockers resolved: yes.
- Governance fields complete: manifest/status/final decision updated.

## finalization conditions

- Finalization may start when: `review.md` outcome is `approved`.
- Finalization must stop when: review is missing, non-independent, or requests changes.
- Compact finalization shape allowed: no, because task is high-governance.
- Conditional finalization artifacts needed: only if final editor makes controlled changes after review.

## restart notes

- Minimum read set: `AGENTS.md`, `task-manifest.md`, latest handoff, current artifact, `/pipelines/research_pipeline.md`.
- Current active version: v1.
- Deprecated/previous versions: none.
- Latest relevant handoff: `handoff-orchestration-chief-editor-to-research-agent.md`.
- Directly relevant pipeline/KB: `/pipelines/research_pipeline.md`, `/kb/research_evidence.md`.

