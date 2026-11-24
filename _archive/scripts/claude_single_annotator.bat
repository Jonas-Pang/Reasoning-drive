@echo off
rem Written by Claude: one lane annotator per image for MapDR and BDD100K (see claude_single_annotator.py);
rem stops both labeling tools, changes the sets, then opens both tools again.
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
"%PY%" -u scripts\claude_single_annotator.py > results\claude_logs\single_annotator.log 2>&1
start "China labeling" cmd /c call "%~dp0label_mapdr.bat"
timeout /t 3 >NUL
start "US labeling" cmd /c call "%~dp0label_bdd.bat"
