@echo off
rem Written by Claude, 2026-11-16: the small UK and India pilot (scripts\claude_pilot_ukin.py). No API calls.
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
if not exist results\claude_logs mkdir results\claude_logs
"%PY%" -u scripts\claude_pilot_ukin.py
echo.
echo Log: results\claude_logs\pilot_ukin.log
pause
