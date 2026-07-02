# Research Synthesis

## Research Question

What audit methodology can be derived from the existing AI Software Studio
Knowledge Base without evaluating the current Studio implementation?

## Scope and Constraint

This synthesis is for methodology design only. It does not determine whether AI
Software Studio currently conforms to any criterion.

All criteria in the future Framework must be justified by KB records or clearly
marked as unsupported/gap-driven.

## KB-Derived Audit Premises

1. AI Software Studio should be audited as an intelligent production system,
   not only as a software repository or AI toolchain. The KB definition combines
   people, tools, processes, knowledge, feedback, governance, and continuous
   improvement.
   KB basis: `glossary-intelligent-production-system`,
   `principle-sociotechnical-production-system`.

2. Mature operation requires autonomy with explicit guardrails, role boundaries,
   decision rights, feedback, escalation, and review. Autonomy without evidence
   or guardrails becomes hidden risk; excessive approval becomes bottleneck or
   rubber-stamp control.
   KB basis: `principle-autonomy-with-guardrails`,
   `pattern-human-ai-checkpoints`, `anti-pattern-human-rubber-stamp-ai`.

3. Quality must be built into the work system and verified through meaningful
   independent checks. Late inspection alone is insufficient, but built-in
   quality does not remove residual risk or independent review needs.
   KB basis: `principle-built-in-quality`, `practice-modern-code-review`,
   `practice-checklists-at-pause-points`, `anti-pattern-checklist-theater`.

4. Knowledge must remain close to work, source-linked, current, and retrievable.
   A KB that is merely a document dump is not organizational memory.
   KB basis: `principle-knowledge-close-to-work`,
   `pattern-provenance-linked-knowledge`,
   `practice-context-and-memory-management`,
   `anti-pattern-knowledge-dump-kb`.

5. AI-agent capability must be evaluated through real workflow evidence,
   tool-loop observability, permissions, context management, and regression
   checks. Demos, anecdotal success, or benchmark scores alone are insufficient.
   KB basis: `pattern-agent-tool-loop`, `pattern-agent-computer-interface`,
   `practice-ai-evaluation-harness`,
   `case-study-swe-bench-and-swe-agent`,
   `anti-pattern-agentic-overengineering`.

6. Delivery maturity is not just speed. It combines small batches, meaningful
   automated checks, secure lifecycle controls, reliability objectives,
   incident learning, and balanced delivery metrics.
   KB basis: `pattern-small-batches`,
   `pattern-continuous-delivery-pipeline`, `pattern-slo-error-budget`,
   `practice-secure-sdlc-ssdf`, `process-incident-management`,
   `metric-dora-four-key-metrics`.

7. Platform capability should be assessed as a product-like internal capability,
   not as a ticket queue or portal UI. Golden paths are useful only when
   maintained, adopted, and paired with justified exceptions.
   KB basis: `pattern-platform-as-product`, `pattern-golden-paths`,
   `framework-platform-maturity`,
   `anti-pattern-platform-as-ticket-queue`,
   `anti-pattern-portal-equals-platform`,
   `tool-internal-developer-portal`.

8. Product and roadmap decisions should be connected to outcomes, customer/user
   evidence, opportunities, alternatives, and experiments. Shipping output is
   not proof of value.
   KB basis: `practice-continuous-discovery`, `pattern-product-trio`,
   `pattern-opportunity-solution-tree`, `anti-pattern-feature-factory`.

9. Measurement must be balanced, contextual, and decision-linked. Single
   productivity metrics and context-free rankings are explicitly warned against.
   KB basis: `framework-space`, `metric-space-balanced-productivity`,
   `framework-dora-core`, `metric-dora-four-key-metrics`,
   `anti-pattern-single-metric-productivity`.

10. Architecture, decisions, and governance must be reviewable through
    stakeholder concerns, viewpoints, compact decision records, status, and
    consequences. Documentation form should match user need.
    KB basis: `standard-iso-42010`,
    `practice-architecture-review-by-viewpoints`,
    `pattern-adr-decision-log`, `decision-technique-adr`,
    `framework-diataxis`.

## Derived Audit Areas

The following areas are justified by KB domain navigation and records:

1. System Governance and Sociotechnical Operating Model.
2. Knowledge, Memory, and Provenance.
3. AI-Agent Work System and Human-AI Control.
4. Built-in Quality, Review, and Verification.
5. Delivery Flow, Reliability, and Operations.
6. Platform Capability and Golden Paths.
7. Product Discovery and Value Validation.
8. Security and AI Risk Management.
9. Measurement, Feedback, and Continuous Improvement.
10. Architecture, Decisions, and Documentation.

These areas intentionally do not mirror the current Studio folder structure.
They come from the KB model of intelligent production systems.

## Assessment Model Implications

- Criterion maturity should measure repeatable capability and evidence quality,
  not merely presence of a file, role name, tool, or checklist.
- Area maturity should aggregate criterion ratings with blockers and evidence
  confidence; a critical governance or safety failure should cap area maturity.
- Studio maturity should be multi-dimensional. It should not collapse to a
  single productivity or delivery number.
- KB support level must be part of every criterion: direct, supporting,
  analogical, or insufficient.
- Applicability limits must be explicit because several KB records are
  Accepted but not applied, Under Evaluation, Rejected for current context, or
  based on analogical case studies.

## Evidence Model Implications

Allowed evidence should include:

- active rules, role specs, pipeline documents, templates, manifests, status
  records, review records, final decisions, source registers, claim tables,
  architecture/decision records, test/eval outputs, CI/release evidence,
  operational logs, incident/postmortem artifacts, product discovery artifacts,
  metric definitions, survey/research summaries, and human approval evidence.

The Framework must distinguish:

- evidence of existence;
- evidence of usage;
- evidence of effectiveness;
- evidence of freshness;
- evidence of ownership;
- evidence of valid exception handling.

## Severity Model Implications

Priority should separate:

- Critical: failure creates unsafe autonomy, false assurance, unreviewable
  claims/changes, security or AI risk blind spots, unrecoverable knowledge loss,
  or inability to audit.
- Important: weakness materially degrades repeatability, decision quality,
  delivery reliability, product learning, or maintainability.
- Improvement: useful maturation opportunity where current evidence is adequate
  for safe operation.
- No Change Needed: criterion meets the expected state with adequate evidence
  and no material freshness or applicability concern.

## Knowledge Gaps Found

The KB is sufficient to design the high-level audit framework, but the following
knowledge is incomplete for strong criterion detail:

- No canonical BRD governance record or BRD artifact exists.
- Product Analyst, Validator, and Historian roles are reserved but not canonical.
- No Studio-specific AI evaluation harness design exists.
- No canonical architecture review artifact exists.
- No incident process exists in current Studio object map.
- No delivery metrics or productivity measurement program exists.
- No exact ISO/IEC 25010 2023 mapping is incorporated.
- A3 Problem Solving lacks direct A3-specific source depth.
- Platform maturity knowledge is accepted but not validated in Studio context.
- Security and AI risk standards are accepted references, but local control
  mapping is not present.
- Knowledge Graph is under evaluation; there is no proof that simple links are
  insufficient.

These gaps must become explicit Framework limitations and future research
recommendations, not invented criteria.

## Research Outcome

Research is sufficient for Writer Agent to draft the Framework package, provided
that every criterion retains explicit KB references and applicability limits.
