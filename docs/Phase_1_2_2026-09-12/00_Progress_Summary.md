# Phase 1 and 2 - Progress summary

**Project:** AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN

**System:** PlantGuard | **Student:** Simran Batwal | **Roll:** 28452500003

M.Tech Computer Science, Semester 3 | Guru Nanak Dev University, Amritsar

**Guide:** Dr. Anil Kumar | **Work record:** 12-13 September 2026

## Completed work
I have prepared a focused review of R1-R4 and recorded each paper's problem, method, data, reported results, limitations and connection to PlantGuard. I have also set up an isolated Python environment, defined the first two-zone telemetry contract, and completed the first tomato dataset download and audit.

The selected original files passed download, checksum and decoding checks. The release contains 4,486 retained images for the three-class benchmark, 235 external images and 180 unsupported leaf images. Synthetic quality and non-leaf cases are stored separately. Ten telemetry tests passed, and an independent verification matched all 4,942 downloaded raw-file hashes and the frozen split fingerprint.

The data scripts and contract are implemented. The dashboard, ESP32 firmware and trained models are not yet implemented. The Colab verification notebook is prepared; it has not been executed in my Colab account.

## What the research changed in my plan
1. I will report internal and external image performance separately. The controlled-image accuracy in R1 does not establish field accuracy.
2. I will describe image-sensor fusion as previous work, with R3 and R4 as relevant examples. My proposed study is a measured reliability comparison, not a claim that combining AI and sensors is new.
3. I will keep missing sensor readings missing. Estimated data will not be presented as physical measurements.
4. I will treat early blight and late blight as different disease labels. They are not two stages of one disease.
5. I will keep biological forecasting conditional on independent, time-labelled disease events. Public still images are not enough for an early-warning claim.
6. I will record uncertain labels, duplicate decisions and excluded images before training. A high score on an unchecked dataset would be difficult to defend.

## Current research question
How do the four selected image models and a simple quality/uncertainty policy compare on supported images, different capture conditions and unfamiliar inputs?

I will compare MobileNetV3 Large, ResNet50, EfficientNet-B0 and ViT-B/16 using the same data lists. The comparison will include macro-F1, per-class recall, accepted-case error, answer coverage, unsupported acceptance and laptop inference time. The detailed protocol follows in this report.

## Next milestone
The next software milestone is a laptop dashboard with image upload, two zones, history and clearly labelled simulated sensor readings. In parallel, a small training pipeline check will establish the Colab runtime and checkpoint workflow before the full four-model experiments.

Hardware purchase will follow the working software and model-comparison checkpoint. Actual calibration, wireless behaviour and field evidence will be added after the components arrive. College processing remains on a laptop; the later market design uses VPS/cloud AI.

## Discussion points for my guide
I would like feedback on the three-class tomato scope, the proposed reliability comparison and the evaluation requirements. Expert help with uncertain external labels would improve the study. I will record any suggested changes before the final model experiments.

This report contains the progress record, experiment protocol, dataset audit and four detailed paper reviews. The separate Hinglish revision guide explains how to discuss the work in simple terms.
