@echo off
rem Written by Claude: ONE labeling window for every country in configs\labeling_regions.json (China, US, UK, India), at http://127.0.0.1:8780/
rem (see scripts\label_all.py). Stops any labeling tool already open on 8765-8768 / 8780 first. (8770 is left free for the demo and blind-review page.)
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
if not exist results\claude_logs mkdir results\claude_logs
for /L %%i in (1,1,3) do (
  for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":8765 :8766 :8767 :8768 :8780" ^| findstr LISTENING') do taskkill /PID %%p /T /F >NUL 2>&1
  timeout /t 1 >NUL
)
title Labeling - CN / US / UK / IN (close to stop)
"%PY%" -u scripts\label_all.py %*
if errorlevel 1 pause
