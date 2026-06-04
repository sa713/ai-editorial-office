# Publication Scope Proposal

## Goal

Safely publish the AI editorial office core to a private GitHub repository
without carrying over real working materials, client-specific policy files,
large source documents, binaries, or task-local context that may belong outside
GitHub.

## Recommended Strategy

Recommended strategy: create a separate clean/export branch or clean/export copy
that contains only the safe editorial core.

Do not publish the current repository as-is. The current Git index contains 964
tracked files, including 102 tracked binary/source files and 503 sensitive
candidates matched by `tasks`, `learn`, `kb/clients/sber`, Sber/editorial-policy,
or related path patterns.

Publishing the current repository after removing some tracked files from the
index is possible, but it is riskier as a first publication step because the
current branch has mixed concerns: editorial core, learning sources, historical
task artifacts, client-specific materials, generated images, and binary files.
A clean/export branch or copy gives a smaller review surface and avoids
accidentally pushing historical task or source material.

## Safe Core Candidates

Consider these files and folders as candidates for the first private GitHub
publication, after a final manual review:

- `AGENTS.md`
- `README.md`
- `.gitignore`
- `GITHUB_PUBLISHING_CHECKLIST.md`
- `PUBLISHING_AUDIT.md`
- `PUBLICATION_SCOPE_PROPOSAL.md`
- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/README.md`
- `ai-editorial-office/project-state.md`
- `ai-editorial-office/agents/`
- `ai-editorial-office/pipelines/`
- `ai-editorial-office/templates/`
- `ai-editorial-office/scripts/`
- `ai-editorial-office/tests/`
- `ai-editorial-office/kb/00_index.md`
- Generic `ai-editorial-office/kb/*.md` files that are not client-specific and
  do not contain internal or restricted materials.
- `editorial_knowledge/`, after spot-checking for internal examples or copied
  restricted language.
- `about/`, only if the memory-package copies are intentionally part of the
  publication and have been spot-checked.
- `retrospectives/`, only if historical maintenance records are approved for
  publication and do not expose sensitive client/task context.

## Exclude From First GitHub Publication

Exclude these from the first GitHub push unless there is explicit manual
approval:

- `ai-editorial-office/tasks/`
- `ai-editorial-office/learn/`
- `ai-editorial-office/kb/clients/sber/`
- `sber-editorial-policy.clean.md`
- Any Sber/editorial-policy source or derived file.
- All tracked binary/source files: PDF, PPTX, DOCX, XLSX, CSV, PNG, JPG/JPEG,
  WEBP, MP4, MOV, MP3, WAV.
- Real working tasks, including briefs, drafts, final texts, reviews, handoffs,
  source snapshots, communications, interviews, and task-local notes.
- Task-local system maintenance records if they include diffs, copied policy
  text, client-specific context, or operational history not intended for GitHub.
- Generated visual artifacts and extracted source images.

## Tracked Binary/Source Files

The tracked binary/source list contains 102 files. Main groups:

- `ai-editorial-office/tasks/TASK-0019/extracted_images/`: 83 PNG files.
- `ai-editorial-office/tasks/TASK-0019/`: 5 source/generated files, including
  PDF-derived PNG/contact sheet/visual output.
- `ai-editorial-office/tasks/TASK-0017/`: 4 files, including a source PDF and
  generated PNG/WEBP images.
- `ai-editorial-office/tasks/TASK-0020/`: 2 files, including a source PDF and
  generated PNG.
- `ai-editorial-office/tasks/TASK-0011/`: 2 CSV data files.
- `ai-editorial-office/tasks/TASK-0016/`: 1 source PDF.
- `ai-editorial-office/tasks/TASK-0018/`: 1 source PDF.
- `ai-editorial-office/tasks/TASK-0010/`: 1 XLSX file.
- `ai-editorial-office/learn/`: tracked PDF/PPTX/DOCX source materials.

The first 80 lines of `/tmp/tracked-binary-source-files.txt` are mostly
`ai-editorial-office/tasks/TASK-0019/extracted_images/*.png`, confirming that a
large part of the binary risk is generated or extracted task-local image data.

## Sensitive Candidates

The sensitive-candidate list contains 503 tracked paths. Main groups:

- `ai-editorial-office/tasks/`: all task-local working folders matched by the
  filter. These may contain real briefs, drafts, source snapshots, reviews,
  final texts, handoffs, communications, and internal context.
- `ai-editorial-office/learn/`: learning/source documents, including PDF, PPTX,
  and DOCX files with unclear rights or origin.
- `ai-editorial-office/kb/clients/sber/`: Sber/client-specific policy and review
  materials requiring explicit approval.
- `sber-editorial-policy.clean.md`: root Sber/editorial-policy candidate.
- `ai-editorial-office/tests/sber-mode-smoke-test.md`: test content mentions
  Sber mode and should be reviewed before publication.
- `ai-editorial-office/tasks/EDITORIAL-SYSTEM-UPDATE-SBER-MODE/`: system update
  history for Sber mode; review before publication.
- Task folders with obvious source or communication risk include
  `TASK-0006`, `TASK-0008`, `TASK-0009`, `TASK-0010`, `TASK-0011`,
  `TASK-0012`, `TASK-0016` through `TASK-0020`, `TASK-0023`, and `TASK-0031`.

## Proposed Next Step

Prepare a clean export directory containing only the safe core candidates, then
run a diff/inventory check against that export before creating any private
GitHub repository or push.

This is safer than cleaning the current branch first because it avoids changing
or untracking real local working materials while giving the future GitHub repo a
small, auditable first payload.

## Notes

- `.gitignore` does not remove files already tracked by Git and does not clean
  Git history.
- A private GitHub repository still moves material outside the local workspace;
  private visibility is not a substitute for source-rights, client, internal,
  or personal-data review.
- Sber/client-specific files require a separate explicit decision before any
  publication.
- Binary/source files should be excluded from the first push unless each file is
  intentionally approved.
- No files should be deleted, untracked, or history-cleaned until a separate
  cleanup step is approved.
