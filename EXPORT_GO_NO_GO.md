# Export GO/NO-GO Review

## Scope

Final manual review of the clean export at
`/tmp/ai-editorial-office-github-export` before creating a future private GitHub
repository.

The review focused on files that still contained meaningful Sber/client-profile,
internal, local, corporate, or audit-related markers after automated checks.

## Reviewed Files

- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/project-state.md`
- `ai-editorial-office/kb/00_index.md`
- `ai-editorial-office/tests/README.md`
- `ai-editorial-office/templates/artifacts/task_manifest_template.md`
- `ai-editorial-office/templates/artifacts/orchestration_plan_template.md`
- `PUBLISHING_AUDIT.md`
- `PUBLICATION_SCOPE_PROPOSAL.md`
- `EXPORT_MANIFEST.md`
- `EXPORT_AUDIT.md`
- `EXPORT_CONTENT_AUDIT.md`

## Decision

GO WITH CAVEATS: the export can be used as the first payload for a private
GitHub repository, provided the repository is created as private and the user
accepts that Sber-mode references remain in the exported system as mechanics.

The export does not contain the excluded source areas: working `tasks/`,
`learn/`, `kb/clients/`, `about/`, `editorial_knowledge/`, `retrospectives/`,
or binary/source files.

## Sber-mode Decision

Sber-mode references are acceptable in private repo as system mechanics.

Reason: the reviewed files include routing/scaffold references to `sber`,
`client_profile`, and `/kb/clients/sber/...`, but they do not include the actual
Sber client profile directory, Sber editorial policy source, extracted policy
content, real Sber tasks, or bank documents. The references explain how the
system would activate a client profile if such files are present; they are not
client-specific policy content themselves.

Caveat: if the future repo should be generic/public-looking even though private,
these references can be generalized later in a separate editing step.

## Findings

### Real working materials

Not found.

No working `tasks/` folder, task-local briefs, drafts, source snapshots,
handoffs, final materials, or generated task outputs are present in the export.

### Personal data

Not found.

Automated email and phone checks found no email-like strings and no Russian
phone-like strings. Manual review of the target files did not find names,
employee contacts, client data, or personal identifiers.

### Client-specific policy content

Not found.

The export contains Sber-mode/client-profile mechanics and placeholder paths,
but not the actual `ai-editorial-office/kb/clients/sber/` files, not
`sber-editorial-policy.clean.md`, and not copied policy fragments.

### Internal systems or URLs

Not found.

No `http://` or `https://` links, `localhost`, `127.0.0.1`, `intranet`, `jira`,
`confluence`, `wiki`, or `sharepoint` references were found. The link scan
mostly matched generic words such as `local` and `corporate`.

### Secrets

Not found.

The secret scan produced only false positives: checklist/audit mentions of
secrets, the generic UX label `Reset password`, and shell `pwd` used to compute
a repository path.

### Remaining caveats

- Sber-mode is visible as a named system mechanism in `AGENTS.md`,
  `project-state.md`, templates, `kb/00_index.md`, and `tests/README.md`.
- `ai-editorial-office/tests/README.md` references the excluded
  `sber-mode-smoke-test.md`; the file itself was not exported.
- Root audit/proposal files intentionally mention excluded sensitive paths as
  evidence of what was left out.
- Generic KB files were included and should still receive a final human
  spot-check before the first push.

## Recommended Next Step

Create a private GitHub repository from the clean export after user approval.

Do not use the current main repository as the first payload. Use
`/tmp/ai-editorial-office-github-export` as the source for the initial private
repo contents.
