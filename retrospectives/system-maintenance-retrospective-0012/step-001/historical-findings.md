# Historical / retrospective findings

## Summary

Historical mentions of `MVP` appear in old retrospectives, task artifacts, architecture reviews, diffs, and generated reports. These files explain how the system reached its current model, but they are not active policy under the Step 1 active-policy criteria.

The main historical narrative:

- early MVP role set was validated as coherent;
- TASK-0001 showed MVP success but high operational weight;
- later reviews identified the Artist Agent conflict with MVP-only wording;
- `system-maintenance-retrospective-0011-1` legalized Artist Agent as a bounded `non-MVP extension role`;
- later compression work preserved the MVP role set while reducing duplication.

## Historical mentions in retrospectives and task history

| File | Line | Exact formulation | Historical meaning |
| --- | ---: | --- | --- |
| `retrospectives/0001/iteration-plan-001/artifact-ownership-map.md` | 12 | `active MVP constraints` | Old ownership map for current system-state responsibilities. |
| `retrospectives/0001/iteration-plan-001/artifact-ownership-map.md` | 34 | `MVP role set;` | Historical planning term for role set. |
| `retrospectives/0001/architecture-review-001/system-strengths.md` | 13 | `В MVP есть канонические роли:` | Earlier architecture review validates canonical roles. |
| `retrospectives/0001/architecture-review-001/system-strengths.md` | 158 | `отдельному Editor Agent в MVP;` | Historical argument against separate Editor Agent. |
| `retrospectives/0001/architecture-review-001/system-strengths.md` | 162 | `single-agent or minimal-agent MVP first...` | General architecture principle, not active policy. |
| `retrospectives/0001/architecture-review-001/proposed-improvements.md` | 427 | `Сохранить MVP role set...` | Old recommendation to keep role set. |
| `retrospectives/0001/architecture-review-001/raw-findings.md` | 34 | `The current MVP agent set is sensible.` | Old raw finding. |
| `retrospectives/0001/architecture-review-001/context-and-memory-review.md` | 215 | `MVP workflow` | Old finding about duplicated workflow wording. |
| `retrospectives/0001/implementation-step-001/implementation-plan.md` | 17 | `active MVP agents` | Old implementation safety note. |
| `retrospectives/0001/implementation-step-002/diff.md` | 97 | `not automatic in the current MVP;` | Historical diff text. |
| `retrospectives/0001/implementation-step-002/diff.md` | 113 | `not automatic in the current MVP.` | Historical diff text. |
| `retrospectives/0001/implementation-step-005/diff.md` | 99 | `handoff exists to the correct next MVP role;` | Historical diff text from earlier pipeline contract. |
| `retrospectives/0001/iteration-spec-001/target-files.md` | 16 | `active MVP constraints` | Old iteration target note. |
| `retrospectives/TASK-0001-retrospective.md` | 7 | `real MVP success` | Historical task evaluation. |
| `retrospectives/TASK-0001-retrospective.md` | 58 | `The MVP role model is stable enough...` | Historical validation of role model. |
| `retrospectives/TASK-0001-retrospective.md` | 64 | `MVP has no separate Editor Agent` | Historical diagnosis of status/role friction. |
| `retrospectives/TASK-0001-retrospective.md` | 96 | `For MVP validation...` | Historical throughput assessment. |
| `retrospectives/TASK-0001-retrospective.md` | 118 | `independent enough for MVP` | Historical review assessment. |
| `retrospectives/TASK-0001-retrospective.md` | 163 | `For MVP validation...` | Historical scaling assessment. |
| `retrospectives/TASK-0001-retrospective.md` | 193 | `for MVP article tasks` | Historical recommendation on status model. |
| `retrospectives/TASK-0001-retrospective.md` | 249 | `Do not add new MVP roles yet.` | Historical recommendation against new roles. |
| `retrospectives/TASK-0001-retrospective.md` | 257 | `## MVP readiness assessment` | Historical readiness section. |
| `retrospectives/TASK-0001-retrospective.md` | 259 | `MVP readiness...` | Historical readiness finding. |
| `retrospectives/TASK-0001-retrospective.md` | 263 | `The MVP is operationally coherent...` | Historical assessment. |
| `ai-editorial-office/tasks/TASK-0001/orchestration_plan.md` | 71 | `Only MVP roles may be used...` | Old task plan; not active after Artist Agent legalization. |
| `ai-editorial-office/tasks/TASK-0001/orchestration_plan.md` | 72 | `There is no separate active Editor Agent in MVP.` | Old task-specific rule. |
| `ai-editorial-office/tasks/TASK-0001/orchestration_plan.md` | 135 | `No non-MVP agents may be introduced.` | Old task-specific strict rule, superseded by extension logic. |
| `ai-editorial-office/tasks/TASK-0001/orchestration_plan.md` | 181 | `non-MVP editing role` | Old task-specific artifact/role warning. |
| `ai-editorial-office/tasks/TASK-0001/orchestration_plan.md` | 309 | `a non-MVP role is requested;` | Old escalation condition. |
| `ai-editorial-office/tasks/TASK-0001/handoff-research-research-agent-to-chief-editor.md` | 136 | `No non-MVP Editor Agent exists.` | Old handoff note. |
| `ai-editorial-office/tasks/TASK-0001/handoff-intake-intake-agent-to-chief-editor.md` | 208 | `MVP roles are assigned...` | Old task handoff. |
| `ai-editorial-office/tasks/TASK-0001/handoff-planning-chief-editor-to-research-agent.md` | 254 | `next valid MVP role` | Old handoff validity note. |
| `ai-editorial-office/tasks/TASK-0001/handoff-planning-chief-editor-to-writer-agent.md` | 60 | `next valid MVP role` | Old handoff validity note. |
| `ai-editorial-office/tasks/TASK-0001/handoff-planning-chief-editor-to-writer-agent.md` | 133 | `No separate Editor Agent exists in MVP.` | Old task note. |
| `ai-editorial-office/tasks/TASK-0001/handoff-planning-chief-editor-to-writer-agent.md` | 301 | `next valid MVP role` | Old handoff validity note. |
| `ai-editorial-office/tasks/TASK-0001/final_decision.md` | 17 | `MVP validation run` | Historical closure. |
| `ai-editorial-office/tasks/TASK-0001/final_decision.md` | 120 | `successful MVP validation` | Historical classification. |
| `ai-editorial-office/tasks/TASK-0001/final_decision.md` | 130 | `successful MVP validation... not proof of production readiness` | Historical conclusion. |
| `ai-editorial-office/tasks/TASK-0001/status.md` | 37 | `MVP validation run` | Historical status. |
| `ai-editorial-office/tasks/TASK-0001/status.md` | 68 | `successful MVP validation` | Historical status row. |
| `ai-editorial-office/tasks/TASK-0001/status.md` | 138 | `successful MVP validation` | Historical classification. |
| `ai-editorial-office/tasks/TASK-0002/retrospective.md` | 5 | `стабилизированная MVP-редакция` | Historical TASK-0002 conclusion. |
| `ai-editorial-office/tasks/TASK-0002/retrospective.md` | 140 | `Оставить MVP role set без изменений.` | Historical recommendation. |
| `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0002/status.md` | 30 | `MVP role separation unchanged.` | Historical system-update status. |
| `retrospectives/architecture-review-002/optimization-opportunities.md` | 18 | `MVP role set` | Historical optimization target. |
| `retrospectives/architecture-review-002/optimization-opportunities.md` | 40 | `Research + review достаточно для MVP` | Historical argument against fact checker. |
| `retrospectives/architecture-review-002/anti-regression-check.md` | 21 | `MVP roles без расширения.` | Historical anti-regression item. |
| `retrospectives/architecture-review-002/final-recommendation.md` | 19 | `MVP agent set.` | Historical recommendation. |
| `retrospectives/architecture-review-002/proposed-roadmap.md` | 80 | `не менять MVP agent set;` | Historical roadmap item. |
| `retrospectives/system-maintenance-retrospective-0010/step-003/implementation-plan.md` | 21 | `Do not change... MVP agent set` | Historical step boundary. |
| `retrospectives/system-maintenance-retrospective-0010/step-003/diff_agents.md` | 29 | `MVP role routing` | Historical diff note. |
| `retrospectives/system-maintenance-retrospective-0010/step-003/rollback-notes.md` | 23 | `MVP agent set` | Historical rollback note. |
| `retrospectives/system-maintenance-retrospective-0010/step-003/diff.md` | 60 | `No MVP agent set change.` | Historical diff note. |
| `retrospectives/system-maintenance-retrospective-0010/step-004/rollback-notes.md` | 33 | `MVP agent` | Historical rollback note. |
| `retrospectives/visual-editorial-review-001/executive-summary.md` | 9 | `только MVP-роли... non-MVP roles` | Historical Artist Agent conflict. |
| `retrospectives/visual-editorial-review-001/executive-summary.md` | 22 | `MVP-role политикой` | Historical Artist Agent conflict. |
| `retrospectives/visual-editorial-review-001/missing-pieces.md` | 16 | `активные production roles только MVP-роли` | Historical gap before Artist Agent legalization. |
| `retrospectives/visual-editorial-review-001/final-verdict.md` | 13 | `non-MVP extension` | Historical recommendation. |
| `retrospectives/visual-editorial-review-001/production-readiness.md` | 25 | `MVP-only limitation` | Historical readiness risk. |
| `retrospectives/visual-editorial-review-001/risk-review.md` | 7 | `только MVP-роли` | Historical risk. |
| `retrospectives/visual-editorial-review-001/responsibility-review.md` | 36 | `активные production roles только MVP-роли` | Historical conflict. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/implementation-plan.md` | 7 | `non-MVP extension role` | Historical Step 0011-1 scope. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/implementation-plan.md` | 22 | `non-MVP role as forbidden` | Historical problem statement. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/implementation-plan.md` | 26 | `MVP set unchanged` | Historical implementation plan. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/implementation-plan.md` | 27 | `non-MVP extension roles are forbidden unless explicitly legalized` | Historical planned policy. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/implementation-plan.md` | 30 | `non-MVP bans` | Historical planned policy. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/artist-agent-legitimacy-decisions.md` | 5 | `legal non-MVP extension role` | Historical decision legalizing Artist Agent. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/artist-agent-legitimacy-decisions.md` | 7 | `ordinary MVP role set` | Historical scope boundary. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/artist-agent-legitimacy-decisions.md` | 11 | `Non-MVP extension roles remain forbidden by default.` | Historical decision. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/artist-agent-legitimacy-decisions.md` | 41 | `MVP agent set remains unchanged` | Historical decision. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/artist-agent-legitimacy-decisions.md` | 47 | `Pipelines still default to MVP roles.` | Historical decision. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/artist-agent-legitimacy-decisions.md` | 49 | `non-MVP extension roles` | Historical decision. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/safety-check.md` | 15 | `non-MVP extension role` | Historical validation. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/safety-check.md` | 19 | `MVP agent set remains unchanged` | Historical validation. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/safety-check.md` | 36 | `non-MVP bans` | Historical validation. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/safety-check.md` | 38 | `MVP-owned` | Historical validation. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/changed-files.md` | 35 | `non-MVP prohibitions` | Historical change summary. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-001/rollback-notes.md` | 23 | `non-MVP roles as fully forbidden` | Historical rollback risk. |
| `retrospectives/system-maintenance-retrospective-0011-1/step-002/diff.md` | 26 | `MVP agent set remains unchanged... Artist Agent... extension` | Historical diff context. |

## Detailed historical diff mentions

`retrospectives/system-maintenance-retrospective-0011-1/step-001/diff.md` contains a compact historical diff with multiple `MVP` / `non-MVP` lines. These are not active policy, but they are important because they show how Artist Agent became legal as a bounded extension.

| Line | Exact formulation | Historical meaning |
| ---: | --- | --- |
| 14 | `-В MVP активными production roles являются только эти канонические роли и файлы:` | Removed old absolute role-set wording. |
| 15 | `+В MVP активными production roles для обычных текстовых задач являются эти канонические роли и файлы:` | Added ordinary-text-task scope. |
| 18 | `+Только канонические agent files из /agents/*.md должны использоваться как активные спецификации для MVP-ролей и явно легализованных extension-ролей...` | Added extension-role allowance. |
| 20 | `+Non-MVP extension roles are forbidden by default unless this charter explicitly legalizes them.` | Added default-ban / explicit-legalization model. |
| 33 | `+The MVP agent set remains unchanged for ordinary text tasks. Artist Agent is a bounded visual-branch extension, not a universal production role.` | Preserved core text-task roles while legalizing Artist Agent narrowly. |
| 35 | `- chief_editor выбирает pipeline, назначает MVP-роли...` | Removed old orchestration wording. |
| 36 | `+ chief_editor выбирает pipeline, назначает MVP-роли или явно легализованные extension-роли только когда их условия выполнены...` | Added extension-role assignment condition. |
| 52 | `- Only MVP agents may be used...` | Removed absolute pipeline ban. |
| 53 | `+ By default, only MVP agents may be used...` | Added default wording. |
| 54 | `+ Explicitly legalized non-MVP extension roles may be assigned only under AGENTS.md conditions...` | Added bounded extension allowance. |
| 56 | `- This pipeline must not assign work to any non-MVP role.` | Removed absolute non-MVP role ban. |
| 57 | `+ This pipeline must not assign work to non-MVP extension roles by default.` | Added default ban. |
| 60 | `- task requires a non-MVP production role;` | Removed old blocker wording. |
| 61 | `+ task requires a non-MVP production role that is not explicitly legalized in AGENTS.md,` | Added unauthorized-role distinction. |
| 64 | `- request to use a non-MVP role;` | Removed old escalation wording. |
| 65 | `+ request to use a non-MVP role that is not explicitly legalized in AGENTS.md,` | Added unauthorized-role distinction. |
| 68 | `- confirm current owner role and next role are valid MVP roles;` | Removed old restart check. |
| 69 | `+ confirm current owner role and next role are valid MVP roles or explicitly legalized` | Added extension-role restart check. |
| 70 | `+ extension roles whose AGENTS.md conditions apply;` | Completed bounded extension condition. |
| 76 | `+ Legalized Artist Agent only as bounded non-MVP visual extension.` | Historical boundary confirmation. |
| 77 | `+ Kept MVP agent set unchanged for ordinary text tasks.` | Historical boundary confirmation. |

## Generated / old report mentions

`about/project_tree.md` is not in the active-policy list requested for Step 1, but it is a report-like system map with seven mentions:

- `operational MVP with strong governance and artifact discipline`
- `active MVP. Strongest operational layer.`
- `MVP roles`
- `current MVP agents`
- `Purpose: active MVP role specifications.`
- `introduce non-MVP roles by implication.`
- `mature MVP role set.`

Recommendation: classify as old/generated report context unless the project explicitly treats `project_tree.md` as active documentation in a later step.

## Historical handling recommendation

Do not rewrite historical files as part of the terminology migration. They are useful audit trail. If a later cleanup needs historical consistency, add a short note in new reports explaining that old `MVP` language means the former term for the current core operating model.
