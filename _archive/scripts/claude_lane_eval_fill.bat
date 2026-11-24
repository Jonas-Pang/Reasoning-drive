@echo off
rem Written by Claude: the dev lane runs that did not finish on 2026-11-15 (China Test C: dropped connection;
rem Test R of both countries: needs the Test A run). See scripts\claude_lane_eval.py.
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
if not exist results\claude_logs mkdir results\claude_logs
title Lane tests (dev, missing runs) - close to stop
"%PY%" -u scripts\claude_lane_eval.py --regions CN --tests C,R
"%PY%" -u scripts\claude_lane_eval.py --regions US --tests R
echo.
pause
