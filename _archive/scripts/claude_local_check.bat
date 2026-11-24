@echo off
rem Written by Claude, 2026-11-16: download the local models to D:\Ollama\models if missing, then try each on 2
rem development images.
rem Log: results\claude_logs\local_check.log (models) and results\claude_logs\lane_eval_dev_local_*.log (the tries)
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
set LOG=%CD%\results\claude_logs\local_check.log
set OLLAMA_MODELS=D:\Ollama\models
set OLLAMA=D:\Ollama\ollama.exe
if not exist "%OLLAMA%" set OLLAMA=%LOCALAPPDATA%\Programs\Ollama\ollama.exe
title Local models check - close to stop
echo === %DATE% %TIME% >> "%LOG%"
rem is the Ollama server answering? if not, start it (with the models on D:)
powershell -NoProfile -Command "try { (Invoke-WebRequest -UseBasicParsing http://127.0.0.1:11434/api/version -TimeoutSec 5).Content } catch { 'no server' }" >> "%LOG%" 2>&1
powershell -NoProfile -Command "try { Invoke-WebRequest -UseBasicParsing http://127.0.0.1:11434/api/version -TimeoutSec 5 | Out-Null; exit 0 } catch { exit 1 }"
if errorlevel 1 (
  echo starting ollama serve >> "%LOG%"
  start "Ollama server (keep open)" /min "%OLLAMA%" serve
  timeout /t 15 >NUL
)
for %%m in (qwen3.5:4b qwen3.5:9b gemma4:12b) do (
  echo.
  echo Downloading %%m if missing ...
  echo --- pull %%m >> "%LOG%"
  "%OLLAMA%" pull %%m
  if errorlevel 1 (echo pull %%m FAILED >> "%LOG%") else (echo pull %%m ok >> "%LOG%")
)
echo --- ollama list >> "%LOG%"
"%OLLAMA%" list >> "%LOG%" 2>&1
for %%p in (local_qwen35_4b local_qwen35_9b local_gemma4_12b) do (
  echo.
  echo Trying %%p on 2 development images ...
  echo --- try %%p >> "%LOG%"
  "%PY%" -u scripts\claude_lane_eval.py --api %%p --split dev --regions US --tests A --limit 2 >> "%LOG%" 2>&1
  echo exit %ERRORLEVEL% >> "%LOG%"
)
echo --- ollama ps >> "%LOG%"
"%OLLAMA%" ps >> "%LOG%" 2>&1
echo.
echo Done. The log is %LOG%
pause
