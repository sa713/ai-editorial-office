# Orchestration Plan

Task ID: `TASK-0004B`

Owner: `chief_editor`

Selected pipeline: `article_pipeline`

Review required: yes

## Routing

1. Intake: create `brief.md`.
2. Orchestration: fix structure-before-writing pressure before drafting.
3. Writing: create `outline.md`, `draft.md`, `writer-notes.md`.
4. Review: check usefulness, path clarity, section roles, duplication, navigation, rereading cost, action discoverability, reference usability.
5. Finalization: create `final.md` from approved draft.
6. Comparison: compare `TASK-0004/final(1).md` and `TASK-0004B/final.md` after finalization only.
7. Governance: create `final_decision.md` and compact handoff.

## Research Decision

Separate research stage is omitted. The task is a rewrite from supplied source material, with no external claims required. All factual claims must come from the source draft or task brief.

## Structure-Before-Writing Notes

### Expected Reader Usage Mode

Mixed:

- quick scanning to choose one of three paths;
- role-specific reading for Автор and Исполнитель;
- reference lookup for fields, statuses, restrictions and disputes;
- repeated operational use while a карточка moves through the process.

### Proposed Structure Type

Overview plus decision routes:

1. what the exchange is for;
2. choose your path;
3. path for Автор;
4. path for Исполнитель;
5. path for Идея;
6. shared reference: statuses, fields, restrictions, disputes, contacts.

This should reduce rereading: the reader first chooses a path, then uses compact reference blocks.

### Reader-Path Risks

- Автор may need the fastest path from "create" to "choose executor" and miss moderation.
- Исполнитель may think a comment means assignment.
- Idea author may fill deadline because the idea form looks like task creation.
- Readers may confuse task flow and idea flow because they share fields.
- Disputes may be too late in the text unless visible from all paths.

### Section-Role Map

| Future section | Role |
| --- | --- |
| What you can do | orientation and scope |
| Choose your path | routing |
| If you publish a task | action path for Автор |
| If you want to execute a task | action path for Исполнитель |
| If you submit an idea | action path for Идея |
| Fields and restrictions | reference |
| Statuses and who acts | reference and navigation |
| Disputes and contacts | escalation |

### Duplication-Risk Areas

Do not explain the full task lifecycle separately in overview, Автор path and Исполнитель path. Use one compact lifecycle reference, then role-specific action lists.

Do not repeat the same field list separately for task and idea. Use one field reference with differences for idea.

Do not repeat curator contacts in every role path. Mention escalation in role paths and keep contacts in one final section.

Do not re-explain "подзадачи запрещены" in every section. Put it in restrictions.

## Artifact Scope

No `research.md`, `sources.md`, `facts.md`, `claims_table.md` or `claims-used.md` required: no new external claims are introduced.

