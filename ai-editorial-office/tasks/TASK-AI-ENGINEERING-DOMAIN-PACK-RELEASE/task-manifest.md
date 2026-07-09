# Task Manifest

## task identity

- Task ID: `TASK-AI-ENGINEERING-DOMAIN-PACK-RELEASE`
- Task title: AI Engineering Domain Pack Release
- Task type: source-backed domain-pack release / canonical documentation change
- Owner/current role: `chief_editor`
- Created: 2026-07-10
- Last updated: 2026-07-10

## current state

- Current status: `finalized`
- Selected pipeline: `research`
- Risk mode: `high-governance`
- Process depth: `full`
- Execution profile: `expanded`
- Client profile: `none`
- Client profile status: `not_applicable`
- Current working artifact: `final_decision.md`
- Latest relevant handoff: `handoff-finalization-final-editor-to-chief-editor.md`
- Next required action: create the final release commit excluding unrelated
  `diff_intake.md`, then hand back the RC and commit hash to the user.

## active domain context

- Domain Knowledge Pack Standard: active as the canonical release standard.
- Software Architecture Domain Pack: active for adjacent-domain and architecture
  boundary synthesis.
- Cybersecurity Domain Pack: active for defensive AI safety, misuse, and
  escalation boundaries.
- DevSecOps Domain Pack: active for delivery, runtime, data/secret, and
  operational workflow handoff boundaries.
- Candidate AI Engineering Domain Pack: not active as canon until reviewed and
  accepted; task-specific research supplies the new domain context.
- Confidence: `verified` for repository canon; external claims require current
  authoritative sources and claim-level traceability.
- Stale/stop condition: stop if a material claim lacks inspectable source
  support, if boundary ownership conflicts with canon, or if pack content
  becomes operational misuse guidance.

## current version pointers

- Canonical pointer owner: this manifest
- Current active artifact set: all files marked current in the inventory below
- Replaces: none
- Deprecated/previous versions: none
- Versions no longer working artifacts: none
- Version conflict state: none
- What to read on restart: this manifest, round 1 `review.md`, `status.md`, the
  current working artifact, and only the standard/template files named in the
  next action packet
- Old versions read only for: comparison or reviewer/governance traceability
- Do not use latest modified as source of truth: yes

## governance state

- Review required: yes
- Review artifact/current version: `review.md`, round 2
- Review outcome: `approved`
- Compact finalization shape allowed: no
- Human approval required: yes, Project Lead acceptance after Release Candidate
- Human approval evidence: not yet applicable
- Final decision artifact: `final_decision.md`

## artifact inventory

| Artifact | Current? | Required / conditional / optional | Notes |
| --- | --- | --- | --- |
| `brief.md` | yes | required | User mission normalized |
| `task-manifest.md` | yes | required | Current task pointer |
| `status.md` | yes | required | Transition history |
| `orchestration_plan.md` | yes | required | Expanded execution contract |
| `handoff-orchestration-chief-editor-to-research-agent.md` | yes | required | Research assignment |
| `research.md` | yes | required | Task-local research synthesis |
| `sources.md` | yes | required | Full-evidence source register |
| `facts.md` | yes | required | Extracted usable facts |
| `claims_table.md` | yes | required | Claim-level traceability |
| `../../research/ai_engineering_pack_landscape.md` | yes | required | Release research |
| `handoff-research-research-agent-to-chief-editor.md` | yes | required | Research sufficiency transfer |
| `../../research/ai_engineering_pack_architecture_synthesis.md` | yes | required | Architecture synthesis |
| `handoff-architecture-chief-editor-to-writer-agent.md` | yes | required | Bounded writing contract |
| `../../kb/ai_engineering_domain_pack.md` | yes | required | Canonical candidate pack |
| `claims-used.md` | yes | required | Published claim traceability |
| `../../research/ai_engineering_pack_release_report.md` | yes | required | Release/validation report |
| `../../releases/S4-R5/release-pack.md` | yes | required | Project Lead review packet |
| `handoff-release-writer-agent-to-review-agent.md` | yes | required | Independent review assignment |
| `review.md` | yes | required | Round 1 changes requested; bounded re-review pending |
| `handoff-repair-writer-agent-to-review-agent.md` | yes | required | Bounded re-review assignment |
| `final.md` | yes | required | Finalized release-candidate summary |
| `handoff-finalization-final-editor-to-chief-editor.md` | yes | required | Final governance assignment |
| `final_decision.md` | yes | required | Chief Editor RC governance decision |

## stale or conflicting state

- Current release state is synchronized to S4.R5 Review / Release Candidate in
  `BACKLOG.md`, `ROADMAP.md`, canonical `project-state.md`, and the current
  release packet.
- Round 1 review identified stale task-local restart pointers; this manifest is
  the repaired current pointer. Historical S4.R4 mismatch notes remain only in
  status/review history.

## active constraints

- User constraints: complete S4.R5 to Release Candidate; do not stop at an
  intermediate milestone; do not touch the legacy/private archive.
- Pipeline constraints: research is separate from writing; full evidence and
  independent review are mandatory.
- Client-profile constraints: none.
- Governance constraints: no new roles, pipelines, capabilities, lifecycle
  stages, gates, policy owners, approval workflows, or mandatory artifacts.

## open questions

- None blocking. `/about` synchronization is complete and its copied
  `project-state.md` is byte-aligned with canon.

## next action packet

Minimum restart read set:

- `AGENTS.md` or invariant summary;
- this manifest;
- `review.md`, especially Required Changes And Re-review Scope;
- this manifest and `status.md`;
- `../../kb/ai_engineering_domain_pack.md`;
- `../../research/ai_engineering_pack_release_report.md`;
- `../../releases/S4-R5/release-pack.md`;
- `../../kb/domain_knowledge_pack_standard.md` and
  `../../templates/release-pack.md`.

Next action:

- Role: `chief_editor`
- Action: create the final release commit excluding unrelated
  `diff_intake.md`, then hand back the RC and hash.
- Expected output: committed Release Candidate ready for Project Lead review.
- Stop conditions: source insufficiency, unresolved contradiction affecting a
  linchpin claim, unsafe detail, or canon-boundary conflict.

## lifecycle notes

- Legacy task folders consulted: current S4.R3/S4.R4 release artifacts were
  consulted only as release-packet precedent, not as authority.
- Old artifact versions consulted: no.
- Safe-to-ignore material: unrelated root-level `diff_intake.md`.
