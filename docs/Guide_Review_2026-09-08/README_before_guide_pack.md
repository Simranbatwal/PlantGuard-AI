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
- College roadmap: 180 calendar days. Planning budget: INR 24,180 including contingency, subject to quotes.
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
