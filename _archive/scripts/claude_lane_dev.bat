@echo off
rem Runs lane tests A, B, C on the US development images with the real API (costs money), then lists the runs.
rem Arguments are passed on, e.g.  claude_lane_dev.bat --limit 2   for a smoke test.
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
rem The project may sit on the shared drive (F:), with the Python environment kept on this PC:
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
"%PY%" -u scripts\claude_lane_dev.py US %*
pause
