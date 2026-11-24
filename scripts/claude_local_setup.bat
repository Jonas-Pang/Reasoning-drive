@echo off
rem Written by Claude, 2026-11-16: set up local models for the lane tests (Ollama on this computer, free, offline).
rem Everything goes on D: : Ollama in D:\Ollama, the models in D:\Ollama\models (about 18 GB).
rem  1. writes the graphics card and the free space on C: and D: to results\claude_logs\local_setup.log
rem  2. if Ollama is not installed: downloads the official installer from https://ollama.com/download/OllamaSetup.exe
rem     and opens it with the folder D:\Ollama - click Install yourself
rem  3. sets OLLAMA_MODELS=D:\Ollama\models for your Windows user (so Ollama keeps its models on D:) and restarts Ollama
rem  4. downloads three models: qwen3.5:9b (Mar 2026), gemma4:12b (Jun 2026), qwen3.5:4b (Mar 2026)
rem  5. tries qwen3.5:9b on 2 development images (scripts\claude_lane_eval.py --api local_qwen35_9b --limit 2)
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
set PY=%CD%\.venv\python.exe
if not exist "%PY%" set PY=%CD%\.venv\Scripts\python.exe
if not exist "%PY%" set PY=%USERPROFILE%\.venvs\reasoning_drive\Scripts\python.exe
if not exist "%PY%" set PY=D:\Project\Reasoning_Drive\.venv\python.exe
if not exist results\claude_logs mkdir results\claude_logs
set LOG=%CD%\results\claude_logs\local_setup.log
set ODIR=D:\Ollama
set OLLAMA_MODELS=D:\Ollama\models
title Local models setup - close to stop
echo === %DATE% %TIME% >> "%LOG%"
echo --- graphics card >> "%LOG%"
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv >> "%LOG%" 2>&1
echo --- free space (GB) C: and D: >> "%LOG%"
powershell -NoProfile -Command "'C: ' + [math]::Round((Get-PSDrive C).Free/1GB,1); 'D: ' + [math]::Round((Get-PSDrive D).Free/1GB,1)" >> "%LOG%" 2>&1
if not exist D:\ (
  echo Drive D: was not found. >> "%LOG%"
  echo Drive D: was not found.
  goto end
)
if not exist "%OLLAMA_MODELS%" mkdir "%OLLAMA_MODELS%"

set OLLAMA=
if exist "%ODIR%\ollama.exe" set OLLAMA=%ODIR%\ollama.exe
if not defined OLLAMA if exist "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" set OLLAMA=%LOCALAPPDATA%\Programs\Ollama\ollama.exe
if defined OLLAMA goto have_ollama
echo Ollama is not installed. Downloading the official installer from ollama.com ...
echo --- downloading OllamaSetup.exe >> "%LOG%"
powershell -NoProfile -Command "$ProgressPreference='SilentlyContinue'; Invoke-WebRequest -Uri 'https://ollama.com/download/OllamaSetup.exe' -OutFile \"$env:TEMP\OllamaSetup.exe\"" >> "%LOG%" 2>&1
if not exist "%TEMP%\OllamaSetup.exe" (
  echo Download failed - see the log. You can install Ollama yourself from https://ollama.com/download
  echo download failed >> "%LOG%"
  goto end
)
echo.
echo The Ollama installer opens now (folder D:\Ollama). Click Install, wait until it finishes, then come back here.
start /wait "" "%TEMP%\OllamaSetup.exe" /DIR="%ODIR%"
if exist "%ODIR%\ollama.exe" set OLLAMA=%ODIR%\ollama.exe
if not defined OLLAMA if exist "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" set OLLAMA=%LOCALAPPDATA%\Programs\Ollama\ollama.exe
if not defined OLLAMA (
  echo Ollama was not found after the installer. Install it, then run this file again.
  echo ollama not found after install >> "%LOG%"
  goto end
)
:have_ollama
echo --- ollama: %OLLAMA% >> "%LOG%"
"%OLLAMA%" --version >> "%LOG%" 2>&1
rem keep the models on D: (user setting read by Ollama), then restart Ollama so that it uses it
setx OLLAMA_MODELS "%OLLAMA_MODELS%" >NUL
echo --- OLLAMA_MODELS=%OLLAMA_MODELS% >> "%LOG%"
taskkill /IM "ollama app.exe" /F >NUL 2>&1
taskkill /IM ollama.exe /F >NUL 2>&1
timeout /t 2 >NUL
for %%d in ("%OLLAMA%") do set OAPP=%%~dpdollama app.exe
if exist "%OAPP%" (start "" "%OAPP%") else (start "Ollama server" /min "%OLLAMA%" serve)
timeout /t 8 >NUL

for %%m in (qwen3.5:9b gemma4:12b qwen3.5:4b) do (
  echo.
  echo Downloading %%m ...
  echo --- pull %%m >> "%LOG%"
  "%OLLAMA%" pull %%m
  if errorlevel 1 (echo pull %%m FAILED >> "%LOG%") else (echo pull %%m ok >> "%LOG%")
)
echo --- models >> "%LOG%"
"%OLLAMA%" list >> "%LOG%" 2>&1
echo --- model folder >> "%LOG%"
dir /s "%OLLAMA_MODELS%" | find "File(s)" >> "%LOG%" 2>&1

echo.
echo Trying qwen3.5:9b on 2 development images ...
"%PY%" -u scripts\claude_lane_eval.py --api local_qwen35_9b --split dev --regions US --tests A --limit 2
:end
echo.
echo Done. The log is %LOG%
pause
