# Step 6 Diff Summary

The local repository exposes project files as untracked, so tracked `git diff`
does not provide a reliable baseline. This file records the semantic diff
applied in Step 6.

## Global Rule

`ai-editorial-office/AGENTS.md`

```diff
- Current-version guidance existed only as a short restart/context rule.
+ Added `Current-version discipline`.
+ Requires one explicit current version pointer for version-heavy tasks.
+ Allows pointer in `task-manifest.md` or another canonical task-local owner
+ named by the manifest.
+ Forbids restart guessing from version suffix, directory order, or latest
+ modified timestamp.
+ Requires stop-and-clarify with Chief Editor when version state is unclear.
+ Explicitly states this is not a registry, database, automation, scoring system,
+ sync engine, or document-management framework.
```

## Manifest Template

`ai-editorial-office/templates/artifacts/task_manifest_template.md`

```diff
+ Expanded current-version pointer fields:
+ canonical pointer owner;
+ current active artifact or set;
+ replaced version;
+ deprecated/previous versions;
+ versions no longer working artifacts;
+ version conflict state;
+ restart read target;
+ allowed old-version read reasons;
+ no latest-modified source of truth.
```

## Navigation

`about/project_tree.md`

```diff
+ Added navigation guidance for version-heavy tasks:
+ use explicit current-version pointer;
+ do not infer current artifact from newest modified time, file order, or suffix;
+ open old versions only for comparison, retrospective analysis, unresolved
+ conflict, unclear current version, or reviewer/governance traceability;
+ stop and route clarification to Chief Editor when unclear.
```

## Pipeline Restart Checks

`ai-editorial-office/pipelines/*.md`

```diff
+ Added restart checks to article, social, UX writing, review, and research
+ pipelines:
+ confirm current-version pointer when multiple versions exist;
+ do not use latest modified time as source of truth;
+ stop and ask Chief Editor if current version state is unclear.
```

## Explicit Non-Changes

```diff
  No versioning system.
  No artifact registry.
  No database logic.
  No automation.
  No orchestration engine.
  No governance model change.
  Pipelines not redesigned.
  No final review update.
```
