# MVP inventory

## Summary

`MVP` is still an active policy term. It does not only mean "early product version"; in this editorial system it currently encodes:

- the core role set for ordinary text tasks;
- default role admissibility;
- extension-role default bans and exceptions;
- the no-separate-Editor-Agent rule;
- the direct `writing` / `ux-writing` -> `review` transition;
- default production and review sequences;
- handoff validity checks;
- governance escalation triggers.

Active policy contains 67 Markdown mentions across 14 files.

Historical / retrospective material contains many additional mentions across old task artifacts, retrospectives, diffs, and review reports. Those mentions document prior decisions and should not be treated as live policy.

`editorial_knowledge/*.md` has no `MVP` mentions.

## Requested phrase coverage

| Requested phrase | Found in active policy | Notes |
| --- | --- | --- |
| `MVP` | yes | Core term across AGENTS, project state, pipelines, one role file, template, and KB. |
| `MVP role` / `MVP roles` | yes | Used for role admissibility, handoff targets, boundaries, and governance checks. |
| `MVP agent` / `MVP agents` | yes | Used for active role set and pipeline defaults. |
| `MVP workflow` | yes | Used as `MVP workflow default` in `project-state.md` and `MVP default workflow` in `AGENTS.md`. |
| `MVP architecture` | no exact active phrase | The architecture concept appears historically, but active policy phrases the same idea as role set, workflow, or operating constraints. |
| `MVP phase` | no exact active phrase | Historical text mentions "current phase" plus active MVP agents; active policy does not use the exact phrase. |

## Active policy files with `MVP`

| File | Mentions | System role of mentions |
| --- | ---: | --- |
| `ai-editorial-office/AGENTS.md` | 12 | Main governance charter: role set, extension policy, workflow, status semantics, artifacts. |
| `ai-editorial-office/project-state.md` | 5 | Current state mirror: current agents, workflow default, normalization decisions. |
| `ai-editorial-office/agents/chief_editor.md` | 3 | Chief Editor role boundaries and self-checks. |
| `ai-editorial-office/pipelines/article_pipeline.md` | 7 | Pipeline role admissibility, sequence, blockers, restart checks. |
| `ai-editorial-office/pipelines/social_pipeline.md` | 7 | Pipeline role admissibility, sequence, blockers, restart checks. |
| `ai-editorial-office/pipelines/ux_writing_pipeline.md` | 7 | Pipeline role admissibility, sequence, blockers, restart checks. |
| `ai-editorial-office/pipelines/review_pipeline.md` | 7 | Review role admissibility, handoff targets, sequence, review-gate checks. |
| `ai-editorial-office/pipelines/research_pipeline.md` | 6 | Research role admissibility, handoff targets, blockers, restart checks. |
| `ai-editorial-office/templates/agent_template.md` | 1 | Template guard for creating new role specs. |
| `ai-editorial-office/kb/editorial_policy.md` | 3 | Editorial authority, role creation ban, missing-role blocker. |
| `ai-editorial-office/kb/task_statuses.md` | 5 | Status model and direct writing-to-review rule. |
| `ai-editorial-office/kb/glossary.md` | 2 | Definitions for handoff and orchestration. |
| `ai-editorial-office/kb/tone_of_voice.md` | 1 | Defines writing-capable agents for tone. |
| `ai-editorial-office/kb/forbidden_patterns.md` | 1 | Route changes to owning role. |

## Historical / retrospective groups

Historical mentions fall into these groups:

- Early architecture review and iteration planning: prior MVP design assumptions, role-set validation, and simplification proposals.
- TASK-0001 / TASK-0002 run history: validation of the original role model and evidence that MVP worked but was operationally heavy.
- Visual / Artist Agent review: documents the former conflict between Artist Agent and MVP-only role policy.
- `system-maintenance-retrospective-0011-1`: records the change that legalized Artist Agent as a bounded `non-MVP extension role`.
- `system-maintenance-retrospective-0010`: records role compression and no-change decisions around the MVP agent set.
- `about/project_tree.md`: generated/old system map; useful as report context, not listed as active policy by the Step 1 criteria.

## Main interpretation

The active system uses `MVP` as a proxy for "current core operating model." A safe replacement should therefore not be a single blind term. The replacement needs to distinguish:

- core roles for ordinary text work;
- explicitly legalized extension roles such as Artist Agent;
- unauthorized extension roles;
- default operating model and production sequence;
- optional revision/status bridge semantics;
- historical validation language that should remain historical.
