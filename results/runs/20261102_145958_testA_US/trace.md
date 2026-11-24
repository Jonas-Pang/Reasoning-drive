# Reasoning trace of run 20261102_145958_testA_US

```
fl_20261017_night_01_f0001950 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has a visible head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight from
                      its lane at the next intersection and restricts turns and U-turns.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight-pointing arrow permits going straight.
    turn_left                 prohibited      The straight-only arrow restricts left turns.
    turn_right                prohibited      The straight-only arrow restricts right turns.
    u_turn                    prohibited      The straight-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 222 output (hidden reasoning 0) | 3.13 s
```

```
fl_20261017_night_01_f0001950 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has a visible head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight from
                      its lane at the next intersection and restricts turns and U-turns.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight-pointing arrow permits going straight.
    turn_left                 prohibited      The straight-only arrow restricts left turns.
    turn_right                prohibited      The straight-only arrow restricts right turns.
    u_turn                    prohibited      The straight-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 222 output (hidden reasoning 0) | 2.79 s
```

```
fl_20261017_night_01_f0001950 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has a visible head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-ahead lane-use arrow permits proceeding straight from
                      its lane and restricts turns and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight-ahead arrow permits proceeding straight.
    turn_left                 prohibited      The straight-ahead arrow restricts left turns.
    turn_right                prohibited      The straight-ahead arrow restricts right turns.
    u_turn                    prohibited      The straight-ahead arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 225 output (hidden reasoning 0) | 2.77 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white arrow inside the rectangle has one head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight from
                      that lane and prohibits turning left, turning right, or making a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight-pointing arrow permits going straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits making a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 219 output (hidden reasoning 0) | 2.83 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white arrow inside the rectangle has one head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight from
                      that lane and prohibits turning left, turning right, or making a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits making a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 217 output (hidden reasoning 0) | 4.02 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white arrow inside the rectangle has one head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight from
                      its lane and prohibits turning left, turning right, or making a U-turn from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight-pointing arrow permits going straight.
    turn_left                 prohibited      The straight-only arrow prohibits turning left.
    turn_right                prohibited      The straight-only arrow prohibits turning right.
    u_turn                    prohibited      The straight-only arrow prohibits making a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 222 output (hidden reasoning 0) | 2.88 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          The rectangle contains several broad, solid white transverse stripes separated by dark
                      gaps.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, these stripes mark a pedestrian crosswalk, which drivers must keep
                      clear for pedestrians; this marking does not govern any of the six listed actions.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the described stripes are classified as other, and all six actions are not
                      applicable.
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2659 input + 234 output (hidden reasoning 0) | 3.05 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          The rectangle contains several broad, parallel white bars separated by dark pavement,
                      with a continuous white bar across their near ends.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, these crosswalk markings designate a pedestrian crossing and do
                      not themselves govern any of the six listed vehicle actions.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the described crosswalk is classified as other, and all six actions are not
                      applicable.
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2659 input + 237 output (hidden reasoning 0) | 2.97 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          The rectangle contains several broad, solid white transverse stripes separated by dark
                      pavement.
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
Step 4  Check         Consistent: the described stripes are an other marking, and all six actions are not
                      applicable.
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2659 input + 233 output (hidden reasoning 0) | 3.27 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken yellow line is visible to the left of my car inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line at the left edge of the roadway marks its
                      boundary and does not itself prohibit crossing it.
Step 3  Decide
    cross_line                allowed         The solid yellow edge line does not itself prohibit crossing.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a single solid yellow line, and only crossing it is governed.
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 233 output (hidden reasoning 0) | 3.06 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken yellow line is visible to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line at the left edge of the roadway marks its
                      boundary and restricts crossing it for a lane change or overtaking.
Step 3  Decide
    cross_line                prohibited      The solid yellow left-edge line restricts crossing it for a lane
                                              change or overtaking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a single solid yellow line, and only crossing it is governed.
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 243 output (hidden reasoning 0) | 3.18 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken yellow line is visible inside the rectangle to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a solid yellow line marking the left edge of a divided roadway may
                      be crossed when necessary, so it does not itself prohibit crossing.
Step 3  Decide
    cross_line                allowed         The solid yellow left-edge line does not itself prohibit
                                              crossing.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 221 output (hidden reasoning 0) | 3.61 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single unbroken yellow line runs along the left side of my lane.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow center line discourages crossing to pass but
                      does not prohibit crossing when safe.
Step 3  Decide
    cross_line                allowed         The single solid yellow line discourages but does not prohibit
                                              crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 218 output (hidden reasoning 0) | 2.81 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single unbroken yellow line runs along the left side of my lane.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow center line discourages crossing to pass but
                      does not categorically prohibit crossing it.
Step 3  Decide
    cross_line                allowed         The single solid yellow line discourages, but does not prohibit,
                                              crossing.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 219 output (hidden reasoning 0) | 2.97 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken yellow line runs along the left side of my lane inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow center line marks opposing traffic and
                      generally permits crossing to pass when safe, unless another restriction applies.
Step 3  Decide
    cross_line                allowed         A single solid yellow center line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 217 output (hidden reasoning 0) | 3.79 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single unbroken yellow line runs along the left side of the
                      car's lane.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow center line restricts crossing it to pass,
                      but permits crossing it to turn left when safe.
Step 3  Decide
    cross_line                prohibited      The solid yellow center line restricts crossing it to change
                                              lanes or overtake.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 226 output (hidden reasoning 0) | 3.06 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken yellow line is visible inside the rectangle to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow center line marks the boundary with opposing
                      traffic and prohibits crossing it to pass, though it may be crossed to turn left when
                      safe.
Step 3  Decide
    cross_line                prohibited      The solid yellow center line prohibits crossing to change lanes
                                              or overtake.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 228 output (hidden reasoning 0) | 2.77 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken yellow line is visible to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow line marking the left edge of a roadway may
                      be crossed when necessary and safe.
Step 3  Decide
    cross_line                allowed         The solid yellow left-edge line permits crossing when necessary
                                              and safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 213 output (hidden reasoning 0) | 2.6 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A faint, single, unbroken light-colored line is visible inside the rectangle, but its
                      color is too unclear to identify confidently.
    Evidence          partial
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a solid white line at the left edge of a roadway marks its
                      boundary and does not itself prohibit crossing.
Step 3  Decide
    cross_line                not_determined  The line's color is unclear, so the applicable crossing rule
                                              cannot be determined.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Corrected the crossing decision to not_determined because the line's color is unclear;
                      all other actions are not_applicable.
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding
Tokens                2659 input + 253 output (hidden reasoning 0) | 3.56 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single faint, unbroken white line is visible inside the rectangle to the left of the
                      car.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a solid white lane line discourages crossing but does not prohibit
                      it.
Step 3  Decide
    cross_line                allowed         The solid white lane line discourages crossing but permits it.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2659 input + 211 output (hidden reasoning 0) | 5.62 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A faint single light-colored line runs along the left side of the road, but its color
                      and whether it is solid or broken are too unclear to determine.
    Evidence          partial
    Output 1          white_solid, position left
Step 2  Rule          In the United States, crossing an edge line is generally permitted when necessary and
                      safe, but the line's type must be identifiable to apply that rule here.
Step 3  Decide
    cross_line                not_determined  The line's color and pattern are too unclear to determine the
                                              applicable crossing rule.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         The marking type was corrected to other because its color and pattern cannot be
                      identified; crossing remains undecided.
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding
Tokens                2659 input + 259 output (hidden reasoning 0) | 3.69 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle is a worn white lane-use arrow; its right-pointing head is visible,
                      but the worn upper portion does not clearly show whether it also points straight.
    Evidence          partial
    Output 1          arrow / right, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow permits the movements it indicates and prohibits
                      movements it does not indicate.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The worn upper portion leaves a straight-pointing head
                                              undecided.
    turn_left                 prohibited      No left-pointing head is visible; the arrow does not indicate a
                                              left turn.
    turn_right                allowed         The visible right-pointing head indicates a right turn.
    u_turn                    prohibited      No U-turn head is visible; the arrow does not indicate a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the visible right-pointing head supports a right turn, while wear leaves
                      straight travel undecided.
Result                Output 1 wrong (label arrow/straight_left); Output 2 wrong (go_straight: label allowed,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding; UNSAFE: turn_right
Tokens                2659 input + 274 output (hidden reasoning 0) | 3.66 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle is a worn white lane-use arrow in my lane; its right-pointing head
                      is visible, but the worn upper portion does not clearly show whether it also points
                      straight.
    Evidence          partial
    Output 1          arrow / right, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow permits the movements it indicates and prohibits
                      movements it does not indicate.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The worn upper portion hides whether a straight arrowhead is
                                              present.
    turn_left                 not_determined  No left-pointing arrowhead is visible, but wear leaves its
                                              absence uncertain.
    turn_right                allowed         The visible right-pointing arrowhead permits a right turn.
    u_turn                    not_determined  No U-turn indication is visible, but wear leaves its absence
                                              uncertain.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the arrow is worn, so movements dependent on its hidden features remain
                      undetermined.
Result                Output 1 wrong (label arrow/straight_left); Output 2 wrong (go_straight: label allowed,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding; UNSAFE: turn_right
Tokens                2659 input + 274 output (hidden reasoning 0) | 3.51 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle is a worn white lane-use arrow; its right-pointing head is visible,
                      but the worn upper portion does not clearly show whether it also points straight.
    Evidence          partial
    Output 1          arrow / right, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow permits travel in its indicated direction and
                      restricts movements in directions it does not indicate.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The worn upper portion leaves a straight-pointing head
                                              undecided.
    turn_left                 prohibited      The visible right-pointing head does not indicate a left turn.
    turn_right                allowed         The visible right-pointing head permits a right turn.
    u_turn                    prohibited      The visible right-pointing head does not indicate a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the arrow is worn, so straight travel is undetermined; only lane-use
                      movements are governed.
Result                Output 1 wrong (label arrow/straight_left); Output 2 wrong (go_straight: label allowed,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding; UNSAFE: turn_right
Tokens                2659 input + 272 output (hidden reasoning 0) | 3.35 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines run along the road to the left
                      of my car.
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
Step 4  Check         Consistent: the marking type matches the visible lines, and only the governed action has
                      an applicable result.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 240 output (hidden reasoning 0) | 2.9 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel yellow lines appear solid and unbroken.
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
Step 4  Check         Consistent: the type matches the visible lines, and only the governed action has an
                      applicable result.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 231 output (hidden reasoning 0) | 2.95 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel yellow lines run continuously without visible breaks.
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
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 213 output (hidden reasoning 0) | 2.94 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      side to pass or change lanes.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to pass
                                              or change lanes.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is double solid yellow, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 231 output (hidden reasoning 0) | 2.83 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      side to pass or change lanes.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to pass
                                              or change lanes.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is double solid yellow, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 231 output (hidden reasoning 0) | 2.86 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6-sol | repeat 3
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
Step 4  Check         Consistent: the marking type matches the visible lines, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 234 output (hidden reasoning 0) | 2.74 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle, to the left of my
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
Step 4  Check         Consistent: the marking type matches the visible lines, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 235 output (hidden reasoning 0) | 3.0 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel solid yellow lines are visible to the left of my car.
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
Step 4  Check         Consistent: the marking is double solid yellow, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 232 output (hidden reasoning 0) | 2.73 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel solid yellow lines are visible to the left of my car.
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
Tokens                2659 input + 230 output (hidden reasoning 0) | 2.9 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
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
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 212 output (hidden reasoning 0) | 2.86 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, a double solid yellow centerline prohibits crossing from either
                      side to pass or change lanes.
Step 3  Decide
    cross_line                prohibited      The double solid yellow centerline prohibits crossing to pass or
                                              change lanes.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 211 output (hidden reasoning 0) | 2.63 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from the
                      adjacent lane to change lanes or overtake.
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
Tokens                2659 input + 213 output (hidden reasoning 0) | 2.95 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6-sol | repeat 1
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
Step 4  Check         Consistent: the marking is double solid yellow, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 233 output (hidden reasoning 0) | 2.68 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6-sol | repeat 2
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
Step 4  Check         Consistent: the marking is double solid yellow, and only cross_line is governed by it.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 235 output (hidden reasoning 0) | 2.82 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
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
Step 4  Check         Consistent: the marking is double solid yellow, and only crossing is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 226 output (hidden reasoning 0) | 2.94 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6-sol | repeat 1
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
Tokens                2659 input + 218 output (hidden reasoning 0) | 2.57 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6-sol | repeat 2
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
Step 4  Check         Consistent: the marking type matches the visible lines, and only the governed action has
                      an applicable result.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 237 output (hidden reasoning 0) | 2.89 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from the
                      adjacent lane.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 201 output (hidden reasoning 0) | 2.6 s
```

```
fl_20261017_night_01_f0012135 | Test A | gpt-6-sol | repeat 1
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
Step 4  Check         Consistent: the marking type matches the visible lines, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 235 output (hidden reasoning 0) | 9.47 s
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
Tokens                2659 input + 234 output (hidden reasoning 0) | 2.86 s
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
Step 4  Check         Consistent: the marking type matches the visible lines, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 233 output (hidden reasoning 0) | 3.28 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines are visible to the left of my
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
Step 4  Check         Consistent: the description matches the marking type, and only the governed action has
                      an applicable result.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 237 output (hidden reasoning 0) | 3.84 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel yellow lines appear unbroken, with no visible gaps.
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
Step 4  Check         Consistent: the marking type matches the visible lines, and only crossing is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 231 output (hidden reasoning 0) | 3.28 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel yellow lines appear unbroken, with no visible gaps.
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
Step 4  Check         Consistent: the marking type matches the visible lines, and only crossing is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 231 output (hidden reasoning 0) | 4.67 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel yellow lines are visible: one is unbroken, and the
                      other has a visible dash and gap.
    Evidence          full
    Output 1          yellow_solid_dashed, position left
Step 2  Rule          In the United States, a solid-and-broken yellow centerline permits crossing from the
                      broken-line side but prohibits crossing from the solid-line side.
Step 3  Decide
    cross_line                prohibited      The line nearest my lane is solid, so crossing it is prohibited.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 wrong (label yellow_double_solid); Output 2 correct; evidence group wrong
Tokens                2659 input + 232 output (hidden reasoning 0) | 2.84 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines are visible to the left of my
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
Step 4  Check         Consistent: the marking is double solid yellow, and only crossing it is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 234 output (hidden reasoning 0) | 2.73 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines are visible to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      side to pass or change lanes.
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
Tokens                2659 input + 217 output (hidden reasoning 0) | 2.96 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel yellow lines run continuously without visible breaks
                      to the left of my car.
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
Step 4  Check         Consistent: the marking type matches the visible lines, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 235 output (hidden reasoning 0) | 3.61 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel yellow lines run continuously without visible breaks
                      to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      side to pass or change lanes.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to pass
                                              or change lanes.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is double solid yellow, and only cross_line is governed by it.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 234 output (hidden reasoning 0) | 3.44 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6-sol | repeat 3
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
Step 4  Check         Consistent: the marking is double solid yellow, and only crossing is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 232 output (hidden reasoning 0) | 2.69 s
```

```
fl_20261017_night_01_f0014235 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines run along the left side of my
                      car's lane.
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
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 221 output (hidden reasoning 0) | 2.95 s
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
Step 4  Check         Consistent: the marking is double solid yellow, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 233 output (hidden reasoning 0) | 3.45 s
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
Step 4  Check         Consistent: the description matches the marking type, and only cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 233 output (hidden reasoning 0) | 2.66 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has a head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight from
                      that lane and restricts turns and U-turns from it.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow restricts left turns.
    turn_right                prohibited      The straight-only arrow restricts right turns.
    u_turn                    prohibited      The straight-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 217 output (hidden reasoning 0) | 2.79 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white arrow inside the rectangle has a head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight from
                      that lane and restricts turns and U-turns.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               allowed         The straight arrow permits proceeding straight.
    turn_left                 prohibited      The straight-only arrow restricts left turns.
    turn_right                prohibited      The straight-only arrow restricts right turns.
    u_turn                    prohibited      The straight-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 215 output (hidden reasoning 0) | 2.72 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white lane-use arrow inside the rectangle has a head pointing straight ahead.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          In the United States, a straight-only lane-use arrow permits proceeding straight from
                      that lane and restricts turns and U-turns from it.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               allowed         The straight-pointing arrow permits going straight.
    turn_left                 prohibited      The straight-only arrow restricts left turns.
    turn_right                prohibited      The straight-only arrow restricts right turns.
    u_turn                    prohibited      The straight-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2659 input + 221 output (hidden reasoning 0) | 2.86 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel solid yellow lines border a central paved area, with
                      a short white marking visible within it.
    Evidence          partial
    Output 1          two_way_left_turn_lane, position left
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for a left turn
                      and used to turn left out of it, but not for through travel.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               not_applicable  not governed by this marking
    turn_left                 allowed         The centre lane permits turning left out of it.
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait allowed         The centre lane permits entering to wait for a left turn.
Step 4  Check         consistent
Result                Output 1 wrong (label other); Output 2 not scored; evidence group over_withholding
Tokens                2659 input + 235 output (hidden reasoning 0) | 2.92 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel solid yellow lines border a central paved area, with
                      a broken yellow line visible beside each solid line.
    Evidence          full
    Output 1          two_way_left_turn_lane, position left
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for a left turn
                      and used to turn left out of the lane, but not for through travel.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The two-way left-turn lane permits turning left out of it.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering it to wait for a
                                              left turn.
Step 4  Check         Consistent: the described paired solid-and-broken yellow edges identify the lane, and
                      only its two governed actions are assigned outcomes.
Result                Output 1 wrong (label other); Output 2 not scored; evidence group wrong
Tokens                2659 input + 269 output (hidden reasoning 0) | 3.57 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel solid yellow lines border a center lane on the left,
                      and a solid and a broken yellow line border it on the right; the broken line has a
                      visible dash and gap.
    Evidence          full
    Output 1          two_way_left_turn_lane, position left
Step 2  Rule          In the United States, a two-way left-turn lane may be entered to wait for a left turn
                      and used to turn left out of it, but not for through travel.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The center lane may be used to turn left out of it.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The center lane may be entered to wait for a left turn.
Step 4  Check         Corrected the description to identify the visible center-lane boundaries; the marking
                      type and actions are consistent.
Result                Output 1 wrong (label other); Output 2 not scored; evidence group wrong
Tokens                2659 input + 275 output (hidden reasoning 0) | 3.45 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single unbroken white line runs along the left side of my lane inside the rectangle.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a single solid white lane line discourages crossing but does not
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
Tokens                2659 input + 213 output (hidden reasoning 0) | 3.18 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single continuous white line runs along the left side of my lane inside the rectangle.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a single solid white lane line discourages crossing but does not
                      prohibit it.
Step 3  Decide
    cross_line                allowed         The solid white lane line discourages crossing but permits it.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a solid white line, and only crossing it is governed.
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2659 input + 225 output (hidden reasoning 0) | 2.99 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single solid white line runs along the left side of the car's lane inside the
                      rectangle.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          In the United States, a single solid white lane line discourages crossing but does not
                      prohibit it.
Step 3  Decide
    cross_line                allowed         The solid white lane line discourages crossing but permits it.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2659 input + 211 output (hidden reasoning 0) | 3.47 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6-sol | repeat 1
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
    cross_line                prohibited      The double solid yellow lines prohibit crossing to change lanes
                                              or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking type matches the visible lines, and only the governed action has
                      an applicable result.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 236 output (hidden reasoning 0) | 3.19 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines are visible to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      side to pass or change lanes.
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
Tokens                2659 input + 217 output (hidden reasoning 0) | 3.78 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines run along the left side of my
                      lane.
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
Tokens                2659 input + 219 output (hidden reasoning 0) | 3.46 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines run along the left side of my
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
Step 4  Check         Consistent: the type matches the visible double solid yellow lines, and only cross_line
                      is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 237 output (hidden reasoning 0) | 3.01 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines run along the left side of my
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
Step 4  Check         Consistent: the type matches the visible double solid yellow lines, and only cross_line
                      is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 237 output (hidden reasoning 0) | 2.84 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines run along the left side of my
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
Step 4  Check         Consistent: the type matches the visible double solid yellow lines, and only cross_line
                      is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 237 output (hidden reasoning 0) | 3.17 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines are visible to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to pass or
                      change lanes.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to pass
                                              or change lanes.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking type matches the visible lines, and only crossing is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 229 output (hidden reasoning 0) | 3.09 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines are visible to the left of my
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
Step 4  Check         Consistent: the type matches the visible lines, and only the governed action has an
                      applicable result.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 237 output (hidden reasoning 0) | 2.77 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines are visible to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing to overtake or
                      change lanes.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to
                                              overtake or change lanes.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking type matches the visible lines, and only crossing is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 231 output (hidden reasoning 0) | 2.95 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible to the left of my car.
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
Tokens                2659 input + 231 output (hidden reasoning 0) | 2.75 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Two parallel, unbroken yellow lines are visible inside the rectangle to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow center lines prohibit crossing from either
                      direction, except for a permitted left turn into a driveway or side road.
Step 3  Decide
    cross_line                prohibited      The double solid yellow center lines prohibit crossing to change
                                              lanes or overtake.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the visible double solid yellow lines match the marking type, and only
                      cross_line is governed.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 244 output (hidden reasoning 0) | 3.04 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two parallel, unbroken yellow lines are visible to the left of my
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
Step 4  Check         Consistent: the marking type matches the visible lines, and only the governed action has
                      an applicable result.
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2659 input + 238 output (hidden reasoning 0) | 3.07 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken longitudinal line is visible to the left of my car, with a dash
                      and a gap inside the rectangle.
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
Step 4  Check         Consistent: the marking type matches the visible line, and only crossing is governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 234 output (hidden reasoning 0) | 3.06 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken longitudinal line is visible, with a dash and a gap inside the
                      rectangle.
    Evidence          full
    Output 1          white_dashed, position left
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
Tokens                2659 input + 206 output (hidden reasoning 0) | 3.0 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken longitudinal line is visible to the left of my car, with a dash
                      and a gap inside the rectangle.
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
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 219 output (hidden reasoning 0) | 3.18 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white line appears in separated segments, with a visible
                      gap between them.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing to change lanes when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the description matches a white dashed line, and only crossing it is
                      governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 232 output (hidden reasoning 0) | 2.96 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white line appears in separated segments, with a visible
                      gap between them.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          In the United States, a dashed white lane line separates lanes traveling in the same
                      direction and permits crossing it to change lanes when safe.
Step 3  Decide
    cross_line                allowed         The dashed white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the description matches a dashed white line, and only crossing it is
                      governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 233 output (hidden reasoning 0) | 2.97 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white longitudinal line appears in separated segments
                      with a visible gap.
    Evidence          full
    Output 1          white_dashed, position left
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
Tokens                2659 input + 214 output (hidden reasoning 0) | 2.73 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line is visible inside the rectangle, with dashes and gaps.
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
Step 4  Check         Consistent: the type matches the visible line, and only crossing is governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 224 output (hidden reasoning 0) | 2.87 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line is visible inside the rectangle, with dashes separated by
                      gaps.
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
Step 4  Check         Consistent: the description matches a white dashed line, and only crossing it is
                      governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 228 output (hidden reasoning 0) | 2.87 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line is visible inside the rectangle, with dashes and gaps.
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
Step 4  Check         Consistent: the marking is a broken white line, and only crossing it is governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 227 output (hidden reasoning 0) | 3.95 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken longitudinal line with visible dashes and gaps lies to the left of
                      my car.
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
Step 4  Check         Consistent: the type matches the visible line, and only crossing is governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 228 output (hidden reasoning 0) | 3.67 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white broken line with visible dashes and gaps lies to the left of my car.
    Evidence          full
    Output 1          white_dashed, position left
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
Tokens                2659 input + 206 output (hidden reasoning 0) | 2.46 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white longitudinal line has visible dashes separated by
                      gaps to the left of my car's lane.
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
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 219 output (hidden reasoning 0) | 2.78 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a short white dash and a separate small white segment are visible,
                      with a gap between them; the marking is to the right of my car.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing it when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 227 output (hidden reasoning 0) | 3.1 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a short white dash and a separate small white segment are visible,
                      with a gap between them.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing it when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 217 output (hidden reasoning 0) | 2.81 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white dash is visible, with dark pavement before and
                      after it.
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
Tokens                2659 input + 215 output (hidden reasoning 0) | 4.37 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a white longitudinal line appears as one dash with a visible gap
                      beyond it.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing it when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 213 output (hidden reasoning 0) | 2.97 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white longitudinal line appears as a dash with a visible
                      gap beyond it.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing it when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the described white dash and gap match the marking type, and only crossing
                      is governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 232 output (hidden reasoning 0) | 2.9 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white line segment is visible, but no gap or second
                      segment is visible to establish whether it is broken or solid.
    Evidence          partial
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line permits crossing between lanes, while a
                      solid white lane line discourages crossing but does not itself prohibit it.
Step 3  Decide
    cross_line                allowed         Whether the line is broken or solid is hidden, but crossing is
                                              permitted or only discouraged in either case.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Corrected the evidence to partial because no gap is visible; the crossing decision is
                      unchanged, and all other actions are not applicable.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group over_withholding
Tokens                2659 input + 265 output (hidden reasoning 0) | 3.41 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a single white longitudinal line to the right of my car has a
                      visible dash and gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing it to change lanes when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing to change lanes when
                                              safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking type matches the visible line, and only crossing is governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 237 output (hidden reasoning 0) | 2.91 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white longitudinal line to the right of my car has a visible dash and gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a visible broken white line, and only crossing it is
                      governed.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 228 output (hidden reasoning 0) | 2.96 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a white longitudinal line to the right of my car has a visible
                      dash and gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a broken white lane line separates lanes traveling in the same
                      direction and permits crossing it when safe.
Step 3  Decide
    cross_line                allowed         The broken white lane line permits crossing when safe.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the described white dashed line governs only crossing, and the reasons match
                      the actions.
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2659 input + 232 output (hidden reasoning 0) | 2.91 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a white pavement arrow in my lane has a visible head pointing
                      left; no other arrowhead is visible.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn-only lane arrow permits a left turn and restricts
                      other movements from that lane at the next intersection.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-pointing arrow restricts going straight.
    turn_left                 allowed         The left-pointing arrow permits turning left.
    turn_right                prohibited      The left-pointing arrow restricts turning right.
    u_turn                    prohibited      The left-pointing arrow restricts a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a left arrow, and only movements governed by a lane-use arrow
                      receive allowed or prohibited actions.
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 256 output (hidden reasoning 0) | 3.33 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a white marking in my lane shows a horizontal arrowhead pointing
                      left; the rest of the arrow is too dark to make out.
    Evidence          partial
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow permits the indicated movement and restricts
                      movements not indicated by the arrow.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The obscured part of the arrow could contain another direction.
    turn_left                 allowed         The visible left-pointing head permits a left turn.
    turn_right                not_determined  The obscured part of the arrow could contain another direction.
    u_turn                    not_determined  The obscured part of the arrow could contain another direction.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the visible left-pointing head supports a left turn, while the obscured
                      portion leaves other directions undecided.
Result                Output 1 correct (label arrow/left); Output 2 wrong (go_straight: label prohibited,
                      turn_right: label prohibited, u_turn: label allowed); evidence group over_withholding
Tokens                2659 input + 266 output (hidden reasoning 0) | 3.65 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a white marking in my lane shows a horizontal bar, but its
                      arrowhead is not visible.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow restricts movements from its lane to the
                      directions shown by its arrowhead.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The arrowhead is not visible, so whether it permits straight
                                              travel is undecided.
    turn_left                 not_determined  The arrowhead is not visible, so whether it permits a left turn
                                              is undecided.
    turn_right                not_determined  The arrowhead is not visible, so whether it permits a right turn
                                              is undecided.
    u_turn                    not_determined  The arrowhead is not visible, so whether it permits a U-turn is
                                              undecided.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the arrowhead is hidden, so only the governed movements are not_determined.
Result                Output 1 wrong (label arrow/left); Output 2 wrong (go_straight: label prohibited,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 280 output (hidden reasoning 0) | 3.3 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white pavement arrow has a visible head pointing left and a curved shaft; no
                      other arrowhead is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn-only lane-use arrow permits a left turn and restricts
                      straight travel, right turns, and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow restricts straight travel.
    turn_left                 allowed         The left-only arrow permits a left turn.
    turn_right                prohibited      The left-only arrow restricts right turns.
    u_turn                    prohibited      The left-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 236 output (hidden reasoning 0) | 3.14 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white pavement arrow has a visible head pointing left and a curved shaft; no
                      other arrowhead is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn-only lane-use arrow permits a left turn and restricts
                      straight travel, right turns, and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow restricts straight travel.
    turn_left                 allowed         The left-only arrow permits a left turn.
    turn_right                prohibited      The left-only arrow restricts right turns.
    u_turn                    prohibited      The left-only arrow restricts U-turns.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 236 output (hidden reasoning 0) | 2.93 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white lane-use arrow inside the rectangle has a visible head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-only lane-use arrow directs traffic in that lane to turn
                      left at the next intersection, not to proceed straight, turn right, or make a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow does not permit going straight.
    turn_left                 allowed         The left-pointing arrow directs traffic to turn left.
    turn_right                prohibited      The left-only arrow does not permit turning right.
    u_turn                    prohibited      The left-only arrow does not permit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 236 output (hidden reasoning 0) | 3.17 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle is a white lane-use arrow with a visible head pointing left and a
                      shaft extending to the right; no other arrowhead is visible.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn-only lane-use arrow permits a left turn and restricts
                      straight travel, right turns, and U-turns from that lane.
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
Tokens                2659 input + 241 output (hidden reasoning 0) | 2.91 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle is a white lane-use arrow with a visible head pointing left and a
                      shaft extending straight ahead.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow permits travel only in the direction indicated by
                      its head, so this arrow permits a left turn and restricts other movements at the
                      intersection.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The arrow points left, so going straight is prohibited.
    turn_left                 allowed         The arrow points left, so turning left is allowed.
    turn_right                prohibited      The arrow points left, so turning right is prohibited.
    u_turn                    prohibited      The arrow points left, not in a U-turn direction, so a U-turn is
                                              prohibited.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the arrow type matches its visible head, and only movements governed by the
                      arrow receive action decisions.
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 270 output (hidden reasoning 0) | 3.4 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle is a white lane-use arrow with a visible head pointing left and a
                      shaft extending to the right; no other arrowhead is visible.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane-use arrow restricts traffic in that lane to
                      turning left at the next intersection.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-turn arrow restricts the lane to turning left.
    turn_left                 allowed         The left-turn arrow permits turning left.
    turn_right                prohibited      The left-turn arrow restricts the lane to turning left.
    u_turn                    prohibited      The left-turn arrow restricts the lane to turning left.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the visible left arrow matches the marking type, and only lane-use movements
                      receive applicable actions.
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 258 output (hidden reasoning 0) | 3.34 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A white pavement marking is visible inside the rectangle, but its arrowhead is too faint
                      to make out its direction.
    Evidence          partial
    Output 1          arrow, position in_ego_lane
Step 2  Rule          In the United States, a lane-use arrow restricts movements from its lane to the
                      directions shown by its arrowhead.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_determined  The arrowhead direction is too faint to determine whether it
                                              permits going straight.
    turn_left                 not_determined  The arrowhead direction is too faint to determine whether it
                                              permits turning left.
    turn_right                not_determined  The arrowhead direction is too faint to determine whether it
                                              permits turning right.
    u_turn                    not_determined  The arrowhead direction is too faint to determine whether it
                                              permits a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the arrowhead is unclear, so only the movements governed by the arrow are
                      not_determined.
Result                Output 1 wrong (label arrow/left); Output 2 wrong (go_straight: label prohibited,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 273 output (hidden reasoning 0) | 3.4 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a white transverse marking is visible, but its full shape is too
                      faint to identify its type.
    Evidence          partial
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, a transverse pavement marking does not by itself govern any of the
                      six listed actions.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the visible transverse marking is classified as other, and none of the six
                      actions is governed by it.
Result                Output 1 wrong (label arrow/left); Output 2 wrong (go_straight: label prohibited,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 234 output (hidden reasoning 0) | 3.27 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a white transverse marking is visible, but its full shape is too
                      faint to identify its type.
    Evidence          partial
    Output 1          other, position in_ego_lane
Step 2  Rule          In the United States, a transverse pavement marking does not by itself govern any of the
                      six listed actions.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 not_applicable  Not governed by this marking.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the visible transverse marking is classified as other, and none of the six
                      actions is governed by it.
Result                Output 1 wrong (label arrow/left); Output 2 wrong (go_straight: label prohibited,
                      turn_left: label allowed, turn_right: label prohibited, u_turn: label allowed); evidence
                      group over_withholding
Tokens                2659 input + 234 output (hidden reasoning 0) | 3.17 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white lane-use arrow inside the rectangle has a head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn-only lane-use arrow requires traffic in that lane to
                      turn left at the next intersection.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits going straight.
    turn_left                 allowed         The left-only arrow permits turning left.
    turn_right                prohibited      The left-only arrow prohibits turning right.
    u_turn                    prohibited      The left-only arrow does not authorize a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a visible left arrow, and only lane-use movements receive
                      applicable actions.
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 233 output (hidden reasoning 0) | 2.87 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white curved arrow inside the rectangle has a head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane-use arrow requires traffic in that lane to turn
                      left at the next intersection and prohibits other movements.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-pointing arrow requires a left turn, not straight
                                              travel.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-pointing arrow requires a left turn, not a right turn.
    u_turn                    prohibited      The left-pointing arrow specifies a left turn, not a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 236 output (hidden reasoning 0) | 2.93 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          A single white lane-use arrow inside the rectangle has a head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn-only lane-use arrow requires traffic in that lane to
                      turn left at the next intersection.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits going straight.
    turn_left                 allowed         The left-only arrow permits turning left.
    turn_right                prohibited      The left-only arrow prohibits turning right.
    u_turn                    prohibited      The left-only arrow does not authorize a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is a visible left arrow, and only movements governed by a lane-
                      use arrow receive applicable actions.
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct
Tokens                2659 input + 237 output (hidden reasoning 0) | 2.87 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a white lane-use arrow has a visible head pointing left and
                      another pointing right.
    Evidence          full
    Output 1          arrow / left_right, position in_ego_lane
Step 2  Rule          In the United States, a left-right lane-use arrow permits turns in either indicated
                      direction and prohibits straight travel and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The arrow has no straight-pointing head, so straight travel is
                                              prohibited.
    turn_left                 allowed         The left-pointing head permits a left turn.
    turn_right                allowed         The right-pointing head permits a right turn.
    u_turn                    prohibited      The arrow does not indicate a U-turn, so it is prohibited.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 wrong (label two_way_left_turn_lane); Output 2 wrong
                      (enter_center_lane_to_wait: label allowed); evidence group wrong
Tokens                2659 input + 238 output (hidden reasoning 0) | 4.94 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a white lane-use arrow has visible heads pointing left and right.
    Evidence          full
    Output 1          arrow / left_right, position in_ego_lane
Step 2  Rule          In the United States, a left-right lane-use arrow permits turns in either indicated
                      direction and prohibits straight travel and U-turns from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The arrow has no straight-pointing head, so straight travel is
                                              prohibited.
    turn_left                 allowed         The left-pointing head permits a left turn.
    turn_right                allowed         The right-pointing head permits a right turn.
    u_turn                    prohibited      The arrow does not indicate a U-turn, so it is prohibited.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 wrong (label two_way_left_turn_lane); Output 2 wrong
                      (enter_center_lane_to_wait: label allowed); evidence group wrong
Tokens                2659 input + 235 output (hidden reasoning 0) | 3.13 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, a white lane-use arrow has visible heads pointing left and right.
    Evidence          full
    Output 1          arrow / left_right, position in_ego_lane
Step 2  Rule          In the United States, a left-right lane-use arrow permits turns in either indicated
                      direction and prohibits straight travel or a U-turn from that lane.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The arrow has no straight head, so straight travel is
                                              prohibited.
    turn_left                 allowed         The left-pointing head permits a left turn.
    turn_right                allowed         The right-pointing head permits a right turn.
    u_turn                    prohibited      The arrow does not indicate a U-turn, so it is prohibited.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 wrong (label two_way_left_turn_lane); Output 2 wrong
                      (enter_center_lane_to_wait: label allowed); evidence group wrong
Tokens                2659 input + 233 output (hidden reasoning 0) | 2.7 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6-sol | repeat 1
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two white lane-use arrows are visible: a large arrow pointing left
                      and a smaller arrow pointing left and right.
    Evidence          full
    Output 1          arrow / left_right, position in_ego_lane
Step 2  Rule          In the United States, lane-use arrows permit the indicated turns and restrict movements
                      not indicated by the arrows.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      Neither visible arrow points straight, so the lane-use rule
                                              prohibits it.
    turn_left                 allowed         Both visible arrows point left, so the lane-use rule permits it.
    turn_right                allowed         The smaller visible arrow points right, so the lane-use rule
                                              permits it.
    u_turn                    prohibited      Neither visible arrow indicates a U-turn, so the lane-use rule
                                              prohibits it.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the marking is described as arrows, and only lane-use movements receive
                      applicable actions.
Result                Output 1 wrong (label two_way_left_turn_lane); Output 2 wrong
                      (enter_center_lane_to_wait: label allowed); evidence group wrong
Tokens                2659 input + 263 output (hidden reasoning 0) | 3.61 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6-sol | repeat 2
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two white lane-use arrows are visible: a large arrow pointing left
                      and a smaller arrow pointing left and right.
    Evidence          full
    Output 1          arrow / left_right, position in_ego_lane
Step 2  Rule          In the United States, lane-use arrows permit travel only in the directions indicated by
                      their arrowheads.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The visible arrowheads do not point straight, so the lane-use
                                              rule prohibits it.
    turn_left                 allowed         The visible arrowheads point left, so the lane-use rule permits
                                              it.
    turn_right                allowed         The smaller arrowhead points right, so the lane-use rule permits
                                              it.
    u_turn                    prohibited      No arrowhead indicates a U-turn, so the lane-use rule prohibits
                                              it.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         Consistent: the described arrowheads match the marking type, and only lane-use movements
                      receive applicable actions.
Result                Output 1 wrong (label two_way_left_turn_lane); Output 2 wrong
                      (enter_center_lane_to_wait: label allowed); evidence group wrong
Tokens                2659 input + 268 output (hidden reasoning 0) | 3.25 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6-sol | repeat 3
-------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v4
Step 1  Look          Inside the rectangle, two white lane-use arrows are visible: a large arrow pointing left
                      and a smaller arrow pointing left and right.
    Evidence          full
    Output 1          arrow / left_right, position in_ego_lane
Step 2  Rule          In the United States, lane-use arrows permit the indicated turns and prohibit movements
                      not indicated by the arrows.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      Neither arrow points straight, so the lane-use rule prohibits
                                              going straight.
    turn_left                 allowed         Both arrows point left, so the lane-use rule permits turning
                                              left.
    turn_right                allowed         The smaller arrow points right, so the lane-use rule permits
                                              turning right.
    u_turn                    prohibited      Neither arrow indicates a U-turn, so the lane-use rule prohibits
                                              it.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Result                Output 1 wrong (label two_way_left_turn_lane); Output 2 wrong
                      (enter_center_lane_to_wait: label allowed); evidence group wrong
Tokens                2659 input + 245 output (hidden reasoning 0) | 2.79 s
```
