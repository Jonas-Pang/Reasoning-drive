# Reasoning of lane run 20261117_022231_laneC_UK

```text
lingoqa__train_27ca312fb6ce3cb70036e317c6c758ba_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a wet, urban street with buildings lining both sides. Ahead, the road
                        continues into the distance, appearing to be a standard road section rather than an
                        immediate intersection or ramp. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the lane.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, words, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is a solid white
                        edge_line, and the right boundary is a dashed white lane_line, which fits the roles
                        assigned. | markings: There are no markings in my lane to contradict the boundaries or
                        each other. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: On a road having a single broken line along with a solid line, the
                        driver of the vehicle driving on the left of broken line may cross the broken line in
                        order to o vertake, but shall return to his lane after completing the manoeuvre,
                        observing the safety precautions specified in regulation 12. [[IN-6(7)]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so the default permissive
                        rule applies. [null]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is an edge_line
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (WRONG, label not_determined): Allowed, as the right boundary is a dashed
                        lane_line and [IN-6(7)] permits crossing the broken line to overtake.
Step 6  go_straight     allowed (contested, label not_determined): Allowed, as there are no markings in my
                        lane prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane governing this action.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane governing this action.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You are in the leftmost lane, which is the edge lane. You may change left after
                        signaling, and you may change right to overtake, as the dividing line is broken. You
                        may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb']
Tokens                  in 5792, out 1067, 26.68 s

lingoqa__train_d21bf5635928983657b67b4aa8a13fac_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where traffic flow is visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific lane markings like arrows, text, or areas
                        are visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The left boundary is a solid
                        white lane line, and the right boundary is a dashed white lane line, which fits the
                        roles of lane_line. | markings: There are no arrows, words, or areas in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element. [null]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a lane_line
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (contested, label prohibited): Allowed, as the right boundary is a lane_line
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane prohibiting
                        straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       allowed: Allowed, as there are no markings in my lane prohibiting a left turn, and the
                        boundaries do not prohibit it.
Step 6  turn_right      allowed: Allowed, as there are no markings in my lane prohibiting a right turn, and
                        the boundaries do not prohibit it.
Step 6  u_turn          allowed: Allowed, as there are no markings in my lane prohibiting a U-turn, and the
                        boundaries do not prohibit it.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of two. You may change lanes after signaling, and all
                        movements (straight, left, right, U-turn) appear permitted by the lane markings, but
                        you should observe the intersection ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'turn_right allowed
                        although a prohibited-movement marking forbids it']
Tokens                  in 5792, out 1009, 24.08 s

lingoqa__train_dde41275b6a47da6fe2992ae2f1b7673_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the lane closest
                        to the center of the road. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol painted on the road.; line:stop_line
                        (partial): A white dashed line marking the lane boundary ahead.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles
                        (both are lane_lines). | roles: The white dashed lines fit the role of lane_line. |
                        markings: The bicycle symbol is within the lane, and the stop line is ahead, which is
                        consistent. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            symbol:bike: A vehicle of that class shall drive in that lane only. [[IN-6(2)]]
Step 5  Rule            line:stop_line: A motor vehicle facing the red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a dashed
                        lane_line and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (WRONG, label not_determined): Allowed, as the right boundary is a dashed
                        lane_line and [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in a bicycle lane, so you must adhere to the rules for this special lane. You
                        may change lanes after signaling, and you may proceed straight ahead, but you must
                        stop before the marked stop line if required by traffic signals or pedestrian
                        crossings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['leftmost lane, but
                        a lane line on the left']
Tokens                  in 5792, out 1118, 13.85 s

lingoqa__train_e12d585d1cf304230d7d39744f0797cd_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into a built-up area, but no immediate intersection or ramp is clearly
                        visible in the lane ahead. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the lane, followed by a curb and a
                        sidewalk/grass verge.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, words, symbols, areas, or lines are
                        visible across my lane in the immediate view.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The left boundary is solid
                        white and has a curb, fitting the role of an edge_line. The right boundary is dashed
                        white, fitting the role of a lane_line. | markings: There are no markings in my lane
                        to contradict the boundaries or each other. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so the default permissive
                        rule applies. [null]
Step 6  change_left     allowed (contested, label not_determined): Allowed, as the left boundary is an
                        edge_line and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed lane_line and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane governing this action.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane governing this action.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; no action is allowed
                        against a prohibition, and all decisions are based on visible features.
Advice                  You are in the leftmost lane; you may change left or right after signaling. You may
                        proceed straight ahead, but you cannot turn left or right based on the current
                        markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb']
Tokens                  in 5792, out 1065, 27.76 s

lingoqa__train_f2b37a8b7f23380de3834e8165fd2620_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential street with buildings on the left side. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 1, mine 1, full)
Step 2  Left            There is a curb and a continuous white line marking the edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a continuous white line marking the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): The text 'SLOW' is painted across the lane.
Step 4  Cross-check     position: The lane count (1) and ego lane index (1) agree with the boundary roles
                        (both are edge_lines). | roles: The white solid line on the left fits the role of an
                        edge_line with a curb, and the white solid line on the right fits the role of an
                        edge_line without a curb. | markings: The text 'SLOW' is present in the lane and does
                        not contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:other: No specific rule passage covers the meaning of the 'SLOW' text marking.
                        [null]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid edge_line,
                        and [IN-6(1)] mandates driving within the lane and changing lanes only after
                        signaling/marking.
Step 6  change_right    prohibited: prohibited: The right boundary is a solid edge_line, and [IN-6(1)]
                        mandates driving within the lane and changing lanes only after signaling/marking.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked place to wait for a left turn or
                          a two-way left-turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should proceed straight in your current lane. Lane changes are prohibited by the
                        solid edge lines, and you should observe the 'SLOW' marking by driving cautiously.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 5792, out 1041, 15.27 s
```
