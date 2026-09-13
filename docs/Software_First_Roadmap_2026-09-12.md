# PlantGuard: software-first fast-track roadmap
Date: 12 September 2026
Student: Simran Batwal | Roll: 28452500003 | Guide: Dr. Anil Kumar
Project: AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN

## Working decision
I will prepare and test the software before purchasing the physical components. The first purchase will follow a working software demonstration and a final compatibility check. College processing will run on a laptop. The later market version will run its main AI on VPS/cloud.

This schedule replaces the earlier immediate-purchase order. The earlier master plan and guide reports remain reference documents. Work will start from the currently agreed tomato-first scope; later guide feedback will be recorded as changes rather than assumed approval.

## Verified starting position
- Topic, initial planning, guide report and preliminary literature notes are available.
- Application, firmware, downloaded datasets and trained models have not been implemented yet; their folders currently contain placeholder files.
- Laptop checked on 12 September: Intel Core i7-6600U, four logical processors, approximately 7.7 GB RAM, Intel HD Graphics 520, approximately 56.8 GB free on C: at the time of inspection.
- No NVIDIA GPU was listed. Use the laptop for development, data checks, simulation and small CPU runs. Full model comparisons should use an accessible GPU runtime.
- Free Google Colab GPU availability is variable. No paid compute, hardware order or third-party account action is authorised by this plan alone.

## Time assumption
Target approximately 20-25 focused working days to reach the software purchase checkpoint, with up to 8-10 hours of available daily project time. Allow about 3-5 calendar weeks because GPU sessions, downloads, review changes and debugging can delay completion. This is an estimate, not a promised completion date.
After parts arrive, allow a further 7-14 working days for assembly, calibration and an integrated engineering demonstration. Delivery time is additional. Biological forecasting or field-generalisation evidence may need much longer and is not compressed into this schedule.

## Phase 1: foundation and paper review - days 1-2
Work:
- Read R1-R4 in depth: problem, data, method, reported results, limitations, split design and relevance to PlantGuard.
- Record what is established prior work and what the proposed reliability comparison changes.
- Audit existing project files, install an isolated development environment and record dependency versions.
- Define the image classes, two-zone sensor message format and directory structure.
- Set up run IDs, dataset versions, Git/source revision records and experiment tracking.

Outputs:
- Four detailed source-linked paper notes, a research comparison table, environment record and tracked task list.
- No fabricated completion status for papers not yet fully examined.
Checkpoint: the data and experiment protocol is clear enough to implement.

## Phase 2: datasets and data checks - days 2-5
Work:
- Download the selected tomato healthy, early-blight and late-blight image data from identified sources.
- Keep source URL, version/retrieval date, licence, original counts and actual local checksums.
- Detect unreadable images, exact duplicates and likely near duplicates.
- Create training/validation/test lists before augmentation. Group by plant/session/source where trustworthy identifiers exist; document limitations where they do not.
- Keep a separate external-condition image evaluation where labels and rights are compatible.
- Prepare separate unfamiliar and poor-quality input cases without using test examples to tune thresholds.

Outputs:
- Actual downloaded files, a manifest, per-class counts, exclusions, split lists and a data audit.
Checkpoint: no assumed class counts; no unresolved duplicate leakage in the selected benchmark.
Only the first tomato subset is required initially. Other crops remain in the wider roadmap after the core pipeline passes.

## Phase 3: laptop dashboard and sensor simulator - days 4-8
Work:
- Build a local browser dashboard usable from the desktop, initially launched through a simple local start command/shortcut.
- Implement Python/FastAPI services, SQLite records, image upload and two-zone views.
- Build an explicitly labelled simulator that sends the same measurement schema planned for ESP32.
- Include normal, missing, stale, repeated, implausible and disconnected sensor scenarios.
- Save images and sensor histories with their source type, zone and time.
- Show an untrained/not-configured model state until a real trained model is available.

Outputs:
- Working laptop application, simulated two-zone logs and API tests.
Checkpoint: an image and its records can move through the application; no demonstration data is presented as a physical measurement.
A separate Windows-native application is not required for the first milestone; the desktop-accessible dashboard is the initial interface.

## Phase 4: four image-model experiments - days 7-14
Models: MobileNetV3 Large, ResNet50, EfficientNet-B0 and a documented ViT configuration.

Work:
- Use pretrained weights and fine-tune for the supported tomato categories.
- First run short pipeline tests; distinguish these from the final training runs.
- Use the same dataset split and comparable tuning effort, while retaining each model's documented preprocessing.
- Measure GPU/runtime availability and pilot epoch time before setting the final training budget.
- Train all four models, preserve best and last checkpoints, and resume interrupted runs where supported.
- Select hyperparameters and confidence thresholds using validation data.
- Repeat final runs with multiple seeds when the available compute supports it; if only one run is possible, report that limitation clearly.
- Evaluate the final configurations on the untouched internal test and compatible external test.
- Select the deployment model using classification performance, errors, size and measured laptop latency.

Outputs:
- Four completed model run records, checkpoints, learning curves, metrics, confusion matrices and image-level predictions.
- A comparison table generated from saved results.
Checkpoint: actual final results exist for each planned model; placeholder values and short smoke runs do not count as completed comparisons.

## Phase 5: quality handling and integration - days 12-17
Work:
- Connect the selected trained model to the dashboard.
- Add image-quality checks, a validation-tuned uncertainty/rejection policy and limited rescan requests.
- Validate sensor schema, freshness and missing-data handling using simulation.
- Compare accepted-case errors, answer coverage, unfamiliar-input errors, rescan count and response time.
- Keep image diagnosis and environmental context as separate outputs unless a properly labelled paired fusion experiment is possible.
- Prepare a small reviewed management-information module with source and review date.

Outputs:
- Integrated image workflow, saved comparison cases and repeatable simulated fault tests.
Checkpoint: the system does not turn missing sensor data into a confident biological conclusion.
Simulation can test software decisions. It cannot establish sensor accuracy, disease lead time or real-world image-sensor improvement.

## Phase 6: software purchase checkpoint - days 18-22, buffer to day 25
Work:
- Finish end-to-end testing, startup instructions, data export and a demonstration recording.
- Prepare firmware and interface code for the selected ESP32 design; compile where possible before boards are available.
- Save repeatable test cases and a simple restore/backup procedure.
- Update the guide report and draft thesis chapters from the work actually completed.
- Recheck component compatibility, availability and current vendor prices. Record dated public listings separately from formal quotations.
- Finalise the shopping list only after the software checkpoint.

Required before the user buys components:
1. Laptop app launches and image analysis works with a genuinely trained model.
2. All four planned model comparisons have saved results.
3. Two simulated zones use the planned real-device schema.
4. Missing/stale data and poor-quality images have defined tested responses.
5. Checkpoints, predictions and experiment metadata are retained.
6. Hardware BOM and interfaces are internally consistent.
7. Software-only achievements and pending physical tests are clearly listed.

## Phase 7: purchase and hardware validation - after delivery, 7-14 working days
The user purchases components after Phase 6. No component order is placed automatically.

Work:
- Inspect components and check supplies, logic levels and exact sensor variants.
- Bring up one ESP32, read one sensor at a time and calibrate in the selected medium.
- Duplicate the working node and verify separate Wi-Fi telemetry.
- Replace simulated inputs with real readings without changing the data contract.
- Check camera placement, sensor locations, gaps, reconnect and a 24-hour log.
- Store real records with source_type=physical and separate them from simulated records.

Outputs:
- Working two-pot/two-node engineering demonstration, calibration logs, real telemetry and measured limitations.
Physical power behaviour, firmware flashing, Wi-Fi reliability and sensor calibration cannot be completed before this phase.

## Phase 8: final academic package - alongside development and after real tests
Draft introduction, related work and methods during the software phases.
Fill results only from saved experiments. Add hardware findings after measurements.

Final outputs:
- Thesis/report with sourced related work and actual results.
- Model comparison, confusion matrices, graphs and failed-case analysis.
- Software architecture, final wiring, component cost statement and calibration method.
- Demonstration screenshots/video, presentation and updated viva preparation.
- Reproducibility instructions, code revision and dataset/run references.

## Data-dependent work that remains conditional
RF/XGBoost sensor learning needs labelled examples. GRU/LSTM forecasting needs independent time-labelled disease events. Severity requires suitable region annotations. Continual learning needs verified new labels and old/new task evaluation. Two pots and synthetic sensor data are not enough to claim validated biological forecasting. Public images will not be paired with invented sensor values.

## Daily working pattern
Use available time for a mix of implementation, testing and understanding rather than treating ten hours as a guaranteed accelerator for every task.
- About 4 hours: coding/data work.
- About 2 hours: training supervision, evaluation or debugging.
- About 1.5 hours: paper reading and viva understanding.
- About 1 hour: experiment notes, figures and thesis draft.
- About 1.5 hours: review, integration and buffer.
Adjust this split to the phase. Long GPU jobs have their own wall-clock duration.

## Responsibilities
Assistant: source review, software and firmware preparation, data processing, training/evaluation scripts, accessible run execution, debugging and evidence organisation.
Student: account sign-in or GPU-session access where required, guide feedback, understanding the work, later physical assembly/photographs and purchase.
No background work after the conversation ends or scheduled run is assumed. Running jobs need explicit runtime/session management.

## Compute references
- Google Colab resource availability and session limits: https://research.google.com/colaboratory/faq.html
- PyTorch local CPU/CUDA setup: https://pytorch.org/get-started/locally/

## Current completion record
Completed now: reviewed project state, checked laptop hardware, agreed software-first ordering from the user's request, and prepared this roadmap.
Not completed now: detailed R1-R4 review, dataset downloads, application implementation or model training.


## Phase 1-2 completion update - 13 September 2026
Research foundation and first tomato data release completed; see [release index](Phase_1_2_2026-09-12/README.md). This update supersedes the initial completion record above. Data tooling and telemetry contract tests are implemented. The laptop dashboard, firmware, Colab runtime execution and trained models remain next-phase work. Hardware purchase timing is unchanged.
