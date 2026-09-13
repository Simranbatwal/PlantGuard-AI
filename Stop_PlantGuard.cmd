@echo off
cd /d "%~dp0"
".venv\Scripts\python.exe" "tools\launch_plantguard.py" --stop
if errorlevel 1 pause
