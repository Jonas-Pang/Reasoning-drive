@echo off
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist results\claude_logs mkdir results\claude_logs
"%PY%" -u scripts\claude_fetch_mapdr.py > results\claude_logs\fetch_mapdr.log 2>&1
