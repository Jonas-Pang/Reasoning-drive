# Lane tests on HiPerGator (UF)

Written by Claude, 2026-11-16. Runs the Gemma 4 models (Ollama, the same downloads as on the laptop) on a HiPerGator GPU.
Only Google's Gemma 4: UF does not allow language models from countries of concern on UF computing resources
(https://docs.rc.ufl.edu/software/apps/ollama), so no Qwen here.

## 1. Make the bundle (Windows, once)
Double-click `scripts\claude_hpg_bundle.bat`. It writes `F:\Project\reasoning_drive_hpg.zip`: the project without
`.env`, keys, caches and logs, plus the two labeling workspaces (the selected MapDR and BDD100K frames).

## 2. Copy it to HiPerGator
Open OnDemand (https://ood.rc.ufl.edu) -> Files -> `/blue/<your group>/<you>/` -> Upload the zip. Then in a terminal
(Clusters -> HiPerGator Shell Access):

    cd /blue/$(id -gn)/$USER
    unzip -q reasoning_drive_hpg.zip
    cd reasoning_drive_hpg/Reasoning_Drive
    bash hpg/setup.sh

## 3. Run
    sbatch hpg/run_lane.sbatch                          # L4 (24 GB), all three models, dev and test, Tests A-R
    sbatch --partition=hpg-b200 hpg/run_lane.sbatch     # a B200 (180 GB) instead
    PROFILES="hpg_gemma4_12b" SPLITS="dev" TESTS="A,B" sbatch hpg/run_lane.sbatch    # a part
    squeue -u $USER                                     # is it running?
    tail -f hpg_logs/rd_lane_<job>.log                  # progress

A job that hits the time limit continues where it stopped when submitted again (answers are cached).

## 4. Bring the results back
    cd /blue/$(id -gn)/$USER/reasoning_drive_hpg/Reasoning_Drive
    zip -qr ../hpg_results.zip results/runs configs/lane_protocol__hpg_*.json results/claude_logs/lane_eval_*hpg_*.log hpg_logs -x 'results/runs/cache/*'

Download `hpg_results.zip` in Open OnDemand -> Files and unzip it into `F:\Project\Reasoning_Drive` (the run folders
have new names, nothing on F: is overwritten). Then `python scripts/claude_lane_report.py --split test` shows all models.
