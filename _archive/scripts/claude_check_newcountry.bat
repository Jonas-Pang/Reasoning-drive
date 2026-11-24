@echo off
rem Written by Claude, 2026-11-16: checks after adding UK and India (no API calls): the frozen protocol of CN/US still
rem matches, the new countries' rule files fit the template, and their prompts build. Log: results\claude_logs\check_newcountry.log
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
set LOG=results\claude_logs\check_newcountry.log
echo === %DATE% %TIME% > %LOG%
echo --- lane protocol >> %LOG%
"%PY%" main.py lane protocol --prompt lane_v3 >> %LOG% 2>&1
echo --- lane protocol --region UK >> %LOG%
"%PY%" main.py lane protocol --prompt lane_v3 --region UK >> %LOG% 2>&1
echo --- regulations list >> %LOG%
"%PY%" main.py regulations list >> %LOG% 2>&1
echo --- regulations check UK >> %LOG%
"%PY%" main.py regulations check UK >> %LOG% 2>&1
echo --- regulations check IN >> %LOG%
"%PY%" main.py regulations check IN >> %LOG% 2>&1
echo --- lane prompt B UK >> %LOG%
"%PY%" main.py lane prompt --test B --region UK --prompt lane_v3 >> %LOG% 2>&1
echo --- lane prompt C IN >> %LOG%
"%PY%" main.py lane prompt --test C --region IN --prompt lane_v3 >> %LOG% 2>&1
echo === done >> %LOG%
