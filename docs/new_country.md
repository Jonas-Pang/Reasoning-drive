# Adding a country

The steps that took the United Kingdom and India from nothing to a pilot run (2026-11-16). Every step uses the same tools
as China and the US; no code changes. Paid API calls are marked **(API)**; everything else is free.

| Step | Command | What comes out |
|---|---|---|
| 1. Country folder | copy `regulations/_template/` to `regulations/<CODE>/`, fill `region.yaml` (name, `driving_side: left` or `right`, the documents and their URLs) | the country is listed by `python main.py regulations list` (status planned) |
| 2. Rule text | `python main.py regulations fetch <CODE>`, then **(API)** `python main.py regulations extract-all <CODE> --real` (about $0.10–0.25 per country) | `regulations/<CODE>/passages_draft.yaml`: passages with section, page, quote check and force (mandatory, recommended, permissive, informative) |
| 3. Read and accept | read the draft against the source (delete what is not a rule for drivers, fix sections), then `python main.py regulations accept <CODE>` | `passages_lane.yaml`, `norms.yaml`; status *in use*: Test B can use the country |
| 4. Rule table | write `regulations/<CODE>/lane_action_rules.json` from `regulations/_template/` (rows: line attributes -> change allowed or prohibited, with the passage IDs; markings -> movements) | the labeling tool suggests the actions; `python main.py regulations check <CODE>` checks every rule ID |
| 5. Test C partner | `configs/experiment.yaml`, `lane.control_region`: which country's passages the control gets (UK <-> IN: both keep left) | Test C stays fixed when more countries are added |
| 6. Images | `datasets/<CODE>/dataset.yaml` names the collection; `python main.py data fetch <CODE> --root <DATASETS_ROOT>` (or download yourself where the dataset needs registration) | images under `DATASETS_ROOT/<collection>` |
| 7. Labeling workspace | `python main.py label --data <DATASETS_ROOT>/<collection>_ws images init <collection> --source <DATASETS_ROOT>/<collection>`; set the quota and `lane_annotators_required` in `datasets/<CODE>/<collection>/<collection>.set.json` | the candidate index, dev/test by clip hash |
| 8. Same labeling window | add one line to `configs/labeling_regions.json` (region, workspace, set, a free port); `scripts/label_all.bat` | the country appears in the switch of the one labeling window |
| 9. Pick and label | pick frames into the quota cells, label the lane, save as done (model drafts allowed: they are the owner's drafts until reviewed; their origin goes to `results/claude_logs/provenance_labels.csv`) | `<collection>.lanes.csv` with final labels |
| 10. Licence | add the collection to `data.send_to_api` in `configs/experiment.yaml` only after reading its terms | images may be sent to the model |
| 11. Development run | **(API)** `python scripts/claude_lane_eval.py --split dev --regions <CODE> --tests A,B` | runs in `results/runs/`, `results/lane_report_dev.md` |
| 12. Freeze and test | `python main.py lane freeze --add --note "..."` adds the new country to the frozen protocol without touching the frozen ones; then **(API)** `--split test` | the country's test runs, each once |

Rule sources (owner's requirement, 2026-11-16):

* **Official texts only, about lane markings.** Every passage must come from the government's own publication of the law or
  of the national marking standard: the legislation site or official gazette (legislation.gov.uk, the Gazette of India,
  the Federal Register), the government's own guidance (GOV.UK Highway Code), or the national standard named by law
  (GB 5768, MUTCD). Not Wikipedia, driving-school sites, commercial law databases or summaries, and not another
  benchmark's rule handbook (GeoDrive-Bench compiles its handbooks from Wikipedia and earlier studies).
* Prefer the **latest consolidated version** and record in `region.yaml` the URL, the version shown on the page and the
  date it was read. Check the publisher's list of amendments before a freeze; a passage whose text changed is re-read.
* Keep to what decides a lane action: longitudinal lines (lane, centre, warning, edge, double lines), lane arrows and
  words, hatching and chevrons, reserved lanes, stop and give-way lines, box junctions. Parking and loading markings are
  not lane rules.
* Where the official text gives no answer (e.g. whether a single solid white lane line may be crossed in the UK), the rule
  table row stays **contested** with a note; it is never filled from an unofficial source.

Images (owner's requirement, 2026-11-16): every picked frame must show at least one painted lane boundary of my lane, and
my car must be inside its lane (not on or across a line, not changing lanes). Frames with no lane markings, or where the
car straddles a line, are removed, also from the "degraded" group (degraded = worn or partly hidden paint, not no paint).

Notes:

* A country added after the freeze does not stop the frozen countries' test runs: `lane protocol` lists it under
  "not in the protocol yet", and its own test images are refused until `lane freeze --add`.
* Left-hand traffic needs nothing special in the prompt (it names the driving side; left and right are from my car).
  The rule table decides what a line means: the same white solid line between lanes is prohibited to cross in China and
  India, only discouraged (allowed) in the US, and not covered by the UK passages of this pack (allowed, contested).
* Markings outside the schema (UK zig-zag lines, red route lines as a pattern) would need new values in
  `configs/schemas/lane_schema.json`, which is part of the frozen protocol: add them only before a new freeze.

## The UK and India pilot (2026-11-16)

| Country | Rules | Images | Pilot labels |
|---|---|---|---|
| UK (keeps left) | The Highway Code (rules 127–143, Road markings), TSRGD 2016 Schedule 9 Part 6 and Schedule 11 Part 4; 115 passages | LingoQA (Wayve, London), 488 GeoDrive-Bench candidate frames in 231 clips | 5 dev + 11 test, drafted by the model, every one reviewed by the owner |
| India (keeps left) | Motor Vehicles (Driving) Regulations, 2017; 31 passages (IRC:35, the marking code, is a priced publication and not used) | IDD Multimodal (IIIT Hyderabad), 561 candidate frames in 3 drives (d1 dev; d0, d2 test) | 4 dev + 9 test, the same way |

LingoQA has many scenes of the same junctions in different clips, so the clip hash alone does not keep dev and test apart;
the pilot picks avoid places that appear on both sides. Many London and Indian frames have few lane markings (kerbs,
yellow waiting lines, medians). The first pilot picks kept some of them; the owner rejected that on 2026-11-16 (see
"Images" above), and the picks without a lane line or with the car on a line are being replaced.
UK rules extended on 2026-11-17 with TSRGD 2016 Schedule 11 Part 4 (the legal meaning of lane, centre, warning and edge
lines, hatching and lane arrows; 21 passages, copied from legislation.gov.uk without the API).
