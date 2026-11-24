"""Independent annotations, the final label, and agreement between annotators.

Every person's label is kept as its own row in <trip>.annotations.csv (never overwritten by someone
else). The FINAL label in <trip>.labels.csv is derived from them:

  * fewer finished annotations than required        -> waiting
  * all finished annotations agree on every scored field, nobody unsure
                                                     -> done (final_source = agreed, or single)
  * any disagreement, or someone marked it unsure    -> conflict, decided by the owner
  * decided by the owner                             -> done or excluded (final_source = adjudicated)

Scored fields: marking type, arrow type, position, broken-line side, visibility, whether the visible
part decides the behavior, and the six actions. Accepted rule IDs and privacy boxes are not
compared: the final label takes the union of everyone's.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict

from .core import (ANNOTATION_COLUMNS, COMPARE_FIELDS, FINAL_FIELDS, OWNER, LabelStore, Paths, ToolError, Trip,
                   derive_evidence, list_trip_ids, read_json, today, utc_now, write_csv, write_json)


class AnnotationStore:
    """All annotations of one trip, keyed by (image_id, annotator)."""

    def __init__(self, path):
        from .core import read_csv
        self.path = path
        self.rows: dict[tuple, dict] = {}
        for r in read_csv(path):
            self.rows[(r["image_id"], r["annotator"])] = {c: r.get(c, "") or "" for c in ANNOTATION_COLUMNS}

    def save(self) -> None:
        rows = sorted(self.rows.values(), key=lambda r: (r["image_id"], r["annotator"]))
        write_csv(self.path, rows, ANNOTATION_COLUMNS)

    def get(self, image_id: str, annotator: str) -> dict | None:
        return self.rows.get((image_id, annotator))

    def for_image(self, image_id: str) -> list[dict]:
        rows = [r for (iid, _), r in self.rows.items() if iid == image_id]
        return sorted(rows, key=lambda r: (r.get("saved_utc", ""), r["annotator"]))

    def put(self, row: dict) -> None:
        clean = {c: ("" if row.get(c) is None else str(row.get(c))) for c in ANNOTATION_COLUMNS}
        clean["expected_evidence"] = derive_evidence(clean["visibility"], clean["behavior_decidable"])
        self.rows[(clean["image_id"], clean["annotator"])] = clean

    def delete_image(self, image_id: str) -> None:
        for key in [k for k in self.rows if k[0] == image_id]:
            del self.rows[key]

    def all(self) -> list[dict]:
        return list(self.rows.values())


LABEL_FIELDS = ["marking_type", "arrow_type", "position", "dashed_side", "visibility", "behavior_decidable"]


def fields_to_row(row: dict, fields: dict, schema: dict) -> dict:
    """Label fields as the pages send them -> annotation / final-label columns."""
    from .core import ACTIONS
    for k in LABEL_FIELDS:
        if k in fields:
            row[k] = str(fields[k] or "").strip()
    if row.get("marking_type") != "arrow":
        row["arrow_type"] = ""
    if row.get("marking_type") not in schema.get("needs_dashed_side", []):
        row["dashed_side"] = ""
    if row.get("visibility") != "V1":
        row["behavior_decidable"] = ""
    row["expected_evidence"] = derive_evidence(row.get("visibility", ""), row.get("behavior_decidable", ""))
    acts = fields.get("actions") or {}
    for a in ACTIONS:
        if a in acts:
            row["act_" + a] = acts[a] or ""
    if "accepted_rule_ids" in fields:
        row["accepted_rule_ids"] = ";".join(str(i) for i in (fields["accepted_rule_ids"] or []) if i)
    if "privacy_boxes" in fields:
        boxes = [[int(round(float(v))) for v in b] for b in (fields["privacy_boxes"] or []) if isinstance(b, (list, tuple)) and len(b) == 4]
        row["privacy_boxes"] = json.dumps(boxes)
    return row


def has_box(row: dict) -> bool:
    return all(str(row.get(k, "")).strip() not in ("", "None") for k in ("bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2"))


def _boxes(text: str) -> list:
    try:
        v = json.loads(text or "[]")
        return v if isinstance(v, list) else []
    except json.JSONDecodeError:
        return []


def union_privacy(*texts: str) -> str:
    seen, out = set(), []
    for t in texts:
        for b in _boxes(t):
            key = tuple(int(round(float(x))) for x in b)
            if key not in seen:
                seen.add(key)
                out.append(list(key))
    return json.dumps(out)


def differences(a: dict, b: dict) -> list[str]:
    return [f for f in COMPARE_FIELDS if (a.get(f) or "") != (b.get(f) or "")]


def required_for(trip_meta: dict) -> int:
    return int(trip_meta.get("annotators_required", 2))


def merge_item(item: dict, anns: list[dict], required: int) -> dict:
    """Recompute the final label of one item from its annotations. Owner decisions are kept."""
    item = dict(item)
    item["privacy_boxes"] = union_privacy(item.get("privacy_boxes", ""), *[a.get("privacy_boxes", "") for a in anns])
    if item.get("final_source") == "adjudicated":
        return item
    done = [a for a in anns if a.get("status") == "done"]
    item["annotators"] = ";".join(a["annotator"] for a in done)
    for f in FINAL_FIELDS:
        item[f] = ""
    item["final_source"] = ""
    if item.get("label_status") == "excluded":
        return item
    if not has_box(item):
        item["label_status"] = "kept"
        return item
    if len(done) < required:
        item["label_status"] = "waiting"
        return item
    unsure = any(a.get("unsure") == "1" for a in done)
    agree = all(not differences(done[0], a) for a in done[1:])
    if unsure or not agree:
        item["label_status"] = "conflict"
        return item
    first = done[0]
    for f in FINAL_FIELDS:
        item[f] = first.get(f, "")
    ids = []
    for a in done:
        for i in (a.get("accepted_rule_ids") or "").split(";"):
            if i and i not in ids:
                ids.append(i)
    item["accepted_rule_ids"] = ";".join(ids)
    item["label_status"] = "done"
    item["final_source"] = "agreed" if len(done) > 1 else "single"
    return item


def merge_trip(paths: Paths, trip: Trip, labels: LabelStore | None = None, anns: AnnotationStore | None = None,
               save: bool = True) -> Counter:
    labels = labels or LabelStore(paths.labels_csv(trip.id))
    anns = anns or AnnotationStore(paths.annotations_csv(trip.id))
    req = required_for(trip.meta)
    counts = Counter()
    for iid, item in list(labels.rows.items()):
        new = merge_item(item, anns.for_image(iid), req)
        labels.put(new)
        counts[new["label_status"]] += 1
    if save:
        labels.save()
    return counts


def adjudicate(labels: LabelStore, anns: AnnotationStore, image_id: str, choice: str, fields: dict | None,
               note: str, decided_by: str, required: int) -> dict:
    """choice: an annotator code, 'edit' (fields given), 'exclude', or 'reopen'."""
    item = labels.get(image_id)
    if item is None:
        raise ToolError(f"Unknown image {image_id}")
    item = dict(item)
    if choice == "reopen":
        item["final_source"] = ""
        item["adjudication_note"] = ""
        if item.get("label_status") == "excluded":
            item["label_status"] = "waiting"
        item = merge_item(item, anns.for_image(image_id), required)
        labels.put(item)
        return item
    if choice == "exclude":
        item["label_status"] = "excluded"
    else:
        if choice == "edit":
            src = fields or {}
        else:
            src = anns.get(image_id, choice)
            if src is None:
                raise ToolError(f"No annotation from {choice} for {image_id}")
        for f in FINAL_FIELDS:
            item[f] = src.get(f, "") or ""
        item["expected_evidence"] = derive_evidence(item.get("visibility", ""), item.get("behavior_decidable", ""))
        item["label_status"] = "done"
    item["final_source"] = "adjudicated"
    item["adjudication_note"] = f"{choice}: {(note or '').strip()}".strip()
    item["annotators"] = ";".join(a["annotator"] for a in anns.for_image(image_id) if a.get("status") == "done")
    item["labeler"] = decided_by
    item["label_date"] = today()
    item["privacy_boxes"] = union_privacy(item.get("privacy_boxes", ""), *[a.get("privacy_boxes", "") for a in anns.for_image(image_id)])
    labels.put(item)
    return item


def migrate_owner_labels(paths: Paths, trip: Trip, owner: str = OWNER) -> int:
    """Labels made before annotations existed become the owner's annotations (nothing is lost)."""
    if paths.annotations_csv(trip.id).exists():
        return 0
    labels = LabelStore(paths.labels_csv(trip.id))
    anns = AnnotationStore(paths.annotations_csv(trip.id))
    n = 0
    for r in labels.all():
        if r.get("marking_type") and r.get("final_source", "") == "":
            row = {c: r.get(c, "") for c in ANNOTATION_COLUMNS if c in r}
            row.update({"image_id": r["image_id"], "annotator": owner, "source": "local", "package_id": "",
                        "status": "done" if r.get("label_status") == "done" else "draft", "unsure": "0",
                        "comment": "", "saved_utc": utc_now()})
            anns.put(row)
            n += 1
    anns.save()
    if n:
        merge_trip(paths, trip, labels, anns)
    return n


# ------------------------------------------------------------------ annotators (private registry)

def load_annotators(paths: Paths) -> dict:
    p = paths.annotators_json
    return read_json(p) if p.exists() else {}


def annotator_code(paths: Paths, name: str) -> str:
    """Pseudonymous code for a helper (ann01, ann02 ...). The name stays on the data drive only."""
    reg = load_annotators(paths)
    for code, info in reg.items():
        if info.get("name", "").strip().lower() == name.strip().lower():
            return code
    n = 1
    while f"ann{n:02d}" in reg:
        n += 1
    code = f"ann{n:02d}"
    reg[code] = {"name": name.strip(), "added_utc": utc_now()}
    write_json(paths.annotators_json, reg)
    return code


# ------------------------------------------------------------------ agreement

def _kappa(pairs: list[tuple[str, str]]) -> float | None:
    """Fleiss' kappa for two ratings per item (raters may differ between items)."""
    if not pairs:
        return None
    po = sum(a == b for a, b in pairs) / len(pairs)
    cats = Counter(v for p in pairs for v in p)
    total = 2 * len(pairs)
    pe = sum((c / total) ** 2 for c in cats.values())
    if pe >= 1.0:
        return None
    return (po - pe) / (1 - pe)


def agreement(paths: Paths, trip_ids: list[str] | None = None) -> dict:
    pairs: dict[str, list] = defaultdict(list)
    all_agree, by_type = [], defaultdict(lambda: [0, 0])
    unsure = 0
    for tid in trip_ids or list_trip_ids(paths):
        anns = AnnotationStore(paths.annotations_csv(tid))
        by_image = defaultdict(list)
        for a in anns.all():
            if a.get("status") == "done":
                by_image[a["image_id"]].append(a)
        for iid, rows in by_image.items():
            if len(rows) < 2:
                continue
            rows = sorted(rows, key=lambda r: (r.get("saved_utc", ""), r["annotator"]))[:2]
            if any(r.get("unsure") == "1" for r in rows):
                unsure += 1
            for f in COMPARE_FIELDS:
                pairs[f].append((rows[0].get(f, ""), rows[1].get(f, "")))
            ok = not differences(rows[0], rows[1])
            all_agree.append(ok)
            t = by_type[rows[0].get("marking_type") or "?"]
            t[0] += ok
            t[1] += 1
    fields = []
    for f in COMPARE_FIELDS:
        ps = pairs.get(f, [])
        k = _kappa(ps)
        fields.append({"field": f, "items": len(ps),
                       "percent_agreement": round(sum(a == b for a, b in ps) / len(ps), 3) if ps else "",
                       "fleiss_kappa": round(k, 3) if k is not None else ""})
    return {
        "items": len(all_agree),
        "all_fields_agree": round(sum(all_agree) / len(all_agree), 3) if all_agree else None,
        "unsure_pairs": unsure,
        "fields": fields,
        "by_marking_type": {t: {"agree": a, "items": n} for t, (a, n) in sorted(by_type.items())},
    }


def write_agreement(paths: Paths, log=print) -> dict:
    ag = agreement(paths)
    write_csv(paths.labels_dir / "agreement.csv", ag["fields"], ["field", "items", "percent_agreement", "fleiss_kappa"])
    if ag["items"]:
        log(f"  Agreement between two independent annotators on {ag['items']} images: "
            f"all scored fields equal on {ag['all_fields_agree']:.0%}.")
        weak = [f for f in ag["fields"] if f["items"] and f["percent_agreement"] < 0.9]
        for f in ag["fields"]:
            if f["items"]:
                log(f"    {f['field']:32s} {f['percent_agreement']:.0%} agree   kappa {f['fleiss_kappa'] if f['fleiss_kappa'] != '' else '—'}")
        if weak:
            log("  Below 90% agreement, the guide for these fields needs to be clearer: " + ", ".join(f["field"] for f in weak))
        log("  (Kappa is unstable when nearly all labels share one value; read it together with the percent agreement.)")
    return ag
