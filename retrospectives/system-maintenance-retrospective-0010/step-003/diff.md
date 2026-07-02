# Step 3 Diff Summary

The local repository exposes these project files as untracked, so `git diff`
does not provide a reliable tracked baseline. This file records the semantic
diff applied in Step 3.

## Agent Specs

`ai-editorial-office/agents/*.md`

```diff
- Long role specs repeated global `AGENTS.md` rules, lifecycle guidance,
- pipeline sequence, artifact minimalism, review requirements, context-loading
- policy, prompt/failure behavior, and large artifact shape examples.
+ Agent specs now use a compact role-local structure:
+ mission;
+ primary responsibilities;
+ inputs;
+ outputs;
+ forbidden actions;
+ decision boundaries;
+ stop conditions;
+ handoff expectations;
+ role-specific quality checks.
```

## Canonical Ownership

```diff
- Agent files restated rules already owned by `AGENTS.md`, pipelines, and
- templates.
+ Agent files now give a short canonical-owner reference plus local
+ role-specific consequence and boundary.
```

## Role Boundaries

```diff
  Chief Editor remains coordinator and final governance owner, not writer.
  Review Agent remains independent reviewer, not rewriter.
  Final Editor remains controlled finalizer, not governance approver.
  Research Agent remains evidence owner, not writer.
  Intake Agent remains intake/classification, not analyst or designer.
  UX Writer remains interface-copy owner, not general writer.
  Writer remains draft owner, not researcher, reviewer, or finalizer.
```

## Line Count

```diff
- 3460 total lines across agent specs before Step 3.
+ 866 total lines across agent specs after Step 3.
```

## Explicit Non-Changes

```diff
  No roles added.
  No roles removed.
  No MVP agent set change.
  No pipeline change.
  No template change.
  No governance model change.
  No review optionality change.
  No automation.
  No Step 4-6 work.
```
