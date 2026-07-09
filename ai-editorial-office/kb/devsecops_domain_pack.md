# DevSecOps Domain Knowledge Pack

Status: release candidate

Pack name: DevSecOps Domain Knowledge Pack

Domain: DevSecOps, secure software delivery, CI/CD, automation,
configuration, supply-chain risk, deployment boundaries, validation evidence,
and operational-security assumptions.

Maintainer context: AI Editorial Office canonical KB, created for release
`S4.R3`.

Created: 2026-07-10

Last reviewed: 2026-07-10

Stale if:

- NIST SSDF, OWASP SAMM, OWASP ASVS, SLSA, OpenSSF Scorecard, GitHub Actions,
  GitLab CI/CD, Kubernetes, Docker, CIS Docker/Kubernetes Benchmarks, NTIA
  SBOM resources, Microsoft SDL, or Google SRE production guidance changes
  materially;
- repeated Engineering Review, Architecture Review, or release tasks expose
  missing DevSecOps terms, risks, activation boundaries, or review questions;
- a future accepted Domain Knowledge Pack Standard adds required sections;
- this pack causes confusion with a role, capability, pipeline, review gate,
  policy owner, security owner, or mandatory artifact set;
- the pack is not reviewed for 12 months after acceptance.

## Purpose

This pack helps AI Editorial Office apply source-backed DevSecOps context when
secure delivery, CI/CD, automation, configuration, supply-chain risk,
deployment boundaries, validation evidence, or operational-security
assumptions materially affect a task.

It helps existing roles and capabilities reason about:

- whether a delivery flow is safe enough to accept or recommend;
- which secure development controls matter for the task;
- which CI/CD permissions, triggers, secrets, artifacts, caches, or runners are
  risky;
- which supply-chain assumptions are visible or missing;
- which dependency, package, image, action, tool, or artifact trust questions
  should be asked;
- which configuration, environment, container, runtime, or infrastructure
  risks should be reviewed;
- what validation evidence is needed before accepting a security-sensitive
  delivery change;
- which operational-security assumptions should be named.

This pack is not a capability, role, pipeline, framework, lifecycle stage,
review gate, governance layer, policy owner, security owner, client profile,
task status model, or mandatory ordinary task artifact.

## Intended Use

Use this pack as domain context for DevSecOps-sensitive work. It may support:

- Chief Editor routing and activation decisions;
- Research Agent source framing;
- Writer Agent drafting of delivery, automation, configuration, supply-chain,
  deployment, or validation guidance;
- Review Agent challenge inside the existing review gate;
- Final Editor preservation of reviewed DevSecOps caveats;
- Engineering Review when secure delivery context improves implementation or
  change-safety judgment;
- Architecture Review when deployment, runtime, or operational boundaries have
  architectural significance.

The pack does not decide review outcomes, release acceptance, deployment
approval, task status, incident response, compliance posture, or final
governance.

## When To Activate

Activate this pack only when DevSecOps context materially changes evidence
depth, terminology, risk handling, review focus, or output quality.

Typical activation triggers:

- the task evaluates or changes a CI/CD workflow, pipeline, release job, build
  job, deployment job, or automation script;
- a workflow token, job token, service account, deployment credential, cloud
  credential, signing key, package registry token, or secret is involved;
- workflow triggers, forked code, untrusted pull requests, protected branches,
  protected tags, environment reviewers, or deployment approvals affect risk;
- build artifacts, release artifacts, package publishing, container image
  publishing, SBOMs, provenance, attestations, or signatures are material;
- dependency, package, action, plugin, image, toolchain, or binary artifact
  trust is material;
- Docker, Kubernetes, runner, local deployment, service file, runtime profile,
  RBAC, namespace, or infrastructure configuration changes affect deployment or
  operational security;
- a change modifies security-sensitive delivery gates, scanning, build
  validation, artifact verification, deployment promotion, or environment
  separation;
- a review needs evidence that a delivery change has been validated
  proportionally to its blast radius;
- Engineering Review identifies secure delivery as a material implementation
  or change-safety lens.

Record activation in the smallest existing task artifact that keeps the next
role safe:

- `orchestration_plan.md`;
- `task-manifest.md`;
- `research.md`;
- writer notes;
- `review.md`;
- `final_decision.md`.

Activation note should name:

- active pack: `DevSecOps Domain Knowledge Pack`;
- activation reason;
- relevant sections or sources;
- evidence confidence;
- boundary limits and stale-if triggers;
- stop conditions.

## When Not To Activate

Do not activate this pack when:

- "security", "DevOps", "automation", "deployment", or "pipeline" is only an
  incidental term;
- the task is ordinary writing, copyediting, formatting, summarization, or
  navigation with no secure delivery claim;
- the work is a small local code change with no CI/CD, automation,
  configuration, dependency, credential, artifact, runtime, deployment,
  validation, or operational-security impact;
- Engineering Review can handle code/config/change safety without additional
  DevSecOps domain context;
- the task is mainly application vulnerability analysis, abuse-case modeling,
  identity architecture, cryptography, incident response, penetration testing,
  malware analysis, or broad cybersecurity control selection;
- the task is mainly software architecture design fitness and delivery/runtime
  security is not material;
- the task asks for legal, regulatory, or compliance attestation without
  task-specific authoritative sources;
- exact platform behavior, feature tier, current syntax, or provider-specific
  semantics must be verified and this pack has not been refreshed against the
  relevant source;
- activation would create a new role, capability, workflow, review gate,
  policy, approval requirement, or mandatory artifact.

Do not activate merely because a source mentions CI, CD, DevOps, container,
Kubernetes, Docker, SBOM, SLSA, scanner, security, secrets, cloud, or
production.

## Questions This Pack Can Answer

This pack can help answer:

- Is this delivery flow safe enough to recommend, merge, or accept for this
  task context?
- What can this automation read, write, deploy, publish, delete, or expose?
- Which identities, tokens, service accounts, keys, and credentials execute
  the workflow, and what is their effective scope?
- Can untrusted code, metadata, artifacts, caches, dependencies, or inputs
  influence a privileged context?
- Which secrets are available, when are they injected, and how would exposure
  be detected and remediated?
- Are CI/CD permissions, default tokens, job tokens, runners, triggers, and
  environment approvals scoped to least privilege?
- What third-party actions, packages, images, tools, plugins, scripts, or
  binary artifacts are trusted, pinned, updated, and reviewed?
- What artifact is produced, how is it identified, and can provenance,
  attestation, or signing connect it to source and build process?
- Which dependency or supply-chain risk is visible, and which risk requires
  task-specific research?
- Which configuration or environment boundary separates local development,
  test, staging, production, release publishing, and privileged deployment?
- Which Docker, Kubernetes, runner, runtime, RBAC, or service-account
  assumptions affect secure deployment?
- Which validation evidence is needed before accepting a security-sensitive
  delivery change?
- Which operational assumptions, monitoring, rollback, patching, ownership, or
  incident-response dependencies should be named?
- What DevSecOps questions should be asked first?

This pack cannot answer:

- whether Project Lead should accept a release;
- whether Engineering Review passes or fails;
- which exact cloud, CI/CD, or registry feature must be configured without
  source-specific research;
- whether a vulnerability is exploitable without task-specific security
  evidence;
- whether a compliance, legal, or audit claim is acceptable;
- whether a scanner, SBOM, SLSA level, Scorecard score, signature, or
  attestation proves safety by itself.

## Domain Boundary

In scope:

- secure SDLC and secure delivery context;
- CI/CD workflow and pipeline security;
- automation permissions, tokens, triggers, runners, artifacts, caches, logs,
  and deployment jobs;
- dependency, package, third-party action, plugin, container image, toolchain,
  SBOM, provenance, attestation, signature, and artifact risks;
- secrets and credentials used by delivery, deployment, build, runtime, and
  infrastructure paths;
- configuration and environment safety for local, test, staging, production,
  and release environments;
- Docker, Kubernetes, runner, service-account, runtime, and infrastructure
  considerations when tied to delivery or deployment;
- validation evidence and operational-security assumptions.

Out of scope:

- broad cybersecurity strategy, threat modeling, and control selection as a
  full domain;
- incident response ownership;
- vulnerability triage as a standalone security domain;
- cryptographic design, identity architecture, IAM strategy, or zero-trust
  architecture beyond delivery-specific context;
- compliance/legal attestation;
- cloud platform architecture selection;
- software architecture design fitness except where delivery/runtime
  boundaries overlap;
- implementation code review beyond secure delivery context.

Adjacent domains:

- Engineering Review: use this pack for DevSecOps context; implementation and
  change-safety review remains owned by `kb/engineering_review.md`.
- Software Architecture Domain Pack: use for architectural structure,
  boundaries, quality attributes, or design tradeoffs beyond delivery/security
  automation.
- Future Cybersecurity Domain Pack: use or research separately for threats,
  controls, vulnerabilities, abuse cases, cryptography, identity, or incident
  risk outside delivery context.
- Knowledge Evolution: use for stale-source updates, pack corrections,
  retirement, and canon-update candidates.

Overloaded terms:

- `DevSecOps`: in this pack, secure delivery context integrated into
  development, automation, deployment, validation, and operations; not a team
  name, role, maturity score, tool bundle, or governance owner.
- `pipeline`: can mean CI/CD workflow, release process, editorial pipeline, or
  data pipeline. Clarify before applying guidance.
- `workflow`: can mean GitHub Actions workflow, GitLab pipeline job flow, human
  work process, or automation script. Clarify execution and authority.
- `runner`: the execution environment for CI/CD jobs; trust depends on hosting,
  isolation, reuse, network, secret access, and cleanup.
- `token`: can be a repository token, workflow token, job token, package token,
  OIDC token, service-account token, PAT, or cloud credential. Scope and
  lifetime matter.
- `secret`: any sensitive credential or value whose exposure has security
  impact; masking is not equivalent to safety.
- `artifact`: any build output, package, image, report, binary, archive,
  attestation, SBOM, log, or evidence object.
- `environment`: can mean shell environment, CI environment, deployment
  environment, Kubernetes namespace, runtime environment, or editorial task
  environment.
- `container`: in this pack, usually Docker/OCI/container runtime or Kubernetes
  workload context; not C4 application-container notation.
- `gate`: a validation or approval point inside a delivery system; not an AI
  Editorial Office review gate unless the editorial canon says so.

## Evidence And Confidence Rules

Claims this pack supports with high confidence:

- secure development should be integrated into the SDLC and handled
  risk-proportionally;
- CI/CD and deployment automation are security-sensitive because they execute
  code with credentials, permissions, artifact publication paths, and
  deployment authority;
- least privilege applies to workflow tokens, job tokens, service accounts,
  runners, environments, and secrets;
- untrusted code, pull requests, metadata, artifacts, caches, and inputs must
  be separated from privileged execution contexts;
- supply-chain risk spans source, dependencies, build, builder, artifact,
  publication, distribution, verification, and runtime consumption;
- secrets require minimization, scoping, secure injection, masking caveats,
  rotation paths, and exposure response;
- container/runtime/infrastructure guidance must be platform-specific and
  evidence-backed;
- validation evidence should be proportional to the change's blast radius.

Claims this pack cannot support by itself:

- exact current behavior of a CI/CD provider, cloud provider, registry,
  Kubernetes distribution, Docker version, runner feature, or secret manager;
- compliance or audit conclusions;
- exploitability or severity of a vulnerability;
- a universal required SLSA level, Scorecard score, SBOM format, scan tool,
  CIS setting, or approval gate;
- a final Engineering Review or release acceptance verdict.

Evidence expectations:

- Use this pack for durable vocabulary, first questions, risk prompts, and
  evidence categories.
- Use task-specific primary sources for exact provider behavior, syntax,
  versioned controls, cloud configuration, or feature-tier claims.
- Treat scanner output, SBOMs, Scorecard checks, signatures, attestations, and
  provenance as evidence signals that need context, not as standalone proof of
  safety.
- Preserve source date/version and stale-if notes for volatile claims.
- Escalate to research when source behavior, platform semantics, regulatory
  duties, or security impact is uncertain.

## Domain Vocabulary

| Term | Meaning in this pack | Notes |
| --- | --- | --- |
| Secure SDLC | A software-development lifecycle with security activities integrated into planning, design, implementation, verification, release, and response. | NIST SSDF, OWASP SAMM, and Microsoft SDL inform this framing. |
| SSDF | NIST Secure Software Development Framework, a high-level secure development practice set. | Use for vocabulary and lifecycle context, not as a checklist mandate. |
| DevSecOps | Secure delivery practice across development, security, automation, deployment, validation, and operations. | Not a separate AI Editorial Office role or gate. |
| CI/CD workflow | Executable automation that builds, tests, validates, packages, publishes, or deploys software. | Treat as privileged code when it has write, secret, artifact, or deploy authority. |
| Workflow trigger | Event or condition that starts automation. | Risk depends on trust of actor, input, ref, branch, tag, fork, and event type. |
| Privileged context | Execution context with sensitive secrets, write permissions, artifact publication rights, deployment ability, or production access. | Keep untrusted inputs away from it unless safely mediated. |
| Workflow token | Token automatically or explicitly available to a CI/CD job. | Examples include GitHub `GITHUB_TOKEN` and GitLab CI job token; exact behavior is platform-specific. |
| Runner | Environment where CI/CD jobs execute. | Trust depends on isolation, persistence, reuse, host access, network, and credential exposure. |
| Secret | Sensitive value such as credential, key, token, password, certificate, signing material, or connection string. | Masking and base64 encoding are not equivalent to secrecy. |
| OIDC | Federated identity mechanism often used to request short-lived cloud credentials from CI/CD. | Preferable to long-lived static secrets when correctly scoped. |
| Protected branch/tag | Source ref with restrictions on who can modify it or which checks/reviews are required. | Supports source integrity and release provenance assumptions. |
| Protected environment | Deployment environment with access controls, approvals, variables/secrets, or reviewers. | Platform-specific; verify exact behavior. |
| Artifact | Output from build or delivery automation, including packages, images, binaries, logs, reports, SBOMs, or attestations. | Artifacts can carry trust and leakage risk. |
| Provenance | Evidence about where and how an artifact was built. | SLSA provides supply-chain vocabulary for provenance and verification. |
| Attestation | Authenticated statement about an artifact, build, source, or process. | Useful only if the verifier trusts issuer, identity, scope, and predicate. |
| SBOM | Software Bill of Materials: component inventory for software. | Transparency evidence, not a safety verdict. |
| Supply-chain risk | Risk that source, dependencies, build systems, tools, artifacts, publication, distribution, or verification are compromised or misleading. | Consider both direct and transitive trust. |
| Dependency risk | Risk from libraries, packages, modules, images, actions, plugins, or tools used to build or run software. | Includes provenance, maintainer, update, license, vulnerability, and behavior risks. |
| Base image | Container image used as the starting point for another image. | Trust, size, update cadence, pinning, and rebuild behavior matter. |
| Runtime profile | Security posture applied at runtime, such as Kubernetes Pod Security profile or container isolation settings. | Platform/version-specific. |
| Least privilege | Grant only the permissions needed for the task and duration. | Applies to humans, automation, service accounts, runners, secrets, and jobs. |
| Blast radius | Maximum plausible harm if the change or credential is misused. | Use to scale review and validation evidence. |
| Rollback | Controlled way to revert or mitigate a deployment or release. | Security-sensitive changes need operational fallback assumptions. |

## DevSecOps Principles

These principles are guidance, not policy. Use only when DevSecOps context is
material and evidence supports the claim.

### Secure Delivery Is A System

Source basis: NIST SSDF, OWASP SAMM, Microsoft SDL, SLSA.

Do not evaluate a scanner, workflow step, or approval in isolation. Ask how
source, dependency, build, validation, artifact, deployment, runtime, response,
and operations fit together.

### Treat CI/CD As Privileged Code

Source basis: GitHub Actions secure-use guidance, GitLab CI/CD security docs,
OpenSSF Scorecard.

Workflow files and automation scripts can expose secrets, write repositories,
publish artifacts, mutate environments, and deploy production changes. Review
them like code that carries authority.

### Least Privilege Applies To Automation

Source basis: GitHub token guidance, GitLab job-token guidance, Kubernetes RBAC
guidance.

Default tokens, job tokens, service accounts, repository permissions, runner
access, package permissions, cloud credentials, environment permissions, and
secret access should be scoped to the work and duration required.

### Separate Untrusted Inputs From Privileged Contexts

Source basis: GitHub Actions security guidance, GitLab forked merge-request
warnings, SLSA threat model.

Untrusted pull requests, forks, event payloads, cache contents, artifacts,
dependency scripts, build metadata, and generated files should not directly
control privileged commands, release publishing, deployment, or secret-bearing
jobs.

### Minimize Long-Lived Secrets

Source basis: GitHub OIDC and secret guidance, GitLab external secrets and ID
tokens, Docker build-secret guidance, Kubernetes Secret guidance.

Prefer short-lived, scoped, auditable credentials where available. If static
secrets are required, record scope, storage, injection point, masking limits,
rotation, deletion, and exposure response.

### Visibility Is Not A Verdict

Source basis: NTIA SBOM resources, SLSA, OpenSSF Scorecard, OWASP ASVS.

SBOMs, Scorecard results, attestations, provenance, signatures, scan output,
and test reports improve visibility. They do not prove safety unless their
scope, freshness, trust model, and verification path match the task.

### Validate Proportionally To Blast Radius

Source basis: OWASP SAMM, OWASP ASVS, NIST SSDF, Google SRE production
readiness guidance.

More authority, exposure, production impact, or irreversibility requires
stronger evidence: inspected config, relevant tests, least-privilege proof,
secret-handling evidence, artifact verification, rollback, monitoring, and
residual-risk notes.

## Secure SDLC / SSDF Concepts

Use secure SDLC concepts to frame where evidence should appear in delivery
work. Do not force every task through a maturity assessment.

NIST SSDF concept groups:

- prepare the organization: define roles, practices, toolchain expectations,
  criteria, and security responsibilities;
- protect the software: protect source, code, build outputs, release artifacts,
  credentials, and software integrity evidence;
- produce well-secured software: integrate secure design, secure coding,
  review, testing, dependency handling, and vulnerability reduction into the
  build path;
- respond to vulnerabilities: identify, triage, remediate, communicate, and
  learn from vulnerabilities after release.

OWASP SAMM framing:

- Governance, Design, Implementation, Verification, and Operations are distinct
  but connected business functions;
- Implementation includes secure build, secure deployment, and defect
  management;
- Operations includes incident management, environment management, and
  operational management.

Practical use:

- Ask which lifecycle surface the task changes.
- Ask whether security expectations appear before, during, and after build and
  deployment.
- Ask whether response and operational assumptions are visible when production
  or release impact exists.
- Avoid turning SSDF or SAMM into a mandatory checklist unless the user
  specifically requests that standard.

## CI/CD Security

Start CI/CD review with authority:

- What starts the workflow?
- Who or what can influence the input?
- Which repository, branch, tag, environment, package, registry, or deployment
  target can the job affect?
- Which token or credential is available?
- What can the job read, write, publish, or deploy?
- Is the runner trusted for the secrets and permissions it receives?

Common CI/CD review surfaces:

- default token permissions and per-job permissions;
- privileged triggers such as protected branches, tags, scheduled workflows,
  manually dispatched workflows, `pull_request_target`, `workflow_run`, merge
  request pipelines, release events, or external webhooks;
- fork and pull-request behavior;
- third-party actions, includes, templates, plugins, and reusable workflows;
- pinning of actions, images, packages, tools, and installers;
- branch/tag protection, CODEOWNERS, required reviews, and workflow-file review
  ownership;
- runner isolation, reuse, privileged container mode, host mounts, daemon or
  socket access, network access, and cleanup;
- logs, artifacts, caches, summaries, annotations, and test reports that may
  expose secrets or influence later jobs;
- environment reviewers, protected variables, deployment approvals, and
  promotion rules;
- package publishing, image publishing, release creation, signing, and
  provenance/attestation publication.

GitHub-specific caution:

- Set default `GITHUB_TOKEN` permissions to the minimum needed and raise
  permissions explicitly per job when required.
- Treat `pull_request_target` and `workflow_run` patterns carefully when
  untrusted code can be checked out or can affect a privileged job.
- Prefer pinning third-party actions by full-length commit SHA for sensitive
  workflows.
- Use OIDC when it can replace long-lived cloud credentials and the trust
  policy is tightly scoped.
- Use CODEOWNERS or equivalent review for workflow files where changes affect
  secrets, write permissions, or deployment.

GitLab-specific caution:

- Treat `.gitlab-ci.yml` as executable security-sensitive code.
- Review merge-request pipeline behavior from forks before exposing protected
  variables, job tokens, or deployment credentials.
- Scope job-token access and project allowlists.
- Treat runner security as part of secret and token safety; shared or reused
  runners with privileged Docker or shell executors can widen exposure.
- Prefer external secret providers or ID-token based retrieval where available
  and correctly scoped.

## Supply Chain Security

Supply-chain review should connect source, dependency, build, artifact,
publication, distribution, verification, and use.

Ask:

- Which source ref, commit, branch, or tag is trusted?
- Who can change that source or release ref?
- Which dependencies, packages, actions, plugins, images, tools, and
  installers participate directly or transitively?
- Is the build process reproducible, isolated, authenticated, or otherwise
  protected for the task's risk?
- Which builder produced the artifact, and is builder identity meaningful?
- Is provenance produced, distributed, and verified by consumers?
- Are signatures or attestations tied to the expected identity, source, build
  process, and artifact digest?
- Is an SBOM available when component transparency matters?
- Can consumers verify what they are installing, deploying, or running?
- What happens if a dependency maintainer, registry, action, image, package,
  or build runner is compromised?

SLSA use:

- Use SLSA v1.2 for source/build/provenance vocabulary and supply-chain threat
  framing.
- Do not claim a SLSA level unless the task-specific evidence supports the
  exact requirements.
- Treat SLSA provenance as a verification input, not a substitute for review of
  source, dependencies, runtime configuration, or deployment authority.

OpenSSF Scorecard use:

- Use checks such as branch protection, code review, CI tests, dangerous
  workflows, binary artifacts, token permissions, pinned dependencies, and
  maintained status as signals.
- Do not treat a Scorecard score as a pass/fail verdict for AI Editorial
  Office review.

SBOM use:

- Use SBOMs to understand component inventory, not to prove that the software
  is vulnerability-free or safe.
- Ask whether the SBOM covers the relevant artifact, build, dependency scope,
  and version.
- Ask whether the consumer has a process to use SBOM information.

## Secrets And Credentials

Secret safety depends on necessity, scope, lifetime, storage, injection path,
runtime exposure, logs, transformations, runner trust, and rotation.

Ask:

- Is the secret necessary for this job or environment?
- Where is it stored?
- Who can read, edit, rotate, delete, or trigger use of it?
- When is it injected and into which process?
- Can untrusted code, metadata, dependency scripts, artifacts, caches, or logs
  access or influence it?
- Is it scoped to least privilege and shortest practical lifetime?
- Is OIDC or an external secret provider available instead of a static secret?
- Does masking cover exact values only, and what happens after transformation,
  encoding, truncation, or concatenation?
- Is the secret copied into images, artifacts, caches, logs, summaries, shell
  history, config files, or generated manifests?
- Is rotation and revocation documented after suspected exposure?

Platform-specific reminders:

- GitHub and GitLab secret masking is useful but not a guarantee against
  malicious workflow or script behavior.
- GitLab variables defined in `.gitlab-ci.yml` are visible in repository
  history and should not hold sensitive values.
- Docker build arguments and environment variables are inappropriate for build
  secrets because they can persist in image history or final images; use build
  secret mounts or SSH mounts where available.
- Kubernetes Secrets are not encrypted by base64 encoding and must be protected
  through access control, encryption-at-rest where configured, namespace
  boundaries, and careful manifest handling.

## Configuration And Environment Safety

Configuration and environment review should expose where a change runs, what it
can reach, and which defaults apply.

Ask:

- Which environment is affected: local, CI, preview, test, staging,
  production, package registry, release registry, Kubernetes namespace, cloud
  account, or customer-facing system?
- Which configuration source wins if defaults, env vars, files, CLI flags,
  secrets, generated manifests, and deployment variables conflict?
- Are production credentials or resources available in non-production jobs?
- Are protected branches, tags, variables, environments, namespaces, or
  deployment targets enforcing the intended boundary?
- Does the change relax permissions, approvals, branch protection, environment
  protection, runner isolation, network access, or runtime isolation?
- Can local deployment scripts affect production or shared resources by
  default?
- Does the script or config require explicit target selection, dry-run,
  confirmation, rollback, or validation for high-impact operations?
- Are logs, debug flags, error reporting, or diagnostics safe for secrets and
  personal/sensitive data?
- Is configuration drift possible between what was reviewed and what is
  deployed?

Do not assume that staging and production are equivalent. Do not assume that a
local script is low risk if it carries credentials, writes infrastructure, or
publishes artifacts.

## Dependency And Tooling Risk

Dependency review should examine both security findings and trust chain.

Ask:

- What changed: direct dependency, transitive dependency, action, plugin,
  image, base image, build tool, installer, package manager, lockfile,
  checksum, or generated artifact?
- Is the update pinned or floating?
- Does the lockfile or digest match the reviewed dependency?
- Who maintains the dependency and what is the release/channel trust model?
- Was the update produced by an authenticated and reviewed source?
- Are install scripts, postinstall hooks, generated code, native extensions,
  or binary downloads introduced?
- Does the dependency gain network, file-system, build, deploy, or credential
  access?
- Are vulnerability findings, changelog, diff, tests, and compatibility
  evidence relevant to the risk?
- Does the tooling run in a privileged CI/CD or release context?

High-risk signals:

- unpinned third-party actions or images in release workflows;
- new binary artifacts committed to source without provenance;
- new package registry, installer curl script, or opaque download path;
- dependency update that changes build or deploy tooling;
- bypassed lockfile, missing checksum, or changed registry source;
- newly privileged dependency script or plugin;
- broad ignore/suppression of dependency or container findings.

## Container / Runtime / Infrastructure Considerations

Container and runtime guidance must remain platform-specific and evidence
backed. Use this pack for questions, not universal hardening mandates.

Docker/build questions:

- Is the base image trusted, minimal enough, current, and pinned or otherwise
  traceable?
- Are images rebuilt regularly to pick up upstream fixes?
- Does the Dockerfile avoid unnecessary packages, tools, credentials, and
  build leftovers?
- Are multi-stage builds used when they reduce runtime footprint or secret
  exposure?
- Are secrets passed through BuildKit secret mounts or SSH mounts rather than
  build args or environment variables?
- Are image tests and relevant scans run in CI before publish or deploy?
- Is the Docker daemon socket protected from untrusted jobs or containers?

Kubernetes/runtime questions:

- Which namespace, service account, RBAC role, and admission policy apply?
- Does the workload need privileged mode, host namespaces, host path mounts,
  broad capabilities, root user, or unrestricted networking?
- Which Kubernetes Pod Security profile or equivalent policy is intended:
  Privileged, Baseline, or Restricted?
- Can the workload read Secrets it does not need?
- Are service-account tokens mounted only when needed?
- Are wildcard RBAC permissions, cluster-admin bindings, or system:masters-like
  access present?
- Are manifests, Helm charts, Kustomize overlays, and generated deployment
  output reviewed for the actual target environment?

CIS benchmark use:

- CIS Docker and Kubernetes Benchmarks are useful secure-configuration
  references for task-specific checks.
- Do not cite detailed CIS controls unless the relevant benchmark text has
  been inspected for the specific version and context.

## Validation And Evidence Expectations

Validation should match authority, exposure, and reversibility.

Useful evidence categories:

- inspected workflow, script, Dockerfile, manifest, dependency, or config diff;
- source-backed explanation of platform semantics when exact behavior matters;
- successful relevant tests, build checks, lint checks, policy checks, or scan
  results;
- token and permission evidence, including default and per-job scopes;
- secret inventory for the affected path and evidence that secrets are not
  logged, copied, cached, baked into images, or exposed to untrusted jobs;
- trigger and trust-boundary analysis for forks, pull requests, tags, branches,
  webhooks, scheduled jobs, manual dispatch, release jobs, and chained
  workflows;
- dependency provenance, lockfile, checksum, digest, changelog, advisory, or
  maintainer/release evidence;
- artifact identity, digest, signature, provenance, attestation, or SBOM when
  material;
- branch/tag/environment protection evidence for release or production paths;
- runner, container, namespace, service-account, RBAC, or runtime evidence when
  deployment context matters;
- rollback, monitoring, alerting, ownership, patching, incident-response, or
  operational-readiness evidence for production-impacting changes;
- explicit residual risk and unknowns.

Evidence should be stronger when the change:

- can deploy to production;
- can publish packages or images;
- can access secrets or cloud credentials;
- can alter release artifacts;
- can change workflow permissions or triggers;
- can affect shared infrastructure;
- can bypass review, validation, or environment protection;
- is hard to roll back.

Do not require all evidence categories for every task. Choose proportionally
and record why omitted evidence is acceptable.

## Operational Security Considerations

Secure delivery continues after merge.

Ask:

- Who owns the workflow, credential, deployment target, runtime, and rollback
  after the change lands?
- What monitoring or alerting would reveal failed deployment, credential
  misuse, artifact tampering, unexpected traffic, or runtime drift?
- What logs are available, and are they safe to retain?
- How are vulnerabilities, dependency updates, base image updates, and runtime
  patches handled after release?
- What incident-response or escalation path exists if the delivery path is
  abused?
- Can the system roll back, disable, rotate, revoke, or quarantine quickly?
- What SLO, reliability, or production-readiness assumption interacts with the
  security decision?
- Are operational runbooks, ownership, access, and emergency procedures
  adequate for the blast radius?

Use Google SRE production-readiness and SLO guidance for operational
assumption prompts. Do not use it as security-control authority.

## Review Questions

Review Agent may use these questions inside the existing review gate when this
pack is active:

- Was pack activation justified by material DevSecOps context?
- Did the artifact stay within DevSecOps context instead of creating policy,
  roles, gates, or mandatory artifacts?
- Does the task name the delivery surface being changed?
- Does it identify what automation can read, write, publish, deploy, delete,
  or expose?
- Are workflow triggers and trust boundaries clear?
- Are untrusted inputs separated from privileged contexts?
- Are workflow/job tokens, service accounts, and permissions least-privilege
  for the task?
- Are secrets minimized, scoped, injected safely, protected from logs/artifacts,
  and rotatable after exposure?
- Are third-party actions, packages, images, tools, and binary artifacts
  pinned, reviewed, or otherwise justified?
- Does supply-chain reasoning cover source, dependency, build, artifact,
  publication, distribution, and verification where material?
- Does the artifact treat SBOMs, Scorecard, SLSA, signatures, scans, and
  attestations as evidence signals rather than verdicts?
- Are configuration and environment boundaries explicit?
- Are container/runtime/RBAC/namespace/runner assumptions reviewed when
  relevant?
- Is validation evidence proportional to blast radius?
- Are residual risks, assumptions, unknowns, and stale-source limits visible?
- Did the pack support Engineering Review without replacing Engineering
  Review?

## Common Mistakes

- Treating DevSecOps as a new AI Editorial Office role or review gate.
- Treating a scanner, score, SBOM, SLSA label, signature, or attestation as
  automatic proof of safety.
- Reviewing application code but ignoring the workflow that builds, signs,
  publishes, or deploys it.
- Giving default workflow tokens broad write permission because it is
  convenient.
- Letting untrusted pull-request code run in a job that has secrets or
  deployment authority.
- Assuming masked secrets cannot be exfiltrated by malicious workflow code.
- Storing sensitive values in repository-visible CI variables, Docker build
  args, logs, artifacts, or generated manifests.
- Trusting self-hosted or reused runners without checking isolation, cleanup,
  privileged mode, and network reachability.
- Pinning source dependencies while leaving CI actions, images, or installers
  floating.
- Treating base images, action versions, or package sources as harmless
  implementation detail.
- Ignoring artifacts, caches, logs, and test reports as possible leakage or
  trust channels.
- Treating staging as proof of production safety without checking environment
  differences.
- Treating Kubernetes Secrets as encrypted merely because values are base64
  encoded.
- Expanding a local deploy script without considering credentials, target
  selection, dry run, rollback, and confirmation.
- Replacing Engineering Review with a DevSecOps checklist.

## Source Register

| Source | Class | Authority | Version/date | Last checked | Relevance | Confidence limits |
| --- | --- | --- | --- | --- | --- | --- |
| NIST SP 800-218, Secure Software Development Framework Version 1.1 (`https://csrc.nist.gov/pubs/sp/800/218/final`, `https://csrc.nist.gov/Projects/ssdf`) | U.S. government special publication | Primary/authoritative for secure development framing | February 2022; project page checked as current | 2026-07-10 | Secure SDLC vocabulary; Prepare, Protect, Produce, Respond practice framing | High for secure-development context; not a universal DevSecOps implementation checklist |
| OWASP SAMM (`https://owasp.org/www-project-samm/`, `https://owaspsamm.org/model/`) | OWASP maturity model | Authoritative OWASP project | Version 2.0.3 / version 2 model | 2026-07-10 | Secure build, secure deployment, defect management, verification, operations, environment management | High for maturity vocabulary; do not force every task through a maturity assessment |
| OWASP ASVS (`https://owasp.org/www-project-application-security-verification-standard/`) | OWASP verification standard | Authoritative OWASP project | Latest stable 5.0.0 | 2026-07-10 | Application security verification vocabulary and evidence rigor | High for application-control verification context; not a CI/CD standard |
| SLSA Specification v1.2 (`https://slsa.dev/spec/v1.2/`, `https://slsa.dev/spec/v1.2/threats`) | Supply-chain integrity specification | Industry consensus open specification | v1.2 approved | 2026-07-10 | Source/build tracks, provenance, verification, attestations, supply-chain threat model | High for supply-chain concepts; do not claim levels without task-specific evidence |
| OpenSSF Scorecard (`https://scorecard.dev/`, `https://github.com/ossf/scorecard/blob/main/docs/checks.md`) | OpenSSF security-health tool/docs | Authoritative project docs | Current docs; checks continually change | 2026-07-10 | Repository signals: branch protection, code review, CI tests, dangerous workflows, pinned dependencies/actions, binary artifacts | Medium-high for automated signal ideas; scores are not review verdicts |
| GitHub Actions secure use reference (`https://docs.github.com/en/actions/reference/security/secure-use`) | Platform security documentation | Primary vendor docs | Current GitHub Docs | 2026-07-10 | Workflow secrets, `GITHUB_TOKEN`, script injection, `pull_request_target`, third-party action pinning, OIDC, environment reviewers | High for GitHub Actions tasks; verify exact platform behavior at task time |
| GitHub Actions token and secrets docs (`https://docs.github.com/en/actions/tutorials/authenticate-with-github_token`, `https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets`) | Platform security documentation | Primary vendor docs | Current GitHub Docs | 2026-07-10 | Token permissions, secret handling, masking, environment secrets | High for GitHub Actions; platform-specific |
| GitLab CI/CD variables docs (`https://docs.gitlab.com/ci/variables/`) | Platform security documentation | Primary vendor docs | Current GitLab Docs | 2026-07-10 | Sensitive variables, masked/protected/hidden variables, forked MR exposure, review before running pipelines | High for GitLab variables; version-specific behavior may change |
| GitLab CI/CD job token docs (`https://docs.gitlab.com/ci/jobs/ci_job_token/`) | Platform security documentation | Primary vendor docs | Current GitLab Docs | 2026-07-10 | Short-lived job tokens, allowlists, runner security, public/internal access | High for GitLab job-token tasks; feature/version specifics require refresh |
| GitLab external secrets docs (`https://docs.gitlab.com/ci/secrets/`) | Platform security documentation | Primary vendor docs | Current GitLab Docs | 2026-07-10 | External secret providers and ID-token based retrieval | High for GitLab secret retrieval; tier/provider availability matters |
| Kubernetes Pod Security Standards (`https://kubernetes.io/docs/concepts/security/pod-security-standards/`) | Kubernetes official docs | Primary project docs | Current docs, v1.36 nav | 2026-07-10 | Privileged, Baseline, and Restricted runtime profile vocabulary | High for Kubernetes workload context; exact enforcement depends on cluster/version |
| Kubernetes Secrets good practices (`https://kubernetes.io/docs/concepts/security/secrets-good-practices/`) | Kubernetes official docs | Primary project docs | Current docs | 2026-07-10 | Secret encryption, access control, namespace separation, external stores, manifest caution | High for Kubernetes secret handling; provider-specific behavior needs refresh |
| Kubernetes RBAC good practices (`https://kubernetes.io/docs/concepts/security/rbac-good-practices/`) | Kubernetes official docs | Primary project docs | Current docs | 2026-07-10 | Least privilege, service-account/token distribution, wildcard permissions, cluster-admin risk | High for Kubernetes RBAC; exact impact depends on cluster configuration |
| Docker build best practices (`https://docs.docker.com/build/building/best-practices/`) | Docker official docs | Primary vendor/project docs | Current Docker Docs | 2026-07-10 | Multi-stage builds, trusted/minimal base images, rebuilds, image testing in CI | Medium-high for Docker builds; not a full runtime security standard |
| Docker build secrets (`https://docs.docker.com/build/building/secrets/`) | Docker official docs | Primary vendor/project docs | Current Docker Docs | 2026-07-10 | Build secret mounts and SSH mounts; avoiding build args/env for secrets | High for Docker/BuildKit build-secret handling |
| Docker Engine security and daemon access (`https://docs.docker.com/engine/security/`, `https://docs.docker.com/engine/security/protect-access/`) | Docker official docs | Primary vendor/project docs | Current Docker Docs | 2026-07-10 | Container isolation, daemon attack surface, socket protection, SSH/TLS daemon access | Medium-high; hardening depends on host/runtime/orchestration |
| CIS Kubernetes Benchmark (`https://www.cisecurity.org/benchmark/kubernetes`) | CIS benchmark landing page | Authoritative benchmark publisher | Kubernetes benchmark 2.0.1 listed | 2026-07-10 | Secure configuration benchmark reference for Kubernetes | High for benchmark existence/version; detailed controls require task-specific PDF inspection |
| CIS Docker Benchmark (`https://www.cisecurity.org/benchmark/docker`) | CIS benchmark landing page | Authoritative benchmark publisher | Docker benchmark 1.8.0 listed | 2026-07-10 | Secure configuration benchmark reference for Docker | High for benchmark existence/version; detailed controls require task-specific PDF inspection |
| NTIA SBOM resources (`https://www.ntia.gov/page/software-bill-materials`) | U.S. government SBOM resource hub | Authoritative public-sector SBOM reference | 2021 resources | 2026-07-10 | SBOM definition, component transparency, production/acquisition/use concepts | High for SBOM purpose; SBOM alone does not prove safety |
| Microsoft Security Development Lifecycle (`https://www.microsoft.com/en-us/securityengineering/sdl/`) | Vendor secure development lifecycle guidance | Major vendor/practitioner source | Current Microsoft page | 2026-07-10 | SDL integrated into DevOps, lifecycle practice framing, supply-chain consumption context | Medium-high; Microsoft-specific practices should be adapted, not mandated |
| Google SRE Book, production environment and SLO chapters (`https://sre.google/sre-book/production-environment/`, `https://sre.google/sre-book/service-level-objectives/`) | Practitioner book from Google SRE/O'Reilly | Authoritative practitioner reference | 2017 online book | 2026-07-10 | Production readiness, monitoring, rollout, operational assumptions, SLO context | Medium for security control selection; strong for operational-readiness prompts |

## Confidence Notes

High confidence:

- The selected sources are authoritative enough for durable DevSecOps
  vocabulary, secure delivery principles, review prompts, and evidence
  categories.
- DevSecOps context belongs as a Domain Knowledge Pack rather than as a new
  role, capability, pipeline, gate, or policy owner.
- CI/CD and deployment automation require explicit security review when they
  handle credentials, permissions, artifacts, release publication, or
  production access.
- Secret masking, SBOMs, Scorecard, SLSA, scan output, signatures, and
  attestations are evidence inputs, not standalone verdicts.

Medium confidence:

- Exact provider behavior, feature availability, default permissions, and
  syntax may change quickly; future platform-sensitive tasks should re-check
  primary vendor docs.
- Docker, Kubernetes, and CIS guidance is useful for review prompts, but exact
  hardening decisions depend on runtime, cluster, host, cloud, version, and
  organizational constraints.

Limited confidence:

- Detailed CIS benchmark controls were not reproduced because public landing
  pages confirm benchmark identity/version while detailed controls require
  task-specific PDF inspection.
- Exact cloud-provider deployment-hardening guidance is intentionally not
  generalized in this pack.
- This pack does not cover broad cybersecurity threat modeling, identity
  architecture, cryptography, incident response, or compliance control
  selection.

## Update Rules

Update this pack when:

- a registered source changes materially, is superseded, retired, or
  contradicted;
- CI/CD platform guidance changes defaults for tokens, secrets, forked
  workflows, environment protection, runner isolation, artifact attestations,
  OIDC, or protected variables;
- SLSA, OpenSSF Scorecard, NTIA SBOM guidance, CIS Benchmarks, Kubernetes, or
  Docker guidance changes in ways that affect pack prompts;
- repeated tasks show missing activation criteria, boundary language, review
  questions, vocabulary, or evidence expectations;
- Engineering Review or Review Agent identifies unsupported, misleading, or
  over-prescriptive guidance;
- a future Cybersecurity Domain Pack requires clearer boundary or handoff
  language;
- Project Lead or Chief Editor accepts a source-backed improvement;
- a future accepted Domain Knowledge Pack Standard adds required sections.

Update path:

- small source-backed clarifications may update this pack directly through a
  reviewed task;
- high-governance, source-heavy, disputed, or boundary-changing updates should
  use a release or reviewed system task;
- preserve provenance, source date/version, and what changed.

## Retirement Rules

Retire or deprecate this pack when:

- AI Editorial Office no longer performs DevSecOps-sensitive delivery,
  automation, configuration, supply-chain, deployment, validation, or
  operational-security work;
- source support becomes too stale or weak to maintain confidence;
- a better canonical owner or replacement pack supersedes it;
- it repeatedly causes confusion with Engineering Review, cybersecurity
  guidance, roles, capabilities, pipelines, review gates, policy ownership, or
  mandatory artifacts;
- maintenance cost exceeds future value.

Retirement must preserve enough context for future readers to know why the
pack should no longer be used. Do not delete historical task artifacts merely
to clean the narrative.

## Relation To Existing Canon

This pack may support:

- Engineering Review when implementation/change safety involves secure
  delivery, CI/CD, automation, configuration, secrets, supply chain,
  deployment, runtime, or operational-security assumptions;
- Architecture Review when deployment, runtime, environment, or ownership
  boundaries have design significance;
- Professional Analysis when DevSecOps reasoning affects synthesis,
  recommendation, risk, or uncertainty;
- Professional Communication when DevSecOps caveats and evidence need clear
  reader transfer;
- Knowledge Evolution when source freshness, pack updates, boundary fixes, or
  retirement are needed.

This pack must not override:

- `AGENTS.md` for governance, role boundaries, task flow, review gate, and
  final decision authority;
- `kb/domain_knowledge_pack_standard.md` for pack structure, activation,
  evidence, boundary, review, update, and retirement rules;
- `kb/engineering_review.md` for implementation/change safety review and
  Engineering Review outcomes;
- `kb/software_architecture_domain_pack.md` for software architecture domain
  context;
- `kb/editorial_evidence_framework.md` for evidence taxonomy and confidence
  labels;
- `kb/editorial_learning_framework.md` for Knowledge Evolution;
- task-local `task-manifest.md`, `orchestration_plan.md`, `status.md`,
  `review.md`, `final.md`, or `final_decision.md`.

`/about` disposition:

- `/about` may summarize or reference this pack for external memory alignment.
- Canonical production use remains under `ai-editorial-office/kb/`.
- If `/about` diverges from this pack, this pack wins.
