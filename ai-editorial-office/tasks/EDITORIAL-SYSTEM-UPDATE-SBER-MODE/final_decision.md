# Final Decision

Task ID: `EDITORIAL-SYSTEM-UPDATE-SBER-MODE`

## decision

Approved for repository diff.

## rationale

The update adds Sber as an isolated client profile under
`/kb/clients/sber/`, imports the supplied cleaned Sber editorial policy source,
and records activation rules that prevent the profile from becoming global AI
Editorial Office policy.

## governance notes

- Review gate remains mandatory.
- Sber-mode activates only when a task is Sber-owned, Sber-product,
  Sber-communication, or explicitly asks for Sber policy/style.
- Independent materials where Sber is only a topic, source, case, example, or
  competitor stay `client_profile: none`.
- Missing, stale, or unverified Sber source requires
  `client_profile_status: pending_source`; agents must not invent rules or claim
  Sber-policy compliance.

## verification

- `/about` memory package check: passed.
- `git diff --check`: passed.
- Smoke-test scenarios: recorded in `tests/sber-mode-smoke-test.md` and
  task-local `sber-mode-smoke-test.md`.

## final status

`finalized`
