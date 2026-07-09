# Orchestration Plan

## task summary

- Task ID: `TASK-CYBERSECURITY-DOMAIN-PACK-RELEASE`
- User goal: complete `S4.R4 - Cybersecurity Domain Pack` to release-candidate
  state.
- Deliverable: source-backed cybersecurity domain pack plus release research,
  validation, release pack, review, and governance closure.
- Audience/channel: Project Lead review inside AI Editorial Office repository.
- Current active version: initial release task.

## task classification

- Task type: domain knowledge pack release.
- Risk mode: `high-governance`.
- Factual sensitivity: high; source-backed cybersecurity guidance and system
  canon integration.
- Human approval likely required: yes for accepted release, no for local
  release-candidate production.
- Rationale: the release changes canonical KB, source register expectations,
  current release state, and external memory if required.

## process depth

- Depth: `full`.
- Execution profile: `expanded`.
- Rationale: release is source-heavy, security-sensitive, canonical, and
  requires independent review plus release-pack readiness evidence.
- Forbidden depth shortcuts: no direct production without research; no skipped
  review; no finalization before approved review; no pack-as-policy drift.
- Expanded profile trigger, if any: active from start due high-governance
  release scope.

## selected pipeline

- Pipeline: `research`.
- Why this pipeline: the release follows the roadmap release cycle:
  research -> architecture synthesis -> capability/domain release ->
  validation -> memory sync when required.
- Pipeline exceptions or local constraints: release implementation uses a
  task-local mini-contract while preserving the existing review gate and
  governance model.

## client profile

- Client profile: `none`.
- Client profile status: `not_applicable`.
- Activation reason: none.
- Non-activation reason, if considered and rejected: task is a repository
  system release, not client-owned communication.
- Client-profile files: none.
- Stop condition: activate no client profile unless user explicitly changes
  task ownership.

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

- Rationale: the user supplied release ID, governing files, deliverables,
  source preferences, constraints, validation scope, and handback format.
- Production may start: yes.
- If `ask`: not applicable.
- If `constrain`: keep the pack defensive, review-oriented, and subordinate to
  existing canon.
- If `block`: not applicable.

## editorial decision frame

- Chosen editorial route: source-backed domain-pack release with compact
  research, architecture synthesis, canonical pack, release report, review, and
  release pack.
- Why this route serves the task: it follows the Domain Knowledge Pack Standard
  and roadmap release model without adding operational architecture.
- Alternatives considered:
  - Alternative route, one line: create a security-review capability.
    - Why rejected, one line: duplicates Engineering Review and violates the
      user's no-new-capability constraint.
  - Alternative route, one line: extend the DevSecOps pack with broad
      cybersecurity content.
    - Why rejected, one line: blurs delivery-specific context with broader
      threat, control, abuse-case, and assurance context.
  - Alternative route, one line: create a standalone security workflow or
      approval gate.
    - Why rejected, one line: explicitly forbidden and inconsistent with domain
      pack architecture.
- Writer/UX Writer contract:
  - Result type: canonical domain pack and release documents.
  - Angle or reader path: practical source-backed defensive cybersecurity
    context for existing AI Editorial Office roles and capabilities.
  - Scope boundary: broad cybersecurity context, not DevSecOps ownership,
    incident response operations, legal compliance, penetration testing, or
    exploit guidance.
  - Must include: activation boundaries, safety boundaries, assets/actors/trust
    boundaries, threats/abuse cases, weakness classes, controls/mitigations,
    risk/assurance, secure design, evidence expectations, review questions,
    source register, confidence/update/retirement rules, and canon relations.
  - Must not include: exploit steps, bypass procedures, malware guidance,
    credential theft guidance, stealth/persistence guidance, unauthorized
    access instructions, new roles, new gates, new pipelines, or mandatory
    artifacts.
  - Source boundary and confidence: authoritative cybersecurity standards,
    frameworks, and maintained references; exact platform behavior requires
    task-specific refresh.
- Review focus: pack standard compliance, source support, safety boundary,
  adjacent-domain boundary, no architecture drift, scenario validation, and
  release readiness.
- Reroute triggers: source evidence insufficient, safety boundary conflict,
  DevSecOps/Engineering Review duplication, new-governance drift, or validation
  failure.

## custom workflow mini-contract

- Deviation: roadmap release work adds architecture synthesis, release report,
  and release pack to the research pipeline.
- Reason: Domain Expertise releases require research, synthesis,
  implementation, validation, memory disposition, and release-pack readiness.
- Owner: `chief_editor`.
- Review gate preserved: yes.
- Governance model unchanged: yes.

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Intake | `chief_editor` | yes | User request is sufficiently defined |
| Research | `research_agent` | yes | Source-backed landscape and source register |
| Writing/UX writing | `writer_agent` | yes | Pack and release documents |
| Review | `review_agent` | yes | `review.md` required |
| Finalization | `final_editor` | yes | Final deliverable pointer after approved review |
| Final governance | `chief_editor` | yes | `final_decision.md` required |

## required knowledge and evidence

- Required KB:
  - `kb/domain_knowledge_pack_standard.md`
  - `kb/engineering_review.md`
  - `kb/devsecops_domain_pack.md`
  - `kb/software_architecture_domain_pack.md`
- Required source/evidence files:
  - `AGENTS.md`
  - `ROADMAP.md`
  - `BACKLOG.md`
  - `project-state.md`
  - authoritative cybersecurity sources in the source register
- Evidence gaps: none blocking; volatile source versions must be recorded with
  last-checked date.

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `brief.md` | required | all roles | Mission scope |
| `task-manifest.md` | required | all roles | Current state |
| `status.md` | required | all roles | Status history |
| `cybersecurity_pack_landscape.md` | required | Writer / Review | Source-backed research |
| `cybersecurity_pack_architecture_synthesis.md` | required | Writer / Review / Project Lead | Architecture fit |
| `kb/cybersecurity_domain_pack.md` | required | future tasks / Review | Canonical domain pack |
| `cybersecurity_pack_release_report.md` | required | Review / Project Lead | Validation and release result |
| `release-pack.md` | required | Project Lead | Release readiness |
| `review.md` | required before finalization | Chief Editor / Final Editor | Review gate |
| `qa-checklist.md` | omitted | none | Review checklist can live in `review.md` |
| `review-summary.md` | omitted | none | `review.md` is sufficient |
| `open-questions.md` | omitted unless blockers appear | Chief Editor | No current blockers |
| `final.md` | required after approved review | Chief Editor | Final deliverable pointer |
| `finalization-notes.md` | omitted unless controlled changes are needed | Chief Editor | No separate consumer yet |
| `finalization-checklist.md` | omitted unless finalization risk expands | Chief Editor | Release pack and final decision carry readiness |

## structure-before-writing plan

- Reader path: purpose -> activation -> boundary -> concepts -> guidance ->
  evidence -> review questions -> source register -> maintenance/canon
  relations -> safety.
- Section roles: each section answers a specific downstream question and avoids
  repeating the standard.
- Required structure: Domain Knowledge Pack Standard plus user-required
  cybersecurity sections.
- Duplication risks: duplicating Engineering Review, DevSecOps pack,
  Architecture Review, compliance ownership, or incident response ownership.

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | `research_agent` | Brief and governing docs | Landscape research | Sources sufficient |
| 2 | `chief_editor` / `writer_agent` | Research | Architecture synthesis | Fit decision recorded |
| 3 | `writer_agent` | Research and synthesis | Cybersecurity pack and release report | Draft release complete |
| 4 | `review_agent` | All release artifacts | `review.md` | Approved or changes requested |
| 5 | `final_editor` | Approved review | `final.md` | Final pointer complete |
| 6 | `chief_editor` | Final artifacts and validation | `final_decision.md` | Release candidate ready |

## status transitions

- Starting status: `research`
- Next expected status: `writing`
- Status owner: `chief_editor`
- Status update trigger: research complete, production complete, review result,
  finalization, or blocker.

## review requirements

- Review artifact: `review.md`
- Review depth: high-governance full review.
- Reviewer independence requirement: `review_agent` must be distinct from
  research and writer role instances.
- Claims/evidence checks required: source register support, confidence limits,
  pack-standard section completeness, safety constraints, adjacent-pack
  boundaries, scenario validation, and command validation.
- Optional review artifacts justified: no; `review.md` can carry the checklist.

## human approval requirements

- Required: yes for accepted release; no for release-candidate production.
- Approval owner: Project Lead.
- Evidence needed: completed release pack, approved review, validation results,
  final decision, and commit hash.
- Cannot proceed past: release candidate can be produced; accepted release
  requires Project Lead review.

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Safety overreach into offensive details | High | Writer / Review | Keep categories defensive and exclude operational misuse instructions |
| Duplication of DevSecOps pack | Medium | Writer / Review | Keep delivery automation in DevSecOps and broad security context here |
| Pack treated as policy owner | High | Chief Editor / Review | Repeated canon-boundary language |
| Source staleness | Medium | Research | Source register, stale-if triggers, update rules |
| Over-activation for incidental security terms | Medium | Chief Editor / Review | Strong non-activation criteria and scenario validation |

## unresolved questions

- None blocking.

## escalation conditions

- Stop or escalate if safety constraints conflict with requested pack content,
  source evidence cannot support a material claim, or the release would require
  a new role, pipeline, gate, or policy owner.

## completion criteria

- Required artifacts complete.
- Review outcome acceptable.
- Blockers resolved.
- Governance fields complete.
- Release pack recommends Project Lead review.

## finalization conditions

- Finalization may start when: `review.md` has outcome `approved`.
- Finalization must stop when: review is missing, blocked, changes requested,
  or no longer matches current artifacts.
- Compact finalization shape allowed: no, because release is high-governance.
- Conditional finalization artifacts needed: no unless review requests them.

## restart notes

- Minimum read set: `AGENTS.md`, `ROADMAP.md`, `BACKLOG.md`,
  `project-state.md`, this task manifest, this plan, status, latest handoff,
  current working artifact, and required KB.
- Current active version: this release task and listed deliverables.
- Deprecated/previous versions: none.
- Latest relevant handoff: none yet.
- Directly relevant pipeline/KB: `research` pipeline and named governing KB.

