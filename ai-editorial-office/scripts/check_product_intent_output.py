#!/usr/bin/env python3
"""Validate test-only Product Intent Review reader-output records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


MODES = {"not_needed", "limited", "full"}
OUTCOMES = {"approved", "changes_requested", "blocked"}
FORMS = {"report", "decision-memo", "research-report", "embedded"}
REQUIRED_SECTIONS = {
    "verdict",
    "main_gap",
    "next_decision",
    "evidence_boundary",
    "production_consequence",
}
FORM_BY_READER_JOB = {
    "quick_state": {"report", "embedded"},
    "management_decision": {"decision-memo"},
    "evidence_trace": {"research-report"},
    "embedded_review": {"embedded"},
}


def _present(value: Any) -> bool:
    return value not in (None, "", [], {})


def evaluate(case: dict[str, Any]) -> tuple[str, list[str]]:
    mode = case.get("mode")
    if mode not in MODES:
        return "blocked", ["unsupported mode"]

    sections = case.get("sections", [])
    if mode == "not_needed":
        issues = []
        if sections:
            issues.append("not_needed must not add Product Intent Review sections")
        if case.get("standalone_product_intent_report", False):
            issues.append("not_needed must not create a standalone report")
        return ("changes_requested" if issues else "approved"), issues

    issues: list[str] = []
    form = case.get("selected_form")
    reader_job = case.get("reader_job")
    if form not in FORMS:
        issues.append("selected output form must reuse an existing form")
    if reader_job not in FORM_BY_READER_JOB:
        issues.append("reader job is missing or unsupported")
    elif form not in FORM_BY_READER_JOB[reader_job]:
        issues.append("selected output form does not fit the reader job")

    if case.get("new_deliverable_profile", False):
        issues.append("new deliverable profile is not justified")
    if case.get("standalone_product_intent_report", False) and not case.get(
        "standalone_explicitly_selected", False
    ):
        issues.append("standalone Product Intent Review report was created by default")

    missing = sorted(REQUIRED_SECTIONS.difference(sections))
    if missing:
        issues.append("reader result misses: " + ", ".join(missing))
    else:
        positions = {name: sections.index(name) for name in REQUIRED_SECTIONS}
        if sections[0] != "verdict":
            issues.append("verdict is not first")
        if not (
            positions["verdict"]
            < positions["main_gap"]
            < positions["next_decision"]
            < positions["evidence_boundary"]
            < positions["production_consequence"]
        ):
            issues.append("product decision sections are not in required order")
        if "editorial_notes" in sections and positions["production_consequence"] > sections.index(
            "editorial_notes"
        ):
            issues.append("editorial remarks appear before the product decision")

    for field in ("verdict_text", "main_gap_text", "next_decision_text", "production_consequence_text"):
        if not _present(case.get(field)):
            issues.append(f"{field} is missing")

    evidence = case.get("evidence", {})
    if not _present(evidence.get("confirmed")):
        issues.append("confirmed evidence is not visible")
    if "assumptions" not in evidence or "unknowns" not in evidence:
        issues.append("assumptions and unknowns are not distinguishable")
    if evidence.get("boundary_statement_count", 0) < 1:
        issues.append("evidence boundary is missing")
    if evidence.get("boundary_statement_count", 0) > 2:
        issues.append("uncertainty is repeated as disclaimer overload")

    if mode == "limited":
        if case.get("output_depth") != "compact":
            issues.append("limited output is not compact")
        if case.get("prints_full_model", False) or case.get("prints_all_checks", False):
            issues.append("limited output exposes full internal analysis")
        if case.get("alternative_count", 0) > 1:
            issues.append("limited output contains unnecessary alternatives")
    else:
        if case.get("output_depth") not in {"decision-ready", "evidence-heavy"}:
            issues.append("full output is not decision-ready")
        if case.get("mechanical_method_dump", False):
            issues.append("full output is a mechanical method dump")
        if case.get("alternative_count", 0) > 3:
            issues.append("full output contains an unbounded brainstorm")

    if case.get("negative_finding", False) and not case.get("negative_language_direct", False):
        issues.append("negative or no-build finding was softened")

    if case.get("consequence") == "Validate before production":
        validation = case.get("validation", {})
        for field in (
            "can_do_now",
            "premature_now",
            "minimum_artifact",
            "what_to_test",
            "how_to_test",
            "what_to_observe",
            "how_to_decide",
            "inference_limit",
        ):
            if not _present(validation.get(field)):
                issues.append(f"validate-first output misses {field}")

    if reader_job == "management_decision" and not case.get("tradeoffs_visible", False):
        issues.append("decision memo does not show tradeoffs")
    if reader_job == "evidence_trace" and case.get("certainty_exceeds_evidence", False):
        issues.append("research report conclusion exceeds evidence")

    if case.get("source_size") == "large" and case.get("mechanical_source_expansion", False):
        issues.append("large source mechanically expanded the output")
    if case.get("internal_architecture_terms", []):
        issues.append("internal architecture leaked into user-facing output")

    outcome = "changes_requested" if issues else "approved"
    return outcome, issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixtures", type=Path)
    args = parser.parse_args()

    cases = json.loads(args.fixtures.read_text(encoding="utf-8"))
    if not isinstance(cases, list):
        print("error: fixture file must contain a list")
        return 2

    failed = False
    for case in cases:
        name = case.get("name", "unnamed")
        expected = case.get("expected_outcome")
        actual, findings = evaluate(case)
        if expected not in OUTCOMES or actual != expected:
            failed = True
            print(f"FAIL {name}: expected {expected}, got {actual}")
            for finding in findings:
                print(f"- {finding}")
        else:
            print(f"PASS {name} -> {actual}")

    if failed:
        return 2
    print(f"All {len(cases)} Product Intent Review output scenarios passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
