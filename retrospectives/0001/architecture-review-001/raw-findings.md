# Raw findings

## Sources inspected

- `ai-editorial-office/AGENTS.md`
- `ai-editorial-office/project-state.md`
- `ai-editorial-office/agents/chief_editor.md`
- `ai-editorial-office/agents/review_agent.md`
- `ai-editorial-office/pipelines/article_pipeline.md`
- `ai-editorial-office/pipelines/review_pipeline.md`
- `ai-editorial-office/templates/artifacts/task_manifest_template.md`
- `ai-editorial-office/templates/artifacts/handoff_template.md`
- `ai-editorial-office/kb/task_statuses.md`
- `editorial_knowledge/10_operational_rules.md`
- `editorial_knowledge/20_editorial_modes.md`
- `editorial_knowledge/30_compact_editorial_brief.md`
- `editorial_knowledge/31_usefulness_dimensions.md`
- `editorial_knowledge/40_editorial_review_system.md`
- `editorial_knowledge/50_editorial_failure_patterns.md`
- `editorial_knowledge/90_system_review.md`
- selected task artifacts from TASK-0004, TASK-0006, TASK-0008
- external reference: `DenisSergeevitch/agents-best-practices`

## Raw observations

- System is more editorial operating system than agent framework.
- Strongest idea: usefulness-first, not format-first.
- Strongest architecture: repository-first memory plus review-gate.
- The system already knows its main enemy: bureaucracy and artifact bloat.
- There is tension between "production-grade" and "single-user local".
- `README.md` is empty. Not a problem, but the active entrypoint is `AGENTS.md`.
- `project-state.md` is useful but can become a second AGENTS.md if not kept as current-state only.
- `AGENTS.md` is long but coherent.
- The current MVP agent set is sensible.
- Future agents should stay future.
- Review Agent is very powerful; could become overloaded.
- Chief Editor is necessary, but can become bottleneck.
- Writer and reviewer separation is critical.
- Final Editor role makes sense only if finalization is controlled and not rewriting.
- Human approval boundary is good and visible in tasks.
- The word `finalized` may still mislead non-system users.
- TASK-0006 handles publication approval well.
- TASK-0008 is a strong example of system flexibility.
- TASK-0008 also shows custom workflow needs a mini-contract.
- Some older handoff filenames include multiple possible recipients.
- Newer handoff template correctly discourages that.
- `compact-handoff.md` seems to mean final user handoff, not role-to-role handoff.
- This should be clarified.
- Real tasks have many files.
- Many files are justified for complex tasks.
- But artifact count can become a status symbol.
- TASK-0001/TASK-0002 with 25+ files may be normal for early development but not ideal as examples.
- `final(1).md` in TASK-0004 is a file naming smell.
- `.DS_Store` exists; irrelevant to architecture but shows local filesystem noise.
- `editorial_knowledge/90_system_review.md` is unusually self-aware and already names key risks.
- `01_principles.md`, `02_editorial_intent.md`, `03_usefulness_review.md` are tiny/scaffold-like.
- These could confuse retrieval if treated as active source of truth.
- Editorial modes are useful, but list should not grow much.
- Usefulness dimensions are good because they prevent over-dry writing.
- Emotional usefulness is powerful but easy to abuse.
- Review system has good false-positive prevention.
- Failure patterns are concrete and practical.
- Failure patterns should not become mandatory checklist items.
- A few worked examples would be higher value than more theory.
- "source traceability" is strong in system docs.
- "trust labels" for source content are underdeveloped.
- Prompt injection risk is not urgent for local writing, but source documents can still contain instructions.
- Treat source materials as data unless promoted to instruction.
- Best-practices emphasizes model proposes, harness acts. In this repo, "harness" is mostly markdown discipline, not code.
- That is acceptable for current maturity.
- Do not build code harness too early.
- No tool execution layer exists inside AI-editorial-office; most risk is editorial side effect, not API side effect.
- Editorial side effects include sending, publishing, stakeholder interpretation, reputational risk.
- Publication/delivery approval state is the analog of permission gate.
- The system could benefit from event trace, but markdown run ledger may be enough.
- A full event store is overkill.
- A short run ledger inside status or manifest could help.
- Manifest freshness is the highest-leverage small improvement.
- Review independence evidence is another small improvement.
- Risk modes should control review depth more explicitly.
- Low-risk path is mentioned but not materialized.
- Future low-risk compact path should not become a separate complicated pipeline.
- Status vs stage distinction is subtle.
- Some agents may confuse `approved` status with review outcome.
- System already says local role outcome must map through status model. Good.
- There is no automated check for stale status transitions.
- Do not add automation yet; add checklist first.
- "No artifact should duplicate another artifact's primary responsibility" is a core principle worth preserving.
- Some templates are long and may themselves cause context bloat.
- Best-practices says context should be built, not dumped. The repo agrees, but role specs are long.
- Agent specs could be shortened after responsibility map is stable.
- Pipeline docs could be shortened after common lifecycle extraction.
- This should be medium/deep work, not quick win.
- Current system is viable for controlled real tasks.
- Next learning should come from real task retrospectives, not new doctrine.
- A regression set from completed tasks would be valuable.
- Markdown fixtures are enough.
- Do not implement dashboards.
- Do not implement scoring.
- Do not implement autonomous role routing.
- Do not add MCP/connectors unless actual external systems appear.
- Do not treat this as coding-agent architecture; it is an editorial control plane.
- The architecture should remain boring in the best way.

## Potential directions

- Add `process-depth: compact | normal | full` to orchestration.
- Add `artifacts intentionally omitted` to orchestration for low-risk tasks.
- Add `review depth` to review artifacts.
- Add `independence check` to review artifacts.
- Add `source trust labels` to research/review.
- Add `custom workflow mini-contract` to orchestration.
- Create `cases` examples from TASK-0008.
- Run a drift scan after every 3-5 system updates.
- Archive or annotate legacy task artifacts as historical.
- Make `README.md` a short map to `AGENTS.md`, not a manual.
- Keep `project-state.md` as current-state, not permanent policy.
- Create "do not imitate legacy artifacts" note.
- Create "minimal viable task package" note.
- Add "human send approval" line to final decisions when relevant.

## Open questions

- Should compact path combine `status.md` and `task-manifest.md`, or keep both but shorter?
- Should final user-facing handoff be renamed from `compact-handoff.md` to `delivery-handoff.md` or `user-handoff.md`?
- Should custom diagnosis become its own lightweight pipeline after one more similar task?
- How much evidence is enough to prove reviewer independence in a single-user local system?
- Should task folders include a `run-log.md`, or is `status.md` enough?
- Should old task folders be treated as examples or just history?
- How should source material trust be represented without adding heavy metadata?
- Should editorial knowledge have an index that marks active, placeholder, historical, and example files?

## Strong opinions

- Do not add new agents now.
- Do not add a workflow engine now.
- Do not add scoring now.
- Do not expand modes now.
- Do not remove review-gate.
- Do not weaken human approval boundary.
- Do not let compact path become excuse to skip traceability when factual claims exist.
- Do not let high-governance tasks use compact path.
- Do not let examples become templates that every task must follow.
- Keep the system small enough that a user can understand why each artifact exists.
