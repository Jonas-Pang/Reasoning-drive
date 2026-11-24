# Reasoning at every stop: route1 on Town03

Model gpt-6.1-sol, reasoning effort low, prompt prompts/v3. A = Test A US; B = Test B US (MUTCD); C = Test B with the China passages on the same US road.

## Stop 1: broken white lane line

Road 65 lane 2. Intent from the route: change lane across the line. The car (B): changes to the right lane. With C it would: cross.

### A  Test A, US (image only), line  (earlier answer, reused)

```
route1_stop01_line | Test A | gpt-6.1-sol | repeat 1 | from cache
-----------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single white broken longitudinal line, with visible dash
                      portions separated by a clear gap.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          In the United States, a dashed white lane line may be crossed to change lanes when it is
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
Tokens                2584 input + 283 output (hidden reasoning 0) | 5.89 s | $0.00000
```

### B  Test B, US (image + MUTCD), line  (earlier answer, reused)

```
route1_stop01_line | Test B | gpt-6.1-sol | repeat 1 | from cache
-----------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          The rectangle contains segments of a single broken white longitudinal line with a
                      visible gap between them.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          Under US-3B.06-05-06, a broken white lane line permits crossing with care.
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide
    cross_line                allowed         The visible broken white line permits crossing with care.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                4187 input + 292 output (hidden reasoning 0) | 5.81 s | $0.00000
```

### C  Test B, CN rules on a US road, line  (earlier answer, reused)

```
route1_stop01_line | Test B | gpt-6.1-sol | repeat 1 | from cache
-----------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          The rectangle contains a single broken white longitudinal line, with a visible dash, a
                      gap, and part of the next dash.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          Under CN-4.2.2-a, a broken longitudinal line may be crossed.
    Cited passage     CN-4.2.2-a: "Longitudinal markings, set along the direction of travel, take these forms:
                      a solid line means crossing is normally prohibited, and may be crossed in an emergency
                      when it is safe; a broken line means it may be crossed; a broken-solid line m"
Step 3  Decide
    cross_line                allowed         The visible broken white line may be crossed under the cited
                                              rule.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3723 input + 296 output (hidden reasoning 0) | 6.54 s | $0.00000
```

## Stop 2: single solid yellow line on the left

Road 5 lane -1. Intent from the route: cross the yellow line to the left. The car (B): does not cross, stays in its lane. With C it would: not cross.

### A  Test A, US (image only), line

```
route1_stop02_line | Test A | gpt-6.1-sol | repeat 1
----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle is a single continuous yellow line on the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          In the United States, a single solid yellow left-edge line delineates the roadway
                      boundary but does not by itself prohibit crossing it.
Step 3  Decide
    cross_line                allowed         The single solid yellow edge line does not itself prohibit
                                              crossing.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Model's summary       **Clarifying solid yellow lines**  I’m trying to establish the rules around solid yellow
                      lines in the U.S. Generally, a solid yellow line marks the left edge of a divided
                      highway and prohibits crossing for passing, but crossing at the edge might be permitted
                      in some conditions. Developers often expect actions to align with prohibitive rules. So,
                      it seems like the consensus is that a solid yellow line indicates no crossing for
                      passing or lane changes, which I should emphasize!
Result                Output 1 correct (label yellow_solid); Output 2 wrong (cross_line: label prohibited);
                      evidence group wrong; UNSAFE: cross_line
Tokens                2584 input + 412 output (hidden reasoning 124) | 9.95 s | $0.00929
```

### B  Test B, US (image + MUTCD), line

```
route1_stop02_line | Test B | gpt-6.1-sol | repeat 1
----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          The rectangle contains a single solid yellow longitudinal line to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          Under US-3B.09-03, a solid yellow left-edge line indicates driving or passing
                      restrictions to its left, prohibiting crossing it for lane changes or overtaking.
    Cited passage     US-3B.09-03: "If used on the roadways of divided highways or one-way streets, or on any
                      ramp in the direction of travel, left edge line pavement markings shall consist of a
                      normal width solid yellow line to delineate the left-hand edge of a roadway or to"
Step 3  Decide
    cross_line                prohibited      The solid yellow left-edge line restricts driving or passing to
                                              its left.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                4187 input + 308 output (hidden reasoning 0) | 5.15 s | $0.01145
```

### C  Test B, CN rules on a US road, line

```
route1_stop02_line | Test B | gpt-6.1-sol | repeat 1
----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          Inside the rectangle is a single solid yellow longitudinal line to the left of my car.
    Evidence          full
    Output 1          yellow_solid, position left
Step 2  Rule          Under CN-6.1.4, a single solid yellow line prohibits vehicles in both directions from
                      crossing.
    Cited passage     CN-6.1.4: "A single solid yellow line prohibits vehicles in both directions from
                      crossing. It is generally used on two-lane two-way roads with limited sight distance or
                      where overtaking must be prohibited."
Step 3  Decide
    cross_line                prohibited      The single solid yellow line prohibits crossing under CN-6.1.4.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3723 input + 295 output (hidden reasoning 0) | 4.02 s | $0.01040
```

## Stop 3: right-turn arrow

Road 59 lane -5. Intent from the route: go_straight. The car (B): straight not allowed -> goes right instead and re-plans. With C it would: not straight.

### A  Test A, US (image only), arrow

```
route1_stop03_arrow | Test A | gpt-6.1-sol | repeat 1
-----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white bent arrow has a shaft curving to the right and an arrowhead pointing right.
    Evidence          full
    Output 1          arrow / right, position in_ego_lane
Step 2  Rule          In the United States, a right-only lane-use arrow requires traffic in that lane to turn
                      right at the next intersection rather than proceed straight, turn left, or make a
                      U-turn.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               prohibited      The right-only arrow prohibits proceeding straight.
    turn_left                 prohibited      The right-only arrow prohibits turning left.
    turn_right                allowed         The right-pointing arrow allows turning right.
    u_turn                    prohibited      The right-only arrow prohibits making a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Model's summary       **Evaluating arrow design**  I need to confirm if the arrow looks right. The shaft is
                      positioned at the bottom left, starting at coordinates 575, 442, and then it curves up
                      and to the right, ending at 647, 434. The head is a bit faint, but I can still see it.
                      It's interesting how small details can affect the overall appearance, and I'm curious to
                      see if it meets the intended design perfectly.
Result                Output 1 correct (label arrow/right); Output 2 correct; evidence group correct
Tokens                2584 input + 341 output (hidden reasoning 35) | 6.73 s | $0.00858
```

### B  Test B, US (image + MUTCD), arrow

```
route1_stop03_arrow | Test B | gpt-6.1-sol | repeat 1
-----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          A white bent lane-use arrow has a head pointing right.
    Evidence          full
    Output 1          arrow / right, position in_ego_lane
Step 2  Rule          Under the lane-use arrow rule, this right-pointing arrow indicates a right-turn movement
                      rather than straight, left-turn, or U-turn movements.
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               prohibited      The right-only arrow does not permit a straight movement.
    turn_left                 prohibited      The right-only arrow does not permit a left turn.
    turn_right                allowed         The right-pointing arrow permits a right turn.
    u_turn                    prohibited      The right-only arrow does not permit a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/right); Output 2 correct; evidence group correct; citation
                      accepted
Tokens                4187 input + 334 output (hidden reasoning 27) | 6.86 s | $0.01171
```

### C  Test B, CN rules on a US road, arrow

```
route1_stop03_arrow | Test B | gpt-6.1-sol | repeat 1
-----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          A white lane-use arrow inside the rectangle bends to the right and has a right-pointing
                      head.
    Evidence          full
    Output 1          arrow / right, position in_ego_lane
Step 2  Rule          Under CN-5.13.1, the right-pointing guide arrow indicates a right turn rather than
                      straight, left, or U-turn travel.
    Cited passage     CN-5.13.1: "Guide arrows indicate the direction of travel for vehicles. (Table 1
                      meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                      straight or U-turn; left or U-turn; left or right only; merge left; merge right.)"
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               prohibited      The arrow indicates right only, not straight ahead.
    turn_left                 prohibited      The arrow indicates right only, not left.
    turn_right                allowed         The right-pointing arrow indicates a right turn.
    u_turn                    prohibited      The arrow indicates right only, not a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/right); Output 2 correct; evidence group correct; citation
                      accepted
Tokens                3723 input + 338 output (hidden reasoning 26) | 5.75 s | $0.01083
```

## Stop 4: roundabout: line between the circulating lanes

Road 1100 lane -4. Intent from the route: move to the outer lane to leave the roundabout. The car (B): changes to the right lane. With C it would: cross.

### A  Test A, US (image only), line

```
route1_stop04_line | Test A | gpt-6.1-sol | repeat 1
----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A single broken white line, with several dashes and intervening gaps visible, lies to
                      the right of my car.
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
Tokens                2584 input + 283 output (hidden reasoning 0) | 5.09 s | $0.00800
```

### B  Test B, US (image + MUTCD), line

```
route1_stop04_line | Test B | gpt-6.1-sol | repeat 1
----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          The rectangle contains a single broken white longitudinal line, with several white
                      dashes separated by visible gaps.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          Under US-3B.06-05-06, a broken white lane line permits crossing with care.
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide
    cross_line                allowed         The visible broken white line permits crossing with care.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                4187 input + 294 output (hidden reasoning 0) | 4.47 s | $0.01131
```

### C  Test B, CN rules on a US road, line

```
route1_stop04_line | Test B | gpt-6.1-sol | repeat 1
----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          A single broken white longitudinal line with several visible dashes and intervening gaps
                      lies to the right of the car.
    Evidence          full
    Output 1          white_dashed, position right
Step 2  Rule          Under CN-4.2.2-a, a broken longitudinal line may be crossed.
    Cited passage     CN-4.2.2-a: "Longitudinal markings, set along the direction of travel, take these forms:
                      a solid line means crossing is normally prohibited, and may be crossed in an emergency
                      when it is safe; a broken line means it may be crossed; a broken-solid line m"
Step 3  Decide
    cross_line                allowed         The visible broken white line may be crossed under the cited
                                              rule.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_dashed); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3723 input + 294 output (hidden reasoning 0) | 4.19 s | $0.01039
```

## Stop 5: double solid yellow centre line

Road 20 lane 1. Intent from the route: overtake across the centre line. The car (B): does not cross, stays in its lane. With C it would: not cross.

### A  Test A, US (image only), line

```
route1_stop05_line | Test A | gpt-6.1-sol | repeat 1
----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous yellow lines to the left of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          In the United States, double solid yellow centerlines prohibit crossing for passing or
                      changing lanes.
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
Tokens                2584 input + 283 output (hidden reasoning 0) | 4.56 s | $0.00800
```

### B  Test B, US (image + MUTCD), line

```
route1_stop05_line | Test B | gpt-6.1-sol | repeat 1
----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          Inside the rectangle are two parallel solid yellow longitudinal lines to the left of my
                      car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          Double solid yellow center lines prohibit crossing for passing in either direction.
    Cited passage     US-3B.01-04: "The center line markings on two-lane, two-way roadways shall be one of the
                      following: A. Two-direction passing zone markings consisting of a normal width broken
                      yellow line where crossing the center line markings for passing with care is pe"
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing for passing.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                4187 input + 282 output (hidden reasoning 0) | 3.84 s | $0.01119
```

### C  Test B, CN rules on a US road, line

```
route1_stop05_line | Test B | gpt-6.1-sol | repeat 1
----------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          Inside the rectangle are two parallel, continuous yellow longitudinal lines to the left
                      of my car.
    Evidence          full
    Output 1          yellow_double_solid, position left
Step 2  Rule          A double solid yellow line prohibits vehicles in both directions from crossing.
    Cited passage     CN-6.1.2: "A double solid yellow line prohibits vehicles in both directions from
                      crossing. It is generally used on roads with two or more motor-vehicle lanes in one
                      direction and no physical median, and may also be used on two-lane two-way roads with "
Step 3  Decide
    cross_line                prohibited      The two solid yellow lines prohibit crossing under CN-6.1.2.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label yellow_double_solid); Output 2 correct; evidence group correct;
                      citation accepted
Tokens                3723 input + 288 output (hidden reasoning 0) | 4.06 s | $0.01033
```

## Stop 6: junction approach: left-turn arrow and the line to the right lane

Road 44 lane -4. Intent from the route: turn_right. The car (B): right not allowed from this lane; the right line may be crossed -> changes lane, then goes right. With C it would: stay in lane and take the lane's own movement.

### A  Test A, US (image only), line  (earlier answer, reused)

```
route1_stop06_line | Test A | gpt-6.1-sol | repeat 1 | from cache
-----------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle contains a single white longitudinal line with an unbroken solid stretch.
    Evidence          full
    Output 1          white_solid, position right
Step 2  Rule          In the United States, crossing a single solid white longitudinal line is discouraged but
                      not prohibited by the marking alone.
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
Tokens                2584 input + 283 output (hidden reasoning 0) | 4.77 s | $0.00000
```

### B  Test B, US (image + MUTCD), line  (earlier answer, reused)

```
route1_stop06_line | Test B | gpt-6.1-sol | repeat 1 | from cache
-----------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          The rectangle contains a single white longitudinal line with a continuous, unbroken
                      stretch on the right of my lane.
    Evidence          full
    Output 1          white_solid, position right
Step 2  Rule          A single solid white lane line discourages crossing but does not prohibit it, so
                      crossing counts as allowed.
    Cited passage     US-3B.06-05-06: "Where crossing the lane line markings with care is not discouraged or
                      prohibited, the lane line markings shall consist of a normal width broken white line.
                      Where crossing the lane line markings is discouraged, the lane line markings shall c"
Step 3  Decide
    cross_line                allowed         The single solid white line discourages crossing without
                                              prohibiting it.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_solid); Output 2 not scored; evidence group correct;
                      citation accepted
Tokens                4187 input + 298 output (hidden reasoning 0) | 4.63 s | $0.00000
```

### C  Test B, CN rules on a US road, line  (earlier answer, reused)

```
route1_stop06_line | Test B | gpt-6.1-sol | repeat 1 | from cache
-----------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          The rectangle contains an unbroken stretch of a single solid white longitudinal line to
                      the right of my car.
    Evidence          full
    Output 1          white_solid, position right
Step 2  Rule          Under CN-6.2.1, a single solid white lane line prohibits vehicles from crossing it.
    Cited passage     CN-6.2.1: "The no-crossing lane line separates vehicles travelling in the same direction
                      and prohibits vehicles on the solid-line side from crossing. It has two forms: single
                      solid white and broken-solid white."
Step 3  Decide
    cross_line                prohibited      The visible solid white line prohibits crossing under CN-6.2.1.
    go_straight               not_applicable  not governed by this marking
    turn_left                 not_applicable  not governed by this marking
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label white_solid); Output 2 correct; evidence group correct; citation
                      accepted
Tokens                3723 input + 298 output (hidden reasoning 0) | 5.11 s | $0.00000
```

### A  Test A, US (image only), arrow  (earlier answer, reused)

```
route1_stop06_arrow | Test A | gpt-6.1-sol | repeat 1 | from cache
------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          A white lane-use arrow inside the rectangle has a bent shaft and a single head pointing
                      left.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          In the United States, a left-turn lane arrow requires a leftward movement rather than
                      proceeding straight or turning right, but does not by itself prohibit a U-turn.
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking.
    go_straight               prohibited      The left-only arrow prohibits proceeding straight.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow prohibits a right turn.
    u_turn                    allowed         The left-turn arrow does not itself prohibit a U-turn.
    enter_center_lane_to_wait not_applicable  Not governed by this marking.
Step 4  Check         consistent
Model's summary       **Clarifying U-turn rules**  I'm considering whether U-turns are allowed when there's an
                      arrow pointing left in the U.S. Generally, it seems like left arrows don't prohibit
                      U-turns, so that might be a go-ahead! I want to ensure I have that right because traffic
                      rules can vary, and it’s important to understand the nuances. I should double-check
                      local regulations to confirm this, just in case there are exceptions. But overall, it's
                      looking like that might not be a problem!
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct
Tokens                2584 input + 326 output (hidden reasoning 21) | 6.98 s | $0.00000
```

### B  Test B, US (image + MUTCD), arrow  (earlier answer, reused)

```
route1_stop06_arrow | Test B | gpt-6.1-sol | repeat 1 | from cache
------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          A single white bent arrow with its head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          Under US-3B.23-01, the left-pointing lane-use arrow indicates a left-turn movement, not
                      straight, right-turn, or U-turn movements.
    Cited passage     US-3B.23-01: "Lane-use arrow markings are used to indicate the mandatory or permissible
                      movements in certain lanes and in two-way left-turn lanes."
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               prohibited      The left-only arrow does not permit a straight movement.
    turn_left                 allowed         The left-pointing arrow permits a left turn.
    turn_right                prohibited      The left-only arrow does not permit a right turn.
    u_turn                    prohibited      The left-only arrow does not indicate a U-turn movement.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct (u_turn: label allowed); evidence
                      group correct; citation accepted
Tokens                4187 input + 315 output (hidden reasoning 0) | 5.68 s | $0.00000
```

### C  Test B, CN rules on a US road, arrow  (earlier answer, reused)

```
route1_stop06_arrow | Test B | gpt-6.1-sol | repeat 1 | from cache
------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          A white bent arrow with a single head pointing left is visible inside the rectangle.
    Evidence          full
    Output 1          arrow / left, position in_ego_lane
Step 2  Rule          Under CN-5.13.1, the left-pointing guide arrow indicates left turns only, excluding
                      straight travel, right turns and U-turns.
    Cited passage     CN-5.13.1: "Guide arrows indicate the direction of travel for vehicles. (Table 1
                      meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                      straight or U-turn; left or U-turn; left or right only; merge left; merge right.)"
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               prohibited      The left-only arrow does not indicate straight travel.
    turn_left                 allowed         The left-pointing arrow indicates a left turn.
    turn_right                prohibited      The left-only arrow does not indicate a right turn.
    u_turn                    prohibited      The left-only arrow does not indicate a U-turn.
    enter_center_lane_to_wait not_applicable  not governed by this marking
Step 4  Check         consistent
Result                Output 1 correct (label arrow/left); Output 2 correct; evidence group correct; citation
                      accepted
Tokens                3723 input + 309 output (hidden reasoning 0) | 5.74 s | $0.00000
```

## Stop 7: two-way left-turn lane

Road 67 lane 2. Intent from the route: enter the centre lane to wait for a left turn. The car (B): enters the centre lane to wait for a left turn, then (no driveway here) moves back. With C it would: enter.

### A  Test A, US (image only), centre  (earlier answer, reused)

```
route1_stop07_centre | Test A | gpt-6.1-sol | repeat 1 | from cache
-------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions (no rule passages); prompt
                      prompts/v3
Step 1  Look          The rectangle shows a lane to the left of my car bordered on both sides by paired yellow
                      lines, with a solid line on the outside and a broken line on the inside of each pair.
    Evidence          full
    Output 1          two_way_left_turn_lane, position left
Step 2  Rule          In the United States, these paired solid-and-broken yellow boundaries designate a two-
                      way left-turn lane that may be entered to wait for and make a left turn.
Step 3  Decide
    cross_line                not_applicable  not governed by this marking
    go_straight               not_applicable  not governed by this marking
    turn_left                 allowed         The yellow solid-and-broken boundaries designate a center lane
                                              from which left turns are allowed.
    turn_right                not_applicable  not governed by this marking
    u_turn                    not_applicable  not governed by this marking
    enter_center_lane_to_wait allowed         The yellow solid-and-broken boundaries designate a center lane
                                              that may be entered to wait for a left turn.
Step 4  Check         consistent
Model's summary       **Identifying lane markings**  I'm trying to figure out the lane markings: there are two
                      edges with a solid and dashed line on the left boundary, which appears to be double
                      solid. I need to check both edges closely; the solid and dashed lines are visible from
                      certain coordinates. The center lane should be clear. It seems I need to define a two-
                      way lane rectangle, where the right edge is solid and dashed on the left, and the left
                      is solid with a dashed right edge.
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct
Tokens                2584 input + 416 output (hidden reasoning 77) | 8.24 s | $0.00000
```

### B  Test B, US (image + MUTCD), centre  (earlier answer, reused)

```
route1_stop07_centre | Test B | gpt-6.1-sol | repeat 1 | from cache
-------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          Inside the rectangle, a lane to the left of my car is bordered on both sides by paired
                      yellow lines, each with a solid outer line and a broken inner line with visible segments
                      and gaps.
    Evidence          full
    Output 1          two_way_left_turn_lane, position left
Step 2  Rule          Under US-3B.05-01, a lane bordered on both sides by solid and broken yellow lines, with
                      the broken lines facing inward, may be used by traffic in either direction as part of a
                      left-turn maneuver.
    Cited passage     US-3B.05-01: "If a two-way left-turn lane that is never operated as a reversible lane is
                      used, the lane line pavement markings on each side of the two-way left-turn lane shall
                      consist of a normal width broken yellow line and a normal width solid yellow l"
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking as a two-way left-turn lane.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The paired yellow boundaries with broken lines inward identify a
                                              lane usable for left-turn maneuvers.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The paired yellow boundaries with broken lines inward permit
                                              entering the center lane as part of a left-turn maneuver.
Step 4  Check         consistent
Model's summary       **Identifying lane edges**  I need to identify a twlt lane that is rectangular and
                      encompasses both edges. I see that there are two edges: a solid and a broken yellow
                      line, with the ego positioned right of center. I should ensure that both edges are
                      clearly visible in pairs. It looks like entering is allowed from the left side. Let's
                      make sure I have all the details right!
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 correct; evidence group
                      correct; citation accepted
Tokens                4187 input + 406 output (hidden reasoning 38) | 7.5 s | $0.00000
```

### C  Test B, CN rules on a US road, centre  (earlier answer, reused)

```
route1_stop07_centre | Test B | gpt-6.1-sol | repeat 1 | from cache
-------------------------------------------------------------------
Input                 photo with the target marking in a cyan box, the instructions and the rule passages of
                      the region; prompt prompts/v3
Step 1  Look          The rectangle contains a centre lane bounded on both sides by paired yellow lines, with
                      solid outer lines and broken inner lines showing painted segments and gaps.
    Evidence          full
    Output 1          two_way_left_turn_lane, position left
Step 2  Rule          No supplied passage specifically covers a two-way left-turn lane; under the supplied
                      marking definitions, it permits entering the centre lane to wait for a left turn and
                      turning left out of it.
    Cited passage     none
Step 3  Decide
    cross_line                not_applicable  Not governed by this marking as a two-way left-turn lane.
    go_straight               not_applicable  Not governed by this marking.
    turn_left                 allowed         The two-way left-turn lane permits turning left out of the
                                              centre lane.
    turn_right                not_applicable  Not governed by this marking.
    u_turn                    not_applicable  Not governed by this marking.
    enter_center_lane_to_wait allowed         The two-way left-turn lane permits entering to wait for a left
                                              turn.
Step 4  Check         consistent
Model's summary       **Identifying lane boundaries**  I need to identify a center lane with solid and dashed
                      edges, which forms a visible rectangle that spans both edges. It looks likely like a
                      two-way left turn lane. I see that the left boundary has a solid pair, while the right
                      boundary is solid on the ego side and broken on the inner side. The target rectangle
                      does indeed enclose the center lane, so I’ll choose the two-way option.
Result                Output 1 correct (label two_way_left_turn_lane); Output 2 not scored; evidence group
                      correct; citation none_needed
Tokens                3723 input + 393 output (hidden reasoning 62) | 8.87 s | $0.00000
```
