@echo off
rem Written by Claude: open the China (MapDR) labeling from THIS copy of the project. A labeling tool still running on
rem port 8765 (for example the old one started from D:) is stopped first, so the labels are saved in this copy.
for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":8765 " ^| findstr LISTENING') do (
  tasklist /fi "PID eq %%p" | findstr /i python >NUL && taskkill /PID %%p /F
)
timeout /t 2 >NUL
call "%~dp0label_mapdr.bat" %*
