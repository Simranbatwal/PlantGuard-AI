# AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN

System: PlantGuard

Simran Batwal | Roll number: 28452500003

M.Tech | Computer Science | 3rd Semester

Guru Nanak Dev University, Amritsar

Guide: Dr. Anil Kumar

8 September 2026 | Initial-stage proposal


# Sabse pehle project ko samjho

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
Topic discuss hua hai, initial planning hui hai aur aapne kuch papers ki preliminary reading ki hai. Coding abhi start nahi hui. Dataset download aur detailed audit next tasks hain. “Model train ho gaya” ya “dataset ready hai” tabhi kehna jab uska actual evidence ho.

# Plant-health terms and disease labels

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

# Hardware basics: current, voltage and wires

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

# ESP32, chip, module and development board

![esp32](assets/esp32.jpg)

[Product-family source](https://docs.espressif.com/projects/esp-idf/en/v4.3.6/esp32/hw-reference/esp32/get-started-devkitc.html)

![soil](assets/soil.jpg)

[Product-family source](https://www.dfrobot.com/product-1385.html)

![sht31](assets/sht31.jpg)

[Product-family source](https://www.adafruit.com/product/2857)

## ESP32 kya hai?
ESP32 Espressif ki microcontroller family ka naam hai. Hamare selected classic module mein a 32-bit processor, memory interfaces aur Wi-Fi support hai. “ESP” ka guessed full form bolne ki zarurat nahi; manufacturer aur controller family identify karo [H1](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/hw-reference/esp32/get-started-devkitc.html).

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

# Sensors, signals and calibration

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

**Why ADC1?** Classic ESP32 par Wi-Fi ke saath ADC2 use mein restrictions hain. Isliye soil reading ke liye ADC1 pin propose hai. Exact board aur software documentation check hogi [H1](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/hw-reference/esp32/get-started-devkitc.html).

# Soil, air and light measurements

## Capacitive soil sensor
Capacitance electrical charge store karne ki property hai. Probe ke aas-paas medium ki properties change hone se uska response badalta hai. Water content ke saath relation useful ho sakta hai, lekin medium aur installation bhi reading affect karte hain. Resistive probes exposed electrodes ke beech conductivity-based response lete hain; dono types interchangeable calibration nahi rakhte [H2](https://wiki.dfrobot.com/Capacitive_Soil_Moisture_Sensor_SKU_SEN0193).

**Relative moisture index:** selected dry/wet reference responses ke comparison ka number. **VWC:** Volumetric Water Content, yani total soil volume mein water volume ka fraction. Cheap probe ka raw number automatically VWC nahi hai.

## SHT31
SHT31 ek sensor model hai jo air temperature aur relative humidity measure karta hai. Breakout board connections accessible banata hai. SHT31 ko leaf se chipkana nahi; representative air location aur ventilated shield chahiye [H3](https://www.adafruit.com/product/2857).

**Relative humidity:** current temperature par air ke water-vapour level ka saturation ke relative measure. **Dew point:** temperature jahan cooling par condensation start ho sakti hai. High RH aur actual leaf wetness ek hi measurement nahi hain.

## BH1750 and DHT22
BH1750 optional illuminance sensor hai. **Lux** human-vision-weighted light level hai. **PAR** photosynthesis-relevant wavelength region ko refer karta hai; plant-light measurements often photon flux use karti hain. Lux ko directly PAR mat bolo [H6](https://www.adafruit.com/product/4681).

DHT22 air temperature/RH ka alternative sensor model hai. Selected design mein SHT31 use hoga; dono kharidna necessary nahi.

**Viva answer:** “Soil, air humidity and surface wetness are different measurements. They provide context; no single reading proves a disease.”

# Leaf wetness and RS485 interface

## Artificial leaf-wetness plate
Yeh leaf-like exposed surface par moisture response measure karti hai. Isko canopy ke paas separate support par place karenge. Plate dry ya wet kitni der rahi, uska record environmental context de sakta hai. Sensor model ke output units aur threshold ko manual/calibration se confirm karna hai [H4](https://www.renkeer.com/product/leaf-wetness-sensor/).

**Leaf-wetness duration:** selected threshold ke according surface wet rehne ka time. **Threshold:** decision boundary; jaise raw response ke kis value par “wet” count karna hai. Threshold guess karke universal disease rule nahi banega.

## RS485 and Modbus
**RS485** electrical communication standard hai. Differential signalling mein receiver do signal lines ke difference ko reads karta hai. **Modbus RTU** message rules define karta hai: device address, function, register aur error-check information. RS485 electrical layer hai; Modbus message protocol. Dono same term nahi.

**MAX3485** 3.3 V RS485 transceiver family hai. Transceiver transmit aur receive dono karta hai. ESP32 UART signals aur RS485 lines ke beech interface chahiye. A common 5 V MAX485 module ko bina logic check direct substitute nahi karenge [H5](https://www.analog.com/en/products/max3485.html).

| Term | Meaning |
| Register | Sensor protocol mein addressed data location |
| Baud rate | Serial signalling rate; communicating sides ki setting match honi chahiye |
| Parity / stop bit | Serial framing settings |
| A/B lines | Differential pair labels; supplier polarity instructions check karo |
| Termination | Cable-end matching resistance where the bus design requires it |
| DE / RE | Driver/receiver enable controls on relevant transceiver modules |

**Short answer:** “The wetness plate measures a proxy surface. MAX3485 helps my ESP32 communicate with the selected RS485 sensor.”

# Pins, buses and Arduino programming

## Arduino kya hai?
Arduino hardware aur software ecosystem hai. **Arduino Uno** ek board hai; **Arduino IDE** code likhne, compile aur upload karne ka program hai. **Arduino framework/core** supported controller ke liye programming functions deta hai. ESP32 ko compatible core ke saath program kar sakte hain; separate Uno compulsory nahi [T1](https://docs.arduino.cc/software/ide/).

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

# Pots, cables, enclosure and camera

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

# WSN, IoT, Wi-Fi and internet

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

# MQTT, messages and reliable records

## MQTT kaise samjho?
MQTT ek publish/subscribe messaging protocol hai, commonly IoT readings ke liye used. **Publisher** message sends karta hai. **Broker** messages receive karke interested **subscribers** ko forwards karta hai. **Topic** message channel ka name hai [T2](https://mqtt.org/).

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

# Python, OpenCV and research libraries

## OpenCV kya hai?
**Open Source Computer Vision Library** image/video processing ke functions deti hai. PlantGuard mein camera frame lena, image load karna, resize karna aur colour order handle karna useful hoga. OpenCV khud hamara trained plant-disease model nahi hai [T3](https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html).

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

# Application, API and database basics

## Laptop application ke parts
**Frontend** user ko visible interface hai. **Backend** requests, data rules aur processing handle karta hai. **API**, Application Programming Interface, un parts ko defined requests/responses se communicate karne deta hai.

**FastAPI** Python web API framework hai [T4](https://fastapi.tiangolo.com/). **Endpoint** particular API operation ka address hai. **HTTP** web request/response protocol hai; **HTTPS** encrypted transport adds karta hai. Camera upload backend endpoint par ja sakta hai.

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

# Dataset, labels and honest testing

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

# AI, machine learning and neural networks

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

# CNN: image se features kaise bante hain

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

# ResNet50: viva ke liye clear explanation

## What is ResNet50?
ResNet means **Residual Network**. ResNet50 is a standard 50-layer residual image-classification architecture. The name refers to its conventional layer depth, not 50 diseases or 50 training images. He and colleagues introduced residual learning to make deeper networks easier to train [T5](https://arxiv.org/abs/1512.03385).

## Skip connection kya karti hai?
Normal block input x ko transform karke F(x) output deta hai. Residual block input ko a shortcut path se add karta hai: **output = F(x) + x**, when shapes match. Agar dimensions differ hon, shortcut projection use ho sakta hai. This helps information and gradients pass through the network.

**Gradient** loss ka parameter changes ke relative direction/rate batata hai. **Vanishing gradient** mein training signal earlier layers tak bahut small ho sakta hai. Skip connections deeper-network optimisation help karti hain; har problem automatically solve nahi karti.

## Bottleneck block
ResNet50 commonly uses 1x1, 3x3 and 1x1 convolution structure: channels reduce, spatial features process, channels expand. TorchVision implementation mein specific stride placement original paper se differs; isliye library version note karenge [T6](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet50.html).

## PlantGuard mein use
Pretrained weights load karenge, selected disease classes ke liye output head adapt karenge aur train/validate karenge. ResNet50 comparison baseline hoga. Uska result dekhe bina use “best model” nahi kahenge.

**30-second answer:** “ResNet50 is a residual CNN with 50 layers. Its skip connections help train a deep network. I will use a pretrained ResNet50 as one of four disease-classification baselines.”

# MobileNetV3, EfficientNet and ViT

## MobileNetV3 Large
MobileNetV3 computational efficiency ke liye designed image-model family hai. It uses efficient building blocks and architecture search. **Large** variant ka name hai, “large dataset” ka requirement nahi. **Depthwise convolution** channels separately spatially process karti hai; **pointwise 1x1 convolution** channels mix karti hai [T7](https://arxiv.org/abs/1905.02244).

PlantGuard mein yeh speed and model-size comparison ke liye useful candidate hai. Lightweight ka matlab automatically highest accuracy nahi.

## EfficientNet-B0
EfficientNet balances model **depth** (layers), **width** (channels) and input **resolution** through compound scaling. B0 baseline architecture hai; B1/B2 etc related scaled variants hain [T8](https://arxiv.org/abs/1905.11946). Main project B0 compare karega, saare variants purchase/implement nahi karega.

## Vision Transformer, ViT
ViT image ko patches mein divide karke patch representations process karta hai. **Token** patch representation hai. **Positional information** patch location indicate karti hai. **Self-attention** tokens ke relationships ko use karke representation update karti hai [T9](https://arxiv.org/abs/2010.11929).

**Transformer** model architecture family hai; **attention** relevant relationships weight karne ka mechanism. ViT standard CNN ke same local-convolution structure ko simply rename nahi karta. Pretrained ViT use karna small college dataset ke liye practical starting point ho sakta hai.

## Four-way comparison ka short answer
“MobileNetV3 represents an efficient CNN, ResNet50 a residual CNN, EfficientNet-B0 a balanced scaled CNN and ViT a transformer approach. I will compare their accuracy-related metrics and laptop cost using the same data split.”

Exact ViT size, image size and pretrained weights guide review and available compute ke according select honge.

# Training: epochs, batches and learning rate

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

# Overfitting, tuning and fair comparison

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

# Metrics with a solved example

## Binary example: disease present or absent
**TP** true positive: disease present and predicted present. **TN** true negative: absent and predicted absent. **FP** false positive: absent but alarm diya. **FN** false negative: disease present but missed.

Suppose a teaching example has TP = 8, TN = 6, FP = 4 and FN = 2. Total 20 cases. These are example numbers, not PlantGuard results.

| Metric | Calculation and meaning |
| Accuracy | (TP + TN) / total = 14/20 = 70%; all cases mein correct fraction |
| Precision | TP / (TP + FP) = 8/12 = 66.7%; positive predictions mein correct fraction |
| Recall / sensitivity | TP / (TP + FN) = 8/10 = 80%; actual positives mein detected fraction |
| F1 | 2TP / (2TP + FP + FN) = 16/22 = 72.7%; precision-recall balance |
| Specificity | TN / (TN + FP) = 6/10 = 60%; actual negatives mein correct negatives |

**Confusion matrix** actual versus predicted categories ka count table. Multiclass problem mein har class ki precision/recall useful hai. **Macro-F1** each class ke F1 ka equal-weight mean hai. **Weighted-F1** class sample counts se weights use karta hai [T10](https://scikit-learn.org/stable/modules/model_evaluation.html).

## Other terms
**ROC curve** thresholds par true-positive versus false-positive rates show karti hai. **AUC** curve ka area hai. Rare positive cases mein precision-recall analysis bhi useful hai.

**Coverage:** system kitne inputs par answer accept karta hai. **Accepted-case error:** accepted answers mein wrong fraction. Dono together report karna; sab reject karke useful system nahi banta.

**Latency:** response delay. **Throughput:** per-time completed requests. High throughput and low individual latency different properties hain.

# Fusion, quality checks and unknown inputs

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

# Forecasting, Random Forest and time models

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

# Heatmaps, severity and model updates

## XAI and Grad-CAM
**Explainable AI (XAI)** model decisions inspect/understand karne ke methods hain. **Grad-CAM**, Gradient-weighted Class Activation Mapping, compatible CNN ke feature maps/gradients se influential regions highlight karta hai. Heatmap association dikhati hai; biological cause ya exact lesion boundary prove nahi karti.

**Segmentation mask** pixel-level annotation hai. **Severity** disease extent ka measure hai. Image-based area example: marked lesion pixels / marked leaf pixels. Meaningful percentage ke liye correct leaf and lesion masks, adequate image and expert-agreed method chahiye.

## Continual learning
New data/tasks aane par model update karna, while retaining earlier abilities. **Catastrophic forgetting** mein new-task training ke baad old-task performance gir sakti hai. **Regression test** checks that previously supported behaviour still works.

**Versioning** har released model identify karta hai. **Rollback** problem ke baad earlier working version restore karta hai. Self-predicted labels ko verified truth maan kar automatic retrain karna errors repeat kar sakta hai.

## Management retrieval
**Knowledge base** reviewed records ka collection. **Retrieval** relevant saved record find karna. **Embedding** text/image ka numerical representation. **Semantic similarity** meaning-based closeness. A retrieved treatment still needs correct crop, condition and source review [R8](https://doi.org/10.1186/s13007-023-01070-6).

Hamare first prototype mein reviewed management notes possible hain. Precise pesticide dose, numeric severity and continual learning ko already implemented feature ke tarah present nahi karna.

**Viva answer:** “I will first show the evidence. A heatmap is an explanation aid, while severity and model updates require their own labels and tests.”

# Laptop, cloud and other project terms

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

# Paper, research gap and contribution

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

# Meeting ka 10-minute sequence

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
“Sir/Ma'am, mere project ka title AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN hai. System ka naam PlantGuard hai. Abhi topic discussion, initial planning aur preliminary literature reading hui hai. Main coding se pehle aapse scope aur research direction review karwana chahti hoon. College prototype ke liye do tomato pots, do ESP32 sensor nodes aur laptop propose kiya hai.”

## Phir next line
“Mera focus sirf image classification par nahi, balki unclear image, stale sensor reading aur missing data mein system ka reliable behaviour evaluate karna hai. Iske liye main aapko proposed architecture aur comparisons dikhati hoon.”

Guide beech mein question karein toh sequence ko force mat karo. Pehle unka question answer karo, feedback note karo, phir relevant page se continue karo.

# Har component ko kaise explain karein

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

# AI aur data ke basic words

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

# Guide ke questions 1: scope aur novelty

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

# Guide ke questions 2: hardware aur sensing

## 9. Arduino aur ESP32 dono kharidoge?
“Nahi, selected controller ESP32 hai. Arduino framework programming ke liye use ho sakta hai; separate Uno required nahi.”

## 10. AI ESP32 mein chalegi?
“Main disease model laptop par chalega. ESP32 sensors read, status track aur wireless data transmit karega.”

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

# Guide ke questions 3: data aur evaluation

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

# Guide ke questions 4: papers aur delivery

## 26. Kaunse papers padhe? Kya samjha?
“Preliminary reading shuru ki hai. Report mein eight papers ke initial notes hain. Jo papers full padhe hain unke methods aur limitations apne notes se explain karungi; baaki ko reading queue ke roop mein identify karungi.”

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

# Research paper padhne ka practical tareeka

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

Report ke paper summaries se overview lo; original methods bhi padho. Guide ke saamne apni actual reading depth clearly batana. “All papers fully read” tabhi kehna jab methods aur key limitations explain kar pao.

Separate editable **Paper_Reading_Tracker.md** mein apne notes fill karo. Paper ke PDF ko cite karo, AI-generated summary ko primary research source mat banao.

# Meeting ke pehle aur baad kya karna hai

## Meeting se pehle
1. One-page summary aur report architecture page do baar samjho.
2. R1 aur R2 ke original papers kholkar abstract, dataset aur limitations padho; apne five-line notes banao.
3. Naam, roll number 28452500003 aur guide Dr. Anil Kumar ki details check karo. Date actual submission wali use kar sakte ho.
4. Funding proposal mein borrowed camera / tools ki availability mark karo. Estimate ko quotation mat bolo.
5. Laptop par PDFs aur source links ready rakho; printed summary saath le ja sakte ho.

## Guide se yeh decisions lo
“Kya tomato-first scope suitable hai?” “Main reliability-aware diagnosis par focus karun ya forecasting ke liye dataset access available hai?” “Four-model comparison appropriate hai?” “Plant labels verify karne ke liye expert support mil sakta hai?” “Next review mein kaunsa output priority hoga?”

## Funding request ko kaise rakhein
“Sir/Ma'am, main pehle available laboratory resources reuse karna chahti hoon. Remaining two-node components ka separate estimate attach hai. Aap setup aur purchase route suggest kar dein; exact quotations uske according final karungi.”

## Closing script
“Aaj ki discussion se main agreed scope aur changes note kar rahi hoon. Agli meeting tak main priority paper notes, dataset audit aur approved hardware plan dikhaugi. Kya main in three deliverables aur next review date ko note kar loon?”

## Meeting ke baad
Same day feedback sheet complete karo. Har action ke liye owner, due date aur evidence likho. Report ka next version banao; previous version preserve karo. Guide ne scope change bola ho toh pehle plan revise karo, phir implementation start karo.

Kal ka practical first task: R1/R2 reading notes aur dataset manifest template. Isse guide discussion aur subsequent coding dono clearer honge.

# Mock viva and action record

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
Meeting date: ____________________    Guide: Dr. Anil Kumar

Main feedback: __________________________________________________

Scope change: __________________________________________________

Paper / method suggested: ________________________________________

| Action | Due date | Evidence to show |
| ______________ | __________ | __________________ |
| ______________ | __________ | __________________ |
| ______________ | __________ | __________________ |

Next meeting: ____________________

Is handbook ko revision ke liye use karo. Formal report aur cost proposal guide ko dikhane ke liye hain.

# Further reading 1

**T1. Arduino IDE and programming documentation.** [Read the source](https://docs.arduino.cc/software/ide/)

**T2. MQTT official overview.** [Read the source](https://mqtt.org/)

**T3. OpenCV basic image operations.** [Read the source](https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html)

**T4. FastAPI documentation.** [Read the source](https://fastapi.tiangolo.com/)

**T5. He et al. Deep Residual Learning for Image Recognition.** [Read the source](https://arxiv.org/abs/1512.03385)

Hardware and plant-disease paper references H1-H6 and R1-R8 are listed in the college report. Use the exact purchased sensor manual before wiring. These revision notes explain the planned system; actual settings will be recorded during implementation.

# Further reading 2

**T6. TorchVision ResNet50 implementation.** [Read the source](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet50.html)

**T7. Howard et al. Searching for MobileNetV3.** [Read the source](https://arxiv.org/abs/1905.02244)

**T8. Tan and Le. EfficientNet: Rethinking Model Scaling for CNNs.** [Read the source](https://arxiv.org/abs/1905.11946)

**T9. Dosovitskiy et al. An Image is Worth 16x16 Words.** [Read the source](https://arxiv.org/abs/2010.11929)

**T10. scikit-learn classification metrics.** [Read the source](https://scikit-learn.org/stable/modules/model_evaluation.html)

Hardware and plant-disease paper references H1-H6 and R1-R8 are listed in the college report. Use the exact purchased sensor manual before wiring. These revision notes explain the planned system; actual settings will be recorded during implementation.
