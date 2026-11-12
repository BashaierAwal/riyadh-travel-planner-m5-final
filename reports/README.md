# Which results should I read?

## Current V3 experiment

Start with [BASELINE_V3_RESULTS.md](BASELINE_V3_RESULTS.md): the final primary results table, distinct from historical RESULTS.md.

- `M5_REPORT.md`: method, primary V3 results, limitations and historical comparison.
- `v3_summary.json`: saved V3 statistics at their original precision.
- `full_cohort_audit.json`: verification and separate recalculation of all sixty records.
- `v3_tool_trace_checks.json`: checks of recorded tool results.

## Historical and supplementary checks

- `RESULTS.md` and `evaluation.json`: historical V2 arithmetic and offline component/supplementary checks. They are not the V3 experiment summary. Their statements about no model calls refer to the offline check command.
- `verification.log`: an earlier run of 30 tests. This is an unchanged historical log, not the latest test count.
- `colab_integration_verification.log`: later integration verification; the tests use the pinned SDK with simulated HTTP responses. The documented 49-test result does not mean every environment will run all SDK tests without their optional dependencies.
- `live_pilot_audit.json`: the earlier one-case pilot, separate from the formal sixty runs.

Running the frozen evaluation pipeline can regenerate `RESULTS.md` under its original generic heading. This index remains the guide to its historical scope. Original logs and experiment files are not rewritten to look newer.

## Supplementary judge,10 November2026

58 saved V3 plans were judged with overall mean4.522/5; the two generation failures remain unjudged. See [llm_judge/JUDGE_REPORT.md](llm_judge/JUDGE_REPORT.md). The earlier absence of judge grades describes a prior stage, not the final submission status.
