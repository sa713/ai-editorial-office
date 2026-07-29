# Product Intent Review — Step 2 change summary

## Canonical and role diff

- `kb/task_need_recognition.md`: multi-signal advisory recommendation and
  negative-evidence contract.
- `kb/task_object_model.md`: optional recommendation/decision state semantics.
- `agents/intake_agent.md`: signal capture and no-analysis boundaries.
- `agents/chief_editor.md`: final mode, focus, evidence depth, product-first
  consequence, and authority distinctions.
- `/about` exact copies for the two changed role files.

## Template and executable diff

- Orchestration template: conditional routing/state block.
- Manifest template: optional restart-critical state.
- Task-pack generator: explicit mode parsing and conditional owner loading.
- Four synthetic task-pack fixtures.
- New routing shell/manual smoke tests.
- Extended generator and Task Need Recognition regressions.
- Test README discoverability update.

## Preserved surfaces

No changes to:

- Product Intent Review full semantic owner;
- Capability Registry;
- Professional Analysis;
- Review Agent or Final Editor;
- project state;
- Task Status Model;
- Shared Lifecycle Kernel;
- pipelines, review gates, review outcomes, or roles set;
- full analysis/output behavior;
- Step 3.

## Compatibility

Tasks with no explicit Product Intent Review mode keep the previous generated
read set. Ordinary compact tasks and explicit `not_needed` tasks do not load
the owner or add Product Intent Review output. Existing generator regressions
remain green.
