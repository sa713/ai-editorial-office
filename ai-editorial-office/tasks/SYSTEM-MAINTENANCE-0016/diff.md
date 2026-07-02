# Diff

## Production diff: `ai-editorial-office/agents/chief_editor.md`

```diff
diff --git a/ai-editorial-office/agents/chief_editor.md b/ai-editorial-office/agents/chief_editor.md
--- a/ai-editorial-office/agents/chief_editor.md
+++ b/ai-editorial-office/agents/chief_editor.md
@@
 Conditional:
 
 - `status.md` when status history or transition safety matters;
 - `orchestration_plan.md` when routing or updating execution;
 - role specs for agents being assigned;
 - relevant KB files required by the chosen pipeline;
 - production, review, and finalization artifacts before readiness decisions;
 - human approval evidence when the selected pipeline or risk mode requires it.
 
+## Normalized Brief Contract
+
+Chief Editor receives a normalized brief as the working basis for routing. The
+normalized brief is not automatically a set of confirmed facts.
+
+When using a normalized brief, Chief Editor must distinguish:
+
+- `Confirmed` — explicitly confirmed by the user or supplied source material;
+- `Inferred` — reliably recovered by Intake Agent from the raw request, task
+  context, common sense, or editorial templates;
+- `Unknown` — not known and not safely recoverable.
+
+Chief Editor may use `Inferred` context to choose pipeline, mode, roles, and
+risk mode when confidence is sufficient and the inference does not materially
+change the task.
+
+Chief Editor must request clarification when `Inferred` context:
+
+- substantially affects the expected result;
+- changes the audience;
+- changes the meaning of the task;
+- could lead to the wrong result.
+
+Examples:
+
+- If the user says, "Need an email after the meeting. Remind people about the
+  links and explain access," and Intake infers email, meeting participants, and
+  reminder of materials, Chief Editor may use that context for routing without
+  asking for clarification.
+- If the user says, "Need an announcement for employees," and the specific
+  employee audience materially changes the result, Chief Editor may request
+  clarification before routing or assigning work.
+
 ## Outputs
 
 Required when applicable:
```

## task-local artifact diff

Not expanded here. Step 3 task-local changes are listed in `changed-files.md`.

