# Lane prompt lane_v3

lane_v2 with three changes, in `fields.txt`: **go_straight with no arrow in my lane is "allowed"** (it was "not_applicable").
Nothing restricts carrying on straight along my lane, and a boundary that prohibits or discourages a lane change does not
govern going straight. An arrow in my lane still decides the four movements, and the turns and the U-turn stay
"not_applicable" without an arrow or a prohibited-movement marking.

The labels follow the same convention (owner's decision, 2026-11-15; `lane_prefill` in reasoning_drive/labeling/lanes.py and
`scripts/claude_migrate_straight.py` for the labels made before). Because no passage says it in words, the cell is marked
contested and scored separately, so the main action score is comparable with lane_v2 runs.

**stop_first** (new action value, configs/schemas/lane_schema.json): a STOP word (`text:stop`) or the China stop-and-yield
line with 停 (`line:stop_yield`) in my lane turns every movement the lane allows into "stop_first" (allowed only after a full
stop), so going straight is not simply allowed there. Answering "allowed" where the label says stop_first counts as an
unsafe error.

**Special lanes** (owner's decision, 2026-11-15): my car is an ordinary car and the reserved time cannot be seen, so changing
into a bus, HOV, tidal or similar special lane across a `special_lane_line` boundary is "prohibited"; when my own lane is
the special lane (text:bus, text:hov or symbol:hov_diamond in it), leaving it follows the line type. Contested (scored
separately), since it rests on the assumed reserved time.
