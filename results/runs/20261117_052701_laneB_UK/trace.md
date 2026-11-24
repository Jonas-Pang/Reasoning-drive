# Reasoning of lane run 20261117_052701_laneB_UK

```text
lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a street scene in a built-up area, and ahead there is a continuation of the
                        road with traffic moving in both directions. My car is in one of the lanes moving
                        forward. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the center of the road, visible
                        ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes in my direction. | roles: The solid white lines on both sides fit the role of
                        lane_line. | markings: The dashed line ahead is interpreted as a stop line, which is
                        consistent with the lane markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where a vehicle must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white lane_line and [UK-Rule131] states you should keep between lane dividers.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white lane_line and [UK-Rule131] states you should keep between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13640, out 1024, 6.12 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, appearing to be a straight stretch of road. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the center of the road ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (both boundaries are lane_lines, indicating adjacent lanes). | roles: The color
                        (white) and pattern (dashed) of both boundaries fit the role of a lane_line. |
                        markings: The white dashed line ahead is interpreted as a stop line, which is
                        consistent with the lane markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where traffic must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a dashed white
                        line, and [UK-Rule131] recommends keeping between lane dividers.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed white line, and [UK-
                        Rule131] recommends keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules, as the dashed lines permit
                        lane changes and the absence of restrictive markings allows straight travel.
Advice                  You may change lanes left or right as the lane dividers are dashed, and you may
                        proceed straight ahead. You should observe the stop line ahead, which indicates where
                        you must stop if there is a signal or stop sign.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13640, out 1037, 11.41 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a wet, urban street with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or lane end
                        visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, words, symbols, areas, or lines are
                        visible across my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes in my direction. | roles: The color (white) and pattern (solid) of both
                        boundaries fit the role of a lane_line. | markings: The lack of markings in my lane is
                        consistent with the boundaries defining the lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            no_turn:right: No specific rule passage applies to this marking as it was not
                        observed. [null]
Step 6  change_left     prohibited (contested, label not_determined): prohibited: The left boundary is a solid
                        white lane_line, and there is no rule passage stating otherwise.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited: The right boundary is a solid
                        white lane_line, and there is no rule passage stating otherwise.
Step 6  go_straight     allowed (contested, label not_determined): allowed: Nothing restricts carrying on
                        straight along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines. No specific instructions are given for turning
                        movements.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13640, out 1025, 6.83 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings on both sides, and ahead there is a junction
                        marked by a box junction. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line marking the division between lanes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): A white box junction marking is visible ahead.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two. | roles: The left boundary is solid white, fitting
                        the role of an edge line, and the right boundary is dashed white, fitting the role of
                        a lane line. | markings: The box junction marking is ahead in my lane, which is
                        consistent with the lane configuration. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: This line indicates the edge of the carriageway at a road junction,
                        exit from a private drive onto a public road, or the start of a cycle lane. [[UK-
                        TSRGD-S11P4-item8]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            area:grid: The yellow criss-cross marking conveys the prohibition that a person must
                        not cause a vehicle to enter the box junction so that the vehicle has to stop within
                        the box junction due to the presence of stationary vehicles. [[UK-TSRGD-11(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the right boundary is a lane line
                        and the left boundary is an edge line, and there is no marking allowing a change to
                        the left.
Step 6  change_right    allowed (WRONG, label not_determined): allowed, because the right boundary is a dashed
                        lane line, and there is no marking prohibiting a lane change to the right.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane that restrict going straight ahead.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane that allow turning left.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane that allow turning right.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane that allow a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You may change right into the adjacent lane, and you may proceed straight ahead, but
                        you must not enter the box junction if it would require you to stop due to stationary
                        traffic.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 13640, out 1055, 11.14 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road with buildings lining both sides. Ahead, the road continues
                        into a built-up area, and there is no immediate intersection or ramp visible. (lanes
                        2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): A white dashed line marking the edge of the carriageway on the
                        left side of my lane, near the bottom of the photo, with a bicycle symbol painted on
                        it.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes of travel in my direction. | roles: The color (white) and pattern (dashed) of
                        both boundaries fit the role of a lane_line. | markings: The bicycle symbol is on the
                        edge line, which is consistent with it being a lane boundary marking. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            line:crosswalk: No vehicle may proceed past the transverse line nearer the cycle track
                        in a manner or at a time likely to endanger any cyclist or to cause such a cyclist to
                        change speed or course in order to avoid an accident. [[UK-TSRGD-7(d)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, and [UK-Rule131] recommends keeping between lane dividers, which permits lane
                        changes when safe.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and [UK-
                        Rule131] recommends keeping between lane dividers, which permits lane changes when
                        safe.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, and lane changes are permitted as long as
                        you keep between the dashed lane dividers. You may proceed straight ahead, but you
                        should be aware of the cycle crossing area marked on the left side of your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13640, out 1102, 6.45 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road with buildings lining both sides. Ahead, the road continues
                        into a built-up area, and there is no immediate intersection or ramp visible. (lanes
                        2, mine 1, full)
Step 2  Left            There is a white dashed line marking the boundary of the lane.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line marking the boundary of the lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane boundary on the right.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles, as
                        both boundaries are lane lines. | roles: The white dashed lines fit the role of
                        lane_line. | markings: The stop line marking is consistent with the lane boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where a vehicle must stop at signals or a 'Stop'
                        sign. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed white
                        line, and [UK-Rule131] permits keeping between lane dividers.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and [UK-
                        Rule131] permits keeping between lane dividers.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in the lane, and nothing restricts carrying on straight along the lane.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane, and you may change left or right as the lane markings
                        permit. You may proceed straight ahead, but you must stop at the visible stop line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13640, out 1001, 6.96 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there is a continuation of
                        the road with traffic moving in both directions. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the edge of the lane ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The left
                        boundary is solid white, fitting the role of a lane_line, and the right boundary is
                        dashed white, fitting the role of a lane_line. | markings: The stop line is visible
                        ahead, and it is consistent with the lane markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_line: This line indicates where you must stop at signals or police control.
                        [[UK-HC_MARKINGS-p1]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a solid white lane_line, and there is
                        no rule prohibiting a lane change.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane_line, and there
                        is no rule prohibiting a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road, and you must stop at the visible stop
                        line ahead. You may change lanes left or right, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 13640, out 999, 6.6 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there is a junction where the
                        road continues and other lanes are visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, words, symbols, areas, or lines are
                        visible across my lane from the bottom to the end.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        left boundary is solid white, and the right boundary is dashed white, which fits the
                        roles of lane_line. | markings: There are no markings in my lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            no_turn:right: No specific rule passage applies to this marking as it was not
                        observed. [null]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a solid white
                        lane line, and no rule prohibits changing left.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed white lane line, and no
                        rule prohibits changing right.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane that govern turning left.
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane that govern turning right.
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         The actions are consistent with the observations and rules, as the boundaries permit
                        lane changes and the absence of markings permits straight travel.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings governing turns, you should proceed with caution towards the
                        junction ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 13640, out 999, 7.16 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a typical urban street with buildings on both sides, and the road continues
                        straight ahead into the distance. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the carriageway.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line marking the division between lanes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, words, symbols, areas, or lines are
                        visible across the lane in the visible stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two. | roles: The left boundary is a solid white
                        edge_line, and the right boundary is a dashed white lane_line, which is consistent. |
                        markings: There are no markings in the lane to contradict the boundaries or each
                        other. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: This marking indicates the edge of the carriageway at a road junction,
                        exit from a private drive onto a public road, or the start of a cycle lane. [[UK-
                        TSRGD-S11P4-item8]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            no_turn:right: No specific rule passage applies to this placeholder marking as no
                        markings were seen. [null]
Step 6  change_left     allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, and [UK-Rule131] recommends keeping between lane dividers.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        edge_line, and [UK-TSRGD-S11P4-item8] indicates the edge of the carriageway.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You should stay in the left lane to proceed straight, as changing right is prohibited
                        by the solid edge line. Since there are no specific markings for turning, you must
                        obey general traffic laws for turning movements.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb', 'change_right prohibited across a
                        broken lane line']
Tokens                  in 13640, out 1090, 11.41 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a typical urban street with trees lining both sides, and the road continues
                        into the distance. My car is in the lane closest to the left side of the road. (lanes
                        2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the carriageway, followed by a curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): A painted word 'BUS' is visible on the road surface.; arrow:straight
                        (full): A painted arrow pointing straight ahead is visible.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is an edge line, and the right boundary is a lane line, indicating I
                        am in the leftmost lane. | roles: The left boundary is solid white and has a curb,
                        fitting the role of an edge line. The right boundary is dashed white, fitting the role
                        of a lane line. | markings: The 'BUS' text and the straight arrow are within my lane
                        and are consistent with the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: This marking indicates the edge of the carriageway at a road junction,
                        exit from a private drive onto a public road, or the start of a cycle lane. [[UK-
                        TSRGD-S11P4-item8]]
Step 5  Rule            right_boundary: You should keep between lane dividers, which are short, broken white
                        lines used on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            text:bus: Bus lanes are shown by road markings and signs that indicate which (if any)
                        other vehicles are permitted to use the bus lane. [[UK-Rule141]]
Step 5  Rule            arrow:straight: White direction arrows on the road indicate that you need to get back
                        onto your side of the road. [[UK-Rule128-2]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white edge
                        line, and while no specific rule prohibits changing left from an edge line, the solid
                        line suggests a fixed boundary.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane line, and [UK-
                        Rule128] permits crossing double white lines where the nearer line is broken if it is
                        safe.
Step 6  go_straight     allowed (contested, correct): allowed: The arrow:straight marking allows proceeding
                        straight ahead, and no other marking prohibits it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing a left turn.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing a right turn.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the bus lane, so you should adhere to any restrictions indicated by the
                        'BUS' marking. You may change right if safe, and you are permitted to go straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight', 'text:bus'], missed ['text:other']), actions True, unsafe [],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 13640, out 1168, 7.33 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction where
                        the road continues and other traffic is present. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line marking the edge of the carriageway on the right.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid yellow line runs along the right edge of the
                        carriageway.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid yellow
                        edge_line, which fits their roles. | markings: The solid yellow line on the right is
                        interpreted as a stop/yield line, which is consistent with its appearance as a solid
                        line near the edge, although its specific function as a stop/yield line is not fully
                        confirmed by the visual evidence alone. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: The double and single red lines used on Red Routes indicate that
                        stopping to park, load/unload or to board and alight from a vehicle (except for a
                        licensed taxi or if you hold a Blue Badge) is prohibited. [[UK-HC_MARKINGS-p2-8]]
Step 5  Rule            line:stop_yield: You must give way to traffic on a major road when approaching a
                        junction indicated by this marking. [[UK-HC_MARKINGS-p1-4]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a solid white
                        lane_line, and no rule prohibits changing left.
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited, as the right boundary is a solid
                        yellow edge_line, and the rule for this line type is not explicitly stated to permit
                        changing right, but the solid nature suggests restriction.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules, noting that the solid
                        yellow line on the right is interpreted as a stop/yield line, which governs the right
                        boundary's role.
Advice                  You may change left into the adjacent lane, and you may proceed straight ahead. You
                        must give way to traffic on a major road as indicated by the marking near the right
                        edge of your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'go_straight allowed without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 13640, out 1121, 8.45 s
```
