# Step 6 Current-Version Decisions

## Core Rule

Version-heavy tasks must have one explicit current version pointer. The pointer
is task-local and lives in:

- `task-manifest.md`; or
- another canonical task-local owner named by `task-manifest.md`.

## Pointer Contents

The pointer must state:

- current active artifact or artifact set;
- deprecated or previous versions;
- which versions are no longer working artifacts;
- what to read on restart;
- whether a version conflict exists.

## Replacement Rule

When a new version replaces an old version, the new version or manifest must:

- link to the replaced version;
- mark the old version as deprecated or no longer working.

## Restart Rule

Restart must not:

- read all v1/v2/v3 generations automatically;
- infer current state from latest modified time;
- guess current artifact from file order or suffix;
- continue production when version state is unclear.

If version state is unclear, restart stops and routes clarification to Chief
Editor.

## Old Version Reading

Old versions are read only when:

- comparison is needed;
- retrospective analysis is required;
- there is an unresolved version conflict;
- current version is unclear;
- reviewer/governance traceability requires it.

## Boundedness

This is not:

- a version registry;
- a database;
- automation;
- version scoring;
- a sync engine;
- a document-management framework.

It is a small restart and review discipline anchored in existing task-local
artifacts.
