# Evidence Register

Task: `TASK-STUDIO-FIRST-AUDIT`
Date: 2026-07-02
Audit basis: approved Studio Audit Framework from `TASK-STUDIO-AUDIT-FRAMEWORK`

This register records admissible evidence used by the first independent Studio Audit. It does not modify or reinterpret the Framework or Knowledge Base.

## Evidence Items

| ID | Evidence | Source and locator | Evidence type | Confidence | Used for |
|---|---|---|---|---|---|
| E01 | Studio purpose, repository-first structure, canonical ownership map, rule placement discipline. | `ai-editorial-office/AGENTS.md`: lines 5-13, 17-24, 34-63 | Canonical governance document | High | GOV, KNO, ARC |
| E02 | Studio invariants, Chief Editor entry discipline, EDF, role activation and no production action before routing. | `ai-editorial-office/AGENTS.md`: lines 65-133 | Canonical governance document | High | GOV, QUA |
| E03 | Active role set and constraints on unauthorized role extension. | `ai-editorial-office/AGENTS.md`: lines 140-160, 243-266 | Canonical governance document | High | GOV, PLA, PRO |
| E04 | Default workflow, risk modes, process depth rules, execution profiles, controlled stages, handoff protocol, manifest discipline, artifact minimalism. | `ai-editorial-office/AGENTS.md`: lines 485-820 | Canonical governance document | High | GOV, QUA, DEL, ARC |
| E05 | Current project state, completed governance layer, active roles, canonical files, known normalization decisions, future extensions. | `ai-editorial-office/project-state.md`: lines 3-20, 22-48, 53-107, 112-118 | Project state record | Medium-high | GOV, KNO, PRO, ARC |
| E06 | Status taxonomy, valid transitions, direct writing-to-review rule, transition update requirements, blocked state rules, review outcome rules. | `ai-editorial-office/kb/task_statuses.md`: lines 19-148 | Canonical lifecycle KB record | High | GOV, QUA, DEL |
| E07 | Active role specifications exist for `chief_editor`, `research_agent`, `writer_agent`, `ux_writer`, `review_agent`, `final_editor`, `intake_agent`, `artist_agent`; each includes mission, responsibilities, inputs, outputs, forbidden actions and quality checks. | `ai-editorial-office/agents/*.md`; heading scan performed during audit | Role specifications | Medium-high | GOV, PLA, QUA |
| E08 | Pipeline specifications exist for article, research, review, social and UX writing workflows, including purpose, required agents, artifacts, stages, transitions, risk and review requirements. | `ai-editorial-office/pipelines/*.md`; heading scan performed during audit | Process specifications | Medium-high | GOV, DEL, PLA, QUA |
| E09 | Artifact and task templates exist for manifests, status, handoffs, reviews, final decisions, source notes, visual briefs, system change proposals and pipeline-specific tasks. | `ai-editorial-office/templates/**`; inventory scan performed during audit | Template inventory | Medium-high | GOV, QUA, DEL, PLA |
| E10 | Lifecycle validator and memory package checker are documented as read-only checks. | `ai-editorial-office/scripts/README.md`: lines 21-90; `ai-editorial-office/scripts/validate_task_lifecycle.py`: lines 1-6, 15-37, 166-297; `ai-editorial-office/scripts/check_about_memory_package.sh`: lines 4-41 | Tooling evidence | High | QUA, DEL, KNO |
| E11 | Lifecycle validator smoke tests pass. | Command: `bash ai-editorial-office/tests/test_task_lifecycle_validator.sh`; output: all validator smoke tests passed | Test run | High | QUA, DEL |
| E12 | Framework task lifecycle validation passes. | Command: `python3 ai-editorial-office/scripts/validate_task_lifecycle.py ai-editorial-office/tasks/TASK-STUDIO-AUDIT-FRAMEWORK`; output: PASS, 0 blockers, 0 warnings | Tool run | High | GOV, QUA |
| E13 | `TASK-CARE-PR-STRATEGY` lifecycle validation passes. | Command: `python3 ai-editorial-office/scripts/validate_task_lifecycle.py ai-editorial-office/tasks/TASK-CARE-PR-STRATEGY`; output: PASS, 0 blockers, 0 warnings | Tool run | High | GOV, QUA |
| E14 | `TASK-KB-WORKING-MEMORY` lifecycle validation fails due to pipeline mapping, review outcome parsing and final-without-recognized-review result. | Command: `python3 ai-editorial-office/scripts/validate_task_lifecycle.py ai-editorial-office/tasks/TASK-KB-WORKING-MEMORY`; output: FAIL, 3 blockers, 1 warning | Tool run | High | GOV, QUA, KNO |
| E15 | `/about` memory package check fails because root `/about` is absent. | Command: `sh ai-editorial-office/scripts/check_about_memory_package.sh`; output: `find: .../about: No such file or directory`; `FAIL: /about contains 0 files; expected 20.` | Tool run | High | KNO |
| E16 | KB index defines purpose, structure, record types, durability, 55-record set and governance notes. | `ai-editorial-office/kb/ai-software-studio-knowledge-base/index.md`: lines 3-84 | Knowledge Base index | High | KNO, all areas |
| E17 | KB application register shows 55 records: 36 Accepted, 14 Applied, 4 Under Evaluation, 1 Rejected. | `ai-editorial-office/kb/ai-software-studio-knowledge-base/application-register.md`: lines 13-114 | KB implementation register | High | KNO, MET, PLA |
| E18 | KB coverage model defines dimensions, coverage snapshot, validation snapshot, applied-by-Studio-object view, review triggers and coverage rules. | `ai-editorial-office/kb/ai-software-studio-knowledge-base/coverage-model.md`: lines 7-91 | KB coverage model | High | KNO, MET |
| E19 | Studio object map identifies canonical and missing/not-yet-available Studio objects, including BRD, BRD Governance, Historian, Product Analyst and Validator as not yet available. | `ai-editorial-office/kb/ai-software-studio-knowledge-base/studio-object-map.md`: lines 13-91 | KB object mapping | High | PRO, GOV, KNO |
| E20 | KB schema and lifecycle define required record fields, confidence/refresh fields, lifecycle statuses and `not_yet_available` object-link discipline. | `ai-editorial-office/kb/ai-software-studio-knowledge-base/schema.md`: lines 6-124; `lifecycle.md`: lines 13-66 | KB schema/governance | High | KNO, GOV |
| E21 | KB development recommendations state BRD Governance, Product Analyst, Validator and Historian are not canonical and are future development references. | `ai-editorial-office/kb/ai-software-studio-knowledge-base/development-recommendations.md`: lines 13-95 | KB gap record | High | PRO, GOV, ARC |
| E22 | `TASK-KB-WORKING-MEMORY` contains finalized status, approved review, artifact inventory and explicit open question on missing BRD Governance/Historian files. | `ai-editorial-office/tasks/TASK-KB-WORKING-MEMORY/status.md`, `task-manifest.md`, `review.md`; sampled line ranges recorded during audit | Task artifact sample | Medium-high | KNO, GOV, QUA |
| E23 | `TASK-CARE-PR-STRATEGY` contains high-governance execution, role separation, approved review, claim traceability and final governance boundary. | `ai-editorial-office/tasks/TASK-CARE-PR-STRATEGY/task-manifest.md`, `review.md`, `final_decision.md`; sampled line ranges recorded during audit | Task artifact sample | Medium-high | GOV, QUA, DEL |
| E24 | Framework task review and final decision confirm methodology approval, independence, 38 criteria, report/evidence models and no audit results inside Framework. | `ai-editorial-office/tasks/TASK-STUDIO-AUDIT-FRAMEWORK/review.md`, `final_decision.md`; sampled line ranges recorded during audit | Framework approval evidence | High | GOV, all areas |
| E25 | Repository root has no `/about` directory at audit time. | Command: `find . -maxdepth 2 -type d`; observed directory inventory excludes `./about` | Repository inventory | High | KNO |

## Evidence Sufficiency Notes

- Evidence is strongest for governance, knowledge-base structure, editorial lifecycle, review gates and artifact traceability.
- Evidence is mixed for operational consistency because automated lifecycle checks pass for some finalized tasks and fail for one finalized high-governance KB task.
- Evidence is limited for AI evaluation, security control implementation, delivery reliability, product discovery, platform operations, metrics and architecture review because the KB mostly marks those records as Accepted or Under Evaluation rather than Applied.
- Command outputs are used only as audit observations and were not used to alter Studio files outside this audit task.
