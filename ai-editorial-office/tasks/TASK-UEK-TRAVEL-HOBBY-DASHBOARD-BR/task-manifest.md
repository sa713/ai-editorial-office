# Task Manifest

## task identity

- Task ID: TASK-UEK-TRAVEL-HOBBY-DASHBOARD-BR
- Task title: БТ к дашборду "Путешествия и хобби сотрудников УЭК"
- Task type: business requirements / article-style knowledge document
- Owner/current role: chief_editor
- Created: 2026-06-08
- Last updated: 2026-06-08

## current state

- Current status: finalized
- Selected pipeline: article_pipeline
- Risk mode: low-risk
- Process depth: compact
- Execution profile: `compact`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `business_requirements.md`
- Latest relevant handoff: not created; compact execution records role routing in this manifest, `status.md`, `orchestration_plan.md`, and `review.md`
- Next required action: user review of prepared task artifacts

## freshness

- Last verified: 2026-06-08
- Verified by: chief_editor
- Stale if: source requirements or project governance rules change

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact or artifact set: `business_requirements.md`, `review.md`, `final_decision.md`
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: `brief.md`, this manifest, `orchestration_plan.md`, `business_requirements.md`, `review.md`, `final_decision.md`
- Old versions read only for: not applicable
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`
- Review outcome: approved
- Compact finalization shape allowed: yes
- Human approval required: no
- Human approval evidence: not applicable
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | Normalized task brief |
| `task-manifest.md` | yes | required | Restart anchor |
| `status.md` | yes | required | State and transition record |
| `orchestration_plan.md` | yes | required | Routing, compact process, role assignment |
| `business_requirements.md` | yes | required | Main deliverable |
| `draft.md` | yes | required by selected pipeline | Pointer to the main draft artifact |
| `review.md` | yes | required | Independent review gate |
| `final_decision.md` | yes | conditional | Chief Editor governance decision after approved review |

## stale or conflicting state

- None.

## active constraints

- User constraints: prepare Russian product-style BТ as user stories with Given / When / Then acceptance criteria; do not add technical architecture, API, DB schema, UX copy, layouts, plans, estimates, MVP/Phase split, or priorities.
- Pipeline constraints: review required before final governance; role separation preserved.
- Client-profile constraints: none.
- Governance constraints: `AGENTS.md` canonical; no changes to roles, review-gate, pipelines, or production files.

## open questions

- Product open questions are recorded in `business_requirements.md`.

## next action packet

Minimum restart read set:

- `ai-editorial-office/AGENTS.md`;
- this manifest;
- `brief.md`;
- `orchestration_plan.md`;
- `business_requirements.md`;
- `review.md`;
- `final_decision.md`.

Next action:

- Role: user / chief_editor
- Action: review prepared artifacts and decide whether additional product clarifications are needed
- Expected output: acceptance, comments, or new follow-up task
- Stop conditions: conflicting user changes or request to alter editorial governance

## lifecycle notes

- Legacy task folders consulted: no; no existing `/tasks` folder was present under `ai-editorial-office`
- Old artifact versions consulted: no
- Safe-to-ignore material: none
