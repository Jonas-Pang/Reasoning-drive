@echo off
rem One click: build the BDD100K (US) labeling workspace at the images on this PC, then open the labeling tool.
rem Workspace: DATASETS_ROOT\bdd100k   Images: DATA_DIR\extracted\bdd100k\mirror\val   (DATASETS_ROOT comes from .env)
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
rem The project may sit on the shared drive (F:), with the Python environment kept on this PC:
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
if not exist results\claude_logs mkdir results\claude_logs
"%PY%" scripts\label_bdd.py %*
if errorlevel 1 (
  echo.
  echo Something went wrong: see results\claude_logs\label_bdd.log
  pause
)
