# Orchestration Plan

## task summary

- Task ID: TASK-STUDIO-AUDIT-FRAMEWORK
- User goal: create a reusable Studio Audit Framework methodology for AI Software Studio.
- Deliverable: package of markdown documents defining audit methodology, criteria, maturity model, evidence rules, report rules, KB linkage, KB gaps, and first-audit guidance.
- Audience/channel: owner and future independent auditors of AI Software Studio; local markdown artifact package.
- Current active version: initial framework package in this task folder.

## task classification

- Task type: methodology / knowledge content
- Risk mode: high-governance
- Factual sensitivity: high, because criteria must be source-grounded and reusable for future governance.
- Human approval likely required: unknown
- Rationale: The methodology will shape future Studio audits. The user explicitly requires traceability to the Knowledge Base and forbids unsupported criteria.

## process depth

- Depth: full
- Execution profile: expanded
- Rationale: The task requires multi-document output, criterion-level traceability, explicit KB gaps, review, and reusable governance structure.
- Forbidden depth shortcuts: no direct writing before KB evidence mapping; no skipped review; no untraceable criteria; no current-Studio evaluation.
- Expanded profile trigger, if any: criterion-to-KB traceability and high-governance reuse.

## selected pipeline

- Pipeline: article_pipeline
- Why this pipeline: The output is article-like knowledge content with factual, methodological, and source-backed claims.
- Pipeline exceptions or local constraints: The final deliverable is a document package rather than a single article. Article pipeline role separation and review gate remain unchanged.

## client profile

- Client profile: none
- Client profile status: not_applicable
- Activation reason: none
- Non-activation reason, if considered and rejected: the task is independent Studio methodology, not Sber-owned communication or Sber policy writing.
- Client-profile files: none
- Stop condition: activate no client profile unless user explicitly changes task ownership/context.

## preflight gate

| Field | Decision |
| --- | --- |
| Audience | confirmed |
| Channel or context | confirmed |
| Deliverable | defined |
| Source boundary | defined |
| Success criterion | defined |
| Approval boundary | unclear |
| Missing data strategy | proceed |

- Rationale: The user defined the task, source boundary, constraints, and acceptance criteria. Human approval is not needed to draft the methodology, but may be needed after delivery.
- Production may start: yes, starting with research only.
- If `ask`: n/a
- If `constrain`: Framework must be based only on existing KB; gaps are recorded when KB is insufficient.
- If `block`: n/a

## editorial decision frame

- Chosen editorial route: KB-grounded audit methodology package.
- Why this route serves the task: It satisfies the user's request for a reusable method rather than a one-time audit, while preserving explicit evidence linkage.
- Alternatives considered, usually 2-3 compact options:
  - Alternative route, one line: Single long Framework document.
    - Why rejected, one line: It would make criterion traceability, reuse, and review harder.
  - Alternative route, one line: Audit report template only.
    - Why rejected, one line: The user requested full methodology, not only future report structure.
  - Alternative route, one line: Immediate Studio audit.
    - Why rejected, one line: Explicitly forbidden by the user.
- Writer/UX Writer contract:
  - Result type: Markdown document package.
  - Angle or reader path: auditor-first reference method, from principles and scope to criteria, scoring, evidence, reporting, gaps, and first-audit setup.
  - Scope boundary: methodology only; no evaluation of current Studio implementation.
  - Must include: required 10 deliverable categories, criterion rationale, KB references, applicability limits, maturity and severity models, evidence collection rules, audit report structure, KB gaps, first-audit recommendations.
  - Must not include: current audit findings, BRD, proposed Studio process changes, Codex tasks, unsupported criteria.
  - Source boundary and confidence: only local AI Software Studio Knowledge Base records; if insufficient, mark as gap.
- Review focus: traceability to KB, no accidental current-state audit, internal consistency of maturity/scoring/evidence/reporting models, required deliverable coverage.
- Reroute triggers: KB cannot support core criteria; output drifts into actual audit; criteria lack source linkage; review finds role/process violation.

## custom workflow mini-contract

- Deviation: Produce a multi-document package under Article Pipeline.
- Reason: User requested a reusable framework package rather than a single article.
- Owner: chief_editor
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | chief_editor | yes | User brief normalized directly because task is already detailed |
| Research | research_agent | yes | Build KB evidence map and gaps |
| Writing/UX writing | writer_agent | yes | Draft framework documents from approved research |
| Review | review_agent | yes | `review.md` required |
| Finalization | final_editor | yes | Produce final package/index after approved review |
| Final governance | chief_editor | yes | `final_decision.md` required |

## required knowledge and evidence

- Required KB: `/ai-editorial-office/kb/ai-software-studio-knowledge-base/`
- Required source/evidence files: KB index, schema, source register, lifecycle, coverage model, application model/register, studio object map, development recommendations, all relevant records.
- Evidence gaps: to be identified in `research.md` and Framework gap documents.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | User task and constraints |
| `task-manifest.md` | required | all roles | Restart and current state |
| `status.md` | required | all roles | Status history |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `sources.md` | required | writer/reviewer | KB source inventory |
| `research.md` | required | writer/reviewer | Evidence synthesis and gaps |
| `claims_table.md` | required | writer/reviewer | Criterion traceability |
| `facts.md` | conditional | writer/reviewer | Create if fact extraction cannot fit in research/claims table |
| Framework documents | required | reviewer/finalizer/user | Main deliverable |
| `review.md` | required before finalization | Chief Editor / Final Editor | Independent review gate |
| `review-summary.md` | omitted unless needed | Chief Editor / Final Editor | Not needed if `review.md` is complete |
| `qa-checklist.md` | omitted unless needed | Review Agent | Embed checklist in `review.md` unless review becomes too large |
| `open-questions.md` | conditional | Chief Editor | Only if real blockers or deferred questions appear |
| `finalization-notes.md` | conditional | Chief Editor | Needed only if finalization changes are non-trivial |
| `finalization-checklist.md` | omitted unless needed | Chief Editor | Not expected if final package is clear |
| `final_decision.md` | required | user/governance | Final readiness |

## structure-before-writing plan

- Reader path: Why Framework exists -> how it is structured -> what it checks -> how criteria are scored -> how evidence is collected -> how report is formed -> how KB links and gaps are managed -> how first audit should be prepared.
- Section roles: Separate methodology, criteria catalog, scoring, evidence, report template, KB traceability, gaps, and first-audit guidance.
- Required structure: standalone package index plus dedicated documents for major concerns.
- Duplication risks: criteria rationale vs KB linkage; maturity model vs scoring rules; first-audit guidance vs process-change recommendations. Keep cross-references instead of repeated rules.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | user request, AGENTS.md | brief, manifest, status, orchestration | route recorded |
| 2 | research_agent | KB and orchestration | sources, research, claims table | evidence sufficient or gaps named |
| 3 | chief_editor | research artifacts | refreshed orchestration/status if needed | writing can start |
| 4 | writer_agent | brief, research, claims table | framework document package, outline/notes | package ready for review |
| 5 | review_agent | framework package and evidence | review.md | approved/changes_requested/blocked |
| 6 | writer_agent/research_agent | review findings if any | repaired documents | re-review ready |
| 7 | final_editor | approved review and package | final.md | final package index ready |
| 8 | chief_editor | final package and review | final_decision.md | final governance recorded |

## status transitions

- Starting status: planning
- Next expected status: research
- Status owner: chief_editor then research_agent
- Status update trigger: research assignment, research completion, writing start, review outcome, finalization, final decision

## review requirements

- Review artifact: `review.md`
- Review depth: full methodology review.
- Reviewer independence requirement: Reviewer must not be the same role instance as Writer Agent production.
- Claims/evidence checks required: every criterion must have KB support or explicit gap; output must not include current Studio audit findings.
- Optional review artifacts justified: no, unless `review.md` becomes too dense to verify.

## human approval requirements

- Required: unknown
- Approval owner: user
- Evidence needed: explicit user approval after delivery if they want to canonize the Framework.
- Cannot proceed past: publication/canonization outside this task without user approval.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Criteria invented beyond KB | Invalid Framework | research_agent / review_agent | Use claims table and mark KB gaps |
| Methodology becomes actual audit | Violates user constraint | writer_agent / review_agent | Prohibit current-state findings |
| Document package becomes hard to reuse | Weak operational value | writer_agent | Split by user workflows and provide package index |
| Scoring model overfits existing architecture | Narrow audit | writer_agent / review_agent | Use KB object map and coverage model to define broad domains |
| KB gaps hidden as recommendations | Unsupported claims | research_agent / writer_agent | Separate gap registry from criteria |

## unresolved questions

- None blocking.

## escalation conditions

- Stop or escalate if a required criterion cannot be supported and cannot be represented as a KB gap.
- Stop or escalate if current Studio evaluation is needed to continue.
- Stop or escalate if Knowledge Base files are missing or internally inconsistent in a way that prevents methodology drafting.

## completion criteria

- Required artifacts complete: brief, manifest, status, orchestration, research evidence, framework documents, review, final package, final decision.
- Review outcome acceptable: `approved`.
- Blockers resolved: yes.
- Governance fields complete: yes.

## finalization conditions

- Finalization may start when: independent `review.md` approves the Framework package or all required changes are resolved and re-reviewed.
- Finalization must stop when: review is missing, blocked, non-independent, or points to unresolved required changes.
- Compact finalization shape allowed: no, because deliverable is a multi-document high-governance framework.
- Conditional finalization artifacts needed: yes only if final editor makes non-trivial changes after review.

## restart notes

- Minimum read set: `brief.md`, `task-manifest.md`, `status.md`, `orchestration_plan.md`, `research.md`, `sources.md`, `claims_table.md`, current framework package.
- Current active version: initial package in this task folder.
- Deprecated/previous versions: none.
- Latest relevant handoff: none.
- Directly relevant pipeline/KB: article_pipeline, research_pipeline, AI Software Studio Knowledge Base.
