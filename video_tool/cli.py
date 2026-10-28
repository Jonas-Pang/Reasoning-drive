"""Command line: python -m video_tool <command> ...

  ingest   register a new video (one trip): copy into data/raw, hash, record metadata
  scan     analyse the video once: hide stops and crawling, flag dark or blurry moments
  label    open the labeling app in the browser (screen the video, keep frames, label them)
  export   check labels, make blurred copies for reports, write summary and combined label files
  rebuild  re-create the kept frames from the video
  package  make offline labeling packages (zip) for helpers; each frame gets 2 independent labels
  import   read the results files helpers send back; agreed labels become final, others go to ③
  list     show the registered trips (or the image set of a dataset workspace)
  images   dataset images: `images init bdd100k|culane` sets up a dataset workspace (then use label, package, ...)
  resplit  move a whole own-video drive to dev (or test), with the reason logged in labels/split_changes.csv
  hash-sources  SHA-256 / MD5 of every downloaded archive, mirror copy and rule PDF in data_manifest.csv
  combine  all final labels of every workspace in labels/labels.csv and labels/split_v<N>.csv (for the model runs)
  selftest run the whole pipeline on a small synthetic night video and two tiny synthetic datasets

Every command works on one data folder (--data). Own videos and each dataset have their own folder, e.g.
  --data "<root>/UF"   --data "<root>/bdd100k"   --data "<root>/culane"
"""
from __future__ import annotations

import argparse
import sys

from .core import Paths, ToolError, Trip, default_labeler, list_trip_ids, read_csv
from .ingest import TIME_OF_DAY, WEATHER


def _seconds(text: str | None) -> float | None:
    if text in (None, ""):
        return None
    parts = [float(p) for p in str(text).split(":")]
    v = 0.0
    for p in parts:
        v = v * 60 + p
    return v


def _pick_trip(paths: Paths, trip: str | None) -> str:
    if trip:
        return trip
    ids = list_trip_ids(paths)
    if len(ids) == 1:
        return ids[0]
    raise ToolError("Say which trip: " + (", ".join(ids) if ids else "no trips registered yet (run ingest first)"))


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="python -m video_tool", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", help="repository folder (default: the one this tool is in)")
    ap.add_argument("--data", help="data folder (default: DATA_DIR from .env, else <repo>/data)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("ingest", help="register a new video (or several files of one drive)")
    p.add_argument("videos", nargs="+", help="video file(s); several files of one drive become one split group")
    p.add_argument("--trip", help="trip name (default: <place>_<date>_<time-of-day>_NN)")
    p.add_argument("--drive", help="add the file(s) to an existing drive group")
    p.add_argument("--annotators-required", type=int, default=2,
                   help="independent labels needed per frame before it is final (default 2; 1 = only you)")
    p.add_argument("--date", help="recording date YYYY-MM-DD (default: from the file name, else the file date)")
    p.add_argument("--time-of-day", default="night", choices=TIME_OF_DAY)
    p.add_argument("--weather", default="clear", choices=WEATHER)
    p.add_argument("--road", default="", help="e.g. city_street, highway, residential (free text)")
    p.add_argument("--place", default="FL", help="short place tag used in the dataset name (default FL)")
    p.add_argument("--region", default="US", choices=["US", "CN"], help="which rule pack applies")
    p.add_argument("--split", default="test", choices=["test", "dev", "hash"],
                   help="test (default), dev, or hash = the clip rule from section 6.5")
    p.add_argument("--out-width", type=int, default=1280, help="width of saved frames (default 1280 = BDD100K; 0 keeps the original)")
    p.add_argument("--no-copy", action="store_true", help="leave the video where it is instead of copying it into data/raw")
    p.add_argument("--notes", default="", help="short note (the repository is public: no addresses)")

    p = sub.add_parser("scan", help="analyse a video once")
    p.add_argument("trips", nargs="*", help="trip names (default: every trip not scanned yet)")
    p.add_argument("--sample-fps", type=float, default=2.0, help="samples per second (default 2)")
    p.add_argument("--start", help="skip the start, e.g. 2:00 (useful to cut out your street)")
    p.add_argument("--end", help="stop here, e.g. 25:30")
    p.add_argument("--motion-threshold", type=float, help="below this the car counts as standing still (default: automatic)")
    p.add_argument("--min-stop", type=float, default=3.0, help="a stop must last this many seconds to be hidden (default 3)")

    p = sub.add_parser("label", help="open the labeling app")
    p.add_argument("trip", nargs="?")
    p.add_argument("--port", type=int, default=8765)
    p.add_argument("--no-browser", action="store_true")
    p.add_argument("--labeler", default=None, help="your name or initials (default: LABELER in .env, else your user name)")
    p.add_argument("--recheck", action="store_true", help="blind re-check of a sample of finished labels (risk R2)")
    p.add_argument("--new-sample", action="store_true", help="with --recheck: draw a new re-check sample")

    p = sub.add_parser("export", help="check labels, blurred report copies, summary")
    p.add_argument("trips", nargs="*", help="trip names (default: all)")

    p = sub.add_parser("rebuild", help="re-create the kept frames from the video")
    p.add_argument("trip", nargs="?")
    p.add_argument("--skip-hash", action="store_true", help="do not re-check the video SHA-256")

    p = sub.add_parser("package", help="make offline labeling packages for helpers")
    p.add_argument("--to", required=True, help="helper names, comma separated, e.g. --to Alice,Bob,Chen")
    p.add_argument("trips", nargs="*", help="trip names (default: all)")
    p.add_argument("--practice", type=int, default=6, help="practice items per helper, taken from your finished labels (default 6)")
    p.add_argument("--max", type=int, help="at most this many frames per helper in this batch")

    p = sub.add_parser("import", help="read helpers' results files")
    p.add_argument("files", nargs="+", help="results_*.json files, or a folder that holds them")

    sub.add_parser("list", help="show the registered trips")

    p = sub.add_parser("images", help="dataset images (BDD100K, CULane)")
    isub = p.add_subparsers(dest="icmd", required=True)
    pi = isub.add_parser("init", help="set up the --data folder as the workspace of one dataset and build its candidate index")
    pi.add_argument("dataset", choices=["bdd100k", "culane"])
    pi.add_argument("--source", help="the unpacked dataset (default: <repo>/data/extracted/bdd100k/mirror/val or <repo>/data/extracted/culane)")
    pi.add_argument("--rebuild-index", action="store_true", help="read the dataset labels again (labels you made are kept)")

    p = sub.add_parser("resplit", help="move a whole own-video drive to dev (or test); logged in labels/split_changes.csv")
    p.add_argument("trip", help="any trip of the drive; every file of the drive moves together")
    p.add_argument("split", choices=["dev", "test"])
    p.add_argument("--reason", required=True, help="why; written to labels/split_changes.csv")

    p = sub.add_parser("hash-sources", help="add SHA-256 / MD5 of every downloaded source file to data_manifest.csv")
    p.add_argument("--raw", help="folder with the downloads (default: DATA_DIR/raw from .env)")
    p.add_argument("--rehash", action="store_true", help="hash again files already in the manifest with the same size")
    p.add_argument("--budget", type=float, help="start no new file after this many seconds (run again to continue)")

    p = sub.add_parser("combine", help="all final labels of every workspace together, for the model runs")
    p.add_argument("folders", nargs="+", help="the data folders, e.g. <root>/UF <root>/bdd100k <root>/culane")
    sub.add_parser("selftest", help="run everything on a synthetic night video")

    a = ap.parse_args(argv)
    try:
        if a.cmd == "selftest":
            from .selftest import run
            sys.exit(0 if run() else 1)
        if a.cmd == "images":
            from .imagesets import init_workspace
            if not a.data:
                raise ToolError('Give the dataset workspace with --data, e.g. --data "<root>/bdd100k".')
            init_workspace(a.repo, a.data, a.dataset, a.source, rebuild_index=a.rebuild_index)
            return
        if a.cmd == "hash-sources":
            from pathlib import Path
            from .core import DEFAULT_REPO
            from .hash_sources import hash_sources
            hash_sources(Path(a.repo or DEFAULT_REPO), Path(a.raw) if a.raw else None, rehash=a.rehash, budget_s=a.budget)
            return
        if a.cmd == "combine":
            from .imagesets import combine
            combine(a.repo, a.folders)
            return
        paths = Paths.discover(a.repo, a.data)
        if a.cmd == "resplit":
            from .resplit import resplit
            resplit(paths, a.trip, a.split, a.reason)
            return
        if paths.is_images and a.cmd in ("ingest", "scan"):
            raise ToolError(f"{paths.data} is the {paths.collection} workspace (dataset images). Use the own-video folder for videos.")
        if a.cmd == "ingest":
            from .ingest import ingest_many
            ingest_many(paths, a.videos, trip_id=a.trip, drive_id=a.drive, recorded_date=a.date, time_of_day=a.time_of_day,
                        weather=a.weather, road_type=a.road, place=a.place, region=a.region, split=a.split,
                        out_width=a.out_width, copy=not a.no_copy, notes=a.notes,
                        annotators_required=a.annotators_required)
        elif a.cmd == "scan":
            from .scan import scan_trip
            ids = a.trips or [t for t in list_trip_ids(paths) if not Trip(paths, t).meta.get("scan")]
            if not ids:
                raise ToolError("Every trip is scanned already. Name a trip to scan it again.")
            for tid in ids:
                trip = Trip(paths, tid)
                scan_trip(paths, trip, sample_fps=a.sample_fps, start_s=_seconds(a.start), end_s=_seconds(a.end),
                          motion_threshold=a.motion_threshold, min_stop_s=a.min_stop)
                print(f"Next: python -m video_tool label {trip.id}")
        elif a.cmd == "label":
            from .server import serve
            trip = Trip(paths, _pick_trip(paths, a.trip))
            serve(paths, trip, a.labeler or default_labeler(), port=a.port, open_browser=not a.no_browser,
                  recheck=a.recheck, new_sample=a.new_sample)
        elif a.cmd == "export":
            from .export import export_all
            export_all(paths, a.trips or None)
        elif a.cmd == "rebuild":
            from .export import rebuild_trip
            rebuild_trip(paths, _pick_trip(paths, a.trip), skip_hash=a.skip_hash)
        elif a.cmd == "package":
            from .packages import build_packages
            build_packages(paths, a.to.split(","), a.trips or None, practice=a.practice, max_per_person=a.max)
        elif a.cmd == "import":
            from .packages import import_results
            import_results(paths, a.files)
        elif a.cmd == "list" and paths.is_images:
            from .annotations import AnnotationStore
            from .imagesets import quota_table
            from .core import LabelStore
            for tid in list_trip_ids(paths):
                t = Trip(paths, tid)
                store = LabelStore(paths.labels_csv(tid))
                rows = store.all()
                st = {k: sum(r["label_status"] == k for r in rows) for k in ("kept", "waiting", "conflict", "done", "excluded")}
                print(f"{tid}  ({t.meta['dataset']}, {t.meta['region']})  {t.meta.get('index', {}).get('images', 0)} images in the index")
                print(f"  picked {len(rows)}  no box {st['kept']}  waiting {st['waiting']}  conflict {st['conflict']}  "
                      f"done {st['done']}  excluded {st['excluded']}")
                q = quota_table(t, store, AnnotationStore(paths.annotations_csv(tid)))
                for r in q["rows"]:
                    print(f"  {r['group']:9s} dev {r['dev_have']:3d}/{r['dev_target']:<3d} test {r['test_have']:3d}/{r['test_target']}")
                print(f"  labels: {paths.labels_dir}\n  images: {paths.frames_dir(tid)}")
        elif a.cmd == "list":
            ids = list_trip_ids(paths)
            if not ids:
                print("No trips yet. Register one with: python -m video_tool ingest <video>")
            for tid in ids:
                t = Trip(paths, tid)
                rows = read_csv(paths.labels_csv(tid))
                st = {k: sum(r["label_status"] == k for r in rows) for k in ("kept", "waiting", "conflict", "done", "excluded")}
                sc = t.meta.get("scan", {})
                dur = (t.meta["video"].get("duration_s") or 0) / 60
                print(f"{tid:32s} {t.meta['time_of_day']:9s} {dur:5.1f} min  scan {'yes' if sc else 'no ':3s}  kept {len(rows):4d}  "
                      f"no box {st['kept']:3d}  waiting {st['waiting']:3d}  conflict {st['conflict']:3d}  done {st['done']:3d}")
    except ToolError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(130)
