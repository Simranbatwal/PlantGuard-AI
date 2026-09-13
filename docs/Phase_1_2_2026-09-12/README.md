# PlantGuard - Phase 1 and Phase 2 completed work

Release date: 13 September 2026. Data retrieval and preparation: 12 September 2026.

## Start here
- [Progress report PDF](PlantGuard_Phase_1_2_Progress_Report.pdf) - 18 pages, with literature review, methods, measured data counts and limitations.
- [Matching editable report](PlantGuard_Phase_1_2_Progress_Report.md)
- [Simple Hinglish revision guide](03_Simran_Revision_Guide.md)
- [Local and Colab run instructions](04_Run_Instructions.md)
- [Colab verification notebook](../../ml/notebooks/Phase_2_Data_Verification.ipynb)
- [Prepared Colab data/code bundle](../../artifacts/PlantGuard_Phase12_Colab.zip) - approximately 192 MiB.

## Detailed records
- [Research protocol](01_Research_and_Protocol.md)
- [Dataset audit](02_Dataset_Audit.md)
- [R1 review](R1_Detailed_Review.md), [R2 review](R2_Detailed_Review.md), [R3 review](R3_Detailed_Review.md), [R4 review](R4_Detailed_Review.md)
- [Original paper PDFs](papers/)
- [Environment record](environment.json)
- [Independent data verification](verification.json)
- [Telemetry test results](test_results.txt)
- [Dataset manifests and splits](../../data/processed/tomato_v1/)
- [Source metadata and review decisions](../../data/sources/)

## Completion checklist
- [x] Four source papers downloaded and detailed notes prepared.
- [x] Previous work separated from the proposed PlantGuard comparison.
- [x] Python 3.12 environment, pinned dependencies and telemetry contract prepared.
- [x] Ten telemetry tests passed; dependency compatibility check passed.
- [x] 4,942 original images downloaded and hash/decode checked.
- [x] Exact/pixel duplicate and perceptual-similarity screening completed.
- [x] Known source leaf grouping applied; missing identities documented.
- [x] External-image and flagged-pair visual screening decisions saved.
- [x] Final benchmark/external/OOD splits and synthetic-case lists saved.
- [x] Independent verification of all original files and split membership passed.
- [x] PDF rendered and visually inspected; student details and key counts checked.
- [x] Colab package archive verified and notebook code syntax checked.
- [ ] Colab account execution - belongs to the upcoming run setup, not claimed here.
- [ ] Dashboard, firmware and model training - subsequent phases.

## Important boundary
The prepared first benchmark contains 4,486 supported images, 235 external images and 180 unsupported leaves. The external labels remain repository labels after visual screening, not pathology-confirmed ground truth. Natural non-leaf photographs, local images, paired sensor readings and prospective disease events are future data additions. No trained accuracy or hardware performance is claimed.

Phase 3 starts with the laptop dashboard and explicitly labelled sensor simulator. Hardware purchase remains after the working software and four-model checkpoint. The future market AI architecture remains VPS/cloud.
