# Brief

## task title

Behavioral audit of the editorial system

## research goal

Analyze how the editorial system actually behaves across accumulated completed
tasks: how it understands work, routes process depth, writes, reviews,
finalizes, and where repeated system-level errors or useful mechanisms appear.

## questions to answer

- How well does intake identify audience, goal, expected result, context of use,
  and success criteria before production starts?
- How well does Chief Editor choose pipeline, depth, research need, and
  artifacts?
- What recurring writing defects appear across tasks?
- What does review catch well, what does it miss, and does it catch task
  misunderstanding or mostly text-level issues?
- Which parts and artifacts create real value, and which are mostly formal?
- Which repeated system errors are most frequent and highest impact?
- What three changes would produce the largest quality improvement?

## audience or downstream role

Primary audience: the user and future Chief Editor decisions for improving the
editorial system. Downstream use: recommendations only, no implementation in
this task.

## source materials

- Completed and near-completed folders under `ai-editorial-office/tasks/TASK-*`.
- Review artifacts, final artifacts, final decisions, research materials,
  orchestration plans, retrospectives, handoffs, status files, and other
  task-local artifacts that reveal system behavior.
- System maintenance tasks may be used as supporting evidence when they explain
  operating-model evolution, but they are not the main sample for editorial
  behavior.

## factual sensitivity

Medium. The audit is evidence-based and may guide governance changes, but it is
internal and recommendation-only.

## risk mode

Standard.

## constraints

- Do not change the editorial system during analysis.
- Do not rewrite existing project files.
- Do not change `AGENTS.md`, roles, pipelines, memory package, task statuses,
  governance, or review-gate.
- Do not modify completed task artifacts.
- All changes in this task are recommendations only.

## success criteria

- The audit explains how the editorial system works in practice.
- Repeated errors are grouped by type, frequency, impact, stage of origin,
  stage of detection, defenses, and defense effectiveness.
- Useful mechanisms and formal/low-value artifacts are separated.
- The top three improvements are prioritized and justified.
- A final editorial decision states readiness for the next development stage and
  what should or should not be changed now.

## open questions

- None blocking. Sample coverage depends on available completed task artifacts.
