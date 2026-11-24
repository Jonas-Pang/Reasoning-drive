# Reasoning of lane run 20261117_025521_laneB_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. The road continues forward
                        with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides fit the role
                        of crossable lane lines separating traffic in the same direction. | markings: There
                        are no markings in the lane to contradict the boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white line,
                        which allows crossing per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No markings restrict going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 779, 19.34 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with a single lane in each direction, heading
                        straight. (lanes 1, mine 1, full)
Step 2  Left            A broken yellow line separates my lane from the opposite direction of travel.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and greenery
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the center line on the left and
                        edge line on the right. | roles: The yellow dashed line fits the role of a crossable
                        center line; the white solid line fits the role of a road edge line. | markings: There
                        are no markings in the lane to contradict the boundaries. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: Crossing the solid white line is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): Allowed by the broken yellow center line [CN-5.1.1].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       allowed: Allowed by the crossable center line [CN-5.1.1] at an intersection (though no
                        intersection is immediately visible).
Step 6  turn_right      not_applicable: Not applicable as no arrow governs this and the right boundary is a
                        solid edge line.
Step 6  u_turn          allowed: Allowed by the crossable center line [CN-5.1.1] when safe.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may move left to overtake or turn if safe, but do not
                        cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions ['turn_left,
                        u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 7595, out 803, 20.8 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white dashed lines fit the role of crossable lane lines. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 589, 15.72 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an elevated highway structure on the right;
                        the road continues straight ahead. (lanes 3, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the road from a fence and a
                        non-motorized area.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 are consistent with a yellow edge
                        line on the left and a white lane line on the right. | roles: The yellow solid line on
                        the left fits the role of a left-hand edge line, and the white broken line on the
                        right fits the role of a lane line. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: A broken white lane line separates traffic flows in the same direction
                        and may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [CN-4.2.2-a]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 856, 18.97 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an elevated highway structure on the right;
                        the road continues straight ahead. (lanes 3, mine 1, full)
Step 2  Left            A solid yellow line separates the road from a sidewalk area with a white fence.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego position (1) agree with the boundaries: a yellow
                        edge line on the left indicates the leftmost lane of the direction of travel, and a
                        white lane line on the right indicates another lane of the same direction. | roles:
                        The yellow solid line on the left fits the role of a left-hand edge line; the white
                        broken line on the right fits the role of a crossable lane line. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow line, and
                        [CN-4.2.2-a] states crossing a solid line is normally prohibited.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, and
                        [CN-5.2.1-2] allows crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight, and the
                        boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 867, 18.46 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with commercial buildings on the right; the road
                        continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line separates the road from a landscaped median on the left.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The yellow solid
                        line on the left fits the role of a left-hand edge line, and the white broken line on
                        the right fits the role of a lane line. | markings: There are no markings in my lane
                        to contradict. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            left_boundary: Crossing the solid line is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the solid yellow edge line
                        [CN-4.2.2-a].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the right lane. Do not
                        cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 841, 16.84 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a distant overpass or
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides are
                        consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in my lane to contradict the boundaries.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (contested, label prohibited): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 763, 20.79 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an overpass above. The road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        left and right. | roles: The white dashed lines fit the role of crossable lane lines.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 602, 15.45 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a distant city skyline; the road
                        appears to be a bridge or overpass. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides are
                        consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in my lane to contradict the boundaries.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it and the
                        boundaries do not govern it.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 790, 18.42 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines are consistent with the
                        role of crossable lane lines separating traffic in the same direction. | markings:
                        There are no markings in my lane to contradict the boundaries. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (contested, label prohibited): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 750, 18.97 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with a clear path ahead, currently occupied by other
                        vehicles. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and trees beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line, and the white solid line on the right fits the role of
                        an edge line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the boundary of the motor vehicle
                        lane. [[CN-5.4.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 7595, out 650, 19.03 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection or bridge
                        underpass. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line marks the left edge of the roadway, with a concrete barrier beyond
                        it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and my position (1) agree with the boundaries: a yellow
                        edge line on the left and a white lane line on the right. | roles: The yellow solid
                        line fits the role of a left edge line; the white broken line fits the role of a
                        crossable lane line. | markings: There are no markings in my lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the direction of
                        travel. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid yellow edge line
                        (CN-4.2.2-a).
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left boundary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7595, out 835, 18.33 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead under a pedestrian
                        overpass. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the road from opposing traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line is visible on the right, separating my lane from another lane in
                        the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundaries: a
                        center line on the left and a lane line on the right. | roles: The yellow solid line
                        fits the role of a no-crossing center line; the white broken line fits the role of a
                        crossable lane line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow center line,
                        which prohibits crossing according to [CN-6.1.4].
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white lane line,
                        which allows crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the right lane, but do not cross the solid
                        yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 640, 16.69 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 2, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with parked scooters and a
                        sidewalk beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: The white broken line fits the role of a lane
                        line, and the white solid line fits the role of a right edge line. | markings: There
                        are no markings in the lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line marks the right edge of the roadway; crossing it
                        is normally prohibited per [CN-4.2.2-a]. [[CN-5.4.3]]
Step 6  change_left     allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but do
                        not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 650, 18.56 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead under an overpass.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index of 2 agree with having lane lines on
                        both the left and right. | roles: The white broken lines on both sides fit the role of
                        crossable lane lines. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label not_determined): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 7595, out 612, 16.35 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a clear stretch of road with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed patterns for both boundaries fit the
                        role of crossable lane lines. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported without being visible. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 7595, out 613, 16.2 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a traffic
                        signal ahead. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and greenery
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 3 agree with the right boundary being
                        an edge line and the left boundary being a lane line. | roles: The white dashed line
                        on the left fits the role of a lane line, and the white solid line on the right fits
                        the role of an edge line. | markings: The straight-ahead arrow is consistent with the
                        lane's position and boundaries. | unseen: No attributes were reported without being
                        visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the right edge of the roadway;
                        crossing it is normally prohibited by [CN-4.2.2-a]. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the lane is for traveling
                        straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but do
                        not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 7595, out 790, 20.97 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines separating traffic in the same direction. | markings: There are no markings in
                        the lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 739, 17.91 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides are
                        consistent with the role of crossable lane lines. | markings: The straight-ahead arrow
                        is consistent with a through lane bounded by lane lines. | unseen: No attributes were
                        reported without being visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may travel straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. If you need to
                        turn left or right at the intersection, you must change to the corresponding outer
                        lanes.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 904, 18.82 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides are
                        consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: The straight-ahead arrow is consistent with a through lane
                        bounded by lane lines. | unseen: No attributes were reported without being visible. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may travel straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. If you need to
                        turn left or right, you must change to the corresponding outer lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 7595, out 906, 19.96 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white color and dashed/solid patterns fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing from my side.
                        [[CN-6.2.1]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    prohibited (correct): The right boundary is a solid white line, which [CN-6.2.1]
                        prohibits crossing.
Step 6  go_straight     allowed (correct): No marking governs this action, so it is allowed by default.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but you are prohibited from changing lanes to the
                        right. You may proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 7595, out 595, 16.75 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 2, mine
                        1, full)
Step 2  Left            A solid yellow line is on the left, separating the road from a median or opposite
                        traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight and left is painted in the
                        lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the left boundary being
                        a center_line and the right boundary being a lane_line. | roles: The yellow solid line
                        fits the role of a no-crossing center_line; the white broken line fits the role of a
                        crossable lane_line. | markings: The straight-left arrow is consistent with a lane
                        that allows both movements. | unseen: No attributes were reported without being seen.
                        | result: consistent
Step 5  Rule            left_boundary: Crossing the single solid yellow line is prohibited. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_left: The arrow allows the vehicle to go straight or turn left.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the solid yellow center_line
                        [CN-6.1.4].
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane_line [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): Allowed by the guide arrow [CN-5.13.1].
Step 6  turn_left       allowed (correct): Allowed by the guide arrow [CN-5.13.1].
Step 6  turn_right      prohibited (correct): Prohibited by the guide arrow [CN-5.13.1] which only shows
                        straight and left.
Step 6  u_turn          prohibited (WRONG, label allowed): Prohibited by the guide arrow [CN-5.13.1] which
                        does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or turn left at the
                        intersection, or change lanes to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 7595, out 744, 20.98 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 1,
                        full)
Step 2  Left            A solid yellow line is visible on the left, separating the road from a non-motorized
                        lane or shoulder.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 agree with the left boundary being
                        an edge line and the right boundary being a lane line. | roles: The yellow solid line
                        on the left fits the role of a left-hand edge line, and the white broken line on the
                        right fits the role of a lane line. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow edge line, and [CN-4.2.2-a]
                        prohibits crossing solid lines normally.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white lane line, and
                        [CN-5.2.1-2] allows crossing it.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane,
                        but do not cross the yellow line on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 7595, out 815, 17.18 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an underpass beneath the Dashan
                        Bridge. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 are consistent with having
                        lane lines on both the left and right. | roles: The white dashed lines on both sides
                        correctly fit the role of crossable lane lines separating traffic in the same
                        direction. | markings: The straight-ahead arrow is consistent with the lane's position
                        and boundaries. | unseen: No attributes were reported without visual evidence. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may travel straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed: Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed: Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (WRONG, label allowed): Prohibited by the straight-ahead guide arrow
                        (CN-5.13.1), which restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes to the left or
                        right. Do not attempt to turn left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 7595, out 912, 19.92 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a distant intersection. (lanes
                        3, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, with a white fence and sidewalk beyond it.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 agree with the left boundary being
                        an edge line and the right boundary being a lane line. | roles: The yellow solid left
                        boundary fits the role of a left edge line, and the white dashed right boundary fits
                        the role of a lane line. | markings: There are no markings in the lane to contradict.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway;
                        crossing it is normally prohibited by [CN-4.2.2-a]. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow line, which prohibits
                        crossing according to [CN-4.2.2-a].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        according to [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 650, 17.1 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 2, mine
                        1, full)
Step 2  Left            A white solid line separates the lane from a non-motorized lane and a fence on the
                        left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.;
                        line:stop_line (full): A white solid stop line is painted across the lane at the
                        intersection.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        an edge line and the right boundary being a lane line. | roles: The white solid left
                        boundary fits the role of a motor/non-motor separation edge line, and the white dashed
                        right boundary fits the role of a crossable lane line. | markings: The straight arrow
                        and stop line are consistent with a through lane at an intersection. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The white edge line marks the boundary between motor vehicle lanes and
                        non-motorized lanes. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line [CN-5.4.3] and
                        [CN-4.2.2-a].
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1] which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1] which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1] which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed, but do
                        not cross the solid line to the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 7595, out 858, 18.07 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 1,
                        full)
Step 2  Left            A solid yellow line is visible on the left, separating the road from a non-motorized
                        lane or shoulder.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 are consistent with a yellow edge
                        line on the left and a white lane line on the right. | roles: The yellow solid line on
                        the left fits the role of a left edge line; the white broken line on the right fits
                        the role of a crossable lane line. | markings: The straight-ahead arrow is consistent
                        with the lane's position and boundaries. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway;
                        crossing it is normally prohibited by [CN-4.2.2-a]. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow line, which prohibits
                        crossing according to [CN-4.2.2-a].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        allows crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): The straight-ahead arrow allows this movement according to
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): The straight-ahead arrow prohibits movements other than those
                        shown according to [CN-5.13.1].
Step 6  turn_right      prohibited (correct): The straight-ahead arrow prohibits movements other than those
                        shown according to [CN-5.13.1].
Step 6  u_turn          prohibited (correct): The straight-ahead arrow prohibits movements other than those
                        shown according to [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present in view.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed, but do
                        not cross the yellow line on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_right'],
                        citation accepted, contradictions []
Tokens                  in 7595, out 805, 18.16 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with multiple lanes, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction on the
                        left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from another lane of the same direction on the
                        right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['area:grid']), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 752, 15.85 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a clear path ahead leading towards a distant
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left side of the lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the boundaries: a center
                        line on the left and a lane line on the right. | roles: The yellow solid line fits the
                        role of a no-crossing center line, and the white broken line fits the role of a
                        crossable lane line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost motor vehicle lane. You may proceed straight or change lanes
                        to the right, but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['symbol:other']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 784, 17.02 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a bridge overpass on the left; the road
                        continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a red-colored lane to the right.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having a lane line on the
                        left and a boundary on the right. | roles: The white broken line on the left fits a
                        crossable lane line; the white solid line on the right fits a boundary for a special
                        lane (bus/non-motorized). | markings: There are no markings in the lane to contradict.
                        | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits vehicles on the solid-line side from
                        crossing. [[CN-6.2.1]]
Step 6  change_left     allowed: Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited: Prohibited by the solid white special lane line [CN-6.2.1].
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed as there are no markings restricting
                        forward movement.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable as there is no arrow or
                        waiting area governing this.
Step 6  turn_right      not_applicable (WRONG, label allowed): Not applicable as there is no arrow or waiting
                        area governing this.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable as there is no arrow
                        governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane, but do not enter the red lane to
                        your right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:right']), actions False, unsafe ['go_straight'], citation accepted,
                        contradictions []
Tokens                  in 7595, out 786, 18.33 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a concrete barrier on the left, heading
                        towards an intersection. (lanes 3, mine 1, full)
Step 2  Left            A concrete barrier is on the left side of the lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 are consistent with a concrete
                        barrier on the left and a lane line on the right. | roles: The white dashed line fits
                        the role of a crossable lane line. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: The concrete barrier marks the edge of the roadway. [CN-5.4.1] "The
                        carriageway edge line marks the edge of motor vehicle lanes or non-motorized vehicle
                        lanes, or the boundary between motor vehicle lanes and non-motorized ve"
Step 5  Rule            right_boundary: The broken white line is a crossable lane line separating traffic in
                        the same direction. [CN-5.2.1-2] "The crossable lane line separates traffic flows in
                        the same direction and is placed between lanes of the same direction. It is a broken
                        white line."
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the concrete barrier
                        (edge_line) which prevents leaving the roadway
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 7595, out 605, 17.77 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with traffic signals
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with the role of
                        crossable lane lines separating traffic in the same direction. | markings: There are
                        no markings in the lane to contradict the boundaries. | unseen: No attributes were
                        reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 753, 17.37 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with the role of
                        crossable lane lines. | markings: The straight-ahead arrow is consistent with a
                        through lane. | unseen: No attributes were reported without being visible. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, change to the
                        corresponding outer lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation accepted,
                        contradictions []
Tokens                  in 7595, out 882, 17.67 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead on a clear stretch of
                        road. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        left and right. | roles: The white dashed lines fit the role of crossable lane lines.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 592, 16.96 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead towards a distant
                        intersection. (lanes 4, mine 2, full)
Step 2  Left            A double solid yellow line is on the left, separating my lane from opposing traffic.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A broken white line is on the right, separating my lane from another lane of the same
                        direction.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (4) and ego_lane_index (2) imply there is one lane to the
                        left. However, the left boundary is a double solid yellow center line, which means my
                        lane is the leftmost lane of my direction. I must correct the lane count and index:
                        there are 3 lanes in my direction, and I am in lane 1. | roles: The double solid
                        yellow line fits the role of a center line; the broken white line fits the role of a
                        lane line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: corrected lane_count to 3 and
                        ego_lane_index to 1
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): The left boundary is a double solid yellow line, which prohibits
                        crossing according to [CN-6.1.2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may change lanes to the right, but you must not
                        cross the double yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 693, 16.64 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a distant intersection in foggy
                        conditions. (lanes 3, mine 1, full)
Step 2  Left            A double solid yellow line separates the road from opposing traffic.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 agree with the left boundary being
                        a center line and the right boundary being a lane line. | roles: The yellow double
                        solid line fits the role of a center line; the white dashed line fits the role of a
                        lane line. | markings: The straight arrow is consistent with the lane's position and
                        boundaries. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may travel straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): Prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed by the straight guide arrow [CN-5.13.1].
Step 6  turn_left       prohibited (WRONG, label allowed): Prohibited by the straight guide arrow [CN-5.13.1],
                        which restricts movement to straight only.
Step 6  turn_right      prohibited: Prohibited by the straight guide arrow [CN-5.13.1], which restricts
                        movement to straight only.
Step 6  u_turn          prohibited: Prohibited by the straight guide arrow [CN-5.13.1] and the double solid
                        yellow line [CN-6.1.2].
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn, change to the right lanes as
                        the current lane is restricted to straight-ahead travel and crossing to the left is
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left_u_turn']), actions False, unsafe ['go_straight'], citation accepted,
                        contradictions []
Tokens                  in 7595, out 926, 17.84 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an overpass on the left, heading towards an
                        intersection. (lanes 4, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 4 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white broken lines fit the role of crossable lane lines. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 586, 14.64 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an overpass on the left, heading towards an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines fit the role of crossable
                        lane lines separating traffic in the same direction. | markings: There are no markings
                        in my lane to contradict. | unseen: No attributes were reported that were not visible.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 759, 17.45 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines fit the role of crossable
                        lane lines separating traffic in the same direction. | markings: There are no markings
                        in my lane to contradict the boundaries. | unseen: No attributes were reported that
                        were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may go straight or change lanes to the left or right.
                        According to the overhead sign, this lane is for going straight.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 767, 17.56 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines on both sides fit the role of
                        crossable lane lines. | markings: The straight arrow is consistent with a through lane
                        bounded by lane lines. | unseen: No attributes were reported without being visible. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may travel straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): Allowed by the straight guide arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): Prohibited by the straight guide arrow [CN-5.13.1] which does
                        not show a left turn.
Step 6  turn_right      prohibited (correct): Prohibited by the straight guide arrow [CN-5.13.1] which does
                        not show a right turn.
Step 6  u_turn          prohibited (correct): Prohibited by the straight guide arrow [CN-5.13.1] which does
                        not show a U-turn.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. To turn left or
                        right at the intersection, you will need to change to the corresponding outer lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 7595, out 725, 16.8 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position at index 2 agree with having lane lines
                        on both sides. | roles: The white dashed lines fit the role of crossable lane lines. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 735, 16.25 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in China. The road ahead leads to an intersection. My car is in
                        a lane approaching this intersection. (lanes 1, mine 1, full)
Step 2  Left            A yellow solid line is visible on the left, separating my lane from opposing traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A white solid line is visible on the right, separating the motor vehicle lane from a
                        non-motorized lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the boundaries: a
                        center line on the left and an edge line on the right. | roles: The yellow solid line
                        fits the role of a center line, and the white solid line fits the role of an edge
                        line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white; crossing it is normally prohibited as it marks the boundary to a non-motorized
                        lane. [[CN-5.4.3]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow center line,
                        which prohibits crossing according to [CN-6.1.4].
Step 6  change_right    prohibited (WRONG, label not_determined): The right boundary is a solid white edge
                        line, which prohibits crossing into the non-motorized lane according to [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight toward the intersection. Do not cross the solid
                        lines on either side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 675, 15.16 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway approaching an exit ramp to the right. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both sides. | roles: The white dashed lines on both sides are consistent with the
                        role of lane lines separating traffic in the same direction. | markings: There are no
                        markings in my lane to contradict the boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right. If you intend to take the exit indicated by the overhead sign, you will need to
                        change to the rightmost lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 7595, out 784, 16.99 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. There are no immediate
                        intersections or ramps visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides are
                        consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in the lane to contradict the boundaries.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 771, 17.81 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead on a clear stretch of
                        road. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line marks the right edge of the roadway, with a curb and trees beyond
                        it.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The Chinese characters '公交' (bus) are painted in white in the lane.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the white lane line on
                        the left and the yellow edge line on the right. | roles: The white dashed line fits
                        the role of a crossable lane line, and the yellow solid line fits the role of a right-
                        hand edge line for this direction (though yellow is typically left, the presence of
                        the curb and the 'bus' text suggests a reserved lane configuration). | markings: The
                        '公交' text indicates this is a bus lane. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The yellow edge line marks the boundary of the roadway; crossing it is
                        normally prohibited by the nature of the curb. [[CN-5.4.3]]
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the bus lane. [[CN-6.9.1]]
Step 6  change_left     allowed (contested, correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid yellow edge line and the
                        physical curb [CN-5.4.3].
Step 6  go_straight     prohibited (contested, correct): Prohibited because the car is in a bus lane and is
                        not a bus [CN-6.9.1].
Step 6  turn_left       not_applicable: Not applicable; no arrow governs this action.
Step 6  turn_right      not_applicable: Not applicable; no arrow governs this action.
Step 6  u_turn          not_applicable: Not applicable; no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: Not applicable; no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane. You should change left into the general traffic lane
                        immediately.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions ['go_straight
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 7595, out 758, 18.12 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or arterial road, traveling straight ahead on a
                        clear day. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines on both sides fit the role of
                        crossable lane lines. | markings: There are no markings in the lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 597, 16.31 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban arterial road, traveling straight ahead on
                        a clear stretch of road. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with the role of
                        crossable lane lines separating traffic in the same direction. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 617, 17.95 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or expressway with a clear road ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: White dashed lines are consistent with the role of
                        crossable lane lines separating traffic in the same direction. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported without
                        being visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means vehicles may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means vehicles may cross it to change
                        lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or intersection markings.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersection markings.
Step 6  u_turn          not_applicable: Not applicable as there are no U-turn arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 762, 17.99 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban expressway, traveling straight ahead on a
                        road that appears to curve slightly to the right in the distance. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having a lane line on both
                        the left and right. | roles: The white color and dashed/solid patterns fit the role of
                        lane lines separating traffic in the same direction. | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported without being
                        visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on my side from crossing
                        it. [[CN-6.2.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white lane line [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but you are prohibited from changing lanes to the
                        right. Continue straight in your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 7595, out 635, 18.73 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or arterial road with a clear sky and trees
                        on both sides; the road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines are consistent with the
                        role of crossable lane lines separating traffic in the same direction. | markings:
                        There are no markings in the lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 774, 18.23 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or expressway with a clear road ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right would imply I am in the rightmost lane
                        (index 3), but looking at the photo, there is another lane to my left and another to
                        the far left. Wait, looking closer at the bottom, there are three lanes of travel. My
                        lane is the middle one. The right boundary is a lane line, not an edge line. Let me
                        re-examine. Actually, the line to my right is a solid white line, and there is a
                        shoulder/guardrail. This makes my lane the rightmost motor vehicle lane. The lane
                        count is 3, and I am in lane 3. Let me correct: the line to my left is a broken white
                        line, and the line to my right is a solid white edge line. This means I am in the
                        rightmost lane. Lane count is 3, ego_lane_index is 3. | roles: The broken white line
                        on the left fits the role of a lane line. The solid white line on the right fits the
                        role of an edge line. | markings: There are no markings in my lane, which is
                        consistent with a highway stretch. | unseen: No attributes were reported without being
                        seen. | result: corrected lane_count to 3 and ego_lane_index to 3
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line on the right is an edge line marking the boundary
                        of the motor vehicle lane. [CN-5.4.3] "An edge line on the right side of the direction
                        of travel shall be white, and an edge line on the left side of the direction of travel
                        shall be yellow; a motor/"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which permits
                        crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line, and
                        crossing solid lines is normally prohibited per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrows or intersection markings govern this action.
Step 6  turn_right      not_applicable: not_applicable: no arrows or intersection markings govern this action.
Step 6  u_turn          not_applicable: not_applicable: no arrows or intersection markings govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting areas are present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 1060, 19.99 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading towards a slight curve to the left; the road
                        appears to be a highway or an urban arterial road. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a guardrail and a grassy
                        slope beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white broken line on the
                        left fits the role of a lane line, and the white solid line on the right fits the role
                        of an edge line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the right edge of the roadway;
                        crossing it is normally prohibited per [CN-4.2.2-a]. [[CN-5.4.3]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 689, 19.49 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading straight. The road continues forward with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both the left and right. | roles: The white dashed lines on both sides fit the role of
                        crossable lane lines. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 619, 15.87 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway, traveling straight ahead on a clear
                        road. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with the role of
                        crossable lane lines separating traffic in the same direction. | markings: There are
                        no markings in the lane to contradict the boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 763, 17.82 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road or highway, traveling straight ahead with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 610, 17.43 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or urban expressway with a sound barrier
                        wall on the right. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road; you may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 7595, out 598, 14.91 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a slight curve to the left; no
                        intersection is immediately visible ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a concrete barrier beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with having a lane line on
                        the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line, and the white solid line on the right fits the role of
                        an edge line. | markings: There are no markings in the lane to contradict. | unseen:
                        No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line and physical barrier
                        (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings in the
                        lane.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings in the
                        lane.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings in the
                        lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move to the right due to the road edge and barrier.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 808, 20.7 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road, possibly a bridge or highway, with a blue bus ahead
                        in the same lane. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the road, with a metal guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: The white broken line fits the role of a
                        crossable lane line, and the white solid line fits the role of a right-hand edge line.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means vehicles may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line marks the right-hand edge of the motor vehicle
                        lanes. [[CN-5.4.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the right edge
                        line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings None (added None,
                        missed None), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7595, out 653, 17.32 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway, traveling straight ahead on a clear
                        road. (lanes 4, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 4 and my position at index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines are consistent with the
                        role of crossable lane lines separating traffic in the same direction. | markings:
                        There are no markings in the lane, which is consistent with a standard through lane on
                        a highway. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or intersection markings.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersection markings.
Step 6  u_turn          not_applicable: Not applicable as there are no U-turn arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right. Overhead signs indicate speed limits for each lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 783, 18.75 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with a single lane for my direction, leading towards a distant
                        intersection or road end. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating my lane from the opposite
                        direction of travel.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line is visible on the right, marking the edge of the roadway next to a
                        parking area with vehicles.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the presence of a
                        center line on the left and an edge line on the right. | roles: The yellow color of
                        the left boundary fits the role of a center line, and the white color of the right
                        boundary fits the role of an edge line. | markings: There are no markings in my lane
                        to contradict. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white; it marks the edge of the motor vehicle lane. [[CN-5.4.3]]
Step 6  change_left     prohibited (WRONG, label not_determined): The left boundary is a solid yellow center
                        line, which prohibits crossing according to [CN-6.1.4].
Step 6  change_right    prohibited (WRONG, label not_determined): The right boundary is a solid white edge
                        line; while [CN-5.4.3] defines it, [CN-4.2.2-a] states a solid line means crossing is
                        normally prohibited.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to carrying on straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid lines on either side.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 679, 16.95 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road in China, traveling straight ahead on a section that
                        appears to be a one-way road or a divided highway with a physical barrier on the left.
                        (lanes 2, mine 1, full)
Step 2  Left            A concrete physical barrier separates the road from the opposite direction of travel.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 are consistent with a physical
                        barrier on the left and a lane line on the right. | roles: The white dashed line on
                        the right fits the role of a crossable lane line. | markings: There are no markings in
                        the lane to contradict. | unseen: No attributes were reported that were not visible. |
                        result: consistent
Step 5  Rule            left_boundary: The physical barrier marks the edge of the motor vehicle lane.
                        [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle lanes or non-
                        motorized vehicle lanes, or the boundary between motor vehicle lanes and non-motorized
                        ve"
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     prohibited (correct): prohibited by the physical barrier (curb) acting as an edge
                        line.
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the left lane of your direction. You may continue straight or change to the
                        right lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 643, 16.94 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead towards a clear stretch
                        of road. (lanes 2, mine 1, full)
Step 2  Left            A yellow solid line is visible on the left, separating the road from a median area.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        a center_line and the right boundary being a lane_line. | roles: The yellow solid line
                        on the left fits the role of a center_line; the white broken line on the right fits
                        the role of a lane_line. | markings: There are no markings in the lane to contradict.
                        | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label not_determined): The left boundary is a solid yellow line,
                        which prohibits crossing according to [CN-6.1.4].
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which allows crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may continue straight or change
                        lanes to the right, but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 645, 15.69 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road heading straight. The road ahead appears to be a single lane
                        in this direction, continuing forward under a height-restriction gantry. (lanes 1,
                        mine 1, full)
Step 2  Left            A solid yellow line separates the lane from a non-motorized lane or shoulder on the
                        left.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a sidewalk and curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a yellow edge
                        line on the left and a white edge line on the right indicate a single-lane road for
                        this direction. | roles: The yellow color for the left edge line and white for the
                        right edge line fit the roles of left and right edge lines respectively. | markings:
                        There are no markings in the lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the left-hand edge of the
                        direction of travel. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The white edge line on the right marks the right-hand edge of the
                        direction of travel. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow line, and [CN-4.2.2-a]
                        prohibits crossing solid lines.
Step 6  change_right    prohibited (correct): The right boundary is a solid white line and a curb;
                        [CN-4.2.2-a] prohibits crossing solid lines.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Lane changes to either side are
                        prohibited by the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 816, 42.93 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. A pedestrian
                        overpass is visible on the right. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a sidewalk and a
                        pedestrian bridge structure.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white broken line fits
                        the role of a lane line, and the white solid line fits the role of a right edge line.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means vehicles may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line marks the right edge of the roadway. [CN-5.4.3]
                        "An edge line on the right side of the direction of travel shall be white, and an edge
                        line on the left side of the direction of travel shall be yellow; a motor/"
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line and the presence of a
                        curb (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the right edge line into the sidewalk area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 7595, out 801, 18.01 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead with no immediate
                        intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a sidewalk and trees
                        beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white dashed line fits
                        the role of a crossable lane line, and the white solid line fits the role of a right-
                        hand edge line. | markings: There are no markings in the lane to contradict. | unseen:
                        No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 7595, out 793, 18.23 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead on a clear day. (lanes
                        1, mine 1, full)
Step 2  Left            A raised concrete median with a hedge on top is to the left of the lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a non-motorized lane on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a physical median
                        on the left and an edge line on the right. | roles: The white solid line on the right
                        fits the role of a motor/non-motor separation edge line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: The physical separation (curb/median) means a road edge line is
                        generally not marked; crossing into the median is prohibited. [CN-5.4.5] "Where a non-
                        motorized lane is needed and there is no separating facility between it and the motor
                        vehicle lanes, a motor/non-motor separation line shall be prov"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The white solid line marks the boundary between motor vehicle lanes
                        and non-motorized vehicle lanes. [CN-5.4.1] "The carriageway edge line marks the edge
                        of motor vehicle lanes or non-motorized vehicle lanes, or the boundary between motor
                        vehicle lanes and non-motorized ve"
Step 6  change_left     prohibited (correct): prohibited by the physical median/curb (CN-5.4.5)
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
                        (CN-4.2.2-a)
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the right boundary into the non-
                        motorized lane or the left boundary into the median.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 689, 17.36 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an overpass on the left; the road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position at index 2 agree with having lane lines
                        on both sides. | roles: The white dashed lines on both sides fit the role of crossable
                        lane lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 754, 19.86 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with a single lane for motor vehicles in my direction, leading
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is on the left, separating my lane from opposing traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line is on the right, separating the motor vehicle lane from a non-
                        motorized lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the center line on
                        the left and the edge line on the right. | roles: The yellow color of the left
                        boundary fits the center_line role, and the white color of the right boundary fits the
                        edge_line role. | markings: The straight arrow is consistent with a single-lane road
                        leading straight. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the direction of travel for vehicles is
                        straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow center line, which prohibits
                        crossing according to [CN-6.1.4].
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line; while
                        [CN-5.4.3] defines it, [CN-4.2.2-a] states a solid line means crossing is normally
                        prohibited.
Step 6  go_straight     allowed (correct): The straight arrow in the lane allows this movement according to
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): The straight arrow in the lane prohibits movements other than
                        straight ahead according to [CN-5.13.1].
Step 6  turn_right      prohibited (correct): The straight arrow in the lane prohibits movements other than
                        straight ahead according to [CN-5.13.1].
Step 6  u_turn          prohibited (correct): The straight arrow in the lane prohibits movements other than
                        straight ahead according to [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present in view.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight ahead. Do not cross the boundaries to the left
                        or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 801, 16.96 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in China. The road ahead appears to be a straight stretch with
                        vehicles queued in front of my car. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line separates my lane from a median area with greenery.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from a non-motorized vehicle lane where bicycles
                        are present.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the boundaries: a
                        center line on the left and an edge line on the right. | roles: The yellow solid line
                        on the left fits the role of a center line; the white solid line on the right fits the
                        role of an edge line. | markings: There are no markings in my lane to contradict. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white; as a solid line, crossing is normally prohibited per [CN-4.2.2-a]. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow center line, which prohibits
                        crossing per [CN-6.1.4].
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line, which
                        prohibits crossing per [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid lines on either side.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 7595, out 668, 16.41 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead towards a distant
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line separates the road from a non-motorized lane or shoulder on the
                        left.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego position (1) agree with the boundaries: a yellow
                        edge line on the left and a white lane line on the right. | roles: The yellow solid
                        line fits the role of a left edge line; the white broken line fits the role of a
                        crossable lane line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the motor vehicle
                        roadway; crossing it is normally prohibited by [CN-4.2.2-a]. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed for lane changes. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow line, which prohibits
                        crossing according to [CN-4.2.2-a].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        allows crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost motor vehicle lane. You may continue straight or change lanes
                        to the right, but do not cross the yellow line on the left.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions False, unsafe ['change_right'], citation accepted,
                        contradictions []
Tokens                  in 7595, out 697, 16.8 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 2, mine
                        1, full)
Step 2  Left            A yellow solid line is seen on the left, separating the road from a median or opposite
                        traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        a center_line and the right boundary being a lane_line. | roles: The yellow solid line
                        fits the role of a center_line; the white dashed line fits the role of a lane_line. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label not_determined): The left boundary is a solid yellow center
                        line, which prohibits crossing according to [CN-6.1.4].
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, which allows
                        crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight or change to the right lane, but you
                        must not cross the solid yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 658, 16.9 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 2, mine
                        1, full)
Step 2  Left            A yellow solid line is visible on the left, separating the road from opposing traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        a center_line and the right boundary being a lane_line. | roles: The yellow solid line
                        fits the role of a center_line; the white dashed line fits the role of a lane_line. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow center line,
                        which prohibits crossing according to [CN-6.1.4].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white lane line,
                        which allows crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may change lanes to the right, but
                        you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7595, out 630, 16.73 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a city road with a single lane in my direction, continuing straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is on the left, separating my lane from traffic in the opposite
                        direction.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line is on the right, marking the edge of the roadway next to a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the center line on
                        the left and edge line on the right. | roles: The yellow solid line on the left fits
                        the role of a no-crossing center line; the white solid line on the right fits the role
                        of a road edge line. | markings: There are no markings in my lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white; it marks the edge of the roadway. [[CN-5.4.3]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow line, which
                        prohibits crossing according to [CN-6.1.4].
Step 6  change_right    prohibited (WRONG, label not_determined): The right boundary is a solid white edge
                        line and a curb, which prohibits leaving the roadway according to [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to carrying on straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a solid yellow line, which prohibits crossing
                        according to [CN-6.1.4].
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 7595, out 675, 17.12 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a multi-lane layout, heading towards an intersection.
                        (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a non-motorized lane on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the white lane
                        line on the left and the white edge line on the right. | roles: The white dashed line
                        fits the role of a crossable lane line, and the white solid line fits the role of a
                        road edge line. | markings: There are no markings in my lane to contradict. | unseen:
                        No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line marks the edge of the motor vehicle lane and the
                        boundary to a non-motorized lane; crossing it is normally prohibited per [CN-4.2.2-a].
                        [[CN-5.4.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost motor vehicle lane. You may go straight or change to the left
                        lane, but do not cross the solid white line into the non-motorized lane on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 678, 21.13 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a city road with a straight path ahead. My car is in a single lane of travel.
                        (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating my lane from opposing traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line is visible on the right, separating the motor vehicle lane from a
                        non-motorized lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the center line on the left and
                        edge line on the right. | roles: The yellow solid line on the left fits the role of a
                        no-crossing center line; the white solid line on the right fits the role of a
                        motor/non-motor separation edge line. | markings: There are no markings in my lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: The white line marks the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow center line,
                        which prohibits crossing per [CN-6.1.4].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, which prohibits
                        crossing per [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid lines on either side.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 679, 17.65 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with the role of
                        crossable lane lines. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 738, 18.4 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection with a tall cylindrical building
                        on the right. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is on the left, separating the lane from opposing traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line is on the right, separating the lane from a non-motorized lane or
                        sidewalk.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the center line on the left and
                        edge line on the right. | roles: The yellow solid line fits the role of a no-crossing
                        center line; the white solid line fits the role of a road edge line. | markings: The
                        straight arrow is consistent with a single through lane. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the direction of travel for this lane
                        is straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label not_determined): Prohibited by the solid yellow center line
                        [CN-6.1.4].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the solid white edge line
                        [CN-5.4.3] and the general rule for solid lines [CN-4.2.2-a].
Step 6  go_straight     allowed (correct): Allowed by the straight guide arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): Prohibited by the straight guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (WRONG, label allowed): Prohibited by the straight guide arrow [CN-5.13.1],
                        which restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight through the intersection. Lane changes to the
                        left or right are prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_right', 'line:stop_line']), actions False,
                        unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 937, 18.78 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an underpass. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white dashed lines fit the role of crossable lane lines. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 594, 14.55 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an underpass. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position at index 2 agree with having lane lines
                        on both sides. | roles: The white dashed lines fit the role of crossable lane lines. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 743, 17.32 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction on the
                        left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a non-motorized vehicle lane on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having a lane line on the
                        left and an edge line on the right, as there is one lane to the left and no motor
                        lanes to the right. | roles: The white broken line fits the role of a crossable lane
                        line, and the white solid line fits the role of a motor/non-motor separation edge
                        line. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The white solid line on the right marks the boundary between motor
                        vehicle lanes and non-motorized vehicle lanes. [CN-5.4.3] "An edge line on the right
                        side of the direction of travel shall be white, and an edge line on the left side of
                        the direction of travel shall be yellow; a motor/"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there are no guide arrows or waiting areas.
Step 6  turn_right      not_applicable: Not applicable as there are no guide arrows or waiting areas.
Step 6  u_turn          not_applicable: Not applicable as there are no guide arrows or waiting areas.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the solid white
                        line to the right into the non-motorized lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 860, 18.83 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane road heading towards an overpass; the road appears to be a
                        local access road or a side street. (lanes 1, mine 1, full)
Step 2  Left            A low hedge and greenery form the left side of the lane.
                        none none, curb no, edge_line, evidence full
Step 2  Right           A solid red wall and a concrete curb form the right side of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 are consistent with the boundaries
                        being edge lines on both sides. | roles: The absence of paint on both sides is
                        consistent with the presence of physical boundaries (hedge on left, wall/curb on
                        right). | markings: There are no markings in the lane, which is consistent with a
                        simple access road. | unseen: No attributes were reported that were not visible. |
                        result: consistent
Step 5  Rule            left_boundary: This is an edge line marking the boundary of the motor vehicle lane.
                        [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle lanes or non-
                        motorized vehicle lanes, or the boundary between motor vehicle lanes and non-motorized
                        ve"
Step 5  Rule            right_boundary: This is an edge line marking the boundary of the motor vehicle lane.
                        [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle lanes or non-
                        motorized vehicle lanes, or the boundary between motor vehicle lanes and non-motorized
                        ve"
Step 6  change_left     prohibited (correct): The left boundary is a physical hedge; no marking allows
                        crossing it.
Step 6  change_right    prohibited (correct): The right boundary is a physical curb and wall; no marking
                        allows crossing it.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not attempt to leave the lane as it
                        is bounded by a hedge on the left and a wall on the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_left decided with nothing marked on that side']
Tokens                  in 7595, out 640, 17.1 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 3,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a green fence and curb
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 3 agree with the right boundary being
                        an edge line and the left boundary being a lane line. | roles: The white dashed line
                        on the left fits the role of a lane line, and the white solid line on the right fits
                        the role of an edge line. | markings: There are no markings in my lane to contradict.
                        | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the boundary of the motor vehicle
                        lane; crossing it is normally prohibited by [CN-4.2.2-a]. [[CN-5.4.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable as there is no arrow in my
                        lane.
Step 6  turn_right      not_applicable (WRONG, label allowed): Not applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable as there is no arrow in my
                        lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but do
                        not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:right', 'line:stop_line']), actions False, unsafe ['change_left',
                        'go_straight'], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 658, 18.23 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road under a bridge, heading straight on a clear stretch of
                        highway. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the road from a shoulder or
                        opposite traffic area.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        a center_line and the right boundary being a lane_line. | roles: The yellow solid line
                        on the left fits the role of a center_line; the white dashed line on the right fits
                        the role of a lane_line. | markings: There are no markings in the lane to contradict.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the solid yellow center line
                        [CN-6.1.4].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed; do not cross the solid yellow
                        line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 788, 18.68 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway heading straight; the road continues forward with
                        no immediate intersection or ramp. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a metal guardrail beyond
                        it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A yellow number '60' is painted inside a white circle in my
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as index 3 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line, and the white solid line on the right fits the role of
                        an edge line. | markings: The speed limit marking is a standard informative marking
                        and does not contradict the boundaries. | unseen: No attributes were reported without
                        being visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line marks the right edge of the roadway. [CN-5.4.3]
                        "An edge line on the right side of the direction of travel shall be white, and an edge
                        line on the left side of the direction of travel shall be yellow; a motor/"
Step 5  Rule            text:speed_limit: The yellow number shows the maximum speed limit for this lane.
                        [CN-5.14.2] "Pavement speed limit markings show the speed limit of a lane and are
                        placed at the start of the lane and at other suitable places where the maximum speed
                        is lim"
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which permits
                        crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line, and
                        crossing it is normally prohibited per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight, and the
                        boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line. Observe the 60 km/h speed limit painted in your
                        lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 950, 18.16 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. The road continues forward
                        with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides are
                        consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in the lane to contradict the boundaries.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 769, 17.92 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or arterial road with a clear path ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines are consistent with the
                        role of crossable lane lines separating traffic in the same direction. | markings:
                        There are no markings in the lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 764, 17.64 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban arterial road, traveling straight ahead on
                        a clear day. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides are
                        consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in the lane to contradict the boundaries.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 780, 18.46 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or arterial road, heading straight ahead
                        with no immediate intersection or ramp visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a concrete barrier beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 3 agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white broken line on the
                        left fits the role of a lane line; the white solid line on the right fits the role of
                        an edge line. | markings: There are no markings in the lane to contradict. | unseen:
                        No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line (CN-4.2.2-a) and the
                        physical barrier.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no intersection or arrow governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no intersection or arrow governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable as there is no intersection or arrow governing this
                        action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not attempt to move right as it is the edge of the road.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 805, 19.36 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road passing under an overpass, with the road
                        continuing straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        left and right. | roles: The white dashed lines fit the role of crossable lane lines.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 7595, out 608, 16.7 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or expressway, with a clear road ahead and
                        no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines separating traffic in the same direction. | markings: There are no markings in
                        the lane to contradict. | unseen: No attributes were reported without being visible. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 7595, out 620, 16.53 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or expressway with a clear road ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines are consistent with the
                        role of crossable lane lines separating traffic in the same direction. | markings:
                        There are no markings in the lane to contradict. | unseen: No attributes were reported
                        that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 758, 16.45 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading straight. The road continues forward with no
                        immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, with a metal guardrail beyond it.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        a center_line and the right boundary being a lane_line. | roles: The yellow solid line
                        on the left fits the role of a center_line; the white broken line on the right fits
                        the role of a lane_line. | markings: There are no markings in the lane to contradict.
                        | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label not_determined): The left boundary is a solid yellow line,
                        which prohibits crossing according to [CN-6.1.4].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may continue straight or change to
                        the right lane, but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 656, 17.46 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway, traveling straight ahead on a clear road. (lanes
                        3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides are
                        consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in the lane, which is consistent with a
                        standard highway through-lane. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 7595, out 781, 18.1 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban expressway, traveling straight ahead on a
                        clear day. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines on both sides fit the role of
                        crossable lane lines. | markings: There are no markings in the lane to contradict the
                        boundaries. | unseen: No attributes were reported without being visible. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 7595, out 616, 16.36 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in the same direction. The road
                        continues straight ahead with no immediate intersection or ramp visible. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines on both sides fit the role of
                        crossable lane lines. | markings: There are no markings in the lane to contradict the
                        boundaries. | unseen: No attributes were reported without being visible. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present to govern this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 616, 16.57 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading towards a clear stretch of highway with no
                        immediate intersection or ramp ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides fit the role
                        of crossable lane lines separating traffic in the same direction. | markings: There
                        are no markings in my lane to contradict the boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        allows crossing per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 7595, out 764, 18.18 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with overhead
                        traffic signals. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        left and right. | roles: The white dashed lines fit the role of crossable lane lines.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white line,
                        which [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 587, 16.48 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead on a clear day. (lanes
                        3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        left and right. | roles: The white dashed lines fit the role of crossable lane lines.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, correct): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 590, 16.12 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white line,
                        which [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in or next to the lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 597, 16.38 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both sides. | roles: The white dashed lines fit the role of crossable lane lines. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right, or continue
                        straight.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 7595, out 730, 16.7 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: White dashed lines are consistent with the role of
                        crossable lane lines separating traffic in the same direction. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported without
                        visual evidence. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  change_right    allowed (contested, label prohibited): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7595, out 745, 16.02 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken yellow line separates my lane from the lane to the left.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with the boundaries: a center
                        line on the left indicates the leftmost lane of my direction, but here it is a yellow
                        line, meaning my lane is the first lane to the right of the opposing traffic flow.
                        Wait, if there are 3 lanes in my direction, and I am in the middle, I should have lane
                        lines on both sides. The yellow line on the left indicates it is the boundary to
                        opposing traffic, making my lane the leftmost lane (index 1). Let me re-evaluate: the
                        yellow line is the center line. Therefore, my lane is the leftmost lane of my
                        direction. | roles: The yellow dashed line fits the role of a crossable center line.
                        The white dashed line fits the role of a crossable lane line. | markings: There are no
                        markings in my lane to contradict. | unseen: No attributes were reported without being
                        seen. | result: corrected lane_count to 2 and ego_lane_index to 1
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, correct): The left boundary is a broken yellow center line, which
                        [CN-5.1.1] allows crossing for overtaking or turning.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white lane line,
                        which [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          allowed: The left boundary is a broken yellow center line, which [CN-5.1.1] allows
                        crossing for a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may change lanes to the right or
                        cross the center line to overtake or make a U-turn when safe.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 7595, out 799, 18.62 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a distant intersection under
                        bright sunlight. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        left and right. | roles: The white dashed lines fit the role of crossable lane lines.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 590, 16.57 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines are consistent with the
                        role of crossable lane lines separating traffic in the same direction. | markings:
                        There are no markings in my lane to contradict the boundaries. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per CN-5.2.1-2.
Step 6  go_straight     allowed (correct): No marking restricts going straight, and the boundaries do not
                        govern this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 781, 49.34 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        overhead lane-use signs. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: White dashed lines are consistent with the role of
                        crossable lane lines separating traffic in the same direction. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported without
                        visual evidence. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right. Check the overhead signs for specific lane destinations at the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 760, 16.57 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label not_determined): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, label not_determined): No marking governs this action, and the
                        lane does not end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 591, 36.72 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead towards a distant
                        intersection with overhead signs. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line is on the left, separating my lane from the leftmost lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line is on the right, separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with the boundaries: a center
                        line on the left indicates the leftmost lane is for opposite traffic or a special
                        lane, but here it is a yellow solid line, and a lane line on the right indicates
                        another lane of the same direction. | roles: The yellow solid line fits the role of a
                        no-crossing center line; the broken white line fits the role of a crossable lane line.
                        | markings: There are no markings in my lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow line, which
                        prohibits crossing according to [CN-6.1.4].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right, but you must not cross the
                        solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 664, 16.24 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. The road continues forward
                        with no immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the road from a sidewalk/bus
                        stop area.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A broken yellow line separates my lane from the lane to the right.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego position (1) are consistent with a yellow edge
                        line on the left and a yellow center line on the right, indicating this is a two-way
                        road where my lane is the leftmost of my direction. | roles: The yellow color for both
                        boundaries fits their roles as a left edge line and a center line for opposing
                        traffic. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken yellow center line allows crossing for overtaking, turning,
                        or U-turns when safe. [[CN-5.1.1]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid yellow edge line
                        [CN-4.2.2-a].
Step 6  change_right    allowed (contested, label prohibited): Allowed by the broken yellow center line
                        [CN-5.1.1].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: Not applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: Not applicable as no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of a two-way road. You may proceed straight or change
                        lanes to the right, but do not cross the solid yellow line on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 812, 18.56 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. There are no intersections or
                        ramps immediately ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken yellow line separates my lane from the lane to the left.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego position (2) agree with the boundaries: a center
                        line on the left and an edge line on the right indicate my lane is the rightmost of
                        the two lanes in my direction, but the yellow color of the left boundary indicates it
                        separates opposing traffic, meaning my lane is the only lane for my direction here. |
                        roles: The yellow dashed line fits the role of a crossable center line; the white
                        solid line fits the role of a road edge line. | markings: There are no markings in my
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: Crossing the solid white line is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken yellow center line
                        [CN-5.1.1].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          allowed: Allowed by the broken yellow center line [CN-5.1.1].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or move left across the center line if safe. Do not cross
                        the right edge line into the barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 7595, out 832, 18.72 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both the left and right. | roles: The white dashed lines on both sides fit the role of
                        crossable lane lines. | markings: The straight-ahead arrow is consistent with a
                        through lane bounded by lane lines. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may travel straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead guide arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. Do not attempt to
                        turn left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 728, 15.95 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a bridge
                        overhead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both left and right. | roles: The white dashed lines on both sides fit the role of
                        crossable lane lines. | markings: The straight-ahead arrow is consistent with a
                        through lane bounded by lane lines. | unseen: No attributes were reported without
                        being visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may travel straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. If you need to
                        turn left or right, you must change to the corresponding outer lanes.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 901, 18.58 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white dashed lines fit the role of crossable lane lines. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 7595, out 581, 15.76 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, driving straight ahead towards a
                        distant intersection. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the road from a non-motorized
                        lane or median.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        a center line and the right boundary being a lane line. | roles: The yellow solid line
                        on the left fits the role of a center line; the white broken line on the right fits
                        the role of a lane line. | markings: There are no markings in the lane to contradict.
                        | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow line, which
                        prohibits crossing according to [CN-6.1.4].
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which allows crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may continue straight or change
                        lanes to the right, but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 654, 17.19 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): A white zebra-striped crosswalk is painted across the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        left and right. | roles: The white dashed lines fit the role of crossable lane lines.
                        | markings: The crosswalk is a standard transverse marking and does not contradict the
                        boundaries. | unseen: No attributes were reported without visual evidence. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            line:crosswalk: A crosswalk is an informative marking for pedestrian crossing and does
                        not govern vehicle movements out of the lane. [null]
Step 6  change_left     allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  change_right    allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no arrows or markings restricting
                        straight movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes. Be mindful of
                        the crosswalk and pedestrians ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 7595, out 680, 17.45 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines are consistent with the
                        role of crossable lane lines separating traffic in the same direction. | markings:
                        There are no markings in my lane to contradict the boundaries. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 745, 18.05 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection with overhead
                        lane-use signs. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and greenery
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): White Chinese characters are painted on the pavement in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as index 3 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line; the white solid line on the right fits the role of an
                        edge line. | markings: The text in the lane does not restrict movement or contradict
                        the boundaries. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white solid edge line marks the right edge of the roadway;
                        crossing it is normally prohibited by [CN-4.2.2-a]. [[CN-5.4.3]]
Step 5  Rule            text:other: The text does not govern the seven primary actions.
Step 6  change_left     allowed (contested, correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings in my lane restricting
                        it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 731, 17.28 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        left and right. | roles: The white color and dashed/solid patterns fit the role of
                        lane lines separating traffic in the same direction. | markings: The straight arrow is
                        consistent with the lane boundaries. | unseen: No attributes were reported without
                        being visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on my side from crossing.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the lane is for traveling straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white lane line [CN-6.2.1].
Step 6  go_straight     allowed (correct): Allowed by the straight guide arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): Prohibited by the straight guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but do
                        not change to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 7595, out 719, 16.96 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection. A white truck is directly ahead
                        in the same lane. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line separates the lane from a median strip with trees.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates the lane from a non-motorized vehicle lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the center line on the left and
                        edge line on the right. | roles: The yellow solid line on the left fits the role of a
                        center line; the white solid line on the right fits the role of an edge line. |
                        markings: The straight arrow is consistent with a single through lane. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Crossing the solid yellow center line is prohibited. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white edge line marks the boundary between motor vehicle and non-
                        motorized lanes. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-5.4.3] and the fact
                        that it is a non-motorized lane.
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead arrow [CN-5.13.1] which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead arrow [CN-5.13.1] which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead arrow [CN-5.13.1] which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight through the intersection. Do not change lanes
                        to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 751, 17.19 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a city street with buildings on both sides; the road continues straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line separates the lane from the left side of the road.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the lane, next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a center line on
                        the left and an edge line on the right. | roles: The yellow color and solid pattern of
                        the left boundary fit the role of a no-crossing center line; the white color and solid
                        pattern of the right boundary fit the role of a road edge line. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and the
                        presence of a curb [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 790, 18.19 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection with traffic
                        signals. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both sides. | roles: The white color and dashed/solid patterns fit the role of lane
                        lines separating traffic in the same direction. | markings: There are no markings in
                        the lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on my side from crossing
                        it. [[CN-6.2.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the solid white lane line
                        [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but you are prohibited from changing to the right.
                        You can proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 7595, out 637, 16.28 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a crosswalk
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.;
                        line:crosswalk (full): A white zebra-striped crosswalk is painted across the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: White dashed lines are consistent with the role of
                        crossable lane lines separating traffic in the same direction. | markings: The
                        straight arrow is consistent with the boundaries and the road layout. | unseen: No
                        attributes were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may proceed straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            line:crosswalk: The crosswalk is an informative marking for pedestrian crossing and
                        does not govern the seven specific vehicle actions. [null]
Step 6  change_left     allowed (WRONG, label not_determined): allowed; the left boundary is a broken white
                        line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label not_determined): allowed; the right boundary is a broken white
                        line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed; the guide arrow allows straight movement (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited; the guide arrow only shows straight ahead,
                        prohibiting other movements (CN-5.13.1).
Step 6  turn_right      prohibited (correct): prohibited; the guide arrow only shows straight ahead,
                        prohibiting other movements (CN-5.13.1).
Step 6  u_turn          prohibited (correct): prohibited; the guide arrow only shows straight ahead,
                        prohibiting other movements (CN-5.13.1).
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change lanes to the left or right if needed
                        before the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 7595, out 1004, 20.23 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides, driving straight ahead. (lanes
                        2, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and my position (2) agree with the boundaries: a center
                        line on the left and an edge line on the right mean I am in the rightmost lane of a
                        two-way road (or the rightmost lane of my direction). | roles: The yellow solid line
                        on the left fits the role of a no-crossing center line; the white solid line on the
                        right fits the role of a road edge line. | markings: There are no markings in my lane
                        to contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white solid line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and the presence of a
                        curb [CN-5.4.1]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 801, 16.64 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road or bridge, with a clear path ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A concrete barrier and railing form the left edge of the road.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A concrete barrier and railing form the right edge of the road.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the presence of physical
                        barriers on both sides. | roles: The physical barriers act as the boundaries of the
                        roadway. | markings: There are no markings in the lane to contradict the boundaries. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The left boundary is a physical edge marking the edge of the motor
                        vehicle lane. [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle
                        lanes or non-motorized vehicle lanes, or the boundary between motor vehicle lanes and
                        non-motorized ve"
Step 5  Rule            right_boundary: The right boundary is a physical edge marking the edge of the motor
                        vehicle lane. [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle
                        lanes or non-motorized vehicle lanes, or the boundary between motor vehicle lanes and
                        non-motorized ve"
Step 6  change_left     prohibited (correct): prohibited by the physical barrier (curb) on the left.
Step 6  change_right    prohibited (correct): prohibited by the physical barrier (curb) on the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight; lane changes are prohibited by the
                        physical barriers.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 606, 15.51 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. The road continues
                        forward with no immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a red-painted bicycle
                        lane beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white broken line on the
                        left fits the role of a lane line; the white solid line on the right fits the role of
                        an edge line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the right edge of the direction of
                        travel; crossing it is normally prohibited by [CN-4.2.2-a]. [[CN-5.4.3]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost motor vehicle lane. You may change lanes to the left, but do
                        not cross the solid white line into the bicycle lane on the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 689, 17.06 s
```
