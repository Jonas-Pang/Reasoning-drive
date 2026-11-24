@echo off
rem Written by Claude: lane tests with the real API on the final lane labels (see scripts\claude_lane_eval.py).
rem TEST split, resume after the OpenAI credits ran out on 2026-11-16: China Test R and US Tests A-R got no answers
rem (HTTP 429), so they run again with --again (recorded in each manifest). China A-D are complete and are not rerun.
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
if not exist results\claude_logs mkdir results\claude_logs
title Lane tests (TEST split, resume) - close to stop
"%PY%" -u scripts\claude_lane_eval.py --split test --again --regions CN --tests R
if errorlevel 2 goto end
"%PY%" -u scripts\claude_lane_eval.py --split test --again --regions US --tests A,B,C,D,R
:end
echo.
pause
