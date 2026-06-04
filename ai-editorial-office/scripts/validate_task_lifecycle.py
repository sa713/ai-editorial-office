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
MANIFEST_STATUS_RE = re.compile(r"\b(current status|current_status|status)\b", re.IGNORECASE)
LABELED_OUTCOME_RE = re.compile(
    r"(?im)^\s*(?:review[_ -]?outcome|outcome|verdict|status)\s*:\s*"
    r"(approved|changes_requested|blocked)\b"
)
SINGLE_OUTCOME_LINE_RE = re.compile(
    r"(?im)^\s*(approved|changes_requested|blocked)\s*$"
)
ANY_OUTCOME_RE = re.compile(r"\b(approved|changes_requested|blocked)\b", re.IGNORECASE)


def usage() -> str:
    return "Usage: python3 ai-editorial-office/scripts/validate_task_lifecycle.py PATH_TO_TASK_FOLDER"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def is_blank(text: str) -> bool:
    return not text.strip()


def extract_review_outcome(text: str) -> str | None:
    """Return the first recognizable review outcome in a soft markdown shape."""
    for pattern in (LABELED_OUTCOME_RE, SINGLE_OUTCOME_LINE_RE, ANY_OUTCOME_RE):
        match = pattern.search(text)
        if match:
            return match.group(1).lower()
    return None


def validate_task(task_dir: Path) -> tuple[list[str], list[str]]:
    blockers: list[str] = []
    warnings: list[str] = []

    for file_name in REQUIRED_FILES:
        if not (task_dir / file_name).is_file():
            blockers.append(f"{file_name} is missing.")

    manifest_path = task_dir / "task-manifest.md"
    if manifest_path.is_file():
        manifest_text = read_text(manifest_path)
        if is_blank(manifest_text):
            blockers.append("task-manifest.md is empty.")
        elif not MANIFEST_STATUS_RE.search(manifest_text):
            blockers.append("task-manifest.md does not mention current status.")

    status_path = task_dir / "status.md"
    if status_path.is_file() and is_blank(read_text(status_path)):
        blockers.append("status.md is empty.")

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
