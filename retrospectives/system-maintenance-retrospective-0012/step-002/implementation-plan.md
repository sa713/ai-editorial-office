# Step 2 implementation plan

Status: completed.

Scope:

- Replace active `MVP` terminology with the role and operating model terms approved by Step 1.
- Edit only active policy files.
- Preserve role set, pipeline behavior, governance, review, and visual branch semantics.
- Do not edit historical retrospectives or task history.
- Do not start Step 3.

Source of truth:

- `retrospectives/system-maintenance-retrospective-0012/step-001/mvp-inventory.md`
- `retrospectives/system-maintenance-retrospective-0012/step-001/active-policy-findings.md`
- `retrospectives/system-maintenance-retrospective-0012/step-001/replacement-strategy.md`

Implementation sequence:

1. Updated `AGENTS.md` first as the governance source of truth.
2. Introduced the active terminology:
   - Core roles.
   - Extension roles.
   - Unauthorized extension roles.
   - Current operating model.
3. Updated `project-state.md` as a state mirror, not a new policy source.
4. Updated `agents/chief_editor.md` to preserve assignment boundaries.
5. Updated all pipeline role-admissibility, blocker, handoff, sequence, and restart-check wording.
6. Updated KB and `templates/agent_template.md` terminology.
7. Re-ran active-policy searches for `MVP`, `non-MVP`, and requested phrase families.

Validation performed:

- Active policy search for `\bMVP\b`, `non-MVP`, `MVP role`, `MVP agent`, `MVP workflow`, `MVP architecture`, and `MVP phase`.
- Targeted checks for:
  - Artist Agent;
  - extension role policy;
  - direct `writing` -> `review`;
  - absence of separate Editor Agent;
  - handoff validity checks;
  - pipeline role admissibility.

Result:

- Active policy no longer depends on `MVP` terminology.
- Historical files remain unchanged.
