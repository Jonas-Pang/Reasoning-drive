# Reasoning trace of run 20261027_221432_testA_US

```
fl_20261017_night_01_f0001950 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight and
                      prohibits left turns, right turns, and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               allowed         The straight-pointing arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2584 input + 295 output (hidden reasoning 0) | 3.38 s
```

```
fl_20261017_night_01_f0001950 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight and
                      prohibits left turns, right turns, and U-turns from that lane at the next intersection.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               allowed         The straight-pointing arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2584 input + 299 output (hidden reasoning 0) | 3.94 s
```

```
fl_20261017_night_01_f0001950 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight from
                      its lane and prohibits left turns, right turns, and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow prohibits a left turn.
    turn_right                prohibited      The straight-only arrow prohibits a right turn.
    u_turn                    prohibited      The straight-only arrow prohibits a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2584 input + 298 output (hidden reasoning 0) | 3.74 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight and
                      prohibits turning left, turning right, or making a U-turn from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow prohibits a left turn.
    turn_right                prohibited      The straight-only arrow prohibits a right turn.
    u_turn                    prohibited      The straight-only arrow prohibits a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2584 input + 296 output (hidden reasoning 0) | 4.01 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow has a single clearly visible head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight and
                      prohibits left turns, right turns, and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2584 input + 290 output (hidden reasoning 0) | 4.55 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow has a single clearly visible head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow requires traffic in that lane to
                      proceed straight rather than turn left, right, or make a U-turn.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               allowed         The straight arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow prohibits a left turn from this lane.
    turn_right                prohibited      The straight-only arrow prohibits a right turn from this lane.
    u_turn                    prohibited      The straight-only arrow prohibits a U-turn from this lane.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2584 input + 303 output (hidden reasoning 0) | 3.42 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a white crosswalk formed by broad repeated bars with dark gaps
                      and narrow white transverse boundary lines.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, a marked crosswalk identifies a pedestrian crossing where drivers
                      must yield or stop for pedestrians as required by applicable law, rather than
                      prescribing any of the six listed lane movements.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the visible crosswalk is classified as other, and all six actions are
                      not_applicable.
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2584 input + 320 output (hidden reasoning 0) | 4.22 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a white crosswalk marking with broad repeated stripes separated
                      by dark pavement gaps and connected by transverse white borders.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, a marked crosswalk identifies a pedestrian crossing where drivers
                      must yield or stop for pedestrians as required by applicable law, rather than
                      prescribing any of the six listed lane movements.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2584 input + 303 output (hidden reasoning 0) | 3.88 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a white crosswalk consisting of broad solid stripes between two
                      transverse white boundary lines.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, a marked crosswalk identifies a pedestrian crossing where drivers
                      must yield to pedestrians as required by applicable law, rather than prescribing any of
                      the six listed maneuvers.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2584 input + 297 output (hidden reasoning 0) | 3.94 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single yellow longitudinal line with a continuous, unbroken
                      stretch.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow left-edge line marks the roadway boundary and
                      prohibits crossing it for lane changes or overtaking.
Step 3  Decide
    cross_line                prohibited      The solid yellow edge line prohibits crossing for lane changes
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 290 output (hidden reasoning 0) | 3.44 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single yellow longitudinal line with a continuous, unbroken
                      stretch.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow edge line discourages crossing but does not
                      itself prohibit crossing.
Step 3  Decide
    cross_line                allowed         The single solid yellow line discourages crossing but does not
                                              prohibit it.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2584 input + 343 output (hidden reasoning 58) | 4.87 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A single solid yellow longitudinal line with an unbroken visible stretch lies inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow edge line discourages crossing but does not
                      by itself prohibit it.
Step 3  Decide
    cross_line                allowed         The single solid yellow line discourages crossing but does not
                                              prohibit it.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2584 input + 303 output (hidden reasoning 16) | 3.94 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single continuous yellow longitudinal line beside the curb.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow longitudinal line discourages crossing but
                      does not itself prohibit it.
Step 3  Decide
    cross_line                allowed         The single solid yellow line discourages crossing but does not
                                              prohibit it.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2584 input + 322 output (hidden reasoning 40) | 4.54 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, a single solid yellow longitudinal line runs along the left side
                      of my lane.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line prohibits crossing it for passing or
                      overtaking.
Step 3  Decide
    cross_line                prohibited      The solid yellow line prohibits crossing for passing or
                                              overtaking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 341 output (hidden reasoning 57) | 5.0 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle shows a continuous single yellow longitudinal line to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow left-edge line must not be crossed for changing
                      lanes or overtaking.
Step 3  Decide
    cross_line                prohibited      The solid yellow line prohibits crossing for a lane change or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 380 output (hidden reasoning 93) | 7.83 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single yellow longitudinal line with a visible unbroken
                      stretch to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow line discourages crossing but does not by
                      itself prohibit crossing when otherwise lawful and safe.
Step 3  Decide
    cross_line                allowed         The single solid yellow line discourages crossing but does not
                                              itself prohibit it.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2584 input + 344 output (hidden reasoning 47) | 4.82 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single yellow longitudinal line with a visible unbroken
                      stretch.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow line discourages crossing for passing but
                      does not by itself prohibit crossing.
Step 3  Decide
    cross_line                allowed         The single solid yellow line discourages crossing but does not
                                              by itself forbid it.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2584 input + 287 output (hidden reasoning 0) | 3.73 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single yellow longitudinal line with a visible unbroken
                      stretch.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow line discourages crossing but does not by
                      itself prohibit it.
Step 3  Decide
    cross_line                allowed         The single solid yellow line discourages crossing but does not
                                              itself prohibit it.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2584 input + 333 output (hidden reasoning 47) | 4.54 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A single yellow solid line runs diagonally through the rectangle along the left side of
                      the lane.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow line discourages crossing for passing but
                      does not by itself prohibit crossing.
Step 3  Decide
    cross_line                allowed         The single solid yellow line discourages crossing but does not
                                              itself forbid it.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2584 input + 433 output (hidden reasoning 142) | 8.04 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          No usable pavement marking is visible inside the cyan rectangle; the dark pavement and
                      faint streaks do not reveal a definite paint colour or line pattern.
    Evidence          insufficient
    Output 1          none_visible, position left
Step 2  Rule          No marking-specific United States traffic rule can be applied because no pavement
                      marking is discernible in the rectangle.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking: no marking is visible.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding
Tokens                2584 input + 324 output (hidden reasoning 27) | 3.99 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A faint, apparently yellow single longitudinal line is visible on the left, but darkness
                      and wear obscure whether it is continuously solid or broken.
    Evidence          partial
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow line discourages crossing rather than
                      categorically prohibiting it, while a broken yellow line permits crossing when safe.
Step 3  Decide
    cross_line                allowed         The single yellow line does not categorically prohibit crossing
                                              under either visible-pattern interpretation.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         The solid classification is tentative because the pattern is obscured; either single-
                      line pattern permits crossing under the stated rule, and all unrelated actions are
                      not_applicable.
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding; UNSAFE: cross_line
Tokens                2584 input + 492 output (hidden reasoning 154) | 8.51 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A worn white lane-use arrow inside the rectangle has heads pointing straight ahead and
                      left.
    Evidence          full
    Output 1          arrow / straight_left, position in_ego_lane
Step 2  Rule          In the United States, a straight-and-left lane-use arrow permits proceeding straight or
                      turning left, prohibits turning right, and does not itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrowhead permits proceeding straight.
    turn_left                 allowed         The left arrowhead permits turning left.
    turn_right                prohibited      The arrow permits only straight and left movements, not a right
                                              turn.
    u_turn                    allowed         The permitted left movement does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight_left); Output 2 correct; evidence group correct
Tokens                2584 input + 426 output (hidden reasoning 121) | 7.19 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a worn white lane-use arrow with one head pointing straight
                      ahead and another pointing left.
    Evidence          full
    Output 1          arrow / straight_left, position in_ego_lane
Step 2  Rule          In the United States, a straight-and-left lane-use arrow permits straight travel or a
                      left turn, prohibits a right turn, and does not itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               allowed         The straight arrowhead permits straight travel.
    turn_left                 allowed         The left arrowhead permits a left turn.
    turn_right                prohibited      The straight-and-left arrow does not permit a right turn.
    u_turn                    allowed         The left-turn indication does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight_left); Output 2 correct; evidence group correct
Tokens                2584 input + 420 output (hidden reasoning 110) | 6.19 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A worn white lane-use arrow inside the rectangle has arrowheads pointing straight ahead
                      and left.
    Evidence          full
    Output 1          arrow / straight_left, position in_ego_lane
Step 2  Rule          In the United States, a straight-and-left lane-use arrow permits proceeding straight or
                      turning left, excludes a right turn, and does not by itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrowhead permits proceeding straight.
    turn_left                 allowed         The left arrowhead permits turning left.
    turn_right                prohibited      The straight-and-left arrow excludes a right turn.
    u_turn                    allowed         The straight-and-left arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight_left); Output 2 correct; evidence group correct
Tokens                2584 input + 444 output (hidden reasoning 139) | 7.57 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow lines curve ahead with no visible
                      breaks.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changing
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 284 output (hidden reasoning 0) | 3.66 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing them to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 280 output (hidden reasoning 0) | 3.47 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow lines form an unbroken double line to
                      the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, a double solid yellow centerline prohibits crossing it to change
                      lanes or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 293 output (hidden reasoning 0) | 3.37 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow longitudinal lines are visible to the
                      left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 289 output (hidden reasoning 0) | 4.26 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous solid yellow longitudinal lines to the
                      left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them for
                      overtaking or changing lanes.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for changing lanes
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 287 output (hidden reasoning 0) | 3.08 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous solid yellow lines to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing for passing or
                      changing lanes into opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for passing or
                                              changing lanes.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 286 output (hidden reasoning 0) | 3.43 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, solid yellow longitudinal lines to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing for overtaking
                      or changing lanes into opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 288 output (hidden reasoning 0) | 3.52 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous solid yellow lines to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changing
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 286 output (hidden reasoning 0) | 3.12 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous solid yellow lines to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing for overtaking
                      or changing lanes.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for changing lanes
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 285 output (hidden reasoning 0) | 3.45 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow longitudinal lines are visible to the
                      left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 289 output (hidden reasoning 0) | 3.5 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 285 output (hidden reasoning 0) | 3.81 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous yellow longitudinal lines to the left
                      of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for a lane change
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 289 output (hidden reasoning 0) | 3.2 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains two parallel, continuous yellow lines to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing for passing or
                      changing lanes.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for passing or
                                              changing lanes.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 281 output (hidden reasoning 0) | 3.44 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow lines run along the left side of my
                      lane.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 286 output (hidden reasoning 0) | 3.69 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel yellow solid lines run along the left side of my
                      lane.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 286 output (hidden reasoning 0) | 3.48 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous yellow lines to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing to change lanes
                      or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 286 output (hidden reasoning 0) | 3.27 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing for overtaking
                      or changing lanes into opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 288 output (hidden reasoning 0) | 4.19 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous yellow lines to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 285 output (hidden reasoning 0) | 3.79 s
```

```
fl_20261017_night_01_f0012135 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 282 output (hidden reasoning 0) | 3.33 s
```

```
fl_20261017_night_01_f0012135 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 281 output (hidden reasoning 0) | 3.39 s
```

```
fl_20261017_night_01_f0012135 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous solid yellow lines.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 282 output (hidden reasoning 0) | 3.93 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Two parallel, continuous yellow lines are visible inside the cyan rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing to change lanes
                      or overtake opposing-direction traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 283 output (hidden reasoning 0) | 3.55 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Two parallel, continuous yellow lines are visible inside the cyan rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 280 output (hidden reasoning 0) | 3.05 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous solid yellow lines.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing them to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 279 output (hidden reasoning 0) | 3.36 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changing
                                              or overtaking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 285 output (hidden reasoning 0) | 3.94 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow lines form an unbroken double line to
                      the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 290 output (hidden reasoning 0) | 3.51 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel yellow longitudinal lines have continuous, unbroken
                      stretches.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing them to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 283 output (hidden reasoning 0) | 3.55 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing from the lane to
                      change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 280 output (hidden reasoning 0) | 3.29 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous yellow longitudinal lines.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing them to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 279 output (hidden reasoning 0) | 3.26 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing into the opposing lane
                      to pass or change lanes.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changing
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 281 output (hidden reasoning 0) | 3.5 s
```

```
fl_20261017_night_01_f0014235 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains two parallel, continuous yellow lines to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing them to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      Both yellow lines are solid, prohibiting crossing for lane
                                              changes or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 285 output (hidden reasoning 0) | 3.54 s
```

```
fl_20261017_night_01_f0014235 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous yellow lines to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing them to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 284 output (hidden reasoning 0) | 3.1 s
```

```
fl_20261017_night_01_f0014235 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel, continuous yellow lines are visible to the left of
                      my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing them to change lanes
                      or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 288 output (hidden reasoning 0) | 3.8 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single white arrow with a visible head pointing straight
                      ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow requires proceeding straight and
                      prohibits left turns, right turns, and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2584 input + 291 output (hidden reasoning 0) | 3.44 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight and
                      prohibits left turns, right turns, and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2584 input + 291 output (hidden reasoning 0) | 3.84 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight and
                      prohibits left turns, right turns, and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight-pointing arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits making a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2584 input + 294 output (hidden reasoning 0) | 3.91 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains worn white transverse strokes and short parallel strokes forming
                      a non-arrow pavement marking.
    Evidence          partial
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, this non-arrow, non-longitudinal marking does not itself govern
                      any of the six specified actions.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label other); Output 2 not scored; evidence group over_withholding
Tokens                2584 input + 448 output (hidden reasoning 162) | 8.4 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains faded white pavement lettering made of elongated straight and
                      curved strokes; the complete word is not clearly legible.
    Evidence          partial
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, pavement lettering conveys a message rather than independently
                      granting or prohibiting any of the six specified maneuvers.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is classified as pavement text, and all six actions are
                      not_applicable.
Result                Output 1 correct (label other); Output 2 not scored; evidence group over_withholding
Tokens                2584 input + 535 output (hidden reasoning 224) | 11.09 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains white crosswalk markings, with transverse lines and broad bars
                      extending between them.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, crosswalk markings identify a pedestrian crossing where drivers
                      must yield or stop for pedestrians as required by applicable law, rather than prescribe
                      any of the six listed maneuvers.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2584 input + 542 output (hidden reasoning 243) | 10.56 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single white longitudinal line with a visible unbroken stretch.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a single solid white longitudinal line discourages crossing but
                      does not by itself prohibit it.
Step 3  Decide
    cross_line                allowed         The single solid white line discourages crossing but does not
                                              prohibit it.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2584 input + 300 output (hidden reasoning 15) | 3.76 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, a single solid white line runs along the left side of my lane.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a single solid white longitudinal line discourages crossing but
                      does not by itself prohibit it.
Step 3  Decide
    cross_line                allowed         The single solid white line discourages crossing but does not
                                              prohibit it.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2584 input + 309 output (hidden reasoning 21) | 4.12 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, a single solid white longitudinal line runs along the left side of
                      my lane.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          In the United States, crossing a single solid white lane line is discouraged but not
                      prohibited by the marking alone.
Step 3  Decide
    cross_line                allowed         The single solid white line discourages crossing but does not
                                              prohibit it.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2584 input + 307 output (hidden reasoning 18) | 3.78 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow lines run diagonally along the left side
                      of my lane.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing to change lanes
                      or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for changing lanes
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 289 output (hidden reasoning 0) | 3.38 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous solid yellow lines to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for a lane change
                                              or overtaking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 287 output (hidden reasoning 0) | 3.29 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous solid yellow lines to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing for passing or
                      changing lanes.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for changing lanes
                                              or overtaking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 284 output (hidden reasoning 0) | 3.3 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow longitudinal lines are visible to the
                      left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for changing lanes
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 287 output (hidden reasoning 0) | 3.52 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow lines run along the left side of my
                      lane.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing to change lanes
                      or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 287 output (hidden reasoning 0) | 3.32 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow longitudinal lines are visible on the
                      left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing them to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for a lane change
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 310 output (hidden reasoning 21) | 3.8 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow lines run along the left side of my
                      lane.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing into the opposing lane
                      to pass or change lanes.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for a lane change
                                              or overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 316 output (hidden reasoning 26) | 3.91 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, two parallel solid yellow lines form a double line to the left of
                      my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing them to change lanes
                      or overtake opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 315 output (hidden reasoning 24) | 4.39 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains two parallel solid yellow longitudinal lines to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing into opposing traffic
                      to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changing
                                              or overtaking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 311 output (hidden reasoning 24) | 4.1 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing for overtaking
                      or changing lanes into opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 313 output (hidden reasoning 23) | 3.88 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains two parallel, continuous yellow lines to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing them to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 304 output (hidden reasoning 19) | 3.72 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains two parallel, continuous yellow lines to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow lines prohibit crossing for passing or
                      changing lanes into opposing traffic.
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for lane changes or
                                              overtaking.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2584 input + 308 output (hidden reasoning 22) | 3.86 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single broken white line, with visible white dashes separated
                      by unpainted gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 281 output (hidden reasoning 0) | 3.92 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single broken white longitudinal line with visible dashes and
                      intervening gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The visible broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 278 output (hidden reasoning 0) | 3.91 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single broken white line, with visible white dashes separated
                      by unpainted gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line may be crossed to change lanes when it is
                      safe to do so.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 287 output (hidden reasoning 0) | 4.35 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains portions of a single broken white longitudinal line, with white
                      dashes separated by a visible gap.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line may be crossed to change lanes when it is
                      safe to do so.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 287 output (hidden reasoning 0) | 3.48 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, a single white longitudinal broken line has visible dash portions
                      separated by a gap.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 278 output (hidden reasoning 0) | 3.28 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, a single broken white longitudinal line has visible dash portions
                      separated by an unpainted gap.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 281 output (hidden reasoning 0) | 3.41 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single broken white longitudinal line, with white dashes
                      separated by visible gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe.
Step 3  Decide
    cross_line                allowed         The visible broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 279 output (hidden reasoning 0) | 3.33 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single broken white longitudinal line with visible dashes and
                      gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 275 output (hidden reasoning 0) | 3.03 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single broken white longitudinal line, with visible dashes
                      separated by gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 277 output (hidden reasoning 0) | 3.28 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single broken white line with visible painted dashes and
                      intervening gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 277 output (hidden reasoning 0) | 3.34 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single broken white line with visible dashes and gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 275 output (hidden reasoning 0) | 3.25 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single broken white longitudinal line with visible dashes and
                      gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 275 output (hidden reasoning 0) | 3.19 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single broken white longitudinal line, with a visible white
                      dash and intervening unpainted gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 282 output (hidden reasoning 0) | 3.79 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single broken white longitudinal line, with a visible white
                      dash and gaps between segments.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line may be crossed to change lanes when safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 280 output (hidden reasoning 0) | 3.51 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, a single white broken longitudinal line has a visible dash
                      followed by an unpainted gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line may be crossed to change lanes when it is
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 313 output (hidden reasoning 27) | 4.24 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single broken white line, with a long dash, a gap, and a short
                      visible portion of the next dash.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line may be crossed to change lanes when safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 288 output (hidden reasoning 0) | 3.53 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single broken white line, with a long dash and a smaller
                      distant dash separated by a visible gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 284 output (hidden reasoning 0) | 3.3 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single broken white line, with a long dash, a gap, and a small
                      portion of the next dash visible.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 287 output (hidden reasoning 0) | 3.99 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, a single white broken longitudinal line has visible painted
                      segments separated by gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a dashed white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The visible dashed white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 278 output (hidden reasoning 0) | 3.83 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single broken white longitudinal line, with visible dash
                      segments and intervening gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 279 output (hidden reasoning 0) | 3.77 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle, a single white broken longitudinal line has visible painted
                      segments separated by gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a dashed white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The visible dashed white line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2584 input + 278 output (hidden reasoning 0) | 3.41 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a white curved lane-use arrow with its arrowhead pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane arrow requires a leftward movement rather than
                      straight or right travel and does not itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits going straight.
    turn_left                 allowed         The left-pointing arrow allows a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-turn arrow does not itself forbid a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 367 output (hidden reasoning 67) | 5.89 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow has a bent shaft and a single arrowhead pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane arrow permits left turns and excludes straight
                      and right movements, but does not by itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow excludes straight movement.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow excludes a right turn.
    u_turn                    allowed         The left-turn arrow does not by itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 342 output (hidden reasoning 41) | 5.27 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white bent lane-use arrow with a single head pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane arrow requires a leftward movement rather than
                      straight or right travel, and does not by itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits going straight.
    turn_left                 allowed         The left-pointing arrow allows a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-turn arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 350 output (hidden reasoning 47) | 5.39 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A single white curved arrow with a clearly visible head pointing left is inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane-use arrow requires a leftward movement rather
                      than proceeding straight or turning right, and does not itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-turn arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 324 output (hidden reasoning 21) | 4.17 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a white curved arrow with a single arrowhead pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane arrow prohibits straight and right movements and
                      permits a left turn; the arrow alone does not prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-turn arrow alone does not prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 321 output (hidden reasoning 22) | 4.45 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a white curved arrow with a single arrowhead pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane-use arrow requires a leftward movement rather
                      than straight or right travel and does not by itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow permits turning left.
    turn_right                prohibited      The left-only arrow prohibits turning right.
    u_turn                    allowed         The left-turn arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 338 output (hidden reasoning 39) | 4.6 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a white bent lane-use arrow with a single head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow requires a left turn rather than
                      proceeding straight or turning right, but does not itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow allows a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-turn arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 299 output (hidden reasoning 0) | 3.48 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow with a curved shaft and a single head pointing left is visible
                      inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane arrow requires a leftward movement, prohibiting
                      straight and right movements but not by itself prohibiting a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-turn arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 347 output (hidden reasoning 41) | 6.7 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white curved lane-use arrow with a single head pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow requires a left turn rather than
                      proceeding straight or turning right, but does not itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow allows a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-only arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 301 output (hidden reasoning 0) | 3.35 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow inside the rectangle has a head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane arrow requires a left turn rather than a straight
                      or right movement, but does not by itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow allows a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-turn arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 336 output (hidden reasoning 37) | 4.25 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow inside the rectangle has a head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane arrow requires a leftward movement rather than
                      proceeding straight or turning right, but does not by itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow allows a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-turn arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 351 output (hidden reasoning 51) | 4.83 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a white lane-use arrow with a head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane arrow requires a left turn rather than proceeding
                      straight or turning right, but does not itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow allows a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-pointing arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 349 output (hidden reasoning 49) | 4.82 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single white curved lane-use arrow with its head pointing
                      left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow requires a left turn rather than
                      proceeding straight or turning right, but does not by itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-only arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 301 output (hidden reasoning 0) | 3.99 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white curved lane-use arrow with a clearly visible head pointing left is inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow requires a left turn rather than
                      proceeding straight or turning right, but does not by itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         A left-turn arrow does not by itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 303 output (hidden reasoning 0) | 3.76 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white curved lane-use arrow with a single clearly visible head pointing left is inside
                      the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow requires a left turn rather than
                      proceeding straight or turning right, but does not itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow allows a left turn.
    turn_right                prohibited      The left-only arrow prohibits turning right.
    u_turn                    allowed         The left-turn arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 301 output (hidden reasoning 0) | 3.18 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle shows a centre lane bordered on each side by a solid yellow line and a
                      broken yellow line, with white curved arrows pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane permits entering and waiting to turn
                      left, and turning left out of the centre lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The two-way left-turn lane permits turning left out of it.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering to wait for a left
                                              turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2584 input + 348 output (hidden reasoning 31) | 4.62 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle shows a centre lane bounded on each side by a solid yellow line and a
                      broken yellow line, with white curved left-turn arrows pointing in opposite travel
                      directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for and make a
                      left turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The two-way left-turn lane permits left turns out of the centre
                                              lane.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering to wait for a left
                                              turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2584 input + 332 output (hidden reasoning 15) | 4.25 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle shows a centre lane bounded on both sides by paired solid and broken
                      yellow lines, with two white curved left-turn arrows facing opposite travel directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for and make a
                      left turn, but is not a through-travel lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The two-way left-turn lane permits left turns out of the centre
                                              lane.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering to wait for a left
                                              turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2584 input + 349 output (hidden reasoning 26) | 4.18 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle shows two white curved arrows pointing in opposite directions within a
                      lane bordered on each side by a solid yellow line and a broken yellow line.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for and make a
                      left turn.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               not_applicable  not governed by this marking
    turn_left                 allowed         The two-way left-turn lane permits left turns out of the centre
                                              lane.
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering to wait for a left
                                              turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2584 input + 366 output (hidden reasoning 53) | 4.93 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle shows white curved arrows pointing in opposite directions within a lane
                      bordered on each side by a solid yellow line paired with a broken yellow line.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for and make a
                      left turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The two-way left-turn lane permits left turns out of the center
                                              lane.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering to wait for a left
                                              turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2584 input + 358 output (hidden reasoning 45) | 4.9 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two white curved arrows pointing in opposite directions,
                      between yellow boundaries on each side consisting of a solid outer line and a broken
                      inner line.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for and make a
                      left turn, rather than used as a through-travel lane.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               not_applicable  not governed by this marking
    turn_left                 allowed         The opposite-facing arrows and paired solid-and-broken yellow
                                              boundaries designate a lane for left turns.
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait allowed         The designated two-way left-turn lane permits entering to wait
                                              for a left turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2584 input + 387 output (hidden reasoning 57) | 5.9 s
```
