# Step 2 Diff Summary

The local repository exposes project files as untracked, so `git diff` does not provide a reliable tracked baseline. This file records the semantic diff applied in Step 2.

## Global Context Loading

`ai-editorial-office/AGENTS.md`

```diff
+ Added short context path for ordinary restart and stage transition:
+ AGENTS/invariants, task-manifest, latest relevant handoff,
+ current working artifact, and only directly relevant pipeline/KB/editorial knowledge.

+ Added "do not read by default" list:
+ whole project, all retrospectives, all old task folders, all versions,
+ all pipelines, all agent specs, all editorial_knowledge.

+ Added context expansion levels:
+ compact / low-risk, standard, high-governance / conflict / restart uncertainty.

+ Added rules for legacy task folders and old artifact versions.
+ Added requirement that version-heavy tasks use manifest current-version pointers.
```

## Manifest Template

`ai-editorial-office/templates/artifacts/task_manifest_template.md`

```diff
+ Added `current version pointers` section:
+ current active version;
+ deprecated/previous versions;
+ read on restart;
+ version conflict state.

+ Updated next-action read packet to prefer manifest, latest relevant handoff,
+ current working artifact, and directly relevant rule files.
```

## Navigation

`about/project_tree.md`

```diff
+ Added Context Navigation section.
+ Clarified legacy task folders are read only for evidence, comparison,
+ retrospective work, or explicit task requirement.
+ Clarified old artifact versions are read only for comparison, version conflict,
+ missing current-version pointer, or retrospective work.
```

## Pipelines

`ai-editorial-office/pipelines/*.md`

```diff
- Restart sections listed long detailed file sets as common restart reads.
+ Restart sections now defer to AGENTS short context path.
+ Expanded reading remains allowed for high-governance, conflict, evidence,
+ review, governance, product-context, or restart uncertainty.

- Required input sections implied broad preload.
+ Required input sections now say inputs are read only when relevant to current
+ stage or selected depth.
```

## Role Specs And Scaffolds

`ai-editorial-office/agents/*.md`
`ai-editorial-office/templates/agent_template.md`
`ai-editorial-office/templates/tasks/*_task_template.md`

```diff
- Context loading lists preloaded brief/status/orchestration/pipeline/spec files.
+ Context loading now follows AGENTS short context path and expands only for
+ scope, governance, conflict, comparison, traceability, or restart uncertainty.
```

## Explicit Non-Changes

```diff
  Review remains mandatory.
  Governance model unchanged.
  Roles unchanged.
  Pipelines not replaced.
  No context engine added.
  No automation added.
  No Step 3-6 work started.
```
