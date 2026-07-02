# Task Manifest

## task identity

- Task ID: TASK-STUDIO-AUDIT-FRAMEWORK
- Task title: Studio Audit Framework for AI Software Studio
- Task type: methodology / knowledge content
- Owner/current role: chief_editor
- Created: 2026-07-02
- Last updated: 2026-07-02

## current state

- Current status: finalized
- Selected pipeline: article_pipeline
- Risk mode: high-governance
- Process depth: full
- Execution profile: expanded
- Client profile: none
- Client profile status: not_applicable
- Current working artifact: final.md
- Latest relevant handoff: handoff-review-review-agent-to-final-editor.md
- Next required action: deliver summary to user

## freshness

- Last verified: 2026-07-02
- Verified by: chief_editor
- Stale if: source KB changes, task scope changes, or framework artifact set changes

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: planned Studio Audit Framework document package in this task folder
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: brief.md, this manifest, status.md, orchestration_plan.md, sources.md, research.md, claims_table.md, current framework artifacts
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: review.md
- Review outcome: approved
- Compact finalization shape allowed: no
- Human approval required: unknown for delivery, not required for drafting methodology
- Human approval evidence: none
- Final decision artifact: final_decision.md

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | User task normalized and constraints recorded |
| `task-manifest.md` | yes | required | Current restart pointer |
| `status.md` | yes | required | Current state and history |
| `orchestration_plan.md` | yes | required | Routing, scope, role, and evidence contract |
| `sources.md` | yes | required | KB source inventory |
| `research.md` | yes | required | KB-grounded evidence synthesis and gaps |
| `facts.md` | no | conditional | Required if fact-level extraction improves reviewability |
| `claims_table.md` | yes | required | Draft criterion-to-KB traceability |
| Framework documents | yes | required | Draft package in `framework/` |
| `review.md` | yes | required | Independent review approved |
| `final.md` | yes | required | Delivery index/pack after approved review |
| `final_decision.md` | yes | required | Chief Editor final governance decision |

## stale or conflicting state

- None.

## active constraints

- User constraints: Framework only; no audit; no evaluation of current Studio; no BRD; no process changes; no Codex tasks; all criteria grounded in KB.
- Pipeline constraints: research separated from writing; Writer cannot self-review; review required before finalization.
- Client-profile constraints: none.
- Governance constraints: high traceability from each criterion to KB; insufficient KB must be stated explicitly.

## open questions

- None blocking. The exact file split may be refined during writing while preserving required deliverables.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `status.md`;
- `ai-editorial-office/pipelines/article_pipeline.md`;
- `ai-editorial-office/pipelines/research_pipeline.md`;
- `ai-editorial-office/kb/ai-software-studio-knowledge-base/index.md`;
- KB records directly referenced by research artifacts.

Next action:

- Role: chief_editor
- Action: deliver concise summary and file list to user.
- Expected output: final response with created files, structure, models, KB records, gaps, first-audit guidance, and review outcome.
- Stop conditions: KB is inaccessible, criteria cannot be traced to KB, or task drifts into auditing the current Studio.

## lifecycle notes

- Legacy task folders consulted: no
- Old artifact versions consulted: no
- Safe-to-ignore material: non-KB project history unless needed for editorial process compliance
