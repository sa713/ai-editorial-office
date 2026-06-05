This is a synthetic/sanitized end-to-end case. It is not a real task folder and does not contain real course source files, confidential methodology, internal training materials, participant data, client data, or restricted content.

# Case Report

## What Was Checked

This case checked whether the AI editorial office can produce an internal task/post for source-based course development while keeping the original course source outside the safe-core repo.

## Mechanics That Worked

- Preflight Gate selected `constrain`; this worked as protection from inventing course details, not as a safety refusal.
- Compact execution worked with one additional evidence artifact: `source_summary.md`.
- Compact-evidence fit better than no-research because the task depends on a supplied course description, even though the original file is not committed.
- Source/provenance boundary was important: the source file was used as a task-local attachment concept and summarized safely, but not imported into `kb/`, `learn/`, `tasks/`, or the repo.
- Task pack generator was useful as a read-set check for `writer` and `review_agent`.
- Review gate was not bypassed: `final.md` was created only after `review.md` recorded outcome: approved.

## What Was Useful

The useful mechanism was separating “we have a source” from “we can publish the source”. `source_summary.md` gave the writer and reviewer enough boundary context without exposing or committing the original course description.

## What Broke Or Felt Extra

Nothing blocked the case after clarifying that the course description will be an attachment for employees and does not need to be read or committed by Codex. The task pack generator may still warn about missing handoff files in compact cases; this remains a candidate convention to review across the first three case reports.

- Task pack generator did not include `source_summary.md` in writer or review_agent read sets, even though this is a source-based compact-evidence case. This should be treated as a follow-up improvement candidate for task pack generator.

## Roadmap Follow-Up

Compare the first three `case_report.md` files and decide whether compact E2E case conventions should explicitly document how to handle task-local attachments, source summaries, and expected task pack generator warnings.

- Consider updating task pack generator so source-based tasks include task-local `source_summary.md`, `source_notes.md`, or equivalent evidence summary when present.
