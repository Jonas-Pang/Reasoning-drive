# Prompts

Every request is built from the fixed templates of one folder; only the photo and the rule block change.

```
instructions (developer message)
  role.txt                 who the model is and what it judges
  procedure.txt            the steps, with the slot {RULES_STEP}:  rules_step_A.txt (no rules) | rules_step_B.txt (the listed rules)
  fields.txt               how to fill in each answer field, with the slot {CITATION}:  citation_A.txt | citation_B.txt
  rule block (Test B, C)   rules_header.txt with the country's name and standard, then the passages of regulations/<CODE>/:
                             ## <part of the lane>
                             [<rule_id>] <source>, section <section>, page <page>
                             <text>
user message
  user.txt                 the country's name and driving side, and the photo
answer
  strict JSON schema       built from configs/schemas/ (the model cannot add fields or values)
```

The single-marking folders (`v1` to `v4`) have the same parts under the names `step2_A.txt`, `step2_B.txt` and `answer_fields.txt`. Test A and Test B differ only in the two slots and the rule block; Test C fills the rule block with another country's passages. A new country changes only what goes into the slots (`regulations/<CODE>/`), never the templates. `python main.py prompt --test B` and `python main.py lane prompt --test B --region CN` print the prompt as it is sent, and every run records the hashes of its instructions, user message and schema.

| Folder | Task |
|---|---|
| `v1` … `v4` | one marked lane marking; v4 is selected (the README of each folder says what changed) |
| `lane_v1` | the lane the car drives in: both boundaries, the markings in it, seven actions |
| `lane_v2` | lane_v1 with the force of each passage, and Test D |
| `lane_v3` | lane_v2, and going straight without an arrow is allowed (see its README) |
| `regulation_extraction` | reading a new standard's PDF into passages (`python main.py regulations extract`) |
