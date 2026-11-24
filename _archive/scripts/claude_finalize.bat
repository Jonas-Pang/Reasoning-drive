@echo off
rem Written by Claude: finish the CN and US lane labels (see claude_finalize.py): stops both labeling tools,
rem finalizes, writes the review and spot-check lists, then opens both tools again.
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
for /L %%i in (1,1,3) do (
  for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":8765 :8766" ^| findstr LISTENING') do taskkill /PID %%p /T /F
  timeout /t 1 >NUL
)
"%PY%" -u scripts\claude_finalize.py > results\claude_logs\finalize_run.log 2>&1
start "China labeling" cmd /c call "%~dp0label_mapdr.bat"
timeout /t 3 >NUL
start "US labeling" cmd /c call "%~dp0label_bdd.bat"
