# Sber Client Profile: Usage Rules

Canonical scope: `/kb/clients/sber/`

This file defines how the Sber client profile is activated and used. It does not
replace `AGENTS.md`, task instructions, `brief.md`, selected pipeline rules,
role boundaries, review-gate, factual accuracy requirements, or governance.

## Activation

Activate `client_profile: sber` only when the current task explicitly fits at
least one condition:

1. The deliverable is created for the Sber group, from Sber's point of view, or
   as a Sber-owned communication.
2. The deliverable is about a Sber product, service, interface, campaign,
   customer communication, employer communication, internal communication, or UX
   flow and is meant to sound like Sber.
3. The user explicitly asks to write, edit, adapt, or review by the Sber
   editorial policy, Sber tone, Sber style, or Sber redpolicy.
4. `brief.md`, `task-manifest.md`, or `orchestration_plan.md` already contains
   `client_profile: sber`.

## Non-activation

Do not activate Sber-mode when:

- Sber is only mentioned as a market example, case, competitor, historical
  subject, source, or object of independent analysis;
- the task is a neutral article about Sber, not a communication for Sber;
- the user asks for general AI Editorial Office style while using Sber only as a
  topic;
- Sber appears only inside source material and the user has not promoted that
  source into a client-style instruction.

When uncertain, Intake Agent may propose `client_profile: sber`, but Chief
Editor must confirm, reject, or block the activation before production.

## Manifest fields

For active Sber-mode, record the profile in `task-manifest.md`:

```yaml
client_profile: sber
client_profile_status: active | pending_source | not_applicable
client_profile_files:
  - /kb/clients/sber/usage-rules.md
  - /kb/clients/sber/editorial-policy.md
  - /kb/clients/sber/sber-review-checklist.md
```

Use `pending_source` when the task requests Sber policy compliance but the
cleaned source policy is absent, incomplete, stale, or unverified.

Use `active` only when the cleaned source policy is available, verified, and the
profile is safe to apply.

Use `not_applicable` only when Sber-mode was considered and rejected.

## Priority

For Sber tasks, apply rules in this order:

1. `AGENTS.md` and other project-level workflow/governance rules.
2. Current user instruction, if it does not conflict with project rules.
3. Task `brief.md`.
4. Selected pipeline and active role specs for workflow, ownership, and gates.
5. Sber client profile for client-specific content constraints.
6. General `/kb` style, tone, glossary, and editorial standards.
7. Task-local notes and previous drafts.

Sber rules can tighten wording, tone, naming, terminology, and review checks.
They cannot cancel review, role separation, source discipline, safety, legal
constraints, factual verification, or explicit task requirements.

## Source discipline

Do not infer Sber rules from memory, brand impressions, old examples, public
marketing pages, or unrelated Sber texts unless Chief Editor explicitly approves
those sources for the task.

If `editorial-policy.md` is still a placeholder, do not write “по редполитике
Сбера” as a quality claim. Use a safer note:

> Sber client profile was routed, but the cleaned Sber editorial-policy source
> is pending. The draft follows only the task brief and available explicit
> constraints.
