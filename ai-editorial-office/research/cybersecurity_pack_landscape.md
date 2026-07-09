# Cybersecurity Pack Landscape

Status: research complete for S4.R4 release synthesis.

Date: 2026-07-10

Research role: `research_agent`

## Research Question

What durable, source-backed cybersecurity knowledge should AI Editorial Office
package so future security-sensitive analysis, review, risk interpretation,
secure design, defensive recommendation, assurance, and professional
communication tasks can ask better questions without creating a new role,
capability, workflow, policy owner, review gate, or operational security
approval path?

## Source Selection

The research prioritized sources that are primary, authoritative, maintained,
or widely treated as standards for cybersecurity risk management, controls,
secure design, application security, threat/weakness vocabulary, and assurance:

- NIST cybersecurity risk, control, secure development, systems security, zero
  trust, and cyber resiliency publications;
- OWASP application and API security standards and cheat sheets;
- MITRE ATT&CK and CWE as maintained threat/weakness vocabularies;
- CIS Controls as prioritized defensive safeguards;
- ISO/IEC 27001 as an accessible ISMS reference;
- Microsoft SDL and STRIDE as practitioner threat-modeling and secure
  development guidance.

Excluded:

- shallow blogspam;
- operational exploit walkthroughs;
- penetration-testing or malware procedure sources;
- compliance-only material that would turn the pack into policy;
- incident-response operational playbooks beyond high-level defensive context;
- vendor marketing without inspectable security content.

## Executive Findings

Cybersecurity expertise belongs in AI Editorial Office as a Domain Knowledge
Pack: source-backed context for security-sensitive questions. It should help
existing roles and capabilities reason about assets, actors, trust boundaries,
threats, abuse cases, weakness classes, controls, evidence, assurance, and
residual risk.

The pack should emphasize:

- risk as a relationship among assets, threats, vulnerabilities, likelihood,
  impact, controls, evidence, and residual uncertainty;
- assets, actors, data, identities, privileges, interfaces, dependencies, and
  trust boundaries as first-class security context;
- secure design and threat modeling before control selection;
- authorization, authentication, access control, input handling,
  misconfiguration, cryptography, logging/monitoring, dependency, API, data,
  and resilience concerns as recurring review surfaces;
- MITRE ATT&CK for adversary tactic/technique vocabulary, not for offensive
  procedure reproduction;
- MITRE CWE for weakness vocabulary, root-cause framing, and weakness-to-risk
  analysis;
- NIST SP 800-53 and CIS Controls as control selection prompts, not automatic
  compliance verdicts;
- OWASP ASVS and API Security Top 10 as application/API security verification
  and awareness references;
- evidence and assurance proportional to security impact and blast radius;
- safety boundaries that keep pack use defensive and review-oriented.

The pack should not:

- decide whether Engineering Review, Architecture Review, or final governance
  passes;
- own cybersecurity policy, compliance attestation, incident response, approval,
  or operational security decisions;
- become a penetration-testing method, exploit guide, abuse playbook, or
  offensive capability reference;
- create a Security Reviewer role, security pipeline, approval gate, or
  mandatory artifact;
- duplicate the DevSecOps Domain Pack's delivery automation, CI/CD,
  supply-chain, deployment, and operational-security focus.

## Source Register

| Source | Class | Version/date | Last checked | Relevance | Confidence limits |
| --- | --- | --- | --- | --- | --- |
| NIST Cybersecurity Framework 2.0 Resource Center (`https://www.nist.gov/cyberframework`) | U.S. government framework resource | CSF 2.0, 2024; resource center current with 2026 updates | 2026-07-10 | Cybersecurity risk management framing, organizational profiles, informative references, governance/risk vocabulary | High for broad risk-management context; not a task-specific control checklist |
| NIST SP 800-37 Rev. 2, Risk Management Framework (`https://csrc.nist.gov/pubs/sp/800/37/r2/final`) | U.S. government special publication | December 2018 | 2026-07-10 | RMF process vocabulary, lifecycle risk management, categorization, control selection/assessment, monitoring | High for RMF concepts; not an AI Editorial Office lifecycle owner |
| NIST SP 800-53 Rev. 5, updated through Release 5.2.0 (`https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final`) | U.S. government control catalog | September 2020; planning note for Release 5.2.0, 2025-08-27 | 2026-07-10 | Security/privacy control families, functionality and assurance framing, control selection prompts | High for control vocabulary; detailed control claims need source-specific inspection |
| NIST SP 800-30 Rev. 1 (`https://csrc.nist.gov/pubs/sp/800/30/r1/final`) | U.S. government special publication | September 2012 | 2026-07-10 | Risk assessment, likelihood/impact, threat/vulnerability/residual-risk vocabulary | High for risk-assessment concepts; older but still canonical |
| NIST SP 800-218 SSDF v1.1 (`https://csrc.nist.gov/pubs/sp/800/218/final`) | U.S. government special publication | February 2022 | 2026-07-10 | Secure software development practices, vulnerability reduction, supplier communication | High for secure-development context; DevSecOps-specific delivery details belong in DevSecOps pack |
| NIST SP 800-160 Vol. 1 Rev. 1 (`https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final`) | U.S. government systems security engineering publication | November 2022 | 2026-07-10 | Secure systems engineering, trustworthiness, security requirements, assurance, validation/verification | High for secure design and assurance framing; systems-engineering depth must be task-scaled |
| NIST SP 800-160 Vol. 2 Rev. 1 (`https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final`) | U.S. government cyber resiliency publication | December 2021 | 2026-07-10 | Anticipate, withstand, recover, and adapt framing; resilience and adverse-condition context | High for resiliency concepts; not an incident-response playbook |
| NIST SP 800-207, Zero Trust Architecture (`https://csrc.nist.gov/pubs/sp/800/207/final`) | U.S. government special publication | August 2020 | 2026-07-10 | Identity, resource access, policy enforcement, continuous evaluation, zero trust vocabulary | Medium-high; exact architecture decisions need task-specific context |
| OWASP ASVS (`https://owasp.org/www-project-application-security-verification-standard/`) | OWASP verification standard | Latest stable 5.0.0 | 2026-07-10 | Application security verification requirements and assurance vocabulary | High for app-security verification; not a CI/CD standard |
| OWASP Top 10 2025 (`https://owasp.org/Top10/2025/`) | OWASP awareness project | 2025 release | 2026-07-10 | Broad web-application security risk awareness: access control, misconfiguration, supply chain, crypto, injection, insecure design, auth, integrity, logging/alerting, exceptional conditions | High for risk awareness; not a complete verification checklist |
| OWASP API Security Top 10 2023 (`https://owasp.org/API-Security/editions/2023/en/0x11-t10/`) | OWASP API security awareness project | 2023 release | 2026-07-10 | API-specific authorization, authentication, resource consumption, business-flow, SSRF, misconfiguration, inventory, and third-party API risks | High for API risk prompts; not proof that a specific API is vulnerable |
| OWASP Cheat Sheet Series (`https://cheatsheetseries.owasp.org/`) | OWASP practitioner guidance | Maintained web project | 2026-07-10 | Defensive implementation and review guidance across auth, access control, input validation, logging, secrets, threat modeling, abuse cases, and related topics | Medium-high; individual cheat sheets should be checked when used |
| MITRE ATT&CK (`https://attack.mitre.org/`, `https://attack.mitre.org/resources/updates/`) | Maintained adversary behavior knowledge base | v19, April 2026 current version | 2026-07-10 | Tactics, techniques, mitigations, detections, data components, threat-model vocabulary | High for adversary behavior categories; do not reproduce operational attack steps |
| MITRE CWE (`https://cwe.mitre.org/about/index.html`, `https://cwe.mitre.org/data/index.html`) | Maintained weakness taxonomy | CWE List Version 4.20 | 2026-07-10 | Common software/hardware weaknesses, root-cause vocabulary, Top-N mappings | High for weakness vocabulary; exact weakness applicability requires task evidence |
| CIS Critical Security Controls (`https://www.cisecurity.org/controls/v8`) | CIS prioritized safeguards | v8 and v8.1 download page current | 2026-07-10 | Prioritized safeguards, offense-informed defense, focus/feasibility/measurability principles | High for defensive safeguard framing; detailed safeguard text requires source inspection |
| ISO/IEC 27001:2022 (`https://www.iso.org/standard/27001`) | International standard landing page | Edition 3, 2022-10; one amendment noted | 2026-07-10 | Information security management system, risk-aware organizational security framing | Medium; public page only, full standard is paywalled |
| Microsoft SDL (`https://www.microsoft.com/en-us/securityengineering/sdl/`) | Vendor secure development lifecycle guidance | Current Microsoft page | 2026-07-10 | Secure development lifecycle integration, broad software/platform applicability | Medium-high; Microsoft practice set should be adapted, not mandated |
| Microsoft STRIDE Threat Modeling Tool threats (`https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats`) | Vendor practitioner guidance | Last updated 2022-08-25 | 2026-07-10 | STRIDE threat categories: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege | Medium-high for threat-modeling vocabulary; Microsoft-specific tooling context |

## What The Sources Agree On

### Cybersecurity Is Risk Management Under Uncertainty

NIST CSF, RMF, SP 800-30, and ISO/IEC 27001 all frame cybersecurity around
risk rather than absolute safety. A useful cybersecurity answer should name
the protected asset, plausible threat, relevant weakness or exposure,
potential impact, existing or proposed controls, evidence quality, and
residual risk.

Implication for the pack: avoid "secure/insecure" verdicts without context.
Ask what the concern really is, what could go wrong, how likely or impactful it
is with available evidence, and what risk remains.

### Controls Need Context, Assurance, And Evidence

NIST SP 800-53 provides a broad control catalog and explicitly connects
controls to functionality and assurance. CIS Controls emphasize prioritized,
feasible, measurable safeguards informed by attacker behavior. OWASP ASVS
provides application-security verification requirements and confidence
language.

Implication for the pack: control selection should be proportional and
evidence-backed. A control name is not proof of effectiveness; review should
ask whether it exists, is configured correctly, covers the right boundary, and
has evidence.

### Assets, Actors, Trust Boundaries, And Privilege Shape Security Questions

NIST systems security engineering, STRIDE, OWASP API guidance, and zero-trust
guidance all depend on knowing who or what can access which resource under
which assumptions. API risks repeatedly show that object, function, property,
and business-flow authorization failures appear when identity and authorization
boundaries are underspecified.

Implication for the pack: before recommending controls, identify assets,
actors, data, identities, privileges, interfaces, trust boundaries, and
authorization decision points.

### Threat Modeling Turns Vague Security Concern Into Reviewable Questions

Microsoft STRIDE provides a simple threat vocabulary. MITRE ATT&CK provides a
rich adversary tactic/technique vocabulary based on observed behavior. NIST
SP 800-160 supports secure systems engineering and trustworthiness through the
system lifecycle.

Implication for the pack: threat modeling in AI Editorial Office should stay
defensive and question-oriented: what could be spoofed, tampered with, denied,
exposed, overused, repudiated, or privileged; what adversary behavior category
is relevant; what evidence would confirm or weaken the concern?

### Weaknesses Are Root Causes, Vulnerabilities Are Instance-Specific

MITRE CWE defines common weakness types and distinguishes weaknesses from
specific vulnerabilities. OWASP Top 10 and API Top 10 group common risk areas
that often map to CWE weaknesses, but a real finding still needs task-specific
evidence.

Implication for the pack: use weakness classes to organize reasoning, not to
assert exploitability. Do not claim a vulnerability exists without inspecting
the affected artifact, design, configuration, or behavior.

### Secure Design Is Not The Same As Security Tooling

NIST SP 800-160, SSDF, Microsoft SDL, and OWASP Top 10 all support moving
security earlier into requirements, design, implementation, verification, and
maintenance. Insecure design appears as a web-application risk category in
OWASP Top 10 2025, but the underlying lesson is broader: controls cannot
always compensate for weak requirements, wrong trust boundaries, or unsafe
defaults.

Implication for the pack: secure design questions should precede tooling and
scanner discussions when architecture, requirements, data flow, or abuse case
shape the risk.

### Detection, Response, Recovery, And Resilience Matter, But Ownership Stays Elsewhere

NIST CSF includes detect, respond, and recover functions, and NIST SP 800-160
Vol. 2 emphasizes cyber resiliency. This release should include high-level
review prompts about observability, detection, fallback, recovery, and
residual risk.

Implication for the pack: include defensive resilience context, but do not
create an incident-response workflow or operational approval path.

## Concepts To Carry Into The Pack

| Concept | Source support | Pack consequence |
| --- | --- | --- |
| Asset | NIST CSF/RMF, SP 800-53, ISO/IEC 27001 | Identify what needs protection before selecting controls |
| Threat | NIST SP 800-30, STRIDE, MITRE ATT&CK | Name plausible adverse action or event without operationalizing it |
| Vulnerability | NIST risk sources, CWE | Treat as an instance-specific weakness exposure requiring evidence |
| Weakness | MITRE CWE, OWASP | Use as root-cause vocabulary, not exploitability proof |
| Control | NIST SP 800-53, CIS Controls, OWASP ASVS | Treat as safeguard or requirement needing scope and evidence |
| Assurance | NIST SP 800-53, SP 800-160, ASVS | Ask what evidence supports confidence in the control or design |
| Trust boundary | STRIDE, SP 800-160, API guidance | Clarify where assumptions, privilege, and validation change |
| Abuse case | OWASP cheat sheets, threat modeling | Ask how legitimate features could be misused defensively |
| Least privilege | NIST, CIS, zero trust, OWASP | Scope identities, permissions, and authority to need |
| Defense in depth | NIST/CIS/secure design sources | Avoid single-control assumptions when impact is high |
| Secure by default | secure design and SDL sources | Unsafe defaults require explicit justification and mitigation |
| Residual risk | NIST SP 800-30/RMF | Name what remains after controls and evidence |
| Detection and recovery | NIST CSF, SP 800-160 Vol. 2 | Include observability and resilience prompts without owning incident response |

## First Cybersecurity Questions

- What security concern is this really about: confidentiality, integrity,
  availability, privacy, misuse, fraud, safety, compliance, trust, resilience,
  or reputation?
- What assets, data, identities, interfaces, dependencies, and privileges are
  involved?
- Who are the actors: legitimate user, administrator, service, third party,
  anonymous user, insider, compromised account, automated client, or external
  adversary?
- Where are the trust boundaries and authorization decision points?
- What could be spoofed, tampered with, disclosed, denied, overused, or
  escalated?
- Which weakness class or OWASP risk category is relevant, and what evidence
  supports that mapping?
- Which control families or safeguards should be considered, and which are
  outside the task scope?
- What evidence would raise confidence that the design, implementation, or
  recommendation is safe enough for its context?
- What assumptions would make the recommendation wrong?
- What residual risk remains, and who must own it outside the pack?

## Pack Boundary Implications

In scope:

- security-sensitive analysis and defensive recommendations;
- threat understanding, abuse cases, and weakness-class interpretation;
- control-family and mitigation-context prompts;
- secure design and assurance questions;
- authentication, authorization, access control, input handling,
  configuration, cryptography, logging, monitoring, data handling, API
  security, dependency risk, resilience, and residual-risk framing;
- source-backed review questions for Engineering Review, Architecture Review,
  Professional Analysis, and Professional Communication.

Out of scope:

- exploit development, penetration testing procedures, weaponization, bypass
  instructions, malware, credential theft, stealth, persistence, unauthorized
  access, or adversary operational guidance;
- incident response operations and approval workflow;
- compliance/legal attestation;
- policy ownership or organizational security governance;
- exact vendor or platform configuration without task-specific sources;
- secure delivery, CI/CD, deployment automation, and artifact publishing when
  the DevSecOps Domain Pack is the better primary context.

Adjacent-domain notes:

- Engineering Review owns implementation/change safety. Cybersecurity pack can
  enrich its security and abuse lens but cannot decide its outcome.
- Architecture Review owns design-fitness review. Cybersecurity pack can
  supply threats, trust-boundary, and secure-design context.
- DevSecOps Domain Pack owns secure delivery, CI/CD, automation,
  supply-chain, deployment, and operational-security assumptions.
- Software Architecture Domain Pack owns software architecture domain context.
- Professional Analysis and Professional Communication may use cybersecurity
  context for risk synthesis and reader transfer, but remain separate
  capabilities.

## Safety Findings

The pack can include:

- defensive categories;
- review questions;
- risk and evidence framing;
- secure design prompts;
- control-family examples;
- source-backed assurance expectations;
- refusal/constrain triggers for unsafe requests.

The pack must exclude:

- step-by-step attack procedures;
- exploit code, payload construction, bypass techniques, or intrusion paths;
- malware, persistence, stealth, exfiltration, or credential-theft guidance;
- instructions that help unauthorized access;
- operational incident-response instructions that create a new workflow.

## Research Sufficiency

Sufficiency judgment: enough authoritative evidence exists to create a
release-candidate Cybersecurity Domain Knowledge Pack.

Confidence:

- High for durable risk, control, threat, weakness, secure-design, and
  assurance framing.
- Medium-high for application/API security categories and STRIDE because exact
  applicability depends on task-specific design and evidence.
- Medium for ISO/IEC 27001 details because only the public landing page was
  used.
- Limited for exact current vendor/platform behavior; require task-specific
  source refresh.

No blocking research gaps remain for release-candidate production.

