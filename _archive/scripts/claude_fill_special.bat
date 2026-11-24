@echo off
rem Written by Claude: fill the empty lane-change cells next to a bus, HOV or tidal lane (see
rem scripts\claude_fill_special.py). The China labeling tool is stopped first (it keeps the labels in memory) and
rem opened again afterwards. A backup of every changed file goes to results\claude_logs\backup_special_<time>.
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
for /L %%i in (1,1,3) do (
  for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":8765 " ^| findstr LISTENING') do taskkill /PID %%p /T /F
  timeout /t 1 >NUL
)
"%PY%" -u scripts\claude_fill_special.py
echo.
echo Opening the China labeling tool again ...
call "%~dp0label_mapdr.bat"
