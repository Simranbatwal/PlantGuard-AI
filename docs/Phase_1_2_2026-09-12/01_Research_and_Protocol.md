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
