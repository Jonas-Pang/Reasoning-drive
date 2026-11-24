"""Demo page: pick a labeled image, see the exact prompt, ask the model (Test A / Test B), follow its reasoning step
by step, compare with the label, run a whole batch and compare two runs. Two tasks: the lane-level task (task=lane: my
whole lane, the photo without a box) and the single-marking task of Milestone 4 (task=marking, the default of the API).
For the lane task the answers already in finished runs can be shown without a new request (GET /api/saved). A small web server, on 127.0.0.1 unless another address is given (the Docker
image listens on 0.0.0.0 inside its container). GET /metrics gives Prometheus metrics (reasoning_drive/web/metrics.py),
GET /healthz answers "ok" for health checks."""
from __future__ import annotations

import atexit
import base64
import copy
import os
import hashlib
import json
import shutil
import tempfile
import threading
import time
import traceback
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import cv2
import numpy as np

from ..imageio import imread, imwrite
from .. import config as C
from .. import paths as P
from ..agent import lane as L
from ..evaluation import review as R
from ..data import boxed_jpeg, load_items
from .metrics import DemoMetrics
from ..agent.prompts import passages, prompt_parts
from ..agent.runner import ask, compare_runs, list_runs, load_run, run_batch

WEB = Path(__file__).resolve().parent / "static"
EDITABLE = {"mock": bool, "run.test": str, "run.region": str, "run.repeats": int, "run.limit": int, "run.split": str,
            "api.model": str, "api.reasoning_effort": str, "api.temperature": float, "api.image_detail": str,
            "api.max_output_tokens": int, "api.parallel": int, "api.reasoning_summary": str, "prompt.dir": str,
            "lane.prompt_dir": str, "lane.max_output_tokens": int}


class Demo:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.lock = threading.RLock()
        self.job = {"running": False, "done": 0, "total": 0, "run_id": "", "error": "", "test": "", "region": ""}
        self.metrics = DemoMetrics.create()
        if self.metrics:
            self.metrics.settings(cfg)
        self.uploads: dict = {}          # image_id -> LaneItem of a photo uploaded on the page (kept until the page stops)
        self.upload_dir = None
        self.job_records: dict = {}      # (test, image_id) -> the answers of the batch run started from the page
        from .project_api import ProjectApi
        self.project = ProjectApi(self)
        self._app_cfgs: dict = {}        # model choice of /app -> (settings, mock); see app_cfg_for
        self._user_keys: dict = {}       # browser session -> a key the user typed on /app (memory only, never saved)
        self._video = None               # VideoJobs, made on the first video upload  # the project page (/project): results, evaluation, regulations, CARLA

    # ------------------------------------------------------------ settings
    def config(self) -> dict:
        cfg = C.public(self.cfg)
        counts, lane_counts = {}, {}
        for r in self.cfg["regions"]:
            try:
                counts[r] = len(load_items(self.cfg, r, "any", []))
            except Exception:  # noqa: BLE001
                counts[r] = 0
            try:
                lane_counts[r] = {s: len(L.load_lane_items(self.cfg, r, s)) for s in ("dev", "test", "any")}
            except Exception:  # noqa: BLE001
                lane_counts[r] = {"dev": 0, "test": 0, "any": 0}
        repo = C.repo_of(self.cfg)
        dirs = [d for d in (repo / "prompts").iterdir() if d.is_dir() and ((d / "instructions.txt").exists() or (d / "role.txt").exists())]
        versions = sorted(d.name for d in dirs if not d.name.startswith("lane"))
        lane_versions = sorted(d.name for d in dirs if d.name.startswith("lane"))
        return {"config": cfg, "tests": C.TESTS, "items_per_region": counts, "lane_items_per_region": lane_counts,
                "prompt_versions": versions, "lane_prompt_versions": lane_versions, "config_file": C.CONFIG_FILE, "unsaved": self.unsaved()}

    def unsaved(self) -> list[str]:
        """Settings changed on the page but not written to the settings files."""
        try:
            on_file = C.load(C.repo_of(self.cfg))
        except C.ConfigError:
            return []
        out = []
        for path, (section, key) in C.YAML_PATH.items():
            a, b = self.cfg, on_file
            for k in path.split("."):
                a, b = a[k], b[k]
            if a != b:
                out.append(f"{section}.{key}")
        return out

    def update(self, body: dict) -> dict:
        with self.lock:
            if body.get("reload"):
                self.cfg = C.load(C.repo_of(self.cfg))
                return self.config()
            for path, typ in EDITABLE.items():
                if path not in body:
                    continue
                v = body[path]
                if v in ("", None, "off") and path in ("api.reasoning_effort", "api.temperature", "api.reasoning_summary", "lane.max_output_tokens"):
                    v = None
                elif typ is bool:
                    v = bool(v)
                else:
                    v = typ(v)
                node = self.cfg
                keys = path.split(".")
                for k in keys[:-1]:
                    node = node[k]
                node[keys[-1]] = v
            C.check(self.cfg)
            if body.get("save"):
                C.save(self.cfg)
            if self.metrics:
                self.metrics.settings(self.cfg)
        return self.config()

    # ------------------------------------------------------------ data
    def items(self, region: str, task: str = "marking", split: str = "any") -> list[dict]:
        if task == "lane":
            return self.lane_items(region, split)
        out = []
        for it in load_items(self.cfg, region, "any", []):
            out.append({"image_id": it.image_id, "collection": it.collection, "dataset": it.dataset, "split": it.split,
                        "marking": it.marking, "visibility": it.label.get("visibility", ""), "width": it.width, "height": it.height})
        return out

    def _item(self, image_id: str, region: str | None = None):
        for r in ([region] if region else list(self.cfg["regions"])):
            for it in load_items(self.cfg, r, "any", []):
                if it.image_id == image_id:
                    return it
        raise KeyError(f"Unknown image {image_id}")

    def image(self, image_id: str, width: int | None, task: str = "marking", lines: bool = False) -> bytes:
        if task == "lane":
            it = self._lane_item(image_id)
            jpeg = L.plain_jpeg(it, L.lane_cfg(self.cfg))  # what the model sees: the photo without any drawing
            img = cv2.imdecode(np.frombuffer(jpeg, np.uint8), cv2.IMREAD_COLOR) if (width or lines) else None
            if lines:  # the boundary lines drawn while labeling, for checking only (never sent to the model)
                for side, color in (("left", (0, 165, 255)), ("right", (255, 80, 255))):
                    try:
                        pts = json.loads(it.label.get(f"{side}_line") or "[]")
                    except ValueError:
                        pts = []
                    if len(pts) >= 2:
                        cv2.polylines(img, [np.array(pts, np.int32)], False, color, max(2, img.shape[1] // 400), cv2.LINE_AA)
            if img is None:
                return jpeg
        else:
            jpeg = boxed_jpeg(self._item(image_id), self.cfg)
            if not width:
                return jpeg
            img = cv2.imdecode(np.frombuffer(jpeg, np.uint8), cv2.IMREAD_COLOR)
        if width:
            h = int(round(img.shape[0] * width / img.shape[1]))
            img = cv2.resize(img, (int(width), h), interpolation=cv2.INTER_AREA)
        ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 80 if width else 90])
        return buf.tobytes()

    def prompt(self, test: str, region: str, task: str = "marking") -> dict:
        if task == "lane":
            lc = L.lane_cfg(self.cfg)
            parts = L.lane_prompt_parts(lc, test, region)
            parts["slots"] = {"rules_step": L._read(lc, f"rules_step_{test}.txt"), "citation": L._read(lc, f"citation_{test}.txt")}
            return parts
        return prompt_parts(self.cfg, test, region)

    def passage_map(self, region: str, task: str = "marking") -> dict:
        from ..labeling.packages import _translations
        from types import SimpleNamespace
        zh = _translations(SimpleNamespace(repo=C.repo_of(self.cfg)))
        ps = L.lane_passages(L.lane_cfg(self.cfg), region) if task == "lane" else passages(self.cfg, region)
        return {p["rule_id"]: {"text_en": p.get("text_en", ""), "text_zh": p.get("text_zh") or zh.get(p["rule_id"], ""),
                               "section": p.get("section", ""), "source": p.get("source", "")} for p in ps}

    def ask(self, image_id: str, test: str, use_cache: bool = True, task: str = "marking") -> dict:
        from ..agent.runner import cost_of
        if task == "lane":
            it = self._lane_item(image_id)
            rec = L.ask_lane(self.cfg, it, test, self.cfg.get("mock", False), use_cache)
            return self._finish_lane(rec, it)
        it = self._item(image_id)
        rec = ask(self.cfg, it, test, 0, self.cfg.get("mock", False), use_cache=use_cache)
        cid = (rec.get("answer") or {}).get("cited_rule_id")
        pm = self.passage_map(it.region)
        rec["cited_passage"] = pm.get(cid) if cid else None
        rec["accepted_passages"] = {i: pm.get(i) for i in (it.label.get("accepted_rule_ids") or "").split(";") if i}
        rec["cost_usd"] = round(cost_of(self.cfg, (rec.get("response") or {}).get("usage") or {}, (rec.get("response") or {}).get("model")), 5) if not rec.get("cached") else 0
        if self.metrics:
            self.metrics.answer(self.cfg, rec, "page", "marking")
        return rec

    # ------------------------------------------------------------ lane task
    def _finish_lane(self, rec: dict, it, source: str = "page") -> dict:
        """Passages, cost and metrics of a lane answer. A photo uploaded on the page has no label: no score, only the
        contradictions found inside the answer."""
        from ..agent.runner import cost_of
        self._lane_extras(rec, it.region)
        resp = rec.get("response") or {}
        rec["cost_usd"] = round(cost_of(self.cfg, resp.get("usage") or {}, resp.get("model")), 5) if not (rec.get("cached") or rec.get("mock")) else 0
        if it.collection == "upload":
            rec["checks"] = (rec.get("score") or {}).get("consistency", [])
            rec["score"], rec["label"], source = None, {}, "upload"
        if self.metrics:
            self.metrics.answer(self.cfg, rec, source, "lane")
        return rec

    def ask_stream(self, image_id: str, test: str, use_cache: bool, emit) -> None:
        """One lane answer as server-sent events: status, reasoning (the API's summary of the hidden reasoning), text (the
        answer as the model writes it), done (the parsed, scored record) and fail (an error message). A cached or mock answer is replayed in the
        order it was written, and marked as a replay."""
        try:
            it = self._lane_item(image_id)
            mock = bool(self.cfg.get("mock", False))
            lc = L.lane_cfg(self.cfg)
            emit("status", {"phase": "start", "test": test, "mock": mock, "model": lc["api"]["model"],
                            "effort": lc["api"].get("reasoning_effort"), "summary": lc["api"].get("reasoning_summary")})
            streamed = [False]

            def on_event(kind, d):
                if kind in ("text", "reasoning"):
                    if not streamed[0]:
                        streamed[0] = True
                        emit("status", {"phase": "writing"})
                    emit(kind, {"d": d})
                else:
                    emit("status", {"phase": "note", "note": str(d)})

            rec = L.ask_lane(self.cfg, it, test, mock, use_cache, on_event=None if mock else on_event)
            if not streamed[0] and (rec.get("text") or (rec.get("response") or {}).get("reasoning_summary")):
                emit("status", {"phase": "replay", "source": "mock" if rec.get("mock") else "cache"})
                self._replay(rec, emit)
            emit("done", self._finish_lane(rec, it))
        except Exception as e:  # noqa: BLE001 - the page shows the message
            if not isinstance(e, (KeyError, ValueError, C.ConfigError, FileNotFoundError)):
                traceback.print_exc()
            emit("fail", {"message": str(e).strip("'")})

    @staticmethod
    def _replay(rec: dict, emit, seconds: float = 1.5) -> None:
        summary = (rec.get("response") or {}).get("reasoning_summary") or ""
        text = rec.get("text") or ""
        for kind, body in (("reasoning", summary), ("text", text)):
            if not body:
                continue
            size = max(16, len(body) // 120)
            for i in range(0, len(body), size):
                emit(kind, {"d": body[i:i + size]})
                time.sleep(seconds / 120)

    def upload(self, body: dict) -> dict:
        """A photo uploaded on the page: checked, saved without metadata in a temporary folder, asked like a labeled image."""
        region = body.get("region") or self.cfg["run"]["region"]
        if region not in self.cfg["regions"]:
            raise ValueError(f"Unknown region {region}.")
        data = str(body.get("data") or "")
        if "," in data[:100]:
            data = data.split(",", 1)[1]  # a data: URL
        if len(data) > 14_000_000:
            raise ValueError("The photo is larger than 10 MB.")
        raw = base64.b64decode(data, validate=False)
        img = cv2.imdecode(np.frombuffer(raw, np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("The file is not a JPEG, PNG or WebP image.")
        h, w = img.shape[:2]
        if max(w, h) > 4096 or min(w, h) < 160:
            raise ValueError(f"The photo is {w}×{h} pixels; it must be 160 to 4096 pixels a side.")
        if self.upload_dir is None:
            self.upload_dir = Path(tempfile.mkdtemp(prefix="lane_demo_uploads_"))
            atexit.register(shutil.rmtree, self.upload_dir, True)  # uploaded photos are deleted when the page stops
        image_id = "upload_" + hashlib.sha256(raw).hexdigest()[:12]
        path = self.upload_dir / f"{image_id}.png"
        imwrite(str(path), img)  # decoded and written again: no metadata (GPS position, camera) is kept
        self.uploads[image_id] = L.LaneItem(image_id, "upload", region, "upload", "upload", path, w, h, {})
        self.uploads[image_id].label = {"_name": str(body.get("name") or "")[:80]}
        return {"image_id": image_id, "region": region}

    def lane_items(self, region: str, split: str = "dev") -> list[dict]:
        saved = self._saved_index()
        out = [{"image_id": it.image_id, "collection": "upload", "dataset": "upload", "split": "upload", "width": it.width, "height": it.height,
                "lane_count": "", "ego_index": "", "left": "", "right": "", "markings": [], "yellow": False, "solid": False, "arrow": False,
                "lines": False, "saved": {}, "upload": True, "name": it.label.get("_name", "")}
               for it in self.uploads.values() if it.region == region]
        for it in L.load_lane_items(self.cfg, region, split or "any"):
            lab = it.label
            side = lambda s, lab=lab: " ".join(x for x in (lab.get(f"{s}_color", ""), lab.get(f"{s}_pattern", "")) if x)  # noqa: E731
            toks = [t for t in (lab.get("markings") or "").split(";") if t]
            out.append({"image_id": it.image_id, "collection": it.collection, "dataset": it.dataset, "split": it.split,
                        "width": it.width, "height": it.height, "lane_count": lab.get("lane_count", ""), "ego_index": lab.get("ego_index", ""),
                        "left": side("left"), "right": side("right"), "markings": toks,
                        "yellow": "yellow" in (lab.get("left_color"), lab.get("right_color")),
                        "solid": any("solid" in (lab.get(f"{s}_pattern") or "") for s in ("left", "right")),
                        "arrow": any(t.startswith(("arrow:", "text:", "no_turn:")) for t in toks),
                        "lines": bool(lab.get("left_line") or lab.get("right_line")),
                        "saved": saved.get(it.image_id, {})})
        return out

    def _lane_item(self, image_id: str):
        if image_id in self.uploads:
            it = self.uploads[image_id]
            return L.LaneItem(it.image_id, it.collection, it.region, it.dataset, it.split, it.path, it.width, it.height, {})
        for r in self.cfg["regions"]:
            for it in L.load_lane_items(self.cfg, r, "any"):
                if it.image_id == image_id:
                    return it
        raise KeyError(f"Unknown image {image_id}")

    def _lane_extras(self, rec: dict, region: str) -> None:
        """The rule passages an answer cites and the label accepts, with their text, for the page."""
        pm = self.passage_map(region, "lane")
        ids = {e.get("rule_id") for e in ((rec.get("answer") or {}).get("element_rules") or []) if isinstance(e, dict) and e.get("rule_id")}
        ids |= {i for i in (rec.get("label", {}).get("accepted_rule_ids") or "").split(";") if i}
        rec["passages"] = {i: pm.get(i) for i in sorted(ids)}

    def _saved_runs(self) -> list[dict]:
        """Finished lane runs with real answers, newest first."""
        return [r for r in L.list_lane_runs(self.cfg) if r["finished"] and not r["mock"]]

    def _saved_index(self) -> dict:
        """image_id -> {test: {run_id, lane, output2}} from the newest finished real run of each test that has the image."""
        runs = self._saved_runs()
        rd = P.runs_dir(C.repo_of(self.cfg))
        key = tuple((r["run_id"], (rd / r["run_id"] / "results.jsonl").stat().st_mtime_ns
                     if (rd / r["run_id"] / "results.jsonl").exists() else 0) for r in runs)
        cache = getattr(self, "_saved_cache", None)
        if cache and cache[0] == key:
            return cache[1]
        idx: dict = {}
        for r in runs:
            for rec in L.load_lane_run(self.cfg, r["run_id"])["records"]:
                slot = idx.setdefault(rec["image_id"], {})
                if rec.get("answer") and rec["test"] not in slot:
                    sc = rec.get("score") or {}
                    slot[rec["test"]] = {"run_id": r["run_id"], "lane": sc.get("lane"), "output2": sc.get("output2")}
        self._saved_cache = (key, idx)
        return idx

    # ---- blind review (review.py; page /review)
    def review_items(self, region: str) -> dict:
        return R.review_items(self.cfg, region)

    def review_decide(self, body: dict) -> dict:
        item = R.find_item(self.cfg, str(body.get("item_id", "")))
        return R.save_decision(self.cfg, item, str(body.get("decision", "")), str(body.get("value", "")), str(body.get("reviewer", "")))

    def review_effect(self, region: str) -> dict:
        """Scores of the finished lane runs of a region before and after the review decisions (no API calls)."""
        keys = ("lane", "lane_core", "output2", "markings_exact", "unsafe_errors", "markings_added")
        out = []
        for r in L.list_lane_runs(self.cfg):
            if not r["finished"] or r["mock"] or r["region"] != region:
                continue
            run = L.load_lane_run(self.cfg, r["run_id"])
            before = L.summarize_lane_records(self.cfg, run["records"])["summary"]
            after = L.summarize_lane_records(self.cfg, L.rescore_records(self.cfg, run["records"], True))["summary"]
            out.append({"run_id": r["run_id"], "test": r["test"], "before": {k: before.get(k) for k in keys}, "after": {k: after.get(k) for k in keys}})
        return {"region": region, "decisions": len(R.load_decisions(self.cfg)), "runs": out}

    def passages_lane(self, region: str) -> dict:
        return self.passage_map(region, "lane")

    def run_records(self, run_id: str) -> list[dict]:
        """One line per answer of a finished lane run (for the list of a batch)."""
        return [self._log_entry(r, i + 1, 0) for i, r in enumerate(sorted(L.load_lane_run(self.cfg, run_id)["records"], key=lambda r: r["image_id"]))]

    def record(self, run_id: str | None, test: str, image_id: str) -> dict:
        """One answer of a finished run (run_id) or of the batch running from the page, with its passages."""
        if run_id:
            rec = next((r for r in L.load_lane_run(self.cfg, run_id)["records"] if r["image_id"] == image_id), None)
        else:
            rec = self.job_records.get((test, image_id))
        if rec is None:
            raise KeyError(f"No answer for {image_id}")
        rec = json.loads(json.dumps(rec))
        self._lane_extras(rec, rec.get("region") or self.cfg["run"]["region"])
        return rec

    @staticmethod
    def _log_entry(rec: dict, done: int, total: int) -> dict:
        sc, resp = rec.get("score") or {}, rec.get("response") or {}
        return {"done": done, "total": total, "test": rec.get("test"), "image_id": rec.get("image_id"), "region": rec.get("region"),
                "o1": sc.get("lane", sc.get("output1")), "o2": sc.get("output2"), "unsafe": len(sc.get("unsafe") or []),
                "contradictions": len(sc.get("consistency") or []), "cached": bool(rec.get("cached")), "mock": bool(rec.get("mock")),
                "latency_s": resp.get("latency_s"), "error": (rec.get("error") or rec.get("parse_error") or "")[:160],
                "actions": (rec.get("answer") or {}).get("actions")}

    def saved(self, image_id: str) -> dict:
        """The answers to this image in the newest finished real lane run of each test (no new request)."""
        it = self._lane_item(image_id)
        out = {}
        for test, ref in self._saved_index().get(image_id, {}).items():
            run = L.load_lane_run(self.cfg, ref["run_id"])
            rec = next((x for x in run["records"] if x["image_id"] == image_id and x.get("answer")), None)
            if not rec:
                continue
            self._lane_extras(rec, it.region)
            from ..agent.runner import cost_of
            resp = rec.get("response") or {}
            rec["cost_usd"] = round(cost_of(self.cfg, resp.get("usage") or {}, resp.get("model")), 5) if not (rec.get("cached") or rec.get("mock")) else 0
            rec["from_run"] = {"run_id": ref["run_id"], "prompt": run["manifest"]["prompt_hashes"].get("prompt_dir", ""),
                               "model": run["manifest"]["settings"].get("model", ""), "created_utc": run["manifest"].get("created_utc", "")}
            out[test] = rec
        return out

    # ------------------------------------------------------------ lane advisor (/app): predict, verify, feedback
    # Added by Claude, 2026-11-18. The user-facing page of the deployed system; the pages above are research tools.
    def _applog(self):
        if getattr(self, "_app_log", None) is None:
            from .feedback import AppLog
            self._app_log = AppLog(C.repo_of(self.cfg))
            if self.metrics:
                self.metrics.seed_predictions(self._app_log.predictions())
                self.metrics.seed_feedback(self._app_log.feedback())
        return self._app_log

    def app_info(self, session: str = "") -> dict:
        a = self.cfg["api"]
        return {"model": a.get("model"), "provider": a.get("provider"), "profile": a.get("profile", ""),
                "prompt": self.cfg.get("lane", {}).get("prompt_dir"), "mock": bool(self.cfg.get("mock")),
                "key_set": bool(C.api_key(self.cfg)) if hasattr(C, "api_key") else None,
                "regions": [r for r in ("CN", "US", "UK", "IN") if r in self.cfg["regions"]],
                "models": self.app_models(session),
                "grafana": "http://localhost:3000", "prometheus": "http://localhost:9090"}

    # ---- which model answers on /app (Claude, 2026-11-18): chosen per request on the page
    APP_MODELS = {"navigator": "UF NaviGator", "openai": "OpenAI", "mock": "Mock (no model call)"}

    def app_models(self, session: str = "") -> list[dict]:
        out = []
        uk = self._user_keys.get(session or "")
        if uk:
            out.append({"id": "mykey", "label": f"Your key · {uk['model']} ({uk['provider_label']})", "model": uk["model"],
                        "provider": uk["provider"], "key_env": "your key", "key_set": True, "mock": False, "hint": uk["hint"]})
        for choice, label in self.APP_MODELS.items():
            try:
                cfg, mock = self._app_base(choice)
                a = cfg["api"]
                out.append({"id": choice, "label": f"{label} · {a.get('model')}" if not mock else label, "model": a.get("model"),
                            "provider": a.get("provider"), "key_env": a.get("api_key_env", ""), "base_url": a.get("base_url", ""),
                            "key_set": True if mock else bool(C.api_key(cfg)), "mock": mock})
            except Exception as e:  # noqa: BLE001  (a missing profile must not break the page)
                out.append({"id": choice, "label": label, "error": str(e)[:200], "key_set": False})
        return out

    def _app_base(self, choice: str) -> tuple[dict, bool]:
        """Settings for one model choice: 'navigator' = the NaviGator profile (RD_NAVIGATOR_PROFILE, default
        nav_gemma4_31b_bf16), 'openai' = configs/api.yaml, 'mock' = made-up answers, 'server' = what the service was
        started with. The lane prompt and everything else stay those of the service."""
        if choice in self._app_cfgs:
            return self._app_cfgs[choice]
        if choice == "server":
            out = (self.cfg, bool(self.cfg.get("mock")))
        elif choice in ("navigator", "openai", "mock"):
            base = copy.deepcopy(self.cfg)
            if choice != "mock":
                base["api"] = copy.deepcopy(C.load(C.repo_of(self.cfg))["api"])
            if choice == "navigator":
                from ..cli import _use_api_profile
                _use_api_profile(base, os.environ.get("RD_NAVIGATOR_PROFILE", "nav_gemma4_31b_bf16"))
            out = (base, choice == "mock")
        else:
            raise ValueError(f"Unknown model {choice!r}; use navigator, openai or mock.")
        self._app_cfgs[choice] = out
        return out

    # ---- the user's own API key (Claude, 2026-11-18): typed on the page, kept in this process's memory per browser
    # session, never written to a file, a log or a metric; forgotten on "Forget" or when the service stops.
    USER_PROVIDERS = {"openai": "OpenAI", "navigator": "UF NaviGator", "custom": "OpenAI-compatible"}

    def _user_api(self, body: dict) -> dict:
        prov = str(body.get("provider") or "openai")
        if prov not in self.USER_PROVIDERS:
            raise ValueError("provider must be openai, navigator or custom")
        if prov == "openai":
            api = copy.deepcopy(C.load(C.repo_of(self.cfg))["api"])
        elif prov == "navigator":
            tmp = copy.deepcopy(self.cfg)
            from ..cli import _use_api_profile
            _use_api_profile(tmp, os.environ.get("RD_NAVIGATOR_PROFILE", "nav_gemma4_31b_bf16"))
            api = tmp["api"]
        else:
            api = {"provider": "openai_chat", "temperature": 0, "seed": 6216, "reasoning_effort": None, "image_detail": None,
                   "timeout_s": 600, "max_retries": 2, "parallel": 2, "profile": "user_custom"}
        base = str(body.get("base_url") or api.get("base_url") or "").strip().rstrip("/")
        if not (base.startswith("https://") or base.startswith(("http://localhost", "http://127.0.0.1", "http://host.docker.internal"))):
            raise ValueError("The base URL must start with https:// (or http://localhost for a local server).")
        model = str(body.get("model") or api.get("model") or "").strip()
        if not model or len(model) > 120:
            raise ValueError("Give the model name, e.g. gpt-6.1-sol or gemma-4-31b-it.")
        api.update({"base_url": base, "model": model, "api_key_env": "(key typed on the page)"})
        api.setdefault("price_per_million_tokens", {model: {"input": 0, "output": 0}})
        return api

    @staticmethod
    def _clean_key(key) -> str:
        key = str(key or "").strip()
        if not key or len(key) > 512 or any(c.isspace() for c in key):
            raise ValueError("Paste the API key: one piece of text without spaces.")
        return key

    def user_key_check(self, body: dict) -> dict:
        """Is the key accepted? Asks the provider's free /models list (no tokens, no cost)."""
        import urllib.error
        import urllib.request
        api = self._user_api(body)
        key = self._clean_key(body.get("key")) if body.get("key") else (self._user_keys.get(str(body.get("session") or ""), {}).get("_key") or "")
        if not key:
            raise ValueError("Paste the API key first.")
        req = urllib.request.Request(api["base_url"] + "/models", headers={"Authorization": f"Bearer {key}"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                data = json.loads(r.read().decode("utf-8") or "{}")
            ids = [m.get("id") for m in data.get("data") or [] if isinstance(m, dict)]
            return {"ok": True, "status": 200, "models": len(ids), "model_listed": api["model"] in ids if ids else None,
                    "message": f"Key accepted by {api['base_url']}" + (f"; model {api['model']} " + ("is available." if api["model"] in ids else "is NOT in the list.") if ids else ".")}
        except urllib.error.HTTPError as e:
            msg = {401: "the key was refused (401)", 403: "the key has no access (403)", 404: "the URL has no /models list (404)"}.get(e.code, f"HTTP {e.code}")
            return {"ok": False, "status": e.code, "message": f"Not accepted: {msg}."}
        except (urllib.error.URLError, OSError, ValueError) as e:
            return {"ok": False, "status": 0, "message": f"Cannot reach {api['base_url']}: {str(getattr(e, 'reason', e))[:120]}"}

    def user_key_set(self, body: dict) -> dict:
        session = str(body.get("session") or "")
        if len(session) < 16:
            raise ValueError("No browser session; reload the page.")
        api = self._user_api(body)
        key = self._clean_key(body.get("key"))
        prov = str(body.get("provider") or "openai")
        self._user_keys[session] = {"_key": key, "api": api, "provider": api.get("provider", "openai"),
                                    "provider_label": self.USER_PROVIDERS[prov], "model": api["model"],
                                    "base_url": api["base_url"], "hint": "…" + key[-4:], "set_utc": time.strftime("%H:%M:%S")}
        return self.user_key_info(session)

    def user_key_info(self, session: str) -> dict:
        uk = self._user_keys.get(session or "")
        return {k: v for k, v in uk.items() if not k.startswith("_") and k != "api"} if uk else {}

    def user_key_clear(self, body: dict) -> dict:
        self._user_keys.pop(str(body.get("session") or ""), None)
        return {"ok": True}

    def app_test_for(self, region: str, rules: str | None) -> tuple[str, str | None]:
        """Which rules the model gets: none (Test A), the photo's region (Test B) or another region (Test C)."""
        if region not in self.cfg["regions"]:
            raise ValueError(f"Unknown region {region}.")
        rules = (rules or "none").upper() if rules not in (None, "") else "NONE"
        if rules == "NONE":
            return "A", None
        if rules == region:
            return "B", region
        if rules not in self.cfg["regions"]:
            raise ValueError(f"No rule passages for {rules} on this machine.")
        return "C", rules

    def app_cfg_for(self, choice: str, region: str, rules: str | None, session: str = "") -> tuple[dict, bool]:
        if choice == "mykey":
            uk = self._user_keys.get(session or "")
            if not uk:
                raise ValueError("No API key of yours is set in this browser: open the “Your API key” tab.")
            cfg, mock = copy.deepcopy(self.cfg), False
            cfg["api"] = {**copy.deepcopy(uk["api"]), "_key": uk["_key"]}
        else:
            cfg, mock = self._app_base(choice or "server")
        if not mock and not C.api_key(cfg):
            raise ValueError(f"{cfg['api'].get('api_key_env', 'the API key')} is not set in .env: add it and restart the service, "
                             "or choose Mock / Saved answer.")
        if rules and rules != region:   # Test C: the road of `region` with the rules of `rules`
            cfg = dict(cfg)
            cfg["lane"] = dict(cfg.get("lane") or {})
            cfg["lane"]["control_region"] = {**(cfg["lane"].get("control_region") or {}), region: rules}
        return cfg, mock

    def register_frame(self, image_id: str, region: str, path, w: int, h: int):
        """A video frame becomes an uploaded photo (served by /api/image, deleted when the service stops)."""
        it = L.LaneItem(image_id, "upload", region, "video", "upload", Path(path), w, h, {})
        self.uploads[image_id] = it
        return it

    def app_answer(self, it, test: str, choice: str, rules: str | None, mode: str = "live", session: str = "") -> dict:
        """One answer of the deployed pipeline: lane prompt + rules + model, verification, prediction log, metrics."""
        from . import guard
        cfg, mock = self.app_cfg_for(choice, it.region, rules, session)
        t0 = time.time()
        rec = L.ask_lane(cfg, it, test, mock, True)
        rr = rules or it.region
        self._lane_extras(rec, rr)
        check = guard.verify(C.repo_of(self.cfg), rr, rec, it.path)
        rid = self._applog().log_prediction(rec, check, cfg, mode)
        secs = time.time() - t0
        if self.metrics:
            self.metrics.app_prediction(rec, check, mode, secs)
            if not rec.get("cached") and not mock:
                self.metrics.answer(cfg, rec, "app", "lane")
        ans = rec.get("answer") or {}
        return {"request_id": rid, "rec": rec, "check": check, "seconds": secs, "cached": bool(rec.get("cached")),
                "answer": {k: ans.get(k) for k in ("scene", "lane_count", "ego_lane_index", "left_boundary", "right_boundary",
                                                    "lane_markings", "element_rules", "action_reasons", "actions", "advice")},
                "passages": rec.get("passages", {}), "latency_s": (rec.get("response") or {}).get("latency_s"),
                "model": (rec.get("response") or {}).get("model") or ("mock" if mock else cfg["api"].get("model")),
                "error": rec.get("error") or rec.get("parse_error") or ""}

    @property
    def video(self):
        if self._video is None:
            from .video import VideoJobs
            self._video = VideoJobs(self)
        return self._video

    def _app_index(self) -> dict:
        """image_id -> {test: run_id} from the finished real runs of the main configuration (the page's model and lane
        prompt; on a machine without that model, gemma4:31b + the page's prompt). Used for the 'saved answer' mode."""
        rd = P.runs_dir(C.repo_of(self.cfg))
        prompt = self.cfg.get("lane", {}).get("prompt_dir")
        key = (prompt, len(list(rd.glob("*_lane*"))))
        cache = getattr(self, "_app_cache", None)
        if cache and cache[0] == key:
            return cache[1]
        idx: dict = {}
        for d in sorted(rd.glob("*_lane*"), reverse=True):
            try:
                man = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if man.get("mock") or man.get("prompt_hashes", {}).get("prompt_dir") != prompt or not (d / "scores.json").exists():
                continue
            if man["settings"].get("model") not in (self.cfg["api"].get("model"), "gemma4:31b"):
                continue
            for rec in L.load_lane_run(self.cfg, d.name)["records"]:
                if rec.get("answer"):
                    idx.setdefault(rec["image_id"], {}).setdefault(rec["test"], d.name)
        self._app_cache = (key, idx)
        return idx

    def app_examples(self, region: str) -> list[dict]:
        idx = self._app_index()
        out = []
        for it in L.load_lane_items(self.cfg, region, "test"):
            if it.image_id in idx and "A" in idx[it.image_id] and "B" in idx[it.image_id]:
                out.append({"image_id": it.image_id, "dataset": it.dataset, "width": it.width, "height": it.height})
        return out

    def app_predict(self, body: dict) -> dict:
        from . import guard
        from .feedback import ACTIONS as APP_ACTIONS
        image_id, test = str(body["image_id"]), str(body.get("test") or "B")
        mode = "saved" if body.get("mode") == "saved" else "live"
        it = self._lane_item(image_id)
        t0 = time.time()
        if mode == "saved":
            if test not in ("A", "B"):
                raise ValueError("Saved answers exist for Test A (photo only) and Test B (photo + local rules).")
            run_id = self._app_index().get(image_id, {}).get(test)
            if not run_id:
                raise KeyError("No saved answer of the main configuration for this photo; use a live model.")
            run = L.load_lane_run(self.cfg, run_id)
            rec = json.loads(json.dumps(next(r for r in run["records"] if r["image_id"] == image_id)))
            rec["from_run"] = {"run_id": run_id, "prompt": run["manifest"]["prompt_hashes"].get("prompt_dir", ""),
                               "model": run["manifest"]["settings"].get("model", "")}
            self._lane_extras(rec, it.region)
            check = guard.verify(C.repo_of(self.cfg), it.region, rec, it.path)
            rid = self._applog().log_prediction(rec, check, self.cfg, mode)
            if self.metrics:
                self.metrics.app_prediction(rec, check, mode, time.time() - t0)
            ans = rec.get("answer") or {}
            out = {"request_id": rid, "check": check, "passages": rec.get("passages", {}), "rec": rec,
                   "answer": {k: ans.get(k) for k in ("scene", "lane_count", "ego_lane_index", "left_boundary", "right_boundary",
                                                       "lane_markings", "element_rules", "action_reasons", "actions", "advice")},
                   "latency_s": None, "model": rec["from_run"]["model"], "error": rec.get("error") or rec.get("parse_error") or ""}
            rules = it.region if test == "B" else None
        else:
            rules = body.get("rules")
            if rules is None:
                rules = it.region if test == "B" else "none"
            test, rules = self.app_test_for(it.region, rules)
            out = self.app_answer(it, test, str(body.get("model") or "server"), rules, mode, str(body.get("session") or ""))
        rec = out.pop("rec")
        label = (rec.get("label") or {}) if it.collection != "upload" else {}
        return {**{k: v for k, v in out.items() if k not in ("seconds",)}, "mode": mode, "image_id": image_id,
                "region": it.region, "test": test, "rules": rules, "from_run": rec.get("from_run"),
                "label_actions": {a: label.get(f"act_{a}") for a in APP_ACTIONS} if label and test != "C" else None}

    def app_feedback(self, body: dict) -> dict:
        source = body.get("source") if body.get("source") in ("user", "simulated_reviewer") else "user"
        row = self._applog().add_feedback(body, source)   # simulated_reviewer: scripts/demo_traffic.py, kept apart
        if self.metrics:
            self.metrics.feedback(row)
        return {"ok": True, "themes": row["themes"]}

    def app_summary(self) -> dict:
        return self._applog().summary()

    # ------------------------------------------------------------ batch
    def start_run(self, body: dict) -> dict:
        """Start a batch run in the background: Test A, Test B, or both at the same time (test "AB")."""
        with self.lock:
            if self.job["running"]:
                return {"ok": False, "error": "A run is already going."}
            test = body.get("test") or self.cfg["run"]["test"]
            tests = ["A", "B"] if test == "AB" else [test]
            if any(t not in C.TESTS for t in tests):
                raise ValueError(f"Unknown test {test}.")
            region = body.get("region") or self.cfg["run"]["region"]
            task = body.get("task") or "marking"
            self.job = {"running": True, "done": 0, "total": 0, "per": {t: [0, 0] for t in tests}, "run_id": "", "run_ids": {},
                        "error": "", "test": test, "region": region, "mock": self.cfg.get("mock", False), "task": task, "log": []}
            self.job_records = {}

        if self.metrics:
            for t in tests:
                self.metrics.batches.labels(task, t, region, "mock" if self.cfg.get("mock") else "real").inc()
            self.metrics.running.set(1)

        def progress(t, done, total, rec):
            if self.metrics:
                self.metrics.answer(self.cfg, rec, "batch", task)
            with self.lock:
                self.job_records[(t, rec.get("image_id"))] = rec
                self.job["log"].append(self._log_entry(rec, done, total))
                self.job["per"][t] = [done, total]
                self.job["done"] = sum(v[0] for v in self.job["per"].values())
                self.job["total"] = sum(v[1] for v in self.job["per"].values())
                if rec.get("error") and not self.job["error"]:
                    self.job["error"] = rec["error"]

        def one(t):
            try:
                if task == "lane":
                    rid = L.run_lane(self.cfg, t, region, int(body.get("limit") or 0), body.get("split") or "dev", self.cfg.get("mock", False),
                                     progress=lambda d, n, r: progress(t, d, n, r), log=lambda *a: None, use_cache=bool(body.get("cache", True)))
                else:
                    rid = run_batch(self.cfg, t, region, int(body.get("limit") or 0), int(body.get("repeats") or 1),
                                    body.get("split") or "any", self.cfg.get("mock", False), progress=lambda d, n, r: progress(t, d, n, r),
                                    log=lambda *a: None, use_cache=bool(body.get("cache", True)))
                with self.lock:
                    self.job["run_ids"][t] = rid
                    self.job["run_id"] = rid
            except Exception as e:  # noqa: BLE001
                with self.lock:
                    self.job["error"] = str(e)

        def work():
            threads = [threading.Thread(target=one, args=(t,), daemon=True) for t in tests]
            for th in threads:
                th.start()
            for th in threads:
                th.join()
            with self.lock:
                self.job["running"] = False
            if self.metrics:
                self.metrics.running.set(0)

        threading.Thread(target=work, daemon=True).start()
        return {"ok": True}

    def progress(self, since: int = 0) -> dict:
        with self.lock:
            out = dict(self.job)
            log = self.job.get("log") or []
            out["log"], out["log_total"] = log[since:], len(log)
            return out


def make_handler(demo: Demo):
    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, code, body: bytes, ctype: str):
            if demo.metrics:
                demo.metrics.request(self.command, urlparse(self.path).path, code)
            try:
                self.send_response(code)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(body)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def _sse(self):
            """Start a text/event-stream answer; returns emit(kind, obj)."""
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Accel-Buffering", "no")
            self.end_headers()
            if demo.metrics:
                demo.metrics.request(self.command, urlparse(self.path).path, 200)
            lock = threading.Lock()

            def emit(kind, obj):
                with lock:
                    try:
                        self.wfile.write(f"event: {kind}\ndata: {json.dumps(obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                        self.wfile.flush()
                    except (BrokenPipeError, ConnectionResetError):
                        pass
            return emit

        def _send_file(self, path: Path, ctype: str, download: bool = False):
            """A file with byte ranges (Safari plays a <video> only when the server answers Range requests)."""
            size = path.stat().st_size
            rng = self.headers.get("Range") or ""
            start, end, code = 0, size - 1, 200
            if rng.startswith("bytes="):
                a, _, b = rng[6:].split(",")[0].partition("-")
                if a.strip():
                    start, end = int(a), min(int(b), size - 1) if b.strip() else size - 1
                elif b.strip():
                    start = max(0, size - int(b))
                code = 206
            if start > end or start >= size:
                self.send_response(416)
                self.send_header("Content-Range", f"bytes */{size}")
                self.end_headers()
                return
            if demo.metrics:
                demo.metrics.request(self.command, urlparse(self.path).path, code)
            try:
                self.send_response(code)
                self.send_header("Content-Type", ctype)
                self.send_header("Accept-Ranges", "bytes")
                self.send_header("Content-Length", str(end - start + 1))
                if code == 206:
                    self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
                if download:
                    self.send_header("Content-Disposition", f'attachment; filename="{path.name}"')
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                with path.open("rb") as f:
                    f.seek(start)
                    left = end - start + 1
                    while left > 0:
                        chunk = f.read(min(1 << 20, left))
                        if not chunk:
                            break
                        self.wfile.write(chunk)
                        left -= len(chunk)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def _json(self, obj, code=200):
            self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

        def _err(self, e):
            if not isinstance(e, (KeyError, ValueError, C.ConfigError, FileNotFoundError)):
                traceback.print_exc()
            self._json({"error": str(e).strip("'")}, 400)

        def do_GET(self):
            u = urlparse(self.path)
            q = {k: v[0] for k, v in parse_qs(u.query).items()}
            try:
                if u.path in ("/", "/index.html"):
                    return self._send(200, (WEB / "demo.html").read_bytes(), "text/html; charset=utf-8")
                if u.path in ("/app", "/app.html"):
                    return self._send(200, (WEB / "app.html").read_bytes(), "text/html; charset=utf-8")
                if u.path == "/api/app/info":
                    return self._json(demo.app_info(q.get("session", "")))
                if u.path == "/api/app/userkey":
                    return self._json(demo.user_key_info(q.get("session", "")))
                if u.path == "/api/app/examples":
                    return self._json(demo.app_examples(q.get("region") or "US"))
                if u.path == "/api/app/summary":
                    return self._json(demo.app_summary())
                if u.path == "/api/app/video/status":
                    return self._json(demo.video.status(q.get("job", "")))
                if u.path == "/api/app/video/file":
                    return self._send_file(demo.video.file(q.get("job", ""), q.get("name", "")), "video/mp4",
                                           download=q.get("download") == "1")
                if u.path in ("/review", "/review.html"):
                    return self._send(200, (WEB / "review.html").read_bytes(), "text/html; charset=utf-8")
                if u.path in ("/project", "/project.html"):
                    return self._send(200, (WEB / "project.html").read_bytes(), "text/html; charset=utf-8")
                if u.path.startswith("/api/project/"):
                    return self._project_get(u.path[len("/api/project/"):], q)
                if u.path == "/healthz":
                    return self._send(200, b"ok", "text/plain")
                if u.path == "/metrics":
                    if demo.metrics:
                        demo._applog()          # count the answers and feedback already on disk before the first scrape
                    if not demo.metrics:
                        return self._send(404, b"metrics need the prometheus_client package", "text/plain")
                    body, ctype = demo.metrics.exposition()
                    return self._send(200, body, ctype)
                if u.path.startswith("/static/"):
                    f = WEB / Path(u.path).name
                    if not f.is_file():
                        return self._send(404, b"not found", "text/plain")
                    ctype = {"js": "text/javascript", "css": "text/css"}.get(f.suffix[1:], "application/octet-stream")
                    return self._send(200, f.read_bytes(), ctype + "; charset=utf-8")
                if u.path == "/api/config":
                    return self._json(demo.config())
                task = q.get("task", "marking")
                if u.path == "/api/items":
                    return self._json(demo.items(q.get("region") or demo.cfg["run"]["region"], task, q.get("split", "dev")))
                if u.path == "/api/image":
                    return self._send(200, demo.image(q["id"], int(q["w"]) if q.get("w") else None, task, q.get("lines") == "1"), "image/jpeg")
                if u.path == "/api/prompt":
                    return self._json(demo.prompt(q.get("test", "A"), q.get("region") or demo.cfg["run"]["region"], task))
                if u.path == "/api/saved":
                    return self._json(demo.saved(q["id"]))
                if u.path == "/api/progress":
                    return self._json(demo.progress(int(q.get("since") or 0)))
                if u.path == "/api/ask_stream":
                    return demo.ask_stream(q["id"], q.get("test", "A"), q.get("cache", "1") == "1", self._sse())
                if u.path == "/api/passages":
                    return self._json(demo.passages_lane(q.get("region") or demo.cfg["run"]["region"]))
                if u.path == "/api/run_records":
                    return self._json(demo.run_records(q["id"]))
                if u.path == "/api/record":
                    return self._json(demo.record(q.get("run") or None, q.get("test", "A"), q["id"]))
                if u.path == "/api/runs":
                    return self._json(L.list_lane_runs(demo.cfg) if task == "lane" else list_runs(demo.cfg))
                if u.path == "/api/run":
                    r = load_run(demo.cfg, q["id"])
                    return self._json({"manifest": {k: v for k, v in r["manifest"].items() if k != "config"},
                                       "summary": (r["scores"] or {}).get("summary")})
                if u.path == "/api/compare":
                    return self._json(L.compare_lane_runs(demo.cfg, q["a"], q["b"], q.get("reviewed") == "1") if task == "lane"
                                      else compare_runs(demo.cfg, q["a"], q["b"]))
                if u.path == "/api/review/items":
                    return self._json(demo.review_items(q.get("region") or demo.cfg["run"]["region"]))
                if u.path == "/api/review/effect":
                    return self._json(demo.review_effect(q.get("region") or demo.cfg["run"]["region"]))
                return self._send(404, b"not found", "text/plain")
            except Exception as e:  # noqa: BLE001
                return self._err(e)

        def _project_get(self, what, q):
            pr = demo.project
            if what == "overview":
                return self._json(pr.overview())
            if what == "results":
                return self._json(pr.results())
            if what == "evaluate":
                return self._json(pr.evaluate(q["run"], q.get("other") or None))
            if what == "regulations":
                return self._json(pr.regulations())
            if what == "draft":
                return self._json(pr.draft(q["code"]))
            if what == "passages":
                return self._json(pr.passages(q["code"]))
            if what == "carla":
                return self._json(pr.carla())
            if what == "carla_image":
                return self._send(200, pr.carla_image(q["run"], q.get("kind", "frames"), q["name"]), "image/png")
            if what == "carla_video":
                f = pr.carla_video(q["run"])
                return self._send(200, f.read_bytes(), "video/mp4")
            if what == "jobs":
                return self._json(pr.jobs.state(json.loads(q.get("since") or "{}")))
            return self._send(404, b"not found", "text/plain")

        def _project_post(self, what, body):
            pr = demo.project
            if what == "upload":
                return self._json({"file": pr.save_upload(body)})
            if what == "estimate":
                return self._json(pr.estimate(body))
            if what == "extract":
                return self._json({"job": pr.extract(body)})
            if what == "accept":
                return self._json(pr.accept(body["code"]))
            if what == "start_carla":
                return self._json(pr.start_carla())
            if what == "run_route":
                return self._json({"job": pr.run_route(body)})
            return self._send(404, b"not found", "text/plain")

        def do_POST(self):
            u = urlparse(self.path)
            try:
                n = int(self.headers.get("Content-Length") or 0)
                if u.path == "/api/app/video/upload":   # raw video bytes, not JSON
                    q = {k: v[0] for k, v in parse_qs(u.query).items()}
                    return self._json(demo.video.receive(self.rfile, n, q.get("name", "")))
                body = json.loads(self.rfile.read(n) or b"{}")
                if u.path == "/api/config":
                    return self._json(demo.update(body))
                if u.path == "/api/ask":
                    return self._json(demo.ask(body["image_id"], body.get("test", "A"), bool(body.get("cache", True)), body.get("task", "marking")))
                if u.path == "/api/run":
                    return self._json(demo.start_run(body))
                if u.path == "/api/upload":
                    return self._json(demo.upload(body))
                if u.path == "/api/app/predict":
                    return self._json(demo.app_predict(body))
                if u.path == "/api/feedback":
                    return self._json(demo.app_feedback(body))
                if u.path == "/api/app/video/start":
                    return self._json(demo.video.start(body))
                if u.path == "/api/app/video/delete":
                    return self._json(demo.video.delete(body))
                if u.path == "/api/app/userkey":
                    return self._json(demo.user_key_set(body))
                if u.path == "/api/app/userkey/check":
                    return self._json(demo.user_key_check(body))
                if u.path == "/api/app/userkey/clear":
                    return self._json(demo.user_key_clear(body))
                if u.path == "/api/review/decide":
                    return self._json(demo.review_decide(body))
                if u.path.startswith("/api/project/"):
                    return self._project_post(u.path[len("/api/project/"):], body)
                return self._send(404, b"not found", "text/plain")
            except Exception as e:  # noqa: BLE001
                return self._err(e)

    return H


def _bind(cfg: dict, port: int, host: str = "127.0.0.1") -> tuple[ThreadingHTTPServer, str]:
    demo = Demo(cfg)
    for p in range(port, port + 20):
        try:
            httpd = ThreadingHTTPServer((host, p), make_handler(demo))
            httpd.daemon_threads = True
            return httpd, f"http://{'127.0.0.1' if host in ('0.0.0.0', '::') else host}:{p}/"
        except OSError:
            continue
    raise RuntimeError("No free port.")


def serve(cfg: dict, port: int = 8770, open_browser: bool = True, host: str = "127.0.0.1") -> None:
    """Run the demo until Ctrl+C (command line)."""
    httpd, url = _bind(cfg, port, host)
    print(f"Demo is running at {url}  ({'MOCK answers' if cfg.get('mock') else 'real API calls'}). Press Ctrl+C to stop.", flush=True)
    if open_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        httpd.server_close()


_RUNNING: dict = {}


def start(cfg: dict, port: int = 8770, open_browser: bool = True) -> str:
    """Run the demo in the background (Jupyter keeps working); stop() ends it. Returns the address."""
    stop()
    httpd, url = _bind(cfg, port)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    _RUNNING["httpd"] = httpd
    if open_browser:
        webbrowser.open(url)
    return url


def stop() -> None:
    httpd = _RUNNING.pop("httpd", None)
    if httpd:
        httpd.shutdown()
        httpd.server_close()
