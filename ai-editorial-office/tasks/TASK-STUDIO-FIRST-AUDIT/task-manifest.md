# Task Manifest

## task identity

- Task ID: TASK-STUDIO-FIRST-AUDIT
- Task title: First Independent Studio Audit
- Task type: audit report / high-governance analysis
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
- Next required action: none

## freshness

- Last verified: 2026-07-02
- Verified by: chief_editor
- Stale if: Framework, KB, AGENTS.md, project-state, role specs, pipelines, templates, scripts, or task artifacts change materially.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: finalized audit package in this task folder
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: final.md, final_decision.md, review-packet.md, audit-report/studio-audit-report.md, evidence-register.md, criterion-scorecard.md, kb-implementation-map.md
- Old versions read only for: evidence sampling / governance traceability
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: review.md
- Review outcome: approved
- Compact finalization shape allowed: no
- Human approval required: unknown after delivery
- Human approval evidence: none
- Final decision artifact: final_decision.md

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | User task and constraints |
| `task-manifest.md` | yes | required | Restart pointer |
| `status.md` | yes | required | State history |
| `orchestration_plan.md` | yes | required | Audit execution contract |
| `evidence-register.md` | yes | required | Evidence IDs and confidence |
| `criterion-scorecard.md` | yes | required | Criterion-level scoring |
| `kb-implementation-map.md` | yes | required | KB implementation status |
| `audit-report/` package | yes | required | Official audit report and annexes |
| `review-packet.md` | yes | required | User-requested verification packet |
| `review.md` | yes | required | Independent review |
| `finalization-notes.md` | yes | conditional | Finalization notes |
| `finalization-checklist.md` | yes | conditional | Finalization checklist |
| `final.md` | yes | required | Final delivery index |
| `final_decision.md` | yes | required | Chief Editor final governance |

## stale or conflicting state

- None.

## active constraints

- User constraints: audit only; no fixes; no Framework or KB changes; no BRD;
  no roadmap; no Codex tasks; no implementation recommendations.
- Pipeline constraints: research separated from writing; independent review
  before finalization.
- Framework constraints: use existing Framework strictly; report gaps in
  Framework/KB as observations only.
- Governance constraints: evidence-backed findings and confidence levels.

## open questions

- None blocking. Evidence limitations are recorded in the report.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- `project-state.md`;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- approved Studio Audit Framework;
- KB model files;
- current evidence artifacts.

Next action:

- Role: none
- Action: none.
- Expected output: complete.
- Stop conditions: any attempt to modify Framework/KB or produce implementation plan.

## lifecycle notes

- Legacy task folders consulted: yes, as audit evidence samples only.
- Old artifact versions consulted: only when evidence sampling or governance traceability needs it.
- Safe-to-ignore material: unrelated `.DS_Store`, generated pyc, non-markdown binary files unless relevant to evidence.
