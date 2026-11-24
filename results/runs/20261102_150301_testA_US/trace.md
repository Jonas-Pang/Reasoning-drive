# Reasoning trace of run 20261102_150301_testA_US

```
fl_20261017_night_01_f0001950 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has a visible head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits travel straight from that
                      lane and restricts turns and U-turns.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               allowed         The straight-pointing arrow permits going straight.
    turn_left                 prohibited      The straight-only arrow restricts left turns.
    turn_right                prohibited      The straight-only arrow restricts right turns.
    u_turn                    prohibited      The straight-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 251 output (hidden reasoning 31) | 3.64 s
```

```
fl_20261017_night_01_f0001950 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has a head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits travel straight from that
                      lane and prohibits turning or making a U-turn from it.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               allowed         The straight-pointing arrow permits going straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 249 output (hidden reasoning 31) | 3.06 s
```

```
fl_20261017_night_01_f0001950 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white lane-use arrow inside the rectangle has a visible head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits travel straight from that
                      lane and prohibits turns and U-turns from it.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits travel straight.
    turn_left                 prohibited      The straight-only arrow does not permit a left turn.
    turn_right                prohibited      The straight-only arrow does not permit a right turn.
    u_turn                    prohibited      The straight-only arrow does not permit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 266 output (hidden reasoning 41) | 3.58 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white lane-use arrow inside the rectangle has one head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow directs traffic in that lane to
                      proceed straight rather than turn or make a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight-pointing arrow permits going straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a straight arrow, and only lane-use movements receive
                      applicable actions.
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 256 output (hidden reasoning 19) | 3.9 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has one head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-ahead lane-use arrow permits travel straight from that
                      lane and restricts turns and U-turns.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight-ahead arrow permits going straight.
    turn_left                 prohibited      The straight-ahead arrow restricts turning left.
    turn_right                prohibited      The straight-ahead arrow restricts turning right.
    u_turn                    prohibited      The straight-ahead arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a straight-ahead arrow, and only lane movements are governed.
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 332 output (hidden reasoning 19) | 4.0 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has one head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits travel straight from that
                      lane and prohibits turns and U-turns from it.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits going straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits making a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a straight arrow, only lane-use movements are governed, and
                      each action follows from the stated rule.
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 266 output (hidden reasoning 26) | 3.47 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          The rectangle contains several broad, solid white transverse stripes with dark gaps
                      between them.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, these stripes mark a pedestrian crosswalk, which drivers must
                      yield to pedestrians using, but the marking does not govern the six listed actions.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2659 input + 217 output (hidden reasoning 0) | 2.9 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          The rectangle contains several broad, solid white transverse stripes with dark gaps
                      between them.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, these stripes mark a pedestrian crosswalk, which requires drivers
                      to yield to pedestrians but does not itself govern any of the six listed actions.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2659 input + 217 output (hidden reasoning 0) | 3.11 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          The rectangle contains several broad, parallel white solid bars across the roadway.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, these white bars mark a pedestrian crosswalk, which requires
                      drivers to yield to pedestrians but does not itself determine any of the six listed
                      actions.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2659 input + 216 output (hidden reasoning 0) | 3.14 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single, unbroken yellow line is visible inside the rectangle to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line marking the left edge of the roadway may be
                      crossed when necessary; it does not by itself prohibit crossing.
Step 3  Decide
    cross_line                allowed         The visible solid yellow left-edge line does not prohibit
                                              crossing when necessary.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 286 output (hidden reasoning 61) | 3.58 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single, unbroken yellow line is visible inside the rectangle to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line marking the left edge of the roadway does not
                      by itself prohibit crossing it.
Step 3  Decide
    cross_line                allowed         The visible solid yellow edge line does not by itself prohibit
                                              crossing.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 299 output (hidden reasoning 81) | 3.86 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single solid yellow line is visible inside the rectangle, to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line marking the left edge of the roadway does not
                      by itself prohibit crossing it.
Step 3  Decide
    cross_line                allowed         The solid yellow left-edge line does not by itself prohibit
                                              crossing.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 270 output (hidden reasoning 53) | 4.52 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single, unbroken yellow line is visible inside the rectangle to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line marking the left edge of a divided roadway
                      separates the travel lane from the median and restricts crossing into it.
Step 3  Decide
    cross_line                prohibited      The solid yellow left-edge line restricts crossing into the
                                              median.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 314 output (hidden reasoning 88) | 3.87 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single unbroken yellow line runs along the left side of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line marking the left edge of the roadway restricts
                      crossing onto the area beyond that edge.
Step 3  Decide
    cross_line                prohibited      The solid yellow roadway-edge line restricts crossing it.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the type matches the visible line, and only cross_line is governed by it.
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 352 output (hidden reasoning 116) | 4.46 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken yellow line is visible to the left of my car inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line marking the left edge of a divided roadway
                      separates the travel lane from the median and prohibits crossing into the median.
Step 3  Decide
    cross_line                prohibited      The solid yellow left-edge line prohibits crossing into the
                                              median.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking type matches the visible line, and only crossing it is governed.
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 310 output (hidden reasoning 70) | 4.32 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken yellow line is visible to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line marking the left edge of the roadway does not
                      by itself prohibit crossing it.
Step 3  Decide
    cross_line                allowed         The solid yellow edge line does not by itself prohibit crossing.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 342 output (hidden reasoning 129) | 3.91 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single, unbroken yellow line is visible to the left of my car inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line marking the left edge of the roadway may be
                      crossed when it is safe to do so; it is not a no-passing centerline.
Step 3  Decide
    cross_line                allowed         The solid yellow left-edge line may be crossed when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the description matches the marking type, and only cross_line is governed.
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 368 output (hidden reasoning 123) | 4.79 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken yellow line is visible on the left side of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line marking the left edge of the roadway may be
                      crossed when needed; the edge line itself does not prohibit crossing.
Step 3  Decide
    cross_line                allowed         The visible solid yellow edge line does not prohibit crossing.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 340 output (hidden reasoning 120) | 4.51 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a faint, single pale line appears unbroken along the left side of
                      the pavement; its colour is too unclear to identify confidently.
    Evidence          partial
    Output 1          other, position left
Step 2  Rule          In the United States, whether this line may be crossed depends on what kind of line it
                      is, which the photo does not establish.
Step 3  Decide
    cross_line                not_determined  The line’s colour and type are unclear, so the crossing rule
                                              cannot be determined.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         The description and partial evidence reflect the unclear line; only crossing is
                      undecided, and the other actions are not governed.
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding; contradicts itself: other does not govern cross_line
Tokens                2659 input + 594 output (hidden reasoning 336) | 7.43 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single pale, apparently unbroken line is visible on the left, but the lighting makes
                      its colour unclear.
    Evidence          partial
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a solid white road-edge line marks the roadway boundary; crossing
                      it is generally permitted when necessary.
Step 3  Decide
    cross_line                not_determined  The line appears solid, but its colour is unclear, leaving the
                                              applicable crossing rule undecided.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         The uncertain colour makes the marking type tentative; crossing remains not_determined,
                      and the other actions are not_applicable.
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding
Tokens                2659 input + 459 output (hidden reasoning 208) | 6.35 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A faint, pale, apparently continuous line is visible along the left side of the road,
                      but the darkness makes its colour uncertain.
    Evidence          partial
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a solid white edge line marks the roadway edge and does not itself
                      prohibit crossing it.
Step 3  Decide
    cross_line                not_determined  The line appears continuous, but its uncertain colour leaves the
                                              applicable crossing rule undecided.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         The colour is uncertain, so the white-solid classification is tentative and crossing
                      remains not_determined; all other actions are not_applicable.
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding
Tokens                2659 input + 599 output (hidden reasoning 345) | 7.71 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Worn white pavement lettering is visible inside the rectangle, but its characters are
                      not fully legible.
    Evidence          partial
    Output 1          other, position in_ego_lane
Step 2  Rule          Pavement text may convey a lane instruction, but this worn lettering alone does not
                      establish a rule for any of the six listed actions.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 wrong (label arrow/straight_left); Output 2 wrong (go_straight: label allowed,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 395 output (hidden reasoning 176) | 5.92 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A worn white arrow is visible inside the rectangle, but its head and directions are too
                      obscured to identify reliably.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow governs which movements are permitted from its
                      lane, but the permitted directions cannot be determined without a legible arrow head.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The obscured arrow head leaves this movement undecided.
    turn_left                 not_determined  The obscured arrow head leaves this movement undecided.
    turn_right                not_determined  The obscured arrow head leaves this movement undecided.
    u_turn                    not_determined  The obscured arrow head leaves this movement undecided.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a partially legible arrow, and only the movements it governs
                      are not_determined.
Result                Output 1 wrong (label arrow/straight_left); Output 2 wrong (go_straight: label allowed,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 604 output (hidden reasoning 265) | 7.36 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A worn white pavement marking is visible inside the rectangle, but its shape is too
                      broken to identify a complete arrowhead or other deciding feature.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow restricts movements from its lane to the
                      directions shown by its arrowhead.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The worn arrowhead does not show whether it permits straight
                                              travel.
    turn_left                 not_determined  The worn arrowhead does not show whether it permits a left turn.
    turn_right                not_determined  The worn arrowhead does not show whether it permits a right
                                              turn.
    u_turn                    not_determined  The worn arrowhead does not show whether it permits a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the arrowhead is unclear, so governed movements are not determined and other
                      actions are not applicable.
Result                Output 1 wrong (label arrow/straight_left); Output 2 wrong (go_straight: label allowed,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 656 output (hidden reasoning 382) | 8.26 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from this side
                      to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 233 output (hidden reasoning 19) | 3.11 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from this side
                      to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow lines prohibit crossing to change lanes
                                              or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 235 output (hidden reasoning 22) | 3.14 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, a double solid yellow center line prohibits crossing it to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The visible double solid yellow line prohibits crossing to
                                              change lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the type matches the visible lines, and only crossing is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 260 output (hidden reasoning 27) | 3.41 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking type matches the visible lines, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 272 output (hidden reasoning 42) | 3.63 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle, to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow lines prohibit crossing to change lanes
                                              or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 259 output (hidden reasoning 42) | 3.25 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to pass or
                      change lanes, though crossing to turn left may be permitted.
Step 3  Decide
    cross_line                prohibited      The double solid yellow lines prohibit crossing to pass or
                                              change lanes.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 265 output (hidden reasoning 45) | 3.27 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 280 output (hidden reasoning 69) | 4.17 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow centerlines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 264 output (hidden reasoning 47) | 3.52 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing them from
                      either side to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is double solid yellow, and only crossing is governed by it.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 311 output (hidden reasoning 74) | 3.78 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from this lane
                      to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow lines prohibit crossing to change lanes
                                              or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the type matches the visible lines, and only the governed action has an
                      applicable result.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 257 output (hidden reasoning 26) | 3.33 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, a double solid yellow centerline prohibits crossing into the
                      opposing lane to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow centerline prohibits crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 256 output (hidden reasoning 40) | 3.42 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from this lane
                      to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 262 output (hidden reasoning 48) | 3.5 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle, to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      side to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the type matches the visible lines, and only crossing is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 251 output (hidden reasoning 16) | 3.23 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 255 output (hidden reasoning 44) | 3.3 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle, to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow lines prohibit crossing to change lanes
                                              or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 255 output (hidden reasoning 38) | 3.0 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle, to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The visible double solid yellow center lines prohibit crossing
                                              to change lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the type matches the visible lines, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 260 output (hidden reasoning 25) | 3.39 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the type matches the visible lines, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 319 output (hidden reasoning 87) | 3.89 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the type matches the visible lines, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 299 output (hidden reasoning 67) | 4.2 s
```

```
fl_20261017_night_01_f0012135 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, a double solid yellow center line prohibits crossing it to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center line prohibits crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 304 output (hidden reasoning 19) | 3.21 s
```

```
fl_20261017_night_01_f0012135 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      side to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking type matches the visible lines, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 258 output (hidden reasoning 22) | 3.24 s
```

```
fl_20261017_night_01_f0012135 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, a double solid yellow centre line prohibits crossing it to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow centre line prohibits crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 241 output (hidden reasoning 22) | 3.62 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The visible double solid yellow center lines prohibit crossing
                                              to change lanes or overtake.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 262 output (hidden reasoning 47) | 3.41 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, a double solid yellow center line prohibits crossing it from
                      either side.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center line prohibits crossing.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 235 output (hidden reasoning 25) | 3.35 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle, to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing them to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow lines prohibit crossing to change lanes
                                              or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is double solid yellow, and only crossing the line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 268 output (hidden reasoning 34) | 3.7 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow lines prohibit crossing to change lanes
                                              or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 296 output (hidden reasoning 80) | 4.57 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle, to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 292 output (hidden reasoning 74) | 4.51 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines are visible.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from this side
                      to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 296 output (hidden reasoning 81) | 3.87 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The visible double solid yellow lines prohibit crossing to
                                              change lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 289 output (hidden reasoning 72) | 3.88 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 301 output (hidden reasoning 90) | 4.11 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from this lane
                      to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow lines prohibit crossing to change lanes
                                              or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 258 output (hidden reasoning 45) | 3.21 s
```

```
fl_20261017_night_01_f0014235 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 262 output (hidden reasoning 48) | 3.53 s
```

```
fl_20261017_night_01_f0014235 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 286 output (hidden reasoning 69) | 4.32 s
```

```
fl_20261017_night_01_f0014235 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, a double solid yellow center line prohibits crossing to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center line prohibits crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the type matches the visible lines, and only cross_line is governed by this
                      marking.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 277 output (hidden reasoning 41) | 3.7 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white arrow inside the rectangle has a single head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight from
                      that lane and restricts turns and U-turns.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight-pointing arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow restricts left turns.
    turn_right                prohibited      The straight-only arrow restricts right turns.
    u_turn                    prohibited      The straight-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 252 output (hidden reasoning 33) | 4.52 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle is a white, single-headed arrow pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow permits travel in the direction shown and
                      restricts movements in other directions.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits travel straight ahead.
    turn_left                 prohibited      The straight arrow does not permit a left turn.
    turn_right                prohibited      The straight arrow does not permit a right turn.
    u_turn                    prohibited      The straight arrow does not permit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 243 output (hidden reasoning 26) | 3.68 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has one head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits travel straight from its
                      lane and restricts turns and U-turns.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight-pointing arrow permits going straight.
    turn_left                 prohibited      The straight-only arrow restricts left turns.
    turn_right                prohibited      The straight-only arrow restricts right turns.
    u_turn                    prohibited      The straight-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 245 output (hidden reasoning 26) | 3.49 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white arrow-shaped marking is visible inside the rectangle, but its head is too faint
                      to determine which direction it points.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow restricts movements from its lane to the
                      directions shown by its head.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The arrowhead is too faint to determine whether it permits
                                              straight travel.
    turn_left                 not_determined  The arrowhead is too faint to determine whether it permits a
                                              left turn.
    turn_right                not_determined  The arrowhead is too faint to determine whether it permits a
                                              right turn.
    u_turn                    not_determined  The arrowhead is too faint to determine whether it permits a
                                              U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 wrong (label other); Output 2 not scored; evidence group over_withholding
Tokens                2659 input + 717 output (hidden reasoning 464) | 8.98 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a worn white pavement marking is visible in my lane, but its
                      arrowhead is too faint to identify a direction.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow restricts movements from its lane to the
                      directions shown by its arrowhead.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               not_determined  The arrowhead is too faint to tell whether it permits going
                                              straight.
    turn_left                 not_determined  The arrowhead is too faint to tell whether it permits a left
                                              turn.
    turn_right                not_determined  The arrowhead is too faint to tell whether it permits a right
                                              turn.
    u_turn                    not_determined  The arrowhead is too faint to tell whether it permits a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         Consistent: the arrowhead is unclear, so governed movements are not determined and other
                      actions are not applicable.
Result                Output 1 wrong (label other); Output 2 not scored; evidence group over_withholding
Tokens                2659 input + 927 output (hidden reasoning 650) | 11.87 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, white painted segments run across the roadway, but their worn
                      edges do not show a clear arrowhead or a continuous line.
    Evidence          partial
    Output 1          other, position in_ego_lane
Step 2  Rule          These visible painted segments do not establish a lane-use direction or a longitudinal
                      line-crossing restriction.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the visible segments are classified as other, and none of the six actions is
                      governed by that classification.
Result                Output 1 correct (label other); Output 2 not scored; evidence group over_withholding
Tokens                2659 input + 897 output (hidden reasoning 658) | 12.05 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken white line is visible inside the rectangle, to the left of my car.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a single solid white lane line discourages crossing but does not
                      prohibit it.
Step 3  Decide
    cross_line                allowed         The visible solid white lane line discourages crossing but
                                              permits it.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2659 input + 281 output (hidden reasoning 67) | 3.49 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single continuous white line is visible inside the rectangle, to the left of my car.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          In the United States, crossing a single solid white lane line is discouraged but
                      generally permitted.
Step 3  Decide
    cross_line                allowed         The solid white lane line discourages but does not prohibit
                                              crossing.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2659 input + 266 output (hidden reasoning 55) | 3.37 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single solid white line is visible inside the rectangle, to the left of my car.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a solid white lane line discourages crossing but does not by
                      itself prohibit it.
Step 3  Decide
    cross_line                allowed         The solid white lane line discourages crossing but does not
                                              prohibit it.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2659 input + 279 output (hidden reasoning 64) | 3.7 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, a double solid yellow centerline prohibits crossing it to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow centerline prohibits crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the visible marking is a double solid yellow line, and only cross_line is
                      governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 288 output (hidden reasoning 54) | 3.54 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      side to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 272 output (hidden reasoning 52) | 3.47 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from this side
                      to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 298 output (hidden reasoning 78) | 3.83 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the type matches the visible double solid yellow lines, and only cross_line
                      is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 313 output (hidden reasoning 78) | 4.05 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle, to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to change lanes
                      or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 292 output (hidden reasoning 74) | 4.12 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, a double solid yellow center line prohibits crossing to change
                      lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The visible double solid yellow center line prohibits crossing
                                              to change lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is double solid yellow, and only cross_line is governed by it.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 296 output (hidden reasoning 60) | 3.71 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible on the left side of the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      side to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The visible double solid yellow center lines prohibit crossing
                                              to change lanes or overtake.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 552 output (hidden reasoning 261) | 6.56 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from my lane to
                      change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 430 output (hidden reasoning 210) | 5.56 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines run along the left side of my
                      lane.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from this lane
                      to pass or change lanes.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to pass
                                              or change lanes.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 341 output (hidden reasoning 122) | 3.97 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible on the left side of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing into opposing
                      traffic to change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 283 output (hidden reasoning 65) | 3.54 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible on the left side of my lane inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      side to change lanes or pass.
Step 3  Decide
    cross_line                prohibited      The double solid yellow lines prohibit crossing to change lanes
                                              or pass.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the description matches a double solid yellow line, and only cross_line is
                      governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 262 output (hidden reasoning 27) | 3.93 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible to the left of my car inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from my lane to
                      change lanes or overtake.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 250 output (hidden reasoning 30) | 3.25 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white line appears as separated dashes with visible gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and may be crossed when it is safe to do so.
Step 3  Decide
    cross_line                allowed         The broken white lane line may be crossed when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 257 output (hidden reasoning 38) | 3.96 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white broken line has visible dashes and gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing when safe.
Step 3  Decide
    cross_line                allowed         The visible broken white lane line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 286 output (hidden reasoning 74) | 4.06 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line with visible dashes and gaps lies to the left of my car.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing it when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a broken white line, and only cross_line is governed by it.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 263 output (hidden reasoning 30) | 3.82 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line is visible inside the rectangle, with two dashes separated by
                      a gap.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line permits crossing between lanes when it is
                      safe to do so.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 256 output (hidden reasoning 42) | 3.99 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line is visible inside the rectangle, with dashes separated by a
                      gap.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 263 output (hidden reasoning 49) | 3.26 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white line appears as separated dashes with a visible
                      gap.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 256 output (hidden reasoning 43) | 3.94 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single broken white line is visible inside the rectangle, with dashes separated by
                      gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line may be crossed to change lanes when it is
                      safe to do so.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 245 output (hidden reasoning 31) | 2.98 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white line appears as separate dashes with visible gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a dashed white lane line may be crossed to change lanes when it is
                      safe to do so.
Step 3  Decide
    cross_line                allowed         The visible dashed white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 244 output (hidden reasoning 30) | 3.12 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white line has visible dashes separated by gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a dashed white lane line permits crossing to change lanes when
                      safe.
Step 3  Decide
    cross_line                allowed         The dashed white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 233 output (hidden reasoning 27) | 3.48 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line is visible inside the rectangle, with dashes separated by
                      gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line permits crossing between lanes when it is
                      safe to do so.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 237 output (hidden reasoning 25) | 4.36 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white line has visible dashes separated by gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a dashed white lane line may be crossed when it is safe to change
                      lanes.
Step 3  Decide
    cross_line                allowed         The dashed white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the type matches the visible line, and only cross_line is governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 247 output (hidden reasoning 23) | 3.82 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line is visible inside the rectangle, with dashes separated by
                      gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line permits crossing between lanes when it is
                      safe to do so.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the visible marking is a white dashed line, and only cross_line is governed
                      by it.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 257 output (hidden reasoning 26) | 3.25 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white broken line shows a dash and a gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line permits crossing between lanes when it is
                      safe to do so.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 320 output (hidden reasoning 110) | 4.07 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white longitudinal dash and a gap below it are visible.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a dashed white lane line separates lanes traveling in the same
                      direction and permits crossing when safe.
Step 3  Decide
    cross_line                allowed         The dashed white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 360 output (hidden reasoning 148) | 5.14 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line is visible inside the rectangle, with a dash and a gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing to change lanes when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 290 output (hidden reasoning 74) | 3.86 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line is visible inside the rectangle, with a dash and a gap before
                      another short visible segment.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing to change lanes when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 307 output (hidden reasoning 86) | 3.98 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white line segment with a visible gap is inside the rectangle, to the right of
                      my car.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a dashed white lane line separates lanes traveling in the same
                      direction and permits crossing to change lanes when safe.
Step 3  Decide
    cross_line                allowed         The dashed white lane line permits crossing when safe.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 279 output (hidden reasoning 60) | 4.35 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white line segment is visible inside the rectangle, with a gap between its near
                      end and the bottom of the rectangle.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing to change lanes when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 282 output (hidden reasoning 59) | 3.84 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white line to the right of my car has a visible dash and
                      gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line permits crossing between lanes when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 262 output (hidden reasoning 52) | 4.03 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single broken white line with a visible dash and gap is to the right of my car.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line permits crossing between lanes when it is
                      safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 239 output (hidden reasoning 29) | 3.1 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white longitudinal line to the right of my car appears as separated dashes with
                      a visible gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line permits crossing between lanes when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 249 output (hidden reasoning 39) | 3.75 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A short white pavement marking is visible inside the rectangle, but it is too dark and
                      worn to make out an arrowhead or a complete line pattern.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow governs which directions a driver may take from
                      that lane, but its directions must be visible to determine the permitted movements.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The arrowhead is not visible, so this movement is undecided.
    turn_left                 not_determined  The arrowhead is not visible, so this movement is undecided.
    turn_right                not_determined  The arrowhead is not visible, so this movement is undecided.
    u_turn                    not_determined  The arrowhead is not visible, so this movement is undecided.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the possible arrow's directions are not visible, and only movements governed
                      by a lane-use arrow are undetermined.
Result                Output 1 wrong (label arrow/left); Output 2 wrong (go_straight: label prohibited,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 579 output (hidden reasoning 291) | 7.89 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A short white pavement marking is visible inside the rectangle, but its shape is too
                      unclear to identify an arrowhead or a line pattern.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow permits the movements it indicates and restricts
                      movements it does not indicate.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The unclear arrowhead leaves its indicated direction undecided.
    turn_left                 not_determined  The unclear arrowhead leaves its indicated direction undecided.
    turn_right                not_determined  The unclear arrowhead leaves its indicated direction undecided.
    u_turn                    not_determined  The unclear arrowhead leaves its indicated direction undecided.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the arrowhead is unclear, so governed movements are not determined and other
                      actions are not applicable.
Result                Output 1 wrong (label arrow/left); Output 2 wrong (go_straight: label prohibited,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 624 output (hidden reasoning 363) | 8.41 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A short white marking is visible inside the rectangle, but it is too small and unclear
                      to distinguish an arrowhead or a complete line pattern.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow restricts movements from its lane to the
                      directions shown by its arrowhead.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The arrowhead is unclear, so whether it shows straight is
                                              undecided.
    turn_left                 not_determined  The arrowhead is unclear, so whether it shows left is undecided.
    turn_right                not_determined  The arrowhead is unclear, so whether it shows right is
                                              undecided.
    u_turn                    not_determined  The arrowhead is unclear, so whether it permits a U-turn is
                                              undecided.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the possible arrowhead is unclear, so the governed movements are not
                      determined.
Result                Output 1 wrong (label arrow/left); Output 2 wrong (go_straight: label prohibited,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 645 output (hidden reasoning 368) | 8.3 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white lane-use arrow has a head pointing left and a shaft curving toward it.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane-use arrow directs traffic in that lane to turn
                      left at the next intersection rather than make another movement.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               prohibited      The left-turn arrow restricts the lane to a left turn.
    turn_left                 allowed         The arrow points left, allowing a left turn.
    turn_right                prohibited      The left-turn arrow restricts the lane to a left turn.
    u_turn                    prohibited      The left-turn arrow indicates a left turn, not a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 440 output (hidden reasoning 200) | 6.43 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white lane-use arrow inside the rectangle has one visible head pointing left and a
                      curved shaft.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane-use arrow directs traffic in that lane to turn
                      left; it does not by itself prohibit an otherwise legal U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-turn arrow does not permit going straight.
    turn_left                 allowed         The left-turn arrow permits turning left.
    turn_right                prohibited      The left-turn arrow does not permit turning right.
    u_turn                    allowed         The left-turn arrow does not by itself prohibit an otherwise
                                              legal U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2659 input + 387 output (hidden reasoning 152) | 5.65 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white lane-use arrow has one visible head pointing left and a shaft that curves toward
                      it.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow directs traffic in that lane to turn
                      left at the next intersection, rather than go straight, turn right, or make a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow does not permit going straight.
    turn_left                 allowed         The left-only arrow permits turning left.
    turn_right                prohibited      The left-only arrow does not permit turning right.
    u_turn                    prohibited      The left-only arrow does not indicate a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 321 output (hidden reasoning 83) | 4.03 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white single-headed arrow inside the rectangle points left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow restricts traffic in that lane to
                      turning left at the next intersection.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow restricts the lane to turning left.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow restricts the lane to turning left.
    u_turn                    prohibited      The left-only arrow does not authorize a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 293 output (hidden reasoning 70) | 3.97 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white lane-use arrow inside the rectangle has a visible head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow permits a left turn from its lane and
                      restricts straight travel, right turns, and U-turns.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow restricts straight travel.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow restricts right turns.
    u_turn                    prohibited      The left-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 332 output (hidden reasoning 105) | 4.65 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white lane-use arrow is visible inside the rectangle, with its head pointing
                      left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow requires traffic in that lane to turn
                      left at the next intersection.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow does not permit going straight.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow does not permit a right turn.
    u_turn                    prohibited      The left-only arrow does not permit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 355 output (hidden reasoning 129) | 4.89 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white lane-use arrow is visible inside the rectangle, with its head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane-use arrow directs traffic in that lane to turn
                      left rather than proceed straight, turn right, or make a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-pointing arrow directs traffic to turn left, not go
                                              straight.
    turn_left                 allowed         The left-pointing arrow directs traffic to turn left.
    turn_right                prohibited      The left-pointing arrow directs traffic to turn left, not right.
    u_turn                    prohibited      The left-pointing arrow does not permit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the described left-pointing arrow matches the marking type, and only lane-
                      use movements are governed.
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 529 output (hidden reasoning 265) | 6.79 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A worn white pavement marking is visible inside the rectangle, but its arrowhead and
                      direction are too faint to identify.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow governs which movements are permitted from its
                      lane, but its direction must be identifiable to apply that rule.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The arrowhead is too faint to determine whether it permits
                                              straight travel.
    turn_left                 not_determined  The arrowhead is too faint to determine whether it permits a
                                              left turn.
    turn_right                not_determined  The arrowhead is too faint to determine whether it permits a
                                              right turn.
    u_turn                    not_determined  The arrowhead is too faint to determine whether it permits a
                                              U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the arrow direction is unclear, so only its governed movements are
                      not_determined.
Result                Output 1 wrong (label arrow/left); Output 2 wrong (go_straight: label prohibited,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 530 output (hidden reasoning 255) | 6.95 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A faint white pavement marking is visible inside the rectangle, but its shape and any
                      arrowhead are too indistinct to identify.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow governs which movements may be made from its
                      lane, but its permitted directions cannot be determined without a visible arrowhead.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The arrowhead is indistinct, so this movement is undecided.
    turn_left                 not_determined  The arrowhead is indistinct, so this movement is undecided.
    turn_right                not_determined  The arrowhead is indistinct, so this movement is undecided.
    u_turn                    not_determined  The arrowhead is indistinct, so this movement is undecided.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the indistinct arrowhead leaves only arrow-governed movements undetermined.
Result                Output 1 wrong (label arrow/left); Output 2 wrong (go_straight: label prohibited,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 505 output (hidden reasoning 229) | 5.93 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has one head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane-use arrow requires a leftward movement; a U-turn
                      may also be made from that lane where otherwise permitted.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow does not permit going straight.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow does not permit a right turn.
    u_turn                    allowed         The left-turn arrow permits a U-turn where otherwise legal.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2659 input + 338 output (hidden reasoning 110) | 4.8 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow in the cyan rectangle has a head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow directs traffic in that lane to turn
                      left at the intersection rather than go straight, turn right, or make a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow does not permit going straight.
    turn_left                 allowed         The left-only arrow permits turning left.
    turn_right                prohibited      The left-only arrow does not permit turning right.
    u_turn                    prohibited      The left-only arrow does not indicate a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 442 output (hidden reasoning 211) | 5.51 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle is a single white lane-use arrow with one head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane-use arrow directs traffic in that lane to turn
                      left; the arrow alone does not prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow does not permit going straight.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow does not permit a right turn.
    u_turn                    allowed         The left-turn arrow alone does not prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2659 input + 336 output (hidden reasoning 106) | 4.63 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          The rectangle shows a centre lane with yellow lines on both sides: each side has a solid
                      line beside a broken line, and two white arrows point in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be used to wait for and make a left
                      turn, but not as a through-travel lane.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               not_applicable  not governed by this marking
    turn_left                 allowed         The two-way left-turn lane permits a left turn out of it.
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering it to wait for a
                                              left turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2659 input + 716 output (hidden reasoning 462) | 9.04 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two white arrows point in opposite directions, with yellow solid
                      and broken lines along both sides of the lane.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be used to wait for and make a left
                      turn, but not as a through-travel lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The two-way left-turn lane permits a left turn out of it.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering to wait for a left
                                              turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2659 input + 487 output (hidden reasoning 242) | 5.94 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a center lane has yellow line pairs on both sides, each with a
                      solid line and a broken line; two white arrows point in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for and make a
                      left turn, but is not a through-travel lane.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               not_applicable  not governed by this marking
    turn_left                 allowed         The two-way left-turn lane permits a left turn out of the center
                                              lane.
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering it to wait for a
                                              left turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2659 input + 362 output (hidden reasoning 106) | 4.75 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, yellow solid and broken lines border a lane containing two white
                      arrows pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for a left turn
                      and used to turn left out of the lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The two-way left-turn lane permits a left turn out of it.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering it to wait for a
                                              left turn.
Step 4  Check         Consistent: the marking type matches the visible lines and arrows, and only the two
                      governed actions are assigned outcomes.
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2659 input + 410 output (hidden reasoning 149) | 5.08 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a large white arrow points left and a smaller white arrow points
                      right; yellow solid and broken lines are visible along both sides.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for and make a
                      left turn, but not for through travel.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The two-way left-turn lane permits a left turn out of it.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering to wait for a left
                                              turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2659 input + 355 output (hidden reasoning 109) | 4.75 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, the lane has yellow solid and broken lines along both edges and
                      white arrows pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for and make a
                      left turn, but it is not a through-travel lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The two-way left-turn lane permits turning left from it.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering it to wait for a
                                              left turn.
Step 4  Check         consistent
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2659 input + 512 output (hidden reasoning 269) | 7.22 s
```
