"""configs/carla.yaml and the CARLA folders, without importing carla (so it also works where CARLA is not installed)."""
from __future__ import annotations

import sys
from pathlib import Path

from .. import paths as P


def load_settings(repo=None) -> dict:
    f = Path(repo or P.REPO) / P.CARLA_FILE
    return P.read_yaml(f) or {} if f.exists() else {}


def add_agents_path(settings: dict) -> None:
    """CARLA's route planner (the agents package) is not in the carla wheel: it lives in <carla_root>/PythonAPI/carla."""
    root = (settings.get("server") or {}).get("carla_root")
    if root:
        p = Path(root) / "PythonAPI" / "carla"
        if p.is_dir() and str(p) not in sys.path:
            sys.path.insert(0, str(p))


def set_map(town: str) -> str:
    """Make <town> (e.g. Town03_Opt) the map CARLA loads at start. Switching maps from the Python client crashes this
    CARLA build, so the map is set in the user's Engine.ini and CARLA is started again."""
    import os
    import re
    p = Path(os.environ.get("LOCALAPPDATA", "")) / "CarlaUE4" / "Saved" / "Config" / "WindowsNoEditor" / "Engine.ini"
    text = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    text = re.sub(r"\[/Script/EngineSettings\.GameMapsSettings\][^\[]*", "", text).rstrip()
    text += (f"\n\n[/Script/EngineSettings.GameMapsSettings]\nGameDefaultMap=/Game/Carla/Maps/{town}.{town}\n"
             f"ServerDefaultMap=/Game/Carla/Maps/{town}.{town}\n")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return str(p)
