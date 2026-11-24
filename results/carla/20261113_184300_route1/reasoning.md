# Reasoning at every stop: route1 on Town03

Model gpt-6.1-sol, reasoning effort low, prompt prompts/v3. A = Test A US; B = Test B US (MUTCD); C = Test B with the China passages on the same US road.

## Stop 1: broken white lane line

Road 65 lane 2. Intent from the route: change lane across the line. The car (B): changes to the right lane. With C it would: cross.

### A  Test A, US (image only), line

```
route1_stop01_line | Test A | gpt-6.1-sol | repeat 1
----------------------------------------------------
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
Tokens                2584 input + 283 output (hidden reasoning 0) | 5.89 s | $0.00800
```

### B  Test B, US (image + MUTCD), line

```
route1_stop01_line | Test B | gpt-6.1-sol | repeat 1
----------------------------------------------------
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
Tokens                4187 input + 292 output (hidden reasoning 0) | 5.81 s | $0.01129
```

### C  Test B, CN rules on a US road, line

```
route1_stop01_line | Test B | gpt-6.1-sol | repeat 1
----------------------------------------------------
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
Tokens                3723 input + 296 output (hidden reasoning 0) | 6.54 s | $0.01041
```

## Stop 6: junction approach: left-turn arrow and the line to the right lane

Road 44 lane -4. Intent from the route: turn_right. The car (B): right not allowed from this lane; the right line may be crossed -> changes lane, then goes right. With C it would: stay in lane and take the lane's own movement.

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

### A  Test A, US (image only), line

```
route1_stop06_line | Test A | gpt-6.1-sol | repeat 1
----------------------------------------------------
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
Tokens                2584 input + 283 output (hidden reasoning 0) | 4.77 s | $0.00800
```

### B  Test B, US (image + MUTCD), line

```
route1_stop06_line | Test B | gpt-6.1-sol | repeat 1
----------------------------------------------------
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
Tokens                4187 input + 298 output (hidden reasoning 0) | 4.63 s | $0.01135
```

### C  Test B, CN rules on a US road, line

```
route1_stop06_line | Test B | gpt-6.1-sol | repeat 1
----------------------------------------------------
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
Tokens                3723 input + 298 output (hidden reasoning 0) | 5.11 s | $0.01043
```

## Stop 7: two-way left-turn lane

Road 67 lane 2. Intent from the route: enter the centre lane to wait for a left turn. The car (B): enters the centre lane to wait for a left turn, then (no driveway here) moves back. With C it would: enter.

### A  Test A, US (image only), centre

```
route1_stop07_centre | Test A | gpt-6.1-sol | repeat 1
------------------------------------------------------
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
Tokens                2584 input + 416 output (hidden reasoning 77) | 8.24 s | $0.00933
```

### B  Test B, US (image + MUTCD), centre

```
route1_stop07_centre | Test B | gpt-6.1-sol | repeat 1
------------------------------------------------------
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
Tokens                4187 input + 406 output (hidden reasoning 38) | 7.5 s | $0.01243
```

### C  Test B, CN rules on a US road, centre

```
route1_stop07_centre | Test B | gpt-6.1-sol | repeat 1
------------------------------------------------------
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
Tokens                3723 input + 393 output (hidden reasoning 62) | 8.87 s | $0.01138
```
