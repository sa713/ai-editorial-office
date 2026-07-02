This is a task-local system-update packet for P5. It does not contain real task
materials.

# ChatGPT P5 Report

## Git Diff Summary

Tracked diff:

```text
 ai-editorial-office/ideas/master_backlog.md        | 145 ++++++++++++++++-----
 ai-editorial-office/scripts/generate_task_pack.py  |  47 +++++++
 .../tests/test_task_pack_generator.sh              |  36 +++++
 3 files changed, 195 insertions(+), 33 deletions(-)
```

New untracked production fixtures:

- `ai-editorial-office/tests/fixtures/task_pack/source_summary_compact_evidence/`
- `ai-editorial-office/tests/fixtures/task_pack/client_profile_pending/`

New untracked task-local packet:

- `ai-editorial-office/tasks/TASK-P5-TASK-PACK-GENERATOR/`

## Production Files Changed

- `ai-editorial-office/scripts/generate_task_pack.py`
- `ai-editorial-office/tests/test_task_pack_generator.sh`
- `ai-editorial-office/tests/fixtures/task_pack/source_summary_compact_evidence/`
- `ai-editorial-office/tests/fixtures/task_pack/client_profile_pending/`
- `ai-editorial-office/ideas/master_backlog.md`

## Key Diff: Task Pack Generator

```diff
+SOURCE_EVIDENCE_MODE_RE = re.compile(
+    r"(?i)\b(compact-evidence|source-based|source-bound|task-local supplied source|"
+    r"task-local evidence|source summary reference)\b"
+)
+
+TASK_LOCAL_SOURCE_EVIDENCE_FILES = (
+    "source_summary.md",
+    "source_notes.md",
+    "source-notes.md",
+    "source-summary.md",
+    "source_evidence.md",
+    "evidence_summary.md",
+)
```

```diff
+def collect_task_local_source_evidence(
+    task_dir: Path, known_texts: list[str], known_files: list[Path]
+) -> list[Path]:
+    combined_context = "\n".join(known_texts)
+    if not SOURCE_EVIDENCE_MODE_RE.search(combined_context):
+        return []
+
+    declared_names = {path.name.lower() for path in known_files}
+    declared_context = combined_context.lower()
+    artifacts: list[Path] = []
+
+    for file_name in TASK_LOCAL_SOURCE_EVIDENCE_FILES:
+        path = task_dir / file_name
+        if not path.is_file():
+            continue
+        normalized_name = file_name.lower()
+        if normalized_name in declared_names or normalized_name in declared_context:
+            artifacts.append(path)
+
+    return artifacts
```

```diff
+    if role in {"writer", "review_agent"}:
+        for path in collect_task_local_source_evidence(task_dir, known_texts, known_files):
+            add_item(
+                sections,
+                seen,
+                "Conditional",
+                path,
+                task_dir,
+                "task-local evidence summary for source-based compact-evidence; not original source",
+            )
+            known_texts.append(read_text(path))
+            known_files.append(path)
```

## Tests / Fixtures Added Or Changed

Changed:

- `ai-editorial-office/tests/test_task_pack_generator.sh`
  - added `run_case_absent`;
  - added positive checks for writer/review_agent source summary inclusion;
  - added negative no-source checks;
  - added client-profile pending guard check.

Added:

- `ai-editorial-office/tests/fixtures/task_pack/source_summary_compact_evidence/`
  - compact-evidence / source-based fixture with declared `source_summary.md`;
  - verifies writer and review_agent include the task-local evidence artifact.
- `ai-editorial-office/tests/fixtures/task_pack/client_profile_pending/`
  - pending client-profile fixture;
  - verifies client-profile files are not included without active profile
    status.

## Test Results

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

```text
python3 -m py_compile ai-editorial-office/scripts/generate_task_pack.py
git diff --check
```

Both passed with no output.

Manual generator check on
`ai-editorial-office/tests/end_to_end_cases/system_thinking_course_task`:

- writer pack now includes `source_summary.md`;
- review_agent pack now includes `source_summary.md`;
- read-set reason says: `task-local evidence summary for source-based
  compact-evidence; not original source`.

## Implementation Notes

### Owner

Task pack generation is owned by
`ai-editorial-office/scripts/generate_task_pack.py`.

The smoke-test owner is
`ai-editorial-office/tests/test_task_pack_generator.sh`, with fixtures under
`ai-editorial-office/tests/fixtures/task_pack/`.

### Root Cause

The generator uses role-specific file allowlists such as `brief.md`, `draft.md`,
`claims-used.md`, `facts.md`, and `sources.md`. Task-local evidence summaries
like `source_summary.md` were not part of the writer or review_agent read-set
candidates, so the source-based compact-evidence case could mention the source
summary without the pack including it.

### What Changed

- Added an allowlist for task-local source/evidence summary names.
- Added source/evidence context detection for compact-evidence, source-based,
  source-bound, task-local supplied source, task-local evidence, and source
  summary references.
- Added inclusion only for writer and review_agent.
- Included the artifact only when it exists and is explicitly declared in
  known task context.
- Marked the read-set reason as task-local evidence summary, not original
  source.

### What Did Not Change

- No broad task folder dump.
- No latest-modified logic.
- No client-profile auto-activation.
- No review-gate, roles, pipelines, lifecycle, or validator changes.
- Historical E2E case reports were not rewritten.

## Check Pack

### Change Summary

P5 implements the narrow task pack generator fix identified by P1:
source-based / compact-evidence task packs now include declared task-local
source/evidence summaries for writer and review_agent.

### Key Behavior

- Includes `source_summary.md` or equivalent only when the task context declares
  source-based / compact-evidence source handling.
- Includes the file only for writer and review_agent.
- Does not include all markdown files.
- Keeps client-profile file inclusion behind explicit active profile status.
- Keeps latest modified out of source-of-truth logic.

### Risks

- The source/evidence artifact names are intentionally allowlisted. Future
  differently named artifacts will need either a declared equivalent name or a
  small allowlist update.
- Existing historical E2E case reports still record the original P1 issue; they
  were not rewritten because they are source evidence for the fix.

## Git Status Short

```text
 M ai-editorial-office/ideas/master_backlog.md
 M ai-editorial-office/scripts/generate_task_pack.py
 M ai-editorial-office/tests/test_task_pack_generator.sh
?? ai-editorial-office/tasks/
?? ai-editorial-office/tests/fixtures/task_pack/client_profile_pending/
?? ai-editorial-office/tests/fixtures/task_pack/source_summary_compact_evidence/
?? diff_intake.md
```
