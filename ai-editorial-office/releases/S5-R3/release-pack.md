# Release Pack

Release readiness rule: no release is considered ready for Project Lead review
until a completed `release-pack.md` exists.

## Release

- Release ID: `S5.R3`
- Release title: Memory Hygiene Intelligence
- Status: release candidate ready after independent approval, controlled
  finalization, final staged validation, and local commit; Project Lead review
  pending
- Date: 2026-07-10

## Executive Summary

S5.R3 adds a source-first, manual, reviewable disposition contract for external
project memory inside existing Knowledge Evolution ownership. It distinguishes
mapped exact copies from compact summaries and makes sync, no-sync, correction,
compression, omission, deferral, retirement, validation, and review explicit
without creating a second memory system or allowing `/about`, checkers,
Evaluation Signals, or automation to override repository canon or write memory.

## Architectural Impact

Architecture impact:

- Small

Reason:

The release refines existing Editorial Learning, Memory Curation, stale-
knowledge, Integrity Checking, Chief Editor, Review Agent, and Review Pipeline
behavior. It adds no owner, capability, role, pipeline, lifecycle stage, review
gate, task status, store, score, mandatory artifact, or automation authority.

## Goal Of The Release

Keep external project memory accurate, compact, useful, synchronized, and free
from stale, duplicated, temporary, sensitive, or misleading state while
preserving repository canon as the only authority.

## Architecture Decisions

- Decision: implement Memory Hygiene Intelligence as a bounded refinement of
  the existing Editorial Learning Framework and current Memory Curation,
  stale-knowledge, and Integrity Checking capabilities.
- Rationale: the system already owns source evidence, learning disposition,
  stale/contradictory repair, memory curation, review, and checks; only a precise
  external-memory disposition and validation contract was missing.
- Architecture preserved: yes; `/about` remains a derived 20-file package and
  every write remains explicit, manual, source-backed, and reviewed.

## Capability Decisions

- Capability shape: no new capability; existing Knowledge Evolution and Memory
  Curation behavior refined.
- Activation: only after a material canonical change or saved memory-hygiene
  signal, followed by source/purpose/sensitivity/value judgment.
- Review: existing Review Agent checks source fidelity, exact-copy versus
  summary semantics, privacy, omission, consolidation/retirement context,
  bounded growth, validation, and non-automation inside the existing gate.
- Non-goals: automatic synchronization, full repository mirror, per-commit
  sync, new memory store/owner, completeness scoring, automatic canon/state/
  acceptance changes, or unreviewed propagation.

## Scope

### Implemented

- Source-first memory-hygiene flow and sync/no-sync triggers.
- Eight dispositions: exact-copy, compact-summary, correct, compress, retire,
  omit, defer, and no-sync.
- Exact-copy byte validation and compact-summary semantic review distinction.
- Stale/contradictory repair with canonical-owner precedence.
- Duplicate consolidation, context-preserving compression, and retirement.
- Sensitive, task-local, raw, temporary, and repository-only omission.
- Conditional disposition auditability in existing governance artifacts.
- Existing-role and advisory-check boundaries.
- Ten representative scenarios.
- S5.R2 accepted/S5.R3 Review state normalization.
- Four exact-copy and three compact-summary `/about` updates with no new file.

### Merged

- External-memory disposition into existing Knowledge Evolution ownership.
- Exact-copy/package checks into existing read-only Integrity Checking.
- Memory review into the existing Knowledge Evolution gate.
- Stale, duplicate, correction, supersession, and retirement behavior into the
  existing stale-knowledge path.

### Postponed

- Optional advisory linting for broken summary source pointers or likely drift,
  pending repeated evidence of value.
- Any reconsideration of package mapping or the fixed 20-file set.
- Real-use evaluation of whether S5.R3 reduces future drift and bloat.
- S5.R4 Task Need Recognition.

### Rejected

- New Memory Manager, capability, framework, governance layer, pipeline, stage,
  review gate, store, registry, or mandatory artifact.
- Automatic write, summary, correction, consolidation, omission, or retirement.
- Memory-driven canon change or override.
- Mandatory synchronization after every commit.
- Full repository export or mandatory inclusion of all project details.
- Memory health, completeness, growth, coverage, or quality score.
- Automatic propagation of raw feedback, task evidence, temporary RC state,
  private/sensitive content, or unreviewed material.

## Canonical Files Changed

- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/agents/review_agent.md`
- `ai-editorial-office/kb/00_index.md`
- `ai-editorial-office/kb/capability_registry.md`
- `ai-editorial-office/kb/editorial_learning_framework.md`
- `ai-editorial-office/pipelines/review_pipeline.md`
- `ai-editorial-office/project-state.md`

## Canonical Owners Updated

Updated canonical owners:

- Editorial Learning Framework: Memory Hygiene Intelligence contract.
- Capability Registry: existing Memory Curation and Integrity Checking only.
- Chief Editor: source/materiality/disposition authorization.
- Review Agent/Review Pipeline: fidelity, semantics, privacy, compactness,
  context preservation, validation, and non-automation challenge.
- Project State: current Release Candidate state only.

New canonical owners introduced:

- None

## Non-Canonical Files

- `ai-editorial-office/ROADMAP.md`
- `ai-editorial-office/BACKLOG.md`
- three S5.R3 research/release artifacts
- `ai-editorial-office/tests/memory_hygiene_intelligence_smoke_test.md`
- `ai-editorial-office/tests/README.md`
- `ai-editorial-office/releases/S5-R3/release-pack.md`
- `ai-editorial-office/tasks/TASK-MEMORY-HYGIENE-INTELLIGENCE-RELEASE/`
- `/about` exact copies and compact memory summaries

## Memory Disposition Model

| Disposition | Use | Validation |
| --- | --- | --- |
| exact-copy | mapped operational file | byte identity and package check |
| compact-summary | durable external orientation | semantic source comparison and review |
| correct | wrong/stale/contradictory fact | old claim absent; replacement faithful |
| compress | useful but verbose/duplicate content | unique meaning retained; repetition reduced |
| retire | obsolete/superseded/misleading content | active stale claim removed; repo history kept |
| omit | internal/raw/temporary/task-local/sensitive detail | detail absent; needed context retained |
| defer | source/evidence/approval unresolved | no speculative write; next verification visible |
| no-sync | no external-memory effect | current package remains accurate/sufficient |

## Evaluation Signals

| Decision question | Observation and evidence | Scope / comparison / missing cases | Interpretation, alternatives, and confidence | Existing owner | Project Lead consideration | Explicit non-decision |
| --- | --- | --- | --- | --- | --- | --- |
| Does S5.R3 fit the stable architecture? | Existing Learning/Memory Curation/Integrity Checking/role/review owners hold every action; ten scenarios and final validators pass. | S5.R3 contract and synthetic cases only; real future drift reduction is unknown. | Supported that no new owner/system is needed; real-use value remains unproven. | Editorial Learning Framework, Chief Editor, Review Agent, Project Lead | Review whether the bounded disposition model is usable and proportionate. | No automatic acceptance, memory/canon action, owner change, or S5.R4 start. |
| Does the release bound memory growth without erasing meaning? | Package remains 20 files; four mapped copies replaced, three summaries updated; omission/no-sync/compression/consolidation/retirement cases preserve repository history. | Current release and synthetic cases; no longitudinal package-size evidence. | Contract rejects accumulation and silent deletion; future application remains a human responsibility. | Chief Editor and Review Agent | Preserve continuing-value and context-preservation checks. | No size target, completeness score, automatic deletion, or retention action. |
| Is current release state represented accurately? | Accepted S5.R2 evidence and explicit S5.R3 mission support S5.R2 Done/S5.R3 Review; state and `/about` are updated. | Current repository state; S5.R3 acceptance is intentionally absent. | Verified current RC state; acceptance remains future Project Lead action. | Project State, Roadmap, Backlog, Project Lead | Proceed to architectural review. | S5.R3 is not Done; S5.R4 is not started. |

## Release Metrics

Canonical files changed: 7

Research artifacts: 3 required release artifacts plus task-local sources,
facts, and claim traceability

Templates: 0

Tests: 1 new ten-case manual smoke test; tests index updated; existing lifecycle
and task-pack suites run

Memory package updated: yes; 4 exact copies and 3 compact summaries; still 20
files

Validation scripts executed: 6 repository checks plus structured ten-case,
state, acceptance-boundary, and protected-scope checks

Commits: 1 local Release Candidate commit; hash reported in handback

## Validation Results

| Check | Result |
| --- | --- |
| `git diff --check` | passed |
| `git diff --cached --check` | passed on authorized staged scope |
| `sh ai-editorial-office/scripts/check_about_memory_package.sh` | passed; 20 files and mapped copies match |
| `sh ai-editorial-office/tests/test_task_lifecycle_validator.sh` | passed |
| `sh ai-editorial-office/tests/test_task_pack_generator.sh` | passed |
| direct S5.R3 task lifecycle validation | passed; 0 blockers, 0 warnings |
| ten representative scenarios | passed; 10 cases and 10 pass outcomes |

## Known Risks

- Summary semantic review remains judgment-based.
- Future release state can drift if maintainers ignore material triggers.
- The checker cannot prove summary meaning, privacy, deduplication, or value.
- Conditional no-sync recording trades complete audit logs for lower process
  weight.
- Synthetic cases do not prove real future usefulness or drift reduction.

## Open Questions

- None blocking independent review.

## Recommended Project Lead Decision

Accepted

or

Changes Requested

Recommended decision: Accepted.

## Suggested Next Release

- Do not start S5.R4 automatically. After S5.R3 review, Project Lead may decide
  whether `S5.R4 - Task Need Recognition` should open.

## Acceptance Checklist

- Architecture preserved
- Review gate unchanged
- No new roles
- No new pipelines
- No lifecycle changes
- Repository canon remains authoritative
- Exact-copy and compact-summary branches are distinct
- All eight dispositions are explicit
- Stale/contradictory memory can be repaired
- Duplicate/obsolete memory can be consolidated/retired without silent history deletion
- Sensitive/task-local content defaults to omission
- Evaluation Signals and checks remain advisory/read-only
- No automatic memory/canon changes
- No mandatory per-commit sync or memory score
- Ten scenarios pass
- Memory package remains 20 files
- Final staged validation passed
- Independent review approved with no open findings
- Local commit created; hash reported in handback
