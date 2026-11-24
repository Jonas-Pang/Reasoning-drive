#!/bin/bash
# Written by Claude, 2026-11-16: the lane tests with Gemma 4 (Ollama) on a HiPerGator GPU.
# Submit from the project folder:      sbatch hpg/run_lane.sbatch
#   an L4 (24 GB) instead:             sbatch --partition=hpg-turin hpg/run_lane.sbatch
# Course QoS egn5216 allows per user at most cpu=2, gpu=2, mem=16G (sacctmgr, 2026-11-16), so this job asks for
# exactly that; more CPUs are refused (QOSMaxCpuPerUserLimit). hpg-b200 accepts it but often waits long for a GPU.
#   only some models / splits / tests: PROFILES="hpg_gemma4_12b" SPLITS="dev" TESTS="A,B" sbatch hpg/run_lane.sbatch
# Models: configs/api_profiles.yaml (hpg_*). UF policy allows no models from countries of concern on UF computing
# resources, so only Google's Gemma 4 here. Each model and split runs once; answers already received are cached, so a
# job that stops (time limit) continues where it stopped when submitted again. Log: hpg_logs/rd_lane_<job>.log
#SBATCH --job-name=rd_lane
#SBATCH --partition=hpg-rtx6000
#SBATCH --gpus=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=16gb
#SBATCH --time=24:00:00
#SBATCH --output=hpg_logs/rd_lane_%j.log
set -u
cd "${SLURM_SUBMIT_DIR:-$(dirname "$0")/..}"
mkdir -p hpg_logs
PROFILES="${PROFILES:-hpg_gemma4_e4b hpg_gemma4_12b hpg_gemma4_31b}"
SPLITS="${SPLITS:-dev test}"
TESTS="${TESTS:-A,B,C,D,R}"
ENV="${RD_VENV:-$(cd .. && pwd)/venv}"
PY="$ENV/bin/python"
echo "=== $(date)  node $(hostname)  gpu: $(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>/dev/null)"
echo "profiles: $PROFILES  splits: $SPLITS  tests: $TESTS"

module load ollama
export OLLAMA_MODELS="${OLLAMA_MODELS:-/blue/$(id -gn)/$USER/ollama_models}"
PORT=$((20000 + ${SLURM_JOB_ID:-0} % 20000))         # an own port: other jobs may share the node
export OLLAMA_HOST="127.0.0.1:$PORT"
export RD_OLLAMA_URL="http://127.0.0.1:$PORT"
mkdir -p "$OLLAMA_MODELS"
ollama serve > "hpg_logs/ollama_${SLURM_JOB_ID:-x}.log" 2>&1 &
OPID=$!
trap 'kill $OPID 2>/dev/null' EXIT
# UF's ollama module wraps the command and serves on 0.0.0.0:11434 whatever OLLAMA_HOST says (seen 2026-11-16,
# module ollama 0.33.0), so use whichever of the two addresses answers.
for i in $(seq 90); do
  for u in "http://127.0.0.1:$PORT" "http://127.0.0.1:11434"; do
    curl -s "$u/api/version" >/dev/null && { RD_OLLAMA_URL="$u"; break 2; }
  done
  sleep 2
done
export RD_OLLAMA_URL
export OLLAMA_HOST="${RD_OLLAMA_URL#http://}"
echo "ollama $(curl -s "$RD_OLLAMA_URL/api/version")  models in $OLLAMA_MODELS"

for p in $PROFILES; do
  m=$("$PY" -c "import yaml,sys; print(yaml.safe_load(open('configs/api_profiles.yaml'))['profiles']['$p']['name'])")
  echo; echo "### $p ($m)"
  ollama pull "$m" || { echo "pull $m failed"; continue; }
  for s in $SPLITS; do
    "$PY" -u scripts/claude_lane_eval.py --api "$p" --split "$s" --tests "$TESTS"
  done
done
for s in $SPLITS; do "$PY" scripts/claude_lane_report.py --split "$s"; done
echo "=== done $(date)"
