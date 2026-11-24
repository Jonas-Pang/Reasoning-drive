@echo off
setlocal
rem Creates the project environment in .venv (Python 3.11 and the packages of requirements.txt), then runs the self-test.
rem Uses conda if it is installed (CONDA_EXE, or D:\AnaConda), otherwise the Python launcher (py -3.11).
rem VS Code then finds .venv by itself (Python: Select Interpreter), and Terminal > Run Task runs the project.
cd /d "%~dp0\.."
set ENV=%CD%\.venv
set PY=%ENV%\python.exe
if exist "%ENV%\Scripts\python.exe" if not exist "%PY%" set PY=%ENV%\Scripts\python.exe
if exist "%PY%" goto install

set CONDA=
if defined CONDA_EXE set CONDA=%CONDA_EXE%
if not defined CONDA if exist "D:\AnaConda\condabin\conda.bat" set CONDA=D:\AnaConda\condabin\conda.bat
if defined CONDA (
  echo Creating .venv with conda ...
  call "%CONDA%" create -y -p "%ENV%" -c conda-forge --override-channels python=3.11
  set PY=%ENV%\python.exe
) else (
  echo Creating .venv with py -3.11 ...
  py -3.11 -m venv "%ENV%"
  set PY=%ENV%\Scripts\python.exe
)
if not exist "%PY%" (
  echo Could not create .venv: install Python 3.11 or Anaconda, then run this again.
  exit /b 1
)

:install
"%PY%" -m pip install --upgrade pip
"%PY%" -m pip install -r requirements.txt
"%PY%" main.py selftest
endlocal
