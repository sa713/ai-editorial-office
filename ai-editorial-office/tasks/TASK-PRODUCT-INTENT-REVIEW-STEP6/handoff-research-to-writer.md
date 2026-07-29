# Handoff — Research Agent to Writer Agent

- From: `research_agent`
- To: `writer_agent`
- Reason: baseline, hybrid design, rubric, case schema, expected-result policy,
  and production-change gate are fixed before evaluation results.
- Implement: 30+ case fixture, deterministic runner, runner negative tests,
  catalogue, coverage/baseline/evaluation/defect/repair reports.
- Preserve: product judgment variability, manual evaluation independence,
  critical failure conditions, and all Step 1–5 regressions.
- Do not change: production contracts unless a frozen failing case proves a
  defect; roles, pipelines, stages, gates, statuses, outcomes, deliverables,
  modes, Professional Analysis, project state, or Step 7.
- Escalate if: runner automation would substitute for expert judgment or a
  production repair is proposed without defect evidence.
