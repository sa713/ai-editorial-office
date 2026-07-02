# Brief

Task ID: `EDITORIAL-SYSTEM-UPDATE-SBER-MODE`

## Goal

Add a task-scoped Sber client profile to the AI Editorial Office without turning
Sber editorial policy into the global editorial policy.

## Required changes

- Add `/kb/clients/sber/` scaffold.
- Define activation and non-activation rules.
- Define priority: project rules and user/task instructions stay above Sber
  profile.
- Add Sber-mode detection to Intake Agent and Chief Editor.
- Add Sber review checklist.
- Add `client_profile` fields to task manifest template/memory summary.
- Provide smoke-test scenarios.

## Constraint

The cleaned Sber editorial policy source is not present in this update package.
Do not invent Sber policy content.
