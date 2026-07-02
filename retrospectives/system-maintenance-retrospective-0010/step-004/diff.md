# Step 4 Diff Summary

The local repository exposes project files as untracked, so tracked `git diff`
is not a reliable baseline. A temporary template baseline was used during this
step, and this file records the semantic diff applied in Step 4.

## Template Compression

`ai-editorial-office/templates/**/*.md`

```diff
- Long templates repeated AGENTS rules, pipeline sequence, role behavior,
- artifact minimalism policy, context-loading policy, and long explanatory
- prose.
+ Templates now focus on working forms: purpose, required fields, short fill
+ prompts, conditional creation rules, downstream consumers, and governance
+ fields.
```

## Line Count

```diff
- 5767 total lines across unique template markdown files before Step 4.
+ 1735 total lines across unique template markdown files after Step 4.
```

## Preserved Fields

```diff
  Risk mode and process depth preserved.
  Review verdict and reviewer independence preserved.
  Blockers and open questions preserved.
  Human approval and final decision fields preserved.
  Source/evidence fields preserved where needed.
  Current-version pointer preserved in task manifest.
  Short restart read path preserved.
```

## Conditional Artifacts

```diff
- Conditional artifacts appeared in long lifecycle checklists and could read as
- routine required files.
+ Conditional artifacts are now explicitly conditional:
+ `qa-checklist.md`, `review-summary.md`, `open-questions.md`,
+ `finalization-notes.md`, and `finalization-checklist.md`.
```

## Explicit Non-Changes

```diff
  No role changes.
  No pipeline changes.
  No governance model changes.
  Review was not made optional.
  Mandatory governance fields were not removed.
  No new templates were created.
  No Step 5-6 work was started.
```
