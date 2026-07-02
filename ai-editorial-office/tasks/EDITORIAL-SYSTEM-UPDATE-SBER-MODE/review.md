# Review

## reviewed scope

- Sber client profile files in `/kb/clients/sber/`.
- Client-profile routing rules in `AGENTS.md`, role specs, pipelines, and
  templates.
- `/about` memory package sync.
- Smoke-test coverage.

## checks performed

| Check | Result | Evidence |
| --- | --- | --- |
| `/about` package count and copied-file sync | pass | `ai-editorial-office/scripts/check_about_memory_package.sh` returned OK |
| Whitespace and patch sanity | pass | `git diff --check` returned no issues |
| Production tree ownership | pass | Canonical files updated under `ai-editorial-office/`; `/about` remains memory package |
| Sber policy isolation | pass | Full policy source appears in `/kb/clients/sber/editorial-policy.md`, root source file, and historical `TASK-0031`; not in global KB policy/tone files |
| Sber-mode activation | pass | `AGENTS.md` and `/kb/clients/sber/usage-rules.md` require explicit Sber-owned or Sber-policy task |
| Sber mention non-activation | pass | `AGENTS.md`, usage rules, and smoke tests reject mere topical mentions |
| Pending-source fallback | pass | `AGENTS.md`, usage rules, templates, agents, and smoke tests require `pending_source` if source is absent, stale, or unverified |
| Source-backed policy | pass | `editorial-policy.md` imported from `/sber-editorial-policy.clean.md`; checklist requires source-backed checks |

## findings

No blocking findings.

## notes

- Current Sber profile status can be `active` for explicit Sber-owned or
  Sber-policy tasks because the cleaned source is now present.
- The source remains client-scoped. It is not global AI Editorial Office policy.
- If the source is removed, stale, or unverified for a future task, agents must
  use `client_profile_status: pending_source` and avoid Sber-policy compliance
  claims.

## outcome

`approved`
