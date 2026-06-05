# Preflight Gate Sber Manual Trial

This is a synthetic/sanitized manual trial. It is not a real task folder and does not contain real working materials.

## Purpose

Check whether the existing Preflight Gate examples help distinguish
Sber-owned communication from an independent material where Sber is only a
topic or market example.

This report is test/reference material. It does not replace `AGENTS.md`, Intake
Agent, Chief Editor, task artifacts, client-profile source files, or
review-gate.

## Trial status

- Trial type: sanitized manual trial.
- Source material: synthetic prompts only.
- Real client/source materials: none.
- Production task artifacts: none.

## Scenario A — Sber-owned communication

### Raw request

> Нужно написать короткий push для Сбера о новой функции в приложении. Функция помогает пользователю быстрее найти нужный раздел. Детали функции пока не подтверждены, нужен безопасный черновик.

### Compared examples

- Sber-owned communication: primary match; the request is explicitly for Sber
  and for a product communication.
- Vague release announcement: useful comparison for `constrain`, because details
  are missing but a bounded draft can start.
- Missing source high-governance claim: negative contrast; the scenario has
  unconfirmed product details, but not a numeric user-impacting claim.
- Sber as market case: contrast case; this scenario is owned communication, not
  independent market analysis.

### Preflight decision

Expected preflight decision: `constrain`

### Expected routing

- pipeline: `social`
- risk mode: `standard`
- client_profile: `sber`
- process depth: `compact`
- compact execution: `allowed if Sber profile source status is active or
  task-scoped constraints are clearly bounded`
- required next action: bounded push draft with visible placeholders for
  unconfirmed function details, Sber client-profile considerations, and review
  before finalization

### Why

- The task is explicitly Sber-owned.
- It is a Sber product communication.
- Missing feature details make `proceed` too confident.
- `constrain` allows a safe draft without inventing product behavior.
- Sber profile should activate because ownership is clear.
- Review-gate remains required.

### What should not happen

- should not treat missing function details as confirmed;
- should not invent product behavior or user benefits beyond the request;
- should not skip Sber client-profile considerations;
- should not claim Sber-policy compliance without active source status;
- should not bypass review-gate;
- should not create real task materials.

## Scenario B — Sber as market topic

### Raw request

> Нужен черновик статьи про Сбер как пример крупной цифровой экосистемы на рынке. Нужно использовать его как один из рыночных примеров, без задачи писать от имени Сбера.

### Compared examples

- Sber as market case: primary match; Sber is a topic/example, not the owner of
  the communication.
- Vague release announcement: useful comparison for `constrain`, because the
  draft can start with source placeholders.
- Sber-owned communication: negative contrast; this scenario explicitly says the
  material is not written on behalf of Sber.
- Missing source high-governance claim: partial contrast; market claims need
  sources, but the request is not asking for a specific unverified numeric claim.

### Preflight decision

Expected preflight decision: `constrain`

### Expected routing

- pipeline: `article`
- risk mode: `standard`
- client_profile: `none`
- process depth: `compact`
- compact execution: `allowed with source placeholders for market claims`
- required next action: bounded article draft or outline with explicit source
  placeholders, Sber profile inactive, and review before finalization

### Why

- Sber is a topic and market example, not the communication owner.
- The task is not Sber-owned and does not ask for Sber editorial policy.
- Client profile must remain `none`.
- Market claims require sources or placeholders.
- Applying Sber client policy to an independent article would be a routing
  error.
- `constrain` is safer than `proceed` because the market angle and sources are
  not yet confirmed.

### What should not happen

- should not activate Sber profile when Sber is only a topic/example;
- should not apply Sber editorial policy to an independent article;
- should not invent market claims or ecosystem claims;
- should not write as if on behalf of Sber;
- should not bypass review-gate;
- should not create real task materials.

## Comparison

The key difference is communication ownership.

Scenario A is for Sber and about a Sber product communication, so
`client_profile: sber` is expected. Scenario B is an independent article where
Sber is only a market example, so `client_profile: none` is expected.

Both scenarios use `constrain` because both are clear enough to start a bounded
draft, but not clear enough for overconfident final wording.

## Decision

Manual trial result: examples are useful.

The existing Sber-owned and Sber-as-topic examples make the activation boundary
clear enough for manual routing.

## Need for automated checker

Automated checker is not needed yet.

Recommendation: complete one more sanitized manual trial, for example a
UX/context trial, before deciding whether automation would add value.
