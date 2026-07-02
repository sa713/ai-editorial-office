# Rollout plan

## Status

This is a future implementation plan. Do not implement during specification.

## Step 1. Behavioral boundaries and honesty rule

**Potential files**
`editorial_knowledge/01_principles.md` or another canonical editorial boundary owner.

**Why**
Set limits before adding checks.

**Dependencies**
None.

**Check after step**
No persuasion, scoring, engagement or adoption language added.

**Rollback condition**
If the rule duplicates governance broadly or changes approval semantics.

## Step 2. Failure patterns and review heuristics in editorial knowledge

**Potential files**
`editorial_knowledge/50_editorial_failure_patterns.md`, `editorial_knowledge/40_editorial_review_system.md`.

**Why**
Make the iteration diagnosis-first.

**Dependencies**
Step 1.

**Check after step**
Patterns name concrete reader-action failures and repair direction.

**Rollback condition**
If patterns become psychological labels or campaign advice.

## Step 3. Optional review block for relevant tasks

**Potential files**
Review guidance first; review template only after evidence.

**Why**
Let reviewers catch pressure issues when task type needs it.

**Dependencies**
Step 2.

**Check after step**
Block is explicitly optional and task-type dependent.

**Rollback condition**
If every review starts using it by default.

## Step 4. Optional intake/orchestration prompts

**Potential files**
Task setup scaffold or orchestration prompt owner, only if needed.

**Why**
Some tasks need first-step risk considered before writing.

**Dependencies**
Step 3 and early production feedback.

**Check after step**
Prompts are short and optional.

**Rollback condition**
If orchestration grows new required fields or hidden workflow stages.

## Step 5. Trial on 5-10 production tasks

**Potential files**
No core changes required during trial. Use task-local artifacts.

**Why**
Validate whether reader-state checks help without bloat.

**Dependencies**
Steps 1-4 as minimal implementation.

**Check after step**
Track whether repairs are bounded and whether review stays practical.

**Rollback condition**
If checks cause tone policing, delays or unnecessary artifacts.

## Step 6. Retrospective before any broader implementation

**Potential files**
New retrospective folder only.

**Why**
Prevent broader rollout before evidence.

**Dependencies**
Step 5.

**Check after step**
Decide whether to stop, keep as optional guidance, or make one narrow task-type update.

**Rollback condition**
If evidence does not show repeated value.

## Rollout guard

Pipelines are last. Do not touch them unless the trial shows repeated ambiguity that cannot be solved in editorial knowledge or review guidance.
