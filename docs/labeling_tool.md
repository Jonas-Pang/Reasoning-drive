# Labeling tool: `python main.py label`

Labels for the own dash-cam videos and for the dataset images (BDD100K, CULane), with two independent labels per image and adjudication. The project overview and the reproduction steps are in the [README](../README.md).

## Own dash-cam videos (`reasoning_drive/labeling/`)

A tool that turns recorded drives into labeled frames, with the same label schema as the rest of the project (section 6.1 of the Milestone 3 document), and with **two independent labels per frame**: helpers label offline, disagreements are adjudicated by the owner. Each video is one **trip**; several files of one drive share a drive id, which is the split unit (like a CULane clip). Nothing is dumped as frames: the video is read directly, and only the frames you keep are saved.

```bash
pip install -r requirements.txt          # adds opencv-python-headless
python main.py label selftest            # optional: runs everything on a synthetic night video
python main.py label ingest <folder>/DJI_*.MP4 --time-of-day night --weather clear
python main.py label scan                # hides stops and crawling; flags dark or blurry moments
python main.py label label <trip>        # local app: ① screen ② lane labels ③ disagreements ④ share with helpers
python main.py label lanes-package --to Alice,Bob,Chen   # same as the ④ tab: one offline lane package per helper
python main.py label lanes-import <folder with results_*.json>   # same as dropping the files into the ④ tab
python main.py label export              # checks, blurred report copies, combined files, agreement
```

`package` and `import` make and read the packages of the earlier single-marking task (Milestones 3 and 4); the ④ tab still reads returned files of both kinds.

Several windows can be open at once (for example own videos, BDD100K, CULane and the model demo): each one is a small web server on this computer (`127.0.0.1`) and takes the next free port, starting at 8765 for labeling and 8770 for the demo; the terminal prints the address. Only one window per data folder: a second start on the same folder opens the window that is already running, because two windows on one folder would overwrite each other's labels.

| Step | What happens |
|---|---|
| `ingest` | Copies the video to `data/raw/own_video/<trip>/` (or `--no-copy`), records SHA-256, size, resolution and fps, registers the trip in `datasets/US/own_video/`. Several files at once become one drive group. `--annotators-required 1` for frames only you label. |
| `scan` | Samples the video twice a second. Stops of 3 s or more (red lights, traffic) and crawling are hidden, not deleted. Records brightness, sharpness and hints for painted and yellow lines. `--start` / `--end` cut out your own street. |
| `label` | ① Screen: step or play through what is left, fine-tune by single frames, **K** keeps a frame (1280×720, like BDD100K), **L** opens it in ②; burned-in date / speed / GPS overlays can be blacked out once per trip. ② Lane labels: the lane page (see *Lane mode* below) for every kept frame; label my lane yourself, or leave it to helpers. ③ Disagreements: the same page on the images whose independent lane labels differ; take one annotation or exclude the image (the reason is recorded). ④ Share with helpers: make the lane packages, follow their status, drop the returned results files to import them. Every page has a 中文 / English switch and shows the rule passages as original plus translation; the lane page has its own guide. `--recheck` adds tab ⑤, a blind self re-check (R2) of earlier single-marking labels with the single-marking form and its illustrated guide. |
| `package` | Single-marking task. Assigns every frame that still needs labels to helpers so it gets two labels from different people (yours count). Each helper gets a zip with `index.html`, `data.js`, `images/` and a README. The page works offline in any browser, with no account and no region limits: Chinese / English switch, bilingual rule passages (US passages translated in `configs/rule_translations_zh.json`, used only on the labeling pages), a full guide with examples, a privacy note, practice items with your answers, privacy boxes, autosave, and "Export results". Helpers appear only as codes (ann01, ann02, ...); the code-to-name list is kept in `DATA_DIR/annotators.json`. |
| `import` | Single-marking task. Reads the returned `results_*.json`, stores each helper's labels in `<trip>.annotations.csv`, and recomputes the final labels: if the labels agree on every scored field the label is final; any difference or "unsure" makes it a conflict for ③. Prints agreement and writes `agreement.csv`. |
| `export` | Validates final labels, writes copies with all privacy boxes pixelated to `data/report_figures/own_video/<trip>/` (reports only; model inputs are not blurred), and writes `datasets/US/own_video/all_labels.csv` (answer key: `label_status == done`), `all_annotations.csv`, `summary.csv` and `agreement.csv`. |
| `rebuild` | Re-creates every kept frame from the video (checks the SHA-256 first). |

* Scored fields for agreement: marking type, arrow type, position, broken-line side, visibility, whether the visible part decides the behavior, and the six actions. Rule IDs and privacy boxes are not compared: the final label takes the union (rule IDs from the chosen answer after adjudication).
* Files: `datasets/US/own_video/` holds the trip metadata, final labels, annotations, packages list and agreement; videos, frames, packages and annotator names are kept in `DATA_DIR`.
* Rule table: `regulations/<CODE>/action_rules.json` prefills actions and rule IDs from the marking type, only to keep labels consistent; it is never used to score model answers. Where the passages are silent, one default was fixed before any model is run: a line allows an action unless a passage prohibits it (*discouraged* is not *prohibited*), and an arrow allows the movements it shows and prohibits the others. Two US cells rest on a convention rather than on a passage's own words and are listed under `contested`: a single solid white lane line (crossing allowed, discouraged) and a U-turn from a lane with a left-type arrow (allowed). The single solid yellow left edge line (crossing prohibited) is backed by MUTCD 3B.09 ¶03, and the two-way left-turn lane (entering to wait and turning left allowed) by 3B.05 ¶01. Road edge lines and bike lane lines are not used as targets. An empty cell means no convention yet. `configs/schemas/label_schema.json` holds the allowed values.
* Scoring model answers against these labels: the main score uses only uncontested cells; contested cells are reported separately. Errors are split into unsafe (model allows what the label prohibits) and over-cautious (model prohibits or leaves undetermined what the label allows). When a model disagrees with a label, the case is reviewed blind (the reviewer sees the image, the passages and two unnamed answers) and recorded as model error, label error or ambiguous. Label errors are corrected for every system and logged, and scores are reported before and after the review.
* Licenses: CULane frames must not be redistributed, so they are not for helper packages. BDD100K packages carry the copyright notice.

## Public dataset images (`label images`)

BDD100K (US) and CULane (China) are labeled with the same app, guide, packages and adjudication as the own videos. Their own labels say where lines are, not what they allow, so they are only used to find candidates and to suggest the boundaries of my lane; every scored field is labeled by hand. Each dataset has its own workspace, separate from the own-video folder:

```bash
python main.py label --data "<root>/bdd100k" images init bdd100k   # once: candidate index of the 10,000 val images
python main.py label --data "<root>/culane"  images init culane    # once: candidate index of the 34,680 test frames
python main.py label --data "<root>/bdd100k" label                 # ① pick images  ② lane labels  ③ disagreements  ④ share
python main.py label --data "<root>/bdd100k" export
python main.py label combine "<root>/UF" "<root>/bdd100k" "<root>/culane"
python main.py label hash-sources        # SHA-256 and MD5 of every downloaded archive and rule PDF
```

| Where | What |
|---|---|
| `datasets/bdd100k/`, `datasets/culane/` | `<set>.set.json` (dataset folder, region, license, quotas), `<set>.labels.csv` (final labels), `<set>.annotations.csv`, `packages.csv` |
| `<workspace>/index/<set>/candidates.csv` | every image with its pool (dev / test by the hash rule in 6.5), time of day, hints and suggested boxes |
| `<workspace>/selected/<set>/` | copies of the picked images; the dataset itself is never changed |
| `<workspace>/packages/`, `returned/`, `report_figures/`, `annotators.json` | as for own videos, per workspace |
| `datasets/splits/labels.csv`, `datasets/splits/split_v<N>.csv` | every final label of every workspace, with `collection` and `image_path` (relative to the folder holding the workspaces), for the model runs; a new version after every recorded split change (`datasets/splits/split_changes.csv`), older versions are kept |
| `datasets/splits/split_check_v<N>.json` | the separation check of that version: clips on both sides of the split, development/test pairs within 4 bits (dHash) across all workspaces, prompt examples not taken from development images, and the recorded moves |
| `datasets/splits/coverage_v<N>.csv` | usable final labels per region, split and marking type (arrows by direction), with the number of distinct clips and how the label was reached (agreed by two annotators, adjudicated, single) |

* ① Pick images: filter by pool, hint (BDD100K lane type and style, crosswalk, no lane label; CULane scene category) and time of day. The large image shows my lane as a light area between the two boundaries that the dataset's own lane labels suggest (BDD100K: colour, pattern and curb, listed beside the image; CULane: position only). The lines themselves are not drawn so the paint stays visible; a magnifier follows the mouse and **H** hides the area. **Enter** picks the image into the group the suggestion gives; **1–5** choose the group: a solid line (including solid + dashed and double solid) / no solid line (dashed or none) / a yellow line / an arrow or word in the lane / hard to see. When several fit, the first of arrow or word, yellow line, solid line, no solid line is chosen. **L** opens the picked image in ②, where the same suggestion prefills both boundaries. A quota table shows picked against the Milestone 3 targets (6 per group and region for development, 30 for test, plus 30 hard-to-see test images). Picking never overwrites earlier work; more images can be added at any time.
* For the earlier single-marking task the same dataset labels gave one suggested box per marking (BDD100K labels both edges of a painted line, merged into one box).
* Split rules (6.5): the pool comes from the hash of the clip (BDD100K: the image; CULane: driver folder and clip). At most 2 test images per CULane clip. `export` flags any development image that looks like a test image (dHash within 4 bits).
* CULane packages carry a no-sharing, delete-afterwards notice in Chinese and English (the CULane terms forbid redistribution).

## Lane mode (Milestone 5)

The lane task labels my whole lane on the images kept in a workspace (own frames, BDD100K and CULane picks), so the split stays the same. In the main tool (`label`) tabs ② and ③ show this page and tab ④ makes and imports the lane packages; the owner can also remove an image from the set there. The commands below do the same without the main tool:

```bash
python main.py label --data "<root>/bdd100k" lanes                          # local page, you label as the owner
python main.py label --data "<root>/bdd100k" lanes-package --to ann01 --split dev
python main.py label --data "<root>/bdd100k" lanes-import results_L*.json
python main.py label --data "<root>/bdd100k" lanes-status                   # counts per status, agreement per field
```

The page (English or 中文) has four parts and a save bar that stays at the bottom: where my lane is (lane count and position by click, evidence); both boundaries side by side (the line as painted, with colour and pattern in one click and every other colour and pattern behind "other", the line on my side for a solid-and-dashed pair, curb, role, evidence); the markings in my lane (the usual arrows, ONLY, left-turn waiting area, stop line and crosswalk, with every other marking one click away, evidence); the seven actions and the rule IDs with the passage text and its translation. A new label starts from curb no, evidence clear and, for dataset images, the dataset's own boundary suggestion. The role follows from the line and the lane position, and the actions and rule IDs follow `regulations/<CODE>/lane_action_rules.json` as the label changes; a value the annotator changes stays, and "back to the rule table" undoes the changes. The photo stays in view with a magnifier (**H** hides drawn lines); boundary lines can be drawn with a few clicks (kept for checking, never sent to the model). A label is saved as done only when every field is filled in and the lane count was clicked (or "can't tell"), or when it is marked unsure.

Each image needs two independent lane labels (the set's `lane_annotators_required`, a number or one per split such as `{"dev": 1, "test": 2}`, else `annotators_required`). Agreeing labels become the final lane label (`<set>.lanes.csv`); a disagreement or an unsure label opens the "Disagreements" view, where the owner sees the differing fields and takes one annotation or excludes the image. Helpers get a zip with `index.html`, `data.js` and the images; the page works offline, keeps the work in the browser and exports `results_<package>.json`. CULane packages carry the no-sharing notice. Agreement is written to `datasets/<CODE>/<collection>/lane_agreement.csv` (percent and Fleiss' kappa per field).

Guidance for annotators: judge colour and pattern from the paint you can see, never from where the line is; read an arrow from its head; a boundary decides only the lane change on its side, arrows only the four movements; `not_applicable` means nothing in view governs the action (without an arrow this holds for the turns and the U-turn; going straight is then `allowed`, a project convention scored as contested, because nothing restricts carrying on along the lane and a boundary does not govern it), `not_determined` means the feature that decides it is hidden; `stop_first` means allowed only after a full stop (a STOP word or the 停 stop-and-yield line in the lane turns every allowed movement into it); keep the suggested rule IDs unless a passage says otherwise; mark unsure rather than guess.
