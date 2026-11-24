@echo off
rem Written by Claude: open the US (BDD100K) labeling from THIS copy of the project. Labeling tools still running on
rem port 8766 (for example old ones started from D:) are stopped first, so the labels are saved in this copy.
cd /d "%~dp0\.."
if not exist results\claude_logs mkdir results\claude_logs
set LOG=results\claude_logs\label_us_restart.log
echo === %DATE% %TIME% > %LOG%
for /L %%i in (1,1,5) do (
  netstat -ano | findstr ":8766" >> %LOG%
  for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":8766 " ^| findstr LISTENING') do (
    tasklist /fi "PID eq %%p" /fo csv /nh >> %LOG%
    taskkill /PID %%p /T /F >> %LOG% 2>&1
  )
  timeout /t 1 >NUL
)
echo --- after: >> %LOG%
netstat -ano | findstr ":8766" >> %LOG%
call "%~dp0label_bdd.bat" %*
