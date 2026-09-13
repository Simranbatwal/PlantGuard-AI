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


---

# PlantGuard - Phase 1 research and implementation protocol

Simran Batwal | Roll 28452500003 | M.Tech Computer Science, Semester 3
Guru Nanak Dev University, Amritsar | Guide: Dr. Anil Kumar
12 September 2026

## What I have prepared
I have prepared a detailed review of four relevant papers, an isolated Python development environment, the first telemetry contract, and a reproducible image-data preparation pipeline. The original papers and source metadata are saved with the project. Model training and the dashboard are the next stages.

## What previous work has already established
| Paper | Previous work | Main lesson for my experiment |
| --- | --- | --- |
| R1, Mohanty et al. | CNN classification of controlled leaf images | Keep related leaves together and report external performance separately |
| R2, Singh et al. | A varied web-image dataset and classification/detection benchmarks | Check file counts, labels and image conditions instead of assuming benchmark quality |
| R3, Chen et al. | Image-sensor fusion, estimated missing modality and segmentation | Fusion is previous work; an estimated value is not a measured value |
| R4, Gao et al. | Time-aligned tomato risk modelling and greenhouse control | Forecasting needs chronological, outcome-labelled history |

The detailed reviews contain the source links, reported results, methods and limitations. This is a focused review of R1-R4, not an exhaustive systematic literature survey. I am not claiming that no other research has considered reliability or missing inputs.

## My research question
How do four image models and a simple quality/uncertainty policy compare when the system receives clean images, less controlled photos and unsupported inputs?

The first comparison will use MobileNetV3 Large, ResNet50, EfficientNet-B0 and ViT-B/16. The practical contribution is a reproducible comparison and a working two-zone monitoring workflow that handles incomplete evidence clearly. Whether the proposed policy improves reliability will be determined by experiments.

## Experiments to run after data preparation
1. Image-only baseline: compare the four pretrained architectures using the same train, validation and internal test lists.
2. Generalisation check: evaluate the frozen configurations on the separate compatible PlantDoc external set. Do not fine-tune or select thresholds on this set.
3. Rejection comparison: compare always-answer classification with a validation-selected confidence threshold, then with an image-quality check plus the threshold. Report both error and answer coverage. A model that rejects everything is not useful.
4. Software fault scenarios: missing, stale, duplicate and invalid sensor messages. These test application behaviour, not physical sensor accuracy.
5. Optional rescan study: later obtain paired first/repeat photos. Artificial blur/darkness is a stress test and does not establish real user rescan success.

## Fair model comparison
- Class order is fixed: 0 healthy, 1 early_blight, 2 late_blight.
- Use pretrained image weights with a replaced three-class output layer. Record exact model/weights identifiers and their terms.
- Use the frozen image split and training-only augmentation. All hyperparameter, stopping and threshold decisions use validation data.
- Primary selection metric: validation macro-F1. Record accuracy and per-class precision/recall/F1 as well. Resolve a tied rounded macro-F1 using measured laptop latency, then model size.
- Start with an equal small pilot budget to measure epoch time. Select a comparable tuning budget before final runs; document architecture-specific preprocessing and any resource compromises.
- Planned training seeds: 42, 43 and 44. Report mean and spread if all three are completed; label single-seed results if compute prevents repeats.
- Freeze the final settings before evaluating the internal test. Report all four final configurations, including weak results, without changing them in response to test errors.
- An initial rejection operating point will target at least 85% supported validation coverage, then minimise accepted-case error; also report the full coverage/error curve. Select thresholds on validation/OOD-validation only. This is a proposed research criterion, not achieved performance.
- Report accepted-case error, supported coverage and unsupported acceptance separately. Confidence is not a calibrated probability unless calibration is evaluated.
- Measure CPU inference after warm-up, record batch size, image preprocessing time, repetitions, median and p95 latency. Measure on the laptop, not by transferring a Colab GPU timing.
- Preserve checkpoints, environment, predictions and failed runs using experiments/README.md. Record source revision and split hash with every run.

## Data design
Use the original colour PlantVillage subset for the benchmark. Keep source leaf groups and detected duplicate relations within a single split. Ratios target 70/15/15 by image count, but whole groups take priority, so exact counts may differ slightly. PlantDoc is an external-only custom pool; its original split is recorded but not used as our training split. Unsupported leaves and synthetic image degradations have their own validation/test lists.

Original files remain unchanged. The manifest records SHA-256, repository blob hash, dimensions, label, group and exclusion reason. Near-duplicate matching is conservative screening, not proof of exhaustive identity detection. Remaining unknown plant/session identities limit independence claims. A visually readable image is not automatically a pathology-confirmed label.

## Two-zone telemetry contract
Each record contains schema version, node and zone identity, boot ID, sequence number, timezone-aware capture timestamp, source type, firmware version and measurements. Allowed nodes are PG-A/zone A and PG-B/zone B. The source is physical, simulated or replay. Missing measurements are null, not zero. A relative soil-moisture value requires a calibration ID.

The fields are air temperature in Celsius, relative humidity in percent, raw soil ADC, calibrated relative soil moisture, raw leaf-wetness reading, wet/dry/unknown state and optional lux. Raw leaf-wetness output needs the purchased sensor's register/units documentation. Relative soil moisture is not true volumetric water content. The schema bounds screen impossible encodings; they are not plant-specific care thresholds.

The future backend will add received_at in UTC. It will use node_id + boot_id + sequence for deduplication, preserve captured_at for freshness checks, and flag implausible future clock values. Initial sampling target is 60 seconds; a proposed stale flag after three missed intervals will be tested, not assumed biologically meaningful. No freshness decision is made by this schema alone.

## Development and compute
Local Python 3.12 is isolated in .venv. Pinned dependencies are saved in requirements-phase12.lock.txt. The current environment supports decoding, hashing, split preparation and schema tests. PyTorch and the actual training loop will be added in the model-training phase. Colab access is confirmed by me; a GPU session has not been connected or used yet.

College AI runs on a laptop. The later market version runs main AI on VPS/cloud. Sensor boxes contain sensing, power and communication components. Hardware purchase stays after the working software and four-model comparison checkpoint.

## Questions for my next guide meeting
- Is the tomato-first three-class scope suitable for the initial experimental chapter?
- Is the proposed reliability comparison sufficient, with forecasting conditional on real paired data?
- Can the department help review uncertain external-image labels or provide plant-pathology access?
- Should the final comparison use three seeds or a different evaluation requirement?

I can proceed with the software foundation while recording any changes suggested by my guide.


---

# Phase 2 - Tomato dataset preparation and audit

I have downloaded and checked the selected original images. The first release is tomato_v1. The data lists are ready for controlled experiments; model training is the next stage.

## Actual class counts

| Class | Downloaded | Retained | Train | Validation | Internal test |
| --- | --- | --- | --- | --- | --- |
| healthy | 1591 | 1585 | 1111 | 237 | 237 |
| early blight | 1000 | 1000 | 700 | 152 | 148 |
| late blight | 1909 | 1901 | 1331 | 284 | 286 |
| Total | 4500 | 4486 | 3142 | 673 | 671 |

The split targets 70/15/15. Whole related-image groups are kept together, which explains small differences from exact percentages. Per-class metrics will account for the unequal class sizes.

| External PlantDoc class | Downloaded | Retained external test | Excluded |
| --- | --- | --- | --- |
| healthy | 63 | 46 | 17 |
| early blight | 88 | 81 | 7 |
| late blight | 111 | 108 | 3 |
| Total | 262 | 235 | 27 |

PlantDoc is a custom external-only pool. Original train/test folder names are preserved, but none of these selected images is used for our training or threshold selection. This is not a reproduction of the paper's benchmark split.

## Additional cases
- 180 unsupported leaves: 60 apple healthy, 60 potato healthy and 60 tomato Septoria images. Grouped division gives 89 OOD-validation and 91 OOD-test images. This small controlled-background set is a limited unfamiliar-input challenge.
- 90 synthetic degraded images: blur, darkening and low resolution, derived from 15 validation and 15 test parents. Their parent partitions and transformations are saved. They are not new biological observations.
- 24 synthetic non-leaf geometry images, divided 12/12, are software rejection fixtures. They are not a natural non-leaf benchmark. Natural non-leaf photographs remain a later evaluation addition.

## Checks performed
All 4,942 selected original files downloaded successfully, matched the source Git blob hashes and decoded without errors. Their source size is approximately 181.7 MiB.

The audit found 14 excess byte-identical files and 15 excess decoded-pixel-identical files. These overlap and must not be added together. Fifteen repeated pixel copies were excluded, with originals preserved on disk.

Perceptual-hash screening found 84 candidate pairs at Hamming distance up to 6, including horizontal-mirror comparisons. Eleven cross-label or cross-source candidates were visually inspected. Ten were different photos with similar overall shape and were retained. One pair showed the same scene labelled both early and late blight; both files were quarantined. The remaining candidate relations are conservatively kept within the same partition. The full candidate and decision records are saved.

All 262 external thumbnails and a 36-image benchmark sample were visually screened. Twenty-four external images were quarantined for clear format/content issues or uncertain crop/healthy labels. Examples include charts, composites, insufficient leaf detail and suspicious healthy-labelled leaves. No disease labels were silently changed. Visual screening is not expert pathology confirmation.

Final exclusions are 41 originals: 15 duplicate copies, 2 conflicting-label files and 24 visual exclusions. The retained original-image total is 4,901: 4,486 main benchmark, 235 external and 180 unsupported leaves.

## Leaf identities and split checks
Known source leaf metadata matched 2,918 of the 4,500 supported PlantVillage images. The remaining 1,582 have no matched leaf ID in this audit. Known leaf identities and accepted duplicate relations stay together. The retained benchmark contains 2,248 computational groups; these are not 2,248 independently verified plants.

Assertions passed for separation of file hashes, decoded-pixel hashes, known leaf identities and accepted near-duplicate groups across partitions. Saved decisions remove visually rejected false matches from these relations. Missing plant/session identities and imperfect similarity screening limit biological independence claims. Complete field generalisation has not been established.

No augmentation was used to increase the benchmark before splitting. Derived quality cases preserve the parent partition. Model loaders must use the CSV lists and must not scan all files in a directory, because excluded originals remain on disk.

## Sources and version records
**PlantVillage:** https://github.com/spMohanty/PlantVillage-Dataset

Pinned commit: 7f7ecc7e1eaca78107e3affe7cb5abd9427e139a

The author repository's saved README_HF.md declares CC BY-SA 3.0. Source metadata and attribution are retained.

**PlantDoc:** https://github.com/pratikkayal/PlantDoc-Dataset

Pinned commit: 5467f6012d78d1c446145d5f582da6096f852ae8

The repository contains a CC BY 4.0 licence. Its web-collected images include some stock marks; the repository declaration does not individually verify every original owner's permission. Keep this as an attributed academic benchmark and review rights separately before commercial redistribution.

Both snapshots were retrieved on 12 September 2026. The manifest records original names, source URLs, blob hashes, SHA-256, dimensions, labels and original split names. Six source filenames contained Windows-reserved characters. Their safe local names changed, while their source names, contents and URLs remained recorded.

## Frozen split fingerprint
69377f2755d001fe734c4b60d8ebba22d80b82840f0ad1882a069f87c8ce19c4

This identifies image IDs, file hashes, partitions and groups. Every later run must record it. Data changes require a new release/version with a reason.

## Files to use
- manifest.csv: complete decoded-file audit.
- train.csv, validation.csv, test.csv: main image-model lists.
- external_test.csv, ood_validation.csv, ood_test.csv: separate evaluation lists.
- excluded.csv: originals present on disk but not used.
- quality_cases.csv and nonleaf_fixtures.csv: explicitly synthetic fixtures.
- data/sources/visual_review.csv and pair_review.csv: visual decisions.
- tools/data/download.py, audit.py and verify.py: preparation and checks.

Data preparation is complete for the first benchmark. Expert relabelling, new local photos, paired sensor data and prospective field testing remain future work.


---

# R1 - Controlled images and the external-image gap

**Paper:** Mohanty, Hughes and Salathe (2016), *Using Deep Learning for Image-Based Plant Disease Detection*. Frontiers in Plant Science 7:1419. DOI: https://doi.org/10.3389/fpls.2016.01419
**Reading record:** Full paper downloaded and examined, including methods, results, Table 1 and discussion. The findings below are published results, not my model results.

## Problem and previous work
The paper asks whether a deep image model can identify crop species and disease from leaf photographs. Earlier systems often needed hand-designed colour, shape or texture features. This study tests learning the visual features directly from images.

## Data and method
The authors used 54,306 PlantVillage images covering 38 crop-condition categories from 14 crops. They compared AlexNet and GoogLeNet, training from scratch and transfer learning, and colour, grayscale and segmented images. Images were resized to 256 by 256 pixels. Five training/test proportions, from 20/80 to 80/20, were investigated. The methods keep different views of the same leaf in the same partition. Training lasted 30 epochs; the paper describes SGD and reports precision, recall, F1 and overall accuracy.

Transfer learning means starting with a network that has already learnt general visual features. Segmentation here removes the background; it does not automatically provide a lesion-severity measurement. The many experiment combinations help distinguish the influence of the architecture, image representation and training-set size.

## Reported results and their context
The best colour/transfer-learning GoogLeNet configuration at 80/20 achieved 99.35% accuracy and about 0.9934 mean F1 (Table 1). On two separately collected external sets of 121 and 119 images, the best configurations reached only 31.40% and 31.69% accuracy respectively (results, page 7). These are different-condition, 38-class tests. They must not be compared directly with a future three-class tomato experiment as if the tasks were identical.

## Limitations and my assessment
The authors discuss controlled backgrounds, single leaves and reduced performance outside the source conditions. The external sets are small. A visual classification is also different from laboratory confirmation and cannot establish when infection began. The results show feasibility, but do not justify a promise of 99% field accuracy.

My main lesson is to examine what the test set actually represents. A random image split can be too easy if related views cross partitions. I will therefore use source leaf identities, duplicate groups and separate external images. I will report macro-F1 and per-class recall alongside accuracy because class sizes differ.

## Connection to PlantGuard
I will use only the original colour tomato images for the first benchmark. Healthy, early blight and late blight form the three supported labels. The four selected modern architectures will share the same frozen split. I will not add grayscale or segmented copies of the same photograph as independent samples. The proposed contribution is an evaluated reliability workflow around classification, not the invention of leaf-image classification.

**Guide answer:** This paper showed that CNN classification works well on controlled images, but performance dropped on different photos. My evaluation will therefore include both an internal test and a separate external test.

**Locations to revisit:** Methods pages 2-4; Table 1 and external results page 7; limitations pages 8-9.


---

# R2 - PlantDoc and less controlled images

**Paper:** Singh, Jain, Jain, Kayal, Kumawat and Batra (2020; preprint 2019), *PlantDoc: A Dataset for Visual Plant Disease Detection*. CODS-COMAD, pp. 249-253. DOI: https://doi.org/10.1145/3371158.3371196 ; full text: https://arxiv.org/html/1911.10317
**Reading record:** Full paper, benchmark tables and limitations examined; PDF saved locally.

## Problem and data
PlantDoc addresses the lack of labelled plant photos taken outside a controlled laboratory background. The authors collected about 20,900 candidate internet images and filtered them to 2,598 images across 13 species and 27 healthy/disease categories. The annotation process involved about 300 human hours. Two people checked images using metadata and symptom guidance. The authors also annotated bounding boxes and describe 9,216 cropped leaf regions.

The distinction between original photos, annotated boxes and cropped classification files matters. The current classification repository describes itself as Cropped-PlantDoc, but its local file count must be measured rather than assumed to equal the paper's 9,216 boxes. Our download manifest records the exact repository snapshot and selected files.

## Method and evaluation
The paper compares VGG16, InceptionV3 and InceptionResNetV2 with ImageNet initialisation, PlantVillage training, and PlantVillage followed by PlantDoc fine-tuning. Classification experiments use an 80/20 division and 100 by 100 pixel inputs. SGD uses momentum 0.9 and learning rate 0.001. Detection experiments use MobileNet and Faster R-CNN; the stated detection split is 2,360/238. Classification accuracy and detection mAP are different measures.

## Reported results
In Table 1, VGG16 trained on PlantVillage achieved 15.08% on uncropped PlantDoc; PlantVillage pretraining followed by PlantDoc fine-tuning reached 29.73%. In Table 2, InceptionResNetV2 reached 39.87% when trained on PlantVillage and evaluated on cropped PlantDoc, compared with 70.53% after PlantDoc fine-tuning. Their difference is 30.66 percentage points. It should not be loosely described as a guaranteed 31% improvement for every model or dataset. Table 3 reports the best detection mAP at IoU 0.5 as 38.9, a different task from classification.

## Limitations and my assessment
The authors acknowledge possible labelling mistakes and small class sizes. Web images can contain watermarks, multiple leaves, mixed symptoms and misleading website labels. Related crops of one original photo can also make an image-level split optimistic unless grouped. A web-collected external set tests a different image source; it is not the same as a prospective GNDU greenhouse trial.

I will keep the selected PlantDoc tomato images entirely outside training and threshold selection for the first experiment. I will preserve the original train/test folder names as provenance, but combine their compatible selected files into our external-only evaluation pool. This is a custom external test, not reproduction of the published PlantDoc split or score. Obvious unsuitable images will be excluded with reasons; uncertain disease labels will not be silently corrected without expert evidence.

## Connection to PlantGuard
The repository supplies selected tomato healthy, early-blight and late-blight examples. I will audit them for decode errors, exact and likely near duplicates, overlap with PlantVillage, and obvious image-content issues. The final external count may be lower than the download count. I will present errors and uncertainty, not just a single favourable score.

**Guide answer:** PlantDoc helps me test whether a model trained on clean images also handles more varied photos. Its labels and image quality have limitations, so I have kept its audit and results separate.

**Locations to revisit:** Sections 3.1 and 4; Tables 1-3; Section 7.


---

# R3 - Image and sensor fusion in peach disease analysis

**Paper:** Chen et al. (2024), *Integration of Image and Sensor Data for Improved Disease Detection in Peach Trees Using Deep Learning Techniques*. Agriculture 14(6):797. DOI: https://doi.org/10.3390/agriculture14060797
**Reading record:** The 31-page primary PDF was examined, with attention to collection, alignment, cross-validation, comparison tables and limitations.

## Problem and data
The study aims to recognise peach diseases and segment lesions when visual differences are subtle and some photographs have no accompanying sensor data. Images came from university/garden collection and internet sources during autumn 2023 to spring 2024. Environmental variables include temperature, humidity, light and CO2.

The text describes approximately 10,000 images across ten conditions. Adding the ten class counts in Table 1 gives 8,880. I will record this difference as a detail requiring clarification if reproducing the work. The source data are available on request; no complete paired dataset has been downloaded for PlantGuard. These are peach conditions, not our three tomato labels.

## Method and split
The framework contains tiny-feature attention, an aligned-head module, a Transformer segmentation branch and alignment loss. For a photo with no sensor record, the aligned-head predicts sensor information from visual features. This is learned estimation, not a physical measurement. The paper describes CutOut, CutMix and Mixup augmentation, batch size 32, Adam with initial learning rate 0.0001 and random five-fold cross-validation (Sections 3.3-3.5).

Five-fold evaluation means each fold is held out in turn. For this kind of mixed-source dataset, I would also want to know whether images of the same plant, collection session or augmented parent remain in one fold. That grouping is not made clear enough in the examined method to reproduce an independent-site test.

## Reported results
Table 2 reports 0.94 precision, 0.92 recall and 0.92 accuracy for the proposed disease model, compared with 0.90 accuracy for EfficientNet. Table 3 reports 0.94 mIoU for segmentation, compared with 0.90 for UNet++. Table 4 compares cross-entropy, focal and alignment losses; the proposed disease result is 0.92 accuracy versus 0.90 with focal loss. Table 5 separately reports a 0.94 PlantDoc accuracy. That figure is not directly comparable to R2 without an identical task, split and training protocol.

## Limitations and my assessment
The authors identify class imbalance, variable web-image quality, model complexity and regional generalisation as limitations. A predicted sensor vector needs its own error assessment against held-out physical readings. Good disease accuracy does not by itself prove that estimated temperature or humidity is correct. Similarly, mIoU measures a segmentation mask, not validated biological severity or disease lead time.

The paper is useful evidence that multimodal fusion and missing-modality handling are already studied. My project should not call their basic combination new. For a reproducible comparison I would need the paired raw data, exact fold membership, missingness settings, code and sensor-estimation errors.

## Connection to PlantGuard
I will first implement reliable image-only inference and separate environmental monitoring. If a sensor is unavailable, its value will remain missing. I will not assign random readings to PlantVillage images or treat image-derived values as real observations. A later fusion experiment needs genuinely matched zone/time records and verified labels. Our initial contribution will be a measured comparison of reliability policies under bad images and missing information, with a modest two-node demonstration.

**Guide answer:** Fusion is established previous work. I am studying how a small prototype should behave when its inputs are incomplete, while keeping measurements and estimates distinguishable.

**Locations to revisit:** Table 1 page 8; aligned-head pages 14-15; training pages 17-18; Tables 2-5 pages 21-26; limitations pages 27-28.


---

# R4 - Time-aligned tomato late-blight risk research

**Paper:** Gao et al. (2026), *Environmental-Visual Fusion for Proactive Tomato Late Blight Management in Protected Horticulture*. Horticulturae 12(3):299. DOI: https://doi.org/10.3390/horticulturae12030299
**Reading record:** The 28-page primary PDF was examined, including collection, temporal separation, architecture, main results, ablation and limitations.

## Problem and data
The study asks whether environmental history and visual symptoms can support earlier tomato late-blight warning in a greenhouse. Data were collected in Bayannur, Inner Mongolia, during November 2023 to March 2024. Table 1 reports 18,600 images and 172,800 records for each of four minute-sampled environmental variables: air temperature, relative humidity, leaf wetness and light. Labels cover healthy, potential-risk and symptomatic stages. These are not the same labels as healthy, early blight and late blight: early blight is a separate disease name, not an early stage of late blight.

## Method and split
The environmental branch processes a 24-hour history. A hierarchical visual Transformer extracts image features. Temporal and visual representations are aligned and fused with attention to produce risk scores, followed by greenhouse-control mapping. Section 4.1 describes a chronological 70/15/15 split with a 24-hour buffer between partitions and time-series cross-validation. Training uses 224-pixel images, AdamW, batch size 32, up to 200 epochs and early-stopping patience 20. This is a substantially larger collection and compute setup than two college pots.

## Reported results
Table 2 reports 0.952 accuracy, 0.944 F1, 0.975 AUC and 21.6 hours of risk lead time for the full system. Its vision-only ResNet50 baseline reports 0.914 accuracy and 5.6 hours. Table 5 reports that removing temporal modelling reduces lead time to 8.0 hours. Removing control mapping leaves prediction metrics unchanged, so control benefit and predictive accuracy must be analysed separately. These are the authors' greenhouse results; PlantGuard has not reproduced them.

## Limitations and my assessment
The paper acknowledges one greenhouse and one production cycle, dependence on sensor continuity, and the need for wider validation. Potential-risk labels partly use environmental risk analysis. For an independent early-warning claim, I would check that the labels are confirmed by later disease events rather than simply reproducing rules derived from the same input readings.

The stated 172,800 minute records correspond to 120 days of uninterrupted sampling; the calendar collection window spans about five months. Missing periods, selected intervals and effective sample counts would need clarification before reproduction. I would also record the number of independent outbreaks, class counts, alert threshold, false-alert definition and exactly how future outcomes were confirmed. A temporal gap is helpful, but preprocessing must remain causal: future readings must not be used to interpolate a real-time input. The paper's descriptive collection and data-availability statement do not give us a directly usable paired download in this phase.

## Connection to PlantGuard
This paper supports keeping sensor timestamps, missingness and history in the design. It does not allow us to claim advance warning from a folder of still leaf photos. I will use the public images for current-condition classification. Later, if enough independent time-labelled disease events are available, I can define a forecasting horizon and use chronological splits with a suitable gap. Until then, environmental readings provide monitoring context and any rule-based alert will be named accordingly.

Our college and market compute decisions stay unchanged: laptop first, VPS/cloud later. The paper's greenhouse-control system is not a reason to add a field AI box or automatic sprayer to the current scope.

**Guide answer:** Diagnosis asks what the image shows now. Forecasting asks what will happen later and needs outcome-labelled history. I will finish the diagnosis benchmark first and keep forecasting conditional on suitable data.

**Locations to revisit:** collection/Table 1 pages 5-6; architecture pages 7-11; split page 12; Table 2 page 14; Table 5 page 20; limitations pages 21-23.
