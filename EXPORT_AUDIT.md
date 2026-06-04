# Export Audit

## Checks Performed

- Recreated `/tmp/ai-editorial-office-github-export` outside the current Git
  repository.
- Copied only root service files and the safe editorial core.
- Copied generic `ai-editorial-office/kb/*.md` files only.
- Excluded `ai-editorial-office/kb/clients/` entirely.
- Excluded `ai-editorial-office/tasks/`, `ai-editorial-office/learn/`, `about/`,
  `editorial_knowledge/`, `retrospectives/`, and
  `sber-editorial-policy.clean.md`.
- Excluded `ai-editorial-office/tests/sber-mode-smoke-test.md` because it is
  Sber-mode specific.
- Checked for binary/source file extensions.
- Checked for sensitive path/name patterns.
- Checked current repository status after export creation.

## File Counts

- Export file count before manifest/audit: 52.
- Export file count after adding `EXPORT_MANIFEST.md` and `EXPORT_AUDIT.md`: 54.

## Binary/Source Check

Result: pass.

No export files matched these extensions:

`.pdf`, `.pptx`, `.docx`, `.xlsx`, `.csv`, `.png`, `.jpg`, `.jpeg`, `.webp`,
`.mp4`, `.mov`, `.mp3`, `.wav`, `.zip`, `.tar`, `.tar.gz`, `.7z`, `.rar`.

## Sensitive Path Check

Result: pass with expected false positives.

The sensitive-path scan matched only:

- `ai-editorial-office/templates/tasks/article_task_template.md`
- `ai-editorial-office/templates/tasks/research_task_template.md`
- `ai-editorial-office/templates/tasks/review_task_template.md`
- `ai-editorial-office/templates/tasks/social_task_template.md`
- `ai-editorial-office/templates/tasks/ux_writing_task_template.md`

Explanation: these are generic task templates under `templates/tasks/`, not
working task folders under `ai-editorial-office/tasks/`. They are part of the
safe editorial core and do not contain real task materials.

No `ai-editorial-office/tasks/`, `ai-editorial-office/learn/`,
`ai-editorial-office/kb/clients/`, Sber-specific files, or editorial-policy
source files were copied, except for possible textual mentions inside root
preflight documents.

## Risks

- Root preflight documents may mention excluded sensitive paths as audit
  examples; those mentions do not include full source content.
- Generic KB files were copied as safe-core candidates, but should still receive
  a final human spot-check before GitHub publication.
- The export is not a Git repository and has not been committed or pushed.

## Recommendation

This export can be used as the first candidate payload for a private GitHub
repository after a final human spot-check. It is safer than pushing the current
repository because it excludes tracked working tasks, learning/source libraries,
client-specific Sber materials, binary/source files, and historical task-local
contexts.
