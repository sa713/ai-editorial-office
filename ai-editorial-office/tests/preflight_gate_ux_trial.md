# Preflight Gate UX Context Manual Trial

This is a synthetic/sanitized manual trial. It is not a real task folder and does not contain real working materials.

## Purpose

Check whether the existing Preflight Gate examples help choose a bounded
strategy for a UX writing task with incomplete product context.

This report is test/reference material. It does not replace `AGENTS.md`, Intake
Agent, Chief Editor, UX Writer, task artifacts, product evidence, or
review-gate.

## Trial status

- Trial type: sanitized manual trial.
- Source material: synthetic prompt only.
- Real product/client/source materials: none.
- Production task artifacts: none.

## Raw request

> Нужен UX-текст для ошибки оплаты. Пользователь пытался оплатить, но платёж не прошёл. Нужно короткое сообщение, кнопка и подсказка, что делать дальше. Точных причин ошибки, правил повтора платежа и контакта поддержки пока нет.

## Compared examples

- UX error message example: primary match; the request is product-facing error
  microcopy and maps to `ux_writing`.
- Vague release announcement: useful `constrain` comparison; missing details do
  not require a long questionnaire if placeholders stay visible.
- Missing source high-governance claim: negative contrast; the prompt has
  missing product behavior, but not a precise numeric or user-impacting factual
  claim.
- Legal notice: negative contrast; the task is not legal, customer-notice
  governance, or terms-changing communication.

## Preflight decision

Expected preflight decision: `constrain`

Why not `proceed`:

- Error cause, retry rule, recovery action, and support path are not confirmed.
- Proceeding would risk inventing product behavior.

Why not `ask`:

- The task type, surface, and requested output are clear enough for a bounded
  generic UX copy draft.
- A long intake questionnaire would add friction before a safe placeholder-based
  draft.

Why not `block`:

- The request is not unsafe, deceptive, contradictory, legal, or
  high-governance.

## Expected routing

- pipeline: `ux_writing`
- risk mode: `standard`
- client_profile: `none`
- process depth: `compact`
- compact execution: `allowed with visible placeholders for product behavior`
- required next action: bounded UX copy draft with placeholders for error
  reason, retry rule, recovery action, and support path; review before
  finalization

## Why

- Task type and pipeline are clear.
- A safe generic UX state can start from the supplied payment-failure context.
- Product rules are incomplete and must remain visible as placeholders.
- UX Writer must not invent product behavior, flow logic, support paths, or
  recovery promises.
- `constrain` preserves momentum without turning intake into a long
  questionnaire.
- Review-gate remains required.

## What should not happen

- should not ask long questionnaire;
- should not invent error cause;
- should not invent retry timing;
- should not invent recovery mechanics;
- should not invent support path;
- should not promise successful payment recovery;
- should not activate client_profile;
- should not bypass review-gate;
- should not create real task materials.

## Decision

Manual trial result: examples are useful.

The UX error message example and the existing `constrain` comparisons are enough
to route this scenario without over-asking and without overconfident product
claims.

## Need for automated checker

Automated checker is not needed yet.

Manual examples distinguish `constrain` vs `ask`/`proceed` well for this
UX/context case. The next step is to decide whether the accumulated manual
trials justify automation or whether the markdown smoke-test is sufficient.
