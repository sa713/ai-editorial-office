# Preflight Gate Manual Trial

This is a synthetic/sanitized manual trial. It is not a real task folder and does not contain real working materials.

## Purpose

Check whether the existing Preflight Gate examples help choose a bounded routing
strategy for one realistic, sanitized intake scenario.

This report is test/reference material. It does not replace `AGENTS.md`, Intake
Agent, Chief Editor, task artifacts, or review-gate.

## Raw request

> Нужно написать пост в мессенджер для внутренней команды: завтра меняется порядок сдачи материалов по ежемесячному выпуску. Нужно объяснить, что теперь для каждого выпуска будут два треда - "Статус" и "Материалы"; обсуждения нужно вести только в них; файлы и финальные версии тоже складывать туда. Тон спокойный, рабочий, без канцелярита.

This scenario is sanitized: it does not name real teams, employees, internal
systems, clients, or source materials.

## Compared examples

- Low-risk messenger post: closest positive match because the requested output
  is a short internal messenger post with a clear operational fact.
- Vague release announcement: useful comparison for `constrain`, because the
  draft can start with visible placeholders instead of a long questionnaire.
- Legal notice / high-governance example: negative contrast; this scenario is
  not customer-facing, legal, numeric, or approval-heavy.
- UX example: non-match; the request is about internal coordination messaging,
  not interface copy, product states, or payment behavior.

## Preflight decision

Expected preflight decision: `constrain`

Why not `proceed`:

- The task is understandable, but exact team name, channel name, launch date,
  thread naming convention, and final wording of the rules are not confirmed.
- A final-ready post should not invent those details.

Why not `ask`:

- The missing details do not block a safe bounded draft.
- The system can start with placeholders and explicit assumptions instead of a
  long intake questionnaire.

Why not `block`:

- The task is not deceptive, unsafe, contradictory, legal, or high-governance.

## Expected routing

- pipeline: `social`
- risk mode: `low-risk`
- client_profile: `none`
- process depth: `compact`
- compact execution: `allowed`
- required next action: bounded internal messenger draft with visible
  placeholders and review before finalization

Risk mode rationale: `low-risk` is appropriate because this is an internal
coordination note with no external claims, customer impact, legal effect, client
profile, or sensitive source material. It could become `standard` if the process
change were tied to a formal release governance policy, named stakeholders, or a
published operational mandate.

## What should not happen

- should not ask long questionnaire;
- should not invent exact team/system names;
- should not create legal/high-governance framing;
- should not activate client_profile;
- should not bypass review-gate;
- should not create real task materials.

## Decision

Manual trial result: Preflight examples are useful.

They help choose `constrain` for a realistic internal coordination scenario:
start safely with bounded assumptions and placeholders, while avoiding both a
long intake questionnaire and overconfident final wording.

## Need for automated checker

Automated checker is not needed yet.

Recommendation: add 2-3 more sanitized manual trials after realistic intake
tasks, then decide whether an automated checker would catch meaningful routing
mistakes without creating a new layer of bureaucracy.

## Edge cases to add later

- internal coordination request with named but sanitized approval owner;
- internal post that contains a numeric deadline or operational metric;
- mixed request that asks for both messenger post and UX microcopy;
- request where client name is mentioned as topic but not as communication
  owner.
