# Riyadh Travel Planner — M5 Final Submission

The project files are directly available below; no external attachment is required for saved-result verification. This submission export incorporates the team repository and separately supplied historical source files, with documentation cleanup. Scientific code, original datasets, saved baseline evidence and supplementary judge scores remain unchanged.

## Read first
- [Final M5 report](reports/M5_REPORT.md)
- [Final Baseline V3 primary results](reports/BASELINE_V3_RESULTS.md)
- [Historical V2 results — not the final V3 summary](reports/RESULTS.md)
- [Supplementary judge results and limitations](reports/llm_judge/JUDGE_REPORT.md)
- [Evaluation protocol](docs/EVALUATION_PROTOCOL.md)

20 cases ×3 requested seeds =60 records;58 parsed outputs;49 structurally valid plans. APM93.50%,RBM96.67%,HBM96.67%,IFR81.67%,RTC100%. All failures remain included. Supplementary judge:58 plans,mean4.522/5,not a replacement for primary scoring.

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
