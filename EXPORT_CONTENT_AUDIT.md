# Export Content Audit

## Scope

Checked text content inside `/tmp/ai-editorial-office-github-export` before any
private GitHub repository creation. The audit covered Markdown and shell files
in the clean export.

This step did not modify the main repository and did not modify export files
other than creating this audit report.

## Checks

The following grep checks were performed:

- Sensitive/client/internal markers:
  `Сбер|Sber|sber|банк|bank|УЭК|ДКА|Пульс|CyberPort|внутренн|корпоративн|конфиденциальн|restricted|internal|client|клиент`
- Email-like strings.
- Russian phone-like strings.
- Secret-like strings:
  `api_key`, `secret`, `token`, `password`, `passwd`, `pwd`, `credential`,
  private-key markers, `AUTH`, and `Bearer`.
- Links/internal URL markers:
  `http(s)://`, `localhost`, `127.0.0.1`, `intranet`, `jira`, `confluence`,
  `wiki`, `sharepoint`, `corp`, `local`.

## Findings

### Sensitive/internal markers

Found 193 lines.

Most findings are expected and explainable:

- Root preflight documents (`PUBLISHING_AUDIT.md`,
  `PUBLICATION_SCOPE_PROPOSAL.md`, `EXPORT_MANIFEST.md`, `EXPORT_AUDIT.md`)
  mention excluded sensitive paths and Sber/client materials as audit examples.
  They do not include full source content.
- `ai-editorial-office/AGENTS.md`, `project-state.md`, role files, pipelines,
  and templates mention `client_profile`, `sber`, and `/kb/clients/sber/...` as
  generic routing/scaffold rules. These are system mechanics, not copied client
  policy content.
- Generic style rules mention words like `internal`, `corporate`, and `client`
  as editorial categories or anti-patterns.
- `ai-editorial-office/tests/README.md` mentions the excluded
  `sber-mode-smoke-test.md`. This is not source content, but it should be
  manually reviewed before publication because it references Sber-mode.

No copied working task, `learn/`, `kb/clients/`, Sber policy source, or bank
document content was found in the export.

### Emails

No email-like strings found.

### Phones

No Russian phone-like strings found.

### Secrets

Found 5 lines. All are false positives:

- `PUBLISHING_AUDIT.md` and `GITHUB_PUBLISHING_CHECKLIST.md` mention secrets as
  things to check for.
- `README.md` says not to publish secrets.
- `ai-editorial-office/kb/ux_writing_guidelines.md` contains the generic UX
  label example `Reset password`.
- `ai-editorial-office/scripts/check_about_memory_package.sh` contains a shell
  variable named `repo_root` assigned with `pwd`; this is not a password or
  credential.

No actual token, key, credential, `.env` value, authorization header, or private
key block was found.

### Links/internal URLs

Found 81 lines.

No `http://` or `https://` URLs were found. No `localhost`, `127.0.0.1`,
`intranet`, `jira`, `confluence`, `wiki`, or `sharepoint` hits were found.

The link/internal scan was triggered mostly by the word `local` in normal system
phrases such as `task-local`, `local AI editorial`, `local outcomes`, and
`local path`. It also found generic `corporate` wording in editorial
anti-patterns and visual-template constraints. These are not internal system
URLs or private infrastructure references.

## Files Requiring Manual Review

Review these files by eye before creating a GitHub repository:

- `ai-editorial-office/AGENTS.md`: contains Sber/client-profile routing rules
  and canonical governance language.
- `ai-editorial-office/project-state.md`: contains current Sber-mode state notes.
- `ai-editorial-office/templates/artifacts/task_manifest_template.md`: contains
  `/kb/clients/sber/...` placeholder references.
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`:
  contains `/kb/clients/sber/...` placeholder references.
- `ai-editorial-office/tests/README.md`: references the excluded
  `sber-mode-smoke-test.md`.
- `ai-editorial-office/kb/00_index.md`: references excluded client profile
  location `clients/sber/`.
- Root audit/proposal files: `PUBLISHING_AUDIT.md`,
  `PUBLICATION_SCOPE_PROPOSAL.md`, `EXPORT_MANIFEST.md`, `EXPORT_AUDIT.md`;
  these intentionally list excluded sensitive paths.

## Recommendation

The export can be used as the first payload for a private GitHub repository
after a final human spot-check of the files listed above.

No emails, phone numbers, actual secrets, binary/source files, working task
folders, learning/source libraries, or client-specific source files were found
in the clean export. The remaining findings are mostly system-rule references
and audit descriptions of excluded material.
