# Reasoning of lane run 20261117_030938_laneC_CN_2

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 642, 19.78 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead on a clear stretch of
                        road. (lanes 2, mine 2, full)
Step 2  Left            A broken yellow line separates my lane from the lane to the left.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and greenery
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the right boundary being
                        an edge line and the left boundary being a center line (indicating my lane is the
                        rightmost of the two lanes in my direction, but the left boundary is a center line
                        separating opposite traffic). Wait, if the left boundary is a center line, my lane is
                        the leftmost of my direction. Let me re-evaluate: the yellow line is a center line,
                        meaning traffic to the left is opposite. Thus, there is only 1 lane in my direction.
                        Correcting lane_count to 1 and ego_lane_index to 1. | roles: Yellow dashed for center
                        line and white solid for edge line are consistent with their roles. | markings: No
                        markings in lane, consistent. | unseen: No attributes reported without visual
                        evidence. | result: corrected lane_count to 1 and ego_lane_index to 1
Step 5  Rule            left_boundary: A broken yellow center line permits crossing for passing with care.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway
                        and discourages crossing. [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The left boundary is a broken yellow center line, which permits
                        crossing for passing [US-3B.01-04].
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line, which
                        discourages/prohibits crossing [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a single-lane road. You may go straight or change left to pass if safe, but
                        do not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 761, 16.84 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index of 2 agree with having lane lines on
                        both the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 645, 17.77 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an elevated highway structure on the right;
                        the road continues straight ahead. (lanes 3, mine 1, full)
Step 2  Left            A solid white line is visible on the left, with a fence and parked cars beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 agree with the left boundary being
                        an edge_line and the right boundary being a lane_line. | roles: The white solid left
                        boundary fits the role of an edge_line, and the white broken right boundary fits the
                        role of a lane_line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left edge of the roadway, and
                        crossing it is generally prohibited. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        with care is permitted. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): The left boundary is a solid white edge line, which prohibits
                        crossing [US-3B.09-01-02].
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, which permits
                        crossing [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the left edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 680, 15.35 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an elevated highway structure on the right
                        and a construction fence on the left; the road continues straight ahead. (lanes 3,
                        mine 1, full)
Step 2  Left            A solid white line separates the lane from a shoulder or construction area on the
                        left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 are consistent with a left edge
                        line and a right lane line. | roles: The solid white left boundary fits the role of an
                        edge line, and the broken white right boundary fits the role of a lane line. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the edge of the roadway; crossing it is
                        discouraged or prohibited depending on the application. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): The left boundary is a solid white edge line, which prohibits or
                        discourages crossing [US-3B.09-01-02].
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, which is permissive
                        [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right. Do not cross the solid white line on
                        the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 661, 16.71 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with buildings and shops on the right; the road
                        continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates the roadway from a landscaped median on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        an edge_line and the right boundary being a lane_line. | roles: The solid white edge
                        line and dashed white lane line fit their respective roles. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white edge line, and
                        [US-3A.04-01] states a solid line discourages or prohibits crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, and [US-3A.04-01]
                        states a broken line indicates a permissive condition.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid white line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 656, 18.82 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead towards a distant
                        overpass. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 643, 15.47 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an overpass above. The road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White broken lines are consistent with lane lines separating traffic
                        in the same direction. | markings: No markings are present in the lane, which is
                        consistent with a general through lane. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 642, 17.83 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead on a bridge or
                        overpass with a city skyline in the distance. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 657, 17.64 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index of 2 agree with having lane lines on
                        both sides. | roles: The white dashed lines fit the role of lane lines separating
                        traffic in the same direction. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 639, 16.11 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead towards a distant
                        intersection. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and trees beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: The white broken line fits the role of a lane
                        line, and the white solid line fits the role of an edge line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02] and the presence of a curb.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no lane-use arrows or waiting areas.
Step 6  turn_right      not_applicable: Not applicable as there are no lane-use arrows or waiting areas.
Step 6  u_turn          not_applicable: Not applicable as there are no lane-use arrows or waiting areas.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 674, 19.4 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection or a bridge
                        overpass. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates the lane from a green-painted shoulder or buffer area on
                        the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego position (1) agree with the left boundary being
                        an edge line and the right boundary being a lane line. | roles: The white solid left
                        boundary fits the role of an edge line, and the white broken right boundary fits the
                        role of a lane line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the edge of the roadway; crossing it is
                        discouraged or prohibited depending on the specific application. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white edge line, which
                        discourages or prohibits crossing [US-3A.04-01].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white lane line,
                        which indicates a permissive condition for crossing [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the solid white
                        line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 665, 16.79 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a pedestrian overpass ahead. (lanes 2, mine
                        1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the road from a median or
                        opposite traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        a center line and the right boundary being a lane line. | roles: The yellow solid line
                        fits the role of a center line, and the white broken line fits the role of a lane
                        line. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions. [[US-3B.01-01]]
Step 5  Rule            left_boundary: A solid line prohibits crossing. [[US-3A.04-01]]
Step 5  Rule            right_boundary: The white lane line separates traffic flows in the same direction.
                        [[US-3B.06-01]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow center line,
                        which prohibits crossing according to [US-3A.04-01].
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white lane line,
                        which permits crossing according to [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may continue straight or change to
                        the right lane, but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 720, 20.18 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, approaching an intersection with a turn-off or
                        merge area to the left. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a sidewalk and parked
                        scooters beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the right boundary being
                        an edge line and the left boundary being a lane line. | roles: The white broken line
                        on the left fits the role of a lane line, and the white solid line on the right fits
                        the role of an edge line. | markings: There are no markings in my lane to contradict.
                        | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or prohibited-movement marking in
                        the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or prohibited-movement marking in
                        the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow or prohibited-movement marking in
                        the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the sidewalk area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 704, 17.01 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead towards a clear
                        stretch of road under an overpass. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label not_determined): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 654, 16.89 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. The road continues
                        forward with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the rightmost lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white color and dashed/solid patterns fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white lane line indicates that crossing is discouraged.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a solid white line, which
                        discourages crossing according to [US-3B.06-05-06], but does not strictly prohibit it
                        unless it is a double solid line.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left. Changing to the right is
                        discouraged by the solid line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 655, 19.54 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a signalized intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the rightmost lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 are consistent with having a lane
                        line on both the left and right. | roles: The white color and dashed/solid patterns
                        fit the role of lane lines separating traffic in the same direction. | markings: The
                        straight-ahead arrow is consistent with a through lane. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white lane line indicates that crossing is discouraged.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the permissible movement for
                        this lane is to go straight. [[US-3B.23-01]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white line [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): Discouraged but not prohibited by the solid white
                        line [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead arrow [US-3B.23-01].
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead arrow which only allows
                        straight movement [US-3B.23-01].
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead arrow which only allows
                        straight movement [US-3B.23-01].
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead arrow which only allows
                        straight movement [US-3B.23-01].
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight through the intersection. You may change lanes to the
                        left if needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 761, 17.54 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index of 2 agree with having lane lines on
                        both the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 648, 15.93 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection with traffic
                        signals. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the center of the
                        lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with lane lines separating traffic
                        in the same direction. | markings: The straight-ahead arrow is consistent with a
                        through lane. | unseen: No attributes were reported without visual evidence. | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that going straight is a
                        permissible movement. [[US-FIG-3B-21]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): Allowed by the through lane-use arrow [US-FIG-3B-21].
Step 6  turn_left       prohibited (correct): Prohibited by the through lane-use arrow which does not show a
                        left turn [US-FIG-3B-21].
Step 6  turn_right      prohibited (correct): Prohibited by the through lane-use arrow which does not show a
                        right turn [US-FIG-3B-21].
Step 6  u_turn          prohibited (correct): Prohibited by the through lane-use arrow which does not show a
                        U-turn [US-FIG-3B-21].
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight through the intersection. You may change lanes to the
                        left or right if needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 759, 19.32 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: White dashed lines are consistent with lane lines
                        separating traffic in the same direction. | markings: The straight-ahead arrow is
                        consistent with a through lane. | unseen: No attributes were reported without being
                        visible. | result: consistent
Step 5  Rule            left_boundary: A broken white line indicates that crossing the lane line with care is
                        not discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            right_boundary: A broken white line indicates that crossing the lane line with care is
                        not discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that going straight is a
                        permissible movement. [US-FIG-3B-21]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white left boundary
                        (US-3B.06-05-06).
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white right boundary
                        (US-3B.06-05-06).
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead arrow (US-FIG-3B-21).
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead arrow which does not show a
                        left turn (US-FIG-3B-21).
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead arrow which does not show a
                        right turn (US-FIG-3B-21).
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead arrow which does not show a
                        U-turn (US-FIG-3B-21).
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may go straight or change lanes. If you need to turn
                        left or right, please change to the corresponding outer lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 932, 20.07 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): No marking governs this action, and the lane does not end, so it is
                        allowed by default.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 647, 46.42 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 2, mine
                        1, full)
Step 2  Left            A solid white line separates the lane from a white fence and a non-motorized lane on
                        the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left_u_turn (full): A white arrow pointing both straight and left is painted in
                        the lane.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 are consistent with a left edge
                        line and a right lane line. | roles: The solid white left boundary fits the role of an
                        edge line, and the broken white right boundary fits the role of a lane line. |
                        markings: The turn-and-through arrow is consistent with a general-purpose lane. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left edge of the roadway, and
                        crossing it is discouraged or prohibited. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition for crossing
                        into the adjacent lane. [[US-3A.04-01]]
Step 5  Rule            arrow:left_u_turn: The arrow allows both going straight and turning left. [[US-
                        FIG-3B-21]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white edge line, which
                        prohibits or discourages crossing [US-3B.09-01-02].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white lane line,
                        which permits crossing [US-3A.04-01].
Step 6  go_straight     allowed (correct): The lane-use arrow allows going straight [US-FIG-3B-21].
Step 6  turn_left       allowed (correct): The lane-use arrow allows turning left [US-FIG-3B-21].
Step 6  turn_right      prohibited (correct): No marking in my lane allows turning right; the arrow only shows
                        straight and left [US-FIG-3B-21].
Step 6  u_turn          prohibited (WRONG, label allowed): No marking in my lane allows a U-turn [US-
                        FIG-3B-21].
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight or turn left at the intersection, or
                        change lanes to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left_u_turn'], missed ['arrow:straight_left']), actions False, unsafe
                        ['change_right'], citation in_pack_not_accepted, contradictions ['go_straight allowed
                        although no arrow shows it', 'u_turn prohibited although an arrow shows it']
Tokens                  in 8628, out 797, 19.16 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with lane lines separating traffic
                        in the same direction. | markings: No markings are present in the lane. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive under [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive under [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 639, 15.89 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an underpass beneath the
                        Dashan Bridge. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in my lane
                        to contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 6  change_left     allowed: The left boundary is a broken white line, which is permissive according to
                        US-3B.06-05-06.
Step 6  change_right    allowed: The right boundary is a broken white line, which is permissive according to
                        US-3B.06-05-06.
Step 6  go_straight     allowed (correct): No marking governs this action, and the lane does not end, so it is
                        allowed by default.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label allowed): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:right']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 642, 16.02 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. The road continues
                        forward with no immediate intersection or ramp visible. (lanes 3, mine 1, full)
Step 2  Left            A solid white line is on the left, with a white metal fence and a curb beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and my position (1) agree with the left boundary being an
                        edge line and the right boundary being a lane line. | roles: The solid white edge line
                        on the left and broken white lane line on the right fit their roles. | markings: There
                        are no markings in my lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left edge of the roadway, and
                        crossing it is discouraged or prohibited by the nature of the edge and curb.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition for crossing
                        into the adjacent lane. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): Prohibited by the solid white edge line and physical curb
                        [US-3B.09-01-02].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): Allowed as there are no markings restricting forward movement.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable as there is no arrow or
                        intersection in view.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable as there is no arrow or
                        intersection in view.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable as there is no arrow or
                        intersection in view.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the left boundary due to the curb and solid line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 685, 17.37 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with lane lines separating traffic
                        in the same direction. | markings: The straight arrow is consistent with a through
                        lane. | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that going straight is a
                        permissible movement. [[US-FIG-3B-21]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line
                        [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line
                        [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): Allowed by the through lane-use arrow [US-FIG-3B-21].
Step 6  turn_left       prohibited (correct): Prohibited by the through lane-use arrow [US-FIG-3B-21] which
                        does not show a left turn.
Step 6  turn_right      prohibited (correct): Prohibited by the through lane-use arrow [US-FIG-3B-21] which
                        does not show a right turn.
Step 6  u_turn          prohibited (correct): Prohibited by the through lane-use arrow [US-FIG-3B-21] which
                        does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight through the intersection. You may change lanes to the
                        left or right if needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 751, 17.35 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a signalized intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            A white metal fence and a solid white line are on the left, separating the road from a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 are consistent with a left edge
                        line and a right lane line. | roles: The white solid left boundary fits the role of an
                        edge line, and the white broken right boundary fits the role of a lane line. |
                        markings: The straight-ahead arrow is consistent with a through lane. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left edge of the roadway; crossing
                        it is discouraged or prohibited. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition for crossing
                        into the adjacent lane. [[US-3A.04-01]]
Step 5  Rule            arrow:straight: The through lane-use arrow indicates that going straight is a
                        permitted movement. [[US-FIG-3B-21]]
Step 6  change_left     prohibited (correct): The left boundary is a solid edge line with a curb, which
                        prohibits leaving the roadway [US-3B.09-01-02].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white lane line,
                        which permits crossing with care [US-3A.04-01].
Step 6  go_straight     allowed (correct): The straight-ahead arrow in the lane permits this movement [US-
                        FIG-3B-21].
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking in the lane allows a left turn,
                        and the left boundary prohibits it.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking in the lane allows a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking in the lane allows a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight through the intersection. You may change to the right
                        lane if needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 761, 18.0 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a city road in China with an intersection ahead. My car is in a lane
                        approaching this intersection. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the white lane
                        line on the left and the white edge line on the right. | roles: The white dashed line
                        fits the role of a lane line, and the white solid line fits the role of an edge line.
                        | markings: There are no markings in my lane to check. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive for
                        crossing according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label not_determined): The right boundary is a solid white edge
                        line and a curb, which prohibits leaving the roadway according to [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the right edge line
                        into the curb area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['area:grid']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 670, 16.35 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards a distant
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is on the left, separating the road from a possible median or
                        opposite traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego position (1) agree with the boundaries: a center
                        line on the left and a lane line on the right. | roles: The yellow solid line fits the
                        role of a center line; the white dashed line fits the role of a lane line. | markings:
                        There are no markings in the lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions; crossing it is generally prohibited unless otherwise marked.
                        [[US-3B.01-01]]
Step 5  Rule            right_boundary: The broken white lane line indicates a permissive condition for
                        crossing with care. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow center line, which prohibits
                        crossing [US-3B.01-01].
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, which permits
                        crossing with care [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may go straight or change lanes to
                        the right, but do not cross the yellow line to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['symbol:other']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 658, 16.6 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a bridge overpass on the left; ahead is a
                        straight stretch of road with a bus stop area on the right. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a red-colored bus lane on the right.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with the boundaries: a lane
                        line on the left and a special lane line on the right. | roles: The white color and
                        dashed/solid patterns fit the roles of lane_line and special_lane_line respectively. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white lane line discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed: The left boundary is a broken white line, which is permissive according to
                        [US-3B.06-05-06].
Step 6  change_right    prohibited: The right boundary is a solid white line bordering a special lane, which
                        discourages or prohibits crossing according to [US-3B.06-05-06].
Step 6  go_straight     allowed (WRONG, label prohibited): No marking governs this action, and the boundaries
                        do not restrict it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label allowed): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in or ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not enter the red bus lane on
                        your right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:right']), actions False, unsafe ['go_straight'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 675, 16.32 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a concrete barrier on the left, heading
                        towards a distant intersection. (lanes 2, mine 1, full)
Step 2  Left            A concrete barrier is on the left, with a solid white line painted on the road next to
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The solid white
                        edge line and dashed white lane line fit their respective roles. | markings: There are
                        no markings in my lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left edge of the roadway, and
                        crossing it is prohibited by the nature of the concrete barrier. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition for crossing
                        into the adjacent lane. [[US-3A.04-01]]
Step 6  change_left     prohibited (WRONG, label not_determined): Prohibited by the concrete barrier and the
                        solid edge line [US-3B.09-01-02].
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line
                        [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the right. Do not attempt to move left
                        due to the concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 663, 49.5 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a signalized intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index of 2 agree with having lane lines on
                        both the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): No marking governs this action, and the lane does not end, so it is
                        allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 650, 18.39 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White broken lines are consistent with lane lines separating traffic
                        in the same direction. | markings: The straight arrow is consistent with a through
                        lane. | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the permissible movement for
                        this lane is to go straight. [[US-3B.23-01]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): The straight-ahead arrow allows this movement according to
                        [US-3B.23-01].
Step 6  turn_left       prohibited (correct): The straight-ahead arrow prohibits movements other than straight
                        according to [US-3B.23-01].
Step 6  turn_right      prohibited (correct): The straight-ahead arrow prohibits movements other than straight
                        according to [US-3B.23-01].
Step 6  u_turn          prohibited (correct): The straight-ahead arrow prohibits movements other than straight
                        according to [US-3B.23-01].
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present in view.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight through the intersection. You may change lanes to the
                        left or right if needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 771, 17.36 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with the role of
                        lane lines separating traffic in the same direction. | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported without visual
                        evidence. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive under
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        under [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 650, 18.56 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead towards a distant
                        intersection. (lanes 4, mine 3, full)
Step 2  Left            A double yellow line separates my lane from the lane to its left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (4) and ego position (3) are consistent with a center line on
                        the left and a lane line on the right, as the center line indicates the start of the
                        lanes for my direction from the left. | roles: The double yellow line fits the role of
                        a center line for a multi-lane road, and the broken white line fits the role of a lane
                        line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-06]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): Prohibited by the double solid yellow center line [US-3B.01-06].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the double yellow
                        line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 664, 16.44 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a wide roadway ahead, appearing to be a
                        straight stretch before a distant intersection or crossing. (lanes 3, mine 1, full)
Step 2  Left            A double solid yellow line separates the roadway from the opposite direction of
                        traffic.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The double yellow line on the left indicates my lane is the leftmost of my
                        direction, and the broken white line on the right indicates another lane of my
                        direction exists to the right. This agrees with lane_count 3 and ego_lane_index 1. |
                        roles: Yellow double solid for center_line and white dashed for lane_line are
                        consistent with MUTCD standards. | markings: There are no markings in my lane to
                        contradict. | unseen: No attributes were reported without visual evidence. | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited
                        for traffic traveling in either direction. [[US-3B.01-04]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): Prohibited by the double solid yellow center line [US-3B.01-04].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [US-3A.04-01].
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed as no markings restrict carrying on
                        straight along the lane.
Step 6  turn_left       not_applicable (WRONG, label allowed): Not applicable as there is no arrow or waiting
                        area governing this movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the double yellow line to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left_u_turn', 'arrow:straight']), actions False, unsafe ['go_straight'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 687, 19.73 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an overpass on the left, heading towards a
                        distant intersection. (lanes 4, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 4 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white broken lines fit the role of lane lines separating traffic
                        in the same direction. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): No marking governs this action, and the lane does not end, so it is
                        allowed by default.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 644, 15.89 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an overpass on the left, heading towards an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with lane lines separating traffic
                        in the same direction. | markings: No markings are present in the lane, which is
                        consistent with a general through lane. | unseen: No attributes were reported without
                        visual evidence. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive under [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive under [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 656, 17.92 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 4, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 4 and ego position 2 are consistent with having lane lines
                        on both sides. | roles: White broken lines are consistent with lane lines separating
                        traffic in the same direction. | markings: No markings are present in the lane, which
                        is consistent with a general through lane. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive under
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        under [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 649, 18.97 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with lane lines
                        separating traffic in the same direction. | markings: The straight arrow is consistent
                        with a through lane. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The straight arrow indicates that going straight is a permissible
                        movement. [[US-3B.23-01]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): The straight arrow in the lane allows this movement according to
                        [US-3B.23-01].
Step 6  turn_left       prohibited (correct): No marking in my lane governs this action, and the straight
                        arrow prohibits movements not shown.
Step 6  turn_right      prohibited (correct): No marking in my lane governs this action, and the straight
                        arrow prohibits movements not shown.
Step 6  u_turn          prohibited (correct): No marking in my lane governs this action, and the straight
                        arrow prohibits movements not shown.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes. Turning left or
                        right from this lane is not permitted.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 751, 18.39 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index of 2 agree with having lane lines on
                        both the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 648, 17.11 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in China, approaching an intersection. My car is in a through
                        lane. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a sidewalk and fence
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the white lane
                        line on the left and the white edge line on the right. | roles: The white broken line
                        fits the role of a lane line, and the white solid line fits the role of an edge line.
                        | markings: There are no markings in my lane to contradict. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway
                        and prohibits leaving the roadway. [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The broken white lane line allows crossing with care per
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white edge line and curb prohibit
                        leaving the roadway per [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost through lane. You may proceed straight or change to the left
                        lane, but do not cross the right edge line into the sidewalk.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 675, 16.75 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway approaching an exit ramp on the right. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white dashed lines fit the role of lane lines separating traffic
                        in the same direction. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label not_determined): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 643, 16.58 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. There are no immediate
                        intersections or ramps visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 645, 16.97 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. The road continues
                        forward with no immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line marks the right edge of the roadway, with a curb and trees beyond
                        it.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The Chinese characters '公交' (Bus) are painted in white in the lane.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: The white dashed line fits the role of a lane
                        line; the yellow solid line fits the role of an edge line (though yellow is typically
                        for left edges in the US, the prompt specifies China, but I must use the provided US
                        rules). Under US rules, a yellow edge line is for divided highways or one-way streets
                        [US-3A.03-03-04]. | markings: The 'BUS' text indicates a preferential lane. | unseen:
                        No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            right_boundary: An edge line delineates the right edge of the roadway; however, the
                        rule specifies it shall be white, while this is yellow. Following [US-3A.03-03-04],
                        yellow delineates the left-hand edge or opposite traffic, but here it is on the right.
                        Given it is a solid line, [US-3A.04-01] suggests it discourages or prohibits crossing.
                        [[US-3B.09-01-02]]
Step 5  Rule            text:bus: The word marking BUS ONLY designates a preferential lane reserved for buses.
                        [[US-3E.03-02]]
Step 6  change_left     allowed (contested, correct): Allowed by the broken white lane line [US-3A.04-01].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid yellow edge line
                        [US-3A.04-01] and the physical curb.
Step 6  go_straight     allowed (contested, label prohibited): Allowed as no marking prohibits it, but the
                        lane is reserved for buses [US-3E.03-02].
Step 6  turn_left       not_applicable: Not applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: Not applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: Not applicable as no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane. You should change to the left lane to avoid occupying
                        a reserved lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 875, 19.19 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or arterial road, traveling straight ahead on a
                        clear day. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported that were not visible. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 645, 19.34 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or arterial road, traveling straight ahead on a
                        clear day. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with the role of
                        lane lines separating traffic in the same direction. | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported without being
                        visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 647, 18.65 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway, traveling straight ahead on a clear day. (lanes 2,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a shoulder and guardrail
                        beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line, and the white solid line on the right fits the role of
                        an edge line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive for
                        crossing according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line, and
                        [US-3A.04-01] states a solid line discourages or prohibits crossing; as an edge line,
                        it marks the roadway boundary.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of a two-lane highway. You may continue straight or
                        change lanes to the left, but do not cross the right edge line into the shoulder.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 697, 19.7 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban expressway, traveling straight ahead
                        towards a distant overpass or intersection. (lanes 3, mine 2, full)
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
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white lane line indicates that crossing is discouraged.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a solid white line, which
                        discourages crossing according to [US-3B.06-05-06], but does not strictly prohibit it
                        unless it is a double solid line.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left. Changing to the right is
                        discouraged by the solid line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 653, 15.9 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or arterial road, traveling straight ahead with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 are consistent with having
                        lane lines on both the left and right. | roles: The white broken lines are consistent
                        with the role of lane lines separating traffic in the same direction. | markings:
                        There are no markings in my lane to contradict the boundaries. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 654, 16.85 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway, traveling straight ahead on a clear
                        road. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right shoulder, with a guardrail beyond
                        it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right indicate my lane is the rightmost of
                        the through lanes, but there is one more lane to the left. Wait, if I am in index 2 of
                        3, there should be a lane to my right. Looking again, the right boundary is an edge
                        line, meaning I am in the rightmost lane. Correcting lane_count to 2 and
                        ego_lane_index to 2. | roles: The white broken line fits the role of a lane line, and
                        the white solid line fits the role of an edge line. | markings: There are no markings
                        in my lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: corrected lane_count to 2 and ego_lane_index to 2
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3A.04-01].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, which prohibits
                        crossing according to [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line into the shoulder.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 759, 19.56 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading towards a slight curve to the left; the road
                        appears to be a highway or an arterial road. (lanes 2, mine 1, full)
Step 2  Left            A solid white line is visible on the left, with a guardrail and a grassy area beyond
                        it.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        an edge line and the right boundary being a lane line. | roles: The white solid left
                        boundary fits the role of an edge line, and the white broken right boundary fits the
                        role of a lane line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left-hand edge of the roadway, and
                        crossing it is generally prohibited. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition for crossing
                        into the adjacent lane. [[US-3A.04-01]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white edge line, which
                        prohibits crossing [US-3A.04-01].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white lane line,
                        which permits crossing [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the left edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 668, 16.36 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with traffic moving in the same direction; the road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 649, 16.71 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or arterial road, traveling straight ahead on a
                        clear day. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported that were not visible. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 646, 17.06 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban expressway, traveling straight ahead on a
                        road with sound barriers on both sides. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white color and dashed pattern of both boundaries fit
                        the role of lane lines separating traffic in the same direction. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 656, 16.71 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or expressway with a sound barrier wall on
                        the right. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right shoulder, with a guardrail and
                        sound wall beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having a lane line on the
                        left and an edge line on the right. | roles: The white broken line fits the role of a
                        lane line, and the white solid line fits the role of an edge line. | markings: There
                        are no markings in the lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive for
                        crossing per [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, which prohibits
                        crossing into the shoulder per [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may stay in your lane or change to the left lane. Do not cross the solid white
                        line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 672, 16.37 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a slight curve to the left; no
                        intersection is immediately visible ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a concrete barrier beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: The white broken line fits the role of a lane
                        line, and the white solid line fits the role of an edge line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive for
                        crossing according to [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line and a curb, which
                        prohibits leaving the roadway according to [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 671, 16.8 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road, possibly a bridge or highway, with a bus ahead in the
                        same lane. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: The white broken line fits the role of a lane
                        line, and the white solid line fits the role of an edge line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, and crossing it
                        is prohibited as it marks the edge of the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left. Do not cross the right edge
                        line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings None (added None,
                        missed None), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 671, 16.34 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway, traveling straight ahead on a clear
                        road. (lanes 4, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 4 and my position as index 2 are consistent with having
                        lane lines on both the left and right. | roles: The white broken lines on both sides
                        are consistent with the role of lane lines separating traffic in the same direction. |
                        markings: There are no markings in my lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        US-3B.06-05-06.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per US-3B.06-05-06.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 643, 15.86 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with a single lane of travel in my direction, leading toward a
                        distant intersection or end of the road. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates my lane from a landscaped area and a sidewalk on the
                        left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking or stopping area on the right
                        where vehicles are parked.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the boundaries
                        being edge lines on both sides. | roles: The white solid lines on both sides fit the
                        role of edge lines for a single-lane urban road. | markings: There are no markings in
                        my lane to contradict. | unseen: No attributes were reported that were not visible. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the edge of the roadway; crossing it is
                        discouraged or prohibited depending on the curb/landscape. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway;
                        crossing it is discouraged or prohibited. [[US-3B.09-01-02]]
Step 6  change_left     prohibited (WRONG, label not_determined): Prohibited by the solid white edge line and
                        physical curb/landscape [US-3B.09-01-02].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings in the lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 684, 17.64 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road in China, traveling straight ahead on a road that
                        appears to be a divided highway or a main arterial road. (lanes 1, mine 1, full)
Step 2  Left            A concrete barrier separates my lane from the opposite direction of traffic.
                        none none, curb yes, center_line, evidence full
Step 2  Right           A concrete curb separates my lane from a sidewalk or shoulder area.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The concrete barrier on the left and curb on the right indicate my lane is
                        the only lane in this direction. | roles: The physical boundaries (barrier and curb)
                        fit the roles of center_line and edge_line respectively. | markings: There are no
                        markings in the lane to contradict the boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The concrete barrier prohibits crossing into the opposite direction of
                        traffic. [null]
Step 5  Rule            right_boundary: The concrete curb prohibits leaving the roadway to the right. [null]
Step 6  change_left     prohibited (correct): prohibited by the concrete barrier (left_boundary)
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the concrete curb
                        (right_boundary)
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not attempt to cross the barrier on the
                        left or the curb on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8628, out 600, 16.41 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a pedestrian overpass on the right; the
                        road continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            A raised concrete curb with a hedge on top forms the left edge of the roadway.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and my position (1) agree with the left boundary being an
                        edge line and the right boundary being a lane line. | roles: The white dashed line
                        fits the role of a lane line separating traffic in the same direction. | markings:
                        There are no markings in my lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: The left edge of the roadway is delineated, and crossing it is
                        prohibited by the physical curb. [US-3B.09-01-02]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing into
                        the adjacent lane. [US-3A.04-01]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the physical curb
                        (left_boundary).
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the broken white line
                        (right_boundary) and rule [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 641, 15.44 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a distant intersection. The road
                        is flanked by buildings and a sidewalk on the right. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates my lane from a parking or shoulder area on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk and curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the boundaries, as both are
                        edge lines. | roles: The white solid lines fit the role of edge lines for the right
                        side and the left side of this specific roadway configuration. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: White markings delineate the right-hand edge of the roadway or the
                        left-hand edge of a reversible roadway; here it marks the left edge of the travel way.
                        [US-3A.03-03-04]
Step 5  Rule            right_boundary: A normal width solid white line delineates the right-hand edge of the
                        roadway. [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): The left boundary is a solid white edge line, which discourages
                        or prohibits crossing according to US-3A.04-01.
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line and a curb, which
                        prohibits crossing according to US-3B.09-01-02 and the presence of a physical barrier.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 674, 37.49 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, approaching an intersection with a traffic
                        signal ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: The white broken line fits the role of a lane
                        line, and the white solid line fits the role of an edge line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [US-3B.09-01-02] and the
                        presence of a curb.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the right edge line into the sidewalk.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 666, 16.39 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with buildings and trees on both sides, heading
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a sidewalk and trees
                        beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line, and the white solid line on the right fits the role of
                        an edge line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line, and
                        crossing it to leave the roadway is generally prohibited by its role as an edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to carrying on straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 689, 18.95 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. The road appears to
                        be a one-way street or a divided highway with a median to the left. (lanes 1, mine 1,
                        full)
Step 2  Left            A raised concrete median with a hedge on top forms the left side of the lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a bicycle lane or shoulder on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the boundaries: a median on
                        the left and an edge line on the right. | roles: The solid white line on the right
                        fits the role of a right edge line. | markings: There are no markings in the lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: The physical median prohibits crossing to the left. [null]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the physical median (left_boundary).
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not cross the median to the left or
                        the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8628, out 650, 18.07 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an overpass on the left; the road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 are consistent with having
                        lane lines on both the left and right. | roles: The white broken lines are consistent
                        with the role of lane lines separating traffic in the same direction. | markings:
                        There are no markings in my lane to contradict. | unseen: No attributes were reported
                        that were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 659, 18.76 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in China with a single lane for my direction, leading straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates my lane from a sidewalk or bike lane on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking or pedestrian area on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in my lane.
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the boundaries
                        being edge lines. | roles: The solid white lines on both sides fit the role of edge
                        lines for a single-lane road. | markings: The straight-ahead arrow is consistent with
                        a single through lane. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white edge line delineates the edge of the roadway; crossing it
                        is generally discouraged or prohibited. [US-3B.09-01-02]
Step 5  Rule            right_boundary: A solid white edge line delineates the edge of the roadway; crossing
                        it is generally discouraged or prohibited. [US-3B.09-01-02]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that going straight is a
                        permissible movement. [US-FIG-3B-21]
Step 6  change_left     prohibited (correct): The left boundary is a solid white edge line, which prohibits
                        crossing [US-3B.09-01-02].
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line, which
                        prohibits crossing [US-3B.09-01-02].
Step 6  go_straight     allowed (correct): The straight-ahead arrow allows this movement [US-FIG-3B-21].
Step 6  turn_left       prohibited (correct): No marking governs this action, and the straight arrow prohibits
                        other movements.
Step 6  turn_right      prohibited (correct): No marking governs this action, and the straight arrow prohibits
                        other movements.
Step 6  u_turn          prohibited (correct): No marking governs this action, and the straight arrow prohibits
                        other movements.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight ahead. Do not cross the solid white edge lines
                        on either side.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 757, 20.14 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, facing forward with a line of traffic ahead. The
                        road appears to be a single lane in this direction, bordered by a curb on the right
                        and a median on the left. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line separates the lane from a median area.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A raised concrete curb forms the right edge of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the center line on the left and
                        the curb on the right. | roles: The yellow solid line on the left fits the role of a
                        center line separating opposite traffic or a median. The curb on the right fits the
                        role of an edge line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The yellow line delineates the separation of traffic traveling in
                        opposite directions or the left-hand edge of a divided highway. [[US-3A.03-03-04]]
Step 5  Rule            left_boundary: A solid line discourages or prohibits crossing. [[US-3A.04-01]]
Step 5  Rule            right_boundary: The right edge of the roadway is delineated by the boundary, and
                        crossing it is prohibited by the physical curb. [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow center line [US-3A.04-01].
Step 6  change_right    prohibited (contested, correct): Prohibited by the physical curb [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not attempt to change lanes to the
                        left or right.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 8628, out 726, 17.27 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a line of traffic ahead, approaching what
                        appears to be a straight stretch of road. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a sidewalk and buildings
                        beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white broken line fits
                        the role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive for crossing according to [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, and
                        [US-3B.09-01-02] defines it as the edge of the roadway; crossing it would leave the
                        roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        indication that the lane ends.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 694, 17.06 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. There are no immediate
                        intersections or ramps visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A metal fence and a curb are on the left side of the road.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge (curb/fence) and the right boundary being a lane line. | roles: The
                        white dashed line fits the role of a lane line separating traffic in the same
                        direction. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The left edge of the roadway is delineated; crossing it is prohibited
                        by the physical curb and fence. [US-3B.09-01-02]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [US-3A.04-01]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the curb and fence
                        (US-3B.09-01-02)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (US-3A.04-01)
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 636, 17.04 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. There are no immediate
                        intersections or ramps visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A white metal fence and a curb are on the left, with no painted line on the road
                        surface.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge and the right boundary being a lane line. | roles: The white dashed line
                        on the right fits the role of a lane line separating traffic in the same direction. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The left edge of the roadway is delineated by the curb/fence; crossing
                        it is prohibited as it is not a travel lane. [US-3B.09-01-02]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing into
                        the adjacent lane. [US-3A.04-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the curb and fence (US-3B.09-01-02)
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (US-3A.04-01)
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 650, 16.03 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a city road with a single lane in each direction. The road continues straight
                        ahead with no immediate intersection or ramp visible. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line separates the lane from the opposite direction of traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A concrete curb forms the right edge of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the center line on the
                        left and the curb on the right. | roles: The yellow solid line fits the role of a
                        center line on a two-way road, and the curb fits the role of an edge line. | markings:
                        There are no markings in the lane to contradict. | unseen: No attributes were reported
                        that were not visible. | result: consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions. [[US-3B.01-01]]
Step 5  Rule            left_boundary: A solid line discourages or prohibits crossing. [[US-3A.04-01]]
Step 5  Rule            right_boundary: The right edge of the roadway is delineated by the curb/edge line.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the solid yellow center line
                        [US-3A.04-01].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the physical curb
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no intersection or turn arrow in view.
Step 6  turn_right      not_applicable: Not applicable as there is no intersection or turn arrow in view.
Step 6  u_turn          not_applicable: Not applicable as there is no intersection or turn arrow in view.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in the scene.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or drive onto the
                        curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 686, 16.41 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a multi-lane configuration, approaching an intersection
                        with overhead guidance signs. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a bicycle lane and the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the white lane line on
                        the left and the white edge line on the right. | roles: The white broken line fits the
                        role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line and a curb, which
                        prohibits crossing into the bicycle lane/curb area according to [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost through lane. You may change left into the adjacent lane, but
                        do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 681, 18.08 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings and trees on both sides, heading towards a
                        straight stretch of road. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the lane from traffic in the
                        opposite direction.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line is visible on the right, bordering a sidewalk area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the center line on the left
                        and edge line on the right. | roles: The yellow solid line fits the role of a center
                        line, and the white solid line fits the role of an edge line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported that were
                        not seen. | result: consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions. [[US-3B.01-01]]
Step 5  Rule            right_boundary: The solid white edge line delineates the right-hand edge of the
                        roadway. [[US-3B.09-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow center line,
                        which prohibits crossing for passing [US-3B.01-04].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line and a curb, which
                        prohibits leaving the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 645, 15.11 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in the same direction. The road
                        continues straight ahead towards a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 are consistent with having
                        lane lines on both my left and right. | roles: The white broken lines are consistent
                        with the role of lane lines separating traffic in the same direction. | markings:
                        There are no markings in my lane to contradict the boundaries. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 657, 15.89 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        buildings and pedestrians visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the road from a median or
                        opposite traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:merge_right (full): A white arrow pointing straight and slightly to the right is
                        painted in the lane.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 are consistent with a center line
                        on the left and a lane line on the right. | roles: The yellow solid line on the left
                        fits the role of a center line; the white broken line on the right fits the role of a
                        lane line. | markings: The merge_right arrow indicates the lane ends and merges into
                        the right lane, which is consistent with the lane layout. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions; crossing it is generally prohibited. [[US-3B.01-01]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing into
                        the adjacent lane. [[US-3A.04-01]]
Step 5  Rule            arrow:merge_right: The lane-reduction arrow indicates that the lane ends and traffic
                        must merge to the right. [[US-FIG-3B-21]]
Step 6  change_left     prohibited (WRONG, label not_determined): The left boundary is a solid yellow center
                        line, and [US-3B.01-01] prohibits crossing it into opposite traffic.
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line, and
                        [US-3A.04-01] permits crossing it.
Step 6  go_straight     prohibited (WRONG, label allowed): The merge_right arrow in the lane indicates the
                        lane ends, prohibiting continuing straight in this lane.
Step 6  turn_left       prohibited (correct): No marking governs this action, but the merge_right arrow
                        prohibits movements other than merging right.
Step 6  turn_right      allowed (correct): The merge_right arrow indicates a merge to the right, which allows
                        moving into the right lane.
Step 6  u_turn          prohibited (correct): No marking governs this action, and the merge_right arrow
                        prohibits it.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in the photo.
Step 7  Reflect         consistent
Advice                  Your lane is ending; you must merge right into the adjacent lane before the lane
                        terminates.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:straight_right', 'line:stop_line']), actions
                        False, unsafe [], citation in_pack_not_accepted, contradictions ['go_straight,
                        turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 8628, out 788, 17.8 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a tunnel or underpass. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white broken lines fit the role of lane lines separating traffic
                        in the same direction. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 633, 16.47 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an underpass. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White broken lines are consistent with lane lines separating traffic
                        in the same direction. | markings: No markings are present in the lane, which is
                        consistent with a through lane. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive under
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        under [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 633, 15.62 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction on the
                        left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking or shoulder area on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right would typically mean the rightmost
                        lane, but here the right boundary is an edge line and the left is a lane line, meaning
                        there is at least one lane to the left. The count of 3 lanes for the direction is
                        consistent with the visible layout. | roles: The white broken line fits the role of a
                        lane line, and the white solid line fits the role of an edge line. | markings: There
                        are no markings in the lane to contradict. | unseen: No attributes were reported that
                        were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [US-3B.09-01-02] as it
                        marks the roadway edge.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no lane-use arrows or waiting areas.
Step 6  turn_right      not_applicable: Not applicable as there are no lane-use arrows or waiting areas.
Step 6  u_turn          not_applicable: Not applicable as there are no lane-use arrows or waiting areas.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the solid white
                        line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 721, 18.34 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane road heading towards an overpass; the road appears to be a
                        local access road or a service road. (lanes 1, mine 1, full)
Step 2  Left            A low hedge and dirt shoulder are on the left, with no painted line visible.
                        none none, curb no, edge_line, evidence full
Step 2  Right           A solid red wall and a concrete curb form the right edge of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the boundaries being
                        edge lines on both sides. | roles: The absence of paint and presence of a curb/hedge
                        fit the role of edge lines for a narrow local road. | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: No specific MUTCD rule for an unpainted hedge boundary, but it defines
                        the edge of the drivable path.
Step 5  Rule            right_boundary: The curb delineates the edge of the roadway. [US-3B.18-01-04]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: no marking prohibits crossing the left
                        edge into the shoulder/hedge area, though it is not a travel lane.
Step 6  change_right    prohibited (correct): prohibited: the physical curb and wall prevent moving to the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts continuing straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not attempt to move right due to the
                        wall.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions ['change_left decided with nothing marked on that side']
Tokens                  in 8628, out 638, 20.53 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test C | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 3,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a green-painted area and a metal fence.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 3 agree with the right boundary being
                        an edge line and the left boundary being a lane line. | roles: The white color and
                        dashed pattern of the left boundary fit a lane line; the white color and solid pattern
                        of the right boundary fit an edge line. | markings: There are no markings in my lane
                        to contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway
                        and prohibits crossing it. [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, which prohibits
                        crossing according to [US-3B.09-01-02].
Step 6  go_straight     allowed (WRONG, label prohibited): No marking governs this action, and the boundaries
                        do not restrict it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label allowed): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:right', 'line:stop_line']), actions False, unsafe ['change_left',
                        'go_straight'], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 671, 41.43 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road, traveling straight ahead under a bridge overpass.
                        (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the roadway from a shoulder or
                        median.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        an edge line and the right boundary being a lane line. | roles: The yellow solid line
                        on the left fits the role of an edge line for a divided highway or one-way street; the
                        broken white line on the right fits the role of a lane line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left delineates the left-hand edge of the
                        roadway and indicates driving restrictions left of the marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow edge line,
                        which prohibits crossing [US-3B.09-03].
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, which permits
                        crossing [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 677, 16.69 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway heading straight. The road continues forward with
                        no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): A white circle containing the number 60 is painted on the
                        pavement.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: The speed limit marking is a
                        guidance feature and does not contradict the boundaries. | unseen: No attributes were
                        reported without being visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            text:speed_limit: Word and symbol markings are used for regulating, warning, or
                        guiding traffic. [[US-3B.20-01]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right as needed; please observe the indicated speed limit
                        of 60.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 747, 17.71 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a hazy atmosphere, traveling straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white dashed lines fit the role of lane lines separating traffic
                        in the same direction. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive under
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        under [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 637, 16.14 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway with a clear road ahead. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white color and dashed pattern of both boundaries fit
                        the role of lane lines separating traffic in the same direction. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 645, 17.78 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or arterial road, traveling straight ahead on a
                        clear day. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white color and dashed pattern of both boundaries fit
                        the role of lane lines separating traffic in the same direction. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to US-3B.06-05-06.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to US-3B.06-05-06.
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 646, 17.56 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or arterial road, traveling straight ahead on a
                        clear day. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right edge of the roadway, with a
                        concrete barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 3 agree with the right boundary being
                        an edge line and the left boundary being a lane line. | roles: The white color and
                        dashed/solid patterns fit the roles of lane_line and edge_line respectively. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway
                        and prohibits leaving the roadway. [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line and a curb, which
                        prohibits crossing according to [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 677, 16.56 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road passing under an overpass, with a clear road ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white broken lines fit the role of lane lines separating traffic
                        in the same direction. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive under [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which is permissive under [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 635, 16.41 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway, traveling straight ahead on a clear
                        road. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with the role of
                        lane lines separating traffic in the same direction. | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 646, 16.1 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The road is a multi-lane highway with a clear path ahead and no immediate
                        intersections or ramps visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 are consistent with having
                        lane lines on both my left and right. | roles: The white broken lines on both sides
                        are consistent with the role of lane lines separating traffic in the same direction. |
                        markings: There are no markings in my lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no lane-end
                        or merge, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 662, 17.56 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway, traveling straight ahead on a clear road. (lanes
                        2, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a shoulder beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white color and
                        dashed/solid patterns fit the roles of lane_line and edge_line respectively. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label not_determined): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which prohibits leaving the roadway according to [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can stay in your lane or change to the left lane. Do not cross the right edge line
                        onto the shoulder.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 665, 17.14 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway, traveling straight ahead on a clear road. (lanes
                        3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index of 2 agree with having lane lines on
                        both the left and right. | roles: The white broken lines on both sides fit the role of
                        lane lines separating traffic in the same direction. | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which
                        allows crossing per [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 646, 16.64 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban arterial road, traveling straight ahead
                        with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to US-3B.06-05-06.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to US-3B.06-05-06.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 644, 17.3 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 650, 16.56 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading towards a clear stretch of highway. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with lane lines separating traffic
                        in the same direction. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive under
                        [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive under [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 628, 17.31 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection with overhead
                        traffic signals. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 648, 16.65 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with traffic moving in the same direction; the road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position at index 2 are consistent with having
                        lane lines on both my left and right. | roles: The white dashed lines on both sides
                        are consistent with the role of lane lines separating traffic in the same direction. |
                        markings: There are no markings in my lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (contested, correct): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 660, 18.13 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, looking straight ahead towards a
                        distant intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 638, 17.86 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to the right.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with the boundaries: a white
                        lane line on the left and a yellow center line on the right indicate my lane is the
                        second from the left, and the rightmost of the lanes for my direction. | roles: The
                        white dashed line fits the role of a lane line, and the solid yellow line fits the
                        role of a center line. | markings: There are no markings in my lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            right_boundary: A solid yellow line as a center line prohibits crossing for the
                        traffic adjacent to it. [[US-3B.01-04]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line
                        [US-3A.04-01].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid yellow center line
                        [US-3B.01-04].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: Not applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: Not applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: Not applicable as no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may stay in your lane or change to the left lane, but do not cross the solid
                        yellow line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 656, 17.22 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in China. The road ahead continues straight with no immediate
                        intersection or ramp visible in the immediate foreground. (lanes 2, mine 1, full)
Step 2  Left            I see a yellow solid line on the left, with a two-way left-turn lane beyond it.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           I see a white broken line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the boundaries: a
                        center line on the left and a lane line on the right. | roles: The yellow solid line
                        fits the role of a center line for a two-way left-turn lane, and the white broken line
                        fits the role of a lane line. | markings: There are no markings in my lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the edge of a two-way left-turn lane
                        and prohibits crossing into it except for left-turn maneuvers. [[US-3B.05-01]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition for crossing
                        into the adjacent lane. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow line which, per
                        [US-3B.05-01], prohibits crossing except for left-turn maneuvers; however, as a
                        general lane change, it is prohibited.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white line
                        which, per [US-3B.06-05-06], allows crossing.
Step 6  go_straight     allowed (correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or waiting area governs this action in the visible stretch.
Step 6  turn_right      not_applicable: No arrow governs this action in the visible stretch.
Step 6  u_turn          not_applicable: No arrow governs this action in the visible stretch.
Step 6  enter_waiting_areaallowed: The two-way left-turn lane to the left is governed by [US-3B.05-01],
                          allowing entry for left-turn maneuvers.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. You may enter the two-way
                        left-turn lane to the left only if you intend to turn left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions ['enter_waiting_area allowed without a waiting area or two-way left-
                        turn lane']
Tokens                  in 8628, out 744, 40.36 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards a straight stretch
                        with buildings and a bus stop on the left. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (contested, correct): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 651, 16.58 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a distant intersection under
                        bright sunlight. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white broken lines fit the role of lane lines separating traffic
                        in the same direction. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 628, 15.84 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): No marking governs this action, and the lane does not end, so it is
                        allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 648, 28.04 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 are consistent with having
                        lane lines on both the left and right. | roles: The white broken lines are consistent
                        with the role of lane lines separating traffic in the same direction. | markings:
                        There are no markings in my lane to contradict the boundaries. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        allows crossing per [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 650, 17.45 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a signalized intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index of 2 agree with having lane lines on
                        both the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label not_determined): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, label not_determined): No marking governs this action, and the
                        lane does not end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 649, 35.66 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a clear path ahead, approaching a distant
                        intersection or overpass. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line is on the left, separating my lane from a two-way left-turn lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line is on the right, separating my lane from another lane of the same
                        direction.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego position (2) agree with the boundaries: a center
                        line on the left and a lane line on the right. | roles: The yellow solid line fits the
                        role of a center line for a two-way left-turn lane; the white broken line fits the
                        role of a lane line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the edge of a two-way left-turn lane
                        and prohibits crossing into it except for left-turn maneuvers. [[US-3B.05-01]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition for crossing
                        into the adjacent lane. [[US-3A.04-01]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid yellow line [US-3B.05-01]
                        except for left turns.
Step 6  change_right    allowed (correct): Allowed by the broken white line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: Not applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: Not applicable as no arrow governs this action.
Step 6  u_turn          not_applicable: Not applicable as no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present in the immediate
                          vicinity.
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may change lanes to the right, but do not cross the
                        solid yellow line to the left unless performing a left-turn maneuver.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 689, 16.49 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards a distant
                        intersection. (lanes 2, mine 2, full)
Step 2  Left            A broken yellow line is visible to the left of my lane.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A solid white line is visible to the right of my lane, with a sidewalk and trees
                        beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego position (2) agree with the boundaries: a center
                        line on the left and an edge line on the right indicate my lane is the rightmost of my
                        direction. | roles: The yellow dashed line fits the role of a center line (separating
                        opposite directions), and the solid white line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken yellow center line permits crossing for passing with care.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway
                        and discourages crossing. [[US-3B.09-01-02]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken yellow line,
                        which is a permissive condition [US-3A.04-01].
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line, which
                        discourages or prohibits crossing [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but do
                        not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 667, 16.53 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a concrete barrier on the right and
                        buildings and greenery on both sides. (lanes 2, mine 2, full)
Step 2  Left            A broken yellow line separates my lane from the lane to the left.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A concrete barrier forms the right edge of the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the right boundary being
                        an edge and the left boundary being a center line (indicating a two-way road or a
                        specific lane configuration). | roles: The yellow dashed line fits the role of a
                        center line on a two-way road. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A broken yellow center line permits crossing for passing with care.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The right edge of the roadway is delineated by the boundary, and
                        crossing it into a barrier is prohibited. [[US-3B.09-01-02]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken yellow center line
                        [US-3B.01-04].
Step 6  change_right    prohibited (contested, correct): Prohibited by the concrete barrier [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: Not applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: Not applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: Not applicable as no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left with care. Do not attempt to
                        move right due to the concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 652, 18.15 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both the left and right. | roles: The white dashed lines on both sides fit the role of
                        lane lines separating traffic in the same direction. | markings: The straight-ahead
                        arrow is consistent with a through lane. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that going straight is a
                        permissible movement. [[US-FIG-3B-21]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): The straight-ahead arrow in the lane allows this movement according
                        to [US-FIG-3B-21].
Step 6  turn_left       prohibited (correct): No marking in my lane governs this action, and the arrow only
                        shows straight.
Step 6  turn_right      prohibited (correct): No marking in my lane governs this action, and the arrow only
                        shows straight.
Step 6  u_turn          prohibited (correct): No marking in my lane governs this action, and the arrow only
                        shows straight.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes. Turning left or
                        right from this lane is not permitted by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 764, 16.61 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        overhead guide signs. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the center of the
                        lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 are consistent with having lane lines
                        on both the left and right. | roles: White broken lines are consistent with lane lines
                        separating traffic in the same direction. | markings: The straight-ahead arrow is
                        consistent with a through lane. | unseen: No attributes were reported without visual
                        evidence. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that going straight is a
                        permissible movement. [[US-FIG-3B-21]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): The straight-ahead arrow in the lane allows this movement according
                        to [US-FIG-3B-21].
Step 6  turn_left       prohibited (correct): The lane-use arrow only shows straight ahead, prohibiting other
                        movements.
Step 6  turn_right      prohibited (correct): The lane-use arrow only shows straight ahead, prohibiting other
                        movements.
Step 6  u_turn          prohibited (correct): The lane-use arrow only shows straight ahead, prohibiting other
                        movements.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present in the view.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes. Do not attempt
                        to turn left or right from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 757, 17.05 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with lane lines separating traffic
                        in the same direction. | markings: No markings are present in the lane. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive under [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive under [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 624, 17.41 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in the same direction. The road
                        continues straight ahead with no immediate intersection or ramp visible. (lanes 2,
                        mine 1, full)
Step 2  Left            I see a solid yellow line on the left, beyond which is a sidewalk and a fence.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           I see a broken white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and my position (1) agree with the boundaries: a yellow
                        edge line on the left and a white lane line on the right. | roles: The yellow solid
                        line fits the role of a left edge line for a one-way street or divided highway; the
                        white broken line fits the role of a lane line. | markings: There are no markings in
                        my lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid yellow left edge line delineates the left-hand edge of the
                        roadway and indicates driving restrictions left of the marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow edge line
                        [US-3B.09-03]
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the broken white lane line
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but you must not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 687, 16.11 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a signalized intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): A white zebra-style crosswalk extends across the lane ahead.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 are consistent with having lane lines
                        on both the left and right. | roles: The white broken lines are consistent with lane
                        lines separating traffic in the same direction. | markings: The crosswalk is a
                        standard transverse marking at an intersection. | unseen: No attributes were reported
                        without visual evidence. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            line:crosswalk: A crosswalk is an informative marking for pedestrian crossing and does
                        not govern vehicle movements out of the lane. [null]
Step 6  change_left     allowed (WRONG, label not_determined): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking in my lane restricts going straight; it is
                        allowed by default.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight or change lanes. Be mindful of the
                        crosswalk and the traffic signal ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8628, out 732, 21.49 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both the left and right. | roles: The white dashed lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 636, 18.37 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection with overhead
                        signs. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and greenery
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Chinese characters are painted in the lane, which translate to 'Bus
                        Lane'.
Step 4  Cross-check     position: The lane count of 3 and my position as index 3 agree with the right boundary
                        being an edge line and the left boundary being a lane line. | roles: The white broken
                        line on the left fits the role of a lane line, and the white solid line on the right
                        fits the role of an edge line. | markings: The 'Bus Lane' text indicates this is a
                        preferential lane. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            text:bus: The word marking BUS ONLY or BUS STOP designates a bus only lane, which is a
                        preferential lane. [[US-3E.03-02]]
Step 6  change_left     allowed (contested, correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [US-3B.09-01-02] and the
                        presence of a curb.
Step 6  go_straight     allowed (contested, correct): Allowed as no marking prohibits it, although the lane is
                        reserved for buses.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a bus lane; you should change to the left lane if you are not driving a
                        bus. Do not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed ['text:other']), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 786, 19.55 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with a
                        traffic signal ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the center of the
                        lane.
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 are consistent with having lane
                        lines on both the left and right. | roles: The white dashed lines on both sides are
                        consistent with the role of lane lines separating traffic in the same direction. |
                        markings: The straight-ahead arrow is consistent with a through lane. | unseen: No
                        attributes were reported without being visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that going straight is a
                        permissible movement. [[US-FIG-3B-21]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): The straight-ahead arrow in the lane allows this movement according
                        to [US-FIG-3B-21].
Step 6  turn_left       prohibited (correct): No marking in my lane governs this action, and the straight-
                        ahead arrow prohibits movements not shown.
Step 6  turn_right      prohibited (correct): No marking in my lane governs this action, and the straight-
                        ahead arrow prohibits movements not shown.
Step 6  u_turn          prohibited (correct): No marking in my lane governs this action, and the straight-
                        ahead arrow prohibits movements not shown.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present to govern this
                          action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. Do not attempt to
                        turn left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 787, 19.14 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection. A white truck is ahead in the
                        same lane. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a narrow paved area with a curb and trees.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a paved area where scooters are parked.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries being edge lines.
                        | roles: The solid white lines on both sides fit the role of edge lines for a single-
                        lane road. | markings: The straight arrow is consistent with a through lane. | unseen:
                        No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A solid white line delineates the edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that going straight is a
                        permissible movement. [[US-FIG-3B-21]]
Step 6  change_left     prohibited (correct): The left boundary is a solid white edge line, and [US-3A.04-01]
                        states a solid line discourages or prohibits crossing.
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, and [US-3A.04-01]
                        states a solid line discourages or prohibits crossing.
Step 6  go_straight     allowed (correct): The straight arrow in the lane allows this movement per [US-
                        FIG-3B-21].
Step 6  turn_left       prohibited (correct): No marking in the lane allows a left turn, and the arrow only
                        shows straight.
Step 6  turn_right      prohibited (correct): No marking in the lane allows a right turn, and the arrow only
                        shows straight.
Step 6  u_turn          prohibited (correct): No marking in the lane allows a U-turn, and the arrow only shows
                        straight.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight through the intersection. Do not attempt
                        to change lanes or turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 758, 17.86 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a city street with buildings on both sides. The road ahead is straight with no
                        immediate intersection or ramp visible. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line separates my lane from the left side of the road.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the center line on the left
                        and edge line on the right. | roles: The yellow solid line fits the role of a center
                        line on a two-way road, and the white solid line fits the role of a right edge line. |
                        markings: There are no markings in the lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions. [[US-3B.01-01]]
Step 5  Rule            left_boundary: A solid line discourages or prohibits crossing. [[US-3A.04-01]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: A solid line discourages or prohibits crossing. [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow center line, which prohibits
                        crossing according to [US-3A.04-01].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which prohibits crossing according to [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to carrying on straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 730, 21.84 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection with a traffic
                        signal ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed and solid lines are consistent with lane lines separating
                        traffic in the same direction. | markings: No markings are present in the lane to
                        contradict boundaries. | unseen: No attributes were reported without visual evidence.
                        | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white lane line indicates that crossing is discouraged.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a solid white line, which
                        discourages crossing according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change lanes to the left. Changing to the right is
                        discouraged by the solid line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 633, 16.43 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a signalized intersection with a
                        crosswalk ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.;
                        line:crosswalk (full): A white zebra-style crosswalk extends across the lane ahead.
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both the left and right. | roles: The white dashed lines are consistent with lane
                        lines separating traffic in the same direction. | markings: The straight arrow is
                        consistent with a through lane. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: A through lane-use arrow allows the vehicle to go straight. [[US-
                        FIG-3B-21]]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians and does not govern the seven
                        vehicle actions directly, but is noted in advice. [null]
Step 6  change_left     allowed (WRONG, label not_determined): The left boundary is a broken white line, which
                        is permissive under [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which is permissive under [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): The straight-ahead arrow allows this movement per [US-FIG-3B-21].
Step 6  turn_left       prohibited (correct): The lane-use arrow only shows straight, prohibiting other
                        movements.
Step 6  turn_right      prohibited (correct): The lane-use arrow only shows straight, prohibiting other
                        movements.
Step 6  u_turn          prohibited (correct): The lane-use arrow only shows straight, prohibiting other
                        movements.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight through the intersection. Be prepared to stop for the
                        crosswalk and traffic signal.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 8628, out 814, 18.41 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings on both sides. The road continues straight ahead
                        with no immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the opposite direction of traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 (rightmost) agree with the
                        boundaries: a center line on the left and an edge line on the right. | roles: The
                        yellow solid line fits the role of a center line, and the white solid line fits the
                        role of an edge line. | markings: There are no markings in my lane to check. | unseen:
                        No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions. [[US-3B.01-01]]
Step 5  Rule            left_boundary: A solid line prohibits crossing. [[US-3A.04-01]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: A solid line prohibits crossing. [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow center line, and rule
                        [US-3A.04-01] prohibits crossing it.
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, and rule
                        [US-3A.04-01] prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 722, 17.45 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road or bridge, heading straight toward a distant
                        intersection. (lanes 1, mine 1, full)
Step 2  Left            A solid concrete barrier is on the left side of the lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid concrete barrier and railing are on the right side of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the presence of physical
                        barriers on both sides. | roles: The physical barriers act as edge lines for the
                        single lane. | markings: There are no markings in the lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The physical barrier prohibits leaving the lane to the left. [null]
Step 5  Rule            right_boundary: The physical barrier prohibits leaving the lane to the right. [null]
Step 6  change_left     prohibited (correct): The left boundary is a physical barrier which prohibits
                        crossing.
Step 6  change_right    prohibited (correct): The right boundary is a physical barrier which prohibits
                        crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict forward movement.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight; lane changes are prohibited by the
                        physical barriers on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8628, out 559, 15.23 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a clear view ahead; there are no immediate
                        intersections or ramps visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a red-colored bicycle lane on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white color and
                        dashed/solid patterns fit the roles of lane_line and edge_line respectively. |
                        markings: There are no markings in my lane to check. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a permissive
                        condition [US-3A.04-01].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, which prohibits
                        crossing into the non-roadway area (bicycle lane) [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left. Do not cross the solid white
                        line on the right into the bicycle lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 672, 17.31 s
```
