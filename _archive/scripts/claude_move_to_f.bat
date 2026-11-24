@echo off
rem Written by Claude: copy the project to F:\Project\Reasoning_Drive (next to the data folder on F:), so the same copy runs on
rem Windows and on the Mac. D:\Project\Reasoning_Drive is left as it is (a backup). Safe to run again: only newer
rem files are copied (files changed on F: are kept). Not copied: .venv (each computer keeps its own Python), .vscode, caches.
rem Then scripts\claude_move_check.py fixes the paths in the F: copy and runs a small check (a few cents of API).
set SRC=D:\Project\Reasoning_Drive
set DST=F:\Project\Reasoning_Drive
if not exist F:\Project (
  echo F: is not connected.
  pause
  exit /b 1
)
if not exist "%SRC%\results\claude_logs" mkdir "%SRC%\results\claude_logs"
echo Copying %SRC% to %DST% ...
robocopy "%SRC%" "%DST%" /E /XD .venv .vscode __pycache__ .pytest_cache .ipynb_checkpoints /XF ._* /XO /R:1 /W:1 /NP /NFL /NDL /LOG:"%SRC%\results\claude_logs\move_robocopy.log"
if %ERRORLEVEL% GEQ 8 (
  echo Copying failed: see %SRC%\results\claude_logs\move_robocopy.log
  pause
  exit /b 1
)
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%SRC%\.venv\python.exe
if not exist "%PY%" set PY=%SRC%\.venv\Scripts\python.exe
if not exist "%DST%\results\claude_logs" mkdir "%DST%\results\claude_logs"
echo Checking the copy on F: (log: %DST%\results\claude_logs\move_check.log) ...
"%PY%" -u "%DST%\scripts\claude_move_check.py" %*
echo.
echo Finished. Log: %DST%\results\claude_logs\move_check.log
pause
