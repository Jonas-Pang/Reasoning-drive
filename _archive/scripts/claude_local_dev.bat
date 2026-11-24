@echo off
rem Written by Claude, 2026-11-16: the three local models (Ollama, D:\Ollama) on the DEVELOPMENT images, Tests A and B,
rem China and the US: qwen3.5:4b (about 1.5 h), gemma4:12b (about 6 h), qwen3.5:9b (about 7 h) on an RTX 2060 6 GB.
rem Free, nothing is sent out. Keep the computer plugged in and awake; closing this window stops it (answers already
rem received are kept in the cache and are not asked again). Logs: results\claude_logs\lane_eval_dev_local_*.log
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
set OLLAMA_MODELS=D:\Ollama\models
set OLLAMA=D:\Ollama\ollama.exe
title Local models, dev, Tests A and B - close to stop
powershell -NoProfile -Command "try { Invoke-WebRequest -UseBasicParsing http://127.0.0.1:11434/api/version -TimeoutSec 5 | Out-Null; exit 0 } catch { exit 1 }"
if errorlevel 1 (
  start "Ollama server (keep open)" /min "%OLLAMA%" serve
  timeout /t 15 >NUL
)
for %%p in (local_qwen35_4b local_gemma4_12b local_qwen35_9b) do (
  "%PY%" -u scripts\claude_lane_eval.py --api %%p --split dev --tests A,B
)
"%PY%" -u scripts\claude_lane_report.py --split dev
echo.
echo All done. Table: results\lane_report_dev.md
pause
