# Task Manifest

## task identity

- Task ID: `GLOBAL_RESEARCH_INTELLIGENT_PRODUCTION_SYSTEMS`
- Task title: Global Research: Intelligent Production Systems and AI Software Studio Knowledge Base
- Task type: high-governance research plus knowledge-base creation
- Owner/current role: `chief_editor`
- Created: 2026-07-02
- Last updated: 2026-07-02

## current state

- Current status: `finalized`
- Selected pipeline: `/pipelines/research_pipeline.md` with downstream writing, review, finalization, and Chief Editor governance
- Risk mode: `high-governance`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: finalized research package and permanent KB v1
- Latest relevant handoff: `handoff-final-editor-to-chief-editor.md`
- Next required action: report completion to user

## freshness

- Last verified: 2026-07-02
- Verified by: `chief_editor`
- Stale if: research scope, source corpus, or KB output path changes; source freshness becomes material; review outcome changes.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: research artifacts and KB v1 in this task and `/kb/ai-software-studio-knowledge-base/`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, this manifest, latest handoff, `orchestration_plan.md`, `status.md`, current research or KB artifact, and directly relevant pipeline/KB files.
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: no
- Human approval required: no for local artifact creation; yes for any later publication or adoption as Studio policy.
- Human approval evidence: not applicable for this task's local research output.
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | User request normalized without changing scope. |
| `task-manifest.md` | yes | required | Current task control panel. |
| `status.md` | yes | required | State and transition history. |
| `orchestration_plan.md` | yes | required | High-governance route and artifact contract. |
| `handoff-orchestration-chief-editor-to-research-agent.md` | yes | required | Role transition to research. |
| `research.md` | yes | required | Research synthesis and contradictions. |
| `sources.md` | yes | required | Annotated source traceability. |
| `facts.md` | yes | required | Extracted facts and interpretations. |
| `claims_table.md` | yes | required | Claim-level traceability and draft-use guidance. |
| `handoff-research-research-agent-to-writer-agent.md` | yes | required | Role transition to writing and KB construction. |
| `executive-summary.md` | yes | required | Research artifact requested by user. |
| `research-map.md` | yes | required | Research directions map. |
| `annotated-sources.md` | yes | required | Source annotation requested by user. |
| `trends.md` | yes | required | Trends and durability assessment. |
| `best-practices.md` | yes | required | Practices and patterns. |
| `anti-patterns.md` | yes | required | Anti-patterns. |
| `knowledge-extraction-report.md` | yes | required | Extraction logic and links. |
| `/kb/ai-software-studio-knowledge-base/` | yes | required | Permanent KB v1. |
| `claims-used.md` | yes | required | Claims used in draft/final artifacts. |
| `handoff-writing-writer-agent-to-review-agent.md` | yes | required | Role transition to independent review. |
| `review.md` | yes | required | Independent review before finalization; outcome approved. |
| `handoff-review-review-agent-to-final-editor.md` | yes | required | Role transition to finalization. |
| `created-files.md` | yes | required | Complete file list for delivery review. |
| `final.md` | yes | required after approved review | Final delivery pointer and summary. |
| `handoff-final-editor-to-chief-editor.md` | yes | required | Role transition to final governance decision. |
| `final_decision.md` | yes | required | Chief Editor final governance decision; task finalized. |

## stale or conflicting state

- None.

## active constraints

- User constraints: produce only research, Knowledge Base, and materials needed for later stages; do not audit or improve current Studio processes.
- Pipeline constraints: full evidence set required; research separate from writing; review required before finalization.
- Client-profile constraints: none.
- Governance constraints: no publication, adoption, or policy change is approved by this task.

## open questions

- None blocking. The source corpus is bounded by available public sources and will be marked as v1, not exhaustive.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `handoff-final-editor-to-chief-editor.md`;
- `final.md`, `final_decision.md`, `knowledge-extraction-report.md`, and the permanent KB index;
- `/pipelines/research_pipeline.md`;
- `/pipelines/review_pipeline.md`;
- `/kb/research_evidence.md`.

Next action:

- Role: `chief_editor`
- Action: report finalized artifact locations and key outputs to the user.
- Expected output: concise user-facing completion report.
- Stop conditions: none for this finalized task; any new audit, redesign, or implementation request must start a new scoped task.

## lifecycle notes

- Legacy task folders consulted: no; not needed for this new research task.
- Old artifact versions consulted: no; none exist.
- Safe-to-ignore material: existing unrelated modified files in the worktree.
