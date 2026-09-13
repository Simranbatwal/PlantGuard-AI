# PlantGuard experiment records
Every training or evaluation run gets a unique folder under experiments/runs/<run_id>/.

Required records:
- config.json: architecture, pretrained weights source, seed, transforms, batch size, optimiser, learning rate, epochs and stopping rule.
- environment.json: package versions, CPU/GPU, operating system and code revision.
- dataset.json: data source/version, manifest hash, class mapping and split-list hashes.
- history.csv: per-epoch losses, validation metrics and timing.
- best checkpoint and resume checkpoint.
- metrics.json and per_class_metrics.csv.
- predictions.csv: image ID, split, true label, predicted class, scores and rejection reason.
- confusion_matrix.csv and a plot.
- learning curves, representative errors and measured inference timing.
- notes.md: purpose, observations, failures, limitations and conclusions.

Rules:
1. Keep validation selection separate from final test evaluation.
2. Save failed/interrupted runs with their status; do not retain only the best-looking outcome.
3. Keep simulated and physical sensor records separate.
4. Never copy illustrative report numbers into a measured results table.
5. Do not commit downloaded datasets, private records or large checkpoints to Git. Retain them locally or in an authorised backup.
6. Do not claim a model has finished training until the run and its outputs are verified.

The run index starts empty; there are no completed model experiments yet.
