#!/usr/bin/env python3
"""Validate a local editorial task folder lifecycle.

This MVP validator is intentionally read-only. It checks basic structural and
governance invariants already defined by the editorial system sources.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = ("task-manifest.md", "status.md")
EDITORIAL_ROOT = Path(__file__).resolve().parents[1]
TASK_STATUSES_PATH = EDITORIAL_ROOT / "kb" / "task_statuses.md"
PIPELINES_DIR = EDITORIAL_ROOT / "pipelines"

CURRENT_STATUS_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:current[\s_-]*status|status)\s*:\s*(.+?)\s*$"
)
PREVIOUS_STATUS_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:previous[\s_-]*status|previous|"
    r"from[\s_-]*status)\s*:\s*(.+?)\s*$"
)
SELECTED_PIPELINE_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:selected[\s_-]*pipeline|pipeline)\s*:\s*(.+?)\s*$"
)
CODE_SPAN_RE = re.compile(r"`([a-z][a-z0-9_-]*)`", re.IGNORECASE)
LABELED_OUTCOME_RE = re.compile(
    r"(?im)^\s*(?:review[_ -]outcome|outcome|verdict|status)\s*:\s*"
    r"(approved|changes_requested|blocked)\b"
)
SINGLE_OUTCOME_LINE_RE = re.compile(
    r"(?im)^\s*(approved|changes_requested|blocked)\s*$"
)


def usage() -> str:
    return "Usage: python3 ai-editorial-office/scripts/validate_task_lifecycle.py PATH_TO_TASK_FOLDER"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def is_blank(text: str) -> bool:
    return not text.strip()


def clean_field_value(value: str) -> str:
    return value.strip().strip("`").strip()


def normalize_value(value: str) -> str:
    normalized = clean_field_value(value).lower()
    normalized = re.sub(r"[\s_-]+", "_", normalized)
    return normalized.strip("_")


def normalize_pipeline(value: str) -> str:
    cleaned = clean_field_value(value)
    if "/" in cleaned or "\\" in cleaned:
        cleaned = Path(cleaned).name
    cleaned = re.sub(r"\.md$", "", cleaned, flags=re.IGNORECASE)
    normalized = normalize_value(cleaned)
    if normalized.endswith("_pipeline"):
        normalized = normalized[: -len("_pipeline")]
    return normalized


def extract_labeled_value(text: str, pattern: re.Pattern[str]) -> str | None:
    for match in pattern.finditer(text):
        value = clean_field_value(match.group(1))
        if value:
            return value
    return None


def extract_current_status(text: str) -> str | None:
    return extract_labeled_value(text, CURRENT_STATUS_RE)


def extract_previous_status(text: str) -> str | None:
    return extract_labeled_value(text, PREVIOUS_STATUS_RE)


def extract_selected_pipeline(text: str) -> str | None:
    return extract_labeled_value(text, SELECTED_PIPELINE_RE)


def load_known_statuses(path: Path = TASK_STATUSES_PATH) -> set[str] | None:
    try:
        text = read_text(path)
    except OSError:
        return None

    allowed_section = text
    section_match = re.search(
        r"(?ims)^## allowed statuses\s*(.*?)(?:^##\s+|\Z)", text
    )
    if section_match:
        allowed_section = section_match.group(1)

    statuses = {
        normalize_value(match.group(1))
        for match in CODE_SPAN_RE.finditer(allowed_section)
    }
    return statuses or None


def parse_markdown_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    return cells if len(cells) >= 2 else None


def load_allowed_transitions(path: Path = TASK_STATUSES_PATH) -> dict[str, set[str]] | None:
    try:
        text = read_text(path)
    except OSError:
        return None

    section_match = re.search(
        r"(?ims)^## status transitions\s*(.*?)(?:^##\s+|\Z)", text
    )
    if not section_match:
        return None

    transitions: dict[str, set[str]] = {}
    for line in section_match.group(1).splitlines():
        cells = parse_markdown_table_row(line)
        if cells is None:
            continue

        from_cell, allowed_cell = cells[0], cells[1]
        if from_cell.lower() == "from" or re.fullmatch(r":?-+:?", from_cell):
            continue

        from_match = CODE_SPAN_RE.search(from_cell)
        if not from_match:
            continue

        from_status = normalize_value(from_match.group(1))
        allowed_statuses = {
            normalize_value(match.group(1))
            for match in CODE_SPAN_RE.finditer(allowed_cell)
        }
        transitions[from_status] = allowed_statuses

    return transitions or None


def extract_review_outcome(text: str) -> str | None:
    """Return the first recognizable review outcome in a soft markdown shape."""
    for pattern in (LABELED_OUTCOME_RE, SINGLE_OUTCOME_LINE_RE):
        match = pattern.search(text)
        if match:
            return match.group(1).lower()
    return None


def validate_task(task_dir: Path) -> tuple[list[str], list[str]]:
    blockers: list[str] = []
    warnings: list[str] = []
    known_statuses = load_known_statuses()
    allowed_transitions = load_allowed_transitions()

    for file_name in REQUIRED_FILES:
        if not (task_dir / file_name).is_file():
            blockers.append(f"{file_name} is missing.")

    manifest_path = task_dir / "task-manifest.md"
    manifest_status: str | None = None
    if manifest_path.is_file():
        manifest_text = read_text(manifest_path)
        if is_blank(manifest_text):
            blockers.append("task-manifest.md is empty.")
        else:
            manifest_status = extract_current_status(manifest_text)
            if manifest_status is None:
                blockers.append(
                    "task-manifest.md does not contain a recognizable current status."
                )

    status_path = task_dir / "status.md"
    status_status: str | None = None
    previous_status: str | None = None
    if status_path.is_file():
        status_text = read_text(status_path)
        if is_blank(status_text):
            blockers.append("status.md is empty.")
        else:
            status_status = extract_current_status(status_text)
            if status_status is None:
                warnings.append("status.md does not contain a recognizable current status.")
            previous_status = extract_previous_status(status_text)
            if previous_status is None:
                warnings.append("status.md does not contain a recognizable previous status.")

    if manifest_status is not None and status_status is not None:
        if normalize_value(manifest_status) != normalize_value(status_status):
            blockers.append(
                "task-manifest.md current status "
                f"`{manifest_status}` differs from status.md current status "
                f"`{status_status}`."
            )

    if known_statuses is None:
        warnings.append("Could not verify current status against known task statuses.")
    else:
        for file_name, status_label, status in (
            ("task-manifest.md", "current status", manifest_status),
            ("status.md", "current status", status_status),
            ("status.md", "previous status", previous_status),
        ):
            if status is not None and normalize_value(status) not in known_statuses:
                warnings.append(
                    f"{file_name} {status_label} `{status}` is not listed in "
                    "kb/task_statuses.md."
                )

    if allowed_transitions is None:
        warnings.append("Could not verify status transitions against kb/task_statuses.md.")

    if previous_status is not None and status_status is not None:
        previous_normalized = normalize_value(previous_status)
        current_normalized = normalize_value(status_status)
        if previous_normalized == current_normalized:
            warnings.append(
                "status.md previous status and current status are the same; "
                "transition was not validated."
            )
        elif previous_normalized == "blocked" and current_normalized == "finalized":
            blockers.append("Blocked task must not move directly to finalized.")
        elif (
            allowed_transitions is not None
            and known_statuses is not None
            and previous_normalized in known_statuses
            and current_normalized in known_statuses
            and current_normalized
            not in allowed_transitions.get(previous_normalized, set())
        ):
            blockers.append(
                f"Invalid status transition: `{previous_status}` -> `{status_status}` "
                "is not allowed by kb/task_statuses.md."
            )

    selected_pipeline: str | None = None
    for path in (manifest_path, task_dir / "orchestration_plan.md"):
        if path.is_file():
            pipeline = extract_selected_pipeline(read_text(path))
            if pipeline:
                selected_pipeline = pipeline
                break

    if selected_pipeline is None:
        warnings.append(
            "Selected pipeline was not found in task-manifest.md or "
            "orchestration_plan.md."
        )
    else:
        pipeline_name = normalize_pipeline(selected_pipeline)
        pipeline_path = PIPELINES_DIR / f"{pipeline_name}_pipeline.md"
        if not pipeline_path.is_file():
            blockers.append(
                f"Selected pipeline `{selected_pipeline}` does not map to an "
                "existing pipeline file."
            )

    final_path = task_dir / "final.md"
    review_path = task_dir / "review.md"
    has_final = final_path.is_file()
    has_review = review_path.is_file()

    if has_final and not has_review:
        blockers.append("final.md exists but review.md is missing.")

    review_outcome: str | None = None
    if has_review:
        review_text = read_text(review_path)
        review_outcome = extract_review_outcome(review_text)
        if review_outcome is None:
            blockers.append("review.md does not contain a recognized outcome.")

    if has_final and has_review:
        if review_outcome is None:
            blockers.append("final.md exists but review outcome is missing.")
        elif review_outcome != "approved":
            blockers.append(
                f"final.md exists but review outcome is {review_outcome}, not approved."
            )

    return blockers, warnings


def print_results(task_dir: Path, blockers: list[str], warnings: list[str]) -> None:
    result = "FAIL" if blockers else "PASS"
    print(f"Task lifecycle validation: {task_dir}")
    print(f"Blockers: {len(blockers)}")
    print(f"Warnings: {len(warnings)}")
    print()
    print("BLOCKERS:")
    if blockers:
        for blocker in blockers:
            print(f"- {blocker}")
    else:
        print("- none")
    print()
    print("WARNINGS:")
    if warnings:
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("- none")
    print()
    print(f"Result: {result}")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(usage(), file=sys.stderr)
        return 2

    task_dir = Path(argv[1])
    if not task_dir.exists():
        print(f"Error: path does not exist: {task_dir}", file=sys.stderr)
        print(usage(), file=sys.stderr)
        return 2
    if not task_dir.is_dir():
        print(f"Error: path is not a directory: {task_dir}", file=sys.stderr)
        print(usage(), file=sys.stderr)
        return 2

    blockers, warnings = validate_task(task_dir)
    print_results(task_dir, blockers, warnings)
    return 1 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
