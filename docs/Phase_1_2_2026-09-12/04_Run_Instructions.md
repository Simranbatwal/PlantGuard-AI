# Run PlantGuard Phase 1 and 2

The local environment is ready at `.venv`. From the project folder in PowerShell:

```powershell
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/python.exe tools/data/verify.py
```

To reproduce on a fresh Python 3.12 environment, create a virtual environment and install `requirements-phase12.lock.txt`. The lock file covers data preparation and contracts, not model training. The source metadata and review CSV files are part of the release and must stay with the scripts.

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements-phase12.lock.txt
.venv/Scripts/python.exe tools/data/download.py
.venv/Scripts/python.exe tools/data/audit.py
.venv/Scripts/python.exe tools/data/verify.py
```

`download.py` uses pinned repository commits, verifies Git blob hashes and resumes valid existing files. It saves safe Windows names where the source filename contains reserved characters. Source names and URLs remain in the manifest. A download failure returns a non-zero exit code.

`audit.py` reads originals, produces SHA-256 and pixel hashes, screens 64-bit perceptual hashes (distance <=6 including horizontal mirrors), incorporates saved visual pair decisions and leaf metadata, and produces grouped splits. Do not run two audits at once. Run `verify.py` after an audit before using its outputs.

All model loaders must use the CSV manifests, never a recursive folder glob. Original images are retained even when excluded. Generated quality-case files are selected only by quality_cases.csv. This prevents excluded images or old unlisted derived files from entering a run.

The three class indices are in configs/research_protocol.json. Full training belongs to Phase 4. No trained model is included in this release.

## Colab handoff
Use ml/notebooks/Phase_2_Data_Verification.ipynb and artifacts/PlantGuard_Phase12_Colab.zip. The notebook installs the data dependencies, checks the uploaded bundle and verifies the frozen data. This is a prepared notebook; it has not been run in the user's Colab account. It does not require a GPU. Training and Drive checkpoint notebooks will follow in the model phase.

Never place API tokens, passwords or private field images in source control. The environment, raw datasets, generated data and future model weights are ignored by Git. Keep independent backups of the data and experiment results.
