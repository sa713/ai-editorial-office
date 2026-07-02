# Step 2 Implementation Plan

## Scope

Step: `system-maintenance-retrospective-0010 / step-002`

Focus: short context loading profile.

Goal: reduce limit usage and speed up editorial work by defining a short reading path for ordinary restart and stage transition.

## Implementation Steps

1. Add global short context loading policy to `AGENTS.md`.
2. Define what not to read without cause:
   - whole project;
   - all retrospectives;
   - all old task folders;
   - all artifact versions;
   - all pipelines;
   - all agent specs;
   - all of `editorial_knowledge`.
3. Add context expansion levels:
   - compact / low-risk;
   - standard;
   - high-governance / conflict / restart uncertainty.
4. Add legacy task folder and old artifact version reading rules.
5. Add current-version pointer fields to `task_manifest_template.md`.
6. Normalize restart/context loading language in direct consumers:
   - pipelines;
   - role specs;
   - task/agent scaffolds that contained broad restart lists.
7. Add navigation guidance to `project_tree.md`.
8. Verify no context engine, automation, role, review, or governance changes were introduced.

## Non-Goals

- No role changes.
- No pipeline replacement.
- No mass template redesign.
- No new production artifacts.
- No optional review.
- No governance model change.
- No Step 3-6 work.
- No automation.
- No context engine.

## Status

Completed.
