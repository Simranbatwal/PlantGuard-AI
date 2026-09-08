# PlantGuard AI

Working project folder for the college prototype and future VPS-based market product.

## Start here

- [Final illustrated master plan](docs/Master_Plan_2026-09-08/PlantGuard_Final_Master_Plan.pdf)
- [Editable master plan](docs/Master_Plan_2026-09-08/PlantGuard_Master_Plan_Editable.md)
- [Procurement checklist](docs/Master_Plan_2026-09-08/Procurement_Checklist.md)
- [Logo and component images](docs/Master_Plan_2026-09-08/assets/)
- [Original supplied planning notes](docs/Master_Plan_2026-09-08/reference/Supplied_Latest_Plan.txt)

## Project decisions

- System name: PlantGuard.
- College: two ESP32 wireless sensor nodes, camera, local laptop AI and dashboard.
- Market: all disease AI processing runs on a VPS. Sensor Boxes collect and transmit. An optional gateway only bridges communications.
- The latest supplied written plan and the user's VPS clarification control the design. Earlier images are visual references only.
- Earlier master roadmap: 180 calendar days, with INR 24,180 including optional compute and contingency. See the current hardware-only guide proposal below.
- Status: planning package complete; implementation has not started.

## Work folders

- hardware: BOM, wiring, sensor calibration and enclosure designs.
- firmware: ESP32 source and device configuration.
- backend: API, storage, treatment retrieval and inference integration.
- frontend: dashboard and scan interface.
- ml: model training, evaluation and model cards.
- data: licensed datasets and consented field observations.
- experiments: measured results and reproducibility logs.
- deployment: future VPS configuration and operating instructions.

Update this file and the decision log as implementation progresses. Keep private farm data and credentials out of public repositories.


## Current college guide review pack - 8 September 2026

- Student: Simran Batwal, roll number 28452500003.
- Programme: M.Tech, Computer Science, 3rd Semester, Guru Nanak Dev University, Amritsar.
- Guide: Dr. Anil Kumar.
- Latest user-confirmed title: **AI-Powered Plant Health Monitoring and Disease Detection Using IoT & WSN**. System: **PlantGuard**.
- [One-page guide summary](docs/Guide_Review_2026-09-08/04_One_Page_Guide_Summary.pdf)
- [Detailed college report](docs/Guide_Review_2026-09-08/01_College_Prototype_Guide_Report.pdf)
- [Separate hardware funding proposal](docs/Guide_Review_2026-09-08/02_Hardware_Funding_Proposal.pdf)
- [Hinglish meeting and viva handbook](docs/Guide_Review_2026-09-08/03_Guide_Meeting_and_Viva_Handbook.pdf)
- [Editable files, reading tracker and meeting templates](docs/Guide_Review_2026-09-08/README.md)
- [Complete review pack ZIP](PlantGuard_Guide_Review_2026-09-08.zip)

This pack is the current college proposal for guide review. Its title and confirmed student details supersede older wording. Topic discussion, initial planning and some preliminary reading have occurred. Dataset download/audit and coding are planned; no training or experiments have been completed.

The hardware-only funding ceiling is INR 21,780 (INR 18,150 + 20% contingency). It excludes the older master plan's optional INR 2,000 compute reserve and associated INR 400 contingency. Estimates are not vendor quotations. Tomato-first integration is the proposed core; extensions depend on data, time and guide feedback. The 180-day plan is provisional and starts from scope review.

College AI runs on a laptop. Future market AI runs on VPS/cloud; no separate field AI processing box is proposed. Preserve this review edition and record actual guide feedback before implementation.

## Updated reports and writing style

The current guide folder contains the revised 25-page college report, 7-page funding proposal, 41-page beginner viva handbook and one-page summary. The formal documents use simple first-person English and separate previous research, current progress and proposed work. The handbook explains project terminology in Hinglish with examples and viva answers.

The earlier guide pack is preserved at `docs/archive/Guide_Review_v1_2026-09-08/`. The main ZIP has been refreshed. Future document preferences are saved in AGENTS.md; use “laptop” and natural language, and state actual progress directly.
