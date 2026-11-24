@echo off
rem Written by Claude, 2026-11-16: pack the project for HiPerGator -> F:\Project\reasoning_drive_hpg.zip (see hpg\README.md)
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
"%PY%" -u scripts\claude_hpg_bundle.py
pause
