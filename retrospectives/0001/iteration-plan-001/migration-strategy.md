# Migration strategy

## Strategy

Implement as small, reversible documentation and template changes. Do not migrate existing task folders. Do not rewrite all pipelines at once.

The iteration should move from design decisions to limited canonical updates, then test on new tasks.

## Dependency order

## Step 1: Approve bounded scope

Before editing system files, confirm:

- compact path is a process depth profile, not a new pipeline;
- no new agents;
- no automation;
- no scoring/eval system;
- no doctrine expansion.

Dependency: none.

## Step 2: Add artifact ownership map

Create or add ownership map in the appropriate canonical location.

Why first:

- it prevents future edits from adding more drift;
- it tells where each following change belongs.

Dependency: Step 1.

## Step 3: Define compact execution profile

Add compact path rule to system governance/process docs.

Include:

- allowed use;
- forbidden use;
- minimal artifacts;
- compact review;
- forbidden shortcuts.

Dependency: ownership map, so rule lands in correct place.

## Step 4: Update manifest guidance

Add:

- freshness block;
- normalized governance state;
- shorter late-stage next action packet guidance.

Dependency: compact path, because manifest supports compact execution.

## Step 5: Clarify handoff semantics

Define:

- role-to-role handoff;
- compact final handoff;
- context-summary.

Dependency: manifest guidance, because handoff should not duplicate manifest.

## Step 6: Add review ergonomics

Define:

- compact review;
- normal review;
- full review;
- independence check;
- bounded revision fields.

Dependency: compact path and governance state.

## Step 7: Add custom workflow mini-contract

Update orchestration guidance so custom flows include the mini-contract.

Dependency: ownership map and compact path.

## Step 8: Add source trust rule

Add small trust rule to context/source guidance and review guidance.

Dependency: none strict, but best after ownership map.

## Step 9: Test on new tasks only

Use compact path on 2-3 future tasks:

- low-risk rewrite;
- simple standard internal communication;
- source-light review.

Do not retrofit old tasks.

## Step 10: Retrospective

After test tasks, record:

- artifact count;
- omitted artifacts;
- any restart issue;
- any governance ambiguity;
- whether review quality held.

## Compatibility risks

## Risk: old tasks do not match new conventions

Legacy folders contain older handoff names and larger artifact sets.

Mitigation:

- mark legacy patterns as historical;
- do not rename old files;
- new tasks follow new guidance.

## Risk: compact path conflicts with existing pipeline text

Some pipelines currently imply fuller artifact sets.

Mitigation:

- frame compact path as risk-based artifact depth inside pipeline constraints;
- do not override high-governance requirements.

## Risk: manifest template becomes too large

Freshness and governance blocks could add overhead.

Mitigation:

- keep fields short;
- do not add long instructions to active task manifests;
- keep explanations in template or governance docs.

## Risk: review depth creates new taxonomy overhead

Compact/normal/full review could become another classification ritual.

Mitigation:

- map review depth directly from risk mode and task complexity;
- do not require long rationale unless choosing compact for standard task.

## Rollback strategy

Because changes are documentation/template-level:

1. If compact path causes governance loss, suspend compact profile and return to normal path.
2. If freshness block bloats manifest, reduce it to two fields: `Last updated by` and `Known stale risk`.
3. If review depth causes confusion, keep only compact vs full, with normal as default implicit.
4. If custom mini-contract becomes bureaucratic, reduce it to three fields: why custom, stages, review target.
5. If source trust labels create clutter, keep only the general rule and use labels only in source-heavy tasks.

## What not to migrate

Do not:

- rewrite existing task manifests;
- rename legacy handoffs;
- collapse old review artifacts;
- clean old status files;
- rebuild pipelines wholesale;
- shorten all agent specs in this iteration.

## Done condition

Migration is done when:

- next-system update has a bounded list of target docs;
- compact path is documented;
- manifest freshness and governance state are specified;
- handoff semantics are clear;
- review ergonomics are specified;
- implementation can be tested on future tasks without mass migration.
