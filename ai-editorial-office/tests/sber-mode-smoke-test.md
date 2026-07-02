# Sber-Mode Smoke Test

Purpose: verify that `client_profile: sber` activates only for explicit
Sber-owned or Sber-policy tasks, never for ordinary independent materials where
Sber is only mentioned.

## Cases

| Case | Input | Expected routing | Expected source status |
| --- | --- | --- | --- |
| Sber-owned push | "Напиши пуш для СберБанк Онлайн о новом способе оплаты" | `client_profile: sber` | `active` when `/kb/clients/sber/editorial-policy.md` is present and verified |
| Explicit policy edit | "Отредактируй текст по редполитике Сбера" | `client_profile: sber` | `active` with current source; `pending_source` if source is absent, stale, or unverified |
| Independent article | "Напиши независимую статью о стратегии Сбера в AI" | `client_profile: none` | `not_applicable` |
| Independent comparison | "Сравни Сбер и Т-Банк в посте для моего канала" | `client_profile: none` unless user asks for Sber-owned voice | `not_applicable` |
| Review bypass conflict | `brief.md` has `client_profile: sber`, user asks to skip review | blocked/conflict | Sber profile cannot override `AGENTS.md` |
| Missing source claim | Source absent, writer claims full Sber-policy compliance | blocked or `changes_requested` | `pending_source`; compliance claim forbidden |

## Pass Criteria

- Intake proposes Sber-mode only for explicit client-owned or client-policy
  tasks.
- Chief Editor confirms or rejects activation before production.
- `task-manifest.md` records `client_profile`, `client_profile_status`, and
  `client_profile_files`.
- Writer and UX Writer load Sber profile files only when active.
- Review Agent applies `/kb/clients/sber/sber-review-checklist.md` only when
  active.
- Missing, stale, or unverified source policy produces `pending_source`, not
  invented rules.
- Sber profile never overrides `AGENTS.md`, selected pipeline, role separation,
  source discipline, or review-gate.
