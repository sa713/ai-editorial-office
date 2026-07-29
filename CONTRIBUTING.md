# Contribution Rules

This repository contains only the safe core of the AI editorial office. Treat it
as a public, reusable system skeleton: governance files, agent specifications,
pipelines, templates, generic knowledge, tests, and service documentation may
belong here when they are safe to share and useful across editorial tasks.

## Canonical Rules

- The root `AGENTS.md` is canonical for repository-wide bootstrap rules.
- `ai-editorial-office/AGENTS.md` is canonical for the editorial system itself:
  roles, lifecycle, authority, review-gate, task routing, and governance.
- Do not duplicate or override canonical rules in new documents. Prefer short
  references to the canonical owner.
- Do not change the review-gate casually. Any change that affects review
  requirements, role separation, final approval, or task lifecycle needs a
  separate explicit review.

## Allowed Changes

Contributors may add or update safe, generic system material, including:

- agent specifications;
- pipeline descriptions;
- reusable templates;
- generic knowledge base entries;
- tests and fixtures that do not contain real client data;
- service documents such as contribution, setup, or maintenance notes.

## Restricted Material

Do not add the following without a separate explicit review:

- `tasks/`;
- `learn/`;
- `kb/clients/`;
- internal documents;
- real working materials;
- personal data;
- secrets, tokens, credentials, or private configuration;
- binary files;
- source files or source exports from proprietary/private systems.

If in doubt, keep the material out of the repository and ask for review before
committing.

## Branch Names

Use short, descriptive branch names with a type prefix:

- `docs/<topic>` for documentation-only changes;
- `agents/<topic>` for agent specification changes;
- `pipelines/<topic>` for pipeline changes;
- `templates/<topic>` for template changes;
- `kb/<topic>` for generic knowledge base changes;
- `tests/<topic>` for tests.

Avoid personal names, client names, task identifiers, or confidential context in
branch names.

## Before Push

Before pushing a branch:

- run `git status --short` and make sure only intended files changed;
- inspect `git diff` for accidental policy, role, pipeline, template, or
  knowledge-base changes;
- confirm no `tasks/`, `learn/`, or `kb/clients/` content was added;
- confirm no personal data, secrets, real working materials, binary files, or
  private source exports were added;
- run the relevant tests or document why no tests apply.

## Maintaining Product Intent Review

The semantic owner is
`ai-editorial-office/kb/product_intent_review.md`. The Capability Registry,
roles, pipelines, templates, deliverable profiles, tests, and task artifacts
must reference that owner rather than copy its full contract.

Add or select an evaluation case when:

- a new material product-task class appears;
- a reproducible Product Intent failure mode is found;
- the canonical contract changes;
- regression protection is required.

Do not change the capability when only response style differs, one expert
prefers another valid formulation, the case is already inside allowed
variability, no reproducible defect exists, or the proposal expands scope
without a separate decision.

Change workflow:

1. preserve or add a failing case;
2. record the defect;
3. identify the canonical owner;
4. make the minimum owner-local patch;
5. run neighboring cases;
6. run the full Product Intent and shared regression suite;
7. obtain independent review.

Execution details, expected-result rules, repair-loop evidence, and overfit
protection live in `ai-editorial-office/tests/README.md`.

## Pull Request Checklist

Every pull request should confirm:

- [ ] The change is limited to safe core repository material.
- [ ] Canonical ownership was respected.
- [ ] `AGENTS.md` and `ai-editorial-office/AGENTS.md` were not changed unless
      the PR is explicitly about canonical governance.
- [ ] The review-gate was not changed casually.
- [ ] No `tasks/`, `learn/`, or `kb/clients/` content was added.
- [ ] No internal documents, real working materials, personal data, secrets,
      binaries, or private source exports were added.
- [ ] The branch name follows the repository naming convention.
- [ ] `git status --short` and `git diff` were checked before push.
- [ ] Relevant tests were run, or the PR explains why tests do not apply.
