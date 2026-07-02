This is a task-local system-update packet for P5. It does not contain real task
materials.

# Check Pack

## Change Summary

P5 implements the narrow task pack generator fix identified by P1:
source-based / compact-evidence task packs now include declared task-local
source/evidence summaries for writer and review_agent.

## Production Files Changed

- `ai-editorial-office/scripts/generate_task_pack.py`
- `ai-editorial-office/tests/test_task_pack_generator.sh`
- `ai-editorial-office/tests/fixtures/task_pack/source_summary_compact_evidence/`
- `ai-editorial-office/tests/fixtures/task_pack/client_profile_pending/`
- `ai-editorial-office/ideas/master_backlog.md`

## Key Behavior

- Includes `source_summary.md` or equivalent only when the task context declares
  source-based / compact-evidence source handling.
- Includes the file only for writer and review_agent.
- Does not include all markdown files.
- Keeps client-profile file inclusion behind explicit active profile status.
- Keeps latest modified out of source-of-truth logic.

## Tests

```text
PASS: writer_minimal/writer
PASS: review_with_claims/review_agent
PASS: final_editor_missing_review/final_editor
PASS: chief_editor_feedback/chief_editor
PASS: source_summary_compact_evidence/writer
PASS: source_summary_compact_evidence/review_agent
PASS: writer_minimal/writer absent checks
PASS: client_profile_pending/writer
PASS: client_profile_pending/writer absent checks
All task pack generator smoke tests passed.
```

Additional checks:

- `python3 -m py_compile ai-editorial-office/scripts/generate_task_pack.py`
  passed.
- `git diff --check` passed.
- Manual generator run on
  `ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task`
  includes `source_summary.md` for writer and review_agent.

## Risks

- The source/evidence artifact names are intentionally allowlisted. Future
  differently named artifacts will need either a declared equivalent name or a
  small allowlist update.
- Existing historical E2E case reports still record the original P1 issue; they
  were not rewritten because they are source evidence for the fix.

## What To Show ChatGPT

- `generate_task_pack.py` diff.
- `test_task_pack_generator.sh` diff.
- new source summary and client-profile guard fixtures.
- `implementation-notes.md`.
- this `check-pack.md`.
