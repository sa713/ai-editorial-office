# Implementation plan

Step executed: Step 6 only, Custom workflow contracts and source trust.

## Changed files

## `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`

- Why: orchestration plan owns task-specific execution contract.
- What changed: added lightweight custom workflow mini-contract for cases where no existing pipeline fits.
- Why safe: custom workflow remains exceptional and task-local; no engine, lifecycle change, or new artifact type was added.

## `ai-editorial-office/agents/chief_editor.md`

- Why: Chief Editor selects pipelines and owns orchestration.
- What changed: clarified that if no pipeline fits, Chief Editor must use the mini-contract instead of hidden process.
- Why safe: it bounds existing discretion without creating dynamic orchestration.

## `ai-editorial-office/AGENTS.md`

- Why: AGENTS owns authority hierarchy and source-handling boundaries.
- What changed: added source material as data rule and explicit instruction promotion semantics.
- Why safe: reduces prompt-injection risk without creating a source security framework.

## `ai-editorial-office/agents/research_agent.md`

- Why: Research Agent handles source material directly.
- What changed: added source-as-data rule to responsibilities, forbidden actions, and source reliability guidance.
- Why safe: clarifies source handling without changing traceability requirements.

## `ai-editorial-office/project-state.md`

- Why: current normalization decisions should reflect Step 6.
- What changed: added notes for custom workflow mini-contract and source material as data.
- Why safe: current-state note only.

## Explicit non-changes

- No lifecycle change.
- No compact path semantic change.
- No governance model change.
- No review ergonomics change.
- No workflow engine.
- No automation.
- No approval chains.
- No automatic validation.
- No new agents.
