# Context Loading Decisions

## Short Context Path

For ordinary restart or stage transition, read:

- `AGENTS.md` or a short reference to its active invariants;
- `task-manifest.md`;
- latest relevant handoff;
- current working artifact;
- only the directly relevant pipeline, KB file, or `editorial_knowledge` file.

This is a reading profile, not a context engine.

## What Not To Read By Default

Do not read without a specific reason:

- the whole project;
- all retrospectives;
- all old task folders;
- all artifact versions;
- all pipelines;
- all agent specs;
- all of `editorial_knowledge`.

## Expansion Levels

Compact / low-risk:

- manifest;
- current working artifact;
- `review.md` when reviewing or finalizing;
- only directly relevant rule.

Standard:

- manifest;
- `orchestration_plan.md`;
- current artifact;
- relevant handoff;
- relevant pipeline;
- relevant knowledge file.

High-governance / conflict / restart uncertainty:

- expanded reading allowed;
- source/evidence files;
- status history;
- review trail;
- governance artifacts.

Expanded reading must be tied to the current risk, conflict, decision, or traceability need.

## Legacy Task Folders

Legacy task folders are history, not templates.

They may be read only for:

- evidence of a past decision;
- comparison;
- retrospective work;
- explicit current task requirement.

They must not be used as current workflow templates.

## Old Artifact Versions

Old versions are read only when:

- comparison is needed;
- there is a version conflict;
- no current-version pointer exists;
- the task requires retrospective analysis.

## Current-Version Pointer

For version-heavy tasks, `task-manifest.md` must identify:

- current active version;
- deprecated or previous versions;
- what to read on restart;
- whether version state is clear, conflicting, or unclear.

If a version-heavy task lacks a current-version pointer, restart must stop and route to Chief Editor before old versions are treated as current.

## Governance Preservation

The short context path does not weaken review or governance:

- review remains mandatory;
- high-governance can expand reading;
- source/evidence traceability remains available when needed;
- status history, review trail, and governance artifacts remain available when they affect decisions.
