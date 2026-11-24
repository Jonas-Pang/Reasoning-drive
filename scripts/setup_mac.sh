#!/bin/bash
# The Mac side of the shared drive: a Python 3.11 environment in ~/.venvs/reasoning_drive (kept on the Mac, not on the
# drive), the packages of requirements.txt, then the self-test.      Run from the project:   bash scripts/setup_mac.sh
# Python 3.11 is required: the pinned packages (numpy 2.1.3, matplotlib 3.9.2, ...) have ready-made Mac wheels for it;
# with a newer Python pip tries to compile them and fails. Order of preference: an existing python3.11, else conda
# (miniconda / anaconda) makes one, else Homebrew's python@3.11.
# Updated by Claude 2026-11-18 (the first version used whatever python3 was first on PATH).
set -e
cd "$(dirname "$0")/.."
ENV="$HOME/.venvs/reasoning_drive"

ok_env() { [ -x "$ENV/bin/python" ] && "$ENV/bin/python" -c 'import sys; sys.exit(sys.version_info[:2] != (3, 11))'; }

if [ -d "$ENV" ] && ! ok_env; then
  echo "== $ENV exists but is not Python 3.11 (an earlier attempt): moving it to $ENV.old"
  rm -rf "$ENV.old"; mv "$ENV" "$ENV.old"
fi

if ! ok_env; then
  mkdir -p "$HOME/.venvs"
  if command -v python3.11 >/dev/null 2>&1; then
    echo "== Python 3.11 found: $(command -v python3.11)"
    python3.11 -m venv "$ENV"
  else
    CONDA=""
    for c in conda "$HOME/miniconda3/bin/conda" "$HOME/anaconda3/bin/conda" "/opt/homebrew/Caskroom/miniconda/base/bin/conda"; do
      if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then CONDA="$c"; break; fi
    done
    if [ -n "$CONDA" ]; then
      echo "== No python3.11 on PATH: conda makes one in $ENV"
      "$CONDA" create -y -p "$ENV" python=3.11 pip
    elif command -v brew >/dev/null 2>&1; then
      echo "== No python3.11 and no conda: installing Homebrew python@3.11"
      brew install python@3.11
      "$(brew --prefix python@3.11)/bin/python3.11" -m venv "$ENV"
    else
      echo "Python 3.11 is needed. Install Miniconda (docs.conda.io) or Homebrew, then run this script again." >&2
      exit 1
    fi
  fi
fi

echo "== $("$ENV/bin/python" --version) in $ENV"
"$ENV/bin/python" -m pip install --upgrade pip
"$ENV/bin/python" -m pip install -r requirements.txt
"$ENV/bin/python" main.py selftest || echo "(self-test: see the FAIL lines above; 4 known failures are old rule-table tests)"
echo
echo "Done. Run the project with:  bash scripts/rd.sh <command>     e.g.  bash scripts/rd.sh web --mock"
echo "VS Code: the workspace already points at $ENV/bin/python"
