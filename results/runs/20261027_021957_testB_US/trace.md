# Reasoning trace of run 20261027_021957_testB_US

```
fl_20261017_night_01_f0001950 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a straight-ahead head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this arrow permits going straight and
                      prohibits left turns, right turns, and U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 215 output (hidden reasoning 0) | 3.65 s
```

```
fl_20261017_night_01_f0001950 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a straight-ahead head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this arrow permits going straight and
                      prohibits left turns, right turns, and U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 215 output (hidden reasoning 0) | 3.52 s
```

```
fl_20261017_night_01_f0001950 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a straight-ahead head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this arrow allows proceeding straight
                      and prohibits left turns, right turns, and U-turns from this lane.  (written after the
                      actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 218 output (hidden reasoning 0) | 3.66 s
```

```
fl_20261017_night_01_f0001970 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow has a single clearly visible head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The white arrow points only straight ahead. Under US-3B.23-01, lane-use arrows indicate
                      mandatory or permissible movements, so this arrow permits going straight and excludes
                      left turns, right turns, and U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 211 output (hidden reasoning 0) | 4.0 s
```

```
fl_20261017_night_01_f0001970 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow has a single head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a straight-ahead head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible lane movements, so this arrow allows going straight
                      and prohibits left turns, right turns, and U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 213 output (hidden reasoning 0) | 3.67 s
```

```
fl_20261017_night_01_f0001970 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow has a single head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a straight-ahead head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this arrow allows proceeding straight
                      and prohibits left turns, right turns, and U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 212 output (hidden reasoning 0) | 3.76 s
```

```
fl_20261017_night_01_f0003105 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Broad white transverse bars separated by dark pavement gaps form a crosswalk, with white
                      lines along its edges.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     none
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The broad white transverse bars identify a crosswalk rather than a longitudinal line or
                      lane-use arrow. No supplied passage covers crosswalks, and this marking governs none of
                      the six specified actions.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3960 input + 205 output (hidden reasoning 0) | 4.35 s
```

```
fl_20261017_night_01_f0003105 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Broad white transverse stripes separated by dark pavement gaps form a crosswalk across
                      the rectangle.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     none
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible broad white transverse stripes identify a crosswalk, not a longitudinal line
                      or lane-use arrow. No supplied passage covers crosswalks, and this marking governs none
                      of the six listed actions.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3960 input + 202 output (hidden reasoning 0) | 3.96 s
```

```
fl_20261017_night_01_f0003105 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Broad white transverse stripes separated by dark pavement gaps form a crosswalk across
                      the rectangle.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     none
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The broad white stripes and intervening gaps identify a crosswalk, not a longitudinal
                      line or lane-use arrow. No supplied passage covers crosswalks, and under the supplied
                      definitions this marking governs none of the six actions.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3960 input + 207 output (hidden reasoning 0) | 4.78 s
```

```
fl_20261017_night_01_f0006510 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid yellow line forms an unbroken diagonal stretch inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible single solid yellow line marks the left roadway edge; US-3B.09-03 specifies
                      this marking to indicate driving or passing restrictions to its left, so crossing it
                      from the ego lane is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 210 output (hidden reasoning 0) | 3.63 s
```

```
fl_20261017_night_01_f0006510 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid yellow line runs diagonally through the rectangle, with an unbroken
                      stretch clearly visible.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible single solid yellow line marks the left roadway edge. US-3B.09-03 identifies
                      this marking as indicating driving or passing restrictions to its left, so crossing it
                      from the ego lane is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 215 output (hidden reasoning 0) | 3.72 s
```

```
fl_20261017_night_01_f0006510 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid yellow longitudinal line is visible as an unbroken stretch inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The single solid yellow line marks the left roadway edge. Under US-3B.09-03, this
                      marking indicates driving or passing restrictions to its left, so crossing it from the
                      travel lane is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 211 output (hidden reasoning 0) | 4.14 s
```

```
fl_20261017_night_01_f0006600 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid yellow longitudinal line runs diagonally through the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible single solid yellow line marks the left roadway edge. Under US-3B.09-03,
                      this marking indicates the roadway boundary and driving or passing restrictions to its
                      left, so crossing it for lane changing or overtaking is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 248 output (hidden reasoning 32) | 4.18 s
```

```
fl_20261017_night_01_f0006600 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid yellow line is visible as an unbroken diagonal stretch inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The single solid yellow line marks the left edge of the roadway. Under US-3B.09-03, this
                      marking delineates the left-hand roadway edge and restrictions on driving or passing to
                      its left, so crossing it is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 235 output (hidden reasoning 16) | 4.04 s
```

```
fl_20261017_night_01_f0006600 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid yellow line runs diagonally through the rectangle, with an unbroken
                      stretch visible.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible single solid yellow line marks the left edge of the roadway. Under
                      US-3B.09-03, it indicates the roadway boundary and driving or passing restrictions to
                      its left, so crossing it from my lane is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 243 output (hidden reasoning 23) | 5.15 s
```

```
fl_20261017_night_01_f0007725 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid yellow longitudinal line is visible inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The single solid yellow line marks the left roadway edge. Under US-3B.09-03, this
                      marking indicates the roadway boundary or driving and passing restrictions to its left,
                      so crossing it is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 237 output (hidden reasoning 29) | 4.34 s
```

```
fl_20261017_night_01_f0007725 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid yellow longitudinal line is visible inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The single solid yellow line marks the left roadway edge. Under US-3B.09-03, it
                      indicates driving or passing restrictions to its left, so crossing it from the ego lane
                      is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 219 output (hidden reasoning 12) | 3.61 s
```

```
fl_20261017_night_01_f0007725 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid yellow longitudinal line is visible inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The single solid yellow line marks the left roadway edge. Under US-3B.09-03, this
                      marking indicates driving or passing restrictions to its left, so crossing it from the
                      ego lane is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 229 output (hidden reasoning 21) | 3.97 s
```

```
fl_20261017_night_01_f0008220 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A faint single, apparently continuous longitudinal line is visible, but its colour is
                      too dark to identify confidently.
    Evidence          partial
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_determined
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The marking is provisionally classified as a solid yellow edge line, which US-3B.09-03
                      associates with the roadway edge or restrictions to its left. Because darkness prevents
                      confirmation of its colour, the crossing restriction cannot be determined reliably.
                      (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding; citation accepted
Tokens                3960 input + 314 output (hidden reasoning 89) | 7.56 s
```

```
fl_20261017_night_01_f0008220 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A faint single, apparently continuous longitudinal line is visible inside the rectangle,
                      but its colour is too dark and indistinct to identify reliably.
    Evidence          partial
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3A.04-01: "The general functions of longitudinal lines shall be as follows: A. A
                      double line indicates maximum or special restrictions. B. A solid line discourages or
                      prohibits crossing (depending on the specific application). C. A broken line indicat"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_determined
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The faint continuous line is provisionally classified as solid yellow, but its colour is
                      not reliably visible. US-3A.04-01 states that solid lines discourage or prohibit
                      crossing depending on their application, so the crossing restriction cannot be
                      determined from this image.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding; citation in_pack_not_accepted
Tokens                3960 input + 332 output (hidden reasoning 98) | 7.26 s
```

```
fl_20261017_night_01_f0008220 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A faint single longitudinal stripe is visible, but darkness obscures its colour and
                      whether it is continuously solid or broken.
    Evidence          partial
    Output 1          other, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3A.04-01: "The general functions of longitudinal lines shall be as follows: A. A
                      double line indicates maximum or special restrictions. B. A solid line discourages or
                      prohibits crossing (depending on the specific application). C. A broken line indicat"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_determined
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible longitudinal stripe is too dark to classify reliably. The rule distinguishes
                      permissive broken lines from restrictive solid lines, so crossing permission cannot be
                      determined without a clear pattern.  (written after the actions)
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding; contradicts itself: other does not govern cross_line;
                      citation in_pack_not_accepted
Tokens                3960 input + 348 output (hidden reasoning 138) | 9.67 s
```

```
fl_20261017_night_01_f0008355 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A worn white lane-use arrow has visible heads pointing straight ahead and left.
    Evidence          full
    Output 1          arrow / straight_left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible straight and left arrowheads indicate the permissible lane movements under
                      US-3B.23-01: proceeding straight and turning left are allowed, while turning right and
                      making a U-turn are prohibited.  (written after the actions)
Result                Output 1 correct (label arrow/straight_left); Output 2 correct (u_turn: label allowed);
                      evidence group correct; citation accepted
Tokens                3960 input + 242 output (hidden reasoning 34) | 4.65 s
```

```
fl_20261017_night_01_f0008355 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A worn white lane-use arrow has two visible heads pointing straight ahead and left.
    Evidence          full
    Output 1          arrow / straight_left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible straight and left arrowheads designate straight travel and left turns as the
                      permitted lane movements under US-3B.23-01. Right turns and U-turns are not indicated
                      and are prohibited by this lane-use arrow.  (written after the actions)
Result                Output 1 correct (label arrow/straight_left); Output 2 correct (u_turn: label allowed);
                      evidence group correct; citation accepted
Tokens                3960 input + 256 output (hidden reasoning 42) | 5.12 s
```

```
fl_20261017_night_01_f0008355 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A worn white lane-use arrow has two visible heads pointing straight ahead and left.
    Evidence          full
    Output 1          arrow / straight_left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible straight and left arrowheads indicate permissible straight and left
                      movements under US-3B.23-01. This lane-use arrow does not indicate a right turn or
                      U-turn, so those movements are prohibited.  (written after the actions)
Result                Output 1 correct (label arrow/straight_left); Output 2 correct (u_turn: label allowed);
                      evidence group correct; citation accepted
Tokens                3960 input + 258 output (hidden reasoning 47) | 4.98 s
```

```
fl_20261017_night_01_f0011100 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing for overtaking. This longitudinal marking does not
                      govern the other listed actions.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 208 output (hidden reasoning 0) | 3.82 s
```

```
fl_20261017_night_01_f0011100 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible as unbroken stretches inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing marking under
                      US-3B.01-04, prohibiting crossing for passing from either direction. This longitudinal
                      marking governs only crossing the line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 210 output (hidden reasoning 0) | 3.8 s
```

```
fl_20261017_night_01_f0011100 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a two-direction no-passing marking under
                      US-3B.01-04, prohibiting crossing for passing. This longitudinal marking governs only
                      crossing the line, not the other listed actions.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 210 output (hidden reasoning 0) | 4.14 s
```

```
fl_20261017_night_01_f0011310 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines identify a two-direction no-passing marking. Under
                      US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 201 output (hidden reasoning 0) | 3.27 s
```

```
fl_20261017_night_01_f0011310 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines identify a two-direction no-passing marking. Under
                      US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 201 output (hidden reasoning 0) | 3.57 s
```

```
fl_20261017_night_01_f0011310 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a two-direction no-passing zone under US-3B.01-04,
                      which prohibits crossing them for passing in either direction. This longitudinal marking
                      governs only crossing the line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 208 output (hidden reasoning 0) | 3.37 s
```

```
fl_20261017_night_01_f0011400 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing. This longitudinal marking does not
                      govern the other listed actions.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 206 output (hidden reasoning 0) | 3.55 s
```

```
fl_20261017_night_01_f0011400 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing from either direction. This
                      longitudinal marking governs only crossing the line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 207 output (hidden reasoning 0) | 3.64 s
```

```
fl_20261017_night_01_f0011400 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines identify a two-direction no-passing marking. Under
                      US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 199 output (hidden reasoning 0) | 3.46 s
```

```
fl_20261017_night_01_f0011685 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a two-direction no-passing zone under US-3B.01-04,
                      prohibiting crossing them for passing. This longitudinal marking governs only
                      cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 204 output (hidden reasoning 0) | 3.34 s
```

```
fl_20261017_night_01_f0011685 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel, solid yellow lines with an unbroken stretch of each are visible inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, which prohibits crossing these markings for passing in either direction.
                      This longitudinal marking governs only crossing the line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 216 output (hidden reasoning 0) | 4.3 s
```

```
fl_20261017_night_01_f0011685 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines identify a two-direction no-passing marking. Under
                      US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 201 output (hidden reasoning 0) | 3.75 s
```

```
fl_20261017_night_01_f0011775 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines match the two-direction no-passing marking in
                      US-3B.01-04, which prohibits crossing for passing in either direction.  (written after
                      the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 197 output (hidden reasoning 0) | 3.53 s
```

```
fl_20261017_night_01_f0011775 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two visible solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, which prohibits crossing them for passing in either direction. This
                      longitudinal marking governs only crossing the line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 207 output (hidden reasoning 0) | 3.55 s
```

```
fl_20261017_night_01_f0011775 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing. This longitudinal marking governs
                      only crossing the line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 204 output (hidden reasoning 0) | 3.82 s
```

```
fl_20261017_night_01_f0011910 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines with visible unbroken stretches lie inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a two-direction no-passing zone under US-3B.01-04,
                      prohibiting crossing them for passing. This longitudinal marking governs only
                      cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 206 output (hidden reasoning 0) | 3.93 s
```

```
fl_20261017_night_01_f0011910 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines with continuous visible stretches lie inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing marking. Under
                      US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 203 output (hidden reasoning 0) | 4.0 s
```

```
fl_20261017_night_01_f0011910 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines with visible unbroken stretches are inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing. This longitudinal marking governs
                      only cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 207 output (hidden reasoning 0) | 3.62 s
```

```
fl_20261017_night_01_f0012135 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a two-direction no-passing marking under
                      US-3B.01-04, prohibiting crossing them for passing from the ego lane. This longitudinal
                      marking does not govern the other listed actions.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 209 output (hidden reasoning 0) | 3.76 s
```

```
fl_20261017_night_01_f0012135 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing from either direction. This
                      longitudinal marking governs only crossing the line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 207 output (hidden reasoning 0) | 3.63 s
```

```
fl_20261017_night_01_f0012135 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing. This longitudinal marking governs
                      only cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 203 output (hidden reasoning 0) | 3.93 s
```

```
fl_20261017_night_01_f0012315 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines identify a two-direction no-passing marking.
                      US-3B.01-04 prohibits crossing these lines for passing in either direction.  (written
                      after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 197 output (hidden reasoning 0) | 3.48 s
```

```
fl_20261017_night_01_f0012315 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a two-direction no-passing zone under US-3B.01-04,
                      prohibiting crossing them for passing from either direction. This longitudinal marking
                      governs only cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 205 output (hidden reasoning 0) | 3.51 s
```

```
fl_20261017_night_01_f0012315 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines with visible unbroken stretches lie inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two visible solid yellow lines form a double-solid center line. Under US-3B.01-04,
                      this marking prohibits crossing for passing in either direction.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 201 output (hidden reasoning 0) | 3.63 s
```

```
fl_20261017_night_01_f0012465 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing. This longitudinal marking governs
                      only cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 203 output (hidden reasoning 0) | 3.57 s
```

```
fl_20261017_night_01_f0012465 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing for passing from either direction. This longitudinal
                      marking governs only crossing the line, not the other listed movements.  (written after
                      the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 212 output (hidden reasoning 0) | 3.82 s
```

```
fl_20261017_night_01_f0012465 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible pair of solid yellow lines matches the two-direction no-passing marking in
                      US-3B.01-04, which prohibits crossing for passing in either direction. This longitudinal
                      marking governs only cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 208 output (hidden reasoning 0) | 3.46 s
```

```
fl_20261017_night_01_f0012705 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines with visible unbroken stretches are inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two visible solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing for passing from either direction. This longitudinal
                      marking governs only cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 209 output (hidden reasoning 0) | 3.34 s
```

```
fl_20261017_night_01_f0012705 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines with visible unbroken stretches run through the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing. This longitudinal marking governs
                      only cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 207 output (hidden reasoning 0) | 3.49 s
```

```
fl_20261017_night_01_f0012705 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 195 output (hidden reasoning 0) | 3.17 s
```

```
fl_20261017_night_01_f0014235 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible as unbroken stretches inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a two-direction no-passing zone under US-3B.01-04,
                      prohibiting crossing them for passing. This longitudinal marking governs only
                      cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 206 output (hidden reasoning 0) | 4.12 s
```

```
fl_20261017_night_01_f0014235 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines run diagonally through the rectangle, with both lines
                      visibly unbroken.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing. This longitudinal marking governs
                      only cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 211 output (hidden reasoning 0) | 3.64 s
```

```
fl_20261017_night_01_f0014235 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines with unbroken stretches are visible inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines identify a two-direction no-passing marking. Under
                      US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 204 output (hidden reasoning 0) | 3.6 s
```

```
fl_20261017_night_01_f0014280 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow has a single head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow points only straight ahead. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this straight-only arrow allows
                      proceeding straight and prohibits left turns, right turns, and U-turns.  (written after
                      the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 211 output (hidden reasoning 0) | 3.56 s
```

```
fl_20261017_night_01_f0014280 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a straight-ahead head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this arrow allows going straight and
                      prohibits left turns, right turns, and U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 217 output (hidden reasoning 0) | 3.83 s
```

```
fl_20261017_night_01_f0014280 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a straight-ahead head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this arrow permits going straight and
                      excludes left turns, right turns, and U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 215 output (hidden reasoning 0) | 3.61 s
```

```
fl_20261017_night_01_f0014325 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Worn white transverse lines with short, paired longitudinal bars form a ladder-like
                      pavement marking.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     none
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The transverse lines and connecting bars are a crosswalk-style marking, not a
                      longitudinal lane line or lane-use arrow. No supplied passage covers this marking, and
                      it governs none of the six specified actions.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3960 input + 280 output (hidden reasoning 74) | 7.28 s
```

```
fl_20261017_night_01_f0014325 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          White transverse pavement lines with short, paired longitudinal bars are visible inside
                      the rectangle.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     none
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The transverse lines and short bars are neither a longitudinal lane boundary nor a lane-
                      use arrow. No supplied passage governs this marking, and under the task definitions it
                      governs none of the six listed actions.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3960 input + 294 output (hidden reasoning 91) | 7.86 s
```

```
fl_20261017_night_01_f0014325 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          White transverse pavement lines with several short, parallel white bars between them
                      form a crosswalk pattern.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     none
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The transverse white lines and connecting bars identify a crosswalk rather than a
                      longitudinal lane line or lane-use arrow. No supplied passage covers crosswalk markings,
                      and this marking governs none of the six listed actions.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3960 input + 304 output (hidden reasoning 96) | 7.63 s
```

```
fl_20261017_night_01_f0014670 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid white line runs diagonally through the rectangle.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible single solid white line discourages crossing under US-3B.06-05-06 but does
                      not prohibit it, so crossing is allowed under the specified action definitions.
                      (written after the actions)
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct;
                      citation accepted
Tokens                3960 input + 220 output (hidden reasoning 17) | 4.01 s
```

```
fl_20261017_night_01_f0014670 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid white line forms an unbroken diagonal stretch inside the rectangle.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible single solid white line discourages crossing under US-3B.06-05-06 but does
                      not prohibit it, so crossing is allowed. This longitudinal marking does not govern the
                      other listed actions.  (written after the actions)
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct;
                      citation accepted
Tokens                3960 input + 231 output (hidden reasoning 19) | 3.89 s
```

```
fl_20261017_night_01_f0014670 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single solid white longitudinal line runs diagonally through the rectangle.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible single solid white line discourages crossing under US-3B.06-05-06 but does
                      not prohibit it, so crossing is allowed under the specified action definitions.
                      (written after the actions)
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct;
                      citation accepted
Tokens                3960 input + 217 output (hidden reasoning 13) | 3.53 s
```

```
fl_20261017_night_01_f0015915 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two visible solid yellow lines indicate a two-direction no-passing marking. Under
                      US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 200 output (hidden reasoning 0) | 4.28 s
```

```
fl_20261017_night_01_f0015915 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing. This longitudinal marking does not
                      govern the other listed actions.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 208 output (hidden reasoning 0) | 3.62 s
```

```
fl_20261017_night_01_f0015915 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines with an unbroken stretch of each visible inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing marking.
                      US-3B.01-04 prohibits crossing these lines for passing from either direction.  (written
                      after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 203 output (hidden reasoning 0) | 3.76 s
```

```
fl_20261017_night_01_f0018210 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow longitudinal lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible pair of solid yellow lines identifies a two-direction no-passing marking.
                      Under US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 202 output (hidden reasoning 0) | 3.63 s
```

```
fl_20261017_night_01_f0018210 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow longitudinal lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible pair of solid yellow lines denotes a two-direction no-passing marking.
                      US-3B.01-04 prohibits crossing these lines for passing in either direction.  (written
                      after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 199 output (hidden reasoning 0) | 4.0 s
```

```
fl_20261017_night_01_f0018210 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow longitudinal lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible pair of solid yellow lines indicates a two-direction no-passing zone. Under
                      US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 202 output (hidden reasoning 0) | 3.46 s
```

```
fl_20261017_night_01_f0018240 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Inside the rectangle, two parallel solid yellow longitudinal lines are visible with an
                      unbroken stretch of both lines.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible pair of solid yellow lines is a two-direction no-passing marking. Under
                      US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 240 output (hidden reasoning 27) | 4.38 s
```

```
fl_20261017_night_01_f0018240 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow longitudinal lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a two-direction no-passing zone under US-3B.01-04,
                      which prohibits crossing the center markings for passing from either direction. This
                      longitudinal marking governs only crossing the line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 239 output (hidden reasoning 28) | 4.13 s
```

```
fl_20261017_night_01_f0018240 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow longitudinal lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible pair of solid yellow lines indicates a two-direction no-passing marking.
                      Under US-3B.01-04, crossing these lines for passing is prohibited in either direction.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 228 output (hidden reasoning 24) | 3.96 s
```

```
fl_20261017_night_01_f0018300 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a two-direction no-passing zone under US-3B.01-04,
                      prohibiting crossing them for passing. This longitudinal marking governs only
                      cross_line.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 224 output (hidden reasoning 20) | 3.83 s
```

```
fl_20261017_night_01_f0018300 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a two-direction no-passing zone. Under US-3B.01-04,
                      crossing these lines for passing is prohibited in either direction.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 221 output (hidden reasoning 20) | 3.68 s
```

```
fl_20261017_night_01_f0018300 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines indicate a two-direction no-passing zone under
                      US-3B.01-04, prohibiting crossing them for passing.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 215 output (hidden reasoning 18) | 3.7 s
```

```
fl_20261017_night_01_f0030060 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white line with visible dashes and intervening gaps is inside the
                      rectangle.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and gaps identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this line with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 208 output (hidden reasoning 0) | 4.04 s
```

```
fl_20261017_night_01_f0030060 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line with visible painted dashes and intervening
                      gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and gaps identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this marking with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 206 output (hidden reasoning 0) | 4.18 s
```

```
fl_20261017_night_01_f0030060 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line with visible painted segments and intervening
                      gaps is inside the rectangle.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible broken white line permits crossing with care under US-3B.06-05-06. As a
                      longitudinal line, it does not govern the other listed actions.  (written after the
                      actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 207 output (hidden reasoning 0) | 3.94 s
```

```
fl_20261017_night_01_f0030360 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white line is visible inside the rectangle, with white dash segments
                      separated by an unpainted gap.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and intervening gap identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this marking with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 215 output (hidden reasoning 0) | 3.61 s
```

```
fl_20261017_night_01_f0030360 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line is visible, with painted segments separated by
                      gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white segments and intervening gaps identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this marking with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 207 output (hidden reasoning 0) | 3.56 s
```

```
fl_20261017_night_01_f0030360 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white line is visible, with white dash segments separated by an
                      unpainted gap.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and intervening gap identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this marking with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 212 output (hidden reasoning 0) | 3.44 s
```

```
fl_20261017_night_01_f0030555 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line is visible, with white dashes separated by clear
                      gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and gaps identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this line with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 208 output (hidden reasoning 0) | 4.02 s
```

```
fl_20261017_night_01_f0030555 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line, with visible dash segments and intervening
                      gaps, is inside the rectangle.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and gaps identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this line with care is neither discouraged nor prohibited, so
                      crossing is allowed.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 216 output (hidden reasoning 0) | 3.56 s
```

```
fl_20261017_night_01_f0030555 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line with visible dashes and gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and gaps identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this marking with care is allowed.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 200 output (hidden reasoning 0) | 3.43 s
```

```
fl_20261017_night_01_f0031695 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line with visible painted dashes and intervening
                      gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible broken white line permits crossing with care under US-3B.06-05-06. This
                      longitudinal marking does not govern the other listed actions.  (written after the
                      actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 201 output (hidden reasoning 0) | 3.91 s
```

```
fl_20261017_night_01_f0031695 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line with visible painted dashes and intervening
                      gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible broken white line permits crossing with care under US-3B.06-05-06. This
                      longitudinal marking does not govern the other listed actions.  (written after the
                      actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 201 output (hidden reasoning 0) | 3.75 s
```

```
fl_20261017_night_01_f0031695 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line, with visible painted dashes and gaps between
                      them.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and intervening gaps identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this marking with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 209 output (hidden reasoning 0) | 3.47 s
```

```
fl_20261017_night_01_f0032025 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line is visible, with a white dash and an intervening
                      gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dash and gap identify a broken white lane line. Under US-3B.06-05-06,
                      crossing this marking with care is neither discouraged nor prohibited.  (written after
                      the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 230 output (hidden reasoning 20) | 3.69 s
```

```
fl_20261017_night_01_f0032025 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal marking is visible, with a white dash and an
                      unpainted gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dash and gap identify a broken white lane line. Under US-3B.06-05-06,
                      crossing this marking with care is neither discouraged nor prohibited.  (written after
                      the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 237 output (hidden reasoning 26) | 4.57 s
```

```
fl_20261017_night_01_f0032025 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line is visible, with a white dash and an intervening
                      unpainted gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dash and gap identify a broken white lane line. Under US-3B.06-05-06,
                      crossing this line with care is not discouraged or prohibited.  (written after the
                      actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 241 output (hidden reasoning 28) | 4.17 s
```

```
fl_20261017_night_01_f0032220 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line is visible, with a white dash and a gap before
                      the next short visible segment.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dash and gap identify a broken white lane line. Under US-3B.06-05-06,
                      crossing this line with care is neither discouraged nor prohibited.  (written after the
                      actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 212 output (hidden reasoning 0) | 3.21 s
```

```
fl_20261017_night_01_f0032220 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line is visible, including a long dash, a gap, and a
                      short portion of the next dash.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and intervening gap identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this line with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 218 output (hidden reasoning 0) | 3.6 s
```

```
fl_20261017_night_01_f0032220 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line is visible, with a long dash, a gap, and a small
                      farther dash inside the rectangle.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and intervening gap identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this line with care is not discouraged or prohibited.  (written
                      after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 218 output (hidden reasoning 0) | 3.9 s
```

```
fl_20261017_night_01_f0032505 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line with visible painted segments and intervening
                      gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white segments and gaps identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this marking with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 204 output (hidden reasoning 0) | 3.49 s
```

```
fl_20261017_night_01_f0032505 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line has visible painted segments separated by
                      unpainted gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white segments and intervening gaps identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this marking with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 208 output (hidden reasoning 0) | 3.61 s
```

```
fl_20261017_night_01_f0032505 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A single broken white longitudinal line is visible, with painted segments separated by
                      gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white segments and intervening gaps identify a broken white lane line. Under
                      US-3B.06-05-06, crossing this marking with care is neither discouraged nor prohibited.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3960 input + 207 output (hidden reasoning 0) | 3.31 s
```

```
fl_20261017_night_01_f0032685 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow with a curved shaft and a single arrowhead pointing left is
                      visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The single left-pointing arrowhead indicates a left-turn movement. Under US-3B.23-01,
                      lane-use arrows specify mandatory or permissible movements, so this left-only arrow
                      permits turning left and prohibits going straight, turning right, or making a U-turn.
                      (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 254 output (hidden reasoning 26) | 4.58 s
```

```
fl_20261017_night_01_f0032685 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow with a single head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a left-pointing head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this marking permits a left turn and
                      excludes straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 244 output (hidden reasoning 26) | 4.51 s
```

```
fl_20261017_night_01_f0032685 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow with a single head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The arrow has only a left-pointing head. Under US-3B.23-01, lane-use arrows indicate
                      mandatory or permissible movements, so this marking permits a left turn and prohibits
                      straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 243 output (hidden reasoning 26) | 9.3 s
```

```
fl_20261017_night_01_f0032775 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white curved arrow with a single head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The arrow has only a left-pointing head. Under US-3B.23-01, lane-use arrows indicate
                      mandatory or permissible movements, so this marking permits a left turn and excludes
                      straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 214 output (hidden reasoning 0) | 3.72 s
```

```
fl_20261017_night_01_f0032775 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white curved arrow with a single arrowhead pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrowhead points only left. Under US-3B.23-01, lane-use arrows indicate
                      mandatory or permissible movements, so this arrow permits a left turn and excludes
                      straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 213 output (hidden reasoning 0) | 3.82 s
```

```
fl_20261017_night_01_f0032775 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white curved arrow with a single arrowhead pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a left-pointing head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this arrow permits a left turn but not
                      straight travel, a right turn, or a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 218 output (hidden reasoning 0) | 3.57 s
```

```
fl_20261017_night_01_f0032820 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white arrow with a bent shaft and a single head pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The arrow has only a left-pointing head. Under US-3B.23-01, lane-use arrows indicate
                      mandatory or permissible movements, so this marking allows a left turn and excludes
                      straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 217 output (hidden reasoning 0) | 3.28 s
```

```
fl_20261017_night_01_f0032820 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white bent arrow with a single arrowhead pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a left-pointing head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this marking permits a left turn and
                      prohibits straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 216 output (hidden reasoning 0) | 3.72 s
```

```
fl_20261017_night_01_f0032820 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white bent arrow with a single head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The arrow has only a left-pointing head. Under US-3B.23-01, lane-use arrows indicate
                      mandatory or permissible movements, so this marking permits a left turn and excludes
                      straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 214 output (hidden reasoning 0) | 3.68 s
```

```
fl_20261017_night_01_f0032865 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow with a head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow points only left. Under US-3B.23-01, lane-use arrows indicate
                      mandatory or permissible movements, so this arrow permits a left turn and excludes
                      straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 247 output (hidden reasoning 34) | 4.46 s
```

```
fl_20261017_night_01_f0032865 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow with a head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The arrow has a left-pointing head only. Under US-3B.23-01, lane-use arrows indicate
                      mandatory or permissible movements, so this arrow permits a left turn and excludes
                      straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 244 output (hidden reasoning 28) | 4.49 s
```

```
fl_20261017_night_01_f0032865 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white lane-use arrow with a head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow points only left. Under US-3B.23-01, lane-use arrows indicate
                      mandatory or permissible movements, so this marking allows a left turn but not straight
                      travel, a right turn, or a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 257 output (hidden reasoning 42) | 4.63 s
```

```
fl_20261017_night_01_f0032940 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white curved arrow with a single head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a left-pointing head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this marking allows a left turn and
                      excludes straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 215 output (hidden reasoning 0) | 4.18 s
```

```
fl_20261017_night_01_f0032940 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white curved lane-use arrow with a single head pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The visible arrow has only a left-pointing head. Under US-3B.23-01, lane-use arrows
                      indicate mandatory or permissible movements, so this marking permits a left turn and
                      excludes straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 217 output (hidden reasoning 0) | 3.6 s
```

```
fl_20261017_night_01_f0032940 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A white curved lane-use arrow with a single head pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The arrow has only a left-pointing head. Under US-3B.23-01, lane-use arrows indicate
                      mandatory or permissible movements, so this marking permits a left turn and excludes
                      straight, right-turn, and U-turn movements.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3960 input + 216 output (hidden reasoning 0) | 4.1 s
```

```
fl_20261017_night_01_f0039450 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          The marked lane has a solid yellow line and a broken yellow line along each edge, with
                      the broken lines facing inward, and two white curved arrows pointing in opposite
                      directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid and broken yellow boundaries, with the broken lines toward the lane,
                      identify a two-way left-turn lane under US-3B.05-01. That passage permits using the lane
                      as part of a left-turn maneuver, allowing entry to wait for a left turn and turning left
                      out of it.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; citation accepted
Tokens                3960 input + 270 output (hidden reasoning 18) | 4.85 s
```

```
fl_20261017_night_01_f0039450 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A centre lane is bordered on both sides by paired solid and broken yellow lines, with
                      white curved arrows pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid and broken yellow boundaries and opposing white arrows identify a two-
                      way left-turn lane. US-3B.05-01 permits use of this lane from either direction as part
                      of a left-turn maneuver, allowing entry to wait for a left turn and turning left out of
                      it.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; citation accepted
Tokens                3960 input + 258 output (hidden reasoning 19) | 4.23 s
```

```
fl_20261017_night_01_f0039450 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          The rectangle shows a centre lane bounded on both sides by a solid yellow line alongside
                      a broken yellow line, with the broken lines toward the lane interior and two white
                      curved arrows pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid and broken yellow boundaries, with the broken lines facing inward,
                      identify a two-way left-turn lane. US-3B.05-01 permits using this lane as part of a
                      left-turn maneuver, allowing entry to wait for a left turn and turning left out of the
                      lane.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; citation accepted
Tokens                3960 input + 271 output (hidden reasoning 17) | 4.14 s
```

```
fl_20261017_night_01_f0039465 | Test B | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          A centre lane is bordered on both sides by paired solid and broken yellow lines and
                      contains two white curved arrows pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid and broken yellow boundaries on both sides identify a two-way left-turn
                      lane. US-3B.05-01 permits using this centre lane as part of a left-turn maneuver,
                      allowing entry to wait for a left turn and turning left out of it.  (written after the
                      actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; citation accepted
Tokens                3960 input + 273 output (hidden reasoning 37) | 5.27 s
```

```
fl_20261017_night_01_f0039465 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          The lane has solid and broken yellow lines along both edges, with white curved arrows
                      pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid and broken yellow boundaries and opposing white arrows identify a two-
                      way left-turn lane. US-3B.05-01 permits using this lane as part of a left-turn maneuver,
                      allowing entry to wait for a left turn and turning left out of it.  (written after the
                      actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; citation accepted
Tokens                3960 input + 262 output (hidden reasoning 31) | 4.91 s
```

```
fl_20261017_night_01_f0039465 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v2
Step 1  Look          The rectangle contains two white curved arrows pointing in opposite directions, within a
                      lane bordered on both sides by a solid yellow line and a broken yellow line.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid-and-broken yellow boundaries and opposing white arrows identify a two-
                      way left-turn lane. US-3B.05-01 permits traffic in either direction to use this lane as
                      part of a left-turn maneuver, allowing entry to wait for a left turn and turning left
                      out of it.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; citation accepted
Tokens                3960 input + 279 output (hidden reasoning 33) | 4.77 s
```
