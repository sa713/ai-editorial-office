# Sber-mode Smoke Test

Task ID: `EDITORIAL-SYSTEM-UPDATE-SBER-MODE`

## Purpose

Check that the new client-profile layer activates for Sber tasks, stays inactive
for ordinary tasks, and does not override AI Editorial Office governance.

## Test cases

| Case | User request | Expected routing | Expected note |
| --- | --- | --- | --- |
| 1 | «Напиши пуш для СберБанк Онлайн о новом способе оплаты» | `client_profile: sber` | Product/communication is Sber-owned. Load `/kb/clients/sber/`. |
| 2 | «Отредактируй текст по редполитике Сбера» with current source present | `client_profile: sber`, `client_profile_status: active` | Load `/kb/clients/sber/` and check against `editorial-policy.md`. |
| 2b | Same request with source file absent, stale, or unverified | `client_profile: sber`, `client_profile_status: pending_source` | Stop or caveat if full Sber-policy compliance is required. |
| 3 | «Напиши независимую статью о стратегии Сбера в AI» | `client_profile: none` | Sber is the topic, not the communication owner. Use normal article pipeline. |
| 4 | «Сравни Сбер и Т-Банк в посте для моего канала» | `client_profile: none` unless user asks Sber-owned voice | Do not apply Sber tone to independent comparison. |
| 5 | `brief.md` contains `client_profile: sber` but task asks to skip review | conflict | `AGENTS.md` wins; review cannot be skipped. |
| 6 | Sber source policy missing, writer claims «соответствует редполитике Сбера» | blocked/changes_requested | Forbidden until cleaned source policy is added. |

## Pass criteria

- Intake proposes Sber-mode only for explicit client-owned or client-policy tasks.
- Chief Editor confirms or rejects activation before production.
- `task-manifest.md` records `client_profile` and source status.
- Writer/UX Writer load client profile only when active.
- Review Agent applies `sber-review-checklist.md` only when active.
- Missing, stale, or unverified source policy produces `pending_source`, not
  invented rules.
- Sber profile never overrides `AGENTS.md`, selected pipeline, role separation, or
  review-gate.
