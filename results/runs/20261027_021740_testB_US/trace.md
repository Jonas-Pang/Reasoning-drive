# Reasoning trace of run 20261027_021740_testB_US

```
fl_20261017_night_01_f0001950 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single white lane-use arrow pointing straight ahead.
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
Reasoning             Under US-3B.23-01, lane-use arrows indicate mandatory or permissible lane movements.
                      This straight-only arrow permits proceeding straight from this lane, not left turns,
                      right turns, or U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 4.64 s
```

```
fl_20261017_night_01_f0001950 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single white lane-use arrow inside the ego lane points straight ahead.
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
Reasoning             Under US-3B.23-01, lane-use arrows indicate mandatory or permissible movements. This
                      straight-only arrow permits proceeding straight from this lane, not left turns, right
                      turns, or U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 3.35 s
```

```
fl_20261017_night_01_f0001950 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single white lane-use arrow pointing straight ahead.
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
Reasoning             US-3B.23-01 states that lane-use arrows indicate mandatory or permissible movements in a
                      lane. This straight-only arrow permits proceeding straight and excludes left turns,
                      right turns, and U-turns from this lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 208 output (hidden reasoning 0) | 3.39 s
```

```
fl_20261017_night_01_f0001970 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a white lane-use arrow pointing straight ahead in my lane.
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
Reasoning             Under US-3B.23-01, lane-use arrows indicate mandatory or permissible lane movements.
                      This straight-only arrow permits continuing straight and excludes left turns, right
                      turns, and U-turns from this lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 208 output (hidden reasoning 0) | 5.43 s
```

```
fl_20261017_night_01_f0001970 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A white lane-use arrow inside the ego lane points straight ahead.
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
Reasoning             US-3B.23-01 states that lane-use arrows indicate mandatory or permissible movements in a
                      lane. This straight-only arrow permits continuing straight and excludes left turns,
                      right turns, and U-turns from this lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 208 output (hidden reasoning 0) | 3.84 s
```

```
fl_20261017_night_01_f0001970 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single white lane-use arrow with a visible arrowhead points straight ahead in the ego
                      lane.
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
Reasoning             US-3B.23-01 states that lane-use arrows indicate mandatory or permissible movements in a
                      lane. This straight-only arrow permits continuing straight and excludes left turns,
                      right turns, and U-turns from this lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 214 output (hidden reasoning 0) | 3.83 s
```

```
fl_20261017_night_01_f0003105 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a white crosswalk with broad transverse stripes between two
                      continuous white boundary lines.
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
Reasoning             This is a pedestrian crosswalk, not a longitudinal lane line or lane-use arrow. None of
                      the supplied passages addresses crosswalks, so this marking does not determine any of
                      the listed lane-crossing or intersection movements.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3667 input + 208 output (hidden reasoning 0) | 5.31 s
```

```
fl_20261017_night_01_f0003105 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a white crosswalk formed by broad, spaced solid bars between two
                      solid transverse boundary lines.
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
Reasoning             The target is a transverse crosswalk, not a longitudinal lane line or lane-use arrow.
                      None of the supplied passages governs crosswalks, and this marking does not specify the
                      listed lane-crossing or intersection movements.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3667 input + 210 output (hidden reasoning 0) | 3.98 s
```

```
fl_20261017_night_01_f0003105 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a white crosswalk made of broad solid transverse bars between two
                      solid boundary lines.
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
Reasoning             The marking is a crosswalk, not a longitudinal lane line or lane-use arrow, and none of
                      the supplied passages addresses crosswalks. It therefore does not establish any of the
                      listed lane-crossing or directional permissions under the supplied rules.  (written
                      after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3667 input + 213 output (hidden reasoning 0) | 4.34 s
```

```
fl_20261017_night_01_f0006510 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single solid yellow line marks the left edge of the roadway beside my car.
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
Reasoning             The solid yellow line delineates the left-hand edge of this divided roadway under
                      US-3B.09-03. It restricts driving or passing to its left and does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 236 output (hidden reasoning 26) | 6.81 s
```

```
fl_20261017_night_01_f0006510 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single solid yellow line marks the left edge of my car's roadway.
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
Reasoning             The solid yellow line delineates the left-hand edge of this divided roadway under
                      US-3B.09-03. It marks the roadway boundary, so my car must not cross it to change lanes
                      or overtake; it does not govern intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 218 output (hidden reasoning 0) | 4.35 s
```

```
fl_20261017_night_01_f0006510 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single solid yellow line marking the left edge of my roadway.
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
Reasoning             The cited rule identifies a solid yellow line as the left roadway edge on a divided
                      highway or one-way roadway. My car must remain to its right rather than cross it for a
                      lane change or passing; it does not govern intersection movements.  (written after the
                      actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 215 output (hidden reasoning 0) | 6.19 s
```

```
fl_20261017_night_01_f0006600 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single solid yellow line marks the left edge of my car's roadway alongside the raised
                      median.
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
Reasoning             The solid yellow line delineates the left edge of this divided roadway and indicates a
                      restriction on driving or passing to its left. It does not govern movements at the next
                      intersection.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 237 output (hidden reasoning 29) | 6.48 s
```

```
fl_20261017_night_01_f0006600 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single solid yellow line runs along the left edge of my car's roadway beside the
                      raised median.
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
Reasoning             The solid yellow line marks the left-hand edge of this divided roadway and indicates
                      restrictions on driving to its left. My car must remain to its right; this edge marking
                      does not govern intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 249 output (hidden reasoning 36) | 5.16 s
```

```
fl_20261017_night_01_f0006600 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single continuous solid yellow line marks the left edge of my car's lane beside the
                      raised median.
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
Reasoning             The solid yellow line delineates the left-hand edge of this divided roadway and
                      indicates driving or passing restrictions to its left. My car must not cross it into the
                      median; it does not govern intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 257 output (hidden reasoning 42) | 5.42 s
```

```
fl_20261017_night_01_f0007725 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single solid yellow longitudinal line marks the left edge of my roadway.
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
Reasoning             The solid yellow line delineates the left-hand edge of this divided roadway under
                      US-3B.09-03. It restricts driving or passing to its left and does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 5.25 s
```

```
fl_20261017_night_01_f0007725 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single solid yellow longitudinal line marks the left edge of the roadway.
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
Reasoning             The solid yellow line delineates the left-hand roadway edge under US-3B.09-03. My car
                      must remain to its right rather than cross it for lane changing or passing; this edge
                      marking does not govern intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 213 output (hidden reasoning 0) | 4.03 s
```

```
fl_20261017_night_01_f0007725 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single solid yellow longitudinal line marks the left edge of my lane.
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
Reasoning             The solid yellow line beside the median is a left-edge marking under US-3B.09-03,
                      indicating driving or passing restrictions to its left. My car must not cross it to
                      change lanes or overtake; it does not specify intersection movements.  (written after
                      the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 255 output (hidden reasoning 36) | 5.9 s
```

```
fl_20261017_night_01_f0008220 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single solid yellow longitudinal line runs along the left edge of the roadway.
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
Reasoning             The solid yellow line marks the left-hand edge of this divided roadway and indicates a
                      restriction on driving or passing to its left. It does not govern intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 271 output (hidden reasoning 70) | 8.44 s
```

```
fl_20261017_night_01_f0008220 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          No usable painted pavement marking is visible inside the cyan rectangle; only dark
                      pavement and the adjacent curb can be distinguished.
    Evidence          insufficient
    Output 1          none_visible, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     none
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_determined
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The darkness prevents identifying a painted line and its colour or pattern, so no
                      supplied marking rule can be reliably applied. Whether crossing a line here is permitted
                      cannot be determined from the target area.  (written after the actions)
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding; contradicts itself: none_visible does not govern
                      cross_line; citation none
Tokens                3667 input + 287 output (hidden reasoning 79) | 7.74 s
```

```
fl_20261017_night_01_f0008220 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          No pavement marking with a discernible colour or solid/broken pattern is visible inside
                      the cyan rectangle.
    Evidence          insufficient
    Output 1          none_visible, position left
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     none
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                not_determined
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             The rectangle shows dark pavement beside the curb, but no identifiable painted line.
                      Without a visible colour and pattern, no supplied marking rule can establish whether
                      crossing is permitted.  (written after the actions)
Result                Output 1 wrong (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group over_withholding; contradicts itself: none_visible does not govern
                      cross_line; citation none
Tokens                3667 input + 273 output (hidden reasoning 73) | 6.15 s
```

```
fl_20261017_night_01_f0008355 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A worn white lane-use arrow inside my lane points straight ahead and left.
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             The cited rule states that lane-use arrows indicate mandatory or permissible lane
                      movements. This arrow permits proceeding straight or turning left, but not turning
                      right; it does not establish whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/straight_left); Output 2 correct (u_turn: label allowed);
                      evidence group correct; contradicts itself: not_determined with full evidence; citation
                      accepted
Tokens                3667 input + 252 output (hidden reasoning 44) | 6.14 s
```

```
fl_20261017_night_01_f0008355 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a worn white lane-use arrow with heads pointing straight ahead
                      and left.
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
Reasoning             Under US-3B.23-01, lane-use arrows indicate mandatory or permissible movements. This
                      arrow permits proceeding straight or turning left from the ego lane, rather than turning
                      right or making a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/straight_left); Output 2 correct (u_turn: label allowed);
                      evidence group correct; citation accepted
Tokens                3667 input + 247 output (hidden reasoning 36) | 4.88 s
```

```
fl_20261017_night_01_f0008355 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a worn white lane-use arrow with heads pointing straight ahead
                      and left.
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
Reasoning             Lane-use arrows indicate the mandatory or permissible movements in a lane. This arrow
                      permits proceeding straight or turning left from my lane, but does not permit a right
                      turn or U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/straight_left); Output 2 correct (u_turn: label allowed);
                      evidence group correct; citation accepted
Tokens                3667 input + 238 output (hidden reasoning 33) | 5.0 s
```

```
fl_20261017_night_01_f0011100 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow longitudinal lines to the left of my
                      car.
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
Reasoning             The double solid yellow marking indicates a two-direction no-passing zone under
                      US-3B.01-04. My car may not cross it to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 211 output (hidden reasoning 0) | 4.76 s
```

```
fl_20261017_night_01_f0011100 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow lines to the left of my car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 204 output (hidden reasoning 0) | 3.82 s
```

```
fl_20261017_night_01_f0011100 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines to the left of my
                      car.
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
Reasoning             This passage identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not specify
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 3.76 s
```

```
fl_20261017_night_01_f0011310 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow center lines to the left of my car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing zone.
                      My car may not cross these lines to overtake; this marking does not govern intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 205 output (hidden reasoning 0) | 5.14 s
```

```
fl_20261017_night_01_f0011310 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow center lines to the left of my car.
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
Reasoning             The passage identifies double solid yellow center lines as a two-direction no-passing
                      zone. My car may not cross these lines to overtake; this marking does not specify
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 3.51 s
```

```
fl_20261017_night_01_f0011310 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines to the left of my
                      car.
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
Reasoning             Under US-3B.01-04, double solid yellow center lines indicate a two-direction no-passing
                      zone. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 213 output (hidden reasoning 0) | 3.93 s
```

```
fl_20261017_night_01_f0011400 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow center lines to the left of my car.
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
Reasoning             Under US-3B.01-04, double solid yellow center lines mark a two-direction no-passing
                      zone. My car must not cross these lines to overtake; this marking does not prescribe
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 212 output (hidden reasoning 0) | 5.73 s
```

```
fl_20261017_night_01_f0011400 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow center lines to the left of my car.
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
Reasoning             Under US-3B.01-04, double solid yellow center lines designate a two-direction no-passing
                      zone. My car may not cross these lines to overtake; this marking does not specify
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 212 output (hidden reasoning 0) | 3.79 s
```

```
fl_20261017_night_01_f0011400 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow center lines to the left of my car.
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
Reasoning             The cited passage defines double solid yellow center lines as a two-direction no-passing
                      zone. My car must not cross these lines to overtake; this marking does not govern
                      movements at the next intersection.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 209 output (hidden reasoning 0) | 3.75 s
```

```
fl_20261017_night_01_f0011685 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow longitudinal lines to the left of my
                      car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 5.21 s
```

```
fl_20261017_night_01_f0011685 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow lines to the left of my car.
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
Reasoning             The passage identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 205 output (hidden reasoning 0) | 3.73 s
```

```
fl_20261017_night_01_f0011685 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow lines to the left of my car.
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
Reasoning             The double solid yellow center line denotes a two-direction no-passing zone under
                      US-3B.01-04. My car may not cross it to overtake; this marking does not specify
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 210 output (hidden reasoning 0) | 3.76 s
```

```
fl_20261017_night_01_f0011775 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow lines to the left of my car.
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
Reasoning             Under US-3B.01-04, double solid yellow center lines indicate a two-direction no-passing
                      zone. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 211 output (hidden reasoning 0) | 4.99 s
```

```
fl_20261017_night_01_f0011775 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          Two parallel solid yellow longitudinal lines lie to the left of my car.
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
Reasoning             The passage identifies double solid yellow center lines as a two-direction no-passing
                      zone. My car may not cross these lines for passing; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 202 output (hidden reasoning 0) | 3.66 s
```

```
fl_20261017_night_01_f0011775 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow center lines to the left of my car.
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
Reasoning             Under US-3B.01-04, double solid yellow center lines indicate a two-direction no-passing
                      zone. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 212 output (hidden reasoning 0) | 3.32 s
```

```
fl_20261017_night_01_f0011910 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow lines to the left of my car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 205 output (hidden reasoning 0) | 4.86 s
```

```
fl_20261017_night_01_f0011910 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow center lines to the left of my car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing zone.
                      My car may not cross these lines for passing; this marking does not govern intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 205 output (hidden reasoning 0) | 4.04 s
```

```
fl_20261017_night_01_f0011910 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines to the left of my
                      car.
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
Reasoning             The cited rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      movements at the next intersection.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 210 output (hidden reasoning 0) | 4.12 s
```

```
fl_20261017_night_01_f0012135 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          Two parallel solid yellow lines mark the center of the roadway to the left of my car.
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
Reasoning             The passage identifies double solid yellow center lines as a two-direction no-passing
                      zone. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 207 output (hidden reasoning 0) | 5.18 s
```

```
fl_20261017_night_01_f0012135 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow center lines to the left of my car.
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
Reasoning             The cited passage identifies double solid yellow center lines as a two-direction no-
                      passing zone. My car may not cross these lines to overtake; this marking does not
                      specify intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 207 output (hidden reasoning 0) | 3.77 s
```

```
fl_20261017_night_01_f0012135 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow lines to the left of my car.
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
Reasoning             The passage identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 205 output (hidden reasoning 0) | 4.77 s
```

```
fl_20261017_night_01_f0012315 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow longitudinal lines to the left of my
                      car.
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
Reasoning             Under US-3B.01-04, double solid yellow center lines indicate a two-direction no-passing
                      zone, prohibiting crossing for passing. This center-line marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 210 output (hidden reasoning 0) | 5.73 s
```

```
fl_20261017_night_01_f0012315 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow lines to the left of my car.
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
Reasoning             Under US-3B.01-04, double solid yellow center lines indicate a two-direction no-passing
                      zone, so my car may not cross them to overtake. This marking does not govern movements
                      at the next intersection.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 214 output (hidden reasoning 0) | 4.38 s
```

```
fl_20261017_night_01_f0012315 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow lines to the left of my car.
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
Reasoning             The double solid yellow center line indicates a two-direction no-passing zone under
                      US-3B.01-04. My car may not cross it to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 210 output (hidden reasoning 0) | 4.27 s
```

```
fl_20261017_night_01_f0012465 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          Two parallel solid yellow longitudinal lines are visible inside the rectangle, to the
                      left of my car's lane.
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
Reasoning             The passage identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 210 output (hidden reasoning 0) | 4.78 s
```

```
fl_20261017_night_01_f0012465 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines to the left of my
                      car.
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
Reasoning             The cited rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car must not cross these lines to overtake; this marking does not specify
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 207 output (hidden reasoning 0) | 4.07 s
```

```
fl_20261017_night_01_f0012465 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow center lines to the left of my car.
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
Reasoning             The cited passage identifies double solid yellow center lines as a two-direction no-
                      passing marking. My car may not cross these lines to overtake; this marking does not
                      specify intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 207 output (hidden reasoning 0) | 4.05 s
```

```
fl_20261017_night_01_f0012705 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow center lines to the left of my car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing zone.
                      My car must not cross these lines to overtake; this marking does not specify
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 205 output (hidden reasoning 0) | 4.43 s
```

```
fl_20261017_night_01_f0012705 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines to the left of my
                      car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing zone.
                      My car may not cross these lines to overtake; this marking does not specify intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 3.54 s
```

```
fl_20261017_night_01_f0012705 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, unbroken solid yellow center lines to the left of
                      my car.
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
Reasoning             The cited rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 209 output (hidden reasoning 0) | 3.74 s
```

```
fl_20261017_night_01_f0014235 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow longitudinal lines to the left of my
                      car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines for passing; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 205 output (hidden reasoning 0) | 4.71 s
```

```
fl_20261017_night_01_f0014235 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines to the left of my
                      car.
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
Reasoning             The cited passage identifies double solid yellow center lines as a two-direction no-
                      passing marking. My car may not cross these lines to overtake; this marking does not
                      govern intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 161 output (hidden reasoning 0) | 3.39 s
```

```
fl_20261017_night_01_f0014235 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow longitudinal lines to the left of my
                      car.
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
Reasoning             The cited passage identifies double solid yellow center lines as a two-direction no-
                      passing marking. My car may not cross these lines to overtake; this marking does not
                      specify intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 207 output (hidden reasoning 0) | 3.8 s
```

```
fl_20261017_night_01_f0014280 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single white lane-use arrow inside the ego lane points straight ahead.
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
Reasoning             Under US-3B.23-01, lane-use arrows indicate mandatory or permissible movements in a
                      lane. This straight-only arrow permits proceeding straight and excludes left turns,
                      right turns, and U-turns from this lane.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 209 output (hidden reasoning 0) | 5.41 s
```

```
fl_20261017_night_01_f0014280 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single white lane-use arrow pointing straight ahead.
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
Reasoning             US-3B.23-01 states that lane-use arrows indicate mandatory or permissible lane
                      movements. This straight-only arrow permits continuing straight from my lane, not
                      turning left, right, or making a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 3.62 s
```

```
fl_20261017_night_01_f0014280 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single white lane-use arrow in my lane points straight ahead.
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
Reasoning             Under US-3B.23-01, lane-use arrows indicate mandatory or permissible lane movements.
                      This straight-only arrow permits proceeding straight from my lane, not left turns, right
                      turns, or U-turns.  (written after the actions)
Result                Output 1 correct (label arrow/straight); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 3.76 s
```

```
fl_20261017_night_01_f0014325 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a faded white crosswalk marking with transverse boundary lines
                      and longitudinal bars.
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
Reasoning             The transverse lines and connecting bars identify a crosswalk rather than a longitudinal
                      lane line or lane-use arrow. None of the supplied passages addresses crosswalks, and
                      this marking does not specify any of the listed lane-crossing or intersection movements.
                      (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3667 input + 343 output (hidden reasoning 130) | 9.78 s
```

```
fl_20261017_night_01_f0014325 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a white crosswalk marking with transverse boundary lines and
                      short longitudinal bars across the roadway.
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
Reasoning             The target is a crosswalk rather than a longitudinal lane line or lane-use arrow. None
                      of the supplied passages addresses crosswalks, and this marking does not specify
                      permitted lane changes or intersection movements.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3667 input + 391 output (hidden reasoning 183) | 11.16 s
```

```
fl_20261017_night_01_f0014325 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a white crosswalk marking with worn rectangular bars arranged
                      across the roadway.
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
Reasoning             None of the supplied passages addresses crosswalk markings. This marking identifies a
                      pedestrian crossing rather than governing lane changes or prescribing intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label other); Output 2 not scored; evidence group correct; citation
                      none_needed
Tokens                3667 input + 405 output (hidden reasoning 214) | 12.1 s
```

```
fl_20261017_night_01_f0014670 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains an unbroken stretch of a single solid white line to the left of
                      my car's lane.
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
Reasoning             The cited passage states that a solid white lane line discourages crossing rather than
                      prohibiting it, so crossing counts as allowed here. This longitudinal line does not
                      govern intersection movements or entry into a center turn lane.  (written after the
                      actions)
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct;
                      citation accepted
Tokens                3667 input + 255 output (hidden reasoning 36) | 6.05 s
```

```
fl_20261017_night_01_f0014670 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single solid white longitudinal line to the left of my car.
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
Reasoning             The cited rule states that a solid white lane line discourages crossing rather than
                      prohibiting it. Crossing with care is therefore allowed under this marking; it does not
                      govern intersection movements.  (written after the actions)
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct;
                      citation accepted
Tokens                3667 input + 230 output (hidden reasoning 23) | 4.22 s
```

```
fl_20261017_night_01_f0014670 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains an unbroken stretch of a single solid white longitudinal line to
                      the left of my car.
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
Reasoning             The cited passage states that a solid white lane line discourages crossing rather than
                      prohibiting it. Crossing therefore counts as allowed, while this longitudinal line does
                      not govern intersection movements.  (written after the actions)
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct;
                      citation accepted
Tokens                3667 input + 262 output (hidden reasoning 51) | 6.15 s
```

```
fl_20261017_night_01_f0015915 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines to the left of my
                      car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 5.52 s
```

```
fl_20261017_night_01_f0015915 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, continuous solid yellow lines to the left of my
                      car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing zone.
                      My car may not cross these lines to overtake; this marking does not specify intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 3.52 s
```

```
fl_20261017_night_01_f0015915 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          Two parallel solid yellow lines form a double yellow center line to the left of my car.
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
Reasoning             The passage identifies double solid yellow center lines as a two-direction no-passing
                      zone. My car may not cross these lines to overtake; this marking does not specify
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 207 output (hidden reasoning 0) | 3.82 s
```

```
fl_20261017_night_01_f0018210 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          Two parallel solid yellow lines form a double yellow center line to the left of my car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not prescribe
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 232 output (hidden reasoning 23) | 5.13 s
```

```
fl_20261017_night_01_f0018210 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow longitudinal lines to the left of my
                      car.
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
Reasoning             The cited passage identifies double solid yellow center lines as a two-direction no-
                      passing marking. My car may not cross these lines to overtake; this marking does not
                      govern intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 4.39 s
```

```
fl_20261017_night_01_f0018210 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow longitudinal lines to the left of my
                      car.
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
Reasoning             The cited passage identifies double solid yellow center lines as a two-direction no-
                      passing marking. My car may not cross these lines to overtake; this marking does not
                      govern intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 4.39 s
```

```
fl_20261017_night_01_f0018240 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow longitudinal lines to the left of my
                      car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 240 output (hidden reasoning 33) | 6.07 s
```

```
fl_20261017_night_01_f0018240 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow longitudinal lines to the left of my
                      car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing zone.
                      My car may not cross these lines to overtake; this marking does not specify intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 240 output (hidden reasoning 33) | 4.62 s
```

```
fl_20261017_night_01_f0018240 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The marking is a pair of solid yellow longitudinal lines to the left of my car.
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
Reasoning             The cited passage identifies double solid yellow center lines as a two-direction no-
                      passing marking. My car may not cross these lines to overtake; this marking does not
                      specify intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 248 output (hidden reasoning 39) | 4.82 s
```

```
fl_20261017_night_01_f0018300 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow lines to the left of my car.
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
Reasoning             The rule identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car may not cross these lines to overtake; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 204 output (hidden reasoning 0) | 5.01 s
```

```
fl_20261017_night_01_f0018300 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel solid yellow lines to the left of my car.
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
Reasoning             The passage identifies double solid yellow center lines as a two-direction no-passing
                      marking. My car must not cross these lines to overtake; this marking does not specify
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 218 output (hidden reasoning 12) | 4.16 s
```

```
fl_20261017_night_01_f0018300 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains two parallel, solid yellow longitudinal lines to the left of my
                      car.
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
Reasoning             The cited passage identifies double solid yellow center lines as a two-direction no-
                      passing marking. My car may not cross these lines to overtake; this marking does not
                      govern intersection movements.  (written after the actions)
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 229 output (hidden reasoning 20) | 4.63 s
```

```
fl_20261017_night_01_f0030060 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white longitudinal line, with visible dashes and
                      gaps, to the left of my car's lane.
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
Reasoning             The cited rule states that a broken white lane line permits crossing with care. This
                      marking allows my car to cross into the adjacent lane but does not govern intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 212 output (hidden reasoning 0) | 6.25 s
```

```
fl_20261017_night_01_f0030060 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white longitudinal lane line, with visible dashes
                      and gaps.
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
Reasoning             The cited passage states that a broken white lane line permits crossing with care. My
                      car may cross this line to change lanes when safe; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 3.59 s
```

```
fl_20261017_night_01_f0030060 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line with visible painted segments and
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
Reasoning             The cited passage specifies a broken white lane line where crossing with care is not
                      discouraged or prohibited. My car may cross this line to the left with care; this
                      marking does not govern intersection movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 208 output (hidden reasoning 0) | 4.03 s
```

```
fl_20261017_night_01_f0030360 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white longitudinal lane line to the left of my
                      car, with visible dash segments and gaps.
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
Reasoning             The cited rule states that a broken white lane line permits crossing with care. My car
                      may cross this line to change lanes when safe; this marking does not govern intersection
                      movements or entry into a center turn lane.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 219 output (hidden reasoning 0) | 5.85 s
```

```
fl_20261017_night_01_f0030360 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line to the left of my car, with
                      visible dash segments and gaps.
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
Reasoning             The cited passage states that a broken white lane line permits crossing with care. My
                      car may cross this line to change lanes; this marking does not govern intersection
                      movements or entry into a center turn lane.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 216 output (hidden reasoning 0) | 3.84 s
```

```
fl_20261017_night_01_f0030360 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line to the left of my car, with
                      visible white segments and gaps.
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
Reasoning             The cited passage states that a broken white lane line is used where crossing with care
                      is not discouraged or prohibited. My car may cross this line with care; this marking
                      does not govern intersection movements or entry into a center turn lane.  (written after
                      the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 176 output (hidden reasoning 0) | 3.65 s
```

```
fl_20261017_night_01_f0030555 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line, with visible dashes and gaps, to
                      the left of my car's lane.
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
Reasoning             The cited passage states that a normal broken white lane line is used where crossing
                      with care is not discouraged or prohibited. My car may cross this line with care; the
                      line does not govern intersection movements or entry into a center turn lane.  (written
                      after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 226 output (hidden reasoning 0) | 5.37 s
```

```
fl_20261017_night_01_f0030555 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line, with visible dashes and gaps, to
                      the left of my car.
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
Reasoning             The cited rule specifies a broken white lane line where crossing with care is not
                      discouraged or prohibited. My car may cross this line with care; it does not govern
                      intersection movements or entry into a center turn lane.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 219 output (hidden reasoning 0) | 3.9 s
```

```
fl_20261017_night_01_f0030555 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single broken white longitudinal line with visible dashes and gaps marks the left side
                      of my lane.
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
Reasoning             The rule specifies a broken white lane line where crossing with care is not discouraged
                      or prohibited. My car may cross this line with care; the marking does not govern
                      intersection movements or entry into a center turn lane.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 215 output (hidden reasoning 0) | 3.76 s
```

```
fl_20261017_night_01_f0031695 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single broken white longitudinal line with visible dashes and gaps lies to the left of
                      my car.
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
Reasoning             The cited rule specifies a broken white lane line where crossing with care is not
                      discouraged or prohibited. My car may cross this line with care; this marking does not
                      govern intersection movements or entry into a center turn lane.  (written after the
                      actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 216 output (hidden reasoning 0) | 5.33 s
```

```
fl_20261017_night_01_f0031695 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line with visible dashes and gaps to
                      the left of my car's lane.
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
Reasoning             The cited passage permits crossing a broken white lane line with care. This marking
                      allows changing lanes across it but does not govern intersection movements.  (written
                      after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 204 output (hidden reasoning 0) | 3.64 s
```

```
fl_20261017_night_01_f0031695 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white longitudinal line, with visible dashes and
                      gaps, to the left of my car's lane.
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
Reasoning             The cited rule states that a broken white lane line permits crossing with care. My car
                      may cross this line to change lanes; this marking does not govern intersection movements
                      or entry into a center turn lane.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 219 output (hidden reasoning 0) | 4.07 s
```

```
fl_20261017_night_01_f0032025 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line, with a white dash and adjacent
                      gap visible.
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
Reasoning             The cited passage identifies a broken white lane line as permitting crossing with care.
                      My car may cross this line to change lanes when safe; the marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 161 output (hidden reasoning 0) | 4.08 s
```

```
fl_20261017_night_01_f0032025 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle shows a single broken white lane line to the right of my car, with a
                      visible dash and gap.
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
Reasoning             The cited passage states that a broken white lane line permits crossing with care. My
                      car may cross this line to change lanes; the marking does not govern intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 245 output (hidden reasoning 34) | 4.62 s
```

```
fl_20261017_night_01_f0032025 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single broken white lane line, with a visible dash and gap, lies to the right of my
                      car.
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
Reasoning             The cited passage states that a broken white lane line permits crossing with care. My
                      car may cross this line to change lanes when safe; this marking does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 234 output (hidden reasoning 22) | 4.09 s
```

```
fl_20261017_night_01_f0032220 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line to the right of my car, with a
                      visible dash and gap.
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
Reasoning             The rule identifies a broken white lane line as permitting crossing with care. My car
                      may cross this line to change lanes when safe; this marking does not govern intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 210 output (hidden reasoning 0) | 5.16 s
```

```
fl_20261017_night_01_f0032220 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line to the right of my car, with a
                      visible dash and gap.
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
Reasoning             The cited passage states that broken white lane lines permit crossing with care. My car
                      may cross this line to change lanes; this marking does not govern intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 208 output (hidden reasoning 0) | 3.7 s
```

```
fl_20261017_night_01_f0032220 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line to the right of my car, with a
                      visible dash and gap.
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
Reasoning             The cited passage states that a broken white lane line is used where crossing with care
                      is not discouraged or prohibited. My car may cross this line with care; the marking does
                      not govern intersection movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 215 output (hidden reasoning 0) | 4.38 s
```

```
fl_20261017_night_01_f0032505 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line to the right of my car, with
                      visible segments and gaps.
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
Reasoning             The cited passage permits crossing a broken white lane line with care. My car may cross
                      this line to change lanes; this marking does not govern intersection movements or entry
                      into a center turn lane.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 213 output (hidden reasoning 0) | 5.56 s
```

```
fl_20261017_night_01_f0032505 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single broken white lane line, with visible dash segments and
                      gaps, to the right of my car.
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
Reasoning             The cited rule specifies a broken white lane line where crossing with care is neither
                      discouraged nor prohibited. My car may cross this line with care; it does not govern
                      intersection movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 212 output (hidden reasoning 0) | 3.95 s
```

```
fl_20261017_night_01_f0032505 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single broken white longitudinal line with visible dashes and gaps lies to the right
                      of my car.
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
Reasoning             The cited passage states that a broken white lane line permits crossing with care. My
                      car may cross this line to change lanes; the marking does not govern intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3667 input + 206 output (hidden reasoning 0) | 3.53 s
```

```
fl_20261017_night_01_f0032685 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A white left-turn lane-use arrow with a visible left-pointing head is painted inside my
                      lane.
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             Lane-use arrows indicate mandatory or permissible movements. This left-turn arrow
                      directs my car to turn left rather than proceed straight or turn right; the marking
                      alone does not establish whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 264 output (hidden reasoning 51) | 6.62 s
```

```
fl_20261017_night_01_f0032685 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a white left-turn lane-use arrow with a visible left-pointing
                      head.
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
    u_turn                    not_applicable
    enter_center_lane_to_wait not_applicable
Reasoning             Lane-use arrows indicate mandatory or permissible movements in their lanes. This left-
                      turn arrow directs my car to turn left rather than proceed straight or turn right; it
                      does not independently establish U-turn permission.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3667 input + 208 output (hidden reasoning 0) | 3.9 s
```

```
fl_20261017_night_01_f0032685 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A white left-turn lane-use arrow is visible inside the cyan rectangle in my lane.
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             Lane-use arrows indicate the mandatory or permissible movements in a lane; this arrow
                      directs my car to turn left rather than continue straight or turn right. The left-turn
                      arrow alone does not establish whether a U-turn is permitted.  (written after the
                      actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 212 output (hidden reasoning 0) | 4.67 s
```

```
fl_20261017_night_01_f0032775 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             The cited rule states that lane-use arrows indicate mandatory or permissible movements.
                      This left-only arrow directs my car to turn left rather than proceed straight or turn
                      right; it does not establish whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 216 output (hidden reasoning 0) | 5.6 s
```

```
fl_20261017_night_01_f0032775 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A white lane-use arrow inside the ego lane curves to point left.
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
Reasoning             The passage states that lane-use arrows indicate mandatory or permissible lane
                      movements. This left-only arrow directs the car to turn left rather than proceed
                      straight, turn right, or make a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3667 input + 202 output (hidden reasoning 0) | 4.04 s
```

```
fl_20261017_night_01_f0032775 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single white curved lane-use arrow points left inside the ego lane.
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             Under US-3B.23-01, lane-use arrows indicate mandatory or permissible movements. This
                      left-only arrow permits a left turn rather than proceeding straight or turning right; it
                      does not establish whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 211 output (hidden reasoning 0) | 3.88 s
```

```
fl_20261017_night_01_f0032820 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single white lane-use arrow in the ego lane curves to point left.
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             Lane-use arrows indicate mandatory or permissible movements in a lane. This left-only
                      arrow permits a left turn and excludes straight and right movements; it does not
                      establish whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 204 output (hidden reasoning 0) | 5.4 s
```

```
fl_20261017_night_01_f0032820 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A white lane-use arrow inside my lane points left.
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             Lane-use arrows indicate mandatory or permissible movements in a lane. This left-
                      pointing arrow permits a left turn rather than straight or right travel; it does not
                      establish whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 201 output (hidden reasoning 0) | 3.83 s
```

```
fl_20261017_night_01_f0032820 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A white left-turn lane-use arrow with a visible left-pointing head is painted inside the
                      ego lane.
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
Reasoning             US-3B.23-01 states that lane-use arrows indicate mandatory or permissible movements in a
                      lane. This arrow indicates a left turn only, not straight travel, a right turn, or a
                      U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3667 input + 214 output (hidden reasoning 0) | 3.66 s
```

```
fl_20261017_night_01_f0032865 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A white lane-use arrow inside the ego lane points left.
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             Lane-use arrows indicate mandatory or permissible movements under US-3B.23-01. The left-
                      pointing arrow designates a left turn from this lane, not straight or right travel; it
                      does not establish whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 250 output (hidden reasoning 36) | 6.8 s
```

```
fl_20261017_night_01_f0032865 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A white lane-use arrow inside the ego lane points left.
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             Lane-use arrows indicate the mandatory or permissible movements from their lane. This
                      left-pointing arrow directs the car to turn left rather than proceed straight or turn
                      right; it does not establish whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 234 output (hidden reasoning 26) | 5.19 s
```

```
fl_20261017_night_01_f0032865 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A white lane-use arrow inside the rectangle points left.
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             Lane-use arrows indicate the mandatory or permissible movements in a lane. This left-
                      turn arrow directs my car to turn left rather than proceed straight or turn right; it
                      does not establish whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 230 output (hidden reasoning 24) | 4.31 s
```

```
fl_20261017_night_01_f0032940 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             Under US-3B.23-01, lane-use arrows indicate mandatory or permissible movements. This
                      left-only arrow directs my car to turn left rather than proceed straight or turn right;
                      it does not establish whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 221 output (hidden reasoning 0) | 5.54 s
```

```
fl_20261017_night_01_f0032940 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          A single white curved lane-use arrow points left inside my lane.
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
    u_turn                    not_determined
    enter_center_lane_to_wait not_applicable
Reasoning             Lane-use arrows indicate mandatory or permissible movements in a lane. This left-only
                      arrow permits a left turn rather than straight or right travel; it does not establish
                      whether a U-turn is permitted.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; contradicts itself: not_determined with full evidence; citation accepted
Tokens                3667 input + 202 output (hidden reasoning 0) | 3.49 s
```

```
fl_20261017_night_01_f0032940 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle contains a single white lane-use arrow curving left, with a clearly
                      visible left-pointing arrowhead.
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
Reasoning             US-3B.23-01 states that lane-use arrows indicate mandatory or permissible movements in a
                      lane. This left-only arrow directs my car to turn left, rather than proceed straight,
                      turn right, or make a U-turn.  (written after the actions)
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                3667 input + 220 output (hidden reasoning 0) | 4.0 s
```

```
fl_20261017_night_01_f0039450 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The centre lane is bounded on both sides by solid and broken yellow lines, with the
                      broken lines facing inward, and contains white left-turn arrows pointing in opposite
                      travel directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               not_applicable
    turn_left                 not_applicable
    turn_right                not_applicable
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The inward-facing broken yellow lines paired with outer solid yellow lines identify a
                      two-way left-turn lane under US-3B.05-01. My car may cross into this lane to wait as
                      part of a left-turn maneuver; this marking does not independently determine intersection
                      movements.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 wrong (turn_left: label
                      allowed); evidence group wrong; contradicts itself: two_way_left_turn_lane does not
                      govern cross_line; citation accepted
Tokens                3667 input + 400 output (hidden reasoning 155) | 12.44 s
```

```
fl_20261017_night_01_f0039450 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The centre lane has solid-and-broken yellow lines along both edges, with the broken
                      lines inward, and white left-turn arrows facing opposite directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    not_determined
    enter_center_lane_to_wait allowed
Reasoning             The paired yellow boundaries identify a two-way left-turn lane usable by traffic from
                      either direction as part of a left-turn maneuver. My car may enter or use it to wait for
                      a left turn, but not for through travel or a right turn; this marking does not establish
                      U-turn permission.  (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; contradicts itself: two_way_left_turn_lane does not govern cross_line,
                      go_straight, turn_right, u_turn; citation accepted
Tokens                3667 input + 362 output (hidden reasoning 123) | 7.81 s
```

```
fl_20261017_night_01_f0039450 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle shows a two-way left-turn lane bounded on both sides by paired solid and
                      broken yellow lines, with white left-turn arrows pointing in opposite travel directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The paired yellow boundaries and opposing arrows identify a shared lane for left-turn
                      maneuvers in either direction. My car may enter or cross its boundary as part of a left
                      turn and wait to turn left, but this is not a through-travel or right-turn lane.
                      (written after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; contradicts itself: two_way_left_turn_lane does not govern cross_line,
                      go_straight, turn_right; citation accepted
Tokens                3667 input + 327 output (hidden reasoning 89) | 8.36 s
```

```
fl_20261017_night_01_f0039465 | Test B | gpt-6.1-sol | repeat 1 | from cache
----------------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The centre lane has white left-turn arrows pointing in opposite travel directions and is
                      bordered on both sides by paired solid and broken yellow lines, with the broken lines
                      facing inward.
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
Reasoning             The inward-facing broken yellow lines and opposing left-turn arrows identify a two-way
                      left-turn lane. The cited rule permits traffic in either direction to use this lane as
                      part of a left-turn maneuver, including entering it to wait for a left turn.  (written
                      after the actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; citation accepted
Tokens                3667 input + 290 output (hidden reasoning 51) | 7.66 s
```

```
fl_20261017_night_01_f0039465 | Test B | gpt-6.1-sol | repeat 2
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The rectangle shows paired white left-turn arrows pointing in opposite travel directions
                      in a center lane bordered on both sides by solid-and-broken yellow lines, with the
                      broken lines toward the center lane.
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
Reasoning             The paired arrows and yellow solid-and-broken boundaries identify a two-way left-turn
                      lane. Under US-3B.05-01, traffic in either direction may use this center lane as part of
                      a left-turn maneuver, including entering it to wait for a left turn.  (written after the
                      actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; citation accepted
Tokens                3667 input + 307 output (hidden reasoning 58) | 6.43 s
```

```
fl_20261017_night_01_f0039465 | Test B | gpt-6.1-sol | repeat 3
---------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v1
Step 1  Look          The centre lane has solid-and-broken yellow lines along both edges and two white left-
                      turn arrows pointing in opposite travel directions.
    Evidence          full
    Output 1          two_way_left_turn_lane, position in_ego_lane
Step 2  Rule          (not written separately in this prompt version)
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide        (no reason per action in this prompt version)
    cross_line                allowed
    go_straight               prohibited
    turn_left                 allowed
    turn_right                prohibited
    u_turn                    not_applicable
    enter_center_lane_to_wait allowed
Reasoning             The yellow solid-and-broken boundaries, with broken lines toward the centre lane,
                      identify a two-way left-turn lane under US-3B.05-01. My car may enter and wait to turn
                      left, but this lane is not for through travel or right turns.  (written after the
                      actions)
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; contradicts itself: two_way_left_turn_lane does not govern cross_line,
                      go_straight, turn_right; citation accepted
Tokens                3667 input + 391 output (hidden reasoning 159) | 9.33 s
```
