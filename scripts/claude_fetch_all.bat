@echo off
rem Written by Claude: fetch missing regulations, extract AU drafts, download open datasets. Log: results\claude_logs\fetch_all.log
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist results\claude_logs mkdir results\claude_logs
set LOG=results\claude_logs\fetch_all.log
set R="%PY%" scripts\claude_run.py
echo ==== start %DATE% %TIME% > %LOG%
echo ==== [1] regulations fetch AU,AU-NSW >> %LOG%
%R% regulations fetch AU,AU-NSW >> %LOG% 2>&1
echo ==== [2] regulations extract-all AU and states >> %LOG%
%R% regulations extract-all AU,AU-NSW,AU-VIC,AU-QLD,AU-SA,AU-TAS,AU-ACT,AU-NT --real --budget 5 >> %LOG% 2>&1
echo ==== [3] data fetch CN,UK >> %LOG%
%R% data fetch UK >> %LOG% 2>&1
%R% data fetch CN >> %LOG% 2>&1
echo ==== [4] data status >> %LOG%
%R% data status >> %LOG% 2>&1
echo ==== [5] regulations list >> %LOG%
%R% regulations list >> %LOG% 2>&1
echo ==== Finished %DATE% %TIME% >> %LOG%
