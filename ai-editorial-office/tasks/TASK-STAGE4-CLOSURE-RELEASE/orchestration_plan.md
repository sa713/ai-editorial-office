# Orchestration Plan

## task summary

- Task ID: `TASK-STAGE4-CLOSURE-RELEASE`
- User goal: formally close Stage 4 by synchronizing accepted-state wording only
- Deliverable: reviewed, validated, committed, and pushed state-only closure diff
- Audience/channel: Project Lead through repository artifacts and final handback
- Current active version: this plan

## task classification

- Task type: project-state synchronization release
- Risk mode: `high-governance`
- Factual sensitivity: high for accepted state, low for technical content because technical content is forbidden to change
- Human approval likely required: yes; current mission supplies closure, commit, and push authority
- Rationale: canonical current-state files, release packs, and external memory must agree without changing behavior

## process depth

- Depth: `full`
- Execution profile: `expanded`
- Rationale: multi-surface canonical state, memory synchronization, independent review, commit, and push need full traceability
- Forbidden depth shortcuts: no blind global replacement; no review bypass; no rewriting historical task/research evidence
- Expanded profile trigger: canonical state conflict identified by Stage 4 Strategic Review

## selected pipeline

- Pipeline: `research_pipeline.md` with the custom state-synchronization mini-contract below
- Why this pipeline: the task begins with repository-state research and produces a source-bounded written synchronization result; the local mini-contract handles the non-article repository diff
- Pipeline exceptions or local constraints: the reviewed repository diff is the primary deliverable; task-local `final.md` is only a compact closure summary and must not alter the diff

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

- Rationale: the user named the accepted releases, exact state targets, forbidden changes, validations, commit, and push requirement
- Production may start: yes

## editorial decision frame

- Chosen editorial route: inventory current state-bearing surfaces, apply state-only wording updates, synchronize memory, independently review the diff, validate, commit, and push
- Why this route serves the task: it closes the documented acceptance gap without changing technical content or architecture
- Alternatives considered:
  - Global replacement across all historical artifacts
    - Rejected because it would falsify the release-candidate audit trail.
  - Update only `project-state.md`
    - Rejected because pack identity, index, roadmap, release packs, backlog, and memory would remain inconsistent.
  - Open S5.R1 automatically
    - Rejected because the user explicitly forbids starting Stage 5.
- Writer contract:
  - Result type: bounded lifecycle/state wording patch
  - Scope boundary: only current Stage 4 state surfaces and required task-local closure evidence
  - Must include: accepted pack state, Stage 4 complete, Stage 5 not started, final release-pack state, memory sync
  - Must not include: technical edits, new catalog/framework, new Stage 5 state, rewritten historical RC evidence
  - Source boundary and confidence: repository acceptance verdicts and current user instruction; high confidence
- Review focus: changed-line semantics, technical-content preservation, historical evidence preservation, exact current-state consistency, memory sync, Stage 5 unopened
- Reroute triggers: technical diff, unclear acceptance authority, historical-record rewrite, or validation failure

## custom workflow mini-contract

- Deviation: repository state diff replaces an ordinary draft/final artifact
- Reason: this is a state synchronization release, not editorial content production
- Owner: Writer Agent for wording patch; Review Agent for independent diff verdict; Chief Editor for final closure
- Review gate preserved: yes
- Governance model unchanged: yes

## required agents

| Stage | Role | Required? | Notes |
| --- | --- | --- | --- |
| Research | Research Agent | yes | Inventory and historical/current classification |
| Writing | Writer Agent | yes | Apply state-only wording patch |
| Review | Review Agent | yes | Independent diff review |
| Final governance | Chief Editor | yes | Validate review, commit, push, and record closure |

## required knowledge and evidence

- Required KB: `kb/domain_knowledge_pack_standard.md` only for pack status semantics; no domain pack activated
- Required source/evidence files: Stage 4 release packs, `BACKLOG.md`, `ROADMAP.md`, `project-state.md`, Stage 4 Strategic Review, `/about` validator
- Evidence gaps: none

## artifact scope

| Artifact | Required / conditional / omitted | Consumer | Rationale |
| --- | --- | --- | --- |
| `task-manifest.md` | required | all roles | Restart and governance state |
| `research.md` | required | Writer/Review | Repository-wide state inventory |
| `review.md` | required | Chief Editor | Independent approval |
| `final_decision.md` | required | Project Lead | Closure governance |
| `qa-checklist.md` | omitted | none | Review can contain all checks |
| `review-summary.md` | omitted | none | No separate consumer |
| `final.md` | required | Chief Editor | Compact finalization summary; repository diff remains the deliverable |

## execution order

| Step | Role | Input | Output | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Research Agent | Mission, current repository | Inventory and handoff | Current vs historical surfaces classified |
| 2 | Writer Agent | Inventory and contract | State-only repository patch and handoff | No technical content changed |
| 3 | Review Agent | Mission, inventory, full diff | `review.md` | `approved`, `changes_requested`, or `blocked` |
| 4 | Final Editor | Approved review and diff | `final.md` and finalization handoff | Summary preserves the approved scope without changing the diff |
| 5 | Chief Editor | Approved review, final summary, and validations | `final_decision.md`, commit, push | Remote contains closure commit |

## review requirements

- Review artifact: `review.md`
- Review depth: full changed-line and omission review
- Reviewer independence requirement: reviewer must not be the Writer Agent instance
- Claims/evidence checks required: accepted verdicts, no pending wording on current surfaces, Stage 5 unopened, technical content unchanged, memory package aligned
- Optional review artifacts justified: no

## human approval requirements

- Required: yes
- Approval owner: Project Lead/user
- Evidence needed: current mission
- Cannot proceed past: push if requested scope or destination changes

## known risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Blind replacement rewrites history | Audit trail loss | Research/Writer | Current-vs-historical classification and exact patches |
| Technical pack content changes | Functional/semantic drift | Writer/Review | Limit pack diffs to identity/lifecycle wording |
| Stage 5 opens accidentally | Roadmap/backlog violation | Review | Assert every S5 row remains `Not Started` |
| `/about` diverges or gains files | Memory validation failure | Writer/Review | Exact project-state copy and 20-file validator |
| Unrelated work enters commit | Scope violation | Chief Editor | Stage exact paths and inspect commit scope |

## completion criteria

- Required artifacts complete: yes after research, review, and final decision
- Review outcome acceptable: `approved`
- Blockers resolved: yes
- Governance fields complete: yes

## finalization conditions

- Finalization may start when: independent review approves the complete state-only diff
- Finalization must stop when: any functional/technical change or required validation failure remains
- Compact finalization shape allowed: no; full closure evidence is required
- Conditional finalization artifacts needed: `final.md`, finalization handoff, and `final_decision.md`

## restart notes

- Minimum read set: `AGENTS.md`, `brief.md`, `task-manifest.md`, this plan, `status.md`, latest handoff, current diff
- Current active version: this plan and current manifest
- Deprecated/previous versions: none
- Latest relevant handoff: pending
- Directly relevant pipeline/KB: `research_pipeline.md`; custom mini-contract here; Domain Knowledge Pack Standard for status semantics only
