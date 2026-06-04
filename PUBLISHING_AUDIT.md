# Publishing Audit

Date: 2026-06-04

Scope: local preflight audit before possible publication to a private GitHub
repository. No repository was created and no push was performed.

## Current Structure

- Root: bootstrap `AGENTS.md`, `.gitignore`, service docs, and project folders.
- `ai-editorial-office/`: main editorial system.
- `ai-editorial-office/AGENTS.md`: canonical editorial charter and review-gate
  owner.
- `ai-editorial-office/agents/`: role specifications.
- `ai-editorial-office/pipelines/`: editorial pipeline contracts.
- `ai-editorial-office/templates/`: task and artifact scaffolds.
- `ai-editorial-office/kb/`: knowledge base and client-specific materials.
- `ai-editorial-office/tasks/`: active and historical task folders.
- `ai-editorial-office/learn/`: reference/source documents.
- `about/`: ChatGPT memory package copies and summaries.
- `editorial_knowledge/`: editorial knowledge notes.
- `retrospectives/`: historical maintenance and review records.

## Likely Safe To Publish After Manual Review

- Root service files: `AGENTS.md`, `.gitignore`, `README.md`,
  `GITHUB_PUBLISHING_CHECKLIST.md`, `PUBLISHING_AUDIT.md`.
- Editorial system structure and generic Markdown rules in
  `ai-editorial-office/agents/`, `ai-editorial-office/pipelines/`,
  `ai-editorial-office/templates/`, `ai-editorial-office/scripts/`,
  `ai-editorial-office/tests/`, and generic `ai-editorial-office/kb/` files.
- `about/`, `editorial_knowledge/`, and `retrospectives/` may be publishable as
  system history/reference material, but should still be spot-checked because
  they may mention internal workflows, examples, or copied policy language.

## Requires Manual Review Before Publishing

- All `ai-editorial-office/tasks/TASK-*` folders: task-local artifacts may contain
  real briefs, drafts, letters, source snapshots, names, internal wording, or
  restricted working context.
- `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-*` and
  `ai-editorial-office/tasks/EDITORIAL-SYSTEM-UPDATE-SBER-MODE/`: system history
  and diffs may be acceptable, but can include sensitive policy references.
- `ai-editorial-office/kb/clients/sber/`: client-specific policy materials and
  Sber-mode checks require explicit approval before publication.
- `ai-editorial-office/learn/`: contains reference/source files, including
  large PDFs, PPTX, and DOCX files with unclear redistribution rights or internal
  origin.
- Tracked binary/source files already in Git: `.gitignore` will not remove them
  from history or the index.

## Better Not Publish Without Separate Approval

- `ai-editorial-office/tasks/TASK-0031/Редакционная политика 05.2026.pdf`:
  likely internal bank policy source material.
- `ai-editorial-office/tasks/TASK-0031/sber-editorial-policy.md`: extracted or
  converted policy material; requires explicit approval.
- `ai-editorial-office/kb/clients/sber/editorial-policy.md`: client-specific
  editorial policy content; requires explicit approval.
- `ai-editorial-office/learn/Что нужно уметь редактору Сбера.docx`: Sber-related
  learning/source document; requires explicit approval.
- `ai-editorial-office/learn/*.pdf`, `ai-editorial-office/learn/*.pptx`, and
  `ai-editorial-office/learn/*.docx`: source materials with unclear rights.
- `ai-editorial-office/tasks/TASK-0006/`, `TASK-0008/`, `TASK-0009/`,
  `TASK-0012/`, and `TASK-0023/`: filenames and artifacts indicate real
  communications, instructions, interview/source materials, or internal working
  content.
- `ai-editorial-office/tasks/TASK-0016/` through `TASK-0020/`: contain source
  PDFs and generated images; publish only after rights and sensitivity review.
- `ai-editorial-office/tasks/TASK-0010/` and `TASK-0011/`: contain DOCX/XLSX/CSV
  data files; review for source rights and data sensitivity.

## Binary And Large File Findings

- No `.env`, key, certificate, log, temp, or archive files were found by filename
  scan.
- Large files over 1 MB were found in `ai-editorial-office/learn/` and
  `ai-editorial-office/tasks/`, including PDFs, PPTX, CSV, and PNG files.
- Many binary/source files are already tracked by Git. They should be reviewed
  and, if necessary, removed from the index in a separate explicit cleanup step
  before any GitHub publication.

## Changes Made

- Updated `.gitignore` with OS/editor, secrets, logs/temp, local reports,
  archives, and large/source-material patterns.
- Created root `README.md`.
- Created `GITHUB_PUBLISHING_CHECKLIST.md`.
- Created this `PUBLISHING_AUDIT.md`.
- Created task-local editorial routing artifacts in
  `ai-editorial-office/tasks/SYSTEM-MAINTENANCE-0022/`.

## Risks Found

- Existing Git index includes binary/source files that `.gitignore` now excludes
  for future additions only.
- `ai-editorial-office/tasks/` contains real task materials and should not be
  published wholesale without review.
- Sber-specific policy materials are present and should be treated as restricted
  unless explicit approval says otherwise.
- Root `git status` initially contained an unrelated deletion:
  `sber-editorial-policy.clean.md`. It was restored during Step 0.1 so the
  preflight status no longer contains that unrelated deletion.

## Next Step

Do not push yet. First perform a separate publication cleanup decision:

1. Review tracked binary/source files with `git ls-files`.
2. Decide whether to exclude `ai-editorial-office/learn/` and selected
   `ai-editorial-office/tasks/` materials from the repository index.
3. Review Sber/client-specific files for publication permission.
4. Re-run `git status` and `git diff`.
5. Publish only to a private repository after manual approval.
