# Feedback Loop Smoke Test

Synthetic manual smoke-test for feedback classification.

These cases are not task materials and do not define production governance.

| Case | Expected classification | Must not |
| --- | --- | --- |
| No customer feedback after delivery | no `feedback.md` | must not create placeholder feedback artifact |
| "Too long" for current result | `task_local` | must not change system rules |
| "I always want it shorter and without hype" | `preference` | must not become global editorial policy |
| Weak signal about a repeated miss | `observation` | must not write to `engineering_watchlist.md` automatically |
| Third confirmed source-status miss | `confirmed_pattern` and possible `system_change_candidate` | must not become production change without separate reviewed update |
| Concrete rewrite request for delivered artifact | `task_local` bounded revision or new task, depending on scope | must not bypass review-gate if revised material needs review |
