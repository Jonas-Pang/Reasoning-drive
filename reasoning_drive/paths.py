"""Where everything of the project lives. Every other module asks this file for a path.

    configs/          settings: api.yaml, experiment.yaml, carla.yaml, experiments.yaml, schemas/
    prompts/          prompt versions (v1 to v4 for one marking, lane_v1 for the whole lane)
    regulations/      one folder per country: region.yaml, rule passages, rule tables (same template for every country)
    datasets/         one folder per country with its label collections; splits/ holds the files of all countries
    results/          runs/ (every model run), carla/ (simulation runs), index.csv (one line per run)
    data/             downloads and extracted images (not in git)
"""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

CONFIGS = "configs"
SCHEMAS = "configs/schemas"
PROMPTS = "prompts"
REGULATIONS = "regulations"
REGULATIONS_COMMON = "regulations/_common"
REGULATIONS_TEMPLATE = "regulations/_template"
REGULATIONS_INBOX = "regulations/inbox"
DATASETS = "datasets"
DATASETS_TEMPLATE = "datasets/_template"
SPLITS = "datasets/splits"
RESULTS = "results"
RUNS = "results/runs"
CARLA_RESULTS = "results/carla"
REPORTS = "results/reports"
DATA = "data"

API_FILE = "configs/api.yaml"
EXPERIMENT_FILE = "configs/experiment.yaml"
EXPERIMENTS_FILE = "configs/experiments.yaml"
CARLA_FILE = "configs/carla.yaml"
PROTOCOL_FILE = "configs/lane_protocol.json"
LABEL_SCHEMA = "configs/schemas/label_schema.json"
LANE_SCHEMA = "configs/schemas/lane_schema.json"
RESULTS_INDEX = "results/index.csv"
UNASSIGNED = "_unassigned"     # datasets/_unassigned/<collection>: a collection whose country is not known yet


def _r(repo) -> Path:
    return Path(repo or REPO)


def text_bytes(path) -> bytes:
    """The bytes of a text file with Windows line ends read as Unix ones, so hashes of prompts, rules and code are the
    same on every computer (a Git checkout on Windows may write CRLF)."""
    return Path(path).read_bytes().replace(b"\r\n", b"\n")


def is_repo(repo) -> bool:
    return (_r(repo) / REGULATIONS).is_dir() and (_r(repo) / CONFIGS).is_dir()


def runs_dir(repo) -> Path:
    return _r(repo) / RUNS


def splits_dir(repo) -> Path:
    return _r(repo) / SPLITS


# ------------------------------------------------------------------ countries (regulations/<CODE>/region.yaml)

def region_dirs(repo) -> list[Path]:
    """Folders under regulations/ that hold a region.yaml, sorted by name (the _template folder is not a country)."""
    root = _r(repo) / REGULATIONS
    if not root.is_dir():
        return []
    return sorted(d for d in root.iterdir() if d.is_dir() and not d.name.startswith((".", "_")) and (d / "region.yaml").exists())


def read_yaml(p: Path):
    import yaml
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def read_passages(p: Path) -> list[dict]:
    text = p.read_text(encoding="utf-8")
    if p.suffix in (".yaml", ".yml"):
        import yaml
        return yaml.safe_load(text) or []
    return json.loads(text)


def regions(repo) -> dict:
    """{code: (folder, region.yaml content)} for every country."""
    out = {}
    for d in region_dirs(repo):
        y = read_yaml(d / "region.yaml") or {}
        out[str(y.get("code") or d.name)] = (d, y)
    return out


def passage_files(repo, code: str | None = None) -> list[Path]:
    """Every passages file of one country (or of all countries), in the order region.yaml lists them."""
    files = []
    for c, (d, y) in regions(repo).items():
        if code and c != code:
            continue
        p = y.get("passages") or {}
        for rel in [p.get("marking")] + list(p.get("lane") or []):
            if rel and (d / rel) not in files and (d / rel).exists():
                files.append(d / rel)
    return files


def all_passages(repo, code: str | None = None) -> list[dict]:
    items = []
    for f in passage_files(repo, code):
        items += read_passages(f)
    return [p for p in items if not code or p.get("region") == code]


def _merged_table(repo, name: str) -> dict:
    """A rule table of every country: regulations/_common/<name> (version and notes) plus regulations/<CODE>/<name>."""
    common = _r(repo) / REGULATIONS_COMMON / name
    out = json.loads(common.read_text(encoding="utf-8")) if common.exists() else {}
    for c, (d, y) in regions(repo).items():
        f = d / ((y.get("rule_tables") or {}).get("lane" if name.startswith("lane") else "marking") or name)
        if f.exists():
            out[c] = json.loads(f.read_text(encoding="utf-8"))
    return out


def action_rules(repo) -> dict:
    return _merged_table(repo, "action_rules.json")


def lane_action_rules(repo) -> dict:
    return _merged_table(repo, "lane_action_rules.json")


def rule_table_files(repo, lane: bool = False) -> list[Path]:
    """The files a rule table is made of (for the code and protocol hashes)."""
    name = "lane_action_rules.json" if lane else "action_rules.json"
    files = [_r(repo) / REGULATIONS_COMMON / name]
    for c, (d, y) in regions(repo).items():
        files.append(d / ((y.get("rule_tables") or {}).get("lane" if lane else "marking") or name))
    return [f for f in files if f.exists()]


def translations_zh(repo) -> Path:
    return _r(repo) / REGULATIONS_COMMON / "translations_zh.json"


# ------------------------------------------------------------------ label collections (datasets/<CODE>/<collection>)

def dataset_dirs(repo) -> list[Path]:
    root = _r(repo) / DATASETS
    if not root.is_dir():
        return []
    return sorted(d for d in root.iterdir() if d.is_dir() and not d.name.startswith((".", "_")) and d.name != "splits")


def collection_region(repo, collection: str) -> str | None:
    """The country of a label collection, from datasets/<CODE>/dataset.yaml (collections: [...])."""
    for d in dataset_dirs(repo):
        f = d / "dataset.yaml"
        if f.exists():
            y = read_yaml(f) or {}
            if collection in [str(c.get("name") if isinstance(c, dict) else c) for c in (y.get("collections") or [])]:
                return str(y.get("region") or d.name)
    for d in dataset_dirs(repo):
        if (d / collection).is_dir():
            return d.name
    return None


def collection_dir(repo, collection: str) -> Path:
    """datasets/<CODE>/<collection>; datasets/_unassigned/<collection> when no country lists it."""
    code = collection_region(repo, collection)
    return _r(repo) / DATASETS / (code or UNASSIGNED) / collection
