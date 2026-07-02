# Production stabilization plan

## What to observe

- Artifact count by task type.
- How often compact path is used.
- Whether compact tasks still pass meaningful review.
- Whether manifest is current at restart.
- Whether handoffs stay short.
- Whether custom workflows are exceptional.
- Whether source instructions are treated as data.

## What to measure qualitatively

- Did each artifact change a downstream decision?
- Could another agent restart from manifest/status/handoff?
- Did review identify reader outcome, blockers, and next action?
- Did bounded revision avoid unnecessary rewrite?
- Did final decision preserve publication/delivery approval boundary?
- Did the task feel lighter without becoming less safe?

## When to revisit architecture

Revisit only after repeated production failures, not after one awkward task.

Valid triggers:

- same drift appears in three or more tasks;
- compact path causes actual governance or review failure;
- restart fails despite manifest/status/handoff being present;
- custom workflows repeat and create handoff/review confusion;
- review artifacts repeatedly fail to guide repair.

## What counts as repeated failure

Repeated failure means the same operational problem recurs across different tasks, roles, or task types after the current rule has been applied correctly.

It does not mean:

- one poorly filled template;
- one missing handoff;
- one oversized review;
- one task with unusual source material.

## When iteration-002 would become justified

Iteration-002 becomes justified only if stabilization shows repeated failures that cannot be fixed by trimming, better owner references, or tighter use of existing rules.

Until then: stabilize, observe, and avoid expansion.
