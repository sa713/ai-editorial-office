#!/usr/bin/env python3
"""Validate and summarize the Product Intent Review Step 6 evaluation suite.

The runner checks case structure, coverage, deterministic contract properties,
and the presence of independent manual judgment. It does not generate product
answers or infer product quality from keyword matching.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


MODES = {"not_needed", "limited", "full"}
TASK_CLASSES = {
    "learning_activity",
    "internal_service",
    "communication_campaign",
    "event",
    "work_process",
    "ux_mechanic",
    "ai_tool",
    "simple_editing",
}
SOURCE_KINDS = {
    "anonymized_real",
    "synthetic_boundary",
    "adversarial",
    "simple_negative",
}
FINDING_CLASSES = {
    "proceed",
    "proceed_with_constraints",
    "validate_before_production",
    "reroute",
    "no_build",
    "not_applicable",
}
CONSEQUENCES = {
    "Proceed",
    "Proceed with constraints",
    "Validate before production",
    "Reroute",
    "Stop / no-build recommendation",
}
VALIDATION_DISPOSITIONS = {
    "minimum_test",
    "not_needed",
    "insufficient",
    "not_applicable",
}
MANUAL_STATUSES = {"pass", "fail", "needs_clarification"}
CONFIDENCE = {"low", "medium", "high"}
RUBRIC_DIMENSIONS = {
    "activation_accuracy",
    "problem_fidelity",
    "model_quality",
    "main_gap_quality",
    "product_judgment_quality",
    "production_consequence_quality",
    "validation_quality",
    "communication_quality",
    "authority_discipline",
    "overall_decision_usefulness",
}
CRITICAL_FAILURES = {
    "invented_need",
    "invented_audience",
    "product_owner_substitution",
    "hidden_critical_gap",
    "keyword_only_activation",
    "evidence_free_no_build",
    "full_product_validation",
    "finding_outcome_conflation",
    "compact_path_regression",
    "validation_method_mismatch",
    "second_review_gate",
    "hidden_lifecycle_stage",
}
REQUIRED_CASE_FIELDS = {
    "case_id",
    "title",
    "task_class",
    "source_kind",
    "input",
    "hidden_structure",
    "expected",
    "coverage_tags",
    "pair_ids",
    "observed",
    "manual_evaluation",
}
REQUIRED_HIDDEN_FIELDS = {
    "real_problem",
    "confirmed_evidence",
    "assumptions",
    "unknowns",
    "main_gap",
    "allowed_alternatives",
    "forbidden_conclusions",
}
REQUIRED_EXPECTED_FIELDS = {
    "mode",
    "focus",
    "required_properties",
    "forbidden_errors",
    "acceptable_variability",
    "acceptable_findings",
    "rubric_focus",
}
REQUIRED_OBSERVED_FIELDS = {
    "mode",
    "focus",
    "evidence_boundary",
    "main_gap",
    "finding",
    "finding_class",
    "production_consequence",
    "validation_disposition",
    "validation_method",
    "next_decision",
    "reader_order",
    "properties",
    "errors",
    "governance",
}
REQUIRED_GOVERNANCE_FIELDS = {
    "single_review_gate",
    "owner_decision_preserved",
    "role_boundaries_preserved",
    "finding_outcome_separated",
    "approved_finding_preserved",
    "compact_path_preserved",
}
FINDING_CONSEQUENCE = {
    "proceed": {"Proceed"},
    "proceed_with_constraints": {"Proceed with constraints"},
    "validate_before_production": {"Validate before production"},
    "reroute": {"Reroute"},
    "no_build": {"Stop / no-build recommendation", "Reroute"},
    "not_applicable": {"Proceed"},
}
COVERAGE_MINIMUMS = {
    "cases": 30,
    "task_classes": 8,
    "pairs": 8,
    "adversarial": 10,
    "not_needed": 5,
    "limited": 5,
    "full": 10,
    "no_build_or_reroute": 5,
    "proceed": 5,
    "validation_methods": 5,
    "validation_not_needed": 2,
    "validation_insufficient": 2,
    "anonymized_real": 5,
}


def _present(value: Any) -> bool:
    return value not in (None, "", [], {})


def _score_profile(
    profile_name: str,
    profiles: dict[str, dict[str, Any]],
) -> tuple[dict[str, Any], str | None]:
    profile = profiles.get(profile_name)
    if not isinstance(profile, dict):
        return {}, f"unknown manual score profile: {profile_name}"
    if set(profile) != RUBRIC_DIMENSIONS:
        return profile, f"score profile {profile_name} has wrong rubric dimensions"
    for dimension, value in profile.items():
        if value != "not_applicable" and value not in {0, 1, 2, 3}:
            return profile, f"score profile {profile_name} has invalid {dimension} score"
    return profile, None


def _validate_case(
    case: dict[str, Any],
    profiles: dict[str, dict[str, Any]],
) -> list[str]:
    case_id = case.get("case_id", "unknown")
    issues: list[str] = []
    missing = sorted(REQUIRED_CASE_FIELDS.difference(case))
    if missing:
        return [f"{case_id}: missing case fields: {', '.join(missing)}"]

    if case["task_class"] not in TASK_CLASSES:
        issues.append(f"{case_id}: unsupported task class")
    if case["source_kind"] not in SOURCE_KINDS:
        issues.append(f"{case_id}: unsupported source kind")
    if not _present(case["input"]):
        issues.append(f"{case_id}: input is empty")

    hidden = case["hidden_structure"]
    if not isinstance(hidden, dict):
        issues.append(f"{case_id}: hidden_structure must be an object")
    else:
        hidden_missing = sorted(REQUIRED_HIDDEN_FIELDS.difference(hidden))
        if hidden_missing:
            issues.append(
                f"{case_id}: missing hidden fields: {', '.join(hidden_missing)}"
            )

    expected = case["expected"]
    observed = case["observed"]
    if not isinstance(expected, dict) or not isinstance(observed, dict):
        issues.append(f"{case_id}: expected and observed must be objects")
        return issues

    expected_missing = sorted(REQUIRED_EXPECTED_FIELDS.difference(expected))
    observed_missing = sorted(REQUIRED_OBSERVED_FIELDS.difference(observed))
    if expected_missing:
        issues.append(
            f"{case_id}: missing expected fields: {', '.join(expected_missing)}"
        )
    if observed_missing:
        issues.append(
            f"{case_id}: missing observed fields: {', '.join(observed_missing)}"
        )
    if expected_missing or observed_missing:
        return issues

    expected_mode = expected["mode"]
    observed_mode = observed["mode"]
    if expected_mode not in MODES or observed_mode not in MODES:
        issues.append(f"{case_id}: unsupported mode")
    if expected_mode != observed_mode:
        issues.append(
            f"{case_id}: mode mismatch expected {expected_mode}, got {observed_mode}"
        )
    if expected_mode == "limited" and expected["focus"] != observed["focus"]:
        issues.append(f"{case_id}: limited focus mismatch")
    if expected_mode == "not_needed" and not observed["governance"].get(
        "compact_path_preserved", False
    ):
        issues.append(f"{case_id}: compact path regression")

    required = set(expected["required_properties"])
    properties = set(observed["properties"])
    missing_properties = sorted(required.difference(properties))
    if missing_properties:
        issues.append(
            f"{case_id}: missing required properties: {', '.join(missing_properties)}"
        )

    forbidden = set(expected["forbidden_errors"])
    observed_errors = set(observed["errors"])
    forbidden_present = sorted(forbidden.intersection(observed_errors))
    if forbidden_present:
        issues.append(
            f"{case_id}: forbidden errors present: {', '.join(forbidden_present)}"
        )
    critical_present = sorted(CRITICAL_FAILURES.intersection(observed_errors))
    if critical_present:
        issues.append(
            f"{case_id}: critical contract violations: {', '.join(critical_present)}"
        )
    if observed["finding_class"] not in FINDING_CLASSES:
        issues.append(f"{case_id}: unsupported finding class")
    elif observed["finding_class"] not in set(expected["acceptable_findings"]):
        issues.append(f"{case_id}: finding is outside acceptable range")
    if observed["production_consequence"] not in CONSEQUENCES:
        issues.append(f"{case_id}: unsupported production consequence")
    elif (
        observed["finding_class"] in FINDING_CONSEQUENCE
        and observed["production_consequence"]
        not in FINDING_CONSEQUENCE[observed["finding_class"]]
    ):
        issues.append(f"{case_id}: consequence does not fit product finding")

    disposition = observed["validation_disposition"]
    method = observed["validation_method"]
    if disposition not in VALIDATION_DISPOSITIONS:
        issues.append(f"{case_id}: unsupported validation disposition")
    if disposition == "minimum_test" and not _present(method):
        issues.append(f"{case_id}: minimum validation method is missing")
    if disposition != "minimum_test" and _present(method):
        issues.append(f"{case_id}: validation method exists without minimum_test")

    if observed_mode != "not_needed":
        for field in ("evidence_boundary", "main_gap", "finding", "next_decision"):
            if not _present(observed[field]):
                issues.append(f"{case_id}: active result misses {field}")
        expected_order = ["verdict", "main_gap", "next_decision"]
        if observed["reader_order"][:3] != expected_order:
            issues.append(f"{case_id}: reader result is not verdict-first")
    elif observed["reader_order"] != ["requested_edit"]:
        issues.append(f"{case_id}: not_needed result adds product-review structure")

    governance = observed["governance"]
    if not isinstance(governance, dict):
        issues.append(f"{case_id}: governance must be an object")
    else:
        governance_missing = sorted(REQUIRED_GOVERNANCE_FIELDS.difference(governance))
        if governance_missing:
            issues.append(
                f"{case_id}: governance misses {', '.join(governance_missing)}"
            )
        for field in REQUIRED_GOVERNANCE_FIELDS:
            if field in governance and governance[field] is not True:
                issues.append(f"{case_id}: governance violation: {field}")

    manual = case["manual_evaluation"]
    if not isinstance(manual, dict):
        issues.append(f"{case_id}: manual_evaluation must be an object")
    else:
        for field in ("status", "score_profile", "main_defect", "confidence", "rationale"):
            if field not in manual:
                issues.append(f"{case_id}: manual evaluation misses {field}")
        if manual.get("status") not in MANUAL_STATUSES:
            issues.append(f"{case_id}: invalid manual evaluation status")
        if manual.get("confidence") not in CONFIDENCE:
            issues.append(f"{case_id}: invalid manual confidence")
        scores, profile_issue = _score_profile(
            manual.get("score_profile", ""), profiles
        )
        if profile_issue:
            issues.append(f"{case_id}: {profile_issue}")
        if manual.get("status") == "pass" and _present(manual.get("main_defect")):
            issues.append(f"{case_id}: passing manual judgment has a main defect")
        if manual.get("status") != "pass" and not _present(manual.get("main_defect")):
            issues.append(f"{case_id}: non-passing judgment lacks a main defect")
        if manual.get("status") != "pass":
            issues.append(
                f"{case_id}: independent manual judgment is {manual.get('status')}"
            )
        if manual.get("status") == "pass":
            weak_dimensions = sorted(
                dimension
                for dimension, value in scores.items()
                if value != "not_applicable" and value < 2
            )
            if weak_dimensions:
                issues.append(
                    f"{case_id}: passing judgment is below critical minimum in "
                    + ", ".join(weak_dimensions)
                )
        if not _present(manual.get("rationale")):
            issues.append(f"{case_id}: manual rationale is empty")

    if set(expected["rubric_focus"]).difference(RUBRIC_DIMENSIONS):
        issues.append(f"{case_id}: unknown case-specific rubric dimension")
    if not expected["acceptable_variability"]:
        issues.append(f"{case_id}: acceptable variability is empty")
    if not case["coverage_tags"]:
        issues.append(f"{case_id}: coverage tags are empty")
    return issues


def evaluate_suite(data: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    issues: list[str] = []
    cases = data.get("cases")
    profiles = data.get("score_profiles")
    if not isinstance(cases, list):
        return {}, ["suite: cases must be a list"]
    if not isinstance(profiles, dict):
        return {}, ["suite: score_profiles must be an object"]

    ids = [case.get("case_id") for case in cases if isinstance(case, dict)]
    duplicates = sorted(case_id for case_id, count in Counter(ids).items() if count > 1)
    if duplicates:
        issues.append("suite: duplicate Case IDs: " + ", ".join(duplicates))

    for case in cases:
        if not isinstance(case, dict):
            issues.append("suite: case entry is not an object")
            continue
        issues.extend(_validate_case(case, profiles))

    class_counts = Counter(case.get("task_class") for case in cases)
    source_counts = Counter(case.get("source_kind") for case in cases)
    mode_counts = Counter(case.get("observed", {}).get("mode") for case in cases)
    finding_counts = Counter(
        case.get("observed", {}).get("finding_class") for case in cases
    )
    disposition_counts = Counter(
        case.get("observed", {}).get("validation_disposition") for case in cases
    )
    validation_methods = {
        case.get("observed", {}).get("validation_method")
        for case in cases
        if _present(case.get("observed", {}).get("validation_method"))
    }
    pair_members: dict[str, list[str]] = defaultdict(list)
    for case in cases:
        for pair_id in case.get("pair_ids", []):
            pair_members[pair_id].append(case.get("case_id", "unknown"))
    malformed_pairs = {
        pair_id: members for pair_id, members in pair_members.items() if len(members) != 2
    }
    if malformed_pairs:
        details = "; ".join(
            f"{pair_id}={len(members)}" for pair_id, members in sorted(malformed_pairs.items())
        )
        issues.append("suite: every contrast pair must have two cases: " + details)

    adversarial_count = sum(
        "adversarial" in case.get("coverage_tags", []) for case in cases
    )
    baseline_count = sum(
        "baseline_comparison" in case.get("coverage_tags", []) for case in cases
    )
    manual_count = sum(
        isinstance(case.get("manual_evaluation"), dict) for case in cases
    )
    manual_failures = sum(
        case.get("manual_evaluation", {}).get("status") != "pass" for case in cases
    )

    routing_total = len(cases)
    mode_mismatches = sum(
        case.get("expected", {}).get("mode") != case.get("observed", {}).get("mode")
        for case in cases
    )
    routing_correct = routing_total - mode_mismatches
    over_activation = sum(
        case.get("expected", {}).get("mode") == "not_needed"
        and case.get("observed", {}).get("mode") != "not_needed"
        for case in cases
    )
    missed_activation = sum(
        case.get("expected", {}).get("mode") != "not_needed"
        and case.get("observed", {}).get("mode") == "not_needed"
        for case in cases
    )
    all_errors = [
        error
        for case in cases
        for error in case.get("observed", {}).get("errors", [])
    ]
    critical_violations = sum(error in CRITICAL_FAILURES for error in all_errors)
    main_gap_failures = sum(error == "main_gap_failure" for error in all_errors)
    unsupported_findings = sum(error == "unsupported_product_finding" for error in all_errors)
    validation_mismatches = sum(error == "validation_method_mismatch" for error in all_errors)
    authority_violations = sum(error == "product_owner_substitution" for error in all_errors)
    compact_regressions = sum(error == "compact_path_regression" for error in all_errors)
    production_defects = sum(
        "confirmed_production_defect" in case.get("coverage_tags", []) for case in cases
    )
    repair_loops = data.get("repair_loops", 0)

    coverage = {
        "cases": len(cases),
        "task_classes": len([name for name in class_counts if name in TASK_CLASSES]),
        "pairs": len(pair_members),
        "adversarial": adversarial_count,
        "not_needed": mode_counts["not_needed"],
        "limited": mode_counts["limited"],
        "full": mode_counts["full"],
        "no_build_or_reroute": finding_counts["no_build"] + finding_counts["reroute"],
        "proceed": finding_counts["proceed"] + finding_counts["proceed_with_constraints"],
        "validation_methods": len(validation_methods),
        "validation_not_needed": disposition_counts["not_needed"],
        "validation_insufficient": disposition_counts["insufficient"],
        "anonymized_real": source_counts["anonymized_real"],
    }
    for key, minimum in COVERAGE_MINIMUMS.items():
        if coverage[key] < minimum:
            issues.append(
                f"suite: coverage {key}={coverage[key]} is below required {minimum}"
            )
    if baseline_count < 5:
        issues.append("suite: fewer than five baseline-comparison cases")
    if manual_count != len(cases):
        issues.append("suite: every case requires a manual judgment record")

    metrics = {
        "routing_accuracy": (
            round(routing_correct / routing_total, 4) if routing_total else 0
        ),
        "routing_correct": routing_correct,
        "routing_total": routing_total,
        "over_activation_count": over_activation,
        "missed_activation_count": missed_activation,
        "mode_mismatch_count": mode_mismatches,
        "critical_contract_violations": critical_violations,
        "main_gap_failures": main_gap_failures,
        "unsupported_product_findings": unsupported_findings,
        "validation_method_mismatch": validation_mismatches,
        "authority_boundary_violations": authority_violations,
        "compact_path_regressions": compact_regressions,
        "manual_judgment_cases": manual_count,
        "manual_judgment_failures": manual_failures,
        "confirmed_production_defects": production_defects,
        "repair_loops": repair_loops,
        "unresolved_limitations": data.get("unresolved_limitations", []),
    }
    manifest = {
        "suite_id": data.get("suite_id"),
        "suite_version": data.get("suite_version"),
        "result": "PASS" if not issues else "FAIL",
        "case_ids": ids,
        "coverage": coverage,
        "class_counts": dict(sorted(class_counts.items())),
        "source_counts": dict(sorted(source_counts.items())),
        "mode_counts": dict(sorted(mode_counts.items())),
        "finding_counts": dict(sorted(finding_counts.items())),
        "validation_disposition_counts": dict(sorted(disposition_counts.items())),
        "validation_methods": sorted(validation_methods),
        "pair_members": dict(sorted(pair_members.items())),
        "metrics": metrics,
    }
    return manifest, issues


def _print_text(manifest: dict[str, Any], issues: list[str]) -> None:
    print(f"Evaluation suite: {manifest.get('suite_id')}")
    print(f"Result: {manifest.get('result')}")
    coverage = manifest.get("coverage", {})
    for key in sorted(coverage):
        print(f"coverage.{key}: {coverage[key]}")
    metrics = manifest.get("metrics", {})
    for key in sorted(metrics):
        print(f"metric.{key}: {metrics[key]}")
    if issues:
        print("Issues:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("Issues: none")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("suite", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    data = json.loads(args.suite.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        print("error: suite root must be an object")
        return 2
    manifest, issues = evaluate_suite(data)
    if args.format == "json":
        print(json.dumps({"manifest": manifest, "issues": issues}, ensure_ascii=False, indent=2))
    else:
        _print_text(manifest, issues)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
