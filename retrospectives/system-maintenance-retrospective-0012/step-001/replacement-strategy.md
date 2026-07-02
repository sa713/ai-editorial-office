# Replacement strategy

## Goal

Replace active `MVP` terminology without changing operational meaning.

The target state should make the system read as production-ready while preserving:

- core role boundaries;
- explicit extension-role legalization;
- Artist Agent's bounded visual-branch scope;
- no separate Editor Agent in the default model;
- direct `writing` / `ux-writing` -> `review` validity;
- existing review-gate and governance behavior;
- artifact minimalism.

## Recommended vocabulary

| Current use | Replace with | Use when |
| --- | --- | --- |
| `MVP agent set`, `MVP agents`, `MVP roles` | `core role set`, `core roles`, `core agents` | The sentence defines or checks the ordinary text-task role set. |
| `MVP production roles` | `core production roles` | The sentence refers to roles that own regular production work. |
| `non-MVP extension roles` | `unauthorized extension roles` or `extension roles not explicitly legalized` | The sentence is a ban/escalation condition. |
| `MVP default workflow`, `MVP default production sequence` | `default operating workflow`, `default production sequence` | The sentence defines lifecycle or stage order. |
| `valid in MVP`, `optional in MVP` | `valid in the current operating model`, `optional in the current operating model` | The sentence defines status semantics or transitions. |
| `MVP artifacts` | `required production artifacts` or `required operating artifacts` | The sentence is about artifact obligations, not roles. |
| `MVP execution` | `current operating model` | The sentence names the active editorial authority. |

## Safe sequence for a later Step 2

1. Define the replacement terms first in `AGENTS.md`.
   - `core roles`: ordinary text-task roles.
   - `extension roles`: roles outside the core set.
   - `legalized extension roles`: extension roles explicitly allowed by `AGENTS.md`.
   - `unauthorized extension roles`: extension roles not explicitly legalized or used outside allowed scope.
   - `current operating model`: lifecycle, status, handoff, artifact, and review-gate rules.

2. Replace role-set terminology in the governance source of truth.
   - Start with `AGENTS.md`.
   - Preserve the exact ordinary text-task role list.
   - Preserve Artist Agent as a bounded legalized extension, not a core role.

3. Update the Chief Editor role spec.
   - Replace `existing MVP roles` with `current core roles or explicitly legalized extension roles`.
   - Replace `non-MVP roles` with `unauthorized extension roles`.
   - Keep the role boundary self-check.

4. Update pipeline role-admissibility language consistently.
   - `By default, only core roles may be used...`
   - `Legalized extension roles may be assigned only under AGENTS.md conditions...`
   - Blocking/escalation conditions should mention unauthorized production/extension roles, not all extensions.

5. Update workflow/status language separately.
   - Replace `MVP default production sequence` with `Default production sequence`.
   - Replace `valid in MVP` with `valid in the current operating model`.
   - Keep direct `writing` -> `review` and `ux-writing` -> `review` rules intact.

6. Update KB and template wording after governance and pipelines.
   - `agent_template.md` should allow role creation only after governance adds a core role or legalizes an extension.
   - `glossary.md` should use `active role`, `core role`, and `legalized extension role` where appropriate.
   - `editorial_policy.md` should block missing required core/legalized-extension roles and artifacts.

7. Leave historical files unchanged.
   - Retrospectives and task histories should remain the audit trail.
   - New reports can explain that old `MVP` language maps to the former terminology.

## Do not use

Avoid these replacements:

- `MVP roles` -> `production roles` everywhere.
  - This can make Artist Agent or future roles look broadly assignable.
- `non-MVP roles` -> `extension roles` everywhere.
  - This can accidentally ban already legalized extensions.
- `MVP workflow` -> `core roles`.
  - Workflow/status semantics are not role-set semantics.
- removing `MVP` without adding a clarifying noun.
  - Some sentences would lose the boundary they currently enforce.

## Minimal safe terminology map

If the next step needs the smallest safe patch, use this map:

- `MVP agent set` -> `core role set`
- `MVP agents` -> `core roles`
- `MVP roles` -> `core roles`
- `Non-MVP extension roles are forbidden...` -> `Unauthorized extension roles are forbidden...`
- `non-MVP role that is not explicitly legalized` -> `unauthorized extension role`
- `MVP default workflow` -> `default operating workflow`
- `MVP default production/review sequence` -> `default production/review sequence`
- `in MVP` for status/transition rules -> `in the current operating model`

## Validation checklist for later implementation

After any later replacement step, run:

- active policy `rg -n -i '\bMVP\b'` over the active-policy paths;
- exact phrase search for `non-MVP`, `MVP roles`, `MVP agents`, `MVP workflow`;
- targeted checks for `Artist Agent`, `extension role`, `core role`, `unauthorized extension`;
- review of all pipeline blocker/restart checks;
- review of direct writing-to-review rules;
- review of no-separate-Editor-Agent wording.
