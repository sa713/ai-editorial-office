# Implementation boundaries

## Разрешенные типы правок

- Короткие markdown-level уточнения.
- Template field additions where the field changes restartability, review, governance or artifact omission clarity.
- Pipeline notes that define process depth without changing stage logic.
- Agent notes that clarify existing role behavior without adding duties.
- Cross-reference to canonical owner instead of repeating full rule.
- One-line omission rationale for compact path.
- Short semantic definitions for new/clarified terms.

## Запрещенные типы правок

- Editing core editorial philosophy.
- Adding new agents or pseudo-agents.
- Creating workflow engine, automation platform or task runtime.
- Adding scoring, eval metrics or dashboards.
- Creating new editorial modes.
- Large doctrine docs.
- Mass migration of old tasks.
- Rewriting all pipelines.
- Globally shortening all agent specs.
- Removing or weakening review-gate.
- Collapsing writing and review into one role.
- Treating finalization as publication/delivery approval.
- Making compact path available for high-governance.
- Adding broad source security framework.
- Adding long explanations inside templates.

## Требуют отдельного решения

- Any new canonical document outside target files.
- Any status model change that affects task lifecycle.
- Any pipeline stage reorder.
- Any change to role authority boundaries.
- Any rule that changes human approval requirements.
- Any source traceability reduction.
- Any automated validator or script.
- Any migration or rename in existing task folders.
- Any deletion of legacy artifacts.

## Что считается redesign и запрещено в этой итерации

Redesign means any change that changes the operating model rather than clarifying bounded behavior. In this iteration redesign includes:

- new lifecycle model;
- new role set;
- new agent hierarchy;
- replacing pipelines with engine logic;
- merging review and finalization;
- replacing editorial judgment with numeric scoring;
- rebuilding templates as forms;
- changing risk modes;
- turning compact path into a separate pipeline;
- making source trust a security subsystem;
- converting the system into a general agent platform.

## Reversibility requirement

Every implementation change must be reversible by removing a small doc block, template field or note. If rollback requires broad rewrite, the change is out of scope.

## Anti-bloat test

Before adding a field, section or file, answer:

```text
Does this change writing, review, governance or restartability?
Who owns this rule canonically?
Can another existing file carry this instead?
What is the smallest useful version?
How would we roll it back?
```
