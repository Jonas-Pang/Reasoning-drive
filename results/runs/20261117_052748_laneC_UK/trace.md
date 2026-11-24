# Reasoning of lane run 20261117_052748_laneC_UK

```text
lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a street scene in a built-up area, and ahead there is a continuation of the
                        road with other vehicles and buildings on both sides. My car is in one of the lanes
                        traveling forward. (lanes 2, mine 1, full)
Step 2  Left            There is a curb separating the roadway from the sidewalk/building area.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No lane markings are visible across the lane from
                        bottom to end.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line (curb), and the right boundary is a lane_line
                        (separating from another lane). | roles: The left boundary is an edge_line due to the
                        curb, and the right boundary is a lane_line due to the solid white line separating it
                        from the adjacent lane. | markings: There are no arrows, words, or areas in the lane
                        to contradict the boundaries. | unseen: I reported that no stop line is visible, which
                        is an observation based on the image. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: No specific rule passage covers the general presence of a stop line
                        when no other governing marking is present. [null]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is an edge_line
                        and no marking prohibits the change, and [IN-6(1)] permits lane changes with a signal.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a lane_line and no marking
                        prohibits the change, and [IN-6(1)] permits lane changes with a signal.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited markings
                        in the lane, and nothing restricts carrying on straight along the lane.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; no action is allowed
                        against a prohibition, and all decisions are based on visible features or lack
                        thereof.
Advice                  You are in the left lane of two lanes; you may change lanes after signaling, and you
                        may proceed straight ahead. Since there are no specific turn markings, you must follow
                        general traffic laws for turning.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb']
Tokens                  in 5792, out 1118, 6.51 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane boundary ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is one of two lanes in my direction. | roles: The white dashed lines fit the role
                        of lane_line, as they separate lanes of traffic moving in the same direction. |
                        markings: The stop line marking is consistent with the lane boundaries; it is a
                        transverse line within the lane. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a dashed
                        lane_line and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed lane_line and [IN-6(1)]
                        permits lane changes after signaling.
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
Advice                  You are in the left lane of a two-lane road. You may change lanes after signaling, and
                        you may proceed straight ahead. You should be aware of the stop line ahead, which
                        suggests an upcoming intersection or crossing.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5792, out 1073, 8.4 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a wet, urban street with buildings lining both sides. Ahead, the road
                        continues into a built-up area, and there is no immediate intersection or lane end
                        visible. (lanes 2, mine 1, full)
Step 2  Left            The left boundary is marked by a solid white line, and beyond it, there is a curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           The right boundary is marked by a solid white line, and beyond it, there is no visible
                        curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No lane markings are visible across the lane from
                        bottom to end.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes. | roles: The solid white line on the left fits
                        the role of an edge_line, and the solid white line on the right fits the role of a
                        lane_line. | markings: There are no arrows, words, or areas in the lane to contradict
                        the boundaries. | unseen: I reported 'line:stop_line' with insufficient evidence
                        because no clear stop line was visible. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: No specific rule passage was found for a visible stop line in this
                        context. [null]
Step 6  change_left     allowed (contested, label not_determined): Allowed, as the left boundary is a solid
                        white edge_line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited, as the right boundary is a solid
                        white lane_line, and [IN-6(1)] requires lane changes to be done only after signaling.
Step 6  go_straight     allowed (contested, label not_determined): Allowed, as no arrow prohibits going
                        straight, and the boundaries do not restrict this action.
Step 6  turn_left       not_applicable: Not_applicable, as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking
                        governing this action.
Step 6  u_turn          not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking
                        governing this action.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed against a prohibition, and all decisions are based on visible features or lack
                        thereof.
Advice                  You are in the leftmost lane of two. You may change left after signaling, but changing
                        right is prohibited by the solid white line. You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb']
Tokens                  in 5792, out 1058, 6.74 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street with buildings on both sides, and ahead there is a junction or
                        intersection where the road continues. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the lane, followed by a curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two. | roles: The left boundary is solid white and has a
                        curb, fitting the role of an edge_line. The right boundary is dashed white, fitting
                        the role of a lane_line. | markings: The dashed line observed is interpreted as a stop
                        line, which is consistent with the lane markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the right boundary is a dashed
                        line, and the left boundary is an edge line, but the rule [IN-6(1)] requires signaling
                        for lane changes.
Step 6  change_right    allowed (WRONG, label not_determined): Prohibited, as the right boundary is a dashed
                        line, and the rule [IN-6(1)] requires signaling for lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited markings
                        in the lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited markings in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited markings in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited markings in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which is bordered by an edge line on the left and a
                        dashed lane line on the right. You may proceed straight, but if you wish to change
                        lanes, you must signal first. You must stop before the visible stop line if a traffic
                        signal is red.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['area:grid']), actions False, unsafe [], citation
                        unlisted, contradictions ['change_left allowed across a curb']
Tokens                  in 5792, out 1103, 8.59 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road with buildings lining both sides. Ahead, the road continues
                        into a built-up area, and there is no immediate intersection or ramp visible. (lanes
                        2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A bicycle symbol painted on the road near the bottom left of the
                        photo.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes in my direction. | roles: The color (white) and pattern (solid) of both
                        boundaries fit the role of a lane_line. | markings: The bicycle symbol is present in
                        my lane and does not contradict the lane boundaries or the general flow of traffic. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            symbol:bike: No specific rule passage was found that dictates the action based on the
                        bicycle symbol in this context.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white lane_line, and
                        [IN-6(1)] mandates that lane changes must be made only after giving a proper signal or
                        road marking or signage.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white lane_line, and
                        [IN-6(1)] mandates that lane changes must be made only after giving a proper signal or
                        road marking or signage.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: There is no marked waiting area or two-way left-turn lane visible
                          ahead of my lane.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You should remain in your current lane to proceed straight. Lane changes to the left
                        or right are prohibited by the solid lane markings, and you should use the lane
                        appropriate for your intended turn if you plan to turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5792, out 1076, 6.05 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the edge of the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is one of two lanes in my direction. | roles: The white dashed lines fit the role
                        of lane_line, as they separate lanes of traffic moving in the same direction. |
                        markings: The stop line marking is consistent with the boundaries, as it is located
                        within the lane. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a dashed
                        lane_line and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed lane_line and [IN-6(1)]
                        permits lane changes after signaling.
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
Advice                  You are in the left lane of a two-lane road. You may change lanes after signaling, and
                        you may proceed straight. You should be aware of the stop line ahead, which suggests
                        an upcoming controlled crossing or intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5792, out 1072, 6.71 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban setting, and ahead there is a
                        junction/intersection visible in the distance. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the lane, followed by a curb and a
                        sidewalk area.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the stop line is visible ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is solid white and
                        functions as an edge_line, and the right boundary is dashed white and functions as a
                        lane_line, which is consistent. | markings: The stop line is present and is consistent
                        with the lane markings. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (correct): Allowed, as the right boundary is a dashed line, and the left
                        boundary is an edge line, which permits lane changes if signaled [IN-6(1)].
Step 6  change_right    allowed (correct): Prohibited, as the right boundary is a dashed line, but the lane
                        change must be signaled [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight [no marking governs this
                        action].
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area is visible [not_applicable].
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area is visible [not_applicable].
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area is visible [not_applicable].
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible [not_applicable].
Step 7  Reflect         The actions are consistent with the observations and rules, as lane changes are
                        governed by the boundary lines and the general rule [IN-6(1)].
Advice                  You are in the leftmost lane, which is bordered by an edge line on the left. You may
                        change left or right after signaling, and you may proceed straight. You must stop
                        before the visible stop line if a traffic signal is red.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb']
Tokens                  in 5792, out 1113, 6.88 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there is a junction or
                        intersection where the road continues. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the lane, followed by a curb and a
                        sidewalk area.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A dashed white line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two. | roles: The left boundary is solid white and has a
                        curb, fitting the role of an edge_line. The right boundary is dashed white, fitting
                        the role of a lane_line. | markings: The dashed line observed is interpreted as a stop
                        line, which is consistent with the lane markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the right boundary is a dashed
                        line, and the left boundary is an edge line, but the rule [IN-6(1)] requires signaling
                        for lane changes.
Step 6  change_right    allowed (correct): Prohibited, as the right boundary is a dashed line, and the rule
                        [IN-6(1)] requires signaling for lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited markings
                        in the lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited markings in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited markings in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited markings in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which is bordered by an edge line on the left. You may
                        proceed straight or change lanes, but you must signal any lane change. You should stop
                        before the visible stop line if a traffic signal requires it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb']
Tokens                  in 5792, out 1100, 6.73 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a street scene with buildings on both sides, and the road continues ahead into
                        the distance. My car is in the lane closest to the left side of the road. (lanes 2,
                        mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No lane markings are visible across the lane from
                        bottom to the end of the visible road.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is an edge line, and the right boundary is a lane line, indicating I
                        am in the leftmost lane. | roles: The left boundary is a solid white edge line, and
                        the right boundary is a dashed white lane line, which fits their roles. | markings:
                        There are no arrows, words, or areas in my lane to contradict the boundaries. |
                        unseen: I reported that no stop line is visible, which is an observation based on the
                        image. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: No specific rule passage covers the general presence of a stop line
                        when no other governing marking is present. [null]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is an edge line
                        and [IN-6(1)] permits driving within the lane, and no marking prohibits it.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed lane line and [IN-6(1)]
                        permits lane changes after signaling, and no marking prohibits it.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows in my lane and nothing
                        restricts carrying on straight along my lane.
Step 6  turn_left       allowed: Allowed, as there are no arrows or prohibited-movement markings in my lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      allowed: Allowed, as there are no arrows or prohibited-movement markings in my lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          allowed: Allowed, as there are no markings in my lane that prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, and all movements are permitted based on the visible
                        markings. You should signal appropriately if you intend to change lanes.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb', 'turn_left, turn_right, u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 5792, out 1026, 8.45 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with trees lining both sides, and the road continues
                        into the distance without an immediate intersection visible. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane on the left.
                        white dashed, curb yes, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): White dashed line markings on the road surface in front of
                        the car.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes in my direction. | roles: The white dashed lines on both sides fit the role of
                        lane_line. | markings: The line:stop_line is visible ahead, and it is consistent with
                        the lane markings. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a dashed
                        lane_line and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed lane_line and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road; you may change lanes after signaling. You
                        should stop before the visible stop line if a traffic signal requires it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['text:other']), actions True, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left', 'change_left
                        allowed across a curb']
Tokens                  in 5792, out 1044, 6.43 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection where the road continues. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the edge of the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes in the direction of travel. | roles: The color (white) and pattern (solid) of
                        both boundaries fit the role of a lane_line. | markings: The stop line marking is
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white lane_line and [IN-6(1)] requires driving within the lane and changing lanes only
                        after giving a proper signal or road marking or signage.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited, because the right boundary is a
                        solid white lane_line and [IN-6(1)] requires driving within the lane and changing
                        lanes only after giving a proper signal or road marking or signage.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in the lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight through the junction. Lane
                        changes are prohibited by the solid lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5792, out 1077, 6.58 s
```
