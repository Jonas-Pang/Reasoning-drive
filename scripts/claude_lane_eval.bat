@echo off
rem Written by Claude: lane tests with the real API on the final lane labels (see scripts\claude_lane_eval.py).
rem Default: dev split, China (MapDR) and US, tests A B C D R. Extra arguments are passed on, e.g. --split test
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
if not exist results\claude_logs mkdir results\claude_logs
title Lane tests (dev) - close to stop
"%PY%" -u scripts\claude_lane_eval.py %*
echo.
pause
