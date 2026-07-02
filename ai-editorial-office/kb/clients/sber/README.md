# Sber Client Profile

Client ID: `sber`

Status: `active`

This directory contains task-scoped rules for Sber-related editorial work. It is
not a global AI Editorial Office policy and must not be applied outside tasks
where Sber is the client, communication owner, product owner, or explicitly
requested editorial standard.

## Files

- `usage-rules.md` — activation rules, non-activation rules, priority, and
  manifest fields.
- `editorial-policy.md` — cleaned Markdown transcription of the Sber editorial
  policy source.
- `source-notes.md` — provenance, source status, and update notes.
- `sber-review-checklist.md` — review checklist for tasks with
  `client_profile: sber`.

## Operating rule

Use this profile only when `task-manifest.md` or `orchestration_plan.md` names:

```yaml
client_profile: sber
```

If the cleaned Sber editorial policy is missing, stale, or unverified, agents
must set:

```yaml
client_profile_status: pending_source
```

In `pending_source` status, agents may use only:

- the user's explicit task instructions;
- the task brief;
- the general AI Editorial Office rules;
- source material explicitly supplied for the task.

They must not invent Sber-specific house-style rules or claim that output fully
matches the Sber editorial policy.

When `editorial-policy.md` is present and verified, Sber-owned or explicit
Sber-policy tasks may use:

```yaml
client_profile_status: active
```

The profile still stays task-scoped and never becomes global AI Editorial Office
policy.
