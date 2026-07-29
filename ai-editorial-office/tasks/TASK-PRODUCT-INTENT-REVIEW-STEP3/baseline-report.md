# Baseline Report

## Scope and evidence

Checked the finalized Step 1 owner, Step 2 routing/state/loading implementation,
current role specifications, research and review pipelines, Editorial Decision
Frame and Challenge Lens owners, task templates, generator tests, and repository
status on 2026-07-29.

## Existing foundation

- `/kb/product_intent_review.md` already owns the seven-element model, four
  checks, evidence/assumption/unknown separation, one-main-gap rule, bounded
  alternatives, minimum validation, product finding, and authority boundaries.
- Task Need Recognition and Chief Editor already distinguish advisory
  recommendation from the task-local `not_needed` / `limited` / `full`
  decision.
- Task-pack loading already loads the canonical owner only for `limited` and
  `full`, preserves manifest-over-orchestration restart semantics, and leaves
  `not_needed`/absent tasks compact.
- Chief Editor already records mode, limited focus, evidence depth, an initial
  production consequence, and a reroute trigger, and already states a
  product-first ordering rule.
- The existing system has one Review Pipeline and only the operational outcomes
  `approved`, `changes_requested`, and `blocked`.

## Verified Step 3 gaps

1. Research Agent does not yet have a Product Intent Review evidence-collection
   contract for `limited` versus `full`.
2. Chief Editor does not yet translate an evidence-backed product finding into
   the five named consequence classes or the complete compact product-intent
   block required in the Editorial Decision Frame.
3. Writer Agent and UX Writer do not yet have explicit product-intent
   production boundaries or a deterministic reroute obligation when production
   exposes a material product gap.
4. Review Agent and Review Pipeline do not yet define the conditional Product
   Intent Review dimension, activation/analysis/result checks, minimum
   validation checks, or explicit finding/verdict separation.
5. Final Editor does not yet explicitly preserve an approved negative finding,
   consequence, uncertainty, and owner boundary.
6. Research and review templates cannot yet express the conditional analytical
   and review trace without improvisation.
7. No executable test covers the ten authorized Step 3 cases.

## Canonical ownership decision

- Keep product-intent semantics in `/kb/product_intent_review.md`.
- Extend `/kb/editorial_planning_framework.md` only with the compact transfer
  relationship to the existing Editorial Decision Frame.
- Extend existing role and pipeline owners with role-specific or stage-specific
  consequences.
- Extend conditional sections in existing templates; create no universal
  standalone Product Intent Review template.
- Encode the ten review decisions in an executable, fixture-backed checker so
  negative findings and operational outcomes remain independently testable.

## Forbidden-surface baseline

No Step 3 need exists for a new role, pipeline, lifecycle stage, review gate,
task status, review outcome, evidence taxonomy, project-state release status,
or mandatory task-local artifact. Professional Analysis remains an open release
candidate. Step 4 is outside scope.
