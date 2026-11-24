"""The project page (/project): overview of the settings and countries, every saved run with its evaluation, the
regulations (extract a new standard from a PDF, read the draft, accept it) and the CARLA simulation (start CARLA,
drive a route, look at the stops of finished runs). Long tasks run in the background as jobs; the page polls them."""
from __future__ import annotations

import base64
import importlib.util
import json
import socket
import subprocess
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

from .. import config as C
from .. import paths as P

MAX_UPLOAD = 150 * 1024 * 1024


class Jobs:
    """Background tasks with a log that the page reads (since=N returns only new lines)."""

    def __init__(self):
        self.lock = threading.Lock()
        self.jobs: dict[str, dict] = {}

    def start(self, kind: str, title: str, fn) -> str:
        jid = f"{kind}_{datetime.now():%H%M%S}_{len(self.jobs) + 1}"
        job = {"id": jid, "kind": kind, "title": title, "running": True, "log": [], "result": None, "error": "",
               "started": time.time(), "ended": None}
        with self.lock:
            self.jobs[jid] = job

        def log(*a, **k):
            with self.lock:
                job["log"].append(" ".join(str(x) for x in a))

        def body():
            try:
                job["result"] = fn(log)
            except Exception as e:  # noqa: BLE001  the page shows the error
                job["error"] = f"{type(e).__name__}: {e}"
            finally:
                job["running"], job["ended"] = False, time.time()
        threading.Thread(target=body, daemon=True).start()
        return jid

    def state(self, since: dict | None = None) -> list[dict]:
        with self.lock:
            out = []
            for j in sorted(self.jobs.values(), key=lambda x: x["started"], reverse=True)[:10]:
                n = int((since or {}).get(j["id"], 0))
                out.append(dict({k: v for k, v in j.items() if k != "log"}, log=j["log"][n:], log_total=len(j["log"])))
            return out


class ProjectApi:
    def __init__(self, demo):
        self.demo = demo
        self.jobs = Jobs()
        self.procs: dict[str, subprocess.Popen] = {}

    @property
    def repo(self) -> Path:
        return C.repo_of(self.demo.cfg)

    # ------------------------------------------------------------ overview
    def overview(self) -> dict:
        from ..regulations.store import overview
        from ..simulation.settings import load_settings
        cfg = self.demo.cfg
        datasets = []
        for d in P.dataset_dirs(self.repo):
            y = P.read_yaml(d / "dataset.yaml") if (d / "dataset.yaml").exists() else {}
            cols = []
            for c in (y or {}).get("collections") or []:
                name = c.get("name") if isinstance(c, dict) else c
                cd = d / str(name)
                n = 0
                for f in cd.glob("*.labels.csv"):
                    n += max(0, sum(1 for _ in f.open(encoding="utf-8")) - 1)
                nl = 0
                for f in cd.glob("*.lanes.csv"):
                    nl += max(0, sum(1 for _ in f.open(encoding="utf-8")) - 1)
                cols.append({"name": name, "kind": c.get("kind", "") if isinstance(c, dict) else "", "marking_rows": n, "lane_rows": nl,
                             "source": c.get("source", "") if isinstance(c, dict) else ""})
            datasets.append({"code": d.name, "collections": cols})
        st = load_settings(self.repo)
        prompts = sorted(x.name for x in (self.repo / P.PROMPTS).iterdir() if x.is_dir())
        return {"model": cfg["api"]["model"], "reasoning_effort": cfg["api"].get("reasoning_effort"), "mock": cfg.get("mock"),
                "test": cfg["run"]["test"], "region": cfg["run"]["region"], "prompt": cfg["prompt"]["dir"], "lane_prompt": cfg["lane"]["prompt_dir"],
                "split": cfg["run"]["split"], "api_key_set": bool(C.api_key(cfg)), "countries": overview(self.repo), "datasets": datasets,
                "prompts": prompts, "routes": list((st.get("routes") or {}).keys()),
                "files": {"api": P.API_FILE, "experiment": P.EXPERIMENT_FILE, "carla": P.CARLA_FILE}}

    # ------------------------------------------------------------ results and evaluation
    def results(self) -> list[dict]:
        from ..evaluation.registry import build_index
        return build_index(self.repo)

    def evaluate(self, run_id: str, other: str | None = None) -> dict:
        from ..evaluation.evaluate import evaluate_run, side_by_side
        out = {"run": evaluate_run(self.repo, run_id)}
        if other:
            out["other"] = evaluate_run(self.repo, other)
            out["table"] = side_by_side(self.repo, run_id, other)
        return out

    # ------------------------------------------------------------ regulations
    def regulations(self) -> dict:
        from ..regulations.store import check, overview
        inbox = self.repo / P.REGULATIONS_INBOX
        pdfs = sorted(f.name for f in inbox.glob("*.pdf")) if inbox.is_dir() else []
        return {"countries": overview(self.repo), "problems": check(self.repo), "inbox": pdfs}

    def draft(self, code: str) -> dict:
        d = self.repo / P.REGULATIONS / code.upper()
        f = d / "passages_draft.yaml"
        items = P.read_yaml(f) if f.exists() else []
        log = json.loads((d / "extraction_log.json").read_text(encoding="utf-8")) if (d / "extraction_log.json").exists() else {}
        return {"code": code.upper(), "passages": items or [], "log": log}

    def passages(self, code: str) -> list[dict]:
        return P.all_passages(self.repo, code.upper())

    def save_upload(self, body: dict) -> str:
        name = Path(body.get("filename") or "standard.pdf").name
        if not name.lower().endswith(".pdf"):
            raise ValueError("Only PDF files.")
        data = base64.b64decode(body.get("pdf_base64") or "")
        if not data.startswith(b"%PDF"):
            raise ValueError("This is not a PDF file.")
        if len(data) > MAX_UPLOAD:
            raise ValueError("The PDF is larger than 150 MB: put it in regulations/inbox/ and pick it from the list.")
        inbox = self.repo / P.REGULATIONS_INBOX
        inbox.mkdir(parents=True, exist_ok=True)
        (inbox / name).write_bytes(data)
        return name

    def estimate(self, body: dict) -> dict:
        from ..regulations import extract as X
        pdf = self.repo / P.REGULATIONS_INBOX / Path(body["file"]).name
        pages = X.read_pages(pdf)
        first, last = int(body.get("first") or 1), int(body.get("last") or len(pages))
        nums = X.relevant_pages(pages, bool(body.get("all_pages")), first, last)
        grp = X.groups(nums, pages)
        chars = sum(len(pages[n - 1]) for n in nums)
        return {"file": pdf.name, "pages": len(pages), "pages_with_text": sum(1 for t in pages if t.strip()), "pages_read": len(nums),
                "requests": len(grp), "cost_usd": X.estimate_cost(self.demo.cfg, chars, len(grp)), "model": self.demo.cfg["api"]["model"]}

    def extract(self, body: dict) -> str:
        from ..regulations.extract import extract
        if not body.get("code") or not body.get("name") or not body.get("file"):
            raise ValueError("Give the PDF, the country code and its name.")
        mock = not bool(body.get("real"))
        if not mock and not C.api_key(self.demo.cfg):
            raise ValueError("No API key in .env: extract with mock, or add the key.")
        pdf = self.repo / P.REGULATIONS_INBOX / Path(body["file"]).name
        cfg = self.demo.cfg

        def run(log):
            return extract(self.repo, cfg, pdf, body["code"], body["name"], body.get("driving_side", "right"), body.get("title", ""),
                           mock=mock, all_pages=bool(body.get("all_pages")), first=int(body.get("first") or 1),
                           last=int(body["last"]) if body.get("last") else None, log=log)
        return self.jobs.start("extract", f"{body['code']}: {pdf.name}" + (" (mock)" if mock else ""), run)

    def accept(self, code: str) -> dict:
        from ..regulations.extract import accept
        out = accept(self.repo, code, log=lambda *a: None)
        self.demo.cfg["regions"] = C.load(self.repo)["regions"]   # the new country appears in the page's region list
        return {"file": str(out.relative_to(self.repo)), "regions": list(self.demo.cfg["regions"])}

    # ------------------------------------------------------------ CARLA
    def carla(self) -> dict:
        from ..simulation.settings import load_settings
        st = load_settings(self.repo)
        srv = st.get("server") or {}
        runs = []
        root = self.repo / P.CARLA_RESULTS
        for f in sorted(root.glob("*/summary.json"), reverse=True):
            d = f.parent
            s = json.loads(f.read_text(encoding="utf-8"))
            stops = []
            if (d / "stops.jsonl").exists():
                for line in (d / "stops.jsonl").read_text(encoding="utf-8").splitlines():
                    r = json.loads(line)
                    stops.append({"stop": r.get("stop"), "label": r.get("label"), "intent": r.get("intent"), "action": r.get("action"),
                                  "system_says": r.get("system_says"), "targets": [{"name": t.get("name"), "truth": t.get("truth")}
                                                                                 for t in r.get("targets") or []]})
            runs.append({"run": d.name, "meta": s.get("meta") or {}, "per_experiment": s.get("per_experiment") or s.get("per_test")
                         or s.get("per_ask") or {}, "closed_loop": s.get("closed_loop"), "cost_usd": s.get("cost_usd"),
                         "frames": sorted(x.name for x in (d / "frames").glob("*.png")) if (d / "frames").is_dir() else [],
                         "decisions": sorted(x.name for x in (d / "decisions").glob("*.png")) if (d / "decisions").is_dir() else [],
                         "stops": stops, "findings": json.loads((d / "findings.json").read_text(encoding="utf-8"))
                         if (d / "findings.json").exists() else [],
                         "video": (d / "route_replay.mp4").exists()})
        py = srv.get("python") or ""
        here = importlib.util.find_spec("carla") is not None
        return {"server": {k: srv.get(k) for k in ("host", "port", "carla_root", "version", "python")},
                "reachable": self._reachable(srv.get("host", "127.0.0.1"), int(srv.get("port", 2000))),
                "python_ok": here or (bool(py) and Path(py).exists()), "carla_in_this_python": here,
                "routes": {k: {"map": v.get("map"), "weather": v.get("weather"), "night": bool(v.get("night")),
                               "stops": [{"label": s.get("label"), "intent": s.get("intent")} for s in v.get("stops") or []]}
                           for k, v in (st.get("routes") or {}).items()},
                "experiments": st.get("experiments") or {}, "runs": runs}

    @staticmethod
    def _reachable(host: str, port: int) -> bool:
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return True
        except OSError:
            return False

    def carla_image(self, run: str, kind: str, name: str) -> bytes:
        if kind not in ("frames", "decisions"):
            raise ValueError("kind")
        f = self.repo / P.CARLA_RESULTS / Path(run).name / kind / Path(name).name
        if not f.is_file():
            raise FileNotFoundError(name)
        return f.read_bytes()

    def carla_video(self, run: str) -> Path:
        f = self.repo / P.CARLA_RESULTS / Path(run).name / "route_replay.mp4"
        if not f.is_file():
            raise FileNotFoundError("no replay video")
        return f

    def start_carla(self) -> dict:
        from ..simulation.settings import load_settings
        srv = load_settings(self.repo).get("server") or {}
        exe = Path(srv.get("carla_root") or "") / "CarlaUE4.exe"
        if not exe.exists():
            raise FileNotFoundError(f"{exe} not found: set server.carla_root in configs/carla.yaml")
        if self._reachable(srv.get("host", "127.0.0.1"), int(srv.get("port", 2000))):
            return {"started": False, "note": "CARLA is already running"}
        subprocess.Popen([str(exe)] + [str(a) for a in srv.get("start_args") or []], cwd=str(exe.parent))
        return {"started": True, "note": "CARLA is starting (about a minute)"}

    def run_route(self, body: dict) -> str:
        from ..simulation.settings import load_settings
        st = load_settings(self.repo)
        route = body.get("route") or "route1"
        if route not in (st.get("routes") or {}):
            raise ValueError(f"No route {route} in configs/carla.yaml")
        py = sys.executable if importlib.util.find_spec("carla") else ((st.get("server") or {}).get("python") or "")
        if not py or not Path(py).exists():
            raise ValueError("No Python with the carla package: set server.python in configs/carla.yaml")
        args = [py, "-u", str(self.repo / "main.py"), "carla", "route", route, "--record"]
        if body.get("mock", True):
            args.append("--mock")
        if body.get("preview"):
            args.append("--preview")

        def run(log):
            log("$ " + " ".join(args[2:]))
            p = subprocess.Popen(args, cwd=str(self.repo), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                 encoding="utf-8", errors="replace")
            self.procs[route] = p
            for line in p.stdout:
                log(line.rstrip())
            code = p.wait()
            log(f"(finished with code {code})")
            return {"code": code}
        return self.jobs.start("carla", f"{route}" + (" (mock)" if body.get("mock", True) else " (real API)"), run)
