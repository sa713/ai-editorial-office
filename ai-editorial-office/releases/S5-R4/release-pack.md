# Release Pack

Release readiness rule: no release is considered ready for Project Lead review
until a completed `release-pack.md` exists.

## Release

- Release ID: `S5.R4`
- Release title: Task Need Recognition
- Status: release candidate ready after independent approval, controlled
  finalization, final staged validation, and local commit; Project Lead review
  pending
- Date: 2026-07-10

## Executive Summary

S5.R4 adds an evidence-first advisory capability that helps Chief Editor
recognize likely task type, capabilities, Domain Packs, evidence/research,
risk/consequence and review needs, significance, ambiguity, decomposition, and
uncertainty before work begins. It reuses existing owners, keeps every decision
manual, and adds no automatic routing, activation, role, pipeline, stage, gate,
or plan.

## Architectural Impact

Architecture impact:

- Small

Reason:

One bounded shared capability owner now defines the previously missing
request-to-need recommendation contract. All routing, preflight, risk, depth,
activation, decomposition, planning, review, and governance authority remains
with existing owners.

## Goal Of The Release

Improve the evidence available to Chief Editor for proportional task routing
without making Task Need Recognition a router or decision maker.

## Architecture Decisions

- Decision: add one bounded `kb/task_need_recognition.md` owner and integrate it
  through existing Intake, Chief Editor, task-object, lifecycle, and review
  surfaces.
- Rationale: existing canon owns all component signals and decisions but did
  not own a shared, inspectable request-to-need advisory contract.
- Architecture preserved: yes; recommendations are optional, qualitative, and
  non-binding, and existing artifacts hold the view.

## Capability Decisions

- Capability shape: one shared advisory capability, not a role, router,
  classifier, taxonomy, framework, store, or workflow.
- Activation: Intake or Chief Editor may use the compact view when material;
  Chief Editor alone confirms actual capabilities and Domain Packs.
- Review: existing Review Agent challenges evidence, outcome-over-keyword
  reasoning, negative cases, proportionality, uncertainty, decomposition,
  owner boundaries, and non-automation inside the current gate.
- Non-goals: automatic routing, capability/pack activation, review/research
  selection, task splitting, planning, scoring, or governance.

## Scope

### Implemented

- Evidence-first recognition signal families.
- Likely primary task type plus material secondary aspects.
- Capability and primary/adjacent/no-pack recommendations.
- Qualitative research/evidence and review recommendations with rationale.
- Qualitative risk/consequence recommendation without selecting a risk mode.
- Architecture, engineering, communication, and analytical significance.
- Ambiguity, contradictions, missing information, uncertainty, negative
  evidence, and confidence.
- Advisory split/sequence or keep-coherent recommendation.
- Explicit non-decision and separate Chief Editor decision/next question.
- Ten representative cases including ambiguous, multi-domain, and keyword-rich
  simple requests.
- Existing-owner, state, task lifecycle, and `/about` memory integration.

### Merged

- Request evidence production into Intake Agent's current normalization work.
- Challenge and final route decision into Chief Editor's current authority.
- Review challenge into the existing Review Agent and Review Pipeline.
- Optional recording into existing brief, manifest, or orchestration plan.
- Capability and pack materiality into their existing canonical owners.

### Postponed

- Real-use observation of recognition quality, false-positive/false-negative
  recommendations, simple-task weight, and operational usefulness.
- Any future advisory lint, tooling, or Evaluation Signal based on saved use
  evidence and a separately authorized release.
- S5.R5 Editorial Intelligence Acceptance.

### Rejected

- Automatic intent classification, routing, activation, depth selection,
  decomposition, planning, or lifecycle transition.
- Keyword rules, numeric confidence/risk/complexity/routing scores, thresholds,
  ranks, or universal taxonomies.
- New Task Router, Classifier, Triage Agent, pipeline, stage, review gate,
  status, store, dashboard, or mandatory artifact.
- Duplicate ownership of Preflight, Professional Analysis, Evaluation Signals,
  Architecture Review, Engineering Review, Professional Communication,
  evidence, Domain Packs, or Chief Editor decisions.

## Canonical Files Changed

- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/agents/intake_agent.md`
- `ai-editorial-office/agents/review_agent.md`
- `ai-editorial-office/kb/00_index.md`
- `ai-editorial-office/kb/capability_registry.md`
- `ai-editorial-office/kb/shared_lifecycle_kernel.md`
- `ai-editorial-office/kb/task_need_recognition.md`
- `ai-editorial-office/kb/task_object_model.md`
- `ai-editorial-office/pipelines/review_pipeline.md`
- `ai-editorial-office/project-state.md`

## Canonical Owners Updated

Updated canonical owners:

- Governance/ownership map and Chief Editor entry behavior.
- Capability Registry and Task Need Recognition capability owner.
- Task Object Model and Shared Lifecycle Kernel integration.
- Intake Agent, Chief Editor, Review Agent, and Review Pipeline boundaries.
- Project State current Release Candidate state.

New canonical owners introduced:

- Task Need Recognition capability owner only; no operational authority.

## Non-Canonical Files

- `ai-editorial-office/ROADMAP.md`
- `ai-editorial-office/BACKLOG.md`
- conditional orchestration-plan template section
- three required research/release reports
- ten-case smoke test and tests index
- `ai-editorial-office/releases/S5-R4/release-pack.md`
- `ai-editorial-office/tasks/TASK-TASK-NEED-RECOGNITION-RELEASE/`
- `/about` exact copies and compact memory summaries

## Evaluation Signals

| Decision question | Observation and evidence | Scope / comparison / missing cases | Interpretation, alternatives, and confidence | Existing owner | Project Lead consideration | Explicit non-decision |
| --- | --- | --- | --- | --- | --- | --- |
| Does the release improve the request-to-route evidence boundary? | One shared view separates observed signals, recommendations, uncertainty/negative evidence, explicit non-decision, and Chief Editor decision; 10 cases pass. | Synthetic cases and document contract only; no real-use accuracy or cost evidence. | Supported that the boundary is inspectable; operational improvement remains unproven. | Task Need Recognition, Chief Editor, Review Agent | Assess whether the view is useful and proportionate. | No automatic route, activation, acceptance, or next-release action. |
| Does the release preserve stable architecture? | Existing role, lifecycle, artifact, capability, pack, evidence, and review owners remain authoritative; repository validators pass. | Current patch and owner map; future misuse remains possible. | Verified for this release; one new bounded non-role capability owner is the smallest coherent owner. | AGENTS, capability registry, Chief Editor, Project Lead | Confirm the owner addition is justified and non-duplicative. | No new role, pipeline, stage, gate, status, store, or governance layer. |
| Does recognition protect simple work and uncertainty? | Cases 1 and 10 stay compact with no packs; case 7 remains ambiguous and requests clarification; case 8 keeps one coherent multi-domain decision. | Ten designed cases; no production distribution or adversarial corpus. | Supported contract behavior, with synthetic limitation explicit. | Intake Agent, Chief Editor, Review Agent | Inspect negative evidence and decomposition proportionality. | No accuracy score, confidence threshold, forced label, or automatic split. |

## Release Metrics

Canonical files changed: 11

Research artifacts: 3 required release artifacts plus task-local sources,
facts, and claim traceability

Templates: 1 conditional section in an existing template

Tests: 1 new ten-case manual smoke test; tests index updated; existing lifecycle
and task-pack suites run

Memory package updated: yes; mapped exact copies and three compact summaries;
still 20 files

Validation scripts executed: repository diff, memory package, lifecycle suite,
task-pack suite, direct task validation, structured scenario/state/boundary
checks, and staged-diff validation

Commits: 1 local Release Candidate commit; hash reported in handback

## Validation Results

| Check | Result |
| --- | --- |
| `git diff --check` | passed |
| `git diff --cached --check` | passed on authorized staged scope |
| `sh ai-editorial-office/scripts/check_about_memory_package.sh` | passed; 20 files and mapped copies match |
| `sh ai-editorial-office/tests/test_task_lifecycle_validator.sh` | passed |
| `sh ai-editorial-office/tests/test_task_pack_generator.sh` | passed |
| direct S5.R4 task lifecycle validation | passed; 0 blockers, 0 warnings |
| ten representative scenarios | passed; 10 cases and 10 pass outcomes |

## Known Risks

- Advisory quality depends on available evidence and human judgment.
- Qualitative recommendations may vary across comparable tasks.
- Overuse could make trivial work unnecessarily heavy.
- Pack/current-source staleness still requires owner-specific checks.
- Synthetic cases do not prove operational accuracy or improvement.

## Open Questions

- None blocking independent review.

## Recommended Project Lead Decision

Accepted

or

Changes Requested

Recommended decision: Accepted after architectural review confirms the new
bounded owner is proportionate and Chief Editor authority is preserved.

## Suggested Next Release

- S5.R5 Editorial Intelligence Acceptance, only after Project Lead acceptance
  of S5.R4 and an explicit new mission.

## Acceptance Checklist

- Architecture preserved
- Review gate unchanged
- No new roles
- No new pipelines
- No lifecycle changes
- Validation passed
- Memory synchronized (if required)
- Ready for Project Lead review

## Release Verdict

Project Lead: Accepted

Review Date: 2026-07-10

Reviewer: Project Lead

Notes:

- Release accepted.
- The bounded Task Need Recognition canonical owner is proportionate and does
  not duplicate Chief Editor routing authority.
- Recognition remains evidence-first, qualitative, optional when immaterial,
  and explicitly advisory.
- Chief Editor retains every task type, route, preflight, risk/depth,
  capability/Domain Pack activation, decomposition, planning, next-action, and
  governance decision.
- Risk/consequence is explicit without a score, threshold, severity scale, new
  risk mode, or automatic selection.
- No automatic routing, activation, review/research selection, task splitting,
  planning, lifecycle transition, or approval was introduced.
- No new role, pipeline, lifecycle stage, review gate, task status, store,
  dashboard, or mandatory artifact was introduced.
- Independent review approved the bounded repair; repository and memory
  validation passed.
- S5.R5 remains `Not Started` and must not start automatically.
