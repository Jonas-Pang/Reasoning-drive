# Prompt lane_v1 (lane-level task)

One request per image. The model interprets the whole ego lane: the lane count and the position of my lane, both
boundaries (colour, pattern, the line nearer my lane for a solid-and-broken pair, curb, role) and the guidance
markings in the lane (arrows, prohibited-movement markings, words, symbols, waiting areas, grids, lines across the
lane). It then gives the seven lane actions and one or two sentences of advice.

Hallucination control inside the one response:

1. observation before interpretation: every boundary and marking has an "observation" sentence that is written
   before its attributes, and an evidence level;
2. a cross-check of the observations against each other before any rule is applied (lane position against
   boundary roles, colour against role, arrows against words and areas, attributes reported without being seen);
3. one rule per element (Test B: a passage ID; the rule written for the kind of marking decides over a general one);
4. a reason per action, then a reflection on the decision before the actions are written.

Test A and Test B share every part except the rules step (`rules_step_A.txt` / `rules_step_B.txt`), the citation
slot and the rule block, which lists the region's passages from the files in `regions.<R>.lane_rules` grouped by
element. The answer schema is built in `reasoning_drive/agent/lane.py` from `configs/schemas/lane_schema.json`.
