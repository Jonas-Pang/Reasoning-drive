"""Reasoning Driving: one entry point for the whole project.

    python main.py web                         the web page: runs, reasoning, results, evaluation, regulations, CARLA
    python main.py run --test AB --real        Test A and Test B on the labeled images (configs/experiment.yaml)
    python main.py lane run --test AB --real   the lane task (my whole lane, one request per image)
    python main.py evaluate <run_id>           precision, recall, F1 and confusion matrices of a saved run
    python main.py results                     every saved run in one table (results/index.csv)
    python main.py regulations list            the countries in regulations/ (extract, accept, check: see --help)
    python main.py carla route route1          drive one route of configs/carla.yaml in CARLA
    python main.py label --help                the labeling tool
    python main.py selftest                    every check, without the API and without CARLA

Settings: configs/ (api.yaml, experiment.yaml, carla.yaml). The API key goes in .env (copy .env.example).
"""
import sys

from reasoning_drive.cli import main

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(__doc__)
        sys.exit(0)
    main()
