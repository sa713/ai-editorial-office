# Brief

## raw request summary

Make a focused system update for P1.5 raw brief normalization so the editorial
office can turn noisy natural-language user requests into working `brief.md` or
task definitions without a manual ChatGPT rewrite step.

## user goal

- confirmed: improve Intake Agent handling of raw user requests;
- confirmed: distinguish facts, assumptions, questions, unknowns, noise, and
  source status;
- confirmed: avoid fantasy requirements and architecture expansion.

## audience / reader

- confirmed: AI editorial office agents, mainly `intake_agent` and
  `chief_editor`;
- inferred: future ChatGPT/Codex reviewers using the safe-core repo.

## expected artifact

- confirmed: compact production patch in `intake_agent.md`;
- confirmed: backlog status/update in `master_backlog.md`;
- confirmed: `implementation-notes.md`, `check-pack.md`, and
  `chatgpt_report.md` for review.

## source status

- sources used: repository `AGENTS.md`, `ai-editorial-office/AGENTS.md`,
  `project-state.md`, `master_backlog.md`, current `intake_agent.md`, and
  relevant artifact/task templates;
- source status: local markdown sources available and read;
- source boundary: production files override backlog if conflicts exist.

## constraints

- no new agents;
- no review-gate changes;
- no new mandatory task artifact for every task;
- no capabilities, validators, visual subsystem, or client-profile changes;
- no broad rewrite of intake/chief editor;
- no real task materials, private data, or source files committed.

## explicit requirements

- add raw brief normalization rule;
- add minimal normalization guidance/template;
- add 2-3 sanitized examples;
- explicitly forbid inventing goals, audiences, sources, and requirements;
- update P1.5 backlog status and decision/retrospective log;
- provide a short check-pack.

## assumptions

- A compact custom system-update workflow is appropriate because no existing
  pipeline directly owns production rule patches.
- Task-local artifacts can live under `/tasks/TASK-ID/` to satisfy editorial
  entry discipline without making them safe-core production files.

## open questions

- `/about` is referenced by `project-state.md`, but no `/about` directory exists
  in this checkout; sync/check status must be reported rather than invented.

## acceptance criteria

- raw user requests have a clear path to working `brief.md` / task definition;
- facts, assumptions, questions, unknowns, and noise are separated;
- source status is explicit;
- expected artifacts and acceptance criteria are not fabricated;
- review-gate and role model are unchanged;
- backlog is updated;
- check-pack is available for review.

## suggested task type / pipeline

- task type: system update / governance patch;
- pipeline: compact custom system-update workflow, with review pending via
  `check-pack.md` / `chatgpt_report.md`.

## risks

- overlong guidance could make Intake less compact;
- examples could accidentally look like mandatory formats;
- `/about` sync cannot be completed if the memory package is absent.
