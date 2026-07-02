# Rollback Notes

## Rollback Action

Remove the root bootstrap file:

```text
AGENTS.md
```

Remove the Step 2 retrospective folder if the documentation must also be
reverted:

```text
retrospectives/system-maintenance-retrospective-0014/step-002/
```

## Expected Effect

Removing the root bootstrap returns the repository to the previous state where
the only editorial `AGENTS.md` is nested under:

```text
ai-editorial-office/AGENTS.md
```

That would reintroduce the risk that Codex starts from the repository root and
performs direct technical production before loading the editorial charter.

## Files To Verify After Rollback

- `AGENTS.md` absent from repository root.
- `ai-editorial-office/AGENTS.md` unchanged.
- visual branch, Artist Agent, review system, and pipelines unchanged.
