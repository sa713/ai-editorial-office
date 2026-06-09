#!/usr/bin/env python3
"""Generate a minimal read-only task context pack for a role.

This helper prints a recommended read set. It does not route the task, inspect
the whole project, create files, update files, or replace role judgment.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


SUPPORTED_ROLES = {"writer", "ux_writer", "review_agent", "final_editor", "chief_editor"}
EDITORIAL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = EDITORIAL_ROOT.parent
PIPELINES_DIR = EDITORIAL_ROOT / "pipelines"
KB_DIR = EDITORIAL_ROOT / "kb"

SELECTED_PIPELINE_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:selected[\s_-]*pipeline|pipeline)\s*:\s*(.+?)\s*$"
)
CURRENT_ARTIFACT_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:current(?:[\s_-]*(?:working|active))?"
    r"[\s_-]*(?:artifact|version)|current[\s_-]*(?:artifact|version))"
    r"\s*:\s*(.+?)\s*$"
)
CLIENT_PROFILE_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?client[\s_-]*profile\s*:\s*(.+?)\s*$"
)
CLIENT_PROFILE_STATUS_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?client[\s_-]*profile[\s_-]*status\s*:\s*(.+?)\s*$"
)
CLIENT_PROFILE_FILE_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(/?kb/clients/[^\s`]+|ai-editorial-office/kb/clients/[^\s`]+)\s*$"
)
SOURCE_KEYWORD_RE = re.compile(
    r"(?i)\b(source|source-notes|provenance|pending_source|active|stale|deprecated)\b"
)
SOURCE_EVIDENCE_MODE_RE = re.compile(
    r"(?i)\b(compact-evidence|source-based|source-bound|task-local supplied source|"
    r"task-local evidence|source summary reference)\b"
)

ROLE_FILES: dict[str, tuple[str, ...]] = {
    "writer": (
        "brief.md",
        "normalized-brief.md",
        "research.md",
        "facts.md",
        "claims-used.md",
        "sources.md",
        "draft.md",
    ),
    "ux_writer": (
        "brief.md",
        "normalized-brief.md",
        "content-map.md",
        "states-table.md",
        "terminology-notes.md",
        "ux-copy.md",
        "ux-writer-notes.md",
    ),
    "review_agent": (
        "brief.md",
        "normalized-brief.md",
        "draft.md",
        "ux-copy.md",
        "final.md",
        "research.md",
        "facts.md",
        "claims_table.md",
        "claims-used.md",
        "sources.md",
        "review.md",
    ),
    "final_editor": (
        "final.md",
        "draft.md",
        "ux-copy.md",
        "review.md",
        "final_decision.md",
        "finalization-notes.md",
        "finalization-checklist.md",
    ),
    "chief_editor": (
        "brief.md",
        "normalized-brief.md",
        "orchestration_plan.md",
        "review.md",
        "final_decision.md",
        "feedback.md",
        "system_change_proposal.md",
    ),
}

EVIDENCE_FILES = {"claims-used.md", "claims_table.md", "facts.md", "sources.md"}
TASK_LOCAL_SOURCE_EVIDENCE_FILES = (
    "source_summary.md",
    "source_notes.md",
    "source-notes.md",
    "source-summary.md",
    "source_evidence.md",
    "evidence_summary.md",
)


@dataclass
class ReadItem:
    display_path: str
    reason: str


def usage() -> str:
    roles = ", ".join(sorted(SUPPORTED_ROLES))
    return (
        "Usage: python3 ai-editorial-office/scripts/generate_task_pack.py "
        f"PATH_TO_TASK_FOLDER ROLE\nSupported roles: {roles}"
    )


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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


def display_path(path: Path, task_dir: Path) -> str:
    if path.is_absolute():
        try:
            return str(path.relative_to(task_dir))
        except ValueError:
            try:
                return str(path.relative_to(REPO_ROOT))
            except ValueError:
                return str(path)
    return str(path)


def resolve_task_path(task_dir: Path, value: str) -> Path:
    cleaned = clean_field_value(value)
    if cleaned.startswith("./"):
        cleaned = cleaned[2:]
    if cleaned.startswith("/"):
        cleaned = cleaned[1:]
    return task_dir / cleaned


def resolve_repo_path(value: str) -> Path:
    cleaned = clean_field_value(value)
    if cleaned.startswith("/"):
        return EDITORIAL_ROOT / cleaned.lstrip("/")
    if cleaned.startswith("ai-editorial-office/"):
        return REPO_ROOT / cleaned
    if cleaned.startswith("kb/"):
        return EDITORIAL_ROOT / cleaned
    return REPO_ROOT / cleaned


def add_item(
    sections: dict[str, list[ReadItem]],
    seen: dict[str, ReadItem],
    section: str,
    path: Path,
    task_dir: Path,
    reason: str,
) -> None:
    shown = display_path(path, task_dir)
    if shown in seen:
        if reason not in seen[shown].reason:
            seen[shown].reason = f"{seen[shown].reason}; {reason}"
        return
    item = ReadItem(shown, reason)
    seen[shown] = item
    sections[section].append(item)


def collect_handoff(task_dir: Path) -> Path | None:
    compact = task_dir / "compact-handoff.md"
    if compact.is_file():
        return compact
    candidates = sorted(
        path
        for path in task_dir.glob("handoff*.md")
        if path.is_file() and path.name != "compact-handoff.md"
    )
    return candidates[-1] if candidates else None


def extract_client_profile_files(text: str) -> list[str]:
    return [clean_field_value(match.group(1)) for match in CLIENT_PROFILE_FILE_RE.finditer(text)]


def task_mentions_source(task_dir: Path, known_texts: list[str], known_files: list[Path]) -> bool:
    if any(SOURCE_KEYWORD_RE.search(text) for text in known_texts):
        return True
    return any(SOURCE_KEYWORD_RE.search(path.name) for path in known_files)


def collect_task_local_source_evidence(
    task_dir: Path, known_texts: list[str], known_files: list[Path]
) -> list[Path]:
    combined_context = "\n".join(known_texts)
    if not SOURCE_EVIDENCE_MODE_RE.search(combined_context):
        return []

    declared_names = {path.name.lower() for path in known_files}
    declared_context = combined_context.lower()
    artifacts: list[Path] = []

    for file_name in TASK_LOCAL_SOURCE_EVIDENCE_FILES:
        path = task_dir / file_name
        if not path.is_file():
            continue
        normalized_name = file_name.lower()
        if normalized_name in declared_names or normalized_name in declared_context:
            artifacts.append(path)

    return artifacts


def generate_pack(task_dir: Path, role: str) -> tuple[dict[str, list[ReadItem]], list[str], list[str], list[str]]:
    sections: dict[str, list[ReadItem]] = {
        "Required": [],
        "Role-specific": [],
        "Conditional": [],
    }
    seen: dict[str, ReadItem] = {}
    blockers: list[str] = []
    warnings: list[str] = []
    not_included: list[str] = []
    known_texts: list[str] = []
    known_files: list[Path] = []

    manifest_path = task_dir / "task-manifest.md"
    status_path = task_dir / "status.md"
    orchestration_path = task_dir / "orchestration_plan.md"

    for path, reason in (
        (manifest_path, "task restart anchor and current state"),
        (status_path, "current lifecycle state"),
    ):
        if path.is_file():
            add_item(sections, seen, "Required", path, task_dir, reason)
            known_texts.append(read_text(path))
            known_files.append(path)
        else:
            blockers.append(f"{path.name} is missing.")

    if orchestration_path.is_file():
        add_item(
            sections,
            seen,
            "Required",
            orchestration_path,
            task_dir,
            "selected pipeline, process depth, and routing context",
        )
        known_texts.append(read_text(orchestration_path))
        known_files.append(orchestration_path)
    else:
        warnings.append("orchestration_plan.md is missing.")

    manifest_text = known_texts[0] if manifest_path.is_file() else ""
    orchestration_text = read_text(orchestration_path) if orchestration_path.is_file() else ""

    selected_pipeline = extract_labeled_value(manifest_text, SELECTED_PIPELINE_RE)
    if selected_pipeline is None:
        selected_pipeline = extract_labeled_value(orchestration_text, SELECTED_PIPELINE_RE)

    if selected_pipeline is None:
        warnings.append("Selected pipeline was not found in task-manifest.md or orchestration_plan.md.")
    else:
        pipeline_path = PIPELINES_DIR / f"{normalize_pipeline(selected_pipeline)}_pipeline.md"
        if pipeline_path.is_file():
            add_item(
                sections,
                seen,
                "Conditional",
                pipeline_path,
                task_dir,
                f"selected pipeline contract for `{selected_pipeline}`",
            )
        else:
            warnings.append(
                f"Selected pipeline `{selected_pipeline}` does not map to an existing pipeline file."
            )

    for file_name in ROLE_FILES[role]:
        path = task_dir / file_name
        if path.is_file():
            reason = f"{role} role input"
            if role == "review_agent" and file_name in EVIDENCE_FILES:
                reason = "evidence file for review_agent claim checks"
            add_item(sections, seen, "Role-specific", path, task_dir, reason)
            known_texts.append(read_text(path))
            known_files.append(path)
        else:
            not_included.append(f"`{file_name}` — not present for `{role}` role.")

    current_artifact = extract_labeled_value(manifest_text, CURRENT_ARTIFACT_RE)
    if current_artifact is None:
        warnings.append("Current artifact pointer was not found in task-manifest.md.")
    else:
        artifact_path = resolve_task_path(task_dir, current_artifact)
        if artifact_path.is_file():
            add_item(
                sections,
                seen,
                "Conditional",
                artifact_path,
                task_dir,
                "current artifact pointer from task-manifest.md",
            )
            if artifact_path not in known_files:
                known_texts.append(read_text(artifact_path))
                known_files.append(artifact_path)
        else:
            warnings.append(f"Current artifact `{current_artifact}` was not found.")

    handoff_path = collect_handoff(task_dir)
    if handoff_path is None:
        warnings.append("No handoff file found in task folder root.")
        not_included.append("`handoff*.md` — no handoff candidate found in task folder root.")
    else:
        add_item(
            sections,
            seen,
            "Conditional",
            handoff_path,
            task_dir,
            "latest handoff candidate by explicit filename order",
        )
        known_texts.append(read_text(handoff_path))
        known_files.append(handoff_path)

    client_profile = extract_labeled_value(manifest_text, CLIENT_PROFILE_RE)
    client_profile_status = extract_labeled_value(manifest_text, CLIENT_PROFILE_STATUS_RE)
    if client_profile is None or normalize_value(client_profile) == "none":
        not_included.append("Client-profile files — client_profile is none or not specified.")
    else:
        listed_files = extract_client_profile_files(manifest_text)
        if not listed_files:
            warnings.append(
                f"client_profile `{client_profile}` is set but no client_profile_files are listed."
            )
        if normalize_value(client_profile_status or "") == "active":
            for file_name in listed_files:
                path = resolve_repo_path(file_name)
                if path.is_file():
                    add_item(
                        sections,
                        seen,
                        "Conditional",
                        path,
                        task_dir,
                        f"explicit active client-profile file for `{client_profile}`",
                    )
                else:
                    warnings.append(f"Listed client-profile file `{file_name}` was not found.")
        else:
            warnings.append(
                f"client_profile_status is `{client_profile_status or 'missing'}`; "
                "client-profile files were not included."
            )
            if listed_files:
                not_included.append(
                    "Client-profile files — client_profile_status is not active."
                )

    if role in {"writer", "review_agent"}:
        for path in collect_task_local_source_evidence(task_dir, known_texts, known_files):
            add_item(
                sections,
                seen,
                "Conditional",
                path,
                task_dir,
                "task-local evidence summary for source-based compact-evidence; not original source",
            )
            known_texts.append(read_text(path))
            known_files.append(path)

    add_item(
        sections,
        seen,
        "Conditional",
        KB_DIR / "00_index.md",
        task_dir,
        "KB navigation and ownership index",
    )

    combined_context = "\n".join(known_texts + [manifest_text, orchestration_text])
    if re.search(r"(?i)\bcompact\b", combined_context):
        add_item(
            sections,
            seen,
            "Conditional",
            KB_DIR / "compact_execution.md",
            task_dir,
            "compact execution mentioned in task context",
        )

    if role == "chief_editor" or (task_dir / "feedback.md").is_file():
        add_item(
            sections,
            seen,
            "Conditional",
            KB_DIR / "feedback_loop.md",
            task_dir,
            "feedback handling context for Chief Editor or feedback artifact",
        )

    if task_mentions_source(task_dir, known_texts, known_files):
        source_path = KB_DIR / "source_provenance.md"
        if source_path.is_file():
            add_item(
                sections,
                seen,
                "Conditional",
                source_path,
                task_dir,
                "source/provenance terms found in task context",
            )

    if role in {"chief_editor", "review_agent", "final_editor"}:
        add_item(
            sections,
            seen,
            "Conditional",
            KB_DIR / "task_statuses.md",
            task_dir,
            f"status model context for `{role}`",
        )

    if role == "final_editor" and not (task_dir / "review.md").is_file():
        blockers.append("review.md is missing for final_editor.")

    not_included.append("Latest modified files — never used as source of truth.")
    not_included.append("Whole project scan — not performed by this helper.")
    return sections, blockers, warnings, not_included


def print_list(items: list[str]) -> None:
    if items:
        for item in items:
            print(f"- {item}")
    else:
        print("- none")


def print_items(items: list[ReadItem]) -> None:
    if items:
        for item in items:
            print(f"- `{item.display_path}` — {item.reason}.")
    else:
        print("- none")


def print_pack(
    task_dir: Path,
    role: str,
    sections: dict[str, list[ReadItem]],
    blockers: list[str],
    warnings: list[str],
    not_included: list[str],
) -> None:
    result = "FAIL" if blockers else "PASS"
    print("# Task Pack")
    print()
    print(f"Task folder: {task_dir}")
    print(f"Role: {role}")
    print(f"Result: {result}")
    print()
    print("## Blockers")
    print_list(blockers)
    print()
    print("## Warnings")
    print_list(warnings)
    print()
    print("## Read set")
    print()
    for section_name in ("Required", "Role-specific", "Conditional"):
        print(f"### {section_name}")
        print_items(sections[section_name])
        print()
    print("## Not included")
    print_list(not_included)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(usage(), file=sys.stderr)
        return 2

    task_dir = Path(argv[1]).resolve()
    role = argv[2]

    if role not in SUPPORTED_ROLES:
        print(f"Error: unsupported role: {role}", file=sys.stderr)
        print(usage(), file=sys.stderr)
        return 2
    if not task_dir.exists():
        print(f"Error: path does not exist: {task_dir}", file=sys.stderr)
        print(usage(), file=sys.stderr)
        return 2
    if not task_dir.is_dir():
        print(f"Error: path is not a directory: {task_dir}", file=sys.stderr)
        print(usage(), file=sys.stderr)
        return 2

    sections, blockers, warnings, not_included = generate_pack(task_dir, role)
    print_pack(task_dir, role, sections, blockers, warnings, not_included)
    return 1 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
