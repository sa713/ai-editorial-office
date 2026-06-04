# Export Manifest

## Purpose

Clean export of the AI editorial office safe core for future private GitHub
publication.

## Included

- Root service files:
  - `AGENTS.md`
  - `README.md`
  - `.gitignore`
  - `GITHUB_PUBLISHING_CHECKLIST.md`
  - `PUBLISHING_AUDIT.md`
  - `PUBLICATION_SCOPE_PROPOSAL.md`
- Editorial system core:
  - `ai-editorial-office/AGENTS.md`
  - `ai-editorial-office/README.md`
  - `ai-editorial-office/project-state.md`
  - `ai-editorial-office/agents/`
  - `ai-editorial-office/pipelines/`
  - `ai-editorial-office/templates/`
  - `ai-editorial-office/scripts/`
  - `ai-editorial-office/tests/README.md`
- Generic knowledge files:
  - `ai-editorial-office/kb/*.md`
  - `ai-editorial-office/kb/clients/` is excluded.

## Excluded

- `ai-editorial-office/tasks/`
- `ai-editorial-office/learn/`
- `ai-editorial-office/kb/clients/`
- `about/`
- `editorial_knowledge/`
- `retrospectives/`
- `sber-editorial-policy.clean.md`
- `ai-editorial-office/tests/sber-mode-smoke-test.md`
- Sber/client-specific materials.
- Binary/source files: PDF, PPTX, DOCX, XLSX, CSV, PNG, JPG/JPEG, WEBP, MP4,
  MOV, MP3, WAV, ZIP, TAR, TAR.GZ, 7Z, RAR.
- Private working materials, task-local artifacts, source snapshots, real
  communications, generated images, and extracted source images.

## Canonical Files

- `AGENTS.md`
- `ai-editorial-office/AGENTS.md`

## Notes

This export is intentionally conservative. It does not contain working tasks,
learning/source libraries, Sber/client materials, binary/source files, or private
working materials. It is a candidate payload for a future private GitHub repo,
not a published repository.
