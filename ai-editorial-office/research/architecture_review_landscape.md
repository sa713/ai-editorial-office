# Architecture Review Landscape For AI Editorial Office

Date: 2026-07-08

Status: research artifact only. This report does not modify AI Editorial Office
canon, roles, agents, pipelines, templates, `/about`, `project-state.md`,
`diff_intake.md`, or implementation behavior. Notes about AI Editorial Office
are observations only.

## 1. Executive Summary

World-class architecture review is a disciplined decision-support practice. It
does not merely ask whether a design is elegant, whether code is clean, or
whether a product idea is attractive. It asks whether the architecture is fit
for its drivers, constraints, risks, quality attributes, lifecycle, operating
model, and stakeholder concerns.

Across software architecture, enterprise architecture, cloud architecture,
systems engineering, secure SDLC, threat modeling, reliability engineering,
ADR/RFC practice, and governance, strong architecture review repeatedly shows
the same pattern:

- It starts from architectural drivers, not from a diagram.
- It distinguishes architecture decisions from implementation details.
- It evaluates quality attributes through concrete scenarios.
- It compares tradeoffs instead of treating preferences as proof.
- It makes assumptions, constraints, risks, non-risks, and residual risk
  inspectable.
- It tests designs against stakeholder concerns, operating realities, and
  lifecycle consequences.
- It treats security and reliability as architecture concerns, not late
  checklist reviews.
- It records decision rationale so future maintainers can understand why the
  system is shaped the way it is.
- It avoids bureaucracy by applying deeper review only to decisions with
  architectural significance.
- It is complete when reviewers can make a bounded confidence judgment about
  fitness, risks, required changes, and accepted tradeoffs.

The strongest recurring professional model is scenario-based review. SEI ATAM
evaluates architectures against quality attribute goals, discovers risks,
non-risks, sensitivity points, tradeoff points, and risk themes, and reports
findings to stakeholders. Cloud well-architected frameworks use pillar-based
question sets to assess operational excellence, security, reliability,
performance, cost, and sustainability. Systems engineering reviews trace
architecture back to stakeholder expectations, requirements, interfaces,
verification, and feasibility. Threat modeling reviews security architecture by
asking what is being built, what can go wrong, what will be done, and whether
the team did a good enough job.

Important distinction: architecture review is not code review at a higher level
of abstraction. Code review inspects implementation quality and change safety.
Architecture review inspects whether the design commitments, boundaries,
dependencies, quality attributes, tradeoffs, risks, and decision rationale are
appropriate before or during implementation.

## 2. Architecture Review Competency Map

| Competency | Professional expression | What strong reviewers do | Typical evidence |
| --- | --- | --- | --- |
| Driver discovery | SEI ATAM, systems engineering, enterprise architecture | Identify business, mission, user, technical, regulatory, operational, and lifecycle drivers | brief, mission need, stakeholder concerns, constraints, quality attribute scenarios |
| Architectural significance judgment | RFC, ADR, KEP, architecture governance | Decide whether a change needs architecture review or can stay in normal delivery | scope, reversibility, cross-team impact, quality-attribute impact, interface impact |
| Context modeling | ISO/IEC/IEEE 42010, systems engineering | Identify stakeholders, concerns, system boundary, environment, views, interfaces, assumptions | architecture description, context view, ConOps, dependency map |
| Quality attribute evaluation | SEI ATAM, AWS, Google Cloud, Azure | Test design against concrete scenarios for reliability, security, performance, maintainability, operability, cost, and sustainability | utility tree, well-architected answers, SLOs, tests, operational data |
| Tradeoff analysis | ATAM, NASA trade studies, ADR practice | Compare alternatives against drivers and quality consequences | option matrix, trade study, rejected alternatives, decision rationale |
| Risk analysis | ATAM, NIST RMF, threat modeling, reliability review | Identify risk, non-risk, residual risk, likelihood, consequence, controls, and monitoring triggers | risk register, threat model, risk themes, assurance argument |
| Assumption challenge | Threat modeling, systems engineering, design review | Surface assumptions that must remain true for the architecture to work | assumption log, constraint list, validation plan |
| Security reasoning | OWASP, NIST, secure SDLC | Analyze threats, mitigations, security requirements, control evidence, and abuse paths | threat model, ASVS controls, security architecture view |
| Operability review | Cloud well-architected, SRE | Check observability, deployment, incident response, recovery, ownership, and automation | runbooks, telemetry plan, recovery tests, operational readiness review |
| Decision documentation | ADRs, RFCs, KEPs, ISO architecture descriptions | Record context, decision, alternatives, consequences, status, and future revision triggers | ADR, RFC, KEP, architecture decision log |
| Governance calibration | TOGAF, architecture boards, open-source RFCs | Keep review proportional to risk and significance; avoid using review as paperwork | review threshold, routing criteria, lightweight approval path |
| Finding communication | ATAM, review boards, security assessment | Communicate actionable findings, confidence, required changes, accepted risk, and decision owner | out-brief, written report, blockers, accepted-risk note |

Architecture review competence is therefore a combination of systems thinking,
quality-attribute reasoning, risk reasoning, stakeholder translation, and
decision traceability.

## 3. Professional Architecture Review Workflows

### 3.1 SEI Architecture Evaluation / ATAM

The Architecture Tradeoff Analysis Method is one of the clearest professional
architecture review models. It frames architecture evaluation around business
drivers, quality attribute goals, scenarios, architectural approaches, risks,
non-risks, sensitivity points, tradeoff points, and risk themes.

Common flow:

1. Present the review method and scope.
2. Present business drivers and primary architectural drivers.
3. Present the architecture at enough detail for evaluation.
4. Identify architectural approaches and design commitments.
5. Build a quality attribute utility tree.
6. Analyze architectural approaches against high-priority scenarios.
7. Brainstorm and prioritize additional stakeholder scenarios.
8. Re-analyze architecture against the expanded scenario set.
9. Present risks, non-risks, sensitivity points, tradeoff points, risk themes,
   and major findings.

Distinctive strengths:

- Review is stakeholder-facing and decision-oriented.
- Quality attributes are made concrete through scenarios.
- Architecture is assessed before all implementation evidence exists.
- Tradeoffs are first-class review objects.
- The output is not a pass/fail label only; it is a structured risk and
  decision record.

### 3.2 ISO/IEC/IEEE 42010 Architecture Description Review

ISO/IEC/IEEE 42010 separates architecture from architecture description. That
distinction matters for review: reviewers inspect the description as evidence
for the architecture, but the description is not the architecture itself.

Common review questions from this tradition:

- Is the entity of interest clear?
- Are stakeholders and their concerns identified?
- Are views governed by viewpoints?
- Does each view answer a stakeholder concern?
- Are correspondences and known inconsistencies between views visible?
- Is the architecture description useful for communication, analysis, and
  decision support?

Distinctive strengths:

- Review is organized around stakeholder concerns and viewpoints.
- Multiple views are expected because different concerns need different
  evidence.
- Consistency between views is a review concern, not a documentation nicety.
- Architecture description is a communication and evaluation artifact, not only
  a storage place for diagrams.

### 3.3 Cloud Well-Architected Review

AWS, Google Cloud, and Microsoft Azure all use pillar-based review models. The
exact pillar names differ, but the common review surface is stable:

- operational excellence or operability;
- security, privacy, and compliance;
- reliability and resilience;
- performance efficiency or optimization;
- cost optimization;
- sustainability, in AWS and Google Cloud;
- workload-specific or domain-specific perspectives.

Common flow:

1. Define workload, business context, users, and operating environment.
2. Evaluate the architecture against pillar questions or principles.
3. Identify risks, weaknesses, and improvement areas.
4. Prioritize findings by workload value and risk.
5. Record remediation or accepted risk.
6. Revisit the review as the workload evolves.

Distinctive strengths:

- Review is framed as a constructive conversation, not an audit.
- Pillars keep quality attributes visible across cloud design choices.
- Review tools make the process repeatable.
- Operational and cost consequences are treated as architecture consequences.
- Guidance is updated as cloud platforms and practices evolve.

### 3.4 Enterprise Architecture Governance Review

Enterprise architecture review boards and TOGAF-style governance focus on
alignment between business goals, architecture principles, standards,
roadmaps, target architecture, migration paths, and implementation projects.
In strong organizations, governance is not a committee that approves diagrams.
It is a mechanism for resolving cross-team design consequences and preventing
local optimization from damaging enterprise coherence.

Common flow:

1. Confirm the architecture scope and decision authority.
2. Identify applicable principles, standards, roadmaps, and constraints.
3. Check alignment with business, data, application, and technology
   architecture.
4. Identify deviations, waivers, dependencies, and migration implications.
5. Record decisions, conditions, exceptions, and follow-up ownership.

Distinctive strengths:

- Review looks across organizational boundaries.
- It checks architecture against target-state direction and standards.
- It distinguishes justified exceptions from unmanaged drift.
- It can expose duplicated capabilities, hidden integration costs, and
  platform fragmentation.

### 3.5 Systems Engineering Technical Review

NASA-style systems engineering frames design review as recursive validation of
stakeholder expectations, requirements, logical decomposition, design solution,
concept of operations, feasibility, cost, schedule, and verification. The
architecture is credible only when it can be traced back to mission need and
forward to verification.

Common flow:

1. Capture stakeholder expectations, mission objectives, constraints, and
   concept of operations.
2. Define technical requirements and success criteria.
3. Decompose the system logically.
4. Develop design solutions and architecture alternatives.
5. Analyze feasibility, consistency, cost, schedule, operation, and technical
   risk.
6. Validate that architecture, ConOps, and requirements are mutually
   consistent.
7. Baseline only when the design is credible enough for the next phase.

Distinctive strengths:

- Needs, goals, objectives, requirements, design, and verification are kept
  distinct.
- Traceability is essential, not decorative.
- Independent review team credibility matters.
- Completion depends on sufficient analytical maturity for the lifecycle phase.

### 3.6 Security Architecture Review And Threat Modeling

Security architecture review overlaps architecture review but is not identical
to it. Threat modeling gives architecture review a security lens: identify what
is being built, what can go wrong, what mitigations exist, and whether the work
was good enough for the system at hand.

Common flow:

1. Define the subject, assets, boundaries, trust zones, entry points, and
   assumptions.
2. Identify threats through structured methods such as STRIDE, attack trees,
   kill chains, abuse cases, or adversary paths.
3. Identify mitigations, controls, residual risks, and verification evidence.
4. Prioritize security improvements by likelihood, impact, exploitability, and
   business consequence.
5. Revisit the model when features, incidents, infrastructure, or architecture
   change.

Distinctive strengths:

- Threats are tied to a concrete model of the system.
- Assumptions are explicitly challengeable.
- Review produces a prioritized list of improvements, not only a risk label.
- Security decisions become rational and explainable.

### 3.7 RFC, KEP, And ADR Review

Mature engineering communities use RFCs, Kubernetes Enhancement Proposals, and
Architecture Decision Records to make significant decisions reviewable before
or during implementation.

Common flow:

1. Apply a significance threshold: substantial or non-trivial changes need a
   proposal; small implementation work can use ordinary code review.
2. Socialize the idea with relevant maintainers or stakeholders.
3. Write the proposal with motivation, design, alternatives, drawbacks,
   unresolved questions, and rollout.
4. Collect review feedback publicly or in a traceable forum.
5. Decide when tradeoffs are sufficiently understood.
6. Record decision status and rationale.
7. Track implementation separately from the decision record.

Distinctive strengths:

- Review is lightweight by default but strong for significant changes.
- Alternatives and drawbacks are expected, not embarrassing.
- Decision acceptance is not an implementation guarantee.
- Historical decision records help future maintainers understand why.

## 4. Architecture Drivers And Context

Professional architecture review begins with drivers because architecture only
has meaning relative to a problem, stakeholder set, and operating context.

Common driver classes:

| Driver class | Review question |
| --- | --- |
| Business or mission driver | What organizational outcome or mission need makes this architecture matter? |
| User or customer driver | What user-visible quality or workflow does the architecture need to support? |
| Quality attribute driver | Which qualities materially shape the design: reliability, security, modifiability, performance, cost, operability, scalability, usability, compliance, sustainability? |
| Constraint | What cannot change: regulation, platform, budget, deadline, team skill, deployment model, data residency, compatibility, existing contract? |
| Risk driver | What failure would be expensive, unsafe, irreversible, or reputation-damaging? |
| Lifecycle driver | How will the system be built, operated, evolved, monitored, retired, or handed over? |
| Integration driver | Which external systems, interfaces, protocols, or organizational teams shape the architecture? |
| Governance driver | Which principles, standards, policies, approvals, or accepted-risk decisions apply? |

Architecture review becomes weak when drivers are vague. "Scalable" is not a
driver until the scale, stimulus, response, environment, and business
importance are visible. "Secure" is not a driver until assets, threats,
controls, and residual risk are visible. "Maintainable" is not a driver until
the expected change patterns and ownership model are visible.

A strong review therefore asks:

- What decision is the architecture review supporting?
- What would make the architecture unacceptable?
- What qualities are primary, and which qualities are allowed to lose?
- Which stakeholders are represented, and which are missing?
- Which constraints are real constraints versus preferences?
- Which assumptions must remain true for the design to work?

## 5. Quality Attribute Evaluation

Quality attributes are central because architecture is usually where qualities
conflict. Professional review turns vague qualities into testable scenarios.

Scenario structure often includes:

- source of stimulus;
- stimulus;
- environment;
- artifact or part of system affected;
- expected response;
- response measure.

Examples:

| Quality attribute | Architecture review evidence |
| --- | --- |
| Reliability | SLOs, failure modes, redundancy model, recovery objectives, fault-injection or recovery test plan, graceful degradation behavior |
| Security | trust boundaries, threat model, control mapping, identity and access model, abuse cases, data protection, auditability |
| Performance | workload model, latency or throughput targets, bottleneck analysis, capacity assumptions, scale tests |
| Scalability | growth model, partitioning strategy, horizontal scaling path, state management, quota or limit analysis |
| Maintainability | change scenarios, modular boundaries, dependency direction, ownership, upgrade path, coupling analysis |
| Operability | observability, alerting, runbooks, deployment path, rollback, incident response, support ownership |
| Cost | unit economics, resource model, elasticity, waste controls, financial ownership, cost-risk tradeoffs |
| Sustainability | resource efficiency, region choices, utilization, data retention, lifecycle carbon considerations |
| Compliance | data classification, residency, control evidence, audit trail, retention, policy exception path |

Strong review does not ask whether every quality is maximized. It asks whether
the architecture makes the right tradeoffs for the drivers. A highly available
architecture may cost more and be harder to operate. A simple architecture may
be less flexible. A heavily governed architecture may be safer but slower to
change. Architecture review makes these consequences explicit.

## 6. Tradeoff Analysis

Architecture review is tradeoff review. If there are no meaningful tradeoffs,
the decision may not be architectural.

Professional tradeoff analysis typically compares:

- selected option;
- credible alternatives;
- rejected alternatives;
- decision criteria;
- quality attribute effects;
- risk effects;
- implementation and operating cost;
- reversibility;
- migration consequences;
- dependency and ownership effects;
- known unknowns and revision triggers.

ATAM makes tradeoffs explicit through sensitivity points and tradeoff points.
ADR and RFC practice makes tradeoffs explicit through alternatives,
drawbacks, rationale, and consequences. Systems engineering uses trade studies
to compare design alternatives against mission, cost, schedule, risk, and
technical criteria.

Useful review heuristics:

- If the design has no rejected alternatives, reviewers should suspect
  first-plausible convergence.
- If an option wins on every dimension, the criteria are probably too vague.
- If tradeoffs are described as preferences, the evidence is probably weak.
- If a tradeoff affects another team, lifecycle phase, or quality attribute, it
  is architectural until proven otherwise.
- If a decision is hard to reverse, review depth should increase.

Architectural tradeoff differs from preference. Preference is "we like this
tool." Tradeoff is "this tool improves operational simplicity and team
familiarity, but increases vendor coupling and limits portability; those losses
are acceptable because the workload has low portability need and high support
risk."

## 7. Risk And Threat Assessment

Architecture risk is a possibility that an architectural decision, omission, or
assumption will prevent the system from meeting important drivers. It is not
the same as ordinary task risk. Ordinary task risk may concern schedule,
writing quality, or implementation defects. Architecture risk concerns system
shape: dependencies, boundaries, quality attributes, security posture,
operability, scaling path, governance fit, and future change cost.

Common architecture risk categories:

| Risk category | Review signal |
| --- | --- |
| Driver mismatch | Architecture optimizes for a quality that is not actually primary. |
| Hidden assumption | Design relies on workload, team, vendor, data, or threat assumptions that are not validated. |
| Quality attribute conflict | A choice improves one quality while silently weakening another. |
| Interface fragility | External contracts, schemas, APIs, or organizational boundaries are unstable or underspecified. |
| Security exposure | Trust boundaries, identity, data protection, or threat mitigations are weak or implicit. |
| Reliability gap | Failure modes, recovery objectives, dependency failure, or degradation paths are unclear. |
| Operability gap | Monitoring, deployment, rollback, ownership, and incident response are absent. |
| Scalability illusion | Load, state, quota, or bottleneck assumptions are asserted without evidence. |
| Maintainability debt | Coupling, ownership, or module boundaries make expected changes expensive. |
| Governance drift | Architecture violates principles, standards, compliance, or accepted direction without a recorded exception. |
| Documentation incoherence | Views conflict, decision rationale is missing, or the description cannot support review. |

Threat assessment is a specialized security-risk practice. OWASP threat
modeling emphasizes scope, threats, mitigations, validation, and continuous
updates when features, incidents, or architecture change. NIST RMF emphasizes
risk-based control selection, implementation, assessment, authorization,
continuous monitoring, and accountability. Cloud frameworks connect security
review with identity, data protection, detection, incident response, and shared
responsibility.

Strong architecture review handles risk with precision:

- name the risk;
- identify the architectural cause;
- identify affected driver or quality attribute;
- classify likelihood and consequence at the right granularity;
- distinguish current risk from future risk;
- identify mitigation, fallback, monitoring, or accepted-risk owner;
- record residual risk.

## 8. Decision Documentation

Decision documentation is how architecture review survives time. Without it,
future teams inherit shape without rationale.

Common decision record contents:

- decision title and status;
- context and problem;
- drivers and constraints;
- options considered;
- selected decision;
- rationale;
- consequences;
- risks and mitigations;
- rejected alternatives;
- dependencies;
- decision owner and stakeholders;
- date and revision/supersession history.

ADR guidance emphasizes capturing important architecture decisions with context
and consequences. Rust RFCs and Kubernetes KEPs show how proposal processes can
separate design acceptance from implementation. ISO/IEC/IEEE 42010 shows how
architecture descriptions support communication and review through views,
viewpoints, stakeholders, concerns, and correspondences.

Good decision documentation is not a transcript. It is a compact record of the
decision and the reasoning needed to review, implement, revisit, or supersede
it. It should make future change cheaper by preserving why the architecture is
the way it is.

## 9. Review Board And Governance Practices

Architecture review boards can protect coherence, but they can also become
bottlenecks. Mature practice calibrates governance by significance.

Healthy governance patterns:

- Review thresholds are clear: substantial, cross-cutting, irreversible,
  high-risk, standards-affecting, or quality-attribute-impacting changes need
  architecture review.
- Small changes remain in normal delivery and code review.
- The review board includes people who can assess the relevant concerns:
  architecture, security, reliability, operations, platform, data, product, and
  business.
- Review is constructive decision support, not a surprise audit.
- Exceptions and waivers are explicit, time-bounded when appropriate, and tied
  to owners.
- Findings distinguish blockers, required changes, accepted risks, and
  advisory improvements.
- Decisions are recorded where future implementers can find them.
- Governance monitors drift and learning, not only initial approval.

Anti-bureaucracy lessons from RFC and KEP practice:

- Require proposals for non-trivial changes, not for everything.
- Encourage pre-review socialization before formal review.
- Make templates useful but not ornamental.
- Record major tradeoffs and unresolved questions.
- Use final-comment or final-review periods only when the decision is mature
  enough for closure.
- Keep implementation tracking separate from architecture decision acceptance.

## 10. Review Artifacts And Deliverables

Professional architecture review artifacts are views over the architecture
decision, not the decision itself. The right artifact depends on review scope.

Common artifacts:

| Artifact | Review value | Failure if misused |
| --- | --- | --- |
| Architecture description | Communicates structure, behavior, views, context, and concerns | Becomes diagram inventory without decision value |
| Context diagram | Exposes system boundary, actors, external dependencies, and trust boundaries | Hides non-technical stakeholders or lifecycle context |
| Quality attribute scenarios | Make non-functional requirements testable | Turn into vague labels such as "fast" or "secure" |
| Utility tree | Prioritizes quality drivers | Becomes a taxonomy instead of a decision aid |
| Tradeoff matrix | Compares alternatives against drivers | Becomes preference scoring without evidence |
| Threat model | Exposes assets, threats, mitigations, and residual risk | Becomes a one-time security checklist |
| Risk register or risk themes | Records architecture risks and their business impact | Records symptoms without architectural cause |
| ADR | Captures one important decision and consequences | Becomes paperwork for tiny or already-settled choices |
| RFC or KEP | Coordinates significant design change across stakeholders | Becomes implementation plan with hidden decision criteria |
| Review report or out-brief | Communicates findings, required changes, accepted risks, and confidence | Becomes vague approval without actionable findings |

Architecture evidence differs from general evidence. General evidence supports
claims. Architecture evidence supports fitness of design decisions under
drivers and constraints. It may include diagrams, scenarios, benchmark data,
load tests, threat models, incident history, runbooks, dependency analysis,
policy mappings, stakeholder concerns, cost models, and prior decision records.

## 11. Common Architecture Review Failure Modes

| Failure mode | Signal | Professional recovery pattern |
| --- | --- | --- |
| Diagram review masquerading as architecture review | Review focuses on box-and-arrow notation but not drivers, risks, or tradeoffs | Return to drivers, scenarios, and decision questions |
| Driver blindness | Architecture is evaluated without business, mission, user, or operating context | Reconstruct architectural drivers and stakeholder concerns |
| Quality-label review | Review asks whether system is "secure" or "scalable" without concrete scenarios | Convert qualities into measurable scenarios |
| First-plausible architecture | Only one option is presented; alternatives are absent or strawmen | Require credible alternatives and rejected-option rationale |
| Security as late audit | Threats appear after architecture decisions are fixed | Threat-model early and revisit on architectural change |
| Operability omission | Deployment, monitoring, recovery, ownership, and incident response are missing | Add operational readiness evidence to review |
| False assurance | Review approves based on confidence tone or seniority rather than evidence | Ask what evidence supports the quality and risk judgment |
| Hidden accepted risk | A risk is known but not assigned, accepted, or mitigated | Record owner, residual risk, and decision authority |
| Board bottleneck | Every small change requires architecture approval | Apply significance thresholds and lightweight paths |
| Paper compliance | Templates are completed but decision quality is weak | Review rationale, tradeoffs, and actionable consequences |
| Local optimization | One team improves its design while increasing enterprise/platform cost | Review cross-boundary effects and shared constraints |
| Stale architecture record | Decision record no longer matches implementation or operating reality | Mark superseded, update decision history, or re-review |
| Code-review substitution | Review waits until implementation PRs to challenge architecture | Move architecture challenge earlier for significant changes |
| Product-review substitution | Review discusses desirability but not design fitness | Separate product value from architecture feasibility and risk |

## 12. Best Professional Practices

The strongest practices across sources are practical and repeatable:

- Start with the decision the review must support.
- Identify architectural drivers before evaluating design.
- Use scenarios to evaluate quality attributes.
- Treat architecture as a set of consequential decisions, not only components.
- Review architecture descriptions through stakeholder concerns and viewpoints.
- Compare credible alternatives and record rejected options.
- Identify risks, non-risks, sensitivity points, tradeoff points, and residual
  risk.
- Challenge assumptions that shape the architecture.
- Include security, reliability, operability, cost, and maintainability early.
- Distinguish architecture review from code review, security review, and
  product review.
- Keep architecture review proportional to architectural significance.
- Use lightweight decision records for durable rationale.
- Make review findings actionable: blocker, required change, accepted risk,
  advisory, or follow-up.
- Revisit architecture when drivers, constraints, threats, workloads, or
  operating evidence change.

The most valuable review heuristics:

- If a change crosses boundaries, changes interfaces, affects a quality
  attribute, constrains future choices, or is hard to reverse, it is probably
  architectural.
- If a review cannot name the primary drivers, it cannot judge fitness.
- If a quality attribute has no scenario, reviewers are probably debating
  vocabulary.
- If no tradeoff is visible, the decision may be too small for architecture
  review or the analysis is incomplete.
- If security or operability enters only after implementation, the review is
  late.
- If a decision record lacks consequences, it records preference rather than
  architecture rationale.
- If a review finding lacks owner, severity, and required action, it is not yet
  useful.

## 13. Preliminary Notes For AI Editorial Office

Observations only:

- The current AI Editorial Office architecture already contains several ideas
  that professional architecture review sources treat as important: explicit
  canonical ownership, role boundaries, capability separation, evidence
  quality, analytical reasoning, review independence, and artifact-as-view
  semantics.
- Professional architecture review sources repeatedly separate decision,
  evidence, view, and implementation. That maps conceptually to the current
  principle that artifacts are views over task state.
- ATAM's distinction between risks, non-risks, sensitivity points, tradeoff
  points, and risk themes is more architecture-specific than the general
  evidence or analytical reasoning vocabulary.
- Cloud well-architected frameworks provide a mature pattern for reviewing
  quality attributes without creating one monolithic quality checklist:
  pillars organize questions, while workload context determines materiality.
- Systems engineering sources emphasize traceability from stakeholder need to
  requirements, architecture, verification, and lifecycle phase. This is close
  to the current task-object and reviewability emphasis, but in a more
  architecture-specific setting.
- Threat modeling sources show that security review can be a specialized lens
  inside architecture review without replacing architecture review itself.
- RFC, KEP, and ADR practices show a strong professional pattern of applying
  heavier review only to substantial or non-trivial changes while keeping
  smaller changes lightweight.
- Architecture review findings in professional practice are most useful when
  they distinguish blockers, required changes, accepted risks, non-risks,
  unresolved assumptions, and advisory improvements.
- Professional sources consistently treat architecture review as different from
  code review: architecture review evaluates design commitments and quality
  consequences; code review evaluates implementation changes.
- Professional sources consistently treat architecture review as different from
  product review: architecture review evaluates fitness and consequences of the
  system shape; product review evaluates user/business desirability and product
  direction.
- Professional sources also separate architecture review from security review:
  security review can be one architectural concern or lens, but architecture
  review includes additional qualities such as operability, maintainability,
  reliability, scalability, cost, and evolution.
- A recurring warning across source families is that review can become
  performative if templates replace judgment, diagrams replace drivers, or
  approval replaces risk communication.

## 14. Sources

### Primary And Authoritative Sources

- Carnegie Mellon Software Engineering Institute, "Architecture Tradeoff
  Analysis Method Collection":
  <https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=513908>
- Rick Kazman, Mark Klein, Paul Clements, Carnegie Mellon Software Engineering
  Institute, "ATAM: Method for Architecture Evaluation" (CMU/SEI-2000-TR-004):
  <https://resources.sei.cmu.edu/asset_files/TechnicalReport/2000_005_001_13706.pdf>
- ISO, "ISO/IEC/IEEE 42010:2022 Software, systems and enterprise -
  Architecture description":
  <https://www.iso.org/standard/74393.html>
- IEEE Standards Association, "IEEE/ISO/IEC 42010-2022":
  <https://standards.ieee.org/ieee/42010/6846/>
- AWS, "AWS Well-Architected Framework":
  <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- Google Cloud, "Google Cloud Well-Architected Framework":
  <https://cloud.google.com/architecture/framework>
- Microsoft Learn, "Azure Well-Architected Framework":
  <https://learn.microsoft.com/en-us/azure/well-architected/>
- NIST CSRC, "NIST Risk Management Framework":
  <https://csrc.nist.gov/projects/risk-management/about-rmf>
- NIST CSRC, "SP 800-37 Rev. 2, Risk Management Framework for Information
  Systems and Organizations":
  <https://csrc.nist.gov/pubs/sp/800/37/r2/final>
- OWASP, "Threat Modeling":
  <https://owasp.org/www-community/Threat_Modeling>
- OWASP, "Application Security Verification Standard":
  <https://owasp.org/www-project-application-security-verification-standard/>
- NASA, "Systems Engineering Handbook, 4.0 System Design Processes":
  <https://www.nasa.gov/reference/4-0-system-design-processes/>
- Rust Project, "Rust RFCs":
  <https://github.com/rust-lang/rfcs>
- Kubernetes, "Kubernetes Enhancement Proposals":
  <https://github.com/kubernetes/enhancements/tree/master/keps>
- Architecture Decision Record community repository:
  <https://github.com/architecture-decision-record/architecture-decision-record>
- Michael Nygard, "Documenting Architecture Decisions":
  <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>

### Source Quality Assessment

- Strongest software-architecture evaluation source: SEI ATAM. It is directly
  about architecture evaluation, tradeoffs, quality attributes, risk themes,
  and stakeholder review.
- Strongest architecture-description source: ISO/IEC/IEEE 42010. It is a formal
  standard and is especially useful for stakeholder concerns, viewpoints, views,
  correspondences, and architecture-description boundaries.
- Strongest cloud review sources: AWS, Google Cloud, and Azure
  Well-Architected frameworks. They are vendor-specific, but authoritative and
  operationally mature for cloud workload review.
- Strongest security review sources: OWASP threat modeling and NIST RMF. OWASP
  is more practitioner-oriented; NIST is more governance, risk, control, and
  authorization oriented.
- Strongest systems engineering source: NASA Systems Engineering Handbook. It
  is useful for stakeholder expectations, requirements traceability,
  decomposition, feasibility, independent review, and lifecycle phase maturity.
- Strongest decision-record/process sources: Rust RFCs, Kubernetes KEPs, and
  ADR guidance. They are not general architecture standards, but they show
  mature lightweight practices for deciding when design review is necessary,
  how to record rationale, and how to avoid process overreach.
