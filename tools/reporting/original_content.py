from pathlib import Path

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'output/pdf/PlantGuard_Guide_Pack_2026-09-08'
MASTER=BASE/'output/PlantGuard_Master_Plan'
TITLE='AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN'
STUDENT='Simran Batwal'
ROLL='28452500003'
GUIDE='Dr. Anil Kumar'
INSTITUTE='Guru Nanak Dev University, Amritsar'
DETAILS='M.Tech | Computer Science | 3rd Semester'
DATE='8 September 2026'

SOURCES=[
('R1','S. P. Mohanty, D. P. Hughes and M. Salathe (2016). Using Deep Learning for Image-Based Plant Disease Detection. Frontiers in Plant Science, 7:1419.','https://doi.org/10.3389/fpls.2016.01419'),
('R2','D. Singh et al. (2020; preprint 2019). PlantDoc: A Dataset for Visual Plant Disease Detection. CODS-COMAD.','https://arxiv.org/abs/1911.10317'),
('R3','K. Chen et al. (2024). Integration of Image and Sensor Data for Improved Disease Detection in Peach Trees Using Deep Learning Techniques. Agriculture, 14(6):797.','https://doi.org/10.3390/agriculture14060797'),
('R4','P. Gao et al. (2026). Environmental-Visual Fusion for Proactive Tomato Late Blight Management in Protected Horticulture. Horticulturae, 12(3):299.','https://doi.org/10.3390/horticulturae12030299'),
('R5','T. Wei, Z. Chen, Z. Huang and X. Yu (2024). Benchmarking In-the-Wild Multimodal Disease Recognition and A Versatile Baseline. ACM Multimedia.','https://arxiv.org/abs/2408.03120'),
('R6','J. Dong, H. Zhou, A. Fuentes, S. Yoon and D. S. Park (2025). Enhancing anomaly detection in plant disease recognition with knowledge ensemble. Frontiers in Plant Science, 16:1623907.','https://doi.org/10.3389/fpls.2025.1623907'),
('R7','B. Wang (2024, volume 14/2023). Zero-exemplar deep continual learning for crop disease recognition: a study of total variation attention regularization in vision transformers. Frontiers in Plant Science.','https://doi.org/10.3389/fpls.2023.1283055'),
('R8','J. Ding, Y. Qiao and L. Zhang (2023). Plant disease prescription recommendation based on electronic medical records and sentence embedding retrieval. Plant Methods, 19:91.','https://doi.org/10.1186/s13007-023-01070-6'),
('D1','PlantVillage public dataset repository. Verify the selected files, source, labels and licence before use.','https://github.com/spMohanty/PlantVillage-Dataset'),
('D2','PlantDoc dataset repository. Web-collected plant images; maintain source-level separation.','https://github.com/pratikkayal/PlantDoc-Dataset'),
('D3','PlantWild project and dataset terms. Its image-text multimodality differs from environmental sensor fusion.','https://tqwei05.github.io/PlantWild/'),
('H1','Espressif. ESP32-DevKitC V4 hardware reference, interfaces and board power options.','https://docs.espressif.com/projects/esp-idf/en/stable/esp32/hw-reference/esp32/get-started-devkitc.html'),
('H2','DFRobot. SEN0193 capacitive soil moisture sensor reference.','https://wiki.dfrobot.com/Capacitive_Soil_Moisture_Sensor_SKU_SEN0193'),
('H3','Adafruit. SHT31-D temperature and humidity sensor breakout reference.','https://www.adafruit.com/product/2857'),
('H4','Renke. Leaf-wetness sensor family; obtain a variant-specific quotation and RS485 manual.','https://www.renkeer.com/product/leaf-wetness-sensor/'),
('H5','Analog Devices. MAX3483/MAX3485 family, 3.3 V RS485 transceivers.','https://www.analog.com/en/products/max3485.html'),
('H6','Adafruit. BH1750 light sensor reference.','https://www.adafruit.com/product/4681'),
]

BOM=[
('ESP32 DevKitC V4 / WROOM-32E, matched pair',2,600,'Core'),
('Capacitive soil-moisture probe, SEN0193 class',2,350,'Core'),
('SHT31 temperature / humidity breakout',2,450,'Core'),
('Artificial leaf-wetness plate, RS485 variant',2,3500,'Quote required'),
('3.3 V MAX3485 RS485 interface module',2,300,'Core'),
('BH1750 lux sensor',2,150,'Optional'),
('Breadboard / prototype base',2,200,'Core'),
('Mixed jumpers and insulated hookup wire, lot',1,400,'Core'),
('USB data cable matched to purchased board',2,150,'Core'),
('Regulated supplies and distribution, lot',1,600,'Core'),
('Gasketed prototype enclosure',2,350,'Core'),
('Glands, terminals, fuse and standoffs, lot',1,500,'Core'),
('USB webcam with usable close focus',1,1500,'If needed'),
('Camera / sensor stands and air shields, lot',1,800,'Core'),
('Tomato seedlings, similar compact cultivar',2,150,'Core'),
('10-15 L pot with drainage tray',2,300,'Core'),
('Consistent potting medium, lot',1,500,'Core'),
('Plant stakes, labels and soft ties, lot',1,250,'Core'),
('Spare connectors and assembly consumables',1,600,'Core'),
]

REPORT=[]
def report(title,text): REPORT.append((title,text.strip()))

report('Review purpose and present status', '''
## Purpose of this submission
This initial-stage report presents the proposed college prototype, research direction, hardware requirements and validation plan for PlantGuard. It is intended for discussion with the project guide before implementation begins. The exact academic title is: **AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN**.

PlantGuard will combine close-up leaf photographs with measurements of the plant environment. Two wireless sensor nodes will send readings to an existing laptop, which will run the AI models, store data and display evidence on a local dashboard.

| Activity | Status at this review |
| Topic selection and guide discussion | Undertaken; scope still open to guide feedback |
| Initial system planning | Undertaken; this report records the proposed approach |
| Research-paper reading | Some preliminary reading reported; detailed paper notes are still to be completed |
| Literature briefs in this pack | Prepared for discussion; not a claim that every paper has been fully studied by the student |
| Dataset acquisition and audit | Planned; no completed download is claimed |
| Coding, model training and experiments | Not started; planned after scope review |
| Hardware procurement and assembly | Proposed; subject to availability and institutional approval |

## Decisions requested from the guide
Confirm the primary research question, the tomato-first experimental scope, the model comparisons and the two-node hardware setup. Advise on access to plant-disease expertise, data collection, the review schedule and any departmental report format.

The project is at an initial planning review. The next phase will establish a dated work log, verified data inventory and reproducible implementation. No performance results, completed experiments or approvals are implied.
''')

report('Abstract and problem definition', '''
## Proposed abstract
Plant disease recognition from photographs is useful, but image quality, unseen conditions and changes in field appearance can make predictions unreliable. Environmental measurements provide additional context, although a sensor reading alone does not establish a disease diagnosis. PlantGuard proposes a college-scale system that brings these sources together while retaining their limitations.

Two ESP32-based wireless sensor nodes will monitor soil-moisture response, air temperature, relative humidity and leaf-surface wetness around two tomato plants. A phone or USB camera will provide close-up leaf images. A laptop will perform image inference, maintain time-stamped sensor records, assess input quality and present the resulting evidence. The system will distinguish a current visual finding from an environmental risk indicator and will request another observation when evidence is inadequate.

The proposed experimental work will compare four image-model families, examine performance on data from different capture conditions and evaluate the effect of missing or degraded inputs. A focused research extension will investigate whether quality-aware fusion and a bounded rescan policy improve decision reliability at a reasonable sensing cost. Supervised disease forecasting will be attempted only if suitable independent time-labelled disease events are available.

Expected outputs include a reproducible image benchmark, a two-node wireless prototype, a local dashboard, a labelled data log and an evaluation report. This submission describes the plan; it does not report a completed system or measured accuracy.

## Problem statement
How can a resource-conscious college prototype combine image and environmental evidence without presenting uncertain, stale or faulty measurements as a reliable disease diagnosis?

## Why the problem matters
Controlled-dataset accuracy can overstate performance on unfamiliar images [R1, R2]. Image-sensor integration already appears in published research [R3, R4]. Therefore, PlantGuard should demonstrate reliable behaviour under practical input limitations and substantiate any improvement through controlled comparisons.
''')

report('Objectives and manageable scope', '''
| Objective | Proposed evidence of completion |
| Monitor two plant zones wirelessly | Independent node IDs; time-stamped readings visible on one laptop |
| Compare four vision approaches | Same documented data split; per-class and overall metrics; compute cost |
| Handle uncertain inputs | Unknown / low-quality output and rescan flow tested on held-out examples |
| Integrate contextual evidence | Image and sensor history aligned by plant, zone and capture time |
| Evaluate robustness | Missing readings, noisy inputs and network interruption tests |
| Support reviewable advice | Management record with source, crop, condition and review date |

## Core college deliverable
Use **tomato** for the physical setup and first integrated classification task: healthy, early blight and late blight, plus rejection of unsupported or inadequate inputs. These image labels do not mean that all conditions will be grown experimentally in the two pots. The pots primarily demonstrate monitoring and data integration.

Compare MobileNetV3 Large, ResNet50, EfficientNet-B0 and a small pretrained ViT configuration under a common protocol. Select one deployment model using validation performance, calibration and laptop inference cost. Four comparisons do not require all four models to run simultaneously in the final demonstration.

## Data-dependent extensions
The wider project vision includes potato, maize, apple, grape, pepper and rice as additional image domains. Keep a dataset feasibility matrix for these crops; add them only after the tomato pipeline is stable and the guide agrees. Field validation across seven crops is not promised by a two-pot study.

Severity segmentation, learned risk forecasting, GRU/LSTM comparisons and continual learning require suitable labels or historical events. They are candidate extensions, not unconditional prototype commitments. Automatic irrigation, chemical spraying, solar power and a dedicated AI computer are outside the proposed college build.
''')

report('College architecture and information flow', '''
@diagram college
Figure 1. Proposed local college architecture. Arrows represent information flow, not a circuit wiring diagram.

## How one observation moves through the system
1. The sensors measure their local environment. Each ESP32 adds its node identity and measurement status.
2. Node A and Node B send telemetry over the same Wi-Fi network. USB connections may supply power or support debugging; the final sensor-data path remains wireless.
3. The laptop checks incoming records, stores them and flags missing or implausible values.
4. The student captures a close-up leaf photo and selects the crop, plant and zone. The capture time is recorded.
5. A model processes the image. The application retrieves only relevant sensor history from that same zone and time window.
6. The dashboard shows the visual result, input quality, environmental context, uncertainty and a reviewable next action.

An existing access point provides connectivity; an internet connection is not required for the local demonstration after dependencies and model files are installed. A phone hotspot is usable only after checking that it permits device-to-device communication.

The laptop is the processing platform. The ESP32 is the sensing and communication controller. An optional communication gateway is unnecessary for the first two-node Wi-Fi prototype.
''')

report('Physical setup and placement', '''
@setup
Figure 2. Proposed two-pot setup, drawn schematically. Identical components are used in both zones.

| Part of setup | Placement and purpose |
| Two tomato plants | Similar compact cultivar and growth stage; separate labelled 10-15 L pots with drainage trays |
| Soil probe | In representative root-zone medium; record insertion depth and distance from pot wall |
| SHT31 air sensor | Near canopy in a ventilated radiation shield, away from direct spray and electronics heat |
| Artificial leaf-wetness plate | On its own support near representative foliage; use the manufacturer orientation and record it |
| Camera | Stable stand with repeatable distance, sufficient focus and diffuse illumination |
| ESP32 and wiring | Protected above tray level with strain relief and separated wet / dry areas |

The wetness plate is a proxy surface near the canopy; it is not a clip that must be attached to every leaf. The two pots are two measurement locations, not two statistically adequate disease-treatment groups.

Keep a simple care log: watering time and amount, visible plant condition, light changes, sensor movement and maintenance. Avoid introducing pathogens for a classroom demo. Use appropriately sourced labelled photographs for disease examples; any biological experiment needs a separately reviewed protocol and expertise.
''')

report('Controller and sensor selection', '''
@photos esp32 soil sht31
| Component | Preferred choice and reason |
| Controller | Two matching ESP32 DevKitC V4 boards with ESP32-WROOM-32E modules; integrated Wi-Fi and adequate interfaces [H1] |
| Soil measurement | Capacitive SEN0193-class probe; use calibration and record raw ADC as well as a relative index [H2] |
| Air conditions | SHT31 I2C breakout, preferred over a basic DHT22 for the planned build; protect the sensing element [H3] |

## Why ESP32 rather than a separate Arduino Uno
ESP32 provides the controller and Wi-Fi on one development board. It can be programmed in C++ using the Arduino framework. “Arduino” can refer to a software framework or a board family; using that framework does not require buying an Arduino Uno as well.

Check the exact purchased board before wiring. A generic ESP32 label does not guarantee the same connector, pin layout or module. Reference photographs identify component families; the quotation must identify the actual variant and included accessories.

## What the readings mean
The low-cost soil probe reports an electrical response influenced by the growing medium. A calibrated relative wetness index is suitable for this prototype; it must not be labelled volumetric water content without appropriate calibration. SHT31 measures local air temperature and relative humidity, not the temperature or water content of the leaf itself.
''')

report('Wetness, imaging and assembly choices', '''
@photos leaf bh1750 enclosure
## Leaf-wetness sensor
Use a genuine artificial leaf-wetness plate from a documented RS485 Modbus variant, such as the Renke RS-WS-*-YM-1-T family. Confirm the exact suffix, supply range, register map, cable and output units before ordering. A 3.3 V MAX3485 interface is budgeted between this sensor and each ESP32. A common 5 V MAX485 board is not an automatic substitute [H4, H5].

Leaf wetness adds information about moisture on a proxy surface. Humid air does not guarantee a wet leaf. Do not substitute an exposed rain-detection PCB and describe it as a calibrated leaf-wetness instrument. If the proper plate exceeds budget, record its omission and narrow the experiment.

## Camera and light
Start with an available smartphone or laptop camera. Purchase the budgeted USB webcam only if the available camera cannot focus adequately on a leaf. Compare sample images before purchase: sharpness, exposure, minimum focus distance, colour consistency and mounting matter more than the “1080p” label alone.

BH1750 is an optional light-context sensor [H6]. It measures illuminance in lux, not photosynthetically active radiation. It is not required for the first minimum working prototype.

## Practical accessories
Budget for data-capable USB cables, breadboards, insulated wires, terminals, regulated supplies, fuse protection, standoffs, glands, sensor shields, a camera stand, pots, trays and plant labels. Borrow a multimeter and soldering tools where available. Enclosure selection must accommodate wiring and ventilation; the assembled prototype is not automatically certified weatherproof.
''')

report('Interfaces and calibration plan', '''
| Function | Provisional interface on classic ESP32 DevKitC |
| SHT31 and optional BH1750 | I2C; candidate SDA GPIO21 and SCL GPIO22; verify breakout pull-ups at 3.3 V |
| Capacitive soil probe | ADC1 input, candidate GPIO34; verify the output stays within the selected ADC range |
| RS485 transceiver | UART, candidate RX GPIO16 / TX GPIO17, direction GPIO25; verify board availability |
| Power | Board through a verified USB supply; separate matched sensor supply where required |

These pin choices are a design starting point for the classic WROOM-32E board, not universal wiring instructions. Review the exact modules and sensor manuals before energising the circuit. ADC1 is chosen for soil sampling to avoid classic ESP32 ADC2/Wi-Fi resource conflicts.

## Calibration and commissioning sequence
1. Inspect part markings and supplies with a multimeter. Check polarity, common signal reference and logic voltage compatibility.
2. Read one sensor at a time before assembling the full node. Store raw readings and the sensor/model identifier.
3. Calibrate the soil response in the actual medium using repeatable reference states. Keep calibration coefficients versioned per probe.
4. Co-locate the two air sensors and compare stable readings. Record differences; use a reference instrument if available.
5. Check dry and uniformly wetted plate response according to its manual. Select a wet/dry threshold only from this evidence and retain the raw output.
6. Verify serial/register settings, then run both nodes continuously. Record gaps, resets and disagreement between co-located sensors.

A low-cost calibrated prototype supports comparative measurements. It does not establish laboratory-grade accuracy, absolute water content or a universal disease threshold.
''')

report('Literature review 1: image generalisation', '''
## R1. Mohanty, Hughes and Salathe (2016)
**Method and evidence.** The study trained deep image classifiers using 54,306 controlled leaf images across 14 crops. It reported 99.35% held-out accuracy under its dataset conditions. Performance on differently sourced images was much lower, just above 31% in the paper's external test.

**Critical reading.** The difference between internal and external performance is more informative for PlantGuard than the high headline accuracy. Background and capture conditions can become shortcuts. These are the paper's results, not results obtained in this project.

**Design implication.** Maintain a clean internal test set and a separate external-condition evaluation. Record where images came from and prevent related images crossing the split [R1].

## R2. Singh et al. (2020)
**Method and evidence.** PlantDoc introduced a web-collected, non-laboratory dataset with 2,598 data points spanning 13 plant species and up to 17 disease classes. Its focus is the practical difficulty of recognising disease beyond clean laboratory images.

**Critical reading.** This is a comparatively small and heterogeneous dataset. Image provenance, labels and repeated sources need auditing. Web collection is not the same as a prospectively controlled local field study.

**Design implication.** Use supported tomato classes as an external challenge set after verifying label compatibility. Do not attach invented environmental readings to these images [R2].

## Questions to take into full reading
Which split unit was used? How were duplicates handled? Which classes are comparable across datasets? What changes between the training environment and the external evaluation? Record answers in the paper-reading tracker before making stronger claims.
''')

report('Literature review 2: image-sensor fusion', '''
## R3. Chen et al. (2024)
**Method and evidence.** The peach-tree study combines image and sensor features for disease recognition and segmentation. It introduces an alignment mechanism to bring different feature representations together before using their combined information.

**Critical reading.** A successful crop-specific study does not automatically transfer to tomato or to inexpensive sensors. For a reproducible comparison, inspect how samples were aligned, which modalities were removed in ablations and how independent evaluation data were separated.

**Design implication.** Image-plus-sensor fusion is established prior work. PlantGuard's contribution must be narrower and experimentally demonstrated, such as behaviour under poor-quality or missing inputs [R3].

## R4. Gao et al. (2026)
**Method and evidence.** This protected-horticulture study combines tomato leaf images with environmental time series and links risk estimates to greenhouse control. The authors report approximately 0.95 accuracy and more than 20 hours of warning in their study setting.

**Critical reading.** Their measurements arise from a real greenhouse dataset and a specific experimental protocol. The same lead time cannot be promised from two college pots. Before adopting the method, examine event labels, time splits and what information is available before disease onset.

**Design implication.** Use the study to distinguish current diagnosis from prospective forecasting and to motivate time-aligned data collection. Do not claim early warning until it is measured on independent future events [R4].

## Proposed review outcome
Ask the guide whether the thesis should prioritise reliability-aware diagnosis or forecasting. The first is feasible with controlled quality tests; the second depends on obtaining a sufficiently informative longitudinal disease dataset.
''')

report('Literature review 3: unfamiliar conditions', '''
## R5. Wei et al. (2024)
**Method and evidence.** PlantWild addresses disease recognition in varied real-world imagery and introduces a multimodal baseline using image and text information. It studies the difficulty of distinguishing similar diseases under diverse appearance conditions.

**Critical reading.** Image-text multimodality is different from image-environmental-sensor fusion. Dataset versions and licence terms must be tracked; the project lists non-commercial terms that require separate consideration for any later product use.

**Design implication.** Use this work as a reference for domain variation and dataset auditing. Include only compatible classes and permitted data in a college experiment [R5, D3].

## R6. Dong et al. (2025)
**Method and evidence.** The paper studies anomaly detection in plant-disease recognition with a knowledge ensemble, combining general pretrained knowledge and task-adapted knowledge. It evaluates unfamiliar conditions rather than treating every image as a known class.

**Critical reading.** Known-class accuracy and unknown-input detection measure different capabilities. An unknown detector may reject legitimate examples, so its threshold needs a separate validation protocol.

**Design implication.** Add unsupported-condition and inadequate-image outcomes. Compare rejection behaviour against a simple validation-tuned confidence baseline, using an untouched unknown test set [R6].

## What will be tested in PlantGuard
Challenge examples may include the wrong crop, a non-leaf object, severe blur, overexposure and a disease outside the supported classes. Keep data-quality rejection separate from biological novelty; an out-of-focus photograph is not evidence of a new disease.
''')

report('Literature review 4: updates and advice', '''
## R7. Wang (2024)
**Method and evidence.** This study explores zero-exemplar continual learning for crop-disease recognition with a vision transformer and total-variation attention regularisation. It addresses loss of earlier knowledge when a model learns new disease tasks.

**Critical reading.** Continual-learning evaluation must measure both retained old-task performance and new-task performance. “Improving over time” cannot be assumed from simply retraining on fresh images.

**Design implication.** Archive newly collected examples for expert review. Any later model update should be versioned, tested and reversible. Automatic self-training from PlantGuard's own predictions is outside the initial prototype [R7].

## R8. Ding, Qiao and Zhang (2023)
**Method and evidence.** PRSER retrieves plant-disease prescriptions using sentence embeddings of plant electronic medical records. The approach uses existing records and semantic matching to support recommendation.

**Critical reading.** Historical records from one agricultural context are not automatically appropriate for a different crop, location or registered product label. Retrieval relevance alone does not establish treatment correctness.

**Design implication.** The college dashboard should present a small, expert-reviewed management knowledge base with traceable sources and review dates. It should not invent chemical products or doses [R8].

## Review status and next reading task
These are preliminary literature briefs prepared for this discussion. The student has reported some initial reading; full methods, supplementary material and reproducibility checks remain part of the work plan. No claim of an exhaustive systematic literature review is made.

Priority for the next meeting: complete full notes for R1, R2, R3 and R4, then explain in one minute what each changes in the proposed design.
''')

report('Research question and contribution', '''
## Primary proposed question
Does quality-aware use of environmental context, together with a bounded request for fresh evidence, improve the reliability of plant-health decisions compared with a fixed image-only or naive-fusion pipeline?

The proposed contribution is an evaluated decision policy under practical input limitations. It is not a claim that image classification, sensor networking, fusion, unknown detection or treatment retrieval is individually new.

| Comparison | What changes | What remains comparable |
| A. Image-only baseline | Photograph alone | Same eligible examples and class definition |
| B. Simple context baseline | Image plus available sensor summary | Same time / zone alignment and test cases |
| C. Quality-aware policy | Ignores stale / faulty context; permits abstention | Same trained vision model and evaluation set |
| D. Bounded evidence policy | Requests a rescan or short sampling burst | Same fixed budget and predeclared stopping rule |

## Conditions for a defensible study
For a learned fusion classifier, obtain genuinely paired images, sensor histories and independent labels. If those are insufficient, evaluate a rule-based evidence policy and clearly describe it as such. Synthetic fault injection can test software robustness; it cannot validate real biological disease prediction.

## Predeclared outcomes
Compare macro-F1, per-class recall, error among accepted predictions, fraction of cases accepted, unknown false acceptance, false alerts and extra observations requested. Measure end-to-end latency and data volume. Report trade-offs and failure cases, including no improvement if that is what the evidence shows.

The exact hypothesis, baselines and experiment size should be refined with the guide before model development. A small negative result with a sound protocol is more useful than an unsupported performance claim.
''')

report('Dataset acquisition and labelling', '''
| Data source | Planned role | Required check |
| PlantVillage [D1] | First controlled-image benchmark | Selected crop / class mapping, duplicates, source and licence |
| PlantDoc [D2] | External-condition evaluation | Compatible labels, source overlap and image quality |
| PlantWild [D3] | Optional additional domain challenge | Version, class overlap, permitted academic use |
| Own two-pot observations | Integration, quality and telemetry tests | Plant / zone IDs, capture time, care log and label provenance |
| Expert-supported longitudinal data | Optional fusion / forecast learning | Independent disease events, timing and expert labels |

## Acquisition steps after this review
Create a dataset manifest before training: dataset name, source URL, version or retrieval date, licence, file count, class mapping and exclusions. Download only the chosen subset, retain an unchanged raw copy and generate checksums. Dataset download is currently a planned task.

Split data before augmentation. Keep related images from the same plant, capture session or original source together. Detect exact and near duplicates. Use a held-out test set once the protocol is fixed; use validation data for model and threshold selection.

For own observations, link each image to a plant ID, zone ID, capture timestamp and recent sensor window. Do not assign local sensor values to unrelated public images. Annotate the basis of the label: expert confirmation, dataset label, uncertain visual observation or unlabelled example.

If the guide permits additional crops, create a crop-by-class feasibility table first. Report each dataset's coverage rather than implying that every disease exists for every crop.

Two pots can generate many correlated readings. Thousands of rows from those pots are not thousands of independent disease cases.
''')

report('Model and decision pipeline', '''
## Image-model workflow
Start from pretrained weights for MobileNetV3 Large, ResNet50, EfficientNet-B0 and a manageable ViT configuration. Use each model's documented input preprocessing, a common split and comparable tuning effort. Log seed, software versions, parameters and checkpoints. Use validation-based stopping and class-aware metrics.

The final deployment model is selected after comparison. Measure latency on the actual laptop; GPU training may use approved institutional resources if necessary. This proposal does not assume a new GPU purchase or guaranteed real-time speed.

## Environmental context and fusion
Start with transparent, reviewed rules and rolling sensor summaries. Preserve raw readings, missing-value flags and calibration versions. Separate a current image classification from an environmental risk indicator. A high-risk environment can coexist with a visually healthy leaf; these are not contradictory labels for the same target.

If sufficient paired labelled examples exist, compare simple late fusion and a compact feature-based model. RF/XGBoost are candidates for tabular summaries; GRU/LSTM become relevant only when enough independent, labelled sequences are available.

## Bounded adaptive evidence
An initial policy may request one better photo and, if necessary, a short higher-frequency sensor burst. Cap retries and time, log every request, and return “insufficient evidence” when the limit is reached. Compare the gain against additional user effort and sensor transmissions.

## Explanations and severity
A Grad-CAM-style heatmap can help inspect where a compatible CNN looks; it is not a verified lesion outline. A severity percentage needs lesion annotations, an appropriate segmentation method and validation. Until then, show the image and evidence without claiming a numeric diseased-area estimate.
''')

report('Software, records and dashboard', '''
| Layer | Proposed implementation |
| Node firmware | C++ with Arduino framework; sensor readout, reconnect, sequence number and health flags |
| Telemetry | Local Wi-Fi and MQTT; laptop broker; credentials and node-specific identity |
| Application | Python FastAPI service; validation, image intake and inference |
| Research | PyTorch, OpenCV and scikit-learn; XGBoost only if the experiment requires it |
| Storage | SQLite initially; separate original images and structured records |
| Dashboard | React with TypeScript; local browser interface |

## Minimum record structure
Each reading stores node ID, zone ID, sequence number, device time if valid, laptop receive time, measurement values, units, validity flags and calibration version. Each image stores image ID, plant ID, zone ID, capture time, crop, label provenance and permitted-use status. Each prediction stores model version, input references, confidence, rejection reason and decision-policy version.

Reject malformed records, detect duplicate transmissions and expose missing data. After a connection loss, show the last valid timestamp and an offline indicator; do not display old data as a current measurement. Keep local backups of raw data, manifests and experiment logs.

## Dashboard screens
1. Overview: two zone cards, current values, last contact and sensor-health state.
2. Scan: crop / plant selection, image capture or upload and image-quality feedback.
3. Evidence: image finding, environmental context and uncertainty shown separately.
4. History: time trends, gaps, image events and care-log entries.
5. Review: source-linked management notes and export of a dated observation report.

Any sample dashboard screenshot must be labelled illustrative until it shows a real measured run. Use explicit “demo data” tags for rehearsals that rely on prerecorded examples.
''')

report('Evaluation and acceptance criteria', '''
| Area | Proposed test and report |
| Image recognition | Macro-F1, per-class precision / recall, confusion matrix; internal and external results separately |
| Calibration / rejection | Reliability of confidence, accepted-case error versus coverage; unfamiliar-input false acceptance |
| Sensor and network | Co-location checks, calibration records, missing data rate, recovery after a deliberate disconnect |
| Context policy | Same cases across baselines; ablations for missing / stale / noisy sensor inputs |
| Adaptive observations | Change in accepted-case error versus number of rescans and extra transmissions |
| Forecasting, if justified | Prospective event-based split; false alerts and lead time relative to labelled onset |
| Usability | Student can complete scan, identify zone and understand an uncertain result |

## Prototype acceptance targets to agree with the guide
Demonstrate both wireless nodes simultaneously and preserve their identities. Complete a 24-hour logging run with a documented gap report. Exercise one reconnect event and show that stale values are marked. Capture and analyse one correctly linked image for each zone. Demonstrate a poor-quality or unsupported input without forcing a confident diagnosis.

These are proposed engineering acceptance checks, not completed achievements. A provisional target is at least 95% of expected telemetry records received during the controlled logging run; the actual figure and causes of gaps must be reported.

## Research reporting discipline
Use the same split and tuning rules for comparisons. Estimate uncertainty using independent units such as plant, session or event, rather than treating adjacent sensor readings as independent replicates. Record training cost and deployment latency. Publish limitations, class imbalance and failure examples alongside the best result.

No minimum disease-recognition accuracy is promised before the data audit. The experiment should establish what the model can support, including where it fails.
''')

report('Work plan and review milestones', '''
Time is counted from the guide's scope review, not backdated. The following is a provisional 180-day plan; it should be shortened or adjusted to the official submission calendar.

| Period | Work package | Reviewable output |
| Days 1-7 | Refine question, full notes for four core papers, confirm inventory | Signed-off scope notes; paper matrix; quotation shortlist |
| Days 8-14 | Download / audit chosen datasets; receive first parts | Dataset manifest, class counts and receiving checklist |
| Days 15-21 | One-node sensor bring-up, calibration and local logging | Raw logs and calibration notes; no AI claims yet |
| Days 22-30 | Add second wireless node and camera intake | Two-zone logging demo and first aligned observations |
| Days 31-60 | Four image baselines and reproducible evaluation | Baseline comparison, errors and laptop timings |
| Days 61-90 | Input-quality handling and contextual decision policy | Unknown / fault cases; documented fusion feasibility decision |
| Days 91-120 | Focused policy experiments and dashboard integration | Ablation results; bounded rescan behaviour |
| Days 121-150 | Robustness evaluation; optional data-ready extensions | Final experiment tables and limitations |
| Days 151-180 | Thesis, demonstration rehearsal and paper draft if justified | Final report, reproducible package and presentation |

## First review checkpoint
At the end of the first week, show the guide four completed paper notes, a narrow research question, the dataset manifest template and two or three usable quotations where available. If procurement is delayed, continue dataset audit and offline image baselines after scope approval.

## Change rule
Record any guide-requested change with its reason, revised deliverable and effect on cost or schedule. Do not add every interesting feature to the first build. Protect time for evaluation and writing.
''')

report('Resources, risks and academic outputs', '''
## Resource request
The separate physical-parts proposal estimates **INR 18,150** before contingency and **INR 21,780** including a 20% procurement contingency. The figures are planning allowances, not vendor quotations. They include two leaf-wetness plates and a conditional webcam purchase. Borrow the laptop, Wi-Fi access point and available laboratory tools.

| Constraint | Proposed response |
| Scope becomes too broad | Keep tomato integration and one research question as the core |
| Insufficient labelled disease events | Report monitored context; defer supervised forecasting |
| Leaf-wetness plate is costly / unavailable | Seek exact-variant quotations; stage the purchase or explicitly reduce scope |
| Model succeeds only on clean images | Report external-condition results and failure categories |
| Sensor drift or missing packets | Keep raw values, calibration records, sequence numbers and quality flags |
| Plant variability | Log care conditions; avoid biological efficacy claims from two pots |
| Timeline pressure | Prioritise a working baseline, sound evaluation and a reproducible report |

## Expected academic outputs
A working two-zone demonstration; a documented hardware/interface design; a reproducible dataset audit and image-model comparison; a focused robustness experiment; a local dashboard; and a thesis report with honest limitations.

A research-paper manuscript may follow if the work produces a clear question, valid comparisons and sufficiently supported findings. A publication or acceptance cannot be promised. An initial outline can be prepared now: introduction, related work, methods, experimental design, results to be filled after experiments, discussion and limitations.

The guide's feedback is requested on study scope, biological labelling support, compute access and which extension should be removed first if time or data are limited.
''')

report('Future possibility and guide review record', '''
## Optional path beyond the college prototype
If the college study demonstrates useful and reproducible behaviour, a later pilot could use weather-protected sensor boxes, better field imaging and a hosted PlantGuard service. In that version, **all main AI inference and analysis run on a VPS / cloud server**. Sensor boxes measure and transmit; any field gateway only provides communication and buffering.

This future path would require field validation, suitable data rights, device durability tests, account security, operating-cost measurement and user trials. It is a possible continuation, not a market-ready claim or part of the present hardware-funding request.

## Items for guide feedback
| Decision | Comments / agreed change |
| Tomato-first physical and integrated scope | __________________________________ |
| Primary research question and baseline set | __________________________________ |
| Dataset choices and labelling support | __________________________________ |
| Two-node hardware and leaf-wetness requirement | __________________________________ |
| Optional features to defer | __________________________________ |
| Expected review frequency and submission date | __________________________________ |

## Next meeting record
Review date: ____________________    Next meeting: ____________________

Priority task 1: __________________________________________________

Priority task 2: __________________________________________________

Priority task 3: __________________________________________________

Student: Simran Batwal    Roll number: ____________________

Guide name / signature: ___________________________________________

This record is intentionally blank for the actual meeting. It does not indicate approval.
''')

FUND=[]
def fund(t,b): FUND.append((t,b.strip()))

fund('Request and academic justification', '''
To: Dr. Anil Kumar, Project Guide

For consideration through the appropriate departmental approving authority

Computer Science, Guru Nanak Dev University, Amritsar

**Subject: Request for financial support for the PlantGuard college prototype**

Respected Sir / Madam,

I, Simran Batwal, a student of M.Tech, Computer Science, 3rd Semester, request consideration of financial support for the physical components required for my proposed project, **AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN**, with the system name **PlantGuard**.

The proposed prototype will use two tomato plants, two wireless ESP32 sensor nodes, environmental sensors and a camera connected to an existing laptop-based application. It will support practical work in wireless sensing, data acquisition, AI evaluation and evidence-based plant-health monitoring. Coding and procurement are planned after review of the scope.

The indicative hardware and consumables subtotal is **INR 18,150**. With a **20% contingency of INR 3,630**, the proposed approval ceiling is **INR 21,780**. This is an estimate for planning; actual procurement will depend on accepted quotations, institutional procedure and the final approved configuration.

The laptop, network access point and available laboratory tools will be reused. No VPS subscription, dedicated AI processing box, new computer, GPU or cloud-training expense is included. The optional light sensors and conditional webcam can be omitted if unnecessary.

Kindly review the attached itemised requirement and advise whether support should be through departmental purchase, an approved advance or reimbursement against invoices. Any budget adjustment can be recorded on the approval page.

Yours faithfully,

**Simran Batwal**

Roll number: ____________________    Date: ____________________

Student signature: ____________________
''')

fund('Itemised estimate 1: electronics', '''
All amounts are in INR. Quantities cover **two nodes** unless stated otherwise. Unit figures are provisional allowances, not current vendor offers; obtain quotations for the exact selected variants before purchase.

@bom 0 10

## Technical purchase conditions
The boards must be a matching classic ESP32 DevKitC V4 / WROOM-32E pair, with pinout and USB connector confirmed. Use data-capable cables. Match the SHT31 breakout and I2C pull-ups to 3.3 V operation.

For each leaf-wetness plate, obtain the exact RS485 Modbus variant, supply specification, register map, included cable and warranty terms. The INR 3,500 unit allowance must be replaced by a valid quotation. The associated transceiver must expose ESP32-compatible 3.3 V logic.

The supply/distribution allowance covers regulated low-voltage power appropriate to the purchased variants. If a plate needs a separate supply, include it in the actual quotation; do not connect a higher-voltage sensor supply to ESP32 logic pins.

BH1750 is optional. Omitting both light sensors reduces the subtotal by INR 300. The core two-node study can start without them.
''')

fund('Itemised estimate 2: setup and total', '''
@bom 10 19

@totals

The contingency is a reserve for quotation variation, taxes, shipping or small necessary accessories where not already included. Actual invoices must avoid double counting these charges. Spending above the approved ceiling requires a revised institutional request.

''')

fund('Savings and staged purchasing', '''
## Configuration options
| Configuration | Subtotal | 20% reserve | Planning ceiling |
| Full proposed physical setup | 18,150 | 3,630 | 21,780 |
| Reuse a suitable available camera | 16,650 | 3,330 | 19,980 |
| Omit optional BH1750 pair | 17,850 | 3,570 | 21,420 |
| Reuse camera and omit BH1750 pair | 16,350 | 3,270 | 19,620 |

The full setup is the request baseline. These alternatives preserve both wireless nodes and both leaf-wetness plates. Substituting a cheap rain PCB is not equivalent to funding the documented wetness measurement.

## How expenditure can be staged
Start by confirming the available laptop, camera, access point and laboratory tools. Test sample close-up images before committing to the webcam purchase. If a suitable camera is already available, use the lower configuration above.

The first procurement stage can cover the controller, soil and air measurements, power and basic assembly. The second can add documented leaf-wetness plates, their interfaces and enclosure integration once exact quotations and compatibility are confirmed. The full approved scope still requires both sensing nodes; staging does not mean reporting a one-node setup as the final WSN demonstration.

BH1750 sensors may be omitted without blocking the first integrated demonstration. Any omission of a core measurement must be reflected in the report, experiment design and final expense record.

## Quotation discipline
For each shortlisted supplier, compare the same technical variant and the complete delivered price. Include required cable lengths, supply adapters and protocol-conversion modules. Do not compare an analogue plate with an RS485 model as if they were the same part.

The separate quote-comparison sheet supplied with this pack is blank for actual offers and receipts. No supplier has been selected and no purchase order has been issued through this proposal.
''')

fund('Visual component reference', '''
@photos esp32 soil sht31 leaf bh1750 enclosure

The photographs are manufacturer/product-family references. They explain the required categories; they are not vendor quotations or a claim that a particular pictured brand fits the allowance. Equivalent parts need technical review before acceptance.

## Plant and camera setup
Two labelled 10-15 L pots with drainage trays, two similar tomato seedlings, one batch of medium, soft ties and stakes provide repeatable measurement locations. A shared camera stand should support sharp, close-up leaf photographs. Air-sensor shields and separate wetness-plate supports help avoid misleading readings.

## Already available or to borrow
Existing laptop and phone, local Wi-Fi access point, multimeter, soldering station, cutters and basic assembly tools. Verify availability before placing orders. The two enclosures are prototype protection; no certified field-protection rating is claimed for the finished assembly.

Hardware reference links are included in the college report and in the image source register supplied with this pack.
''')

fund('Procurement, ownership and approval', '''
## Proposed process
1. Guide confirms scope and preferred configuration. Check laboratory inventory first.
2. Collect quotations with exact model, quantity, included cables, taxes, shipping, delivery time and warranty. Follow the institution's required quotation count and purchase procedure.
3. Obtain the appropriate written purchase / reimbursement authorisation. This document is a request, not an issued sanction.
4. Receive and test components; record markings, quantity, invoice, condition and serial number where present. Resolve incorrect voltage or protocol variants before assembly.
5. Maintain a parts register, expense record and receipts. Record reusable assets and consumables according to departmental ownership rules.
6. Show the assembled two-node demonstration, data logs and expenditure reconciliation at the agreed review.

## Approval record
| Field | Entry |
| Proposed ceiling | INR 21,780 |
| Approved ceiling / configuration | __________________________________ |
| Funding source / reference | __________________________________ |
| Purchase route | Department purchase / advance / reimbursement |
| Guide recommendation and remarks | __________________________________ |
| Approving authority name / designation | __________________________________ |
| Signature and date | __________________________________ |

## Expected benefit from the expenditure
The hardware will support sensor calibration, wireless communication tests, image/sensor data association and an inspectable AI demonstration. Reusable electronic components can support further academic work after the project, subject to departmental policy.

Prepared by Simran Batwal. Roll number: ____________________

All signatures and approval fields are left blank for the actual institutional process.
''')

HANDBOOK=[]
def hand(t,b): HANDBOOK.append((t,b.strip()))

hand('Sabse pehle project ko samjho', '''
## Ek sentence mein
“PlantGuard mein hum leaf ki photo aur plant ke aas-paas ke sensors ka data ek laptop par laakar plant-health ki evidence-based information dikhayenge.”

Sirf disease ka naam bolna poora system nahi hai. System ko yeh bhi batana hai ki photo clear thi ya nahi, sensor reading fresh thi ya nahi, aur result ke liye evidence kaafi hai ya nahi.

## Ek simple example
Maan lo photo mein leaf normal dikhti hai, lekin aas-paas hawa humid hai aur wetness plate kaafi der wet rahi. Photo current visible condition batati hai; sensors environment ka context dete hain. Isliye “visually healthy” aur “environment concerning” ek saath aa sakte hain. Is example se actual disease ya future infection prove nahi hota.

## Teen cheezein yaad rakho
1. **ESP32** sensors padhega aur Wi-Fi se bhejega.
2. **Laptop** AI, database aur dashboard chalayega.
3. **Aap** leaf photo ko correct plant / zone se link karoge aur result ko review karoge.

College mein do pots ka setup sensing aur integration demonstrate karega. Diseased plants grow karna compulsory nahi hai. Labelled disease photos se image model test kar sakte hain; un photos ke saath random sensor values attach nahi karni.

## Abhi kya sach mein complete hai
Topic discuss hua hai, initial planning hui hai aur aapne kuch preliminary papers dekhe hain. Coding abhi start nahi hui. Dataset download aur detailed audit next tasks hain. “Model train ho gaya” ya “dataset ready hai” tabhi kehna jab uska actual evidence ho.
''')

hand('Meeting ka 10-minute sequence', '''
| Time | Kya explain karna hai | Kya dikhana hai |
| 0-1 min | Exact title, system name aur current stage | One-page guide summary |
| 1-2 min | Problem: photo aur sensor dono ki limits | Report ka problem statement |
| 2-4 min | Two pots, sensors, Wi-Fi aur laptop flow | Architecture aur physical setup pages |
| 4-6 min | Literature se kya seekha, proposed question | R1-R4 briefs aur research-question page |
| 6-7 min | Scope: tomato first; extensions data-dependent | Objectives / scope page |
| 7-8 min | Data split aur evaluation ka plan | Dataset aur evaluation pages |
| 8-9 min | Hardware cost aur borrowed items | Separate funding proposal |
| 9-10 min | Guide se decisions aur next meeting | Feedback record |

## Opening script
“Sir/Ma'am, mere project ka title AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN hai. System ka naam PlantGuard hai. Abhi topic discussion, initial planning aur preliminary literature reading hui hai. Main coding se pehle aapse scope aur research direction review karwana chahti hoon. College prototype ke liye do tomato pots, do ESP32 sensor nodes aur existing laptop propose kiya hai.”

## Phir next line
“Mera focus sirf image classification par nahi, balki unclear image, stale sensor reading aur missing data mein system ka reliable behaviour evaluate karna hai. Iske liye main aapko proposed architecture aur comparisons dikhati hoon.”

Guide beech mein question karein toh sequence ko force mat karo. Pehle unka question answer karo, feedback note karo, phir relevant page se continue karo.
''')

hand('Har component ko kaise explain karein', '''
| Component | Simple answer | Ek limitation bhi bolo |
| Pot aur tomato plant | Repeatable physical measurement location | Do pots biological efficacy prove nahi karte |
| Soil sensor | Medium ki wetness response read karta hai | Calibration ke bina exact water percentage nahi |
| SHT31 | Air temperature aur relative humidity read karta hai | Leaf ki actual wetness nahi batata |
| Wetness plate | Leaf jaisi proxy surface par moisture sense karti hai | Har real leaf ko directly measure nahi karti |
| ESP32 | Chhota controller jo sensors read aur transmit karta hai | Main disease AI laptop par chalegi |
| MAX3485 | RS485 sensor aur ESP32 ke beech interface | Correct voltage / protocol match chahiye |
| Camera | Leaf ka close-up visual evidence | Blur aur wrong angle result ko affect karte hain |
| Wi-Fi access point | Nodes aur laptop ko network par jodta hai | Internet aur local network alag cheezein hain |
| Laptop | Data store, model run, result display | Speed hardware par measure karni padegi |
| Dashboard | Readings, trends, image aur uncertainty dikhata hai | Screen par number hona correct measurement ka proof nahi |

## WSN kaise samjhana hai
“WSN ka full form Wireless Sensor Network hai. Mere prototype mein do physically separate sensing nodes honge. Dono apne IDs ke saath readings wireless bhejenge. Isi se multiple locations monitor karna demonstrate hoga.”

## IoT aur AI ka role
IoT connected devices aur unke data services ko jodta hai. AI image patterns se classification seekhta hai. WSN sensing network hai. Yeh teen terms related hain, lekin interchangeable nahi hain.

Paper diagram ko wiring diagram ki tarah use mat karna. Actual assembly exact board aur sensor manual ke according hogi.
''')

hand('AI aur data ke basic words', '''
| Word | Beginner meaning |
| Dataset | Labelled examples ka organised collection |
| Label | Example ka known category; label ka source important hai |
| Training | Model examples se parameters seekhta hai |
| Validation | Development ke decisions aur thresholds choose karne ka separate data |
| Test set | Final evaluation ka untouched data |
| Transfer learning | Pehle se trained model ko apne task ke liye adapt karna |
| CNN | Image ke local visual patterns learn karne wali model family |
| ViT | Image patches ke relationships attention se model karne wali family |
| Inference | Trained model ko new image par chalana |
| Overfitting | Training examples par achha, unfamiliar examples par weak performance |
| Data leakage | Test ki information training / selection mein chali jana |
| Fusion | Relevant different evidence sources ko combine karna |
| Ablation | Ek part hata kar dekhna ki uska benefit tha ya nahi |
| Unknown / OOD | Training scope se bahar condition ya input |
| Calibration | Confidence ya sensor output ka observed reality se match check karna |

## Four models kyun?
MobileNetV3 Large relatively compact candidate hai; ResNet50 aur EfficientNet-B0 alternative CNN baselines hain; ViT attention-based comparison dega. Kaun best hai, woh data aur actual evaluation batayegi. Bas naam bada hone se model best nahi hota.

## Accuracy aur recall
Accuracy sab test examples mein correct fraction hai. Recall kisi disease ke actual examples mein kitne detect hue batata hai. Imbalanced classes mein accuracy alone misleading ho sakti hai; isliye per-class metrics aur macro-F1 report karenge.
''')

hand('Guide ke questions 1: scope aur novelty', '''
## 1. Tum exactly kya bana rahi ho?
“Two-node wireless plant-monitoring prototype aur laptop application. Photo classification, sensor context, input-quality checks aur uncertainty display integrate karungi.”

## 2. Isme naya kya hai? Disease detection toh pehle se hai.
“Ji, basic classification aur fusion existing work hai. Proposed study quality-aware evidence use aur bounded rescanning ko compare karegi. Novelty claim related-work review aur results ke baad narrow karungi.”

## 3. Yeh sirf IoT project hai ya research bhi?
“IoT setup implementation platform hai. Research part fixed baselines ke against decision reliability, missing-input robustness aur observation cost evaluate karna hai.”

## 4. Itne features time par ho jayenge?
“Core tomato pipeline aur one research question prioritise karungi. Forecasting, full severity segmentation aur continual learning ko data/time gates ke baad hi add karungi.”

## 5. Tomato hi kyun?
“First integrated setup manageable rahega aur selected disease-image datasets se start kar sakte hain. Final cultivar, labels aur practical availability guide review ke baad freeze karungi.”

## 6. Seven crops ka kya hua?
“Wider image benchmark ke candidate crops hain. Physical prototype tomato ka hoga. Other crops ke labels aur data quality audit karne ke baad selected extensions add honge.”

## 7. Do pots enough hain?
“Wireless system aur data integration demonstrate karne ke liye useful hain. Biological generalisation, treatment efficacy ya disease forecasting prove karne ke liye enough independent cases nahi hain.”

## 8. Actual diseased plant kahaan se aayega?
“Initial image tests approved labelled datasets se honge. Real disease observations ke liye expert-supported access discuss karungi; classroom mein deliberately infection introduce nahi karungi.”
''')

hand('Guide ke questions 2: hardware aur sensing', '''
## 9. Arduino aur ESP32 dono kharidoge?
“Nahi, selected controller ESP32 hai. Arduino framework programming ke liye use ho sakta hai; separate Uno required nahi.”

## 10. AI ESP32 mein chalegi?
“Main disease model existing laptop par chalega. ESP32 sensors read, status track aur wireless data transmit karega.”

## 11. USB laga hai toh wireless kaise?
“USB power ya debugging ke liye ho sakta hai. Final telemetry Wi-Fi se jayegi. Demo mein wireless receipt aur node IDs show karungi.”

## 12. Humidity sensor ho toh leaf wetness kyun?
“Humidity air mein moisture condition batati hai. Leaf-wetness plate surface wetness ka proxy hai; dono same physical measurement nahi hain.”

## 13. Soil sensor se disease pata chal jayegi?
“Nahi. Woh root-zone moisture context dega. Disease label image evidence aur verified labels ke against evaluate hoga.”

## 14. Wetness sensor itna mehenga kyun hai?
“Budget genuine documented plate ke liye rakha hai. Exact model ki quotation leni hai. Cheap rain PCB ko equivalent instrument bolna appropriate nahi hoga.”

## 15. Sensor kharab ho gaya toh?
“Missing, stale aur implausible readings flag hongi. Model context unavailable show karega; faulty value ko valid evidence ke tarah use nahi karega.”

## 16. Internet band ho gaya toh?
“College version local network par laptop ke saath chalega. Local Wi-Fi connection bhi fail ho toh offline status aur gaps log honge; reconnect behaviour test karungi.”

## 17. Camera kaunsa chahiye?
“Pehle available phone ya camera ki close-up quality test karungi. Need ho tab suitable USB webcam; minimum focus distance aur clear leaf detail selection criteria honge.”
''')

hand('Guide ke questions 3: data aur evaluation', '''
## 18. Dataset download kiya hai?
“Sources shortlist hain; download aur audit next task hai. Manifest mein source, licence, counts aur class mapping record karungi.” Download ke baad actual folder aur count dikhana.

## 19. Sensor data public images se kaise match hoga?
“Unrelated public images ko local sensor readings se match nahi karungi. Paired observations khud capture karne ya suitable paired dataset ki zarurat hogi.”

## 20. Train/test split kaise karogi?
“Plant, session ya original source ke related images same split mein rahenge. Duplicate checks aur split augmentation se pehle karungi.”

## 21. Kitni accuracy expect kar rahi ho?
“Abhi target result claim nahi kar sakti. Common protocol par four models compare karke internal aur external performance separately report karungi.”

## 22. Fusion better hai, kaise prove karogi?
“Same eligible cases par image-only, simple context aur quality-aware variants compare karungi. Paired labels insufficient hue toh learned-fusion claim nahi karungi.”

## 23. High confidence ka matlab correct result hai?
“Guaranteed nahi. Confidence calibrate karni hai, unfamiliar inputs evaluate karne hain aur low-evidence cases reject karne hain.”

## 24. Future disease predict kar sakte ho?
“Potential extension hai. Real early warning validate karne ke liye time-labelled independent disease events aur prospective evaluation chahiye. Abhi environmental indicator ko disease probability nahi bolungi.”

## 25. Heatmap se severity mil jayegi?
“Heatmap model attention inspect karne mein help kar sakti hai. Accurate lesion area ke liye segmentation labels aur separate validation chahiye.”
''')

hand('Guide ke questions 4: papers aur delivery', '''
## 26. Kaunse papers padhe? Kya samjha?
“Preliminary reading shuru ki hai. Is report mein eight selected briefs hain. Jo papers full padhe hain unke methods aur limitations apne notes se explain karungi; baaki ko reading queue ke roop mein identify karungi.”

## 27. Ab tak coding kya hui?
“Coding start nahi ki. Scope review ke baad dataset audit, first sensor node aur baseline pipeline se start karungi.”

## 28. Research paper publish karogi?
“Valid experiment aur clear contribution mile toh manuscript prepare karungi. Acceptance ya publication abhi promise nahi kar sakti.”

## 29. Medicine ya spray quantity bhi dogi?
“Initial prototype reviewed management records aur sources dikhayega. Free-form AI se pesticide/dose invent nahi karenge. Any treatment-specific output ko appropriate expert review chahiye.”

## 30. Kitna budget hai aur kisliye?
“Physical parts subtotal INR 18,150 hai. 20% reserve ke saath INR 21,780 ceiling propose ki hai. Existing camera usable ho toh ceiling INR 19,980 ho sakti hai.”

## 31. Agli meeting mein kya dikhaogi?
“Agreed scope, four full paper notes, dataset manifest aur actual download status, inventory/quotations aur first-node plan. Hardware mil gaya ho toh basic logged readings bhi.”

## 32. Isko market mein le ja sakte ho?
“Later field validation ke baad possible pilot explore kar sakte hain. Market AI VPS/cloud par hogi. Abhi college scope aur evidence priority hain.”

## Agar answer nahi aata
“Is point ko maine abhi sufficiently verify nahi kiya. Main exact method/source check karke next review mein evidence ke saath answer laungi.” Phir point notebook mein likho. Guess karke false certainty dikhane ki zarurat nahi.
''')

hand('Research paper padhne ka practical tareeka', '''
## Har paper ke liye three passes
**Pass 1, 15-20 minutes:** title, abstract, main figures aur conclusion. Ek line mein problem aur claimed contribution likho.

**Pass 2, 45-60 minutes:** dataset, labels, method, baselines, train/test split aur main result tables. Jo samajh nahi aata uske terms note karo. Result ki unit aur evaluation setting copy karo, sirf biggest number nahi.

**Pass 3, need ke hisaab se:** implementation, supplementary information, code aur limitations. Important experiment reproduce karna possible hai ya nahi assess karo.

| Note heading | Apne words mein kya likhna hai |
| Research problem | Paper kis exact issue ko solve karta hai? |
| Data | Kitne independent examples, kaunse crops, kis environment se? |
| Method | Input se output tak 4-5 simple steps |
| Evaluation | Split, baselines, metrics aur comparison fairness |
| Finding | Paper kya demonstrate karta hai, kis setting mein? |
| Limitation | Kya test nahi hua; leakage / generalisation concern? |
| PlantGuard link | Kya adopt, compare ya avoid karna hai? |
| Reading status | Abstract read / methods reviewed / full read / reproduced |

## Pehle kin papers par focus karein
R1 se controlled versus external performance samjho. R2 se real-world image difficulties. R3 se sensor-image fusion. R4 se time-series risk aur valid early-warning evaluation. R5-R8 ko phir unknown conditions, updates aur reviewed advice ke context mein padho.

Report ke literature briefs ek starting aid hain. Guide ke saamne apni actual reading depth clearly batana. “All papers fully read” tabhi kehna jab methods aur key limitations explain kar pao.

Separate editable **Paper_Reading_Tracker.md** mein apne notes fill karo. Paper ke PDF ko cite karo, AI-generated summary ko primary research source mat banao.
''')

hand('Meeting ke pehle aur baad kya karna hai', '''
## Meeting se pehle
1. One-page summary aur report architecture page do baar samjho.
2. R1 aur R2 ke original papers kholkar abstract, dataset aur limitations padho; apne five-line notes banao.
3. Roll number aur guide name ke blank fields fill karo. Date actual submission wali use kar sakte ho.
4. Funding proposal mein borrowed camera / tools ki availability mark karo. Estimate ko quotation mat bolo.
5. Laptop par PDFs aur source links ready rakho; printed summary saath le ja sakte ho.

## Guide se yeh decisions lo
“Kya tomato-first scope suitable hai?” “Main reliability-aware diagnosis par focus karun ya forecasting ke liye dataset access available hai?” “Four-model comparison appropriate hai?” “Plant labels verify karne ke liye expert support mil sakta hai?” “Next review mein kaunsa output priority hoga?”

## Funding request ko kaise rakhein
“Sir/Ma'am, main pehle available laboratory resources reuse karna chahti hoon. Remaining two-node components ka separate estimate attach hai. Aap configuration aur purchase route suggest kar dein; exact quotations uske according final karungi.”

## Closing script
“Aaj ki discussion se main agreed scope aur changes note kar rahi hoon. Agli meeting tak main priority paper notes, dataset audit aur approved hardware plan dikhaugi. Kya main in three deliverables aur next review date ko note kar loon?”

## Meeting ke baad
Same day feedback sheet complete karo. Har action ke liye owner, due date aur evidence likho. Report ka next version banao; previous version preserve karo. Guide ne scope change bola ho toh pehle plan revise karo, phir implementation start karo.

Kal ka practical first task: R1/R2 reading notes aur dataset manifest template. Isse guide discussion aur subsequent coding dono clearer honge.
''')

hand('Mock viva and action record', '''
## Five-minute rehearsal
Bina report dekhe explain karo: project ka one-sentence purpose, ESP32 versus laptop role, WSN ka proof, image aur sensor context ka difference, aur abhi project ka actual status. Phir architecture draw karo. Jahan atko, us point ko read karke apne words mein dobara bolo.

## Self-check
| Can I explain this? | Tick / short note |
| Why two nodes and two pots? | ______________________________ |
| Why humidity and leaf wetness differ? | ______________________________ |
| Why public images cannot take random sensor labels? | ______________________________ |
| What exactly will be compared? | ______________________________ |
| Why no accuracy / publication promise yet? | ______________________________ |
| What is core and what is optional? | ______________________________ |
| Where does INR 21,780 come from? | ______________________________ |

## Actual meeting notes
Meeting date: ____________________    Guide: ____________________

Main feedback: __________________________________________________

Scope change: __________________________________________________

Paper / method suggested: ________________________________________

| Action | Due date | Evidence to show |
| ______________ | __________ | __________________ |
| ______________ | __________ | __________________ |
| ______________ | __________ | __________________ |

Next meeting: ____________________

Prepared specifically for Simran Batwal's initial PlantGuard review. Use the formal report for academic submission and this Hinglish handbook for preparation.
''')

SUMMARY='''
**AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN**

Simran Batwal | M.Tech, Computer Science | 3rd Semester

Guru Nanak Dev University, Amritsar | Roll no.: ____________________

## Current stage
Topic discussion, initial planning and some preliminary reading. Dataset download / audit and coding are planned after scope review. No trained-model or experimental results are claimed.

## Proposed college prototype
Two tomato pots; two ESP32 Wi-Fi nodes; capacitive soil probes, SHT31 sensors and genuine leaf-wetness plates. Phone / USB camera provides close-up leaf images. Existing laptop runs the AI, database and dashboard.

@miniarch

## Research focus for guide review
Compare image-only, simple contextual and quality-aware decision policies. Evaluate whether bounded fresh observations improve reliability under uncertain images or faulty / missing sensor data. Learned fusion needs paired labels; forecasting needs independent time-labelled disease events.

## Scope and evidence
Tomato-first integration; four image-model comparisons. Report macro-F1, class recall, accepted-case error / coverage, unknown handling, telemetry gaps and latency. Other crops, severity and continual learning are data-dependent extensions.

## Resources and next 30 days
Indicative physical budget: **INR 18,150 + INR 3,630 reserve = INR 21,780**. Reuse laptop / network / tools. Next: agree scope, read core papers, audit data, calibrate first node and demonstrate two-node wireless logging.

## Guide decisions requested
Research question, dataset / labelling support, hardware configuration, deferred features and next review date. Market continuation, if later pursued, will run main AI on VPS/cloud.

Guide / review date: ____________________    Next meeting: ____________________
'''
