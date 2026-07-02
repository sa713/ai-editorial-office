# Implementation Plan

## scope

This plan covers only Step 3 of `SYSTEM-MAINTENANCE-0016`: implementing the Normalized Brief Contract in Chief Editor.

Owner for this step:

```text
ai-editorial-office/agents/chief_editor.md
```

## implementation steps

1. Add a new `Normalized Brief Contract` section to `chief_editor.md`.
2. State that normalized brief is a working routing basis, not a fully confirmed fact set.
3. Define the labels `Confirmed`, `Inferred`, and `Unknown`.
4. Allow Chief Editor to use inferred context for pipeline, mode, role, and risk-mode choices when confidence is sufficient.
5. Add escalation rule for inferred context that substantially affects result, changes audience, changes task meaning, or could cause the wrong result.
6. Add the two requested examples.
7. Update task-local governance artifacts for Step 3.

## implemented location

The contract was added after `Inputs` and before `Outputs`, because Chief Editor receives normalized briefs as input before producing routing artifacts.

## protected areas

No changes planned or made to:

- Intake Agent;
- pipelines;
- review;
- visual subsystem;
- role model;
- task status model.
