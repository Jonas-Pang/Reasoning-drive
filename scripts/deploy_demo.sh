#!/bin/bash
# One command for the course demo (Module 8 deployment + Module 9 monitoring and feedback):
#   1. checks Docker and .env (names only, never the values)
#   2. builds the image (scripts/docker_build.sh) and starts app + Prometheus + Grafana
#   3. waits until the app answers, Prometheus reads it
#   4. sends traffic and reviewer feedback through the app (scripts/demo_traffic.py, saved answers, no cost)
#   5. opens the app, Grafana and Prometheus in the browser
# usage:  bash scripts/deploy_demo.sh            (stop later with:  docker compose down)
# Added by Claude, 2026-11-18.
set -e
cd "$(dirname "$0")/.."
step() { echo; echo "== $*"; }

step "1/5 checks"
command -v docker >/dev/null 2>&1 || { echo "Docker is not installed: install Docker Desktop for Mac (Apple chip) from docker.com, open it, then run this again."; exit 1; }
docker info >/dev/null 2>&1 || { echo "Docker is installed but not running: open Docker Desktop and wait until it says running."; exit 1; }
[ -f .env ] || { echo "No .env: copy .env.example to .env and fill it in."; exit 1; }
grep -q '^GRAFANA_ADMIN_PASSWORD=.' .env || { echo "Set GRAFANA_ADMIN_PASSWORD=... in .env (any password you choose)."; exit 1; }
if grep -q '^NAVIGATOR_API_KEY=.' .env; then echo "NAVIGATOR_API_KEY set: live answers possible"; else echo "no NAVIGATOR_API_KEY: the page works with saved answers only"; fi

step "2/5 build and start (first time a few minutes)"
bash scripts/docker_build.sh          # builds from a clean copy (the T9 drive's ._ files break docker build)
docker compose up -d --no-build
docker compose ps

step "3/5 wait for the app"
for i in $(seq 1 60); do
  if curl -fs http://localhost:8770/healthz >/dev/null 2>&1; then echo "app is up"; break; fi
  sleep 2
  [ "$i" = 60 ] && { echo "the app did not start; see: docker compose logs demo"; exit 1; }
done
sleep 20   # one or two Prometheus scrapes

step "4/5 traffic and feedback through the app"
PY="$HOME/.venvs/reasoning_drive/bin/python"; [ -x "$PY" ] || PY=python3
"$PY" scripts/demo_traffic.py --per-region 40 --delay 0.3

step "5/5 open the pages"
open http://localhost:8770/app http://localhost:3000 http://localhost:9090/targets 2>/dev/null || true
cat <<'TXT'

What to show:
  App        http://localhost:8770/app   Analyze a photo -> verification banner; Feedback tab -> submit; Monitor tab
  Grafana    http://localhost:3000       user admin, password from .env; dashboard "Lane advisor – monitoring";
                                         Alerting > Alert rules: "More than 30 % of feedback is bad" fires after about 6 min
  Prometheus http://localhost:9090       Status > Targets: demo UP; try the query  app_feedback_total
  Report     bash scripts/rd.sh --script scripts/feedback_report.py
Stop:        docker compose down
TXT
