from original_content import *

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'output/Guide_Review_Revised'
MASTER=BASE/'docs/Master_Plan_2026-09-08'

# Current college report: simple first-person English and a clear proposed-work distinction.
REPORT=[]
def report(t,b):REPORT.append((t,b.strip()))

report('Introduction and current progress','''
## About my project
My project is **AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN**. I have named the system **PlantGuard**. I plan to use leaf photographs and environmental sensors to monitor plant health. A laptop will process the data and display the results.

I have discussed the topic with my guide and prepared an initial plan. I have also started reading related research papers. A detailed study of their methods, datasets and results is still in progress. I will finalise the scope with my guide before starting the main implementation.

| Work | Current progress |
| Topic selection | Topic discussed with my guide |
| Initial planning | Basic system flow and required components identified |
| Literature study | Preliminary reading started; detailed review in progress |
| Dataset preparation | Sources shortlisted; download and checking are the next steps |
| Hardware | Components shortlisted; purchase and assembly are pending |
| Coding and model training | Not started |
| Testing and results | Will begin after implementation |

## Purpose of this report
In this report, I explain the college prototype, the work already published in this area and the part I plan to study. I have included the hardware requirements, software choices, testing method and a proposed schedule.

At the next review, I would like to discuss whether the scope is suitable, which experiments should be given priority and what support is available for checking plant-disease labels.
''')

report('Abstract and problem statement','''
## Abstract
Plant diseases can affect plant growth and crop quality. A leaf photograph can help identify visible symptoms, while sensors can record the surrounding conditions. However, a blurred image, an unfamiliar disease or a faulty sensor may lead to an unreliable result.

In this project, I propose PlantGuard, a plant-health monitoring system using AI, IoT and a Wireless Sensor Network. The college setup will contain two tomato plants and two ESP32 sensor nodes. Each node will measure soil-moisture response, air temperature, relative humidity and leaf wetness. A phone or USB camera will capture leaf photographs. The readings and images will be processed on a laptop and shown on a dashboard.

I will first compare four image-classification models. I will then study how sensor information and input-quality checks can support the image result. When the information is unclear or incomplete, the system will show the problem and may ask for a fresh photograph. I will compare this approach with a simpler image-only system.

The expected outcome is a working two-node prototype and a comparison of its performance under clear, unclear and incomplete inputs. Disease forecasting and other extensions will depend on the availability of suitable data.

## Problem statement
How can I combine leaf images and environmental readings in a practical college prototype while reducing incorrect decisions caused by unclear images, missing readings or faulty sensors?

## Reason for selecting this topic
The project connects computer vision, embedded systems, networking and data analysis. Published work shows that good results on clean leaf images do not always carry over to different conditions [R1, R2]. I want to study this practical problem through a manageable prototype.
''')

report('Objectives and project scope','''
| Objective | What I plan to demonstrate |
| Wireless monitoring | Two sensor nodes send separate readings to a laptop |
| Image classification | Compare MobileNetV3 Large, ResNet50, EfficientNet-B0 and ViT |
| Sensor and image integration | Match each photograph with the correct plant, zone and time |
| Handling unclear inputs | Show low-quality, unknown or missing-data messages when needed |
| Performance comparison | Compare classification results, errors, response time and extra observations |
| User interface | Show readings, images, trends and reviewed management information |

## First prototype
I will start with tomato. The first image task will use healthy, early-blight and late-blight categories. Images outside the supported task should be rejected or marked for review. The physical setup will have two pots to demonstrate two measurement locations.

The two plants are for monitoring and integration tests. They will not be enough to prove disease forecasting or treatment effectiveness. For image-model experiments, I will use suitable labelled datasets and check their sources.

## Work to consider later
The wider plan includes potato, maize, apple, grape, pepper and rice. I will add these image categories only after checking the data and discussing the scope with my guide. The first physical setup will remain tomato-based.

Severity estimation, learned forecasting and continual learning will need additional labels and experiments. I will consider these after the main prototype is working. Automatic watering, spraying and solar power are not required for the first college setup.
''')

report('College architecture and data flow','''
@diagram college
Figure 1. Proposed college system. The arrows show data flow.

## Working sequence
1. The sensors take readings near each plant. Each ESP32 adds its node ID and reading status.
2. Both nodes send their readings over Wi-Fi to the laptop.
3. The application checks and stores the readings. It also records missing values and the last received time.
4. I capture a leaf photograph and select the plant and zone. The image is saved with its capture time.
5. The image model gives a result. The application looks up the relevant sensor history from the same zone.
6. The dashboard shows the image result, sensor conditions and any reason to take another observation.

## Role of each part
The **ESP32** reads sensors and sends data. The **laptop** runs the AI model, application and database. The **Wi-Fi access point** connects the devices. The **camera** provides the leaf image.

USB cables can supply power or help with debugging. The final sensor readings will still travel wirelessly. Once the required software and model files are installed, the college demonstration can run over a local network without an internet connection.

If I use a phone hotspot, I will first check whether it allows the laptop and nodes to communicate with each other.
''')

report('Physical setup and sensor placement','''
@setup
Figure 2. Proposed two-pot arrangement. This drawing shows placement, not electrical wiring.

| Component | Planned placement |
| Tomato plants | Two similar plants in labelled 10-15 L pots with drainage trays |
| Soil probe | In the root-zone medium; insertion depth will be recorded |
| SHT31 | Near the canopy, inside a ventilated shield and away from direct spray |
| Leaf-wetness plate | On a separate support near the leaves, following its installation instructions |
| Camera | On a stable stand at a suitable close-focus distance |
| ESP32 and wires | Above tray level, with protection from water and loose connections |

I will keep the potting medium and care routine as consistent as possible. I will record watering, visible changes, sensor movement and other changes around the plants.

The wetness plate acts as a surface near the plant; it does not measure every leaf directly. The two pots represent two monitored zones. They are not a complete biological trial.

The first demonstration can use labelled disease photographs. I will discuss access to real disease observations with my guide and a suitable plant expert before planning any such study.
''')

report('Controller and main sensors','''
@photos esp32 soil sht31
| Part | Planned choice |
| Controller | Two matching ESP32 DevKitC V4 boards with WROOM-32E modules [H1] |
| Soil sensor | Capacitive SEN0193-class probe [H2] |
| Air sensor | SHT31 temperature and humidity breakout [H3] |

## Why I selected ESP32
ESP32 has built-in Wi-Fi and suitable connections for the required sensors. I can program it using the Arduino framework. A separate Arduino Uno is therefore not required. I will check the exact board model, pin layout and cable connector before assembly.

## Soil moisture
The capacitive probe gives an electrical reading that changes with the surrounding medium. I will record the raw reading and calibrate the probe in the selected potting medium. The displayed value will be a relative moisture index. I will not treat it as an exact soil-water percentage without the required calibration.

## Temperature and humidity
SHT31 measures local air temperature and relative humidity. I selected it for the planned air measurements. It needs a suitable shield so that direct sunlight, water and heat from the electronics do not distort the readings.

The photographs show component families. I will confirm the actual model and electrical requirements from the supplier's documentation before buying or connecting them.
''')

report('Leaf wetness, camera and accessories','''
@photos leaf bh1750 enclosure
## Leaf wetness
I plan to use a documented artificial leaf-wetness plate, such as an RS485 Modbus variant in the Renke RS-WS-*-YM-1-T family. I will confirm the exact model, supply voltage, output units and register details before ordering [H4]. A 3.3 V MAX3485 interface is included for each node [H5].

Air humidity and leaf wetness are different measurements. Humid air does not always mean that the leaf surface is wet. A basic rain-detection board will not be treated as an equivalent calibrated leaf-wetness sensor.

## Camera
I will use a phone or USB camera to capture a clear close-up of the leaf. Before selecting a webcam, I will check the image focus, exposure and mounting distance. A “1080p” label alone does not guarantee a clear close-up.

## Optional light measurement
BH1750 can record light level in lux [H6]. It is optional for the first prototype. Lux is a measure of illuminance; it is not the same as the light measurement used for photosynthesis.

## Assembly items
The setup will also need breadboards, data cables, jumper wires, terminals, regulated power supplies, fuse protection, standoffs, enclosures, sensor supports, pots and trays. I will check the available laboratory tools before requesting any additional equipment.
''')

# Preserve the detailed electrical and calibration information, with simpler surrounding language.
_old_report = dict(__import__('original_content').REPORT)
_interfaces=_old_report['Interfaces and calibration plan']
_interfaces=_interfaces.replace('Provisional interface','Planned interface').replace('These pin choices are a design starting point','I will use these pin choices as a starting point').replace('Review the exact modules and sensor manuals','I will check the exact modules and sensor manuals').replace('before energising the circuit','before switching on the circuit').replace('Co-locate the two air sensors','Place the two air sensors together').replace('Keep calibration coefficients versioned per probe','Save calibration values separately for each probe').replace('A low-cost calibrated prototype supports comparative measurements. It does not establish laboratory-grade accuracy, absolute water content or a universal disease threshold.','I will record the calibration method and any differences between the sensors. This will help me explain the accuracy and limits of the measurements.')
report('Connections and calibration',_interfaces)

for t,b in __import__('original_content').REPORT:
    if t.startswith('Literature review'):
        b=b.replace('**Method and evidence.**','**Work done in the paper.**').replace('**Critical reading.**','**Main limitation.**').replace('**Design implication.**','**Use in my project.**')
        b=b.replace("These are the paper's results, not results obtained in this project.",'')
        b=b.replace('For a reproducible comparison, inspect','In my detailed reading, I will check').replace('The same lead time cannot be promised from two college pots.','A two-pot setup will need more disease observations before I can test early warning.')
        b=b.replace('PlantGuard\'s contribution must be narrower and experimentally demonstrated, such as behaviour under poor-quality or missing inputs.','I will focus on testing what happens when the image is unclear or sensor information is missing.')
        b=b.replace('dataset auditing','checking the dataset').replace('prospectively controlled local field study','planned local field study').replace('A successful crop-specific study does not automatically transfer to tomato or to inexpensive sensors.','Results from peach trees need further testing before they can be applied to tomato and the sensors in my setup.')
        b=b.replace('These are preliminary literature briefs prepared for this discussion. The student has reported some initial reading; full methods, supplementary material and reproducibility checks remain part of the work plan. No claim of an exhaustive systematic literature review is made.','I have started reading papers on these topics. The notes above summarise the main points I have identified so far. I still need to study the methods, additional material and experiment details more closely.')
        b=b.replace('Priority for the next meeting: complete full notes for R1, R2, R3 and R4, then explain in one minute what each changes in the proposed design.','Before the next review, I will prepare detailed notes for R1, R2, R3 and R4 and explain how they affect my project choices.')
        b=b.replace('Ask the guide whether the thesis should prioritise reliability-aware diagnosis or forecasting. The first is feasible with controlled quality tests; the second depends on obtaining a sufficiently informative longitudinal disease dataset.','I will discuss with my guide whether the main study should focus on reliable diagnosis or forecasting. Forecasting will require data showing the conditions before actual disease events.')
        report(t,b)

report('Previous work and my proposed work','''
## What has already been done
Published studies have already used deep learning to classify plant diseases from images. Other studies have combined images with environmental data, handled unfamiliar inputs, studied model updates and retrieved treatment information [R1-R8]. These are the starting points for my project.

| Area | Previous work | What I plan to do in PlantGuard |
| Leaf-image classification | CNN and other image models identify disease categories [R1, R2] | Compare four models using the same checked data split |
| Image and sensor combination | Peach and tomato studies combine visual and environmental information [R3, R4] | Match images to the correct zone and time, then test whether valid context helps |
| Unfamiliar inputs | Anomaly-detection research studies inputs outside known classes [R6] | Include unsupported and unclear inputs in the prototype tests |
| Model updates | Continual learning studies how to learn new tasks without losing old knowledge [R7] | Keep this as a later experiment with checked labels |
| Management information | Retrieval methods use recorded treatment information [R8] | Show a small set of reviewed, source-linked management notes |

## The part I want to investigate
My main question is how the system should behave when the available information is weak. I will compare a normal image-only result with an approach that checks image quality and sensor freshness, uses valid context and asks for one more observation when needed.

I am not proposing a new CNN architecture. I will use published models and study the decision process around them. The useful difference will need to be shown through experiments, especially whether errors reduce without asking the user for too many photographs.
''')

report('Research question and comparisons','''
## Research question
Can checking input quality and asking for a limited number of fresh observations improve plant-health decisions when images or sensor readings are unclear?

| Experiment | Method |
| A. Image-only | Use the leaf photograph alone |
| B. Image with sensor context | Add the available, correctly matched sensor information |
| C. Quality checks | Check for unclear images and missing, old or faulty readings before giving a result |
| D. Fresh observation | Use the checks above and ask for one better photo or a short burst of readings when needed |

## Example of the proposed difference
If an image is blurred and the sensor reading is old, a simple system may still show a disease name. I plan to mark the weak inputs and request a clearer photograph. If the new information is still not enough, the system will say that the result needs review.

## How I will check the benefit
I will compare the methods on the same suitable test cases. I will measure correct and incorrect results, how many cases receive a result, how many need another observation and the time taken. A method that rejects every image is not useful, even if its few accepted answers are correct.

A trained image-sensor model needs genuinely matched images, sensor histories and disease labels. If I cannot obtain enough such data, I will test a simpler rule-based method and explain that limit. Artificially removing readings can test software behaviour, but cannot prove biological disease prediction.
''')

report('Datasets and preparation','''
| Dataset / source | Planned use | What I will check |
| PlantVillage [D1] | First image-model experiments | Crop labels, duplicate files and permitted use |
| PlantDoc [D2] | Test on less controlled images | Compatible labels and overlap with training images |
| PlantWild [D3] | Optional additional image test | Dataset version, class coverage and licence |
| My plant observations | Sensor logging and image-data connection | Plant ID, zone, capture time and care record |
| Expert-checked disease observations | Later fusion or forecasting tests | Correct labels and enough separate disease events |

## Preparation steps
I will download the selected data and make a record of its source, version, licence, class names and file counts. I will keep the original files separately and prepare a working copy for the experiments.

I will divide the data before creating augmented images. Related images from the same plant, session or source will stay in the same group. I will also check for exact and similar duplicates. Training data will teach the model, validation data will help me choose settings, and test data will be kept for the final comparison.

## Matching images and sensors
For a photograph I capture, I will record the correct plant, zone and time. I will then use readings from that location and time period. I will not attach random local readings to an unrelated public image.

Many readings from the same two pots will be related to each other. I will therefore distinguish the number of logged rows from the number of independent plant or disease cases.
''')

report('AI models and result handling','''
## Image classification
I will compare **MobileNetV3 Large, ResNet50, EfficientNet-B0 and ViT** using pretrained models. Pretraining gives a starting point learned from other images. I will adapt the output layer for the selected plant categories and train using the chosen dataset.

I will use the same data split and similar tuning effort for the comparisons. I will record the settings, software versions, training time and results. After testing, I will select one model for the laptop demonstration.

## Sensor information
I will begin with clear rules and summaries of recent readings. The image result describes visible symptoms; the sensor readings describe the environment. A visually healthy leaf can still be in conditions that need attention. These two outputs will be shown separately.

If I obtain enough paired labelled data, I can compare a trained combination method. Random Forest and XGBoost are possible choices for sensor summaries. GRU or LSTM may be useful later for time sequences, but only if there are enough labelled disease events.

## Unclear results and explanations
For poor-quality images or unsupported conditions, the application will ask for another photograph or show that review is needed. I will limit the number of retries. A heatmap may help show which image region influenced a compatible model, but it will not be treated as a measured disease area.

To show a severity percentage, I would need marked diseased regions and a separate test of the area estimate. This is a later task rather than a result assumed in the first prototype.
''')

report('Software and dashboard','''
| Part | Planned software and purpose |
| ESP32 program | C++ with the Arduino framework to read and send sensor data |
| Wireless messages | MQTT on the local Wi-Fi network |
| Application service | Python and FastAPI to receive data and handle image requests |
| Image work | PyTorch for models and OpenCV for image handling |
| Data analysis | scikit-learn; XGBoost if needed for a later comparison |
| Storage | SQLite initially, with separate folders for images |
| Dashboard | React and TypeScript for the browser interface |

## Information to save
For each reading, I will save the node, zone, time, value, unit and reading status. For each photograph, I will save the plant, zone, capture time and label source. Each prediction will include the model version and the input records used.

If a node disconnects, the dashboard will show its last contact time. Old readings will not be displayed as new ones. I will also keep backups of the data and experiment notes.

## Main screens
1. **Overview:** readings from both zones and connection status.
2. **Leaf scan:** select the plant and upload or capture an image.
3. **Result:** image finding, environmental conditions and any request for another observation.
4. **History:** graphs, earlier scans and notes about plant care.
5. **Management notes:** reviewed information with its source and review date.

The first application will run locally on a laptop. I will build the basic data flow before adding the remaining screens.
''')

report('Testing and expected evidence','''
| Test | What I will record |
| Image classification | Accuracy, precision, recall, macro-F1 and confusion matrix |
| Different capture conditions | Separate results for controlled and less controlled images |
| Unclear / unfamiliar input | Incorrectly accepted cases and cases sent for review |
| Sensor readings | Calibration checks, missing readings and differences between sensors |
| Wireless operation | Both node IDs, data gaps and reconnect behaviour |
| Extra observations | Number of rescans, extra readings and change in errors |
| Speed | Time from image submission to displayed result on the laptop |

## First working-demo checks
I plan to run both nodes together and complete a 24-hour logging test. I will check the percentage of expected readings received; 95% is a proposed target for a controlled test. I will also disconnect and reconnect one node to check how the application handles missing data.

For each zone, I will capture a photograph and verify that it links to the correct readings. I will show at least one unclear or unsupported input to test the review message.

## Comparing methods fairly
I will use the same test cases when comparing the decision methods. I will change one main part at a time so that I can see what caused an improvement or failure. I will report the errors and limitations along with the best results.

I have not fixed an accuracy claim at this stage. The results will depend on the dataset, labels and completed experiments.
''')

_schedule=_old_report['Work plan and review milestones']
_schedule=_schedule.replace("Time is counted from the guide's scope review, not backdated. The following is a provisional 180-day plan; it should be shortened or adjusted to the official submission calendar.","I propose the following 180-day schedule from the next scope review. I will adjust it with my guide according to the official submission date and the availability of parts and data.")
_schedule=_schedule.replace('Reviewable output','Output for review').replace('Signed-off scope notes','Agreed scope notes').replace('no AI claims yet','basic sensor test').replace('four full paper notes','detailed notes for four papers').replace('fusion feasibility decision','decision on the data available for fusion').replace('bounded rescan behaviour','limited rescan process').replace('ablation results','results with and without each main part').replace('Ablation results','Results with and without each main part').replace('data-ready extensions','extensions with suitable data')
_schedule=_schedule.replace('At the end of the first week, show the guide','At the end of the first week, I will show my guide').replace('Record any guide-requested change','I will record any change suggested by my guide').replace('Do not add every interesting feature to the first build. Protect time for evaluation and writing.','I will keep enough time for testing and report writing before adding more features.')
report('Work plan and review milestones',_schedule)

report('Resources and expected outcome','''
## Resources
The physical-parts estimate is **INR 18,150**. With a 20% reserve of **INR 3,630**, the proposed total is **INR 21,780**. The separate funding proposal lists the items and alternatives. I will obtain quotations before purchase. A laptop will be used for processing; it is not included in this hardware request.

| Possible difficulty | How I plan to manage it |
| Too many features | Finish tomato integration and the main comparison first |
| Limited disease data | Keep forecasting for later and report the available evidence |
| Costly wetness sensors | Check exact-model quotations and discuss the configuration |
| Weak results on new images | Examine failed examples and report separate external-test results |
| Missing or drifting readings | Keep raw values, calibration notes and connection status |
| Delay in parts | Continue paper reading and dataset preparation |

## Expected outcome
I aim to complete a two-node prototype, a local dashboard, a comparison of four image models and an experiment on handling unclear or incomplete inputs. I will submit the design, code, data records, results and limitations in the final report.

## Possible research paper
After the experiments, I will discuss with my guide whether the results are suitable for a paper. The paper would explain the problem, previous work, proposed method, comparisons and findings. The results section will be written after testing.

For the next review, I need guidance on the main research question, plant-label verification and which optional tasks should be kept for later.
''')

report('Future scope and guide feedback','''
## Future scope
After the college prototype is tested, the system could be developed for a field pilot. Sensor boxes would send readings over the internet, and images would be uploaded from a phone or camera. The main AI processing would run on a **VPS / cloud server**. A field gateway, if needed, would only help with communication.

Before such a pilot, I would need to test the system on more plants and conditions, improve the enclosure and check running costs. This is a later possibility; the present report focuses on the college prototype.

## Points for discussion
| Point | Guide's feedback |
| Tomato-first scope and two-node setup | ______________________________ |
| Main research question | ______________________________ |
| Datasets and plant-label support | ______________________________ |
| Hardware and budget | ______________________________ |
| Optional tasks to keep for later | ______________________________ |
| Next review and submission schedule | ______________________________ |

Review date: ____________________    Next review: ____________________

Task 1: ________________________________________________________

Task 2: ________________________________________________________

Task 3: ________________________________________________________

Student: Simran Batwal | Roll number: 28452500003

Guide: Dr. Anil Kumar | Signature: ____________________
''')

# Rework formal funding language without changing quantities or figures.
FUND=list(__import__('original_content').FUND)
FUND[0]=('Request for project components','''
To: Dr. Anil Kumar, Project Guide

Computer Science, Guru Nanak Dev University, Amritsar

**Subject: Request for financial support for PlantGuard project components**

Respected Sir,

I am Simran Batwal, roll number 28452500003, a student of M.Tech, Computer Science, 3rd Semester. I request financial support for the components required for my project, **AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN**. The system name is **PlantGuard**.

I plan to build a college prototype with two tomato plants, two ESP32 wireless sensor nodes, environmental sensors and a camera. A laptop-based application will receive the readings, process leaf images and display the results. I will begin implementation after discussing the scope with you.

The estimated cost of physical components and consumables is **INR 18,150**. I have included a 20% reserve of **INR 3,630** for price changes and necessary charges. The total amount requested for consideration is **INR 21,780**.

A laptop is not included in this request. I will check the availability of the camera, network equipment and laboratory tools before purchase. The camera allowance and optional light sensors can be removed if they are not needed. Cloud services and a separate AI processing box are not part of this proposal.

I have attached the item-wise estimate. I will obtain quotations for the selected models and follow the department's purchase and reimbursement procedure. Kindly review the requirement and advise on the components and funding support that can be approved.

Yours faithfully,

**Simran Batwal**

Roll number: 28452500003

Date: ____________________    Signature: ____________________
''')

def natural(t):
    changes={
    'an existing laptop-based application':'a laptop-based application','an existing laptop':'a laptop','the existing laptop':'the laptop','existing laptop':'laptop','Existing laptop':'Laptop',
    'indicative allowances':'estimated costs','provisional allowances':'estimated costs','planning allowances':'estimated costs','Planning ceiling':'Proposed total','planning ceiling':'proposed total','Planning unit':'Estimated unit',
    'approval ceiling':'requested total','procurement contingency':'reserve for purchase costs','procurement':'purchase','Procurement':'Purchase','configuration':'setup','Configuration':'Setup','quotation discipline':'checking quotations','Quotation discipline':'Checking quotations',
    'All amounts are in INR. Quantities cover **two nodes** unless stated otherwise. Unit figures are estimated costs, not current vendor offers; obtain quotations for the exact selected variants before purchase.':'All amounts are in INR. The quantities cover **two nodes** unless stated otherwise. These are initial estimates. I will confirm the prices and exact models through quotations before purchase.',
    'No supplier has been selected and no purchase order has been issued through this proposal.':'I will select suppliers after checking their quotations and the department\'s requirements.',
    'These alternatives preserve both wireless nodes and both leaf-wetness plates.':'Each of these options includes two nodes and two wetness plates.',
    'All signatures and approval fields are left blank for the actual institutional process.':'',
    'This document is a request, not an issued sanction.':'',
    'They are not vendor quotations or a claim that a particular pictured brand fits the allowance.':'They show the type of component required. The actual model and cost will be checked before purchase.',
    'they are not vendor quotations or a claim that a particular pictured brand fits the allowance.':'they show the required component type. I will check the actual model and price before purchase.',
    'The photographs are manufacturer/product-family references. They explain the required categories;':'The photographs help identify the components;',
    'The separate quote-comparison sheet supplied with this pack is blank for actual offers and receipts.':'I will record supplier prices and receipts in a separate comparison sheet.',
    }
    for a,b in changes.items():t=t.replace(a,b)
    return t
FUND=[(natural(t),natural(b)) for t,b in FUND]
FUND[1]=('Itemised estimate 1: electronics','''
All amounts are in INR. The quantities cover two nodes. These are initial estimates; I will confirm the exact models and prices through quotations before purchase.

@bom 0 10

## Points I will check before purchase
I will select two matching ESP32 boards and data-capable USB cables. I will check that the sensor breakout boards and communication interfaces work with the selected 3.3 V logic.

The leaf-wetness sensor is the largest part of the estimate. I will obtain a quotation for the exact RS485 Modbus model and check its supply voltage, cable, output units and register details. The INR 3,500 unit cost is an allowance for planning.

The power allowance will cover the regulated supplies required by the selected parts. I will check the sensor supply and ESP32 signal connections separately before assembly.

BH1750 is optional. Removing both light sensors would reduce the parts subtotal by INR 300. The first prototype can work without light measurement.
''')
FUND[2]=('Itemised estimate 2: setup and total','''
@bom 10 19

@totals

I have included a 20% reserve for price changes, tax, delivery and small necessary accessories where these are not already included. I will record the actual amount paid against each invoice and avoid adding the same charge twice.

If the final quotations exceed the approved amount, I will discuss a revised setup or budget before purchase.
''')
FUND[3]=('Cost-saving options','''
| Setup | Subtotal | 20% reserve | Proposed total |
| Full proposed setup | 18,150 | 3,630 | 21,780 |
| Use an available camera | 16,650 | 3,330 | 19,980 |
| Remove optional BH1750 pair | 17,850 | 3,570 | 21,420 |
| Available camera, no BH1750 pair | 16,350 | 3,270 | 19,620 |

## How I plan to reduce the cost
I will first check whether a phone or camera can capture clear close-up leaf images. If it is suitable, I will not need the webcam allowance. I will also check the availability of laboratory tools and network equipment.

I can begin assembly with the controller, soil sensor and air sensor. After checking the first readings and the wetness-sensor quotation, I can add the wetness plate and its interface. The completed wireless setup will still use two nodes.

The optional BH1750 pair can be kept for later. If any main sensor has to be removed because of cost or availability, I will discuss the change with my guide and update the experiment plan.

## Checking supplier offers
I will compare offers for the same technical model, including cable, supply requirements, tax, delivery and warranty. I will record the quoted and paid amounts separately. Supplier selection will follow the department's procedure.
''')
FUND[4]=('Component photographs and setup','''
@photos esp32 soil sht31 leaf bh1750 enclosure

These photographs show the required types of components. I will confirm the actual model, price and electrical details before purchase. The product-source links are provided below each image.

## Plants and camera
I will use two labelled pots with drainage trays, two similar tomato seedlings and a common batch of potting medium. The plant stakes and soft ties will provide support. A stable camera stand will help me capture repeatable close-up images.

## Other equipment
A laptop will run the application. I will check whether the phone/camera, Wi-Fi access point, multimeter, soldering station and basic hand tools are available in the laboratory or can be arranged separately. They are not additional purchases in this estimate.

The enclosures and supports will protect the prototype from loose wiring and accidental splashes. Air-sensor shields and wetness-plate supports are included in the setup allowance.
''')
FUND[5]=('Purchase process and approval','''
## Proposed purchase process
1. I will discuss the component list and final setup with my guide.
2. I will check the laboratory inventory and collect the quotations required by the department.
3. I will follow the approved purchase, advance or reimbursement procedure.
4. On receiving the parts, I will check the model, quantity, condition, supply requirements and operation.
5. I will keep invoices and a parts record. Reusable items will be recorded according to departmental rules.
6. At the review, I will show the working setup, readings and a statement of the actual expenditure.

## Approval details
| Field | Entry |
| Proposed total | INR 21,780 |
| Approved amount / changes | ______________________________ |
| Funding source / reference | ______________________________ |
| Purchase route | Department purchase / advance / reimbursement |
| Guide's recommendation | ______________________________ |
| Approving authority | ______________________________ |
| Signature and date | ______________________________ |

## Use of the components
The components will support sensor calibration, wireless communication and the connection between leaf images and sensor readings. I will use them to build and test the PlantGuard college prototype. Reusable items can support further laboratory work according to departmental rules.

Simran Batwal | Roll number: 28452500003
''')

_human_literature={
"PlantGuard's contribution must be narrower and experimentally demonstrated, such as behaviour under poor-quality or missing inputs":"I will focus on testing the use of unclear images and missing sensor information in the college setup",
'Record answers in the paper-reading tracker before making stronger claims.':'I will record these details in my paper notes.',
'Before adopting the method, examine event labels, time splits and what information is available before disease onset.':'In my detailed reading, I will check event labels, time splits and the information available before disease onset.',
'general pretrained knowledge and task-adapted knowledge':'general pretrained knowledge and knowledge learned for plant classification',
'Maintain a clean internal test set and a separate external-condition evaluation. Record where images came from and prevent related images crossing the split':'I will keep separate tests for familiar and different capture conditions. I will also record image sources and keep related images in the same split',
'Use supported tomato classes as an external challenge set after verifying label compatibility. Do not attach invented environmental readings to these images':'I will check the tomato labels and use suitable examples to test the image models under different conditions. These images will be used separately from my locally recorded sensor data',
'Use the study to distinguish current diagnosis from prospective forecasting and to motivate time-aligned data collection. Do not claim early warning until it is measured on independent future events':'I will use this study to understand the difference between current diagnosis and future warning. I will collect matching timestamps and test early warning only if suitable disease-event records are available',
'Use this work as a reference for domain variation and checking the dataset. Include only compatible classes and permitted data in a college experiment':'I will use this work to understand changes in image conditions. I will check the classes and permission to use the data before including it',
'Add unsupported-condition and inadequate-image outcomes. Compare rejection behaviour against a simple validation-tuned confidence baseline, using an untouched unknown test set':'I will include unclear and unsupported images in my tests. I will compare a simple confidence threshold with the proposed review process using separate test examples',
'Archive newly collected examples for expert review. Any later model update should be versioned, tested and reversible. Automatic self-training from PlantGuard\'s own predictions is outside the initial prototype':'I will save new examples for review. If I later update the model, I will check both old and new tasks and keep the earlier version available',
'The college dashboard should present a small, expert-reviewed management knowledge base with traceable sources and review dates. It should not invent chemical products or doses':'I will prepare a small set of reviewed management notes with their sources and review dates. Treatment-specific details will need suitable expert checking',
}
for i,(t,b) in enumerate(REPORT):
    if t.startswith('Literature'):
        for a,c in _human_literature.items():b=b.replace(a,c)
        REPORT[i]=(t,b)
SUMMARY='''
**AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN**

Simran Batwal | M.Tech, Computer Science | 3rd Semester

Guru Nanak Dev University, Amritsar | Roll number: 28452500003

## Current progress
I have discussed the topic with my guide and prepared an initial plan. Preliminary paper reading has started. Detailed reading, dataset preparation, hardware assembly and coding are the next steps.

## Proposed college setup
Two tomato pots and two ESP32 Wi-Fi nodes will collect soil-moisture response, air temperature, humidity and leaf wetness. A phone / USB camera will capture leaf images. A laptop will run the AI, database and dashboard.

@miniarch

## Previous work and my study
Image classification and image-sensor fusion have already been studied. I will compare four image models and focus on unclear images, old or faulty readings, and requests for fresh observations. I want to check whether this process reduces errors compared with a simpler image-only method.

## Main tests
I will compare classification results, rejected inputs, extra photographs requested, missing readings and response time. Trained fusion needs paired labels. Forecasting and other crop extensions will depend on suitable data.

## Budget and next steps
Physical-parts estimate: **INR 18,150 + INR 3,630 reserve = INR 21,780**. Next, I will agree the scope, complete core paper notes, download and check datasets, and begin the first sensor node.

## Points for guide review
Main research question, data and plant-label support, hardware choices, optional tasks and the next review date.

Guide: Dr. Anil Kumar | Review date: __________ | Next review: __________
'''

HANDBOOK=[(t,natural(b)) for t,b in __import__('original_content').HANDBOOK]
HANDBOOK[0]=(HANDBOOK[0][0],HANDBOOK[0][1].replace('aapne kuch preliminary papers dekhe hain','aapne kuch papers ki preliminary reading ki hai'))
HANDBOOK=[(t,b.replace('Is report mein eight selected briefs hain.','Report mein eight papers ke initial notes hain.').replace('Report ke literature briefs ek starting aid hain.','Report ke paper summaries se overview lo; original methods bhi padho.').replace('Prepared specifically for Simran Batwal\'s initial PlantGuard review. Use the formal report for academic submission and this Hinglish handbook for preparation.','Is handbook ko revision ke liye use karo. Formal report aur cost proposal guide ko dikhane ke liye hain.')) for t,b in HANDBOOK]

# Extra teaching sections are added below; their examples are illustrative, not project results.
LESSONS=[]
def lesson(t,b):LESSONS.append((t,b.strip()))

lesson('Hardware basics: current, voltage and wires','''
## Pehle circuit ka meaning
Circuit electrical current ke liye connected path hai. Power source energy deta hai; component apna kaam karta hai; return path circuit complete karta hai. Sensor signal aur sensor power alag connections ho sakte hain.

| Term | Simple meaning and use |
| Voltage, V | Electrical potential difference. Component ko uski specified voltage deni hoti hai. |
| Current, A / mA | Charge flow ki rate. Supply ko required current safely provide karna chahiye. |
| Resistance, ohm | Current flow ka opposition. Resistor current limit ya signal level set kar sakta hai. |
| Ground, GND | Circuit ka reference point. Non-isolated sensor interfaces usually common reference use karte hain. |
| DC / AC | DC ki polarity fixed hoti hai; AC periodically direction badalta hai. Boards regulated low-voltage DC use karenge. |
| Power, W | Energy-use rate. DC example: 5 V x 0.2 A = 1 W. Yeh sirf calculation example hai. |
| Regulator / adapter | Required supply level provide karta hai. Supply voltage aur logic voltage same hona zaroori nahi. |
| Polarity | Positive aur negative ka correct orientation. |
| Fuse | Excess current par circuit open karne wala protective component. |
| Short circuit | Unintended very-low-resistance path; component damage ho sakta hai. |

## Common viva follow-up
**5 V USB laga hai toh GPIO bhi 5 V hai?** Nahi. Selected ESP32 logic 3.3 V hai. Board ka power input aur signal-pin rating different hain.

**Multimeter kya karta hai?** Voltage, resistance aur suitable mode mein current measure karta hai. Continuity mode connection check karne mein help karta hai. Current measurement ka connection voltage measurement se different hota hai; lab guidance ke saath use karna.
''')

lesson('ESP32, chip, module and development board','''
@photos esp32 soil sht31
## ESP32 kya hai?
ESP32 Espressif ki microcontroller family ka naam hai. Hamare selected classic module mein a 32-bit processor, memory interfaces aur Wi-Fi support hai. “ESP” ka guessed full form bolne ki zarurat nahi; manufacturer aur controller family identify karo [H1].

| Term | Meaning |
| Microcontroller | Processor, memory aur input/output functions wala compact control device |
| Microprocessor | Processing unit; complete system ke liye memory aur other support bhi chahiye |
| SoC | System on Chip; several system functions ek chip mein |
| WROOM-32E module | ESP32 chip aur supporting parts/antenna ko packaged module mein deta hai |
| DevKitC V4 | Development board jo module, power/USB support aur accessible pins deta hai |
| GPIO | General Purpose Input/Output; configurable signal pin |
| RAM | Working data ki temporary memory |
| Flash | Program aur stored data rakhne wali non-volatile memory |
| Clock / MHz | Processor timing rate; model performance ka akela measure nahi |

## PlantGuard mein role
ESP32 sensor values read karega, node ID add karega aur Wi-Fi se send karega. Main disease model laptop par chalega. “ESP32 AI nahi chala sakta” universal statement mat dena; hamare design mein main AI uska role nahi hai.

**Short answer:** “ESP32 is a Wi-Fi-enabled microcontroller. I will use it to collect sensor data and send readings from each plant zone.”
''')

lesson('Sensors, signals and calibration','''
## Sensor kya hota hai?
Sensor physical quantity ko usable signal mein convert karta hai. Temperature sensor heat-related condition measure karta hai; camera light ko image data mein convert karti hai. Controller signal ko read karta hai.

| Term | Meaning / example |
| Analog signal | A range mein continuously varying signal, jaise probe voltage |
| Digital signal | Discrete values / encoded messages, jaise I2C reading |
| ADC | Analog-to-Digital Converter; voltage ko numerical reading banata hai |
| Resolution | Smallest distinguishable step; high resolution automatically high accuracy nahi |
| Accuracy | Reading true/reference value ke kitni close hai |
| Precision | Repeat readings kitni closely agree karti hain |
| Calibration | Reference observations se reading ka relationship check / establish karna |
| Noise | Unwanted variation; repeated values fluctuate kar sakti hain |
| Drift | Time ke saath sensor response ka change |
| Sampling interval | Do measurements ke beech time; 60 s interval = one reading per minute |
| Raw value | Sensor/ADC se mila original output, conversion se pehle |
| Unit | Quantity ka scale, jaise degree Celsius, % RH ya lux |

## Example
Agar dono sensors same place par hain aur consistently different readings dete hain, pehle placement, power, calibration aur reference check karenge. Sirf average lena fault ka solution nahi hai.

**Why ADC1?** Classic ESP32 par Wi-Fi ke saath ADC2 use mein restrictions hain. Isliye soil reading ke liye ADC1 pin propose hai. Exact board aur software documentation check hogi [H1].
''')

lesson('Soil, air and light measurements','''
## Capacitive soil sensor
Capacitance electrical charge store karne ki property hai. Probe ke aas-paas medium ki properties change hone se uska response badalta hai. Water content ke saath relation useful ho sakta hai, lekin medium aur installation bhi reading affect karte hain. Resistive probes exposed electrodes ke beech conductivity-based response lete hain; dono types interchangeable calibration nahi rakhte [H2].

**Relative moisture index:** selected dry/wet reference responses ke comparison ka number. **VWC:** Volumetric Water Content, yani total soil volume mein water volume ka fraction. Cheap probe ka raw number automatically VWC nahi hai.

## SHT31
SHT31 ek sensor model hai jo air temperature aur relative humidity measure karta hai. Breakout board connections accessible banata hai. SHT31 ko leaf se chipkana nahi; representative air location aur ventilated shield chahiye [H3].

**Relative humidity:** current temperature par air ke water-vapour level ka saturation ke relative measure. **Dew point:** temperature jahan cooling par condensation start ho sakti hai. High RH aur actual leaf wetness ek hi measurement nahi hain.

## BH1750 and DHT22
BH1750 optional illuminance sensor hai. **Lux** human-vision-weighted light level hai. **PAR** photosynthesis-relevant wavelength region ko refer karta hai; plant-light measurements often photon flux use karti hain. Lux ko directly PAR mat bolo [H6].

DHT22 air temperature/RH ka alternative sensor model hai. Selected design mein SHT31 use hoga; dono kharidna necessary nahi.

**Viva answer:** “Soil, air humidity and surface wetness are different measurements. They provide context; no single reading proves a disease.”
''')

lesson('Leaf wetness and RS485 interface','''
## Artificial leaf-wetness plate
Yeh leaf-like exposed surface par moisture response measure karti hai. Isko canopy ke paas separate support par place karenge. Plate dry ya wet kitni der rahi, uska record environmental context de sakta hai. Sensor model ke output units aur threshold ko manual/calibration se confirm karna hai [H4].

**Leaf-wetness duration:** selected threshold ke according surface wet rehne ka time. **Threshold:** decision boundary; jaise raw response ke kis value par “wet” count karna hai. Threshold guess karke universal disease rule nahi banega.

## RS485 and Modbus
**RS485** electrical communication standard hai. Differential signalling mein receiver do signal lines ke difference ko reads karta hai. **Modbus RTU** message rules define karta hai: device address, function, register aur error-check information. RS485 electrical layer hai; Modbus message protocol. Dono same term nahi.

**MAX3485** 3.3 V RS485 transceiver family hai. Transceiver transmit aur receive dono karta hai. ESP32 UART signals aur RS485 lines ke beech interface chahiye. A common 5 V MAX485 module ko bina logic check direct substitute nahi karenge [H5].

| Term | Meaning |
| Register | Sensor protocol mein addressed data location |
| Baud rate | Serial signalling rate; communicating sides ki setting match honi chahiye |
| Parity / stop bit | Serial framing settings |
| A/B lines | Differential pair labels; supplier polarity instructions check karo |
| Termination | Cable-end matching resistance where the bus design requires it |
| DE / RE | Driver/receiver enable controls on relevant transceiver modules |

**Short answer:** “The wetness plate measures a proxy surface. MAX3485 helps my ESP32 communicate with the selected RS485 sensor.”
''')

lesson('Pins, buses and Arduino programming','''
## Arduino kya hai?
Arduino hardware aur software ecosystem hai. **Arduino Uno** ek board hai; **Arduino IDE** code likhne, compile aur upload karne ka program hai. **Arduino framework/core** supported controller ke liye programming functions deta hai. ESP32 ko compatible core ke saath program kar sakte hain; separate Uno compulsory nahi [T1].

| Term | Simple meaning |
| Firmware | Controller par chalne wala program |
| Sketch | Arduino environment mein program/project |
| setup() | Program start/reset par initial setup ke liye runs once |
| loop() | Setup ke baad repeatedly called main work function |
| Compile | Source code ko machine-executable form mein convert karna |
| Upload / flash | Compiled program ko board par write karna |
| Serial Monitor | Sent text/values dekhkar debugging karne ka tool |
| Library | Reusable code, jaise SHT31 read karne ke functions |
| I2C | Inter-Integrated Circuit; SDA data aur SCL clock lines wala addressed bus |
| UART | Universal Asynchronous Receiver/Transmitter; TX/RX serial communication |
| SPI | Serial Peripheral Interface; clock, data aur selection signals wala bus |
| Pull-up resistor | Signal ko defined high level par hold karta hai when not pulled low |

## Hamare interfaces
SHT31 aur optional BH1750 I2C use karenge. Soil probe ADC input use karegi. RS485 interface UART se connect hogi. Candidate pins report mein hain; exact board confirm karke final wiring banegi.

**C++ versus Python:** ESP32 firmware C++/Arduino framework mein; laptop processing Python mein. Dono programs ka role alag hai.
''')

lesson('Pots, cables, enclosure and camera','''
| Item | Kya hai aur kyun chahiye? |
| Pot / tray | Root medium contain karta hai; tray drainage water collect karti hai |
| Potting medium | Roots ke liye selected growing material; same mix comparison easy karta hai |
| Seedling / cultivar | Young plant / selected plant variety; similar starting plants useful hain |
| Stake / soft tie | Plant support; labels se identity maintain hoti hai |
| Breadboard | Solderless temporary connections; internal connected rows pehle check karo |
| Jumper wire | Short connection wire; male/female ends board headers se match honge |
| USB data cable | Power ke saath data conductors; charge-only cable upload support nahi karegi |
| Terminal / connector | Wires ko secure, serviceable connection deta hai |
| Standoff / gland | Board support / enclosure mein cable entry and strain relief |
| Enclosure | Electronics ko accidental contact/splash se protect karne ka housing |
| Radiation shield | Sensor ko direct radiation se shade karta hai while allowing air circulation |
| Camera stand | Repeatable image distance aur angle maintain karta hai |

## Camera basics
**RGB** red, green, blue colour channels. **Resolution** pixel dimensions, jaise 1920 x 1080. **Focus** leaf detail ki sharpness. **Exposure** recorded brightness; too dark ya washed-out image details lose kar sakti hai. **Field of view** image mein covered scene area.

**Fixed camera** installed position se capture karti hai. **Manual scan** mein user selected leaf photograph leta hai. Hamara first setup manual close-up scanning se start karega. Camera ka sharp close focus marketing resolution se zyada relevant hai.

**IP rating:** enclosure protection classification. Drilling holes aur assembling parts ke baad finished unit ka same rating assume nahi karna.
''')

lesson('WSN, IoT, Wi-Fi and internet','''
## WSN kya hai?
**Wireless Sensor Network** multiple sensing nodes ka network hai jahan data wireless travel karta hai. Hamare Node A aur Node B different locations se readings bhejenge. **Node** sensing, controller aur communication ka unit hai. **Zone** monitored location/group ka project label hai.

## IoT kya hai?
**Internet of Things** physical devices ko networked data services se connect karne ka concept hai. Local prototype mein data services laptop par run ho sakti hain. Wi-Fi network banana aur internet access hona alag baat hai.

| Term | Simple meaning |
| Wi-Fi | Wireless local network connection |
| Access point | Wireless devices ko local network se connect karta hai |
| Router | Networks ke beech traffic forward karta hai; home unit often access point bhi hota hai |
| LAN | Local Area Network, jaise laboratory network |
| IP address | Network par device/interface ka address |
| Port | Device par particular service ka logical endpoint |
| Gateway | Networks/protocols ke beech forwarding / bridging role |
| Packet | Network par bheja data unit |
| Latency | Send/request se response tak delay |
| Bandwidth | Communication capacity; actual speed conditions par depend karti hai |
| Offline | Connection/service currently unavailable |

**Guide asks: USB laga hai, WSN kahaan hai?** “USB is for power/debugging. The sensor readings are transmitted over Wi-Fi from two identified nodes.”

**Guide asks: gateway AI karega?** “Not in this design. College AI runs on the laptop; a later field gateway would only support communication.”
''')

lesson('MQTT, messages and reliable records','''
## MQTT kaise samjho?
MQTT ek publish/subscribe messaging protocol hai, commonly IoT readings ke liye used. **Publisher** message sends karta hai. **Broker** messages receive karke interested **subscribers** ko forwards karta hai. **Topic** message channel ka name hai [T2].

Example: Node A publishes a soil reading on a zone-specific topic. Laptop broker us message ko application tak pahunchata hai. Topic names ham design karenge; yeh explanation actual implemented service nahi hai.

| Term | Why it matters |
| Payload | Message ke andar actual readings |
| JSON | JavaScript Object Notation; named fields mein structured data |
| Timestamp | Event/reading ka recorded time |
| Node ID / zone ID | Which device / location produced the reading |
| Sequence number | Message order identify karne aur gaps/duplicates detect karne ka counter |
| Duplicate | Same logical reading dobara receive hona |
| Retry / reconnect | Failed send ya connection ko dobara attempt karna |
| Buffer | Temporary waiting storage |
| Stale reading | Reading present hai, lekin ab current condition represent nahi karti |
| QoS | MQTT delivery level; handling depends on selected mode and session setup |

**Important follow-up:** MQTT QoS 1 mein duplicate delivery possible hai. Database mein repeated measurement save na ho, uske liye ID/sequence logic chahiye. Retained message ko fresh measurement mat samjho; timestamp check karna hoga.

Device clock wrong ho sakta hai. Isliye valid device time ke saath laptop receive time aur reading status bhi useful hain.
''')

lesson('Python, OpenCV and research libraries','''
## OpenCV kya hai?
**Open Source Computer Vision Library** image/video processing ke functions deti hai. PlantGuard mein camera frame lena, image load karna, resize karna aur colour order handle karna useful hoga. OpenCV khud hamara trained plant-disease model nahi hai [T3].

OpenCV images commonly BGR order mein read hoti hain; model RGB expect kare toh correct conversion chahiye. **Pixel** image ka small picture element hai. **Channel** colour component ka array hai. **Tensor** multi-dimensional numerical array hai, jise model process karta hai.

| Tool | Meaning and planned role |
| Python | Laptop-side programming language |
| NumPy | Numerical arrays aur calculations |
| pandas | Tables/time records ko organise aur analyse karna |
| PyTorch | Neural models, gradients, training aur inference ke tools |
| TorchVision | Vision models, datasets and transforms for PyTorch |
| scikit-learn | Conventional ML, data splitting aur evaluation tools |
| XGBoost | Boosted-tree library; possible later sensor-summary model |
| Matplotlib | Graphs and result plots |
| Jupyter notebook | Code, explanation and output ko research notebook mein rakhna |

**Library versus model:** library tools provide karti hai; model learned parameters se prediction karta hai. **Algorithm** steps/method hai; **program** us method ka implementation ho sakta hai.

**Viva answer:** “I will use OpenCV to prepare images and PyTorch to train and run the disease model. They have different roles.”
''')

lesson('Application, API and database basics','''
## Laptop application ke parts
**Frontend** user ko visible interface hai. **Backend** requests, data rules aur processing handle karta hai. **API**, Application Programming Interface, un parts ko defined requests/responses se communicate karne deta hai.

**FastAPI** Python web API framework hai [T4]. **Endpoint** particular API operation ka address hai. **HTTP** web request/response protocol hai; **HTTPS** encrypted transport adds karta hai. Camera upload backend endpoint par ja sakta hai.

| Term | Meaning |
| React | User interface banane ki JavaScript library |
| TypeScript | JavaScript with a type system to catch some coding mistakes |
| HTML / CSS | Page structure / appearance and layout |
| Dashboard | Readings, trends aur results ka overview screen |
| SQLite | Application ke saath lightweight file-based relational database |
| PostgreSQL | Separate database server; later larger/multi-user service option |
| SQL | Structured Query Language; relational data query/update karne ke liye |
| Table / row / column | Related records ka collection / one record / one field |
| Primary key | Record ko uniquely identify karne ka field or field set |
| Query | Stored data retrieve/filter karne ka request |
| Model version | Kaunsa trained model prediction ke liye use hua |
| Backup | Restore karne ke liye retained copy |

## Example
Frontend image submit karega. Backend file check karega, model run karega aur result record save karega. Frontend response ko readable form mein show karega. Database khud disease identify nahi karta.

**Authentication** identity check hai; **authorisation** permission check. Local prototype ke baad multi-user service mein dono useful honge.
''')

lesson('Dataset, labels and honest testing','''
## Basic terms
**Dataset** examples ka organised collection. **Label** expected category, jaise tomato early blight. **Annotation** image/record ke saath added information; disease class, bounding box ya lesion mask ho sakta hai. **Ground truth** evaluation reference label hai; expert/source quality check phir bhi needed hai.

| Term | Meaning and PlantGuard example |
| Training set | Model parameters seekhne ke examples |
| Validation set | Settings, thresholds aur model choice ke examples |
| Test set | Final evaluation ke separate examples |
| Class | Supported output category |
| Class imbalance | Some classes ke examples bahut zyada/kaafi kam |
| Duplicate / near duplicate | Same / almost same image |
| Leakage | Test-related information training or selection mein pahunch jana |
| Augmentation | Training images ka permitted variation, jaise rotation |
| Manifest | Source, licence, counts, version aur label mapping ka data record |
| Checksum | File content ka fingerprint for copy/integrity checks |
| Licence | Data use ke conditions |
| Independent sample | Another case that is not merely a closely related repeat |

## Common trap
Ek leaf ki ten similar photos ko randomly train/test mein divide kar diya toh model familiar leaf/background ko recognise kar sakta hai. Isliye related plant/session/source ko group karke split karenge. Augmentation split ke baad training set par hogi.

**PlantVillage / PlantDoc / PlantWild** dataset names hain, algorithms nahi. Unki capture conditions, class coverage aur usage terms differ karti hain. Sensor fusion ke liye photo ke saath real matching sensor history separately chahiye.
''')

lesson('AI, machine learning and neural networks','''
## Relationship
**Artificial Intelligence (AI)** intelligent tasks perform karne wale methods ka broad field hai. **Machine Learning (ML)** data se patterns learn karta hai. **Deep Learning (DL)** multi-layer neural networks use karta hai. Har AI method neural network nahi hota.

| Term | Simple explanation |
| Supervised learning | Inputs aur reference labels se learn karna |
| Classification | Category predict karna, jaise healthy / early blight |
| Regression | Numerical value predict karna |
| Detection | Image mein object/region locate karna; classification se different task |
| Segmentation | Pixels ko regions/classes mein label karna |
| Feature | Useful measurable or learned representation |
| Neural network | Connected numerical operations with learned parameters |
| Neuron / activation | Weighted input calculation and its response |
| Weight / bias | Learned numerical parameters |
| Layer | Network ka processing stage |
| Loss | Prediction error ko training ke liye numerical form dena |
| Inference | Trained model ko a new input par run karna |

## Simple flow
Leaf image numbers mein represented hoti hai. Model layers usse useful patterns extract karti hain. Final output disease categories ke scores deta hai. Training examples aur loss se weights adjust hote hain.

**Does AI understand every plant disease?** Nahi. Performance training data, task, labels aur test conditions par depend karti hai. Unknown condition ko known category force karna wrong answer de sakta hai.

**Short answer:** “Deep learning will learn image features from labelled examples. I will evaluate those predictions using separate test data.”
''')

lesson('CNN: image se features kaise bante hain','''
## CNN ka full form
**Convolutional Neural Network** images ke local patterns process karne wali network family hai. A **convolution filter/kernel** small window ki tarah image par operations karta hai. Learned filters edges, textures aur more complex patterns represent kar sakte hain.

| Term | Simple meaning |
| Feature map | Filter apply hone ke baad spatial responses |
| Stride | Filter movement ka step size |
| Padding | Border handling ke liye added values |
| Receptive field | Output response ko influence karne wala input region |
| Pooling | Nearby responses ko summarise karke spatial size reduce karna |
| ReLU | Negative input ko zero and positive ko unchanged rakhne wali activation |
| Nonlinearity | Network ko simple linear mapping se more complex patterns learn karne deta hai |
| Batch normalisation | Training mein activations normalise karne ka learned/scaled operation |
| Global average pooling | Har feature channel ko spatial average se summarise karna |
| Fully connected layer | Input features ko output scores se connect karta hai |
| Logit | Softmax se pehle raw class score |
| Softmax | Scores ko positive, sum-to-one class values mein convert karta hai |

## PlantGuard example
Input leaf image -> feature extraction -> class scores -> decision checks -> displayed result. A model may learn background shortcuts too, so image-source separation and external testing matter.

**Softmax 0.95 means guaranteed correct?** Nahi. Yeh model score hai. Confidence ka actual correctness se relation evaluate/calibrate karna padta hai. High score on a wrong or unfamiliar input possible hai.
''')

lesson('ResNet50: viva ke liye clear explanation','''
## What is ResNet50?
ResNet means **Residual Network**. ResNet50 is a standard 50-layer residual image-classification architecture. The name refers to its conventional layer depth, not 50 diseases or 50 training images. He and colleagues introduced residual learning to make deeper networks easier to train [T5].

## Skip connection kya karti hai?
Normal block input x ko transform karke F(x) output deta hai. Residual block input ko a shortcut path se add karta hai: **output = F(x) + x**, when shapes match. Agar dimensions differ hon, shortcut projection use ho sakta hai. This helps information and gradients pass through the network.

**Gradient** loss ka parameter changes ke relative direction/rate batata hai. **Vanishing gradient** mein training signal earlier layers tak bahut small ho sakta hai. Skip connections deeper-network optimisation help karti hain; har problem automatically solve nahi karti.

## Bottleneck block
ResNet50 commonly uses 1x1, 3x3 and 1x1 convolution structure: channels reduce, spatial features process, channels expand. TorchVision implementation mein specific stride placement original paper se differs; isliye library version note karenge [T6].

## PlantGuard mein use
Pretrained weights load karenge, selected disease classes ke liye output head adapt karenge aur train/validate karenge. ResNet50 comparison baseline hoga. Uska result dekhe bina use “best model” nahi kahenge.

**30-second answer:** “ResNet50 is a residual CNN with 50 layers. Its skip connections help train a deep network. I will use a pretrained ResNet50 as one of four disease-classification baselines.”
''')

lesson('MobileNetV3, EfficientNet and ViT','''
## MobileNetV3 Large
MobileNetV3 computational efficiency ke liye designed image-model family hai. It uses efficient building blocks and architecture search. **Large** variant ka name hai, “large dataset” ka requirement nahi. **Depthwise convolution** channels separately spatially process karti hai; **pointwise 1x1 convolution** channels mix karti hai [T7].

PlantGuard mein yeh speed and model-size comparison ke liye useful candidate hai. Lightweight ka matlab automatically highest accuracy nahi.

## EfficientNet-B0
EfficientNet balances model **depth** (layers), **width** (channels) and input **resolution** through compound scaling. B0 baseline architecture hai; B1/B2 etc related scaled variants hain [T8]. Main project B0 compare karega, saare variants purchase/implement nahi karega.

## Vision Transformer, ViT
ViT image ko patches mein divide karke patch representations process karta hai. **Token** patch representation hai. **Positional information** patch location indicate karti hai. **Self-attention** tokens ke relationships ko use karke representation update karti hai [T9].

**Transformer** model architecture family hai; **attention** relevant relationships weight karne ka mechanism. ViT standard CNN ke same local-convolution structure ko simply rename nahi karta. Pretrained ViT use karna small college dataset ke liye practical starting point ho sakta hai.

## Four-way comparison ka short answer
“MobileNetV3 represents an efficient CNN, ResNet50 a residual CNN, EfficientNet-B0 a balanced scaled CNN and ViT a transformer approach. I will compare their accuracy-related metrics and laptop cost using the same data split.”

Exact ViT size, image size and pretrained weights guide review and available compute ke according select honge.
''')

lesson('Training: epochs, batches and learning rate','''
| Term | Meaning |
| Pretrained weights | Another training task se learned starting parameters |
| ImageNet | Common large image dataset used for pretraining; plant-disease labels ka substitute nahi |
| Transfer learning | Earlier learned features ko related task ke liye use karna |
| Fine-tuning | Pretrained model ke selected/all weights ko new task par update karna |
| Freeze a layer | Uske weights training mein unchanged rakhna |
| Epoch | Training set ka one complete pass |
| Batch | Ek update ke liye processed examples ka group |
| Iteration / step | Usually one batch-level optimisation step |
| Learning rate | Update step ka scale |
| Optimiser | Gradient use karke weights update karne ka rule, jaise SGD / Adam |
| Backpropagation | Network ke through loss gradients calculate karna |
| Cross-entropy | Classification training mein common loss |
| Hyperparameter | Training se directly learned nahi; selected setting, jaise batch size |
| Checkpoint | Saved weights aur possibly training state |

## Example
1,000 training images aur batch size 100 ho toh one epoch normally 10 batches hoga. 20 epochs ka matlab same dataset ke 20 passes, 20 new independent datasets nahi. Yeh illustration hai; actual counts dataset audit ke baad aayenge.

**Preprocessing:** input resize aur normalisation weights ke documented transform ke according. **Normalisation:** values ko defined scale/statistics mein transform karna. Training/test preprocessing mismatch avoid karna.

**Training versus inference:** training labels/loss se weights updates karta hai; inference saved model se prediction leta hai. Report mein dono ki timing separately record karenge.
''')

lesson('Overfitting, tuning and fair comparison','''
## Overfitting versus underfitting
Overfitting mein model training data ko bahut closely fit karta hai aur new data par weak ho sakta hai. Underfitting mein model training patterns ko bhi adequately learn nahi karta. Sirf high training accuracy dekhna enough nahi.

| Term | Meaning / purpose |
| Generalisation | New appropriate examples par useful performance |
| Domain shift | Capture conditions/source changes, jaise clean background se greenhouse |
| Early stopping | Validation behaviour ke basis par training stop karna |
| Regularisation | Over-complex fitting ko discourage karne ke methods |
| Dropout | Training mein selected activations randomly suppress karna |
| Weight decay | Large weights ko penalise karne ka optimisation component |
| Random seed | Random operations ko more repeatable banane ka starting setting |
| Reproducibility | Data, settings and steps record karke result repeat karne ki ability |
| Cross-validation | Data ko multiple training/validation folds mein evaluate karna |
| Baseline | Comparison ke liye simple / established method |
| Ablation | One component remove karke uska effect measure karna |

## Fair experiment
Four models ke liye same independent split use karenge. Har model ko suitable documented preprocessing aur comparable tuning effort denge. Validation performance se settings select hongi; final test set repeatedly tune karne ke liye use nahi hoga.

**Guide asks: 99% accuracy enough hai?** “Only if the test design and data support the claim. I also need per-class results, leakage checks and testing under different capture conditions.”

Many repeated readings from two pots independence nahi badhati. Confidence intervals calculate karte waqt actual sample grouping matter karti hai.
''')

lesson('Metrics with a solved example','''
## Binary example: disease present or absent
**TP** true positive: disease present and predicted present. **TN** true negative: absent and predicted absent. **FP** false positive: absent but alarm diya. **FN** false negative: disease present but missed.

Suppose a teaching example has TP = 8, TN = 6, FP = 4 and FN = 2. Total 20 cases. These are example numbers, not PlantGuard results.

| Metric | Calculation and meaning |
| Accuracy | (TP + TN) / total = 14/20 = 70%; all cases mein correct fraction |
| Precision | TP / (TP + FP) = 8/12 = 66.7%; positive predictions mein correct fraction |
| Recall / sensitivity | TP / (TP + FN) = 8/10 = 80%; actual positives mein detected fraction |
| F1 | 2TP / (2TP + FP + FN) = 16/22 = 72.7%; precision-recall balance |
| Specificity | TN / (TN + FP) = 6/10 = 60%; actual negatives mein correct negatives |

**Confusion matrix** actual versus predicted categories ka count table. Multiclass problem mein har class ki precision/recall useful hai. **Macro-F1** each class ke F1 ka equal-weight mean hai. **Weighted-F1** class sample counts se weights use karta hai [T10].

## Other terms
**ROC curve** thresholds par true-positive versus false-positive rates show karti hai. **AUC** curve ka area hai. Rare positive cases mein precision-recall analysis bhi useful hai.

**Coverage:** system kitne inputs par answer accept karta hai. **Accepted-case error:** accepted answers mein wrong fraction. Dono together report karna; sab reject karke useful system nahi banta.

**Latency:** response delay. **Throughput:** per-time completed requests. High throughput and low individual latency different properties hain.
''')

lesson('Fusion, quality checks and unknown inputs','''
## Fusion kya hai?
Fusion different relevant data sources combine karna hai. **Modality** data type hai: image, sensor time series, text. **Early/feature fusion** features combine karti hai; **late fusion** model-level outputs/decisions combine karti hai. Har numerical average valid fusion nahi hota.

## Correct matching
Photo aur sensor history same zone aur relevant time se honi chahiye. **Time window** selected recent duration hai. **Alignment** matching identity/time arrange karna hai. **Missing modality** mein one data source absent hai; system ko us situation ka defined response chahiye.

| Term | Meaning |
| Quality check | Blur, exposure, freshness or validity test |
| Confidence | Model ka score; guaranteed correctness nahi |
| Confidence calibration | Scores aur observed correctness ka relationship check/adjust karna |
| OOD | Out of Distribution; training setting se different input |
| Open-set recognition | Known classes ke saath unknown possibilities consider karna |
| Abstention / reject | Enough support na ho toh definite category na dena |
| Fault detection | Sensor/system problem identify karna |
| Adaptive observation | Current information ke basis par another reading/image request |

## PlantGuard example
Blurred photo -> clearer image request. Stale sensor -> mark unavailable. Still unclear -> review message. Retry limit rakhenge, aur extra user effort measure karenge.

**Disagreement trap:** “healthy-looking leaf” current visual assessment ho sakti hai, “high environmental risk” future conditions ka indicator. In numbers ko subtract karke contradiction score banana meaningful nahi unless both target and scale properly defined hon.
''')

lesson('Forecasting, Random Forest and time models','''
## Detection versus prediction
Current visible disease classify karna aur future disease event forecast karna different tasks hain. **Forecast horizon** kitne time aage ka target hai. **Onset** disease start ka labelled reference time. **Lead time** valid alert onset se kitna pehle aaya. Isko real timestamps aur later confirmed events se measure karna hai.

| Method / term | Simple explanation |
| Rule baseline | Human-reviewed conditions se output; trained model nahi |
| Decision tree | Feature-based questions ke branches se prediction |
| Random Forest | Many varied trees ke outputs combine karta hai |
| Boosting | Sequential models earlier errors improve karne ki koshish karte hain |
| XGBoost | Efficient gradient-boosted-tree implementation |
| Time series | Ordered observations over time |
| Rolling mean | Recent window ka average |
| RNN | Recurrent Neural Network; sequential state process karta hai |
| LSTM | Long Short-Term Memory; gated recurrent architecture |
| GRU | Gated Recurrent Unit; another gated sequence architecture |

## Kab use karenge?
RF/XGBoost tabular sensor summaries ke candidates hain. GRU/LSTM ordered sequences handle kar sakte hain. Sirf data rows ka large count enough nahi; disease outcomes aur independent events chahiye.

**Future leakage:** disease onset ke baad ki readings use karke earlier warning claim nahi kar sakte. Evaluation mein sirf decision time tak available information use hogi.

**Short answer:** “At first I will show environmental context. A validated forecast needs separate time-labelled disease data, so it is a later data-dependent experiment.”
''')

lesson('Heatmaps, severity and model updates','''
## XAI and Grad-CAM
**Explainable AI (XAI)** model decisions inspect/understand karne ke methods hain. **Grad-CAM**, Gradient-weighted Class Activation Mapping, compatible CNN ke feature maps/gradients se influential regions highlight karta hai. Heatmap association dikhati hai; biological cause ya exact lesion boundary prove nahi karti.

**Segmentation mask** pixel-level annotation hai. **Severity** disease extent ka measure hai. Image-based area example: marked lesion pixels / marked leaf pixels. Meaningful percentage ke liye correct leaf and lesion masks, adequate image and expert-agreed method chahiye.

## Continual learning
New data/tasks aane par model update karna, while retaining earlier abilities. **Catastrophic forgetting** mein new-task training ke baad old-task performance gir sakti hai. **Regression test** checks that previously supported behaviour still works.

**Versioning** har released model identify karta hai. **Rollback** problem ke baad earlier working version restore karta hai. Self-predicted labels ko verified truth maan kar automatic retrain karna errors repeat kar sakta hai.

## Management retrieval
**Knowledge base** reviewed records ka collection. **Retrieval** relevant saved record find karna. **Embedding** text/image ka numerical representation. **Semantic similarity** meaning-based closeness. A retrieved treatment still needs correct crop, condition and source review [R8].

Hamare first prototype mein reviewed management notes possible hain. Precise pesticide dose, numeric severity and continual learning ko already implemented feature ke tarah present nahi karna.

**Viva answer:** “I will first show the evidence. A heatmap is an explanation aid, while severity and model updates require their own labels and tests.”
''')

lesson('Laptop, cloud and other project terms','''
| Term | Simple meaning / current role |
| CPU | Central Processing Unit; general-purpose processing |
| GPU | Graphics Processing Unit; parallel operations useful for neural training |
| Storage | Saved files; RAM se different |
| Edge processing | Data source ke near computation; college laptop local processing karta hai |
| VPS | Virtual Private Server; hosted virtual server for later market AI |
| Cloud | Remotely hosted computing/storage services |
| Deployment | Trained application ko usable running setup mein place karna |
| Localhost | Computer ka apna network endpoint; another node us name se laptop reach nahi karta |
| Firewall | Network traffic access rules |
| TLS | Transport Layer Security; network connection encryption |
| LoRa | Long-range radio modulation; optional later sensor communication |
| LoRaWAN | LoRa-based networking protocol/architecture; same as raw LoRa nahi |
| ESP-NOW | Espressif wireless device messaging option; first plan uses normal Wi-Fi |
| BOM | Bill of Materials; item, quantity and cost list |
| Contingency | Estimated reserve, actual spending ka proof nahi |

## Future sensor names from the wider plan
**VOC:** Volatile Organic Compounds; gas sensing needs its own study. **pH:** acidity measure. **EC:** Electrical Conductivity. **NPK:** nitrogen, phosphorus, potassium nutrient categories. **CO2:** carbon dioxide. Yeh optional future terms hain, present shopping list nahi.

**MVP / prototype:** first useful limited version / test build. **Pilot:** limited real-use trial. **WSN demo** aur **market-ready product** ki validation needs alag hain. Market plan mein main AI VPS par rahegi; separate field AI box proposed nahi.
''')

lesson('Paper, research gap and contribution','''
## Paper ke sections
**Abstract** short overview. **Introduction** problem and motivation. **Related work** previous studies. **Methodology** proposed method. **Experimental setup** data, hardware/settings and comparisons. **Results** measured findings. **Discussion** interpretation and limitations. **References** original sources.

| Term | Meaning |
| Research gap | Prior work mein a specific unresolved / insufficiently tested issue |
| Research question | Exact question experiment answer karega |
| Hypothesis | Testable expected relationship |
| Novelty | Work ka supported new aspect |
| Contribution | Study kya useful design, data or evidence adds karti hai |
| Literature review | Studies ko compare karke what is known and missing samajhna |
| DOI | Digital Object Identifier; stable scholarly identifier |
| Citation | Particular claim ka source credit/reference |
| Peer review | Other researchers ki evaluation process |
| Preprint | Public manuscript that may not yet have completed peer review |
| Limitation | Study kis conclusion ko support nahi kar sakti |

## Hamara clear answer
“Earlier studies have already done image classification and sensor fusion. I am using those methods as a base. I want to compare how the system responds to unclear images and missing or faulty sensor readings, and whether a limited request for fresh evidence reduces errors.”

**Does this guarantee a new research paper?** Nahi. Related work ka detailed review aur valid results ke baad contribution assess hogi. Four known models run karna useful benchmark ho sakta hai, lekin automatically new algorithm nahi.

Apni actual paper reading se answer do: problem, data, method, finding, limitation, my project link. Kisi result ka number uski test setting ke bina yaad karke repeat mat karo.
''')

lesson('Plant-health terms and disease labels','''
| Term | Simple meaning |
| Root zone | Medium/soil ka area around roots |
| Canopy | Plant ke above-ground leaves/branches ka covering |
| Symptom | Plant mein visible change, jaise yellowing or wilting |
| Lesion | Damaged or diseased tissue ka local area |
| Chlorosis | Green colour ka loss/yellowing |
| Necrosis | Tissue death |
| Wilting | Plant parts ka droop karna; more than one possible cause |
| Pathogen | Disease-causing biological agent |
| Infection | Pathogen ka host mein establish hona |
| Abiotic stress | Non-living cause, jaise water, heat or nutrient problem |
| Disease incidence | Observed population mein affected plants/units ka proportion |
| Disease severity | Affected plant/tissue mein damage ka extent |

**Plant health and disease are not identical.** Yellowing may arise from several causes. A photo model trained on a few diseases cannot automatically rule out water or nutrient stress. [Plant-diagnosis reference](https://extension.psu.edu/solving-the-case-of-crop-disorders-the-role-of-patterns-in-diagnosis)

## First image labels
**Healthy** is the selected dataset's reference category; one healthy-looking leaf does not prove the whole plant is disease-free. **Early blight** is a named disease associated with Alternaria species. **Late blight** is another named disease associated with Phytophthora infestans. The names are not simply early and late stages of the same illness. [Early-blight reference](https://extension.umn.edu/agriculture/specialty-crops/vegetable-farming/disease-management/early-blight-in-tomato-and-potato) | [Tomato disease reference](https://apps.extension.umn.edu/garden/diagnose/plant/vegetable/tomato/fruitrotten.html)

**Guide asks: can the camera confirm every disease?** “No. It can classify supported visual patterns. Similar symptoms and uncertain cases may need plant-expert confirmation.”
''')
LESSONS.insert(0,LESSONS.pop())

TECH_SOURCES=[
('T1','Arduino IDE and programming documentation','https://docs.arduino.cc/software/ide/'),
('T2','MQTT official overview','https://mqtt.org/'),
('T3','OpenCV basic image operations','https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html'),
('T4','FastAPI documentation','https://fastapi.tiangolo.com/'),
('T5','He et al. Deep Residual Learning for Image Recognition','https://arxiv.org/abs/1512.03385'),
('T6','TorchVision ResNet50 implementation','https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet50.html'),
('T7','Howard et al. Searching for MobileNetV3','https://arxiv.org/abs/1905.02244'),
('T8','Tan and Le. EfficientNet: Rethinking Model Scaling for CNNs','https://arxiv.org/abs/1905.11946'),
('T9','Dosovitskiy et al. An Image is Worth 16x16 Words','https://arxiv.org/abs/2010.11929'),
('T10','scikit-learn classification metrics','https://scikit-learn.org/stable/modules/model_evaluation.html'),
]
# Start with orientation, then foundations, then scripts and viva practice.
HANDBOOK=HANDBOOK[:1]+LESSONS+HANDBOOK[1:]
for offset in range(0,len(TECH_SOURCES),5):
    lines=[]
    for key,name,url in TECH_SOURCES[offset:offset+5]:lines.append(f'**{key}. {name}.** [Read the source]({url})')
    lines.append('Hardware and plant-disease paper references H1-H6 and R1-R8 are listed in the college report. Use the exact purchased sensor manual before wiring. These revision notes explain the planned system; actual settings will be recorded during implementation.')
    HANDBOOK.append(('Further reading '+str(offset//5+1),'\n\n'.join(lines)))
