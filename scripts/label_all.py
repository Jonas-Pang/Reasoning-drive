"""Written by Claude: ONE labeling window for every country in configs/labeling_regions.json (now China, MapDR,
and the US, BDD100K). To add a country: build its workspace (python main.py label --data <DATASETS_ROOT>/<folder>
images init <dataset>), then add one entry to configs/labeling_regions.json; it appears in the same window.

    python scripts/label_all.py [--port 8780] [--no-browser]        (or double-click scripts/label_all.bat)

Starts one labeling tool per country inside this one process (China on 8765, US on 8766, as before; each still works
on its own address) and puts a single address in front of them, http://127.0.0.1:8780/ :
  * Lane labeling (tabs ② and ③): the images of BOTH countries in one list. A selector in the lane page's top bar shows
    all, only China or only the US. Every image is saved to its own country's files, exactly as in the separate tools.
  * Picking images (tab ①), the single-marking form and packages (tab ④) belong to one dataset at a time: the
    "中国 / 美国" switch at the top of the page chooses which.
Nothing about the label files changes; this only routes each request to the tool that owns the image.
The country switch at the top and the country menu of the lane page move together (fixed 2026-11-16: they were two
separate settings, so the lane page could still show India after the switch was set to the UK).
Only one copy can run: a second start finds the address taken, opens the running window and stops (two copies used
to share the same ports on Windows and keep separate in-memory states).
The window is at 8780; 8770 stays free for the demo and blind-review page (python main.py ... --port 8770).
Close this window to stop everything."""
import socket
import http.client
import json
import re
import sys
import threading
import time
import webbrowser
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

repo = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo))
from reasoning_drive.labeling.core import Paths, Trip, default_labeler   # noqa: E402
from reasoning_drive.labeling.server import QuietServer, serve           # noqa: E402

PORT = int(sys.argv[sys.argv.index("--port") + 1]) if "--port" in sys.argv else 8780
CONFIG = repo / "configs" / "labeling_regions.json"   # one entry per country: add a line there to add a country


def load_tools() -> list:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    return [(c["region"], c["workspace"], c["set_id"], int(c["port"]), c.get("name") or c["region"])
            for c in cfg["regions"] if c.get("enabled", True)]


TOOLS = load_tools()


class ExclusiveServer(QuietServer):
    """The front address, taken before anything else starts and never shared with a second copy of this script."""
    allow_reuse_address = False

    def server_bind(self):
        if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):   # Windows: refuse a second bind of the same address
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()


try:
    httpd = ExclusiveServer(("127.0.0.1", PORT), BaseHTTPRequestHandler)   # the real handler is set further down
except OSError:
    print(f"The labeling window is already running: http://127.0.0.1:{PORT}/  (opening it; close the other window "
          "first if you want to restart)", flush=True)
    if "--no-browser" not in sys.argv:
        webbrowser.open(f"http://127.0.0.1:{PORT}/")
    time.sleep(3)
    sys.exit(0)
logp = repo / "results" / "claude_logs" / "label_all.log"
logp.parent.mkdir(parents=True, exist_ok=True)
logf = open(logp, "a", encoding="utf-8")


def say(m):
    print(m, flush=True)
    logf.write(m + "\n")
    logf.flush()


def datasets_root() -> Path:
    v = ""
    for line in (repo / ".env").read_text(encoding="utf-8").splitlines():
        k, _, val = line.partition("=")
        if k.strip() == "DATASETS_ROOT":
            v = val.strip().strip('"')
    p = Path(v)
    return p if p.is_absolute() else (repo / p).resolve()


# ------------------------------------------------------------------ start both tools in this process
ports: dict[str, int] = {}
set_region: dict[str, str] = {}
root = datasets_root()
say(f"=== {time.strftime('%Y-%m-%d %H:%M:%S')}  datasets root {root}")
missing = [t for t in TOOLS if not (root / t[1]).is_dir()]
for t in missing:
    say(f"[{t[0]}] skipped: workspace {root / t[1]} not found")
TOOLS = [t for t in TOOLS if t not in missing]
if not TOOLS:
    say(f"No workspace found; check {CONFIG}")
    sys.exit(1)
for region, ws, sid, port, _ in TOOLS:
    paths = Paths.discover(repo, root / ws)
    trip = Trip(paths, sid)
    set_region[sid] = region

    def run(paths=paths, trip=trip, port=port, region=region):
        def log(msg):
            m = re.search(r"http://127\.0\.0\.1:(\d+)/", msg)
            if m:
                ports[region] = int(m.group(1))
            say(f"[{region}] {msg}")
        try:
            serve(paths, trip, default_labeler(), port=port, open_browser=False, log=log)
        except Exception as e:  # noqa: BLE001
            say(f"[{region}] could not start: {e}")
            ports.setdefault(region, -1)
    threading.Thread(target=run, daemon=True).start()

t0 = time.time()
while len(ports) < len(TOOLS) and time.time() - t0 < 120:
    time.sleep(0.3)
if any(p < 0 for p in ports.values()) or len(ports) < len(TOOLS):
    say("A labeling tool did not start (see above). Close other labeling windows and try again.")
    input("Press Enter to close.")
    sys.exit(1)
say(f"Backends: {ports}")


# ------------------------------------------------------------------ the single address in front
def backend_call(region: str, method: str, path: str, body: bytes | None = None, ctype: str | None = None):
    c = http.client.HTTPConnection("127.0.0.1", ports[region], timeout=300)
    headers = {"Content-Type": ctype} if ctype else {}
    c.request(method, path, body=body, headers=headers)
    r = c.getresponse()
    data = r.read()
    out = (r.status, data, r.getheader("Content-Type") or "application/octet-stream", r.getheader("Location"))
    c.close()
    return out


def region_of_image(image_id: str) -> str:
    sid = image_id.split("__", 1)[0] if "__" in image_id else image_id.rsplit("_f", 1)[0]
    return set_region.get(sid, TOOLS[0][0])


NAMES = {r: name for r, _, _, _, name in TOOLS}

SWITCH = """<span id="rd-switch" title="选图、单标线和打包用这个数据集；车道标注（②③）各国同列" style="display:inline-flex;
align-items:center;gap:4px;margin:0 8px;white-space:nowrap;font-size:13px">%s</span>
<script>function rdSet(r){var a=';path=/;max-age=31536000';document.cookie='rd_region='+r+a;
document.cookie='rd_lane_region='+r+a;location.reload()}</script>"""

LANE_FILTER = """<select id="rd-lane-region" title="Country" style="margin-left:6px">%s</select>
<script>document.getElementById('rd-lane-region').onchange=function(){var a=';path=/;max-age=31536000';
document.cookie='rd_lane_region='+this.value+a;if(this.value!=='all')document.cookie='rd_region='+this.value+a;
location.reload()}</script>"""


class Front(BaseHTTPRequestHandler):
    server_version = "reasoning_drive_label_all"

    def log_message(self, fmt, *args):
        pass

    def _cookie(self, name, default):
        c = SimpleCookie(self.headers.get("Cookie") or "")
        return c[name].value if name in c else default

    def _send(self, code, body: bytes, ctype: str, location: str | None = None):
        try:
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            if location:
                self.send_header("Location", location)
            self.end_headers()
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def _json(self, obj, code=200):
        self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def _pass(self, region, method, body=None):
        st, data, ctype, loc = backend_call(region, method, self.path, body, self.headers.get("Content-Type"))
        self._send(st, data, ctype, loc)

    def _lane_state(self):
        want = self._cookie("rd_lane_region", "all")
        merged, items, counts = None, [], {}
        for region, *_ in TOOLS:
            st, data, _, _ = backend_call(region, "GET", "/lanes/api/state")
            s = json.loads(data)
            if "error" in s:
                return self._json(s, 400)
            if merged is None:
                merged = s
            else:   # rule passages and rule tables of every country, whichever tool sent them
                for key in ("passages", "rules"):
                    for code, v in (s.get(key) or {}).items():
                        merged.setdefault(key, {}).setdefault(code, v)
            items += [it for it in s["items"] if want in ("all", it.get("region"))]
        for it in items:
            counts[it["status"]] = counts.get(it["status"], 0) + 1
        counts["mine_done"] = sum(it.get("mine") == "done" for it in items)
        counts["images"] = len(items)
        merged.update(items=sorted(items, key=lambda it: (it.get("region", ""), it.get("split", ""), it["image_id"])),
                      counts=counts, data=" + ".join(NAMES.values()), collection="all")
        return self._json(merged)

    def do_GET(self):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        main = self._cookie("rd_region", TOOLS[0][0])
        main = main if main in ports else TOOLS[0][0]
        try:
            if u.path.startswith("/lanes/"):
                sub = u.path[len("/lanes"):]
                if sub == "/api/state":
                    return self._lane_state()
                if sub in ("/api/item", "/api/image") and "id" in q:
                    return self._pass(region_of_image(q["id"]), "GET")
                if sub in ("/", "/index.html"):
                    st, data, ctype, _ = backend_call(TOOLS[0][0], "GET", self.path)
                    want = self._cookie("rd_lane_region", "all")
                    opts = "".join(f'<option value="{v}"{" selected" if v == want else ""}>{t}</option>'
                                   for v, t in [("all", "全部国家")] + [(r, NAMES[r]) for r, *_ in TOOLS])
                    html = data.decode("utf-8").replace('</select>', '</select>' + LANE_FILTER % opts, 1)
                    return self._send(st, html.encode("utf-8"), ctype)
                return self._pass(main if sub == "/api/agreement" else TOOLS[0][0], "GET")
            if u.path in ("/", "/index.html"):
                st, data, ctype, loc = backend_call(main, "GET", self.path)
                if st == 200 and "html" in ctype:
                    btns = "".join(
                        f'<button onclick="rdSet(\'{r}\')" style="padding:2px 8px;border-radius:4px;'
                        f'border:0;cursor:pointer;{"background:#4a8;color:#fff;font-weight:bold" if r == main else ""}">'
                        f'{NAMES[r]}</button>' for r, *_ in TOOLS)
                    html, sw = data.decode("utf-8"), SWITCH % btns
                    brand = '<div class="brand">Lane Labeler</div>'
                    html = html.replace(brand, brand + sw, 1) if brand in html else html.replace("<body>", "<body>" + sw, 1)
                    data = html.encode("utf-8")
                return self._send(st, data, ctype, loc)
            return self._pass(main, "GET")
        except Exception as e:  # noqa: BLE001
            return self._json({"error": f"{type(e).__name__}: {e}"}, 500)

    def do_POST(self):
        u = urlparse(self.path)
        raw = self.rfile.read(int(self.headers.get("Content-Length") or 0))
        main = self._cookie("rd_region", TOOLS[0][0])
        main = main if main in ports else TOOLS[0][0]
        try:
            if u.path.startswith("/lanes/"):
                body = json.loads(raw or b"{}")
                if u.path == "/lanes/api/check":
                    region = body.get("region") if body.get("region") in ports else TOOLS[0][0]
                elif body.get("image_id"):
                    region = region_of_image(body["image_id"])
                else:
                    region = main
                return self._pass(region, "POST", raw)
            return self._pass(main, "POST", raw)
        except Exception as e:  # noqa: BLE001
            return self._json({"error": f"{type(e).__name__}: {e}"}, 500)


httpd.RequestHandlerClass = Front
url = f"http://127.0.0.1:{PORT}/"
say(f"One labeling window for {' + '.join(NAMES.values())}: {url}   (lane page only: {url}lanes/)")
say("Close this window to stop.")
if "--no-browser" not in sys.argv:
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
