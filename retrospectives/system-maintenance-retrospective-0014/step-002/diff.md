# Diff

The project files are currently untracked in git, so this records the intended
semantic diff for the root bootstrap file.

## `AGENTS.md`

```diff
diff --git a/AGENTS.md b/AGENTS.md
new file mode 100644
--- /dev/null
+++ b/AGENTS.md
@@
+# Codex Entry Bootstrap
+
+This repository contains an editorial system in `ai-editorial-office/`.
+
+If the user request mentions `TASK-*`, work is performed in a `TASK-*` folder,
+or the task belongs to the editorial system, read
+`ai-editorial-office/AGENTS.md` before any production action.
+
+Then start the editorial entry flow there:
+
+- activate `chief_editor`;
+- determine task type;
+- choose the pipeline or mode;
+- create or update `task-manifest.md`;
+- create or update `orchestration_plan.md`;
+- update `status.md` when state changes;
+- assign the required roles.
+
+For editorial `TASK-*` work, the direct path `PDF -> SVG/PNG/MD` is forbidden
+unless the user explicitly asks to bypass the editorial process.
```

## Boundary Confirmation

```diff
+ Added root Codex entry bootstrap.
+ Required nested editorial charter loading for TASK/editorial work.
+ Required editorial entry flow before production.
+ Explicitly blocked direct PDF -> SVG/PNG/MD for editorial TASK work.
- Changed no visual branch rules.
- Changed no Artist Agent rules.
- Changed no review system.
- Changed no pipelines.
```
