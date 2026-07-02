# Executive Summary

Studio Audit Framework is a reusable methodology for independent maturity
audits of AI Software Studio.

It answers how an audit should be planned, what areas should be assessed, how
criteria should be scored, what evidence is admissible, how maturity is
determined, how issues are prioritized, and how a future Audit Report should be
structured.

This document is not an audit. It contains no assessment of the current Studio.

## Source Principle

The Framework is Knowledge-Base-bound:

- every criterion must link to one or more KB records or KB model documents;
- every rationale must be derived from KB knowledge;
- every unsupported candidate criterion must be recorded as a KB gap;
- the Framework must not silently convert auditor preference into a requirement.

Primary source:

- `/ai-editorial-office/kb/ai-software-studio-knowledge-base/`

Task-local evidence map:

- `../sources.md`
- `../research.md`
- `../claims_table.md`

## What the Framework Evaluates

The Framework evaluates AI Software Studio as an intelligent production system:
a sociotechnical system that repeatedly creates valuable outputs by combining
people, tools, processes, knowledge, feedback, governance, and continuous
improvement.

Audit areas:

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

## How Maturity Is Determined

The Framework uses a custom maturity model because the KB warns against
single-metric productivity, context-free ranking, and maturity ladder chasing.

Each criterion is rated from `M0` to `M5`:

- `M0 Not evidenced`
- `M1 Ad hoc`
- `M2 Defined`
- `M3 Operated`
- `M4 Measured`
- `M5 Learning`

Each rating also carries:

- evidence confidence;
- KB support level;
- applicability limit;
- issue priority, if any.

Area and Studio maturity are not simple averages. Critical issues and weak
evidence can cap maturity even when many criteria look mature.

## How Issues Are Prioritized

Findings are classified as:

- `Critical`: unsafe autonomy, false assurance, unreviewable change/claim,
  security or AI risk blind spot, inability to audit, or major knowledge loss.
- `Important`: material degradation of repeatability, decision quality,
  delivery reliability, product learning, maintainability, or governance.
- `Improvement`: useful maturation opportunity where current operation appears
  safe enough under available evidence.
- `No Change Needed`: adequate evidence of expected state and no material
  freshness/applicability concern.

## Future Audit Report Shape

A future Audit Report must contain:

- scope and independence statement;
- evidence inventory;
- area summaries;
- criterion-level findings;
- maturity profile;
- priority register;
- KB traceability appendix;
- KB gap appendix;
- limitations and excluded scope.

It must not present unsupported criteria as findings.

## Key KB Gaps Affecting Future Audits

The current KB is sufficient for the high-level methodology. It is not yet
sufficient for all possible detailed controls.

Important gaps include:

- no canonical BRD governance;
- no canonical Product Analyst, Validator, or Historian roles;
- no Studio-specific AI evaluation harness;
- no canonical architecture review artifact;
- no local incident process or severity taxonomy;
- no delivery or productivity measurement program;
- no exact ISO/IEC 25010 2023 mapping;
- no local security/AI-risk control mapping.

These gaps are future research needs. They are not current audit findings.

