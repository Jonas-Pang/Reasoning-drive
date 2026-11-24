"""Checks of the project layout and of the parts that tie it together, without the API and without CARLA:
the folders, the settings split over configs/, the countries in regulations/ (template, checks, a new country from a
PDF with the extractor, real requests answered by a fake API server), the datasets per country, the evaluation of a
saved run, the results index and the simulation settings."""
from __future__ import annotations

import io
import json
import os
import shutil
import tempfile
from pathlib import Path

from .. import paths as P


def tiny_pdf(pages: list[list[str]]) -> bytes:
    """A minimal PDF with one list of text lines per page (standard Helvetica font)."""
    objs: list[str] = []

    def add(s: str) -> int:
        objs.append(s)
        return len(objs)

    font = add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    contents = []
    for lines in pages:
        esc = [ln.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)") for ln in lines]
        text = "BT /F1 11 Tf 50 750 Td 14 TL " + " ".join(f"({x}) '" for x in esc) + " ET"
        contents.append(add(f"<< /Length {len(text)} >>\nstream\n{text}\nendstream"))
    pages_id = len(objs) + len(pages) + 1
    kids = [add(f"<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 612 792] /Contents {c} 0 R "
                f"/Resources << /Font << /F1 {font} 0 R >> >> >>") for c in contents]
    add(f"<< /Type /Pages /Kids [{' '.join(f'{k} 0 R' for k in kids)}] /Count {len(kids)} >>")
    cat = add(f"<< /Type /Catalog /Pages {pages_id} 0 R >>")
    out, offs = "%PDF-1.4\n", []
    for i, o in enumerate(objs, 1):
        offs.append(len(out.encode("latin-1")))
        out += f"{i} 0 obj\n{o}\nendobj\n"
    xref = len(out.encode("latin-1"))
    out += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n" + "".join(f"{o:010d} 00000 n \n" for o in offs)
    out += f"trailer\n<< /Size {len(objs) + 1} /Root {cat} 0 R >>\nstartxref\n{xref}\n%%EOF\n"
    return out.encode("latin-1")


PAGES = [["1 General", "Paint quality and retroreflectivity are described in Annex A."],
         ["4.1 Lane lines", "A broken white lane line may be crossed when it is safe to change lanes.",
          "A solid white lane line shall not be crossed."],
         ["5.2 Arrows", "A left-turn arrow in a lane means that traffic in that lane shall turn left."]]


def run(log=print) -> bool:
    from .. import config as C
    from ..evaluation import evaluate as E
    from ..evaluation import registry as G
    from ..regulations import extract as X
    from ..regulations import store as S
    results: list[bool] = []

    def check(ok, text, detail=""):
        results.append(bool(ok))
        log(("PASS " if ok else "FAIL ") + text + (f" — {detail}" if detail and not ok else ""))

    repo = P.REPO
    # inside the Docker image datasets/ is a mounted folder; without the mount it is empty
    has_datasets = any((repo / P.DATASETS).glob("*/dataset.yaml"))
    if not has_datasets:
        log("SKIP datasets checks: datasets/ is empty (the Docker image without the mounted folder)")
    want = [P.API_FILE, P.EXPERIMENT_FILE, P.CARLA_FILE, P.EXPERIMENTS_FILE, P.LABEL_SCHEMA, P.LANE_SCHEMA,
            P.REGULATIONS_TEMPLATE + "/region.yaml", "prompts/regulation_extraction/instructions.txt"]
    want += [P.DATASETS_TEMPLATE + "/dataset.yaml"] if has_datasets else []
    missing = [w for w in want if not (repo / w).exists()]
    check(not missing and P.is_repo(repo), "layout: configs/, prompts/, regulations/ (with _template), datasets/ (with _template), results/",
          ", ".join(missing))

    cfg = C.load(repo)
    check(set(cfg["regions"]) >= {"US", "CN"} and cfg["api"]["model"] and cfg["regions"]["CN"]["lane_rules_files"][0].startswith("regulations/CN/"),
          "settings: model from configs/api.yaml, experiment from configs/experiment.yaml, countries from regulations/<CODE>/region.yaml")
    probs = S.check(repo)
    check(not probs, "regulations: every country's files fit the template (fields, unique rule IDs, rule tables cite existing passages)",
          "; ".join(probs[:3]))
    if has_datasets:
        check(P.collection_region(repo, "culane") == "CN" and P.collection_region(repo, "bdd100k") == "US"
              and P.collection_dir(repo, "own_video") == repo / "datasets" / "US" / "own_video",
              "datasets: each label collection belongs to one country (datasets/<CODE>/dataset.yaml)")

    tmp = Path(tempfile.mkdtemp(prefix="project_selftest_"))
    try:
        r2 = tmp / "repo"
        for d in ("configs", "prompts", "regulations", "datasets"):
            shutil.copytree(repo / d, r2 / d, ignore=shutil.ignore_patterns("._*", ".DS_Store"))
        pdf = r2 / "regulations" / "inbox" / "test_standard.pdf"
        pdf.parent.mkdir(parents=True, exist_ok=True)
        pdf.write_bytes(tiny_pdf(PAGES))
        c2 = C.load(r2)
        quiet = lambda *a, **k: None  # noqa: E731
        rep = X.extract(r2, c2, pdf, "ZZ", "Testland", "left", "Test standard 2026", mock=True, log=quiet)
        draft = r2 / "regulations" / "ZZ" / "passages_draft.yaml"
        check(rep["pages"] == 3 and len(rep["pages_read"]) == 2 and draft.exists() and rep["passages"] >= 2,
              "extractor (mock): pages with marking words are found, a draft and region.yaml are written in the template",
              json.dumps(rep)[:300])
        used_before = "ZZ" in C.load(r2)["regions"]
        X.accept(r2, "ZZ", log=quiet)
        c3 = C.load(r2)
        from ..agent.prompts import prompt_parts
        pp = prompt_parts(c3, "B", "ZZ")
        check(not used_before and c3["regions"]["ZZ"]["driving_side"] == "left" and "Testland" in pp["user_text"]
              and "[ZZ-" in pp["instructions"] and "[US-" not in pp["instructions"],
              "accept: the draft becomes the country's passages; Test B of the new country cites them, the prompt names it")

        # real mode against a fake API server: the answer is checked against the page it quotes
        from .selftest import FakeApi
        api = FakeApi()
        api.answer = {"passages": [
            {"section": "4.1", "page": 2, "marking_type": "white solid lane line", "element": "boundary",
             "text_original": "A solid white lane line shall not be crossed.", "text_en": "A solid white lane line shall not be crossed.",
             "text_en_is_translation": False, "actions": {m: ("prohibited" if m == "cross_line" else "not_stated") for m in X.MOVES}},
            {"section": "4.9", "page": 2, "marking_type": "yellow line", "element": "boundary",
             "text_original": "Yellow lines may never be crossed by anyone.", "text_en": "Yellow lines may never be crossed by anyone.",
             "text_en_is_translation": False, "actions": {m: "not_stated" for m in X.MOVES}}]}
        old = os.environ.get("OPENAI_API_KEY")
        os.environ["OPENAI_API_KEY"] = "sk-test-not-a-real-key"
        try:
            c4 = C.load(r2)
            c4["api"]["base_url"] = api.url
            rep2 = X.extract(r2, c4, pdf, "YY", "Otherland", "right", "Other standard", mock=False, log=quiet)
            draft_yy = (r2 / "regulations" / "YY" / "passages_draft.yaml").read_text(encoding="utf-8")
            api.mode, hits0, kept = "no_credit", api.hits, None
            try:
                X.extract(r2, c4, pdf, "YY", "Otherland", "right", "Other standard", mock=False, log=quiet)
            except RuntimeError as e:
                kept = "kept" in str(e) and (r2 / "regulations" / "YY" / "passages_draft.yaml").read_text(encoding="utf-8") == draft_yy
            check(kept and api.hits - hits0 == 1,
                  "extractor: with no API credit left the request is not retried, and the earlier draft is kept",
                  f"kept={kept} requests={api.hits - hits0}")
            api.mode = "ok"
        finally:
            api.httpd.shutdown()
            if old is None:
                os.environ.pop("OPENAI_API_KEY", None)
            else:
                os.environ["OPENAI_API_KEY"] = old
        import yaml
        items = yaml.safe_load((r2 / "regulations" / "YY" / "passages_draft.yaml").read_text(encoding="utf-8"))
        body = api.requests[0] if api.requests else {}
        sent = json.dumps(body)
        check(rep2["requests"] == 1 and len(items) == 2 and items[0]["verified_quote"] and not items[1]["verified_quote"]
              and items[0]["actions_stated"] == {"cross_line": "prohibited"} and items[0]["rule_id"] == "YY-4.1"
              and body.get("text", {}).get("format", {}).get("strict") and "[page 2]" in sent and "Otherland" in sent,
              "extractor (real, fake server): one request with the fixed prompt and strict schema; a quote not on its page is flagged",
              f"{rep2} {items[:1]}")

        # evaluation of a saved run and the results index, on a copy of one run
        runs = sorted(P.runs_dir(repo).glob("*_lane*_US/results.jsonl")) + sorted(P.runs_dir(repo).glob("*_test*_US/results.jsonl"))
        if runs:
            rid = runs[-1].parent.name
            shutil.copytree(runs[-1].parent, P.runs_dir(r2) / rid)
            ev = E.evaluate_run(r2, rid)
            s = json.loads((P.runs_dir(r2) / rid / "scores.json").read_text(encoding="utf-8"))["summary"]
            cm = ev["actions"]["confusion"]
            total = sum(map(sum, cm["matrix"]))
            check(total == ev["actions"]["cells"] and ev["actions"]["unsafe"] == s.get("unsafe_errors")
                  and ev["actions"]["prohibited"]["f1"] is not None and "Confusion matrix" in E.to_markdown(ev),
                  "evaluate: confusion matrix of the action cells, precision/recall/F1 of prohibited; unsafe errors match the run's scores",
                  f"{total} {ev['actions']['cells']} {ev['actions']['unsafe']} {s.get('unsafe_errors')}")
            rows = G.build_index(r2)
            check(any(r["run_id"] == rid for r in rows) and (r2 / P.RESULTS_INDEX).exists(),
                  "results: results/index.csv lists the saved runs")
        else:
            log("SKIP evaluate: no saved run in results/runs/")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    from ..simulation.settings import load_settings
    st = load_settings(repo)
    stops_ok = all(r.get("map") and r.get("stops") for r in (st.get("routes") or {}).values())
    exps = st.get("experiments") or {}
    check(len(st.get("routes") or {}) >= 5 and stops_ok and set(exps) == {"A", "B", "C"}
          and all(v["region"] in cfg["regions"] for v in exps.values()),
          "simulation: configs/carla.yaml has the server, experiments A/B/C of known countries and 5 routes with stops")

    extensions(repo, cfg, check, log)
    multi_documents(repo, check)
    n_ok = sum(results)
    log(f"\n{n_ok}/{len(results)} checks passed")
    return n_ok == len(results)


def multi_documents(repo, check) -> None:
    """A country with several documents (--tag), narrower keywords for a long law, an RTF law, a state that copies a
    national model law (--same-as, region.yaml parent)."""
    from .. import config as C
    from ..agent import lane as L
    from ..regulations import extract as X
    quiet = lambda *a, **k: None  # noqa: E731
    tmp = Path(tempfile.mkdtemp(prefix="project_multi_"))
    try:
        r2 = tmp / "repo"
        for d in ("configs", "prompts", "regulations"):
            shutil.copytree(repo / d, r2 / d, ignore=shutil.ignore_patterns("._*", ".DS_Store", "inbox"))
        inbox = r2 / "regulations" / "inbox"
        inbox.mkdir(parents=True, exist_ok=True)
        rule = ("{n} Keeping to the left of a dividing line. A driver on a road with a dividing line must drive to the left of "
                "the dividing line. A driver must not cross a continuous dividing line unless permitted by rule {m}. "
                "The broken line of a lane line may be crossed when changing marked lanes.")
        model = "\n\n".join(rule.format(n=130 + i, m=160 + i) for i in range(12))  # two pseudo-pages
        state = model + "\n\n" + ("200 State rule about painted islands. A driver must not drive on a painted island marked "
                                   "by a continuous line, except a driver turning at a marked lane with a dividing line nearby. "
                                   "A painted island with a broken line may be crossed to enter a turning lane marked by arrows.")
        (inbox / "model.txt").write_text(model, encoding="utf-8")
        (inbox / "state.txt").write_text(state, encoding="utf-8")
        rtf = inbox / "law.rtf"
        rtf.write_text(r"{\rtf1\ansi{\fonttbl{\f0 Arial;}}{\*\generator Word;}\pard 132 Keeping to the left of a dividing "
                       r"line\par A driver must not cross a dividing line or a lane line\'2dmarking here.\par}", encoding="latin-1")
        c2 = C.load(r2)
        rt = X.read_pages(rtf)
        X.extract(r2, c2, inbox / "model.txt", "ZM", "Modelland", "left", "Model rules", mock=True, log=quiet)
        X.extract(r2, c2, rtf, "ZM", "Modelland", "left", "Model rules (RTF)", mock=True, log=quiet, tag="rtf",
                  keywords=["dividing line"], min_hits=1)
        X.extract(r2, c2, inbox / "model.txt", "ZM", "Modelland", "left", "Model rules", mock=True, log=quiet, tag="code")
        d = r2 / "regulations" / "ZM"
        docs = sorted(f.name for f in (d / X.DRAFTS).glob("*.yaml"))
        merged = X.merge_drafts(d)
        check("fonttbl" not in rt[0] and "lane line-marking" in rt[0] and docs == ["code.yaml", "model.yaml", "rtf.yaml"]
              and any(p["rule_id"].startswith("ZM-RTF-") for p in merged) and any(p["rule_id"].startswith("ZM-CODE-") for p in merged)
              and len({p["rule_id"] for p in merged}) == len(merged),
              "extractor: an RTF law is read; several documents of one country (--tag) keep their own drafts, merged with distinct IDs",
              f"{docs} {[p['rule_id'] for p in merged][:6]}")
        one = X.relevant_pages(["dividing line here", "lane and line and turn"], keywords=["dividing line"], min_hits=1)
        check(one == [1], "extractor: narrower keywords (--keywords, --min-hits) select fewer pages of a long law", str(one))
        rep = X.extract(r2, c2, inbox / "state.txt", "ZS", "Stateland", "left", "State rules", mock=True, log=quiet,
                        same_as=inbox / "model.txt")
        yaml_txt = (r2 / "regulations" / "ZS" / "region.yaml").read_text(encoding="utf-8")
        (r2 / "regulations" / "ZS" / "region.yaml").write_text(yaml_txt.replace("code: ZS", "code: ZS\nparent: ZM", 1), encoding="utf-8")
        c3 = C.load(r2, drafts=True)
        zs = c3["regions"]["ZS"]
        lp = L.lane_passages(L.lane_cfg(c3), "ZS")
        own = [p for p in lp if p.get("region") == "ZS"]
        check(rep["pages_same_as_reference"] and set(zs["rule_regions"]) == {"ZM", "ZS"} and zs["draft"]
              and 1 not in rep["pages_read"] and any(p.get("region") == "ZM" for p in lp) and any("painted island" in p["text_en"] for p in own),
              "extractor: a state's pages that copy the model law are not sent (--same-as); with parent: ZM the state "
              "gets the model law's passages plus its own changes", f"{rep['pages_same_as_reference']} {zs.get('rule_regions')} {len(lp)}")

        # fetch and extract-all: documents listed in region.yaml, served here by a local web server
        import http.server
        import threading
        from ..regulations import sources as SRC
        site = tmp / "site"
        site.mkdir()
        (site / "model.txt").write_text(model, encoding="utf-8")
        (site / "law.pdf").write_bytes(tiny_pdf(PAGES))
        (site / "error.html").write_text("<html>Access denied</html>", encoding="utf-8")
        (site / "index.html").write_text('<a href="law.pdf">current version</a>', encoding="utf-8")

        class Quiet(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *a, **k):
                super().__init__(*a, directory=str(site), **k)

            def log_message(self, *a):
                pass
        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Quiet)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{srv.server_address[1]}"
        try:
            zd = r2 / "regulations" / "ZD"
            zd.mkdir()
            (zd / "region.yaml").write_text(
                "code: ZD\nname: Docland\ndriving_side: left\nstatus: planned\nstandard: {title: Docs, language: en}\n"
                "passages: {marking: passages_lane.yaml, lane: [passages_lane.yaml]}\ndocuments:\n"
                f"  - {{tag: law, title: Law, urls: [{{url: '{base}/error.html', type: pdf}}], "
                f"find: {{page: '{base}/index.html', pattern: 'href=\"([^\"]+\\.pdf)\"', type: pdf}}, file: regulations/inbox/ZD/law}}\n"
                f"  - {{tag: code, title: Code, urls: [{{url: '{base}/model.txt', type: txt}}], file: regulations/inbox/ZD/code}}\n"
                f"  - {{tag: gone, title: Gone, urls: [{{url: '{base}/missing.pdf', type: pdf}}], file: regulations/inbox/ZD/gone}}\n",
                encoding="utf-8")
            res = {r["document"]: r for r in SRC.fetch(r2, ["ZD"], log=quiet)}
            again = {r["document"]: r["status"] for r in SRC.fetch(r2, ["ZD"], log=quiet)}
            check(res["ZD:law"]["status"] == "downloaded" and res["ZD:law"]["file"].endswith("law.pdf")
                  and res["ZD:code"]["status"] == "downloaded" and res["ZD:gone"]["status"] == "failed"
                  and again["ZD:law"] == "kept" and (r2 / "regulations" / "inbox" / SRC.LOG).exists(),
                  "regulations fetch: an error page is refused, the link on the index page is followed, a missing file is "
                  "reported; a file already there is kept", f"{res} {again}")
            c5 = C.load(r2)
            first = {r["document"]: r["status"] for r in SRC.extract_all(r2, c5, ["ZD"], mock=True, log=quiet)}
            second = {r["document"]: r["status"] for r in SRC.extract_all(r2, c5, ["ZD"], mock=True, log=quiet)}
            check(first == {"ZD:law": "extracted", "ZD:code": "extracted", "ZD:gone": "not downloaded"}
                  and second["ZD:law"] == "done before" and second["ZD:code"] == "done before"
                  and (zd / "drafts" / "law.yaml").exists() and (zd / "passages_draft.yaml").exists(),
                  "regulations extract-all: every downloaded document is extracted once; a second run skips what was "
                  "extracted from the same file", f"{first} {second}")
        finally:
            srv.shutdown()

        # data fetch: frames read out of a remote zip by byte ranges, and out of a downloaded tar
        import tarfile
        import zipfile
        from ..labeling import fetch as DF
        arch = tmp / "arch"
        arch.mkdir()
        with zipfile.ZipFile(arch / "images.zip", "w") as z:
            for i in range(30):
                z.writestr(f"images/train/seg{i % 5}/{i}.jpg", bytes([i]) * (5000 + i))
        with tarfile.open(arch / "cam.tar", "w") as t:
            for i in range(4):
                data = bytes([i]) * 300
                ti = tarfile.TarInfo(f"data/00012{i}/cam01/{i}.jpg")
                ti.size = len(data)
                t.addfile(ti, io.BytesIO(data))

        class Ranged(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *a, **k):
                super().__init__(*a, directory=str(arch), **k)

            def log_message(self, *a):
                pass

            def do_GET(self):
                f = arch / self.path.strip("/").split("?")[0]
                data = f.read_bytes()
                rng = self.headers.get("Range")
                if rng:
                    a, _, b = rng.split("=")[1].partition("-")
                    a, b = int(a), min(int(b) if b else len(data) - 1, len(data) - 1)
                    self.send_response(206)
                    self.send_header("Content-Range", f"bytes {a}-{b}/{len(data)}")
                    body = data[a:b + 1]
                else:
                    self.send_response(200)
                    body = data
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
        srv2 = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Ranged)
        threading.Thread(target=srv2.serve_forever, daemon=True).start()
        b2 = f"http://127.0.0.1:{srv2.server_address[1]}"
        try:
            out = tmp / "frames"
            want = ["train/seg1/6.jpg", "train/seg3/13.jpg", "train/seg9/99.jpg"]
            zr = DF.zip_members(f"{b2}/images.zip", want, out, log=quiet)
            DF.download(f"{b2}/cam.tar", out / "raw" / "cam.tar", log=quiet)
            tr = DF.tar_members(out / "raw" / "cam.tar", ["data/000122/cam01/2.jpg"], out)
            check(zr["matched"] == 2 and (out / "train/seg3/13.jpg").read_bytes() == bytes([13]) * 5013
                  and zr["requests"] < 10 and tr["written"] == 1 and (out / "data/000122/cam01/2.jpg").stat().st_size == 300,
                  "data fetch: the wanted frames are read out of a remote zip with a few byte-range requests, and out of "
                  "a downloaded tar", f"{zr} {tr}")
        finally:
            srv2.shutdown()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def extensions(repo, cfg, check, log) -> None:
    """Force of the passages, prompt lane_v2 with Tests D and R, composition level and rule sensitivity, text documents
    in the extractor, folder datasets of new countries, an API key in api.yaml."""
    import copy
    from .. import config as C
    from ..agent import lane as L
    from ..evaluation import difficulty as D
    from ..labeling import imagesets as IS
    from ..regulations import extract as X
    from ..regulations import norms as N

    en, zh, ja = N.NORM_WORDS["en"], N.NORM_WORDS["zh"], N.NORM_WORDS["ja"]
    cases = [("Edge lines shall be white.", en, "mandatory"), ("Vehicles may not cross the solid line.", en, "mandatory"),
             ("A solid white line should be used on approaches.", en, "recommended"), ("Dotted lines may be used.", en, "permissive"),
             ("The width of the line indicates emphasis.", en, "informative"), ("实线表示禁止跨越。", zh, "mandatory"),
             ("车行道边缘线不宜占车道宽度。", zh, "recommended"), ("虚线表示可跨越。", zh, "permissive"),
             ("可变导向车道线用以表示导向方向随需要可变的车道。", zh, "informative"), ("進路を変更してはならない。", ja, "mandatory")]
    got = [(t, N.propose(t, w)[0]) for t, w, _ in cases]
    check(all(g == want for (_, g), (_, _, want) in zip(got, cases)),
          "norms: shall/must/may not/应/禁止 mandatory, should/宜 recommended, may/可 permissive, else informative",
          str([x for x, (t, w, want) in zip(got, cases) if x[1] != want]))
    nm = N.norm_map(repo, "US")
    check(nm.get("US-3B.09-03") == "mandatory" and set(nm.values()) <= set(N.NORMS) and len(nm) == len(P.all_passages(repo, "US")),
          "norms: every US passage has a force (reviewed values in regulations/US/norms.yaml win)")

    c1 = C.load(repo)
    c2 = copy.deepcopy(c1)
    c2["lane"]["prompt_dir"] = "prompts/lane_v2"
    l1, l2 = L.lane_cfg(c1), L.lane_cfg(c2)
    a1, a2, b2 = L.lane_prompt_parts(l1, "A", "CN"), L.lane_prompt_parts(l2, "A", "CN"), L.lane_prompt_parts(l2, "B", "CN")
    d2 = L.lane_prompt_parts(l2, "D", "CN")
    check(a1["hashes"]["instructions"] == a2["hashes"]["instructions"] and a1["hashes"]["user_text"] == a2["hashes"]["user_text"]
          and "] [mandatory] " in b2["instructions"] and "[mandatory]" not in L.lane_prompt_parts(l1, "B", "CN")["instructions"]
          and d2["instructions"] == a2["instructions"] and "China" not in d2["user_text"] and "China" in a2["user_text"],
          "lane_v2: Test A unchanged (same requests as lane_v1); Test B prints the force of each passage; Test D drops the country")
    full = L.lane_passages(l2, "US")
    ans = {"left_boundary": {"color": "yellow", "pattern": "solid", "role": "edge_line", "curb": "no"},
           "right_boundary": {"color": "white", "pattern": "dashed", "role": "lane_line", "curb": "no"},
           "lane_markings": [{"marking": "arrow:left"}]}
    chosen = L.select_passages(full, ans)
    ids = {p["rule_id"] for p in chosen}
    check(0 < len(chosen) < len(full) and "US-3B.09-03" in ids and not any("two-way left-turn" in (p.get("marking_type") or "") for p in chosen),
          "Test R: the passages about the reported elements are kept, the others (here two-way left-turn lanes) left out",
          f"{len(chosen)}/{len(full)}")

    table, schema = D._tables(repo)
    lab = {"left_color": "white", "left_pattern": "solid", "left_curb": "no", "left_role": "lane_line", "left_evidence": "full",
           "right_color": "white", "right_pattern": "dashed", "right_curb": "no", "right_role": "lane_line", "right_evidence": "full",
           "markings": "", "markings_evidence": "full"}
    s_cn = D.sensitivity(table, schema, "CN", lab)
    lab3 = dict(lab, left_color="yellow", left_pattern="solid_dashed", left_near_line="solid", left_role="center_line")
    lab_arrow = dict(lab, right_pattern="solid", markings="arrow:straight")
    check(s_cn["sensitive"] and "change_left" in s_cn["actions"] and D.level(table, schema, "CN", lab)[0] in ("L1", "L2")
          and D.level(table, schema, "CN", lab3)[0] == "L3" and D.level(table, schema, "CN", lab_arrow)[0] == "L3",
          "difficulty: a Chinese white solid lane line is rule-sensitive; a solid-and-broken pair and a lane that commits the car are L3",
          f"{s_cn} {D.level(table, schema, 'CN', lab3)} {D.level(table, schema, 'CN', lab_arrow)}")

    tmp = Path(tempfile.mkdtemp(prefix="project_ext_"))
    try:
        doc = tmp / "law.html"
        doc.write_text("<html><body><h1>Rules</h1><p>Rule 127. A broken white line marks the centre of the road. You may cross it "
                       "when it is safe.</p><p>Rule 128. Double white lines where the line nearest you is solid: you MUST NOT cross "
                       "or straddle it.</p><p>Rule 129. Lane arrows show the lane to use for a turn.</p></body></html>", encoding="utf-8")
        pages = X.read_pages(doc)
        items = X.to_template([{"section": "128", "page": 1, "marking_type": "double white line", "element": "boundary",
                                "text_original": "you MUST NOT cross or straddle it", "text_en": "you MUST NOT cross or straddle it",
                                "text_en_is_translation": False, "norm": "recommended", "actions": {m: "not_stated" for m in X.MOVES}}],
                              "ZZ", "Test code", pages, "en")
        check(len(pages) >= 1 and "MUST NOT" in pages[0] and "<p>" not in pages[0] and items[0]["verified_quote"]
              and items[0]["norm"] == "recommended" and items[0]["norm_check"].startswith("words say mandatory"),
              "extractor: an HTML law is read as text pages; a force that disagrees with the standard's words is flagged")

        img_root = tmp / "lingoqa_src" / "train" / "seg1"
        img_root.mkdir(parents=True)
        import cv2
        import numpy as np
        for k in range(3):
            cv2.imwrite(str(img_root / f"{k}.jpg"), np.zeros((20, 30, 3), np.uint8))
        from ..imageio import imread, imwrite
        uni = tmp / "数据集" / "图.jpg"
        uni.parent.mkdir()
        wrote = imwrite(uni, np.full((8, 9, 3), 200, np.uint8))
        back = imread(uni)
        check(wrote and back is not None and back.shape == (8, 9, 3) and imread(tmp / "missing.jpg") is None,
              "images: a path with Chinese characters is written and read (cv2 alone cannot on Windows); a missing file gives None")
        dc = IS.dataset_cfg(repo, "lingoqa")
        rows = IS._folder_index(tmp / "lingoqa_src", dict(dc, candidates=""), repo, log=lambda *a: None)
        check(dc["region"] == "UK" and dc["reader"] == "folder" and len(rows) == 3 and {r["clip_id"] for r in rows} == {"train/seg1"}
              and rows[0]["width"] == 30 and P.collection_region(repo, "lingoqa") == "UK",
              "datasets: a new country's collection (LingoQA, UK) is read as a folder of images, one clip per folder")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    old = os.environ.pop("ZZ_TEST_KEY", None)
    try:
        m = C._take_key({"api_key_env": "ZZ_TEST_KEY", "api_key": "sk-test-0123456789abcdefghijklmn", "name": "x"})
        check("api_key" not in m and os.environ.get("ZZ_TEST_KEY", "").startswith("sk-test")
              and "sk-test" not in json.dumps(C.public(C.load(repo))),
              "settings: an API key written into api.yaml is used from the environment and never kept in the settings")
    finally:
        os.environ.pop("ZZ_TEST_KEY", None)
        if old is not None:
            os.environ["ZZ_TEST_KEY"] = old

    # lane try: a photo without a label, a draft country, a mirrored frame
    import cv2
    import numpy as np
    drafts = C.load(repo, drafts=True)
    code = next((c for c, r in drafts["regions"].items() if r.get("draft") and r["driving_side"] == "left"), "US")
    try:
        L.lane_passages(L.lane_cfg(drafts), code)
    except C.ConfigError:
        code = "US"  # the draft has no passages yet
    tmp = Path(tempfile.mkdtemp(prefix="rd_try_"))
    out = None
    try:
        img = np.zeros((200, 320, 3), np.uint8)
        img[:, :40] = (0, 200, 255)  # a yellow band on the left
        cv2.imwrite(str(tmp / "frame.png"), img)
        cfg_t = copy.deepcopy(drafts)
        cfg_t["mock"] = True
        out, recs = L.try_images(cfg_t, code, [tmp / "frame.png"], ["A", "B"], True, mirror=True)
        sent = cv2.imread(str(out / "images" / "frame_mirrored.png"))
        man = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
        summ = (out / "summary.md").read_text(encoding="utf-8")
        check(len(recs) == 2 and not any(r["error"] for r in recs) and sent is not None and sent[100, 300, 2] == 255
              and sent[100, 10, 2] == 0 and man["mirrored"] and man["draft_passages"] == bool(drafts["regions"][code].get("draft"))
              and "| A |" in summ and "| B |" in summ and (code == "US" or code not in C.load(repo)["regions"]),
              f"lane try: a photo without a label is asked under {code} (a draft country only with --draft), flipped for left-hand "
              "traffic, and nothing is scored",
              f"code={code} recs={len(recs)} manifest={man}")
        check(C._prompt_language("ja") == "en" and C._prompt_language("zh") == "zh",
              "settings: a standard in Japanese or another language goes into the prompt through its English text")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        if out is not None:
            shutil.rmtree(out, ignore_errors=True)

    # the countries simulation: decisions in the photo's frame, the mirror for left-hand traffic, the video's text layout
    from ..simulation import countries as CT
    from ..simulation import countries_video as CV
    us = CT.decide("turn_right", {"turn_right": "prohibited", "change_right": "allowed"})
    cn = CT.decide("turn_right", {"turn_right": "prohibited", "change_right": "prohibited", "turn_left": "allowed"})
    uk_intent = CT.flip("turn_right", True)
    uk = CT.decide(uk_intent, {"turn_left": "prohibited", "change_left": "allowed"})
    check(us["shift"] == "right" and us["choice"] == "turn_right" and cn["shift"] is None and cn["choice"] == "turn_left"
          and uk_intent == "turn_left" and CT.to_car(uk, True)["shift"] == "right" and CT.to_car(uk, True)["choice"] == "turn_right",
          "countries: the car turns or changes lanes only where the answer allows it; a mirrored country's left and right are "
          "flipped back before driving")
    lines = CV.wrap("A long English sentence that must wrap " * 6 + "中文条文也要能换行" * 20, CV.F["code"], 600)
    check(all(CV.F["code"].getlength(x) <= 600 for x in lines) and len(lines) > 3
          and CV.added_lines("a\nb", "a\nb\nc\nd") == "c\nd" and CV.compact_json({"enum": ["x", "y"]}).startswith("{"),
          "countries video: prompts and traces wrap to the page (English and Chinese); Test B's additions to the prompt are found")
