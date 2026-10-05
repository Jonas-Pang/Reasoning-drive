# Reasoning Driving

**Cross-region lane marking interpretation with a multimodal LLM** · EGN 6216 AI Systems, Fall 2026 · Jiahao Pang

The project shows a GPT model a road image from China or the US and asks what a lane marking means there. Each image is asked twice: once with the image only (Test A) and once with the matching rule text from the local standard (Test B). The comparison shows whether the rule text helps.

This repository covers the data collection stage. `playground.ipynb` downloads the datasets and rule documents, loads them into tables, shows real examples and checks the data quality.

## What the notebook does

| Section | Task |
|---|---|
| 0 Setup | Imports, paths, settings; prints Python and package versions |
| 1 BDD100K | Downloads the BDD100K validation split (official server, or the Dataset Ninja mirror when it is down) and unpacks the images and lane labels |
| 2 CULane | Checks the five CULane archives (test split) and unpacks them |
| 3 Rule sources | Downloads MUTCD Part 3, checks the GB 5768.3-2025 PDF, writes `data_manifest.csv` |
| 4 Load | Builds three tables: BDD100K images, BDD100K lane labels, CULane test frames |
| 5 Size and types | Rows, fields and data types of each table, and the size on disk |
| 6 Examples | Real images from both datasets with their lane annotations drawn on top |
| 7 Data checks | Missing labels, class balance, near-duplicates, image sizes and coordinate ranges, coverage of driving conditions and of the four marking types |
| 8 Rule corpus | Page counts, keyword search and an excerpt of both standards; the curated rule passages |
| 9 Findings and gaps | Summary of what the checks found, including problems that cannot be fixed |
| 10 Changes | What changed compared with the Milestone 2 plan |

## Data sources

| Source | Version / part used | Where it comes from | License | Retrieved |
|---|---|---|---|---|
| CULane (China) | CULane (Pan et al., AAAI 2018), test split: 34,680 frames, 9 scene categories | [Official page](https://xingangpan.github.io/projects/CULane.html) → authors' Google Drive | Non-commercial research and teaching only; must be cited; no redistribution | 2026-10-05 |
| BDD100K (US) | BDD100K 100K images, validation split: 10,000 images with lane labels and scene tags | [bdd100k.com](https://bdd100k.com); official server was unreachable, so the [Dataset Ninja mirror](https://datasetninja.com/bdd100k) of the same release was used | BDD100K License (UC Berkeley): educational, research and non-profit use; copies keep the copyright notice | 2026-10-05 |
| MUTCD (US rules) | 11th Edition (December 2023), Part 3 Markings | [FHWA](https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/part3.pdf) | U.S. government work, no copyright restrictions | 2026-10-05 |
| GB 5768.3 (China rules) | GB 5768.3-2025, Part 3: Road traffic markings (in force from 2026-05-01) | [National standards platform](https://openstd.samr.gov.cn) | Mandatory national standard, free to read; text is copyrighted, so only short quotes are stored | 2026-10-05 |

`data_manifest.csv` is rewritten on every run and lists each downloaded file with its origin, size, retrieval date and license.

## How the datasets are handled

* **Only the needed parts are used.** CULane: the test split, because only the test split is sorted into scene categories (arrow, crossroad, night, no line, ...). BDD100K: the validation split, because the test split has no public labels.
* **BDD100K download.** The notebook first tries the official server. In October 2026 its host name did not resolve (other users report the same on the BDD100K GitHub discussions), so it downloads the Dataset Ninja mirror (one tar archive, Supervisely format) and unpacks only the validation images and their annotation files.
* **CULane download.** The notebook tries `gdown`, but Google Drive blocks popular files ("too many users have downloaded this file"). The five archives (`list`, `annotations_new` and the three `driver_*` test archives) were therefore downloaded in the browser into `data/raw/culane/`; the notebook checks them and unpacks them.
* **Unpacking.** Archives stay in `data/raw/`; unpacked files go to `data/extracted/`. A marker file per archive makes reruns skip finished steps. File names are made safe for the exFAT drive, and macOS `._` helper files are ignored.
* **Labels used.** BDD100K: lane category (e.g. single white, double yellow, crosswalk), solid/dashed, direction, and weather / time of day / scene. CULane: lane positions only (no colour or type) and the scene category of each frame.
* **Rule passages.** 26 short passages from GB 5768.3-2025 and MUTCD Part 3 for the four core marking types are in `rules/rule_passages.json`, each with section and page. Chinese passages keep the original text and have an English translation.

## Storage, privacy and credentials

* The raw data is not copied to any cloud service. CULane may not be redistributed, and the images show people and licence plates. The data lives in `data/` on an external SSD, and `data/` is ignored by Git.
* The repository is **private** and shared with the instructor only, because the saved notebook shows a few dataset images. Faces and plates will be blurred before any image is used in a report.
* No keys or tokens are in the repository. `.env` (ignored by Git) holds local settings such as `DATA_DIR`; `.env.example` shows the format. This notebook does not call the OpenAI API.

## How to run

Tested on macOS with Python 3.11 (conda). The repository and data are on an external SSD at `/Volumes/T9/Project/Reasning_Drive`; the Python environment stays on the laptop, because exFAT drives do not support the links a virtual environment needs.

```bash
conda create -n reasoning-driving python=3.11 -y
conda activate reasoning-driving
cd /Volumes/T9/Project/Reasning_Drive
pip install -r requirements.txt
jupyter lab
```

Open `playground.ipynb` and choose **Kernel → Restart Kernel and Run All Cells**.

* The first run downloads about 20 GB. Later runs reuse `data/` and take about 15 minutes, mostly reading tens of thousands of small label files from the external drive.
* If the five CULane archives are not in `data/raw/culane/`, the notebook stops and says which files to download from the official page.
* To keep the data somewhere else, copy `.env.example` to `.env` and set `DATA_DIR`. The notebook stops with a message if that drive is not connected.
* On Windows: `py -3.11 -m venv .venv`, then `.venv\Scripts\python -m pip install -r requirements.txt` and `.venv\Scripts\python -m jupyter lab`.

## Repository layout

```
Reasning_Drive/
├─ playground.ipynb        data retrieval, inspection and checks
├─ README.md
├─ requirements.txt        pinned packages (Python 3.11)
├─ data_manifest.csv       downloaded files: origin, size, retrieval date, license
├─ config/data_sources.json  URLs, versions and licenses of all sources
├─ labels/labels_template.csv  columns of the label file (filled in Milestone 3)
├─ rules/rule_passages.json    rule passages for the four core marking types
├─ .env.example
├─ .gitignore              keeps data/, archives, PDFs, .env and caches out of Git
└─ data/                   not in Git: raw/ (archives) and extracted/ (unpacked files)
```

## Changes since Milestone 2

* **Storage:** Milestone 2 planned for the laptop's internal disk (about 10 GB free) and deleting archives after unpacking. The data now lives on an external SSD (about 900 GB), so the full CULane test split is used and archives are kept until the image selection is final. Sections 2.3 and 2.6 will be updated in Milestone 3.
* **BDD100K source:** the official server was unreachable, so the mirror of the same release is used.
* **Marking types:** four core types (solid white line, dashed white line, yellow centre line, turn-guide arrow). The no-stopping grid from the proposal was dropped: neither dataset labels it, it was not found in a sample of CULane crossroad frames, and its US counterpart (MUTCD 3B.26) is optional and rare.
