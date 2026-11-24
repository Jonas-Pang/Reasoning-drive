# Lane prompt lane_v2

lane_v1 with two additions; Test A is unchanged, so its answers are the same requests as with lane_v1.

* The force of every passage. `passage_line.txt` prints each passage as `[rule_id] [force] source, section, page`, the force
  taken from `regulations/<CODE>/norms.yaml` (mandatory, recommended, permissive, informative). `rules_header.txt` explains
  the four words, and `rules_step_B.txt` says how to use them: a mandatory passage or a definition of what the marking means
  decides a prohibition; a recommended or informative passage that only discourages an action does not prohibit it.
  This is aimed at the error of prompt v3: the general passage "a solid line discourages or prohibits crossing" read
  against the specific rule for edge lines.
* Test D. `user_D.txt` is the user message without the country: the model infers it from the photo (and says which
  country it thinks it is in `scene`). Everything else is Test A.

Test R (only the passages about the elements of a saved Test A answer) uses the files of Test B.
