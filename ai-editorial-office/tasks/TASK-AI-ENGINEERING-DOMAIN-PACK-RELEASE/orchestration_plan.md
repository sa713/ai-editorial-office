# Orchestration Plan

## task summary

- Task ID: `TASK-AI-ENGINEERING-DOMAIN-PACK-RELEASE`
- User goal: complete S4.R5 as a source-backed AI Engineering Domain Pack
  Release Candidate.
- Deliverable: canonical candidate pack, research landscape, architecture
  synthesis, release report, release pack, validation, review, and RC
  governance closure.
- Audience/channel: Project Lead repository review; reusable canonical KB after
  later acceptance.
- Current active version: task artifact set named by `task-manifest.md`.

## task classification

- Task type: domain-pack research and canonical release implementation.
- Risk mode: `high-governance`.
- Factual sensitivity: high; current AI product behavior, safety, evaluation,
  and security boundaries require authoritative evidence.
- Human approval likely required: yes, for Project Lead acceptance.
- Rationale: the release changes canonical domain context, touches safety and
  adjacent-owner boundaries, and requires external source reconstruction.

## process depth

- Depth: `full`.
- Execution profile: `expanded`.
- Rationale: source-heavy, architecture-sensitive, safety-relevant release with
  multiple canonical and non-canonical artifacts.
- Forbidden depth shortcuts: no direct research-to-canon writing without
  traceability; no self-review; no early `final.md`; no RC claim before review.
- Expanded profile trigger: present from start because of high governance,
  source sensitivity, architectural boundaries, and human acceptance boundary.

## selected pipeline

- Pipeline: `research`, followed by normal writing, independent
  `review_pipeline`, controlled finalization, and Chief Editor governance.
- Why this pipeline: the release's claims and guidance require a reconstructable
  evidence base before canonical writing.
- Pipeline exceptions or local constraints: release artifacts live at the
  user-required repository paths while lifecycle evidence stays task-local.

## client profile

- Client profile: `none`.
- Client profile status: `not_applicable`.
- Non-activation reason: this is repository canon, not client-owned content.
- Stop condition: none.

## domain-pack activation

- Active standard: `kb/domain_knowledge_pack_standard.md`.
- Adjacent active packs: Software Architecture, Cybersecurity, and DevSecOps.
- Activation reason: their boundaries materially constrain the new pack and
  prevent duplicated ownership.
- Candidate AI Engineering pack: task-specific research only until reviewed;
  it is not yet accepted canon.
- Relevant sections: activation/non-activation, boundary, sources/evidence,
  review, update/retirement, safety, and relations to existing canon.
- Confidence: repository constraints `verified`; external AI engineering
  guidance must be `supported` or `verified` from current authoritative sources.

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

- Rationale: the mission names paths, governing sources, required sections,
  safety limits, scenarios, and RC boundary.
- Production may start: yes, beginning with research.

## planning and analytical frame

- Planning level: expanded.
- Analytical question: what durable, source-backed AI engineering context
  improves AI Editorial Office work while remaining bounded beneath existing
  roles, capabilities, domain packs, and review governance?
- Decomposition: system surfaces; prompt/instruction; retrieval; data;
  evaluation; reliability/monitoring; human oversight; safety/misuse;
  integration/workflows; AI-assisted engineering; adjacent-owner boundaries.
- Competing shapes considered:
  - one broad AI engineering context pack;
  - multiple narrow packs for prompts, RAG, evals, and agents;
  - a new AI review workflow or specialist role.
- Working conclusion: one bounded pack best matches the existing Domain
  Knowledge Pack architecture; narrow packs would fragment context, and a role
  or approval workflow is explicitly forbidden.
- Disconfirmation check: split or reroute only if authoritative evidence shows
  one area requires a distinct canonical owner that the current standard cannot
  contain without policy or workflow authority.
- Sufficiency target: authoritative coverage across every required section,
  explicit confidence limits, practical review questions, and scenario proof
  that activation and escalation boundaries work.

## capabilities

- Analytical Reasoning: active for evidence synthesis, boundary decisions, and
  scenario judgments.
- Professional Analysis: active for landscape synthesis and decision-ready
  release reporting.
- Professional Communication: active for a layered Project Lead release packet
  and reusable pack clarity.
- Architecture Review: active for canonical-owner fit, adjacency, quality
  attributes, and architecture preservation.
- Engineering Review: active for changed repository surface, path/link
  integrity, validation evidence, maintainability, and residual change risk.

## quality profile

- Priority attributes: correctness, evidence support, traceability, boundary
  precision, completeness, reviewability, maintainability, and actionability.
- Accepted tradeoffs: prefer durable principles and source pointers over
  exhaustive vendor feature catalogs; preserve detail needed for review even
  when the pack is long.
- Must preserve: safety boundaries, source confidence limits, adjacent-owner
  separation, current-state accuracy, and Project Lead acceptance boundary.
- May relax: narrative polish and broad tutorial detail.
- Review focus: required-section coverage, claim support, practical usefulness,
  non-duplication, scenario validity, and release-state consistency.

## editorial decision frame

Refresh after research sufficiency before Writer Agent starts.

- Chosen editorial route: a single layered AI Engineering Domain Knowledge Pack
  plus required release research and decision artifacts.
- Why this route serves the task: it provides reusable domain context while
  fitting the existing Domain Knowledge Pack Standard and release model.
- Alternatives considered:
  - Separate Prompt, RAG, Evals, and Agents packs.
    - Rejected because it fragments one coherent domain and adds maintenance
      cost without evidence of separate owners.
  - Add an AI specialist role or review/approval workflow.
    - Rejected because roles and gates are explicitly outside pack authority.
  - Produce a short source list with minimal guidance.
    - Rejected because it would not answer the required practical questions or
      support review scenarios.
- Writer contract:
  - Result type: canonical pack plus landscape, synthesis, release report, and
    release pack.
  - Reader path: identity and activation first; system surfaces and durable
    engineering guidance next; review/safety/boundaries and source maintenance
    last.
  - Scope boundary: domain context, not operational policy or approval.
  - Must include: every user-required section, source register, confidence
    notes, adjacent-pack relations, and representative validation.
  - Must not include: new architecture elements, unsafe procedures, unsupported
    product claims, or claims that a framework/checklist proves safety.
  - Source boundary and confidence: only inspected task-local and authoritative
    external sources; volatile details must carry freshness limits.
- Review focus: source sufficiency, required structure, boundary ownership,
  practical usefulness, safety, scenario validation, state/memory sync.
- Reroute triggers: evidence gap, ownership conflict, unsafe detail, or a
  canonical standard requirement the proposed pack cannot satisfy.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake/orchestration | `chief_editor` | yes | Routing and governance only |
| Research | `research_agent` | yes | Full authoritative evidence |
| Writing | `writer_agent` | yes | Candidate pack and release packet |
| Review | `review_agent` | yes | Independent `review.md` |
| Finalization | `final_editor` | yes | Controlled `final.md` and handoff |
| Final governance | `chief_editor` | yes | RC decision, not Project Lead acceptance |

## artifact scope

- Full-evidence artifacts are required because factual sensitivity and review
  traceability are material.
- `review.md` is the primary review artifact; separate `qa-checklist.md` and
  `review-summary.md` are omitted unless independent review finds a concrete
  downstream need.
- `open-questions.md` is omitted unless a real blocker, deferred decision, or
  traceability gap emerges.
- Finalization notes/checklist are omitted unless controlled changes or a
  reviewer/governance traceability need emerges.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `chief_editor` | Mission and canon | Entry artifacts and handoff | Research assignment valid |
| 2 | `research_agent` | Governing docs and authoritative sources | Evidence set and landscape | Research sufficient |
| 3 | `chief_editor` | Research handoff | Refreshed route and writing handoff | Writer contract current |
| 4 | `writer_agent` | Full evidence and route | Synthesis, pack, report, release pack, integration updates | Packet review-ready |
| 5 | `review_agent` | Current packet and evidence | Independent `review.md` | Approved or bounded repair |
| 6 | repair owner | Review findings | Bounded corrections | Re-review approved |
| 7 | `final_editor` | Approved packet | `final.md` and finalization handoff | Meaning unchanged |
| 8 | `chief_editor` | Approved review and finalization | `final_decision.md`, state sync | RC ready for Project Lead |

## review and approval requirements

- Review depth: full, deterministic, source-aware, architecture-aware,
  engineering-aware, and safety-aware.
- Reviewer independence: Review Agent must not be the Writer Agent role
  instance.
- Claims/evidence checks: required against `sources.md`, `facts.md`,
  `claims_table.md`, and `claims-used.md`.
- Human approval: Project Lead acceptance required after RC; no publication or
  acceptance is inferred.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Fast-changing vendor docs | Stale guidance | Research/Review | Date sources and add stale-if triggers |
| AI safety content drifts into offensive detail | Misuse risk | Writer/Review | Keep category-level, defensive guidance |
| Pack duplicates adjacent owners | Architecture drift | Chief/Review | Explicit relations and escalation boundaries |
| Evaluation guidance becomes universal scoring policy | Governance creep | Writer/Review | Keep task-shaped, evidence-backed context |
| Release state drifts across files | Release ambiguity | Writer/Review | Keep candidate state and memory synchronized through final validation |

## completion and finalization conditions

- Required artifacts complete: all user-named deliverables plus task evidence,
  review, finalization, and governance records.
- Review outcome acceptable: `approved` from an independent reviewer.
- Blockers resolved: yes.
- Governance fields complete: RC status, residual risks, Project Lead next step,
  and memory disposition visible.
- Finalization may start only after approved review.
- Compact finalization shape allowed: no; this release needs a task-local
  `final.md` and finalization handoff for RC governance traceability.

## restart notes

- Minimum read set: `task-manifest.md`, latest handoff, current working
  artifact, `brief.md`, and directly relevant pipeline/KB.
- Current active version: task artifact set named by `task-manifest.md`.
- Deprecated/previous versions: none.
- Latest relevant directive: round 1 `review.md`; after repair, use
  `handoff-repair-writer-agent-to-review-agent.md`.
