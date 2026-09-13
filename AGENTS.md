# PlantGuard project context

This is the user's ongoing PlantGuard-AI working folder.

- Read README.md and docs/Master_Plan_2026-09-08/PlantGuard_Master_Plan_Editable.md before implementation decisions.
- Follow the latest supplied written master plan. The user's confirmed market architecture runs AI on a VPS, not a field processing box.
- College processing runs on the laptop. Sensor Boxes contain sensing, power and communication electronics; an optional gateway is a communication bridge.
- Treat concept images as visual references, not authoritative wiring diagrams or evidence of tested performance.
- Preserve original reference material and keep budgets, experiments and claims distinguishable from actual measured results.
- Current status: Phase 1 foundation and Phase 2 dataset preparation complete; data scripts and telemetry contracts are implemented. Application, firmware and trained models are not yet implemented.

## Document writing preferences

- Use simple, natural, professional English in student submissions. Write in first person when describing Simran's own work and plans.
- Avoid assistant-style comments such as "the student has reported", "prepared for discussion; not a claim", and repeated disclaimers. State actual progress directly: preliminary reading and planning have started; detailed reading, data preparation and implementation are next.
- Write "laptop", not "existing laptop", in reports, plans and proposals.
- Clearly separate published previous work, the student's completed work and proposed experiments. Do not invent completed reading, data downloads, coding or measured results.
- Explain the proposed contribution in plain language and retain references for previous work. Do not add unsupported novelty claims or unnecessary features.
- Keep the viva handbook in simple Hinglish. Explain project hardware, software, algorithms, abbreviations and evaluation terms from a beginner's starting point, with examples and short viva answers.
- Preserve earlier report editions when replacing PDFs, and update the matching editable text and project index.


## Development order confirmed on 12 September 2026

- Follow docs/Software_First_Roadmap_2026-09-12.md for current timing: software, data preparation, four image-model comparisons and simulated-input tests before hardware purchase.
- The user plans to buy components only after the software checkpoint. Do not order hardware automatically.
- Preserve model configurations, seeds, split identities, checkpoints, predictions, metrics and failed runs for the thesis.
- Clearly label simulated inputs. Real sensor calibration, physical firmware validation and wireless reliability remain pending until hardware is available.

## Dataset release for implementation

- Read docs/Phase_1_2_2026-09-12/README.md and 02_Dataset_Audit.md before data/model changes.
- Use data/processed/tomato_v1 manifests, not folder globbing; excluded originals remain on disk.
- Preserve the frozen split hash and record it with every model run. Use a new dataset version for changes.
- PlantDoc is external-only in this release. Do not train or tune thresholds on external/internal/OOD test sets.
- Colab is available to the user; a notebook and bundle are prepared, but account execution and training have not yet occurred.
