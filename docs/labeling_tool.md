# Labeling tool: `video_tool`

Labels for the own dash-cam videos and for the dataset images (BDD100K, CULane), with two independent labels per image and adjudication. The project overview and the reproduction steps are in the [README](../README.md).

## Own dash-cam videos (`video_tool/`)

A tool that turns recorded drives into labeled frames, with the same label schema as the rest of the project (section 6.1 of the Milestone 3 document), and with **two independent labels per frame**: helpers label offline, disagreements are adjudicated by the owner. Each video is one **trip**; several files of one drive share a drive id, which is the split unit (like a CULane clip). Nothing is dumped as frames: the video is read directly, and only the frames you keep are saved.

```bash
pip install -r requirements.txt          # adds opencv-python-headless
python -m video_tool selftest            # optional: runs everything on a synthetic night video
python -m video_tool ingest <folder>/DJI_*.MP4 --time-of-day night --weather clear
python -m video_tool scan                # hides stops and crawling; flags dark or blurry moments
python -m video_tool label <trip>        # local app: ① screen ② target box + own label ③ adjudicate ④ share with helpers
python -m video_tool package --to Alice,Bob,Chen   # same as the ④ tab: one offline zip per helper
python -m video_tool import <folder with results_*.json>   # same as dropping the files into the ④ tab
python -m video_tool export              # checks, blurred report copies, combined files, agreement
```

Several windows can be open at once (for example own videos, BDD100K, CULane and the model demo): each one is a small web server on this computer (`127.0.0.1`) and takes the next free port, starting at 8765 for labeling and 8770 for the demo; the terminal prints the address. Only one window per data folder: a second start on the same folder opens the window that is already running, because two windows on one folder would overwrite each other's labels.

| Step | What happens |
|---|---|
| `ingest` | Copies the video to `data/raw/own_video/<trip>/` (or `--no-copy`), records SHA-256, size, resolution and fps, registers the trip in `labels/own_video/`. Several files at once become one drive group. `--annotators-required 1` for frames only you label. |
| `scan` | Samples the video twice a second. Stops of 3 s or more (red lights, traffic) and crawling are hidden, not deleted. Records brightness, sharpness and hints for painted and yellow lines. `--start` / `--end` cut out your own street. |
| `label` | ① Screen: step or play through what is left, fine-tune by single frames, **K** keeps a frame (1280×720, like BDD100K); burned-in date / speed / GPS overlays can be blacked out once per trip. ② For each kept frame draw the **target box** (the marking the model will be asked about). Label it yourself, or "save box only" and leave it to helpers. ③ Compare independent labels side by side and decide conflicts (pick one, edit, or exclude; the reason is recorded). ④ Share with helpers: make the packages, follow their status, drop the returned results files to import them. Every page has a 中文 / English switch, the rule passages are shown as original plus translation, and a detailed illustrated guide (Chinese and English, printable) is built in. `--recheck` adds a blind self re-check (R2). |
| `package` | Assigns every frame that still needs labels to helpers so it gets two labels from different people (yours count). Each helper gets a zip with `index.html`, `data.js`, `images/` and a README. The page works offline in any browser, with no account and no region limits: Chinese / English switch, bilingual rule passages (US passages translated in `config/rule_translations_zh.json`, used only on the labeling pages), a full guide with examples, a privacy note, practice items with your answers, privacy boxes, autosave, and "Export results". Helpers appear only as codes (ann01, ann02, ...); the code-to-name list is kept in `DATA_DIR/annotators.json`. |
| `import` | Reads the returned `results_*.json`, stores each helper's labels in `<trip>.annotations.csv`, and recomputes the final labels: if the labels agree on every scored field the label is final; any difference or "unsure" makes it a conflict for ③. Prints agreement and writes `agreement.csv`. |
| `export` | Validates final labels, writes copies with all privacy boxes pixelated to `data/report_figures/own_video/<trip>/` (reports only; model inputs are not blurred), and writes `labels/own_video/all_labels.csv` (answer key: `label_status == done`), `all_annotations.csv`, `summary.csv` and `agreement.csv`. |
| `rebuild` | Re-creates every kept frame from the video (checks the SHA-256 first). |

* Scored fields for agreement: marking type, arrow type, position, broken-line side, visibility, whether the visible part decides the behavior, and the six actions. Rule IDs and privacy boxes are not compared: the final label takes the union (rule IDs from the chosen answer after adjudication).
* Files: `labels/own_video/` holds the trip metadata, final labels, annotations, packages list and agreement; videos, frames, packages and annotator names are kept in `DATA_DIR`.
* Rule table: `config/action_rules.json` prefills actions and rule IDs from the marking type, only to keep labels consistent; it is never used to score model answers. Where the passages are silent, one default was fixed before any model is run: a line allows an action unless a passage prohibits it (*discouraged* is not *prohibited*), and an arrow allows the movements it shows and prohibits the others. Two US cells rest on a convention rather than on a passage's own words and are listed under `contested`: a single solid white lane line (crossing allowed, discouraged) and a U-turn from a lane with a left-type arrow (allowed). The single solid yellow left edge line (crossing prohibited) is backed by MUTCD 3B.09 ¶03, and the two-way left-turn lane (entering to wait and turning left allowed) by 3B.05 ¶01. Road edge lines and bike lane lines are not used as targets. An empty cell means no convention yet. `config/label_schema.json` holds the allowed values.
* Scoring model answers against these labels: the main score uses only uncontested cells; contested cells are reported separately. Errors are split into unsafe (model allows what the label prohibits) and over-cautious (model prohibits or leaves undetermined what the label allows). When a model disagrees with a label, the case is reviewed blind (the reviewer sees the image, the passages and two unnamed answers) and recorded as model error, label error or ambiguous. Label errors are corrected for every system and logged, and scores are reported before and after the review.
* Licenses: CULane frames must not be redistributed, so they are not for helper packages. BDD100K packages carry the copyright notice.

## Public dataset images (`video_tool images`)

BDD100K (US) and CULane (China) are labeled with the same app, guide, packages and adjudication as the own videos. Their own labels say where lines are, not what they allow, so they are only used to find candidates and to suggest a target box; every scored field is labeled by hand. Each dataset has its own workspace, separate from the own-video folder:

```bash
python -m video_tool --data "<root>/bdd100k" images init bdd100k   # once: candidate index of the 10,000 val images
python -m video_tool --data "<root>/culane"  images init culane    # once: candidate index of the 34,680 test frames
python -m video_tool --data "<root>/bdd100k" label                 # ① pick images  ② label  ③ decide  ④ share
python -m video_tool --data "<root>/bdd100k" export
python -m video_tool combine "<root>/UF" "<root>/bdd100k" "<root>/culane"
python -m video_tool hash-sources        # SHA-256 and MD5 of every downloaded archive and rule PDF
```

| Where | What |
|---|---|
| `labels/bdd100k/`, `labels/culane/` | `<set>.set.json` (dataset folder, region, license, quotas), `<set>.labels.csv` (final labels), `<set>.annotations.csv`, `packages.csv` |
| `<workspace>/index/<set>/candidates.csv` | every image with its pool (dev / test by the hash rule in 6.5), time of day, hints and suggested boxes |
| `<workspace>/selected/<set>/` | copies of the picked images; the dataset itself is never changed |
| `<workspace>/packages/`, `returned/`, `report_figures/`, `annotators.json` | as for own videos, per workspace |
| `labels/labels.csv`, `labels/split_v<N>.csv` | every final label of every workspace, with `collection` and `image_path` (relative to the folder holding the workspaces), for the model runs; a new version after every recorded split change (`labels/split_changes.csv`), older versions are kept |
| `labels/split_check_v<N>.json` | the separation check of that version: clips on both sides of the split, development/test pairs within 4 bits (dHash) across all workspaces, prompt examples not taken from development images, and the recorded moves |
| `labels/coverage_v<N>.csv` | usable final labels per region, split and marking type (arrows by direction), with the number of distinct clips and how the label was reached (agreed by two annotators, adjudicated, single) |

* ① Pick images: filter by pool, hint (BDD100K lane type and style, crosswalk, no lane label; CULane scene category) and time of day, and press 1–5 to pick an image as solid / dashed / yellow centre line / arrow / degraded. A quota table shows picked against the Milestone 3 targets (6 per type and region for development, 30 for test, plus 30 degraded test images). Picking never overwrites earlier work; more images can be added at any time.
* Suggested boxes: BDD100K labels both edges of each painted line, so the edges are merged into one box per marking; for CULane the two boundaries of our lane are suggested. Clicking a dashed suggestion in ② makes it the target box.
* Split rules (6.5): the pool comes from the hash of the clip (BDD100K: the image; CULane: driver folder and clip). At most 2 test images per CULane clip. `export` flags any development image that looks like a test image (dHash within 4 bits).
* CULane packages carry a no-sharing, delete-afterwards notice in Chinese and English (the CULane terms forbid redistribution).
