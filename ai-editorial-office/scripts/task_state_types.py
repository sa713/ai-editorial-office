"""Shared value types for the disposable Task State projection."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class SourceLocation:
    file: str
    line: int | None = None


@dataclass
class Diagnostic:
    level: str
    code: str
    message: str
    source: SourceLocation | None = None
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        if self.source is None:
            result["source"] = None
        return result


@dataclass(frozen=True)
class LocatedValue:
    value: str
    source: SourceLocation


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
