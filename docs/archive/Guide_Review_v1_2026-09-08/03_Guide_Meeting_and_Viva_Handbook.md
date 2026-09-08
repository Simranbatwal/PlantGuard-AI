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
Topic discuss hua hai, initial planning hui hai aur aapne kuch preliminary papers dekhe hain. Coding abhi start nahi hui. Dataset download aur detailed audit next tasks hain. “Model train ho gaya” ya “dataset ready hai” tabhi kehna jab uska actual evidence ho.

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
“Sir/Ma'am, mere project ka title AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN hai. System ka naam PlantGuard hai. Abhi topic discussion, initial planning aur preliminary literature reading hui hai. Main coding se pehle aapse scope aur research direction review karwana chahti hoon. College prototype ke liye do tomato pots, do ESP32 sensor nodes aur existing laptop propose kiya hai.”

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

Report ke literature briefs ek starting aid hain. Guide ke saamne apni actual reading depth clearly batana. “All papers fully read” tabhi kehna jab methods aur key limitations explain kar pao.

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
“Sir/Ma'am, main pehle available laboratory resources reuse karna chahti hoon. Remaining two-node components ka separate estimate attach hai. Aap configuration aur purchase route suggest kar dein; exact quotations uske according final karungi.”

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

Prepared specifically for Simran Batwal's initial PlantGuard review. Use the formal report for academic submission and this Hinglish handbook for preparation.
