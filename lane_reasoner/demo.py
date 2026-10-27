"""Demo page: pick a labeled image, see the exact prompt, ask the model (Test A / Test B), compare with the label,
run a whole batch and compare two runs. A small web server on 127.0.0.1 that only you can reach."""
from __future__ import annotations

import json
import threading
import traceback
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import cv2
import numpy as np

from . import config as C
from .data import boxed_jpeg, load_items
from .prompts import passages, prompt_parts
from .runner import Context, ask, compare_runs, list_runs, load_run, run_batch

WEB = Path(__file__).resolve().parent / "web"
EDITABLE = {"mock": bool, "run.test": str, "run.region": str, "run.repeats": int, "run.limit": int, "run.split": str,
            "api.model": str, "api.reasoning_effort": str, "api.temperature": float, "api.image_detail": str,
            "api.max_output_tokens": int, "api.parallel": int}


class Demo:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.lock = threading.RLock()
        self.job = {"running": False, "done": 0, "total": 0, "run_id": "", "error": "", "test": "", "region": ""}

    # ------------------------------------------------------------ settings
    def config(self) -> dict:
        cfg = C.public(self.cfg)
        counts = {}
        for r in self.cfg["regions"]:
            try:
                counts[r] = len(load_items(self.cfg, r, "any", []))
            except Exception:  # noqa: BLE001
                counts[r] = 0
        return {"config": cfg, "tests": C.TESTS, "items_per_region": counts}

    def update(self, body: dict) -> dict:
        with self.lock:
            for path, typ in EDITABLE.items():
                if path not in body:
                    continue
                v = body[path]
                if v in ("", None) and path in ("api.reasoning_effort", "api.temperature"):
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
        return self.config()

    # ------------------------------------------------------------ data
    def items(self, region: str) -> list[dict]:
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

    def image(self, image_id: str, width: int | None) -> bytes:
        jpeg = boxed_jpeg(self._item(image_id), self.cfg)
        if not width:
            return jpeg
        img = cv2.imdecode(np.frombuffer(jpeg, np.uint8), cv2.IMREAD_COLOR)
        h = int(round(img.shape[0] * width / img.shape[1]))
        ok, buf = cv2.imencode(".jpg", cv2.resize(img, (int(width), h), interpolation=cv2.INTER_AREA), [cv2.IMWRITE_JPEG_QUALITY, 80])
        return buf.tobytes()

    def prompt(self, test: str, region: str) -> dict:
        return prompt_parts(self.cfg, test, region)

    def passage_map(self, region: str) -> dict:
        from video_tool.packages import _translations
        from types import SimpleNamespace
        zh = _translations(SimpleNamespace(repo=C.repo_of(self.cfg)))
        return {p["rule_id"]: {"text_en": p.get("text_en", ""), "text_zh": p.get("text_zh") or zh.get(p["rule_id"], ""),
                               "section": p.get("section", ""), "source": p.get("source", "")} for p in passages(self.cfg, region)}

    def ask(self, image_id: str, test: str, use_cache: bool = True) -> dict:
        it = self._item(image_id)
        rec = ask(self.cfg, it, test, 0, self.cfg.get("mock", False), use_cache=use_cache)
        cid = (rec.get("answer") or {}).get("cited_rule_id")
        pm = self.passage_map(it.region)
        rec["cited_passage"] = pm.get(cid) if cid else None
        rec["accepted_passages"] = {i: pm.get(i) for i in (it.label.get("accepted_rule_ids") or "").split(";") if i}
        from .runner import cost_of
        rec["cost_usd"] = round(cost_of(self.cfg, (rec.get("response") or {}).get("usage") or {}), 5) if not rec.get("cached") else 0
        return rec

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
            self.job = {"running": True, "done": 0, "total": 0, "per": {t: [0, 0] for t in tests}, "run_id": "", "run_ids": {},
                        "error": "", "test": test, "region": region, "mock": self.cfg.get("mock", False)}

        def progress(t, done, total, rec):
            with self.lock:
                self.job["per"][t] = [done, total]
                self.job["done"] = sum(v[0] for v in self.job["per"].values())
                self.job["total"] = sum(v[1] for v in self.job["per"].values())
                if rec.get("error") and not self.job["error"]:
                    self.job["error"] = rec["error"]

        def one(t):
            try:
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

        threading.Thread(target=work, daemon=True).start()
        return {"ok": True}

    def progress(self) -> dict:
        with self.lock:
            return dict(self.job)


def make_handler(demo: Demo):
    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, code, body: bytes, ctype: str):
            try:
                self.send_response(code)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(body)
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
                if u.path.startswith("/static/"):
                    f = WEB / Path(u.path).name
                    if not f.is_file():
                        return self._send(404, b"not found", "text/plain")
                    ctype = {"js": "text/javascript", "css": "text/css"}.get(f.suffix[1:], "application/octet-stream")
                    return self._send(200, f.read_bytes(), ctype + "; charset=utf-8")
                if u.path == "/api/config":
                    return self._json(demo.config())
                if u.path == "/api/items":
                    return self._json(demo.items(q.get("region") or demo.cfg["run"]["region"]))
                if u.path == "/api/image":
                    return self._send(200, demo.image(q["id"], int(q["w"]) if q.get("w") else None), "image/jpeg")
                if u.path == "/api/prompt":
                    return self._json(demo.prompt(q.get("test", "A"), q.get("region") or demo.cfg["run"]["region"]))
                if u.path == "/api/progress":
                    return self._json(demo.progress())
                if u.path == "/api/runs":
                    return self._json(list_runs(demo.cfg))
                if u.path == "/api/run":
                    r = load_run(demo.cfg, q["id"])
                    return self._json({"manifest": {k: v for k, v in r["manifest"].items() if k != "config"},
                                       "summary": (r["scores"] or {}).get("summary")})
                if u.path == "/api/compare":
                    return self._json(compare_runs(demo.cfg, q["a"], q["b"]))
                return self._send(404, b"not found", "text/plain")
            except Exception as e:  # noqa: BLE001
                return self._err(e)

        def do_POST(self):
            u = urlparse(self.path)
            try:
                n = int(self.headers.get("Content-Length") or 0)
                body = json.loads(self.rfile.read(n) or b"{}")
                if u.path == "/api/config":
                    return self._json(demo.update(body))
                if u.path == "/api/ask":
                    return self._json(demo.ask(body["image_id"], body.get("test", "A"), bool(body.get("cache", True))))
                if u.path == "/api/run":
                    return self._json(demo.start_run(body))
                return self._send(404, b"not found", "text/plain")
            except Exception as e:  # noqa: BLE001
                return self._err(e)

    return H


def _bind(cfg: dict, port: int) -> tuple[ThreadingHTTPServer, str]:
    demo = Demo(cfg)
    for p in range(port, port + 20):
        try:
            httpd = ThreadingHTTPServer(("127.0.0.1", p), make_handler(demo))
            httpd.daemon_threads = True
            return httpd, f"http://127.0.0.1:{p}/"
        except OSError:
            continue
    raise RuntimeError("No free port.")


def serve(cfg: dict, port: int = 8770, open_browser: bool = True) -> None:
    """Run the demo until Ctrl+C (command line)."""
    httpd, url = _bind(cfg, port)
    print(f"Demo is running at {url}  ({'MOCK answers' if cfg.get('mock') else 'real API calls'}). Press Ctrl+C to stop.")
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
