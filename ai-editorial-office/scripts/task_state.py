#!/usr/bin/env python3
"""Public facade for the disposable, read-only Task Object projection.

Markdown task artifacts remain authoritative.  The facade coordinates bounded
I/O with lifecycle rule evaluation and preserves the established import and CLI
surface.  It never writes task files, creates caches, routes work, or repairs
conflicts.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from task_state_io import (
    EDITORIAL_ROOT,
    PROJECTION_VERSION,
    TASKS_ROOT,
    read_initial_inputs,
    revalidate_inputs,
)
from task_state_rules import _build_task_state_projection
from task_state_types import Diagnostic, LocatedValue, SourceLocation, utc_now


def build_task_state(
    task_dir: str | Path,
    *,
    allowed_root: str | Path | None = None,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """Return the established JSON-compatible, read-only projection."""

    return _build_task_state_projection(
        task_dir,
        allowed_root=allowed_root,
        generated_at=generated_at,
        read_inputs=read_initial_inputs,
        revalidate=revalidate_inputs,
    )


def print_text(projection: dict[str, Any]) -> None:
    task = projection["task"]
    print("# Task State Projection")
    print()
    print(f"Task ID: {task.get('task_id') or 'unknown'}")
    print(f"Current status: {task.get('current_status') or 'unknown'}")
    print(f"Current stage: {task.get('current_stage') or 'unknown'}")
    print(f"Compatibility mode: {task.get('compatibility_mode')}")
    print(f"Valid for execution: {str(projection['valid_for_execution']).lower()}")
    print()
    print("## Diagnostics")
    if not projection["diagnostics"]:
        print("- none")
    for item in projection["diagnostics"]:
        location = item.get("source") or {}
        suffix = ""
        if location.get("file"):
            suffix = f" [{location['file']}"
            if location.get("line"):
                suffix += f":{location['line']}"
            suffix += "]"
        print(f"- {item['level'].upper()} {item['code']}: {item['message']}{suffix}")


def usage() -> str:
    return (
        "Usage: python3 ai-editorial-office/scripts/task_state.py "
        "PATH_TO_TASK_FOLDER [--format text|json]"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(add_help=False, usage=usage())
    parser.add_argument("task_dir", nargs="?")
    parser.add_argument("--format", choices=("text", "json"), default="json")
    parser.add_argument("-h", "--help", action="store_true")
    args, extras = parser.parse_known_args(argv)
    if args.help:
        print(usage())
        return 0
    if extras or not args.task_dir:
        print(usage(), file=sys.stderr)
        return 2
    projection = build_task_state(args.task_dir)
    if args.format == "json":
        print(json.dumps(projection, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print_text(projection)
    return 1 if any(
        item["level"] == "error" for item in projection["diagnostics"]
    ) else 0


if __name__ == "__main__":
    raise SystemExit(main())
