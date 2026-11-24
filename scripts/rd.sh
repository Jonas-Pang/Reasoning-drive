#!/bin/bash
# Run the project with the Mac environment made by scripts/setup_mac.sh (~/.venvs/reasoning_drive).
#   bash scripts/rd.sh <main.py arguments>          e.g.  bash scripts/rd.sh web --mock
#   bash scripts/rd.sh --script <file.py> [args]    e.g.  bash scripts/rd.sh --script scripts/feedback_report.py
# Prints the full command first, so it can be typed by hand next time.
cd "$(dirname "$0")/.." || exit 1
PY="$HOME/.venvs/reasoning_drive/bin/python"
if [ ! -x "$PY" ]; then
  echo "No environment yet: run  bash scripts/setup_mac.sh  first (VS Code task \"0 · Setup\")." >&2
  exit 1
fi
if [ "$1" = "--script" ]; then
  shift
  echo "+ $PY $*"
  exec "$PY" "$@"
fi
echo "+ $PY main.py $*"
exec "$PY" main.py "$@"
