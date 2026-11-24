#!/bin/bash
# Rebuild and start the demo (app + Prometheus + Grafana), then check the Video tab end to end with Mock answers
# (no API cost): clips 08 (US and China rules) and 04. Double-click in Finder, or: bash scripts/run_demo_check.command
# Log: results/app/run_demo_check.log. Written by Claude, 2026-11-18.
cd "$(dirname "$0")/.." || exit 1
export PATH="/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin:$PATH"
mkdir -p results/app
LOG=results/app/run_demo_check.log
{
echo "== $(date '+%H:%M:%S') start"
docker info >/dev/null 2>&1 || { echo "STOP: Docker is not running"; exit 1; }
echo "== 1/4 build (first time 5-10 min)"
bash scripts/docker_build.sh || { echo "STOP: BUILD FAILED"; exit 1; }
echo "== 2/4 start"
docker compose up -d --no-build || { echo "STOP: UP FAILED"; exit 1; }
docker compose ps
echo "== 3/4 wait for the app"
ok=0
for i in $(seq 1 90); do
  if curl -fs http://localhost:8770/healthz >/dev/null 2>&1; then ok=1; echo "app is up"; break; fi
  sleep 2
done
[ "$ok" = 1 ] || { echo "STOP: app did not start"; docker compose logs --tail 40 demo; exit 1; }
docker compose exec -T demo sh -c 'command -v ffmpeg && ffmpeg -hide_banner -encoders 2>/dev/null | grep -c libx264'
curl -fs http://localhost:8770/app | grep -o 'data-tab="[a-z]*"' | tr '\n' ' '; echo
echo "== 4/4 video check with Mock answers: clips 08 and 04"
python3 scripts/run_violation_clips.py --model mock --only 08 04
echo "== $(date '+%H:%M:%S') DONE"
} 2>&1 | tee "$LOG"
echo
echo "Finished. You can close this window."
