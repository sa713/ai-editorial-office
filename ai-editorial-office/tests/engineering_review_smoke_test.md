# Engineering Review Smoke Test

Status: manual smoke-test / synthetic examples only.

Purpose: check whether Engineering Review activates only when an engineering
surface is material and remains inactive for ordinary editorial work.

This file is not a canonical rule owner. Canonical guidance lives in
`/kb/engineering_review.md`.

## Expected Classification Labels

- `activate`: Engineering Review should be selected.
- `do_not_activate`: Engineering Review should not be selected.
- `activate_with_architecture_review`: Engineering Review should be selected
  and Architecture Review should also be considered.

## Cases

| Case | Scenario | Expected | Lenses |
| --- | --- | --- | --- |
| ER-01 | Codex changes `scripts/generate_task_pack.py` and updates tests. | `activate` | code/change safety; delivery automation; observability if output changes |
| ER-02 | A task changes `.gitignore` and publication-safe file boundaries. | `activate` | configuration; security and abuse |
| ER-03 | A GitHub Actions workflow is added with repository token permissions. | `activate` | delivery automation; security and abuse; configuration |
| ER-04 | A script changes the task-pack JSON/markdown contract consumed by Review Agent. | `activate` | interface/API; code/change safety; reliability/recovery |
| ER-05 | A validator claims improved failure diagnostics. | `activate` | observability; reliability/recovery; code/change safety |
| ER-06 | A future task introduces SQLite storage for task state. | `activate_with_architecture_review` | data/database; reliability/recovery; security and abuse |
| ER-07 | A future task optimizes a slow report generator and claims it is faster. | `activate` | performance; observability; code/change safety |
| ER-08 | A writer edits article tone in `draft.md`. | `do_not_activate` | none |
| ER-09 | A roadmap planning document is reformatted without implementation surfaces. | `do_not_activate` | none |
| ER-10 | A visual brief requests an illustration but no scripts, assets pipeline, or generated-file behavior changes. | `do_not_activate` | none |

## Pass Criteria

- Positive cases select only relevant lenses.
- Negative cases do not activate Engineering Review.
- Database/storage cases also consider Architecture Review because persistent
  task state affects system shape.
- Performance cases require measurement evidence or an explicit no-baseline
  limitation.
- No case creates a new role, pipeline, lifecycle stage, review gate, or
  mandatory artifact.
