# Active policy findings

## High-level finding

Active policy uses `MVP` in several different meanings. The most sensitive uses are role admissibility and pipeline validity checks. Replacing every `MVP` with one phrase would blur the distinction between core roles and legalized extension roles, especially Artist Agent.

Recommended replacement vocabulary:

- `core roles` for the ordinary text-task role set;
- `primary roles` where the text means the default roles used in regular task execution;
- `extension roles` where the text means Artist Agent or future non-core roles;
- `production roles` where the text means roles that may own task work;
- `operating model` where the text means lifecycle, status, artifacts, or workflow;
- remove without replacement only where `MVP` is historical filler and the sentence remains precise.

## Active mentions and replacement recommendations

| File | Line | Exact formulation | Why `MVP` is used | Better replacement |
| --- | ---: | --- | --- | --- |
| `ai-editorial-office/AGENTS.md` | 73 | `## MVP agent set` | Names the current allowed core agent set. | `## Core role set` or `## Core agent set`. |
| `ai-editorial-office/AGENTS.md` | 75 | `В MVP активными production roles для обычных текстовых задач являются эти канонические роли и файлы:` | Defines active production roles for ordinary text tasks. | `В текущем operating model активными core production roles...` |
| `ai-editorial-office/AGENTS.md` | 85 | `Только канонические agent files из /agents/*.md должны использоваться как активные спецификации для MVP-ролей и явно легализованных extension-ролей...` | Separates active specs from duplicates and includes extensions. | `...для core roles и явно легализованных extension roles...` |
| `ai-editorial-office/AGENTS.md` | 87 | `Non-MVP extension roles are forbidden by default unless this charter explicitly legalizes them.` | Default-ban rule for roles outside the core set. | `Unauthorized extension roles are forbidden by default unless this charter explicitly legalizes them.` |
| `ai-editorial-office/AGENTS.md` | 110 | `The MVP agent set remains unchanged for ordinary text tasks. Artist Agent is a bounded visual-branch extension, not a universal production role.` | Protects core text-task role set while allowing Artist Agent only in bounded scope. | `The core role set remains unchanged for ordinary text tasks. Artist Agent is a bounded visual-branch extension...` |
| `ai-editorial-office/AGENTS.md` | 112 | `В MVP нет обязательной роли Editor.` | Encodes no separate Editor Agent in current model. | `В текущем operating model нет обязательной роли Editor.` |
| `ai-editorial-office/AGENTS.md` | 119 | `Они не являются текущими MVP-ролями и не могут быть обязательными участниками task flow.` | Keeps future roles non-active. | `Они не являются текущими core roles...` |
| `ai-editorial-office/AGENTS.md` | 303 | `MVP default workflow:` | Labels the default lifecycle. | `Default operating workflow:` |
| `ai-editorial-office/AGENTS.md` | 444 | `chief_editor выбирает pipeline, назначает MVP-роли или явно легализованные extension-роли...` | Governance rule for role assignment. | `...назначает core roles или явно легализованные extension roles...` |
| `ai-editorial-office/AGENTS.md` | 466 | `В MVP прямой переход writing -> review валиден... В MVP editing не является обязательным этапом...` | Defines status semantics and no Editor Agent rule. | `В текущем operating model...` |
| `ai-editorial-office/AGENTS.md` | 576 | ``editing` — optional revision checkpoint/status bridge; в MVP доработка возвращается...` | Status definition. | `...в текущем operating model доработка возвращается...` |
| `ai-editorial-office/AGENTS.md` | 630 | ``edited.md`, `editor-notes.md` и `revision-requests.md` не являются обязательными MVP-артефактами.` | Artifact minimalism and future-editor guard. | `...не являются обязательными production artifacts...` |
| `ai-editorial-office/project-state.md` | 9 | `- MVP agent set;` | Current state says it records role set. | `- core role set;` |
| `ai-editorial-office/project-state.md` | 18 | `## Current MVP agents` | Heading for current active agents. | `## Current core roles` or `## Current core agents`. |
| `ai-editorial-office/project-state.md` | 49 | `## MVP workflow default` | Current default lifecycle mirror. | `## Default operating workflow` |
| `ai-editorial-office/project-state.md` | 65 | `- MVP does not include separate editor_agent.` | No separate Editor Agent invariant. | `- The current operating model does not include separate editor_agent.` |
| `ai-editorial-office/project-state.md` | 66 | `- Direct writing -> review is valid in MVP...` | Direct transition rule. | `...is valid in the current operating model...` |
| `ai-editorial-office/agents/chief_editor.md` | 24 | `- assign work only to the existing MVP roles;` | Chief Editor assignment boundary. | `- assign work only to current core roles or explicitly legalized extension roles;` |
| `ai-editorial-office/agents/chief_editor.md` | 76 | `- use non-MVP roles or create new roles;` | Prohibition against unauthorized roles. | `- use unauthorized extension roles or create new roles;` |
| `ai-editorial-office/agents/chief_editor.md` | 124 | `- role assignment keeps MVP boundaries intact;` | Self-check for role boundaries. | `- role assignment keeps core-role and extension-role boundaries intact;` |
| `ai-editorial-office/templates/agent_template.md` | 4 | `...explicitly added that role to the MVP agent set.` | Guard against creating unauthorized role specs. | `...explicitly added that role to the core role set or legalized it as an extension role.` |
| `ai-editorial-office/kb/editorial_policy.md` | 5 | `This file is the minimal editorial authority for MVP execution.` | Names current execution authority. | `...for the current operating model.` |
| `ai-editorial-office/kb/editorial_policy.md` | 116 | `- create new MVP roles or route work to non-existing agents;` | Prevents role creation / invalid routing. | `- create new core roles or route work to non-existing agents;` |
| `ai-editorial-office/kb/editorial_policy.md` | 145 | `- a required MVP role or artifact is missing;` | Escalation/blocker condition. | `- a required core role, legalized extension role, or artifact is missing;` |
| `ai-editorial-office/kb/task_statuses.md` | 30 | ``editing` ... not required in MVP and not a separate Editor Agent role.` | Status semantics. | `...not required in the current operating model...` |
| `ai-editorial-office/kb/task_statuses.md` | 63 | `## MVP writing-to-review rule` | Section heading for transition rule. | `## Writing-to-review rule` or `## Default writing-to-review rule`. |
| `ai-editorial-office/kb/task_statuses.md` | 65 | `For MVP, writing -> review is an explicitly valid direct transition.` | Direct transition rule. | `In the current operating model...` |
| `ai-editorial-office/kb/task_statuses.md` | 75 | `ux-writing -> review has the same MVP validity...` | Extends direct transition rule to UX label. | `...has the same default validity...` |
| `ai-editorial-office/kb/task_statuses.md` | 77 | ``editing` is optional in MVP... does not imply a separate Editor Agent in MVP.` | Optional editing bridge. | `...is optional in the current operating model...` |
| `ai-editorial-office/kb/glossary.md` | 17 | `...transfers context, status, blockers, and next action from one MVP role to another.` | Defines handoff between valid roles. | `...from one active role to another.` |
| `ai-editorial-office/kb/glossary.md` | 23 | `...selects the pipeline, assigns MVP roles, defines sequence...` | Defines orchestration as role assignment. | `...assigns core roles or legalized extension roles...` |
| `ai-editorial-office/kb/tone_of_voice.md` | 5 | `...writing-capable MVP agents: writer_agent, ux_writer, final_editor...` | Narrows tone rules to writing-capable core roles. | `...writing-capable core roles...` |
| `ai-editorial-office/kb/forbidden_patterns.md` | 82 | `Route changes to the owning MVP role instead of crossing role boundaries.` | Prevents boundary crossing. | `Route changes to the owning active role...` |
| `ai-editorial-office/pipelines/article_pipeline.md` | 47 | `By default, only MVP agents may be used for this pipeline...` | Default role admissibility. | `By default, only core roles may be used...` |
| `ai-editorial-office/pipelines/article_pipeline.md` | 58 | `This pipeline must not assign work to non-MVP extension roles by default... revision in MVP is handled by writer_agent...` | Extension default ban and revision owner. | `...unauthorized extension roles... revision in the current operating model...` |
| `ai-editorial-office/pipelines/article_pipeline.md` | 169 | `MVP default production sequence:` | Sequence label. | `Default production sequence:` |
| `ai-editorial-office/pipelines/article_pipeline.md` | 189 | `Direct writing -> review handoff is valid in MVP...` | Direct transition and no separate editor role. | `...valid in the current operating model...` |
| `ai-editorial-office/pipelines/article_pipeline.md` | 467 | `task requires a non-MVP production role that is not explicitly legalized...` | Blocking condition. | `task requires an unauthorized production role...` |
| `ai-editorial-office/pipelines/article_pipeline.md` | 500 | `request to use a non-MVP role that is not explicitly legalized...` | Escalation condition. | `request to use an unauthorized extension role...` |
| `ai-editorial-office/pipelines/article_pipeline.md` | 557 | `confirm current owner role and next role are valid MVP roles or explicitly legalized extension roles...` | Restart validity check. | `...valid core roles or explicitly legalized extension roles...` |
| `ai-editorial-office/pipelines/social_pipeline.md` | 45 | `By default, only MVP agents may be used for this pipeline...` | Default role admissibility. | `By default, only core roles may be used...` |
| `ai-editorial-office/pipelines/social_pipeline.md` | 56 | `This pipeline must not assign work to non-MVP extension roles by default... revision in MVP is handled...` | Extension default ban and revision owner. | `...unauthorized extension roles... revision in the current operating model...` |
| `ai-editorial-office/pipelines/social_pipeline.md` | 169 | `MVP default production sequence:` | Sequence label. | `Default production sequence:` |
| `ai-editorial-office/pipelines/social_pipeline.md` | 189 | `Direct writing -> review handoff is valid in MVP...` | Direct transition and no separate editor role. | `...valid in the current operating model...` |
| `ai-editorial-office/pipelines/social_pipeline.md` | 552 | `task requires a non-MVP production role that is not explicitly legalized...` | Blocking condition. | `task requires an unauthorized production role...` |
| `ai-editorial-office/pipelines/social_pipeline.md` | 591 | `request to use a non-MVP role that is not explicitly legalized...` | Escalation condition. | `request to use an unauthorized extension role...` |
| `ai-editorial-office/pipelines/social_pipeline.md` | 648 | `confirm current owner role and next role are valid MVP roles or explicitly legalized extension roles...` | Restart validity check. | `...valid core roles or explicitly legalized extension roles...` |
| `ai-editorial-office/pipelines/ux_writing_pipeline.md` | 51 | `By default, only MVP agents may be used for this pipeline...` | Default role admissibility. | `By default, only core roles may be used...` |
| `ai-editorial-office/pipelines/ux_writing_pipeline.md` | 62 | `This pipeline must not assign work to non-MVP extension roles by default... revision in MVP is handled...` | Extension default ban and revision owner. | `...unauthorized extension roles... revision in the current operating model...` |
| `ai-editorial-office/pipelines/ux_writing_pipeline.md` | 178 | `MVP default production sequence:` | Sequence label. | `Default production sequence:` |
| `ai-editorial-office/pipelines/ux_writing_pipeline.md` | 198 | `Direct writing -> review handoff is valid in MVP...` | Direct transition and no separate editor role. | `...valid in the current operating model...` |
| `ai-editorial-office/pipelines/ux_writing_pipeline.md` | 520 | `task requires a non-MVP production role that is not explicitly legalized...` | Blocking condition. | `task requires an unauthorized production role...` |
| `ai-editorial-office/pipelines/ux_writing_pipeline.md` | 556 | `request to use a non-MVP role that is not explicitly legalized...` | Escalation condition. | `request to use an unauthorized extension role...` |
| `ai-editorial-office/pipelines/ux_writing_pipeline.md` | 613 | `confirm current owner role and next role are valid MVP roles or explicitly legalized extension roles...` | Restart validity check. | `...valid core roles or explicitly legalized extension roles...` |
| `ai-editorial-office/pipelines/review_pipeline.md` | 50 | `By default, only MVP agents may be used for this pipeline...` | Default role admissibility. | `By default, only core roles may be used...` |
| `ai-editorial-office/pipelines/review_pipeline.md` | 61 | `This pipeline must not assign review, editing, writing, finalization, or governance work to non-MVP extension roles by default...` | Extension default ban across responsibilities. | `...unauthorized extension roles by default...` |
| `ai-editorial-office/pipelines/review_pipeline.md` | 97 | `Missing editing status is not a blocker in MVP.` | Review start rule. | `...not a blocker in the current operating model.` |
| `ai-editorial-office/pipelines/review_pipeline.md` | 124 | `TO must be replaced with the receiving MVP role, or an explicitly legalized extension role...` | Handoff filename target validity. | `...receiving core role, or an explicitly legalized extension role...` |
| `ai-editorial-office/pipelines/review_pipeline.md` | 181 | `MVP default review sequence:` | Sequence label. | `Default review sequence:` |
| `ai-editorial-office/pipelines/review_pipeline.md` | 199 | `Direct writing -> review handoff is valid in MVP... Review Agent must not treat a missing editing stage as a blocker in MVP.` | Direct transition and no mandatory editing stage. | `...valid in the current operating model...` |
| `ai-editorial-office/pipelines/review_pipeline.md` | 298 | `handoff exists to the correct next MVP role or explicitly legalized extension role...` | Review completeness check. | `...next core role or explicitly legalized extension role...` |
| `ai-editorial-office/pipelines/research_pipeline.md` | 38 | `By default, only MVP agents may be used.` | Default role admissibility. | `By default, only core roles may be used.` |
| `ai-editorial-office/pipelines/research_pipeline.md` | 50 | `...must not refer work to non-MVP extension roles by default...` | Extension default ban. | `...must not refer work to unauthorized extension roles by default...` |
| `ai-editorial-office/pipelines/research_pipeline.md` | 84 | `TO must be replaced with the receiving MVP role, or an explicitly legalized extension role...` | Handoff filename target validity. | `...receiving core role, or an explicitly legalized extension role...` |
| `ai-editorial-office/pipelines/research_pipeline.md` | 347 | `handoff cannot identify a valid MVP receiving role or an explicitly legalized extension role...` | Blocking condition. | `...valid core receiving role or explicitly legalized extension role...` |
| `ai-editorial-office/pipelines/research_pipeline.md` | 391 | `handoff... exists with TO replaced by a valid MVP receiving role or an explicitly legalized extension role...` | Completion check. | `...valid core receiving role or explicitly legalized extension role...` |
| `ai-editorial-office/pipelines/research_pipeline.md` | 423 | `confirm the current owner role and next required role are valid MVP roles or explicitly legalized extension roles...` | Restart validity check. | `...valid core roles or explicitly legalized extension roles...` |

## Dangerous active places

### Role admissibility

Most dangerous:

- `ai-editorial-office/AGENTS.md:73-119`
- `ai-editorial-office/agents/chief_editor.md:24,76,124`
- all pipeline `required agents` sections
- `ai-editorial-office/templates/agent_template.md:4`
- `ai-editorial-office/kb/editorial_policy.md:116,145`

Risk: replacing `MVP roles` with only `production roles` could accidentally allow Artist Agent or future extension roles everywhere. Replacing `non-MVP` with just `extension` could accidentally ban already legalized Artist Agent again.

### Pipeline behavior

Most dangerous:

- `article_pipeline.md:47,58,467,500,557`
- `social_pipeline.md:45,56,552,591,648`
- `ux_writing_pipeline.md:51,62,520,556,613`
- `review_pipeline.md:50,61,124,298`
- `research_pipeline.md:38,50,84,347,391,423`

Risk: these are executable operating contracts. Bad wording can break who may receive handoffs, which tasks block, and whether extension roles may be used under `AGENTS.md`.

### Governance

Most dangerous:

- `AGENTS.md:444`
- `project-state.md:49,65,66`
- `kb/editorial_policy.md:5,145`
- Chief Editor self-checks in `agents/chief_editor.md`.

Risk: governance may lose the current boundary between default core execution and explicitly legalized extension execution.

### Artist Agent conflict

Most dangerous:

- `AGENTS.md:87,110`
- pipeline default-ban language in all pipelines.

Risk: Artist Agent is legal only as a bounded visual-branch extension. The replacement must keep three states distinct:

- core role;
- legalized extension role;
- unauthorized extension role.

### Meaning break points

Do not replace:

- `MVP agent set` with only `production roles` unless the sentence still excludes unauthorized roles.
- `non-MVP extension roles` with only `extension roles` if the sentence is about unauthorized extensions.
- `MVP` in direct transition rules with `core roles`; those are operating-model rules, not role-set rules.
- `MVP artifacts` with `core roles`; those are artifact-minimalism rules.
