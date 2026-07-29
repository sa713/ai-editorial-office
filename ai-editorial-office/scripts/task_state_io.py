"""Read-only Markdown extraction and task-local filesystem safety helpers."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Iterable

from task_state_types import Diagnostic, LocatedValue, SourceLocation


PROJECTION_VERSION = 1
EDITORIAL_ROOT = Path(__file__).resolve().parents[1]
TASKS_ROOT = EDITORIAL_ROOT / "tasks"
STATUSES_PATH = EDITORIAL_ROOT / "kb" / "task_statuses.md"
CAPABILITIES_PATH = EDITORIAL_ROOT / "kb" / "capability_registry.md"
PIPELINES_DIR = EDITORIAL_ROOT / "pipelines"
AGENTS_DIR = EDITORIAL_ROOT / "agents"

CANONICAL_INPUTS = (
    "brief.md",
    "task-manifest.md",
    "status.md",
    "orchestration_plan.md",
    "review.md",
    "approval.md",
    "final.md",
)
REQUIRED_INPUTS = ("task-manifest.md", "status.md")
TERMINAL_STATUSES = {"finalized", "archived"}
HISTORICAL_STATUSES = TERMINAL_STATUSES | {"failed"}
PAUSED_STATUSES = {"blocked", "human_approval_required"}
REVIEW_OUTCOMES = {"approved", "changes_requested", "blocked"}

CODE_SPAN_RE = re.compile(r"`([a-z][a-z0-9_-]*)`", re.IGNORECASE)
FIELD_PREFIX = r"(?im)^\s*(?:[-*]\s*)?"
TASK_ID_RE = re.compile(FIELD_PREFIX + r"task[\s_-]*id\s*:\s*(.+?)\s*$")
TASK_TYPE_RE = re.compile(FIELD_PREFIX + r"task[\s_-]*type\s*:\s*(.+?)\s*$")
CURRENT_STATUS_RE = re.compile(
    FIELD_PREFIX + r"(?:current[\s_-]*status|status)\s*:\s*(.+?)\s*$"
)
PREVIOUS_STATUS_RE = re.compile(
    FIELD_PREFIX
    + r"(?:previous[\s_-]*status|previous|from[\s_-]*status)\s*:\s*(.+?)\s*$"
)
SELECTED_PIPELINE_RE = re.compile(
    FIELD_PREFIX + r"(?:selected[\s_-]*pipeline|pipeline)\s*:\s*(.+?)\s*$"
)
OWNER_RE = re.compile(
    FIELD_PREFIX
    + r"(?:owner(?:/current[\s_-]*role|[\s_-]*role)?|responsible[\s_-]*role)"
    + r"\s*:\s*(.+?)\s*$"
)
NEXT_ACTION_RE = re.compile(
    FIELD_PREFIX + r"(?:next[\s_-]*(?:required[\s_-]*)?action)\s*:\s*(.+?)\s*$"
)
CURRENT_ARTIFACT_RE = re.compile(
    FIELD_PREFIX
    + r"(?:current(?:[\s_-]*(?:working|active))?[\s_-]*"
    + r"(?:artifact|version)|current[\s_-]*(?:artifact|version))"
    + r"\s*:\s*(.+?)\s*$"
)
CREATED_RE = re.compile(FIELD_PREFIX + r"created\s*:\s*(.+?)\s*$")
UPDATED_RE = re.compile(
    FIELD_PREFIX + r"(?:last[\s_-]*updated|updated)\s*:\s*(.+?)\s*$"
)
SINCE_RE = re.compile(FIELD_PREFIX + r"since\s*:\s*(.+?)\s*$")
REVIEW_OUTCOME_RE = re.compile(
    FIELD_PREFIX
    + r"(?:review[_ -]outcome|outcome|verdict|status)\s*:\s*"
    + r"(approved|changes_requested|blocked)\b"
)
SINGLE_REVIEW_OUTCOME_RE = re.compile(
    r"(?im)^\s*(approved|changes_requested|blocked)\s*$"
)
REVIEWER_ROLE_RE = re.compile(
    FIELD_PREFIX + r"reviewer[\s_-]*role\s*:\s*(.+?)\s*$"
)
PRODUCER_ROLE_RE = re.compile(
    FIELD_PREFIX + r"(?:writer|producer)[\s_-]*role\s*:\s*(.+?)\s*$"
)
REVIEWER_ID_RE = re.compile(FIELD_PREFIX + r"reviewer\s*:\s*(.+?)\s*$")
PRODUCER_ID_RE = re.compile(FIELD_PREFIX + r"producer\s*:\s*(.+?)\s*$")
INDEPENDENCE_RE = re.compile(
    FIELD_PREFIX + r"independence[\s_-]*confirmed\s*:\s*(.+?)\s*$"
)
HUMAN_APPROVAL_REQUIRED_RE = re.compile(
    FIELD_PREFIX + r"human[\s_-]*approval[\s_-]*required\s*:\s*(.+?)\s*$"
)
HUMAN_APPROVAL_STATE_RE = re.compile(
    FIELD_PREFIX
    + r"(?:human[\s_-]*approval[\s_-]*(?:state|status)|approval[\s_-]*status)"
    + r"\s*:\s*(.+?)\s*$"
)
APPROVAL_EVIDENCE_RE = re.compile(
    FIELD_PREFIX + r"(?:human[\s_-]*)?approval[\s_-]*evidence\s*:\s*(.+?)\s*$"
)
REVIEWED_ARTIFACT_RE = re.compile(
    FIELD_PREFIX + r"reviewed[\s_-]*artifact(?:/version)?\s*:\s*(.+?)\s*$"
)
REVIEWED_SHA_RE = re.compile(
    FIELD_PREFIX + r"reviewed[\s_-]*(?:sha-?256|hash)\s*:\s*(.+?)\s*$"
)
LIFECYCLE_CONTRACT_RE = re.compile(
    FIELD_PREFIX + r"lifecycle[\s_-]*contract[\s_-]*version\s*:\s*(.+?)\s*$"
)



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


def known_pipeline_ids() -> set[str]:
    return {
        path.stem[: -len("_pipeline")]
        for path in PIPELINES_DIR.glob("*_pipeline.md")
        if path.is_file() and path.stem.endswith("_pipeline")
    }


def resolve_pipeline_id(value: str) -> str | None:
    """Resolve one existing pipeline from a legacy descriptive field."""
    candidates = known_pipeline_ids()
    normalized = normalize_value(clean_field_value(value))
    exact = normalize_pipeline(value)
    if exact in candidates:
        return exact
    matches = {
        pipeline
        for pipeline in candidates
        if re.search(
            rf"(?<![a-z0-9]){re.escape(pipeline)}(?:_pipeline)?(?![a-z0-9])",
            normalized,
        )
    }
    return next(iter(matches)) if len(matches) == 1 else None


def sha256_bytes(data: bytes) -> str:
    return f"sha256:{hashlib.sha256(data).hexdigest()}"


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def extract_located(
    text: str, pattern: re.Pattern[str], source_name: str
) -> LocatedValue | None:
    match = pattern.search(text)
    if not match:
        return None
    value = clean_field_value(match.group(1))
    if not value:
        return None
    return LocatedValue(value, SourceLocation(source_name, line_number(text, match.start())))


def extract_all_located(
    text: str, pattern: re.Pattern[str], source_name: str
) -> list[LocatedValue]:
    values: list[LocatedValue] = []
    for match in pattern.finditer(text):
        value = clean_field_value(match.group(1))
        if value:
            values.append(
                LocatedValue(
                    value, SourceLocation(source_name, line_number(text, match.start()))
                )
            )
    return values


def parse_markdown_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    return cells if len(cells) >= 2 else None


def load_known_statuses(path: Path = STATUSES_PATH) -> set[str] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    section = text
    match = re.search(r"(?ims)^## allowed statuses\s*(.*?)(?:^##\s+|\Z)", text)
    if match:
        section = match.group(1)
    values = {normalize_value(m.group(1)) for m in CODE_SPAN_RE.finditer(section)}
    return values or None


def load_allowed_transitions(
    path: Path = STATUSES_PATH,
) -> dict[str, set[str]] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    match = re.search(r"(?ims)^## status transitions\s*(.*?)(?:^##\s+|\Z)", text)
    if not match:
        return None
    transitions: dict[str, set[str]] = {}
    for line in match.group(1).splitlines():
        cells = parse_markdown_table_row(line)
        if cells is None:
            continue
        left, right = cells[0], cells[1]
        if left.lower() == "from" or re.fullmatch(r":?-+:?", left):
            continue
        source = CODE_SPAN_RE.search(left)
        if not source:
            continue
        transitions[normalize_value(source.group(1))] = {
            normalize_value(item.group(1)) for item in CODE_SPAN_RE.finditer(right)
        }
    return transitions or None


def load_capability_ids(path: Path = CAPABILITIES_PATH) -> set[str] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    records = text
    match = re.search(r"(?ims)^## Capability Records\s*(.*?)(?:^##\s+|\Z)", text)
    if match:
        records = match.group(1)
    headings = re.findall(r"(?m)^###\s+(.+?)\s*$", records)
    values = {normalize_value(heading) for heading in headings}
    return values or None


def load_role_ids(path: Path = AGENTS_DIR) -> set[str]:
    return {item.stem for item in path.glob("*.md") if item.is_file()}


def extract_review_outcomes(text: str) -> list[LocatedValue]:
    values = extract_all_located(text, REVIEW_OUTCOME_RE, "review.md")
    if values:
        return values
    return extract_all_located(text, SINGLE_REVIEW_OUTCOME_RE, "review.md")


def extract_section_bullets(text: str, heading: str) -> list[str]:
    match = re.search(
        rf"(?ims)^##\s+{re.escape(heading)}\s*(.*?)(?:^##\s+|\Z)", text
    )
    if not match:
        return []
    values: list[str] = []
    for line in match.group(1).splitlines():
        item = re.match(r"^\s*[-*]\s+(.+?)\s*$", line)
        if not item:
            continue
        value = clean_field_value(item.group(1)).rstrip(".")
        normalized = normalize_value(value)
        if (
            normalized in {"none", "not_applicable", "no_active_blockers"}
            or re.match(r"(?i)^none(?:[.:\s]|$)", value)
            or normalized.startswith("repository_note")
        ):
            continue
        values.append(value)
    return values


def extract_capabilities(texts: Iterable[str]) -> list[str]:
    selected: list[str] = []
    seen: set[str] = set()
    for text in texts:
        for heading in ("active capabilities", "capabilities"):
            for raw in extract_section_bullets(text, heading):
                value = normalize_value(raw)
                if value and value not in seen:
                    selected.append(value)
                    seen.add(value)
    return selected



def safe_relative_file(
    task_dir: Path,
    raw_value: str,
    diagnostics: list[Diagnostic],
    code: str,
    *,
    unsafe_level: str = "error",
) -> Path | None:
    cleaned = clean_field_value(raw_value).split(",", 1)[0].strip()
    cleaned = cleaned.strip("[]()")
    if cleaned.startswith("./"):
        cleaned = cleaned[2:]
    candidate_raw = Path(cleaned)
    if candidate_raw.is_absolute() or ".." in candidate_raw.parts:
        diagnostics.append(
            Diagnostic(
                unsafe_level,
                code,
                f"Task-local artifact path `{raw_value}` escapes the task folder.",
                details={"value": raw_value},
            )
        )
        return None
    candidate = task_dir / candidate_raw
    try:
        resolved = candidate.resolve(strict=True)
    except OSError:
        diagnostics.append(
            Diagnostic(
                "warning",
                f"{code}_missing",
                f"Referenced task artifact `{raw_value}` was not found inside the task folder.",
                details={"value": raw_value},
            )
        )
        return None
    try:
        resolved.relative_to(task_dir)
    except ValueError:
        diagnostics.append(
            Diagnostic(
                unsafe_level,
                code,
                f"Referenced artifact `{raw_value}` resolves outside the task folder.",
                details={"value": raw_value},
            )
        )
        return None
    if not resolved.is_file():
        return None
    return resolved


def resolve_task_directory(task_dir: Path, allowed_root: Path) -> Path:
    if ".." in task_dir.parts:
        raise ValueError("Path traversal is not allowed in a task directory path.")
    root = allowed_root.resolve(strict=True)
    resolved = task_dir.resolve(strict=True)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(
            f"Task directory must be inside the allowed tasks root: {root}"
        ) from exc
    if not resolved.is_dir():
        raise ValueError(f"Task path is not a directory: {task_dir}")
    return resolved


def read_initial_inputs(
    task_dir: Path, diagnostics: list[Diagnostic]
) -> tuple[dict[str, str], dict[str, bytes], dict[str, bool]]:
    texts: dict[str, str] = {}
    raw: dict[str, bytes] = {}
    presence: dict[str, bool] = {}
    for name in CANONICAL_INPUTS:
        path = task_dir / name
        presence[name] = path.exists() or path.is_symlink()
        if not presence[name]:
            continue
        if path.is_symlink():
            try:
                target = path.resolve(strict=True)
                target.relative_to(task_dir)
            except (OSError, ValueError):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "external_symlink",
                        f"{name} is an external or broken symlink and was not read.",
                        SourceLocation(name),
                    )
                )
                continue
        if not path.is_file():
            diagnostics.append(
                Diagnostic(
                    "error",
                    "canonical_input_not_file",
                    f"{name} exists but is not a regular file.",
                    SourceLocation(name),
                )
            )
            continue
        try:
            data = path.read_bytes()
            text = data.decode("utf-8")
        except (OSError, UnicodeError) as exc:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "canonical_input_unreadable",
                    f"{name} could not be read as UTF-8.",
                    SourceLocation(name),
                    {"exception": type(exc).__name__},
                )
            )
            continue
        raw[name] = data
        texts[name] = text
    return texts, raw, presence


def revalidate_inputs(
    task_dir: Path,
    fingerprints: dict[str, str],
    initial_presence: dict[str, bool],
    diagnostics: list[Diagnostic],
) -> None:
    """Re-read every fingerprinted input without trusting its original path."""
    for name, before in sorted(fingerprints.items()):
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "source_changed_during_parse",
                    f"Fingerprint source `{name}` is no longer a safe task-local path.",
                    SourceLocation(name),
                )
            )
            continue

        path = task_dir / relative
        if name in initial_presence:
            present_now = path.exists() or path.is_symlink()
            if present_now != initial_presence[name]:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "source_changed_during_parse",
                        f"{name} existence changed during parsing.",
                        SourceLocation(name),
                    )
                )
                continue

        try:
            resolved = path.resolve(strict=True)
            resolved.relative_to(task_dir)
        except (OSError, ValueError):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "source_changed_during_parse",
                    f"{name} became missing, broken or external during parsing.",
                    SourceLocation(name),
                )
            )
            continue
        if not resolved.is_file():
            diagnostics.append(
                Diagnostic(
                    "error",
                    "source_changed_during_parse",
                    f"{name} is no longer a regular task-local file.",
                    SourceLocation(name),
                )
            )
            continue
        try:
            current_data = resolved.read_bytes()
        except OSError as exc:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "source_changed_during_parse",
                    f"{name} could not be re-read during parsing.",
                    SourceLocation(name),
                    {"exception": type(exc).__name__},
                )
            )
            continue
        after = sha256_bytes(current_data)
        if after != before:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "source_changed_during_parse",
                    f"{name} changed during parsing; projection is stale.",
                    SourceLocation(name),
                    {"before": before, "after": after},
                )
            )
