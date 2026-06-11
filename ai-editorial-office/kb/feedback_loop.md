# Feedback Loop

This file is a compatibility entry point for older references and task-pack read
sets.

Use `customer_feedback_loop.md` as the active P5.5 workflow for customer
feedback classification, task-local `feedback.md`, engineering watchlist
signals, and backlog candidates.

Do not maintain a separate taxonomy here. The active classification is:

```text
task_local / preference / observation / confirmed_pattern / system_change_candidate
```

Core guardrails remain unchanged: one feedback item does not change the system,
`feedback.md` is optional, raw feedback stays task-local, and production changes
require a separate reviewed system update.
