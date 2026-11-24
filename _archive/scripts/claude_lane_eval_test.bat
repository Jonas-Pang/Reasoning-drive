@echo off
rem Written by Claude: lane tests with the real API on the final lane labels (see scripts\claude_lane_eval.py).
rem TEST split (held out; prompt lane_v3 frozen on 2026-11-16), China (MapDR) and US, tests A B C D R.
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
if not exist results\claude_logs mkdir results\claude_logs
title Lane tests (TEST split) - close to stop
"%PY%" -u scripts\claude_lane_eval.py --split test %*
echo.
pause
