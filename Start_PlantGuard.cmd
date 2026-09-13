@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo PlantGuard Python environment is missing. See docs\Phase_3_2026-09-13\README.md.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" "tools\launch_plantguard.py"
if errorlevel 1 pause
