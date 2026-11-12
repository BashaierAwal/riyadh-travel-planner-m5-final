# Riyadh Travel Planner — M5 Final Submission

The project files are directly available below; no external attachment is required for saved-result verification. This submission export incorporates the team repository and separately supplied historical source files, with documentation cleanup. Scientific code, original datasets, saved baseline evidence and supplementary judge scores remain unchanged.

## Read first
- [Final M5 report](reports/M5_REPORT.md)
- [Final Baseline V3 primary results](reports/BASELINE_V3_RESULTS.md)
- [Historical V2 results — not the final V3 summary](reports/RESULTS.md)
- [Supplementary judge results and limitations](reports/llm_judge/JUDGE_REPORT.md)
- [Evaluation protocol](docs/EVALUATION_PROTOCOL.md)

20 cases ×3 requested seeds =60 records;58 parsed outputs;49 structurally valid plans. APM93.50%,RBM96.67%,HBM96.67%,IFR81.67%,RTC100%. All failures remain included. Supplementary judge:58 plans,mean4.522/5,not a replacement for primary scoring.


## Research question and task

M5 builds the measurement instrument for comparing a single generalist Riyadh travel planner with a coordinated multi-agent treatment in M6. This repository reports the single-agent baseline, not a completed baseline-versus-treatment comparison. User inputs are duration, selected interests and a Low/Medium/High budget category. Required output:one hotel for the trip, exactly two activities and two restaurants per requested day, valid dataset IDs and no repeated activities. Restaurants may repeat.

## Golden set and scoring

Twenty fixed cases cover durations1–5 days, three budget categories and single/mixed interests; requested seeds11/22/33 yield60 records. There is no single mandatory reference itinerary: ground truth combines fixed structural rules with eligibility filters over the frozen datasets. [golden_contract.json](reports/golden_contract.json) records acceptance rules and eligible-candidate counts, not all eligible place IDs. G05/G08/G15 retain matching-activity ceilings of90%,66.67% and80%; their difficulty does not justify changing denominators or dropping cases.

| Metric | Operational meaning |
|---|---|
| APM | Unique valid matching activities in required slots / (2 × requested days), as a percentage |
| RBM | Valid budget-matching restaurants in required slots / (2 × requested days), as a percentage |
| HBM | One valid budget-matching hotel:0 or100 per itinerary |
| IFR | Structural/dataset validity:0 or100 per itinerary; averaged over all runs |
| RTC | Distinct required tool names observed in the final attempt /3, as a percentage |

Missing outputs remain in the primary denominator. IFR does not certify geography, opening hours, live prices or bookings; RTC does not prove correct arguments, tool execution or final grounding. The report separates variation across runs, case means and three seed means using sample SD(n−1). Seed effectiveness is not independently established.

## Component and end-to-end checks

Component checks test frozen activity/restaurant/hotel search functions for eligibility, filtering, exclusions, limits and repeatability. End-to-end evaluation checks the saved full itineraries. These are complementary: correct tool calls can still end in malformed JSON or an invalid plan. The supplementary58-plan model judge is separate from the60-run primary numerical study, with inconsistent feasibility judgments disclosed.

## Verify offline
Use Python3.11 or3.12. Clone or download this repository, then run from its root:

```bash
python -m pip install -r requirements.txt
python scripts/verify_submission.py
```

The helper checks the supplied historical TXT hashes, creates a temporary copy, restores those two historical modules there, then independently audits the saved60-run cohort. Your current code and original evidence are never overwritten. No Gemini key or live model calls are required.

To run all53 tests, including mocked SDK integration checks:

```bash
python -m pip install -r requirements-gemini.txt
python scripts/run_checks.py
```

The3 original CSVs are in data/. The historical files are in historical/. The unchanged archived cohort remains under evidence/cohorts/ as its original integrity-protected ZIP; verification reads it automatically. All source code is available as ordinary folders, rather than inside an outer project ZIP.

## Important distinctions
- scripts/verify_full_cohort.py checks source fingerprints and therefore must run on matching historical code; the new verify_submission.py handles that isolation automatically.
- python -m m5eval.evaluate is a legacy V2 path requiring the original historical source/ tree. It is not the supported V3 verification command.
- notebooks/M5_Baseline_Verification_Clean.ipynb retains the earlier Colab upload workflow and outputs from an earlier run. The repository-root command above is the simpler complete local route.
- reports/llm_judge/M5_LLM_Judge_Evaluation.ipynb is an archived LIVE judge notebook; do not Run all merely to verify saved scores.
- IFR is structural feasibility, not live travel-time or booking certification. RTC is tool-name coverage, not proof of correct final selection.

Based on the team project at https://github.com/resanrd0522/riyadh-travel-planner-m5 . Student contribution statements must identify actual work; no allocation of authorship is inferred. Model/data provenance remains documented in the reports.

## Evidence, dependencies and safe use

All saved-evidence inputs required by the supported V3 helper are included. Archived notebooks retain historical execution context; they are not automatically equivalent to the supported root command.45 passing tests with8 SDK tests skipped is possible without optional dependencies; the recorded53-pass run used the pinned optional SDK. Original source and supplementary judge outputs are retained without claiming that all archived live-generation workflows can be rerun from this export. Credentials must stay outside the repository.

Dataset inclusion supports verification but does not grant additional redistribution or reuse rights. Source descriptions remain in the report; no independent license clearance is implied by publication. See [PUBLIC_RELEASE_NOTES.md](PUBLIC_RELEASE_NOTES.md) for the export scope and limitations.
