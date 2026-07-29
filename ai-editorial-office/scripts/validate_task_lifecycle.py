#!/usr/bin/env python3
"""Validate a local editorial task folder through TaskStateProjection.

The command is read-only.  Markdown task artifacts remain authoritative; the
shared parser in ``task_state.py`` is the sole normalization layer.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from task_state import EDITORIAL_ROOT, TASKS_ROOT, build_task_state


LIFECYCLE_FIXTURES_ROOT = EDITORIAL_ROOT / "tests" / "fixtures" / "task_lifecycle"
PROJECTION_FIXTURES_ROOT = (
    EDITORIAL_ROOT / "tests" / "fixtures" / "task_state_projection"
)


def usage() -> str:
    return (
        "Usage: python3 ai-editorial-office/scripts/validate_task_lifecycle.py "
        "PATH_TO_TASK_FOLDER [--format text|json] [--mode check]"
    )


def is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve(strict=True).relative_to(root.resolve(strict=True))
    except (OSError, ValueError):
        return False
    return True


def parser_root_for(task_dir: Path) -> Path | None:
    """Return the only allowed root for a production task or repo fixture."""
    if is_within(task_dir, TASKS_ROOT):
        return TASKS_ROOT
    if is_within(task_dir, LIFECYCLE_FIXTURES_ROOT):
        return LIFECYCLE_FIXTURES_ROOT
    if is_within(task_dir, PROJECTION_FIXTURES_ROOT):
        return PROJECTION_FIXTURES_ROOT
    return None


def split_diagnostics(
    projection: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    info: list[dict[str, Any]] = []
    for item in projection["diagnostics"]:
        if item["level"] == "error":
            errors.append(item)
        elif item["level"] == "warning":
            warnings.append(item)
        else:
            info.append(item)
    return errors, warnings, info


def validate_task_projection(task_dir: Path) -> dict[str, Any]:
    allowed_root = parser_root_for(task_dir)
    projection = build_task_state(
        task_dir,
        allowed_root=allowed_root if allowed_root is not None else TASKS_ROOT,
    )
    errors, warnings, info = split_diagnostics(projection)
    return {
        "schema_version": 1,
        "task_dir": str(task_dir),
        "result": "FAIL" if errors else "PASS",
        "errors": errors,
        "warnings": warnings,
        "info": info,
        "projection": projection,
    }


def validate_task(task_dir: Path) -> tuple[list[str], list[str]]:
    """Backward-compatible message-only API backed by the shared projection."""
    result = validate_task_projection(task_dir)
    return (
        [item["message"] for item in result["errors"]],
        [item["message"] for item in result["warnings"]],
    )


def location_suffix(item: dict[str, Any]) -> str:
    source = item.get("source") or {}
    file_name = source.get("file")
    if not file_name:
        return ""
    line = source.get("line")
    return f" [{file_name}:{line}]" if line else f" [{file_name}]"


def print_items(items: list[dict[str, Any]]) -> None:
    if not items:
        print("- none")
        return
    for item in items:
        print(f"- {item['message']}{location_suffix(item)}")


def print_text(result: dict[str, Any]) -> None:
    print(f"Task lifecycle validation: {result['task_dir']}")
    print(f"Blockers: {len(result['errors'])}")
    print(f"Warnings: {len(result['warnings'])}")
    print(f"Info: {len(result['info'])}")
    print()
    print("BLOCKERS:")
    print_items(result["errors"])
    print()
    print("WARNINGS:")
    print_items(result["warnings"])
    print()
    print("INFO:")
    print_items(result["info"])
    print()
    print(f"Result: {result['result']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(add_help=False, usage=usage())
    parser.add_argument("task_dir", nargs="?")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--mode", choices=("check",), default="check")
    parser.add_argument("-h", "--help", action="store_true")
    args, extras = parser.parse_known_args(argv)
    if args.help:
        print(usage())
        return 0
    if extras or not args.task_dir:
        print(usage(), file=sys.stderr)
        return 2

    task_dir = Path(args.task_dir)
    if not task_dir.exists():
        print(f"Error: path does not exist: {task_dir}", file=sys.stderr)
        print(usage(), file=sys.stderr)
        return 2
    if not task_dir.is_dir():
        print(f"Error: path is not a directory: {task_dir}", file=sys.stderr)
        print(usage(), file=sys.stderr)
        return 2

    result = validate_task_projection(task_dir)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print_text(result)
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
