# Reasoning trace of run 20261027_021835_testA_US

```
fl_20261017_night_01_f0001950 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a lane-use arrow with only a straight-ahead head designates
                      straight-only travel at the next intersection. It permits going straight and prohibits
                      left turns, right turns, and U-turns from this lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2358 input + 204 output (hidden reasoning 0) | 4.25 s
```

```
fl_20261017_night_01_f0001950 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The white arrow's single straight-ahead head designates a straight-only lane under U.S.
                      lane-use marking rules. It permits proceeding straight and prohibits left turns, right
                      turns, and U-turns from this lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2358 input + 202 output (hidden reasoning 0) | 4.13 s
```

```
fl_20261017_night_01_f0001950 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             Under U.S. lane-use marking rules, the single straight-ahead arrow designates this lane
                      for straight movement, allowing travel straight ahead and prohibiting left turns, right
                      turns, and U-turns from this lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2358 input + 202 output (hidden reasoning 0) | 4.31 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             Under U.S. lane-use marking rules, the single straight-ahead arrow designates this lane
                      for straight travel, allowing that movement and prohibiting left turns, right turns, and
                      U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2358 input + 198 output (hidden reasoning 0) | 4.75 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The single straight-ahead arrowhead identifies a straight-only lane-use arrow under U.S.
                      rules: proceeding straight is allowed, while left turns, right turns, and U-turns from
                      this lane are prohibited.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2358 input + 200 output (hidden reasoning 0) | 4.51 s
```

```
fl_20261017_night_01_f0001970 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             Under U.S. lane-use marking rules, the single straight-ahead arrow designates this lane
                      for straight travel, allowing that movement and prohibiting left turns, right turns, and
                      U-turns from the lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2358 input + 201 output (hidden reasoning 0) | 5.03 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          The rectangle contains a white crosswalk marking with broad, solid parallel bars
                      separated by dark gaps and bounded by transverse white lines.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The broad white bars and transverse boundaries identify a marked pedestrian crosswalk
                      under U.S. road-marking conventions. A crosswalk does not govern any of the six listed
                      lane-crossing or lane-use actions.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2358 input + 212 output (hidden reasoning 0) | 4.71 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Broad white parallel bars separated by pavement gaps form a crosswalk, with white
                      transverse borders.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The broad white bars and transverse borders identify a marked pedestrian crosswalk under
                      U.S. road-marking conventions. A crosswalk does not govern any of the six specified
                      lane-crossing or lane-use actions.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2358 input + 205 output (hidden reasoning 0) | 4.28 s
```

```
fl_20261017_night_01_f0003105 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Broad white transverse stripes separated by dark pavement gaps form a crosswalk, with
                      white boundary lines across their ends.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The broad white stripes and boundary lines identify a marked pedestrian crosswalk under
                      U.S. road-marking conventions. A crosswalk does not govern any of the six specified
                      lane-crossing or lane-use actions.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2358 input + 209 output (hidden reasoning 0) | 4.45 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid yellow line runs diagonally through the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The single solid yellow line marks the left roadway edge. Under U.S. marking rules, a
                      solid yellow edge line does not itself prohibit crossing, although it does not authorize
                      driving off the roadway.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2358 input + 212 output (hidden reasoning 16) | 4.33 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid yellow line runs diagonally through the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The single solid yellow line marks the left roadway edge. Under U.S. marking rules, an
                      edge line discourages crossing but does not itself prohibit it.  (written after the
                      actions)
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2358 input + 186 output (hidden reasoning 0) | 3.88 s
```

```
fl_20261017_night_01_f0006510 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single continuous yellow line is visible inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The continuous yellow line marks a boundary that must not be crossed for lane changing
                      or overtaking under U.S. marking conventions. This longitudinal line does not govern
                      turning movements.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 227 output (hidden reasoning 36) | 5.1 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid yellow line runs diagonally through the rectangle, with an unbroken
                      visible stretch.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible marking is a single solid yellow line. Under U.S. marking conventions,
                      crossing a single solid yellow line is discouraged rather than categorically prohibited,
                      so this marking alone does not forbid crossing.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2358 input + 246 output (hidden reasoning 42) | 5.64 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid yellow line runs diagonally through the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The unbroken yellow line marks the left boundary of the roadway; crossing it for a lane
                      change or overtaking is prohibited. It does not govern intersection movements.  (written
                      after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 316 output (hidden reasoning 126) | 7.76 s
```

```
fl_20261017_night_01_f0006600 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid yellow line runs diagonally through the rectangle, with an unbroken
                      stretch visible.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible solid yellow line marks the left roadway boundary; under U.S. marking rules,
                      crossing this boundary for lane changing or overtaking is prohibited. It does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 215 output (hidden reasoning 13) | 4.37 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid yellow longitudinal line is visible inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible single solid yellow line prohibits crossing it for changing lanes or
                      overtaking under U.S. marking rules. It does not govern the other listed movements.
                      (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 142 output (hidden reasoning 0) | 3.93 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid yellow longitudinal line is visible inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The unbroken yellow line marks the left roadway edge; under U.S. marking rules, it is
                      not to be crossed for lane changing or overtaking.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 187 output (hidden reasoning 0) | 3.67 s
```

```
fl_20261017_night_01_f0007725 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid yellow line runs along the left side of the lane inside the rectangle.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The single solid yellow line marks the left roadway edge. Under U.S. marking
                      conventions, a solid edge line discourages crossing but does not itself prohibit it; it
                      does not govern turning movements.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2358 input + 320 output (hidden reasoning 119) | 9.11 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          The rectangle shows dark pavement beside a curb, but no painted marking is clearly
                      distinguishable enough to establish its colour or pattern.
    Evidence          insufficient
    Output 1          none_visible, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             No usable pavement marking is distinguishable inside the rectangle, so no marking-
                      specific United States traffic rule can be applied.  (written after the actions)
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding
Tokens                2358 input + 365 output (hidden reasoning 215) | 10.51 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          No pavement marking is clearly discernible inside the rectangle; the surface is dark and
                      blurred.
    Evidence          insufficient
    Output 1          none_visible, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             No usable painted line or arrow is visible in the rectangle, so no marking-specific
                      United States traffic rule can be applied.  (written after the actions)
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding
Tokens                2358 input + 248 output (hidden reasoning 59) | 6.15 s
```

```
fl_20261017_night_01_f0008220 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          The rectangle shows dark pavement beside a curb, but no painted line with discernible
                      colour or pattern is clearly visible.
    Evidence          insufficient
    Output 1          none_visible, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             No pavement marking can be reliably identified in the dark rectangle, so no marking-
                      specific U.S. traffic rule can be applied.  (written after the actions)
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding
Tokens                2358 input + 312 output (hidden reasoning 117) | 7.99 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A worn white lane-use arrow has arrowheads pointing straight ahead and left.
    Evidence          full
    Output 1          arrow / straight_left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The visible straight and left arrowheads designate a lane for proceeding straight or
                      turning left, not right. Under U.S. lane-use marking rules, a left-turn arrow alone does
                      not prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/straight_left); Output 2 correct; evidence group correct
Tokens                2358 input + 271 output (hidden reasoning 72) | 6.79 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A worn white lane-use arrow has heads pointing straight ahead and to the left.
    Evidence          full
    Output 1          arrow / straight_left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The white straight-and-left arrow permits proceeding straight or turning left and
                      excludes a right turn under U.S. lane-use marking rules. The left-turn indication does
                      not itself prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/straight_left); Output 2 correct; evidence group correct
Tokens                2358 input + 326 output (hidden reasoning 129) | 8.53 s
```

```
fl_20261017_night_01_f0008355 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A worn white arrow has one head pointing straight ahead and another pointing left.
    Evidence          full
    Output 1          arrow / straight_left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The straight and left arrowheads permit proceeding straight or turning left and prohibit
                      a right turn from this lane under U.S. lane-use marking rules. A left-turn arrow does
                      not by itself prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/straight_left); Output 2 correct; evidence group correct
Tokens                2358 input + 345 output (hidden reasoning 145) | 9.87 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two continuous yellow lines form a double-solid yellow marking. In the United
                      States, this marking prohibits crossing it to change lanes or overtake.  (written after
                      the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 186 output (hidden reasoning 0) | 3.71 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two continuous yellow lines form a double solid yellow marking. Under United States
                      traffic rules, crossing this marking for lane changing or overtaking is prohibited.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 188 output (hidden reasoning 0) | 3.92 s
```

```
fl_20261017_night_01_f0011100 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid yellow centerline, which under U.S. rules
                      prohibits crossing for overtaking or changing lanes.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 186 output (hidden reasoning 0) | 3.61 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline. Under United States traffic
                      rules, crossing this marking to change lanes or overtake is prohibited.  (written after
                      the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 187 output (hidden reasoning 0) | 3.64 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline, which under U.S. traffic
                      rules prohibits crossing for passing or changing lanes.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 185 output (hidden reasoning 0) | 4.0 s
```

```
fl_20261017_night_01_f0011310 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-yellow centerline. In the United States,
                      crossing this marking to change lanes or overtake is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 140 output (hidden reasoning 0) | 3.38 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous yellow lines are visible inside the cyan rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two continuous yellow lines form a double-solid centerline. Under U.S. marking
                      rules, crossing this line to pass or change lanes is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 188 output (hidden reasoning 0) | 3.74 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-yellow centerline. Under United States rules,
                      crossing this marking to overtake or change lanes is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 186 output (hidden reasoning 0) | 3.91 s
```

```
fl_20261017_night_01_f0011400 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two continuous yellow lines form a double-solid centerline. Under U.S. rules,
                      crossing this marking to change lanes or overtake is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 187 output (hidden reasoning 0) | 3.6 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline. Under United States traffic
                      rules, crossing this marking for overtaking or changing lanes is prohibited.  (written
                      after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 188 output (hidden reasoning 0) | 3.99 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-yellow centerline. Under U.S. rules, crossing
                      this marking to change lanes or overtake is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 187 output (hidden reasoning 0) | 4.07 s
```

```
fl_20261017_night_01_f0011685 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline; under U.S. traffic rules,
                      crossing it for overtaking or changing lanes is prohibited. This longitudinal marking
                      does not govern the other listed actions.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 199 output (hidden reasoning 0) | 4.14 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible double solid yellow lines prohibit crossing from the ego lane to pass or
                      change lanes under U.S. road-marking rules.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 182 output (hidden reasoning 0) | 4.07 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two continuous yellow lines form a double-solid centerline. Under U.S. traffic
                      rules, crossing this marking to change lanes or overtake is prohibited.  (written after
                      the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 188 output (hidden reasoning 0) | 3.29 s
```

```
fl_20261017_night_01_f0011775 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid yellow centerline. Under U.S. marking
                      rules, crossing this line to change lanes or overtake is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 190 output (hidden reasoning 0) | 4.05 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline, which under U.S. rules
                      prohibits crossing for lane changes or overtaking.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 138 output (hidden reasoning 0) | 4.0 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines with unbroken stretches are visible inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline. Under U.S. traffic rules,
                      crossing this marking to change lanes or overtake is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 191 output (hidden reasoning 0) | 4.72 s
```

```
fl_20261017_night_01_f0011910 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-yellow centerline, which under U.S. rules
                      prohibits crossing to overtake or change lanes into opposing traffic. This longitudinal
                      marking does not govern the other listed actions.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 199 output (hidden reasoning 0) | 3.82 s
```

```
fl_20261017_night_01_f0012135 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline, which under United States
                      traffic rules prohibits crossing to change lanes or overtake.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 184 output (hidden reasoning 0) | 3.73 s
```

```
fl_20261017_night_01_f0012135 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-yellow centerline. Under U.S. road-marking
                      rules, crossing this marking for overtaking or changing lanes is prohibited.  (written
                      after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 190 output (hidden reasoning 0) | 3.65 s
```

```
fl_20261017_night_01_f0012135 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-yellow centerline, which under U.S. traffic
                      rules prohibits crossing for overtaking or changing lanes.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 185 output (hidden reasoning 0) | 3.66 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline, which under U.S. rules
                      prohibits crossing for passing or changing lanes.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 182 output (hidden reasoning 0) | 3.52 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two continuous yellow lines form a double solid yellow centerline. Under U.S. rules,
                      crossing this marking for lane changing or overtaking is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 142 output (hidden reasoning 0) | 3.13 s
```

```
fl_20261017_night_01_f0012315 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline, which under U.S. traffic
                      rules prohibits crossing for lane changes or overtaking.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 185 output (hidden reasoning 0) | 3.61 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline. Under U.S. rules, crossing
                      this marking for overtaking or changing lanes is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 188 output (hidden reasoning 0) | 4.43 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, solid yellow lines are visible inside the cyan rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two continuous yellow lines form a double-solid yellow centerline. Under United
                      States marking rules, crossing this marking to change lanes or overtake is prohibited.
                      (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 189 output (hidden reasoning 0) | 4.1 s
```

```
fl_20261017_night_01_f0012465 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines with no visible gaps run through the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-yellow centerline. Under U.S. rules, crossing
                      this marking to change lanes or overtake is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 189 output (hidden reasoning 0) | 3.57 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid yellow centerline. Under U.S. rules,
                      crossing this marking to overtake or change lanes is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 189 output (hidden reasoning 0) | 3.55 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the cyan rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid yellow centerline. In the United States,
                      this marking prohibits crossing to change lanes or overtake.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 188 output (hidden reasoning 0) | 3.83 s
```

```
fl_20261017_night_01_f0012705 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline. Under U.S. traffic rules,
                      crossing this marking to change lanes or overtake is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 189 output (hidden reasoning 0) | 3.97 s
```

```
fl_20261017_night_01_f0014235 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-yellow centerline. Under United States traffic
                      rules, crossing this marking to change lanes or overtake is prohibited.  (written after
                      the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 188 output (hidden reasoning 0) | 3.59 s
```

```
fl_20261017_night_01_f0014235 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines with unbroken stretches are visible inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two unbroken yellow lines form a double solid yellow centerline. Under U.S. road-
                      marking rules, crossing it for overtaking or changing lanes is prohibited.  (written
                      after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 194 output (hidden reasoning 0) | 4.32 s
```

```
fl_20261017_night_01_f0014235 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two continuous yellow lines form a double-solid yellow centerline. Under U.S.
                      traffic rules, crossing it to change lanes or overtake is prohibited.  (written after
                      the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 188 output (hidden reasoning 0) | 3.55 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single white arrow with its head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             The white straight-ahead lane-use arrow designates this lane for straight travel under
                      U.S. marking rules, allowing straight movement and prohibiting left turns, right turns,
                      and U-turns from the lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2358 input + 200 output (hidden reasoning 0) | 4.24 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             Under U.S. lane-use marking rules, the single straight-ahead arrow designates this lane
                      for straight movement. It allows proceeding straight and prohibits left turns, right
                      turns, and U-turns from this lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2358 input + 201 output (hidden reasoning 0) | 4.86 s
```

```
fl_20261017_night_01_f0014280 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white arrow with a single head pointing straight ahead is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / straight, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               allowed
    turn_left                 prohibited
    turn_right                prohibited
    u_turn                    prohibited
    enter_center_lane_to_wait not_applicable
Reasoning             Under U.S. lane-use marking rules, the single straight-ahead arrow designates this lane
                      for straight travel, allowing going straight and prohibiting left turns, right turns,
                      and U-turns from this lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct
Tokens                2358 input + 201 output (hidden reasoning 0) | 4.15 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Worn white transverse lines and short lengthwise bars form a crosswalk-like pattern
                      across the pavement.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The white transverse pattern is not a longitudinal lane boundary or a lane-use arrow.
                      Such a crossing marking does not govern any of the six listed actions.  (written after
                      the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2358 input + 335 output (hidden reasoning 182) | 11.1 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          The rectangle contains white transverse pavement lines with short, paired longitudinal
                      bars between them.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The transverse white lines and connecting bars form a crosswalk marking, rather than a
                      longitudinal lane boundary or lane-use arrow. Under U.S. rules, this marking identifies
                      a pedestrian crossing and does not itself govern any of the six listed actions.
                      (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2358 input + 305 output (hidden reasoning 93) | 7.9 s
```

```
fl_20261017_night_01_f0014325 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          White solid strokes form elongated rectangular outlines arranged across the roadway
                      inside the rectangle.
    Evidence          full
    Output 1          other, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The white rectangular outlines are transverse pavement markings, not a longitudinal lane
                      boundary or a lane-use arrow. They do not govern any of the six listed actions.
                      (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct
Tokens                2358 input + 269 output (hidden reasoning 75) | 6.73 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid white line runs diagonally through the rectangle.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible single solid white line discourages crossing under U.S. marking rules but
                      does not prohibit it, so crossing is allowed under the specified definition. This
                      longitudinal line does not govern the other listed actions.  (written after the actions)
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2358 input + 212 output (hidden reasoning 14) | 4.47 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid white line runs diagonally through the rectangle, with an unbroken
                      stretch visible.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a single solid white longitudinal line discourages crossing but
                      does not by itself prohibit it, so crossing is allowed under the specified
                      interpretation.  (written after the actions)
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2358 input + 213 output (hidden reasoning 18) | 4.84 s
```

```
fl_20261017_night_01_f0014670 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single solid white line runs diagonally through the rectangle, with an unbroken
                      stretch visible.
    Evidence          full
    Output 1          white_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a single solid white longitudinal line discourages crossing but
                      does not itself prohibit it. Thus crossing this line is allowed under the specified
                      interpretation.  (written after the actions)
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct
Tokens                2358 input + 220 output (hidden reasoning 24) | 5.01 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid yellow centerline. In the United States,
                      this marking prohibits crossing it to change lanes or overtake.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 188 output (hidden reasoning 0) | 3.35 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline, which under U.S. rules
                      prohibits crossing for passing or changing lanes.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 184 output (hidden reasoning 0) | 4.11 s
```

```
fl_20261017_night_01_f0015915 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline. Under U.S. rules, crossing
                      this marking to change lanes or overtake is prohibited.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 188 output (hidden reasoning 0) | 4.23 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A centre lane is bordered on both sides by paired yellow lines, with a solid outer line
                      and broken inner line on each side.
    Evidence          full
    Output 1          two_way_left_turn_lane, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The solid-and-broken yellow boundaries on both sides identify a two-way left-turn lane
                      under U.S. marking conventions. This marking permits entering the centre lane to wait
                      for a left turn and turning left out of it.  (written after the actions)
Result                Output 1 wrong (label yellow_double_solid); Output 2 wrong (cross_line: label
                      prohibited); evidence group wrong
Tokens                2358 input + 450 output (hidden reasoning 235) | 12.86 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines indicate a double-yellow no-passing boundary under U.S.
                      rules, prohibiting crossing them to change lanes or overtake.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 218 output (hidden reasoning 30) | 5.14 s
```

```
fl_20261017_night_01_f0018210 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid yellow marking, which prohibits crossing
                      for lane changing or overtaking under United States traffic rules.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 236 output (hidden reasoning 50) | 5.41 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines with an unbroken visible stretch run through the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid yellow centerline. Under United States
                      marking rules, crossing it to change lanes or overtake is prohibited.  (written after
                      the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 217 output (hidden reasoning 24) | 4.75 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two continuous yellow lines form a double solid yellow marking. In the United
                      States, this marking prohibits crossing for overtaking or changing lanes.  (written
                      after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 219 output (hidden reasoning 32) | 4.57 s
```

```
fl_20261017_night_01_f0018240 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel solid yellow lines are visible, with unbroken stretches inside the
                      rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid yellow marking. Under United States
                      rules, crossing this marking to overtake or change lanes is prohibited.  (written after
                      the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 221 output (hidden reasoning 29) | 5.03 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid centerline. Under U.S. traffic rules,
                      crossing this marking to change lanes or overtake is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 211 output (hidden reasoning 21) | 4.51 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid yellow centerline. Under U.S. marking
                      rules, crossing this centerline to change lanes or overtake is prohibited.  (written
                      after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 216 output (hidden reasoning 24) | 4.61 s
```

```
fl_20261017_night_01_f0018300 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Two parallel, continuous solid yellow lines are visible inside the rectangle.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                prohibited
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The two solid yellow lines form a double-solid yellow centerline. Under U.S. rules,
                      crossing this marking to change lanes or overtake is prohibited.  (written after the
                      actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct
Tokens                2358 input + 214 output (hidden reasoning 23) | 5.37 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line with visible dashes and intervening gaps is inside the
                      rectangle.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe. This marking does not govern intersection movements or entry into a center
                      turn lane.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 194 output (hidden reasoning 0) | 4.8 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line with visible dashes separated by gaps is inside the
                      rectangle.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe. The visible white dashes and gaps therefore allow crossing this line; it does
                      not govern turning or straight-ahead movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 202 output (hidden reasoning 0) | 5.15 s
```

```
fl_20261017_night_01_f0030060 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line with visible dashes and intervening gaps is inside the
                      rectangle.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white lane line permits crossing to change lanes when
                      safe. The visible white dashes and gaps therefore do not prohibit crossing this line.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 194 output (hidden reasoning 0) | 4.17 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line is visible inside the rectangle, with white dash segments
                      separated by gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and intervening gaps identify a broken white lane line. Under
                      U.S. rules, this line permits crossing to change lanes when safe.  (written after the
                      actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 194 output (hidden reasoning 0) | 4.06 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line is visible inside the rectangle, with white dash segments
                      separated by a gap.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and intervening gap identify a broken white lane line. In the
                      United States, this marking permits crossing to change lanes when safe.  (written after
                      the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 194 output (hidden reasoning 0) | 3.77 s
```

```
fl_20261017_night_01_f0030360 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line has visible dash portions separated by unpainted gaps inside
                      the rectangle.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe. The visible white dashes and gaps identify this marking; it does not govern
                      intersection movements or entry into a center turn lane.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 205 output (hidden reasoning 0) | 4.72 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line has visible painted dashes separated by unpainted gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and gaps identify a broken white lane line. Under United States
                      road-marking rules, crossing this line to change lanes is permitted when safe.  (written
                      after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 193 output (hidden reasoning 0) | 3.91 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line has visible elongated dashes separated by gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe. The visible white dashes and gaps identify this marking; it does not govern
                      turning or intersection movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 195 output (hidden reasoning 0) | 3.9 s
```

```
fl_20261017_night_01_f0030555 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line with distinct dashes and intervening gaps is visible inside
                      the rectangle.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe. This line does not govern turning movements or entry into a center turn lane.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 195 output (hidden reasoning 0) | 4.29 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line has visible painted dashes separated by unpainted gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe. The visible white dashes and gaps identify this permissive lane boundary.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 192 output (hidden reasoning 0) | 4.47 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line with visible dashes and intervening gaps is inside the
                      rectangle.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe. The visible white dashes and gaps identify this permissive lane boundary.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 193 output (hidden reasoning 0) | 3.77 s
```

```
fl_20261017_night_01_f0031695 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white longitudinal line has visible painted dashes separated by
                      unpainted gaps.
    Evidence          full
    Output 1          white_dashed, position left
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white line permits crossing to change lanes when safe.
                      The visible white dashes and gaps identify this marking; it does not govern turning or
                      straight-through movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 154 output (hidden reasoning 0) | 4.3 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          The rectangle contains a single broken white longitudinal marking, with a visible white
                      dash and an unpainted gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             Under U.S. rules, a broken white longitudinal line permits crossing to change lanes when
                      safe. The visible white dash and gap identify this as a permissive lane boundary.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 199 output (hidden reasoning 0) | 4.45 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          The rectangle contains a single broken white longitudinal marking, with a visible dash
                      and an unpainted gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white longitudinal line permits crossing to change lanes
                      when safe. The visible white dash and gap identify this marking as a broken white line.
                      (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 224 output (hidden reasoning 25) | 5.22 s
```

```
fl_20261017_night_01_f0032025 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          The rectangle contains a single broken white longitudinal marking, with a visible white
                      dash and an unmarked gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dash and gap identify a broken white lane line. In the United States,
                      this marking permits crossing to change lanes when safe.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 192 output (hidden reasoning 0) | 3.8 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line is visible, with a long dash, a gap, and a small portion of
                      the next dash.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dash and gap identify a broken white lane line. In the United States,
                      this marking permits crossing to change lanes when safe.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 196 output (hidden reasoning 0) | 3.87 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line is visible, with a long dash, a gap, and part of the next
                      dash.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The broken white line separates lanes traveling in the same direction under U.S. marking
                      rules; crossing it to change lanes is permitted when safe.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 149 output (hidden reasoning 0) | 3.9 s
```

```
fl_20261017_night_01_f0032220 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line is visible, with a long dash, a gap, and a small portion of
                      the next dash.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a broken white lane line permits crossing to change lanes when
                      safe. The visible white dash-and-gap pattern therefore does not prohibit crossing this
                      line.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 201 output (hidden reasoning 0) | 3.74 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line is visible, with white dash segments separated by unpainted
                      gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             Under U.S. rules, a broken white longitudinal line permits crossing to change lanes when
                      safe. The visible white dashes and gaps therefore allow crossing this line.  (written
                      after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 194 output (hidden reasoning 0) | 4.28 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line is visible, with white dash segments separated by unpainted
                      gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The visible white dashes and intervening gaps identify a broken white lane line. Under
                      U.S. marking rules, crossing this line to change lanes is allowed when safe.  (written
                      after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 196 output (hidden reasoning 0) | 4.31 s
```

```
fl_20261017_night_01_f0032505 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single broken white line is visible, with white dash segments separated by dark
                      pavement gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             Under United States marking rules, a broken white longitudinal line permits crossing to
                      change lanes when safe. The visible white dashes and intervening gaps identify this as a
                      permissive lane boundary.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct
Tokens                2358 input + 198 output (hidden reasoning 0) | 4.08 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white pavement arrow has a curved shaft and a single head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             Under U.S. lane-use rules, the single left-pointing arrow designates a left-turn lane,
                      allowing left turns and prohibiting straight travel and right turns. A left-turn arrow
                      alone does not prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 226 output (hidden reasoning 23) | 4.21 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white lane-use arrow with a bent shaft and a head pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The white left-pointing lane-use arrow designates a left-turn lane, prohibiting straight
                      and right-turn movements. Under U.S. rules, this arrow permits a left turn and does not
                      itself prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 258 output (hidden reasoning 51) | 5.27 s
```

```
fl_20261017_night_01_f0032685 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white lane-use arrow with a single head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             Under U.S. lane-use rules, the single left-pointing arrow designates a left-turn lane,
                      permitting left turns and prohibiting straight and right-turn movements. The left arrow
                      alone does not forbid a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 238 output (hidden reasoning 34) | 5.39 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single white curved arrow with its arrowhead pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The white left-pointing lane-use arrow designates a left-turn lane, allowing left turns
                      and prohibiting straight and right-turn movements. Under U.S. rules, a left-turn arrow
                      alone does not prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 223 output (hidden reasoning 18) | 4.73 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single white curved arrow with its arrowhead pointing left is visible inside the
                      rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The white left-pointing lane-use arrow requires a leftward movement, allowing a left
                      turn and prohibiting straight and right movements. Under U.S. rules, a left-turn arrow
                      alone does not prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 227 output (hidden reasoning 23) | 4.55 s
```

```
fl_20261017_night_01_f0032775 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single white curved arrow has one visible arrowhead pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The white left-pointing lane-use arrow designates a left-turn lane, allowing left turns
                      and prohibiting straight and right movements. Under U.S. marking rules, a left-turn
                      arrow alone does not prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 218 output (hidden reasoning 17) | 4.47 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white lane-use arrow has a bent shaft and a single arrowhead pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The single left-pointing arrow designates a left-turn lane under U.S. pavement-marking
                      rules, allowing left turns and prohibiting straight and right movements. The left-turn
                      arrow alone does not prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 232 output (hidden reasoning 28) | 4.93 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white lane-use arrow has a bent shaft and a single arrowhead pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a left-only lane-use arrow permits a left turn and prohibits
                      straight and right-turn movements. The left arrow alone does not prohibit a U-turn.
                      (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 215 output (hidden reasoning 21) | 4.4 s
```

```
fl_20261017_night_01_f0032820 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white lane-use arrow has a bent shaft and a single arrowhead pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The single left-pointing arrow designates a left-turn lane under U.S. pavement-marking
                      rules, allowing left turns and prohibiting straight and right-turn movements. The left
                      arrow alone does not prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 226 output (hidden reasoning 22) | 4.88 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white lane-use arrow with a head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The visible left-pointing arrow designates a left-turn lane under U.S. lane-use rules,
                      prohibiting straight travel and right turns. It permits a left turn and does not itself
                      prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 228 output (hidden reasoning 27) | 5.14 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white lane-use arrow with a single head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             In the United States, a left-only lane-use arrow permits left turns and prohibits
                      straight-through and right-turn movements. The left arrow alone does not prohibit a
                      U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 226 output (hidden reasoning 32) | 4.44 s
```

```
fl_20261017_night_01_f0032865 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white lane-use arrow has a bent shaft and a head pointing left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The visible left-pointing arrow designates a left-turn lane under U.S. lane-use rules,
                      prohibiting straight and right movements. It permits a left turn and does not itself
                      prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 254 output (hidden reasoning 55) | 6.87 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single white curved arrow with its head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The white left-pointing lane-use arrow requires a leftward movement, prohibiting
                      straight travel and right turns while permitting a left turn. Under U.S. rules, a left-
                      turn arrow alone does not forbid a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 202 output (hidden reasoning 0) | 3.79 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A white curved arrow with a single head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             The single left-pointing arrow designates a left-turn lane under U.S. lane-use rules,
                      permitting left turns and prohibiting straight and right movements. A left-turn arrow
                      alone does not prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 200 output (hidden reasoning 0) | 4.4 s
```

```
fl_20261017_night_01_f0032940 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A single white curved arrow with its head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    allowed
    enter_center_lane_to_wait not_applicable
Reasoning             Under U.S. lane-use rules, the white left-pointing arrow designates a left-turn lane,
                      allowing left turns and prohibiting straight and right-turn movements. The left-turn
                      arrow does not itself prohibit a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2358 input + 202 output (hidden reasoning 0) | 4.9 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          Both edges of the centre lane have a solid yellow line alongside a broken yellow line,
                      with two white curved arrows pointing in opposite directions inside the lane.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid-and-broken yellow boundaries and opposing curved white arrows identify
                      a US two-way left-turn lane. This marking permits entering the centre lane to wait for a
                      left turn and turning left from it.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2358 input + 275 output (hidden reasoning 56) | 5.63 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A centre lane has a solid and a broken yellow line along each edge, with two white
                      curved arrows pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid-and-broken yellow boundaries and opposing white turn arrows identify a
                      shared two-way left-turn lane under U.S. rules. This marking permits entering the centre
                      lane to wait for a left turn and turning left out of it.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2358 input + 214 output (hidden reasoning 39) | 5.44 s
```

```
fl_20261017_night_01_f0039450 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A centre lane has a solid yellow line and a broken yellow line along each edge, with two
                      white curved arrows pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid-and-broken yellow boundaries and opposing white arrows identify a US
                      two-way left-turn lane. This marking permits entering the centre lane to wait for a left
                      turn and turning left out of it.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2358 input + 233 output (hidden reasoning 17) | 4.12 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6.1-sol | repeat 1
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A centre lane has paired solid and broken yellow lines along both edges and two white
                      curved arrows pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid-and-broken yellow boundaries and opposing white turn arrows identify a
                      US two-way left-turn lane. This marking permits entering the centre lane to wait for a
                      left turn and turning left from it.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2358 input + 241 output (hidden reasoning 29) | 4.41 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          A centre lane has paired solid and broken yellow boundary lines on both sides and white
                      curved left-turn arrows pointing in opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid-and-broken yellow boundaries and opposing left-turn arrows identify a
                      US two-way left-turn lane. This marking permits entering the centre lane to wait for a
                      left turn and turning left out of it.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2358 input + 265 output (hidden reasoning 50) | 5.36 s
```

```
fl_20261017_night_01_f0039465 | Test A | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v2
Step 1  Look          The rectangle contains a white curved left-turn arrow and an oppositely oriented white
                      turn arrow, between yellow boundaries that each have a solid line beside a broken line.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_applicable
    go_straight               not_applicable
    turn_left                 allowed
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired solid-and-broken yellow boundaries and opposing white turn arrows identify a
                      shared two-way left-turn lane under U.S. marking rules. This marking permits entering
                      the center lane to wait for a left turn and turning left from it.  (written after the
                      actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2358 input + 295 output (hidden reasoning 67) | 6.66 s
```
