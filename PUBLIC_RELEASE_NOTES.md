# Final M5 submission: scope and reproducibility

## Included
- Current evaluation/generation modules, tests, verification scripts and documentation.
- Frozen original activity, restaurant and hotel datasets under data/.
- Twenty golden cases and saved acceptance/candidate-count contracts.
- Complete preserved Baseline V3 cohort, pilot evidence and numerical summaries.
- Supplementary judge scores, reasons, summary and archived execution notebook.
- Historical evaluate.txt and experiment.txt plus verify_submission.py for isolated source-fingerprint verification.

## Supported verification
Install requirements.txt, then run python scripts/verify_submission.py from the repository root. The helper verifies historical TXT hashes, creates a temporary copy, restores only the two historical modules there and runs the independent60-record audit. It makes no new model request and leaves original code/evidence unchanged. Full software tests require optional requirements-gemini.txt; clearly distinguish skipped tests from executed passes.

## Historical material and exclusions
The original course PDFs, historical source/ notebooks and missing V2 full outputs are not supplied. Legacy python -m m5eval.evaluate requires that omitted source/ tree and is not the supported V3 route. Archived notebooks may require historical upload filenames, private source archives or live credentials; their saved outputs are not claims of a fresh execution. The unchanged cohort ZIP is read automatically by the helper; it is an internal integrity-preserved evidence artifact, not an external required attachment.

## Data rights and public visibility
This is a public repository:included datasets and recorded model/tool evidence are visible to everyone. Inclusion was authorized for this export but does not establish the upstream datasets' redistribution licenses or grant new rights. Original sources are described in reports/M5_REPORT.md. Before any further redistribution or reuse, verify the applicable source terms; an explicit license record has not been independently established here. No blanket open-data or open-source license is implied.

## Interpretation and provenance
Primary scores, scientific code, original datasets and judge outputs were not changed by submission packaging. Computational audits are automated checks, not independent human annotation or provider attestation. Names and local environment paths were generalized in exported development notes; no human-review claim is substituted. The original review snapshot is preserved outside this export. Actual student contributions must be factual; this repository does not allocate decision-making roles.

IFR is structural feasibility;RTC is narrow tool-name coverage. Supplementary judge scores use58 plans and do not replace60-run primary scores. Judge inconsistency, missing timestamp and absent independent human calibration remain disclosed. Do not commit credentials, invent missing measurements or silently replace failed records.
