# Riyadh Travel Planner — M5 Final Submission

## Start here

- [Final M5 report](reports/M5_REPORT.md)
- [Supplementary judge report](reports/llm_judge/JUDGE_REPORT.md)
- [Download the complete project, code, tests and saved evidence](riyadh-travel-planner-m5-main.zip)
- [Offline verification notebook](notebooks/M5_Baseline_Verification_Clean.ipynb)

Approved baseline:20 cases ×3 requested seeds =60 saved runs,58 parsed outputs and49 structurally valid plans. Primary means:APM93.50%,RBM96.67%,HBM96.67%,IFR81.67%,RTC100%. Failures remain included. Supplementary judge:58 generated itineraries,mean4.522/5; not a replacement for primary scoring.

## Verification

1. Download riyadh-travel-planner-m5-main.zip from this repository. This archive contains the complete public project snapshot, including Python code and saved60-run evidence.
2. Obtain riyadh_m4_datasets.zip from the private course-submission attachment. It contains the unchanged original M4 CSV datasets, omitted publicly because redistribution permission is not established.
3. Download [evaluate.txt](historical/evaluate.txt) and [experiment.txt](historical/experiment.txt). These are historical fingerprint-matching source files, not replacements for current code.
4. Open the verification notebook in a fresh Colab session. Upload project and datasets when prompted, followed by the two historical files. It verifies checksums, runs tests and audits an isolated historical-source copy. No new Gemini generation is needed.

The cleaned notebook retains outputs from an earlier run and documents the verified workflow; it does not claim a fresh execution of that exact cleaned notebook. Independently reproduced submission checks:53 tests passed;60/60 saved records audited,13/13 historical source files and3/3 datasets matched.

The older python -m m5eval.evaluate path requires the omitted original historical source tree. Use the dedicated V3 verification notebook instead. Do not overwrite existing results or current source to resolve a fingerprint mismatch.

## Scope

IFR is structural and dataset feasibility, not booking availability, opening hours or travel-time certification. RTC is required-tool-name coverage, not proof that selected items came from tool results. Actual monetary cost is not established.

This final submission export is based on the team project maintained at https://github.com/resanrd0522/riyadh-travel-planner-m5 . Numerical scores, primary evidence, model code and supplementary judge outputs remain unchanged.
