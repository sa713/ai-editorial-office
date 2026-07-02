# Orchestration Plan

## task summary

- Task ID: TASK-STUDIO-FIRST-AUDIT
- User goal: conduct the first independent audit of AI Software Studio.
- Deliverable: official Studio Audit Report and supporting analytical maps.
- Audience/channel: AI Software Studio owner and future governance use.
- Current active version: initial audit package.

## task classification

- Task type: audit report / high-governance analysis
- Risk mode: high-governance
- Factual sensitivity: high, because report evaluates current Studio maturity.
- Human approval likely required: unknown after delivery
- Rationale: The audit produces official maturity findings and must preserve
  evidence, independence, and constraints.

## process depth

- Depth: full
- Execution profile: expanded
- Rationale: Audit requires evidence inventory, criterion scorecard, area
  maturity, KB implementation analysis, report, and independent review.
- Forbidden depth shortcuts: no scoring without evidence; no recommendations;
  no Framework/KB modifications; no skipped review.
- Expanded profile trigger, if any: first official audit and high-governance
  evidence requirements.

## selected pipeline

- Pipeline: article_pipeline
- Why this pipeline: final deliverable is a reviewed analytical report based on
  research evidence.
- Pipeline exceptions or local constraints: Research stage performs audit
  evidence collection and scoring under Framework; Writer Agent drafts report
  from saved scorecard without changing findings.

## client profile

- Client profile: none
- Client profile status: not_applicable
- Activation reason: none
- Non-activation reason, if considered and rejected: independent Studio audit is
  not Sber communication.
- Client-profile files: none
- Stop condition: none.

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

- Rationale: User gave explicit audit scope and constraints. Evidence gaps will
  be recorded as limitations.
- Production may start: yes, starting with evidence collection.
- If `ask`: n/a
- If `constrain`: no process changes, no BRD, no roadmap, no Codex tasks.
- If `block`: n/a

## editorial decision frame

- Chosen editorial route: Framework-bound evidence audit.
- Why this route serves the task: It uses the approved methodology and keeps
  findings separated from implementation planning.
- Alternatives considered:
  - Alternative route, one line: Update Framework/KB during audit.
    - Why rejected, one line: User explicitly forbids changing either during audit.
  - Alternative route, one line: Produce roadmap after findings.
    - Why rejected, one line: User explicitly forbids development planning.
  - Alternative route, one line: Summarize without criterion-level evidence.
    - Why rejected, one line: Framework requires evidence-backed scoring.
- Writer contract:
  - Result type: official audit report package.
  - Angle or reader path: evidence -> criterion scores -> area maturity -> KB
    implementation -> risks/debt/limitations -> conclusion.
  - Scope boundary: current Studio assessment only; no implementation plan.
  - Must include: required report sections and additional analytical materials.
  - Must not include: recommendations, BRD, roadmap, Codex tasks, Framework/KB edits.
  - Source boundary and confidence: current repository evidence, approved
    Framework, existing KB.
- Review focus: evidence linkage, no recommendations, maturity consistency,
  Framework conformance, no accidental KB/Framework modification.
- Reroute triggers: missing Framework files, unauditable evidence base, or report
  drifting into implementation planning.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake/orchestration | chief_editor | yes | Route and constraints |
| Evidence collection/scoring | research_agent | yes | Framework-bound audit evidence |
| Report writing | writer_agent | yes | Draft official report from scorecard |
| Review | review_agent | yes | Independent review |
| Finalization | final_editor | yes | Final package index after approved review |
| Final governance | chief_editor | yes | Final decision |

## required knowledge and evidence

- Required Framework: `TASK-STUDIO-AUDIT-FRAMEWORK/framework/`
- Required KB: `kb/ai-software-studio-knowledge-base/`
- Required project evidence: AGENTS, project-state, agents, pipelines,
  templates, KB, scripts/tests, task artifacts, ideas/backlog/watchlist.
- Evidence gaps: to be recorded in report.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Scope and constraints |
| `task-manifest.md` | required | all roles | Restart pointer |
| `status.md` | required | all roles | State history |
| `orchestration_plan.md` | required | all roles | Execution contract |
| `evidence-register.md` | required | writer/reviewer | Evidence IDs |
| `criterion-scorecard.md` | required | writer/reviewer | Scoring basis |
| `kb-implementation-map.md` | required | writer/reviewer | KB realization analysis |
| `audit-report/*.md` | required | reviewer/user | Audit deliverables |
| `review.md` | required | final_editor/chief_editor | Review gate |
| `final.md` | required | user | Final index |
| `final_decision.md` | required | user/governance | Governance closure |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | chief_editor | user request, AGENTS, Framework | task pack | research may start |
| 2 | research_agent | Framework, KB, repo evidence | evidence register, scorecard, KB map | report can be drafted |
| 3 | writer_agent | scorecard and evidence | audit-report package | ready for review |
| 4 | review_agent | report/evidence | review.md | approved/changes_requested/blocked |
| 5 | final_editor | approved report | final.md | package ready |
| 6 | chief_editor | final package/review | final_decision.md | finalized |

## status transitions

- Starting status: research
- Next expected status: writing
- Status owner: current role
- Status update trigger: evidence complete, writing complete, review outcome,
  finalization, final decision.

## review requirements

- Review artifact: `review.md`
- Review depth: full audit report review.
- Reviewer independence requirement: reviewer must not be the writer/scorer role instance.
- Claims/evidence checks required: all findings need evidence IDs; all scores
  must use Framework maturity/evidence rules.
- Optional review artifacts justified: yes only if `review.md` becomes too dense.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Audit becomes roadmap | Violates user constraints | all roles | Prohibit recommendations/tasks |
| Evidence gaps overinterpreted | Unfair maturity scoring | research_agent/review_agent | Record confidence and limits |
| Framework gap treated as Studio failure | Invalid conclusion | research_agent/review_agent | Separate Framework/KB gaps |
| Old task artifacts overgeneralized | Sampling bias | research_agent | Record sampling limitations |

## unresolved questions

- None blocking.

## escalation conditions

- Stop if Framework or KB would need modification to continue.
- Stop if user requests implementation planning during audit.
- Stop if evidence is too incomplete to score an area and mark it unauditable
  instead of inventing a score.

## completion criteria

- Evidence register complete.
- Criterion scorecard complete.
- KB implementation map complete.
- Audit report package complete.
- Independent review approved.
- Final decision recorded.

## finalization conditions

- Finalization may start when: `review.md` outcome is approved.
- Finalization must stop when: any required change remains unresolved.
- Compact finalization shape allowed: no.
- Conditional finalization artifacts needed: finalization notes/checklist if
  final editor makes non-trivial changes.

## restart notes

- Minimum read set: brief, manifest, status, orchestration plan, Framework,
  evidence register, criterion scorecard, KB implementation map, report package.
- Current active version: initial audit package.
- Deprecated/previous versions: none.
- Latest relevant handoff: none.
- Directly relevant pipeline/KB: article_pipeline, research_pipeline, approved
  Studio Audit Framework, AI Software Studio KB.

