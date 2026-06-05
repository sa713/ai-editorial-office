# Feedback Loop Smoke Test

Synthetic manual smoke-test for feedback classification.

These cases are not task materials and do not define production governance.

| Case | Expected classification | Must not |
| --- | --- | --- |
| Single minor reaction | `task-local note` | must not change `AGENTS.md` |
| Concrete rewrite request | `bounded revision` | must not become system rule |
| Concrete revision with possible repeated style signal | `bounded revision + possible pattern watch` | must not create system change proposal from one signal; must not update KB with raw feedback |
| Accepted result with future preference | `task-local note + future preference watch` | must not reopen task automatically; must not create bounded revision without explicit current-artifact change request |
| Repeated style complaint | `possible system pattern` | must not update KB with raw feedback |
| Repeated governance failure | `system change proposal` | must not change production files without reviewed update |
