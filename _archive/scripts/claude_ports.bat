@echo off
rem Written by Claude: list what listens on the labeling ports (log only, changes nothing).
cd /d "%~dp0\.."
set LOG=results\claude_logs\ports.log
echo === %DATE% %TIME% > %LOG%
netstat -ano | findstr ":876" >> %LOG%
for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":876" ^| findstr LISTENING') do wmic process where ProcessId=%%p get ProcessId,CommandLine /format:list >> %LOG% 2>&1
