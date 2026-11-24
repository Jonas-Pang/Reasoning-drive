#!/bin/bash
# Written by Claude, 2026-11-16. Run ONCE on HiPerGator, from the project folder:   bash hpg/setup.sh
# Creates the Python environment next to the project (../venv), installs requirements.txt and lists the lane items.
set -e
cd "$(dirname "$0")/.."
module load python/3.11 2>/dev/null || module load python
ENV="${RD_VENV:-$(cd .. && pwd)/venv}"
[ -x "$ENV/bin/python" ] || python3 -m venv "$ENV"
"$ENV/bin/python" -m pip install --upgrade pip -q
"$ENV/bin/python" -m pip install -r requirements.txt -q
echo "Python environment: $ENV ($("$ENV/bin/python" --version))"
"$ENV/bin/python" main.py lane items --region CN --split dev
"$ENV/bin/python" main.py lane items --region US --split dev
echo
echo "Ready. Start the lane runs with:   sbatch hpg/run_lane.sbatch   (RTX PRO 6000 by default)"
echo "  inside an Open OnDemand Desktop instead:   mkdir -p hpg_logs; SLURM_SUBMIT_DIR=\$PWD bash hpg/run_lane.sbatch 2>&1 | tee hpg_logs/desktop_run.log"
