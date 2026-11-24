# Reasoning of lane run 20261117_040830_laneA_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a fence on the left. The road
                        continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line marks the edge of the roadway next to a sidewalk and some
                        greenery.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow edge line prohibits moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right boundary and
                        curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change to the left
                        lane if needed, but you must not move to the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 750, 5.08 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. The road ahead appears to be a
                        straight stretch with a slight curve or intersection in the distance. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line and a curb separate my lane from the sidewalk/curb on the right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A yellow arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as both boundaries are solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 735, 6.64 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch with a median or divider in the center. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the center median/divider.
                        white solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane on the right
                        (the center area).
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 695, 6.64 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure on the right. The road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The white dashed lines correctly
                        function as lane lines between lanes of the same direction. | markings: The straight
                        arrow is consistent with the lane's purpose and the dashed boundaries. | unseen: None
                        | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You are permitted to change
                        lanes to the left or right as needed, as the lane markings are dashed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 2934, out 784, 6.73 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated highway structure on the right. My car is in
                        a lane heading straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): No markings visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly function as lane lines between
                        lanes of the same direction. | markings: No markings are present to contradict the
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 719, 6.13 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and shops on both sides. The road ahead is
                        straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible on the ground in my
                        lane, possibly a lane divider or extension.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles (lane line
                        on left, edge line on right). | roles: The white dashed line on the left and solid
                        white line on the right fit the roles of a lane line and an edge line respectively. |
                        markings: No clear arrows or text are visible to contradict the boundaries. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the left lane. Do not attempt to move into
                        the lane on your right as it is bounded by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2934, out 770, 5.89 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test A | gemma4:12b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which appears to be a
                        turn lane.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:left (full): A white arrow pointing left is visible in the lane to my right.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries
                        (white line on left, yellow line on right). | roles: The white line on the left and
                        yellow line on the right are standard for lane separation in this context. | markings:
                        The straight arrow in my lane is consistent with the lane's purpose. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane on the right.
Step 5  Rule            arrow:straight: The arrow allows the car to proceed straight ahead.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. Lane changes to the left or right are
                        prohibited by the solid lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left not_applicable although an arrow shows it']
Tokens                  in 2934, out 818, 11.56 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure overhead. The road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is next to a
                        curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a lane
                        line on my left and an edge line on my right. | roles: The white dashed line on the
                        left is a standard lane line; the white solid line on the right is a standard edge
                        line. | markings: No markings are visible to contradict the boundaries. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line prohibits moving to the right onto the curb or
                        shoulder.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right edge line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead or change into the left lane if needed. Do not attempt
                        to move to the right as it is bounded by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 752, 6.35 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test A | gemma4:12b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a city skyline in the distance. The road appears to be a
                        wide boulevard with a median on the left and a sidewalk/curb on the right. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right, which appears to be a
                        parking or stopping area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. A white
                        line on the left indicates another lane of my direction, and a white line on the right
                        with a curb indicates the edge of the roadway. | roles: The white solid lines
                        correctly represent a lane divider and an edge line. | markings: The straight arrow in
                        my lane is consistent with the lane's purpose. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving into the area to the
                        right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines. Continue straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 813, 16.07 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide intersection or turn area ahead. My car is in a
                        lane that appears to be a dedicated turn lane or a lane ending at a junction. (lanes
                        3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which has a large
                        '15' speed limit marking.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): A large white '15' speed limit marking is visible in the lane
                        to my right, but my lane itself has no specific arrows or text.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white line on
                        the left and yellow line on the right. | roles: The white line on the left and yellow
                        line on the right are standard for lane separation in this context. | markings: No
                        markings are in my lane, but the '15' is clearly in the adjacent lane. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane on the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by solid white line
Step 6  change_right    prohibited (contested, correct): prohibited by solid yellow line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane where lane changes to the left or right are prohibited by solid
                        lines. You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:speed_limit'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 786, 7.13 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear intersection ahead. My car is in a lane heading
                        towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from the sidewalk and parked cars.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 715, 6.31 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway in China. The road ahead is straight with several
                        lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        shoulder or edge area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A yellow arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving to the right onto the
                        shoulder/edge.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 728, 6.19 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass ahead. My car is in a lane heading
                        straight toward a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a sidewalk/curb area form the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a lane
                        line on my left and an edge line on my right. | roles: The white solid line on the
                        left is a standard lane line; the white solid line and curb on the right are standard
                        edge lines. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose and the surrounding boundaries. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right off the
                        roadway.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended and permitted
                        movement for this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 803, 6.95 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large intersection ahead. My car is in a lane that
                        appears to be the rightmost lane of the main roadway. (lanes 3, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line marks the right edge of the roadway, next to a sidewalk and parked
                        scooters.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible at the intersection.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow edge line and curb prohibit moving to the right off
                        the roadway.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to come to a complete stop before
                        entering the intersection.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane_line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid yellow edge_line and
                        curb
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the stop_line
Step 6  turn_left       stop_first: stop_first due to the stop_line
Step 6  turn_right      stop_first: stop_first due to the stop_line
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You must come to a complete stop at the white line
                        before proceeding. Lane changes to the left or right are prohibited by the solid
                        markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left, turn_right decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 2934, out 785, 6.85 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test A | gemma4:12b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass. My car is in a lane heading
                        straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right, which is bounded by a
                        curb/barrier.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line and curb define the edge of the roadway, allowing for
                        lane changes to the right if space permits.
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the dashed left boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may continue straight or change lanes to the left or
                        right as needed. Observe the speed limits indicated on the overhead signs.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions ['change_right allowed across a curb']
Tokens                  in 2934, out 701, 5.84 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane to my right, which ends at a curb and
                        a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead in your current lane. You are permitted to change lanes
                        to the left if necessary, but you must not move to the right as it is restricted by a
                        solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 751, 6.47 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with an intersection ahead. My car is in a lane
                        heading towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from the sidewalk/shoulder on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving onto the
                        shoulder/sidewalk to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. Lane changes to the left or right are
                        prohibited by the solid lines. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 730, 6.17 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane heading towards
                        the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. Lane changes to the left or right are
                        prohibited by the solid white lines. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 719, 5.73 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. The road appears to be a divided
                        highway or a large boulevard with multiple lanes in the same direction. (lanes 4, mine
                        2, full)
Step 2  Left            A white dashed line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane to
                        my right.; arrow:straight (full): A white arrow pointing straight ahead is painted in
                        the lane to my left.; arrow:left (full): A white arrow pointing left is painted in the
                        leftmost lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the presence of lane lines on both sides. | roles: The white dashed lines correctly
                        identify as lane lines between lanes of the same direction. | markings: The straight
                        arrow in my lane is consistent with the dashed lane lines allowing for lane changes. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left or right as needed, as the boundaries are dashed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation None, contradictions
                        ['turn_left not_applicable although an arrow shows it']
Tokens                  in 2934, out 926, 6.22 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road with an intersection or junction ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly function
                        as lane lines between lanes of the same direction. | markings: The straight arrow in
                        my lane is consistent with the lane's purpose and the surrounding lane markings. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended and allowed
                        movement for this lane.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 781, 5.95 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide intersection or junction ahead. My car is in a
                        lane heading straight. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane on the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 719, 5.5 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a left-
                        turn arrow. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left_right (full): A white arrow pointing left and a white arrow pointing
                        straight ahead.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:left_right: The arrow allows for turning left or going straight ahead.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by solid left_boundary
Step 6  change_right    prohibited (correct): prohibited by solid right_boundary
Step 6  go_straight     allowed (correct): allowed by arrow:left_right
Step 6  turn_left       allowed (correct): allowed by arrow:left_right
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label allowed): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn left. Lane changes to the
                        left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left_right'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation None, contradictions ['go_straight allowed although no arrow shows it',
                        'turn_right not_applicable although an arrow shows it']
Tokens                  in 2934, out 739, 5.47 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in the middle lane of a
                        three-lane roadway. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the presence of lane
                        lines on both sides. | roles: The white solid lines correctly function as lane lines
                        between lanes of the same direction. | markings: No markings are present to contradict
                        the boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 736, 6.39 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road passing under a bridge (Dashan Bridge). The road ahead appears to be
                        a wide intersection or a large open area with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from a sidewalk/pedestrian area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A large yellow arrow pointing straight ahead is painted in the
                        center of my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving onto the sidewalk to the
                        right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited: prohibited
Step 6  change_right    prohibited: prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Proceed straight ahead as indicated by the lane arrow. Do not attempt to change lanes
                        to the left or right as both boundaries are solid.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 735, 6.83 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a white fence on the left and trees on the right. The
                        road ahead appears to be a straight stretch with an intersection or signalized area in
                        the distance. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 2934, out 700, 14.21 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The white dashed lines correctly
                        identify as lane lines between lanes of the same direction. | markings: The straight
                        arrow in my lane is consistent with the lane's purpose. | unseen: None | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows me to change lanes to the left.
Step 5  Rule            right_boundary: The dashed line allows me to change lanes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that my lane is intended for going straight ahead.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left or right as needed, as both boundaries are dashed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 2934, out 784, 6.03 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane that appears
                        to be a dedicated straight-through lane. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane on the right.
Step 5  Rule            arrow:straight: The arrow indicates that this lane is intended for straight-through
                        traffic.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to proceed straight through the intersection. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk', 'line:stop_line']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 715, 5.45 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane facing
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        bike lane or a separated path.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (full): A large yellow grid pattern is painted across the intersection area
                        ahead of my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries (lane
                        line on left, edge line on right). | roles: The white solid lines correctly identify
                        the lane-line and edge-line roles. | markings: The grid area is consistent with an
                        intersection ahead. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving into the area to the right.
Step 5  Rule            area:grid: The grid indicates a keep-clear area or intersection zone.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight through the intersection. Lane
                        changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 774, 6.31 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a wide boulevard. My car is in a lane heading straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): A white diamond symbol is painted in the center of my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries
                        (yellow center line on left, white lane line on right). | roles: The yellow solid line
                        correctly identifies a center line, and the white solid line identifies a lane
                        boundary. | markings: The diamond symbol is a neutral marking and does not contradict
                        the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            symbol:other: The diamond symbol does not govern specific movements.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 758, 6.24 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane heading
                        straight or turning left. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight ahead and slightly left.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight_left: The arrow allows going straight or turning left.
Step 6  change_left     prohibited: prohibited by solid white lane_line
Step 6  change_right    prohibited: prohibited by solid white edge_line and curb
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by arrow:straight_left
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by arrow:straight_left
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn left. Lane changes to the
                        left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_left'], missed ['arrow:right']), actions False, unsafe
                        ['go_straight', 'turn_left'], citation None, contradictions []
Tokens                  in 2934, out 742, 6.21 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a concrete barrier on the left and a white car in the
                        adjacent lane to the right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a concrete barrier on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:left_turn_waiting (full): none; area:two_way_left_turn_lane (full): none
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a left
                        edge line (barrier) and a right lane line. | roles: The white solid lines correctly
                        identify the edge and the adjacent lane boundary. | markings: No markings are present
                        in the lane, which is consistent with the straight-ahead flow. | unseen: None |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line and barrier prohibit moving to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane on the right.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane'], missed []), actions False,
                        unsafe [], citation None, contradictions []
Tokens                  in 2934, out 765, 6.89 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in one of the lanes
                        moving forward. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is next to a
                        curb.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead in your current lane. You are permitted to change lanes
                        to the left, but changing to the right is prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 735, 9.17 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles (lane
                        lines on both sides). | roles: The white solid lines correctly function as lane lines.
                        | markings: The straight arrow is consistent with the lane's purpose and the
                        surrounding lane markings. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that this lane is designated for straight-ahead
                        travel.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines. Proceed straight ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 756, 6.41 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a fence on the left. The road
                        continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Changing to the right is
                        prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 680, 6.06 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the left and a large digital sign on the
                        right. The road ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries
                        (center line on left, lane line on right). | roles: The yellow double solid line
                        correctly identifies a center line, and the white solid line identifies a lane line. |
                        markings: No markings are present to contradict the boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left.
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 719, 5.42 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide intersection or large junction ahead. My car is in
                        a lane heading straight. (lanes 3, mine 2, full)
Step 2  Left            A double yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left.
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (correct): prohibited by left_boundary (double solid yellow line)
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by right_boundary (solid white line)
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by arrow:straight
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['arrow:left_u_turn']), actions False, unsafe ['go_straight'], citation None,
                        contradictions []
Tokens                  in 2934, out 736, 7.82 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bridge structure overhead on the left. The road
                        continues straight ahead into a city area. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right, which appears to be a
                        dedicated lane or a lane near a sidewalk.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the presence of lane
                        lines on both sides. | roles: The white solid lines correctly identify the boundaries
                        as lane lines. | markings: The straight arrow is consistent with the lane's path and
                        the surrounding boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 773, 7.06 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road under an overpass. The road continues straight ahead towards a
                        city area. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        dedicated bus or special lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the presence of lane
                        lines on both sides. | roles: The white solid lines correctly identify the boundaries
                        between lanes of the same direction. | markings: No markings are present to contradict
                        the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 732, 13.27 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large intersection or complex junction ahead. My car is
                        in one of the right-hand lanes. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from the sidewalk/curb area on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (correct): allowed by the dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right_boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change to the left if needed,
                        but you are prohibited from moving to the right due to the curb and solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 750, 13.46 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with an intersection ahead. My car is in one of the
                        central lanes. (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white dashed lines on both sides. | roles: The white dashed lines correctly
                        identify as lane lines between lanes of the same direction. | markings: The straight
                        arrow in my lane is consistent with the dashed lane lines allowing for lane changes. |
                        unseen: None | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You are permitted to change lanes to
                        the left or right as needed, as indicated by the dashed lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 2934, out 786, 6.96 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane heading towards
                        the intersection. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane or a lane ending.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left if
                        necessary, but you are prohibited from changing lanes to the right due to the solid
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 744, 13.96 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road approaching a large intersection. My car is in a lane heading
                        towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane to my right, which appears to be a
                        bike lane or a separate travel lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead in your current lane. You are permitted to change lanes
                        to the left if necessary, but you must not change lanes to the right due to the solid
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 746, 6.68 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass ahead. My car is in a lane heading
                        straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): White dashed lines on the pavement indicate lane
                        divisions.
Step 4  Cross-check     position: The lane count and my position are consistent with the boundaries (lane line
                        on left, edge line on right). | roles: The white dashed line on the left and solid
                        line/barrier on the right fit the roles of a lane line and an edge line. | markings:
                        No specific arrows or text are visible in my lane to contradict the boundaries. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and barrier prohibit lane changes to the right.
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane if needed. Do not attempt to move
                        to the right as it is blocked by a solid line and barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2934, out 755, 76.41 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median on the left and a curb/barrier on the right. The
                        road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right, which is an edge
                        lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving into the area to the
                        right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary and
                        curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 697, 6.56 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the right. The road ahead
                        appears to be a straight stretch with a turn lane or special markings in the center.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to its left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line and a curb separate my lane from the sidewalk/curb area.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): A left turn arrow is painted in the lane to my left.;
                        arrow:straight (full): A straight arrow is painted in my lane.; arrow:right (full): A
                        right turn arrow is painted in the lane to my right.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. A yellow
                        line on my left indicates a lane to my left, and a yellow line/curb on my right
                        indicates the edge of the roadway. | roles: The yellow solid lines correctly identify
                        the lane boundaries and the edge of the road. | markings: The straight arrow in my
                        lane is consistent with my lane's role as a straight-through lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving onto the sidewalk/curb
                        to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, label prohibited): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. Do not attempt to change lanes to the
                        left or right as the solid yellow lines prohibit it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed ['text:bus']), actions None,
                        unsafe [], citation None, contradictions ['turn_left not_applicable although an arrow
                        shows it', 'turn_right not_applicable although an arrow shows it']
Tokens                  in 2934, out 897, 6.66 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the right and a wall on
                        the left. Ahead, there is a gantry with signs and a merging area. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line is next to a concrete barrier and a metal guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): A yellow lane line is visible to the right
                        of my lane, but no markings are inside my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. A white
                        line on the left indicates another lane of my direction, and a white line/barrier on
                        the right indicates the edge. | roles: The white solid lines and the concrete barrier
                        correctly fit the roles of lane line and edge line. | markings: No markings are
                        present in my lane to contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and barrier prohibit moving to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines and the concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 765, 7.02 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the left and a guardrail
                        on the right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            a solid white line separates my lane from the lane to its left
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid yellow line separates my lane from the lane to its right
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): no markings visible in my lane; line:yield_line
                        (insufficient): no markings visible in my lane; line:stop_yield (insufficient): no
                        markings visible in my lane; line:crosswalk (insufficient): no markings visible in my
                        lane; arrow:merge_left (insufficient): no markings visible in my lane;
                        arrow:merge_right (insufficient): no markings visible in my lane; arrow:two_way_left
                        (insufficient): no markings visible in my lane; no_turn:left (insufficient): no
                        markings visible in my lane; no_turn:right (insufficient): no markings visible in my
                        lane; text:only (insufficient): no markings visible in my lane; text:bus
                        (insufficient): no markings visible in my lane; text:hov (insufficient): no markings
                        visible in my lane; text:stop (insufficient): no markings visible in my lane;
                        text:keep_clear (insufficient): no markings visible in my lane; text:speed_limit
                        (insufficient): no markings visible in my lane; symbol:hov_diamond (insufficient): no
                        markings visible in my lane; symbol:bike (insufficient): no markings visible in my
                        lane; symbol:other (insufficient): no markings visible in my lane;
                        area:left_turn_waiting (insufficient): no markings visible in my lane;
                        area:two_way_left_turn_lane (insufficient): no markings visible in my lane; area:grid
                        (insufficient): no markings visible in my lane; area:channelizing (insufficient): no
                        markings visible in my lane
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by solid yellow right_boundary
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'no_turn:left', 'no_turn:right', 'symbol:bike',
                        'symbol:hov_diamond', 'symbol:other', 'text:bus', 'text:hov', 'text:keep_clear',
                        'text:only', 'text:speed_limit', 'text:stop'], missed []), actions False, unsafe [],
                        citation None, contradictions ['go_straight allowed without the stop that the STOP or
                        停 marking in my lane requires']
Tokens                  in 2934, out 1117, 8.82 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The sun is high and
                        bright, causing significant glare. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        guardrail.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries (lane
                        line on left, lane line on right). | roles: The white dashed line on the left and
                        solid line on the right are consistent with standard lane markings. | markings: No
                        markings are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 6  change_left     allowed (correct): The dashed left boundary allows it.
Step 6  change_right    prohibited (WRONG, label allowed): The solid right boundary prohibits it.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Changing to the right lane is
                        prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 727, 6.84 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass or bridge structure to the left.
                        The road ahead appears to be a continuous stretch of highway. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane
                        or shoulder.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. A white
                        line on the left indicates another lane of my direction, and a white line on the right
                        indicates the edge of the roadway. | roles: The white solid lines correctly fit the
                        roles of a lane line and an edge line. | markings: No markings are present in my lane.
                        | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving onto the shoulder or the area to
                        the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 740, 20.75 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with trees on both sides. The road ahead is
                        straight. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the edge of
                        the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): none
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a lane
                        line on my left and an edge line on my right. | roles: The white solid lines are
                        consistent with lane and edge boundaries in a right-hand traffic system. | markings:
                        No markings are visible in my lane. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving onto the shoulder or area to the
                        right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 751, 6.07 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a guardrail on the right. The road ahead is
                        straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a metal guardrail form the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and guardrail prohibit moving to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary and guardrail
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You can continue straight or change to the left lane. Do
                        not attempt to move to the right as it is blocked by a guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 697, 14.42 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the right and a metal
                        guardrail on the left. The road ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right, which is bounded by a
                        concrete barrier.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible on the left side of the
                        lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You can continue straight or change to the left lane.
                        Changing to the right lane is prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2934, out 701, 6.64 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or major road with a median and guardrails. The road ahead is
                        straight with multiple lanes of traffic. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        guardrail.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. You may change lanes to the left if
                        necessary, but you are prohibited from changing lanes to the right due to the solid
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 744, 6.12 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway in China with traffic moving to the right. The road continues
                        straight ahead with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right, which is the
                        rightmost lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        having a lane line on both my left and right. | roles: The white dashed lines
                        correctly identify the boundaries as lane lines between lanes of the same direction. |
                        markings: No markings were observed in my lane. | unseen: No attributes were reported
                        that were not visible. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): The left boundary is a dashed line, which allows a lane change.
Step 6  change_right    allowed (correct): The right boundary is a dashed line, which allows a lane change.
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right as needed, as the lane markings are dashed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 767, 5.37 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a sound barrier on both sides. The road ahead
                        is straight and clear. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is adjacent to a
                        sound barrier.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with a
                        lane line on my left and a lane line on my right. | roles: The white dashed line on
                        the left and white solid line on the right are consistent with standard lane markings.
                        | markings: No markings are present in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if needed, but you are
                        prohibited from changing to the right lane due to the solid line. Proceed straight
                        ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 752, 5.57 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a sound barrier on the right. The road ahead
                        is straight. (lanes 3, mine 2, full)
Step 2  Left            a white dashed line separates my lane from the lane to my left
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           a solid white line separates my lane from the shoulder/edge
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): a white arrow pointing straight ahead in my lane
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right onto the
                        shoulder.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (correct): left_boundary is dashed, which allows lane changes.
Step 6  change_right    prohibited (correct): right_boundary is solid and there is a curb, which prohibits
                        moving right.
Step 6  go_straight     allowed (contested, correct): arrow:straight indicates straight movement is allowed.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. You may change to the left lane if
                        needed, but do not move to the right as it is restricted by a solid line and curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 588, 5.85 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a construction area or barrier on the left. The road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the center
                        of my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving onto the sidewalk or
                        shoulder to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane_line
Step 6  change_right    prohibited (correct): prohibited by the solid white edge_line and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 574, 5.05 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road with a bus ahead. The road appears to be a bridge or elevated
                        section with guardrails on both sides. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a metal guardrail form the right edge of my lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and guardrail prohibit moving to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines and the guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 675, 5.96 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or bridge with overhead signs. My car is in one of the middle
                        lanes. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): left_boundary allows it
Step 6  change_right    allowed (correct): right_boundary allows it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may continue straight or change lanes to the left or
                        right as needed, as the lane markings are dashed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 674, 5.39 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a wide roadway. The road ahead appears to continue
                        straight with a slight curve or intersection in the distance. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk and parked vehicles.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the presence of lane
                        lines on both sides. | roles: The white solid lines correctly function as lane lines
                        in a right-hand traffic environment. | markings: No markings are present to contradict
                        the boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit changing into the lane to the
                        right.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a middle lane. You may proceed straight ahead, but lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 754, 6.93 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median separating opposing traffic. My car is in a lane
                        heading forward, with a sidewalk and trees to the right. (lanes 2, mine 2, full)
Step 2  Left            A concrete median/curb separates my lane from the opposing traffic.
                        none none, curb yes, center_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The median prohibits crossing into the opposing traffic lanes.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right onto the
                        sidewalk.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the median and the solid edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 674, 5.92 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass on the right. My car is in a lane
                        heading straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a raised curb separate my lane from the sidewalk and pedestrian
                        area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving onto the sidewalk.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the left.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        curb on the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 695, 21.13 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. The car is in a lane heading
                        straight. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane
                        or a lane next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit changing into the lane/area to
                        the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (correct): prohibited by the solid white right_boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 701, 46.24 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass on the right. The road ahead
                        appears to continue straight. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from the sidewalk/pedestrian area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving onto the sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. Lane changes to the left or right are
                        prohibited by the solid lines and the curb. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 722, 6.19 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median separating opposing traffic. The road continues
                        straight ahead with buildings and trees lining the sides. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right off the
                        roadway.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 683, 5.21 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear sky. Ahead, the road continues straight with a
                        wide intersection or open area visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        bike lane or a shoulder area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the presence of lane
                        lines on both sides. | roles: The white solid lines correctly function as lane lines
                        between lanes of the same direction. | markings: No markings are present to contradict
                        the boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 752, 6.34 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overpass to the left and a sidewalk with trees to the
                        right. The road ahead appears to be a straight continuation of the current path.
                        (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line prohibits moving onto the sidewalk or shoulder.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (correct): The dashed left boundary line allows it.
Step 6  change_right    prohibited (WRONG, label allowed): The solid right edge line and curb prohibit it.
Step 6  go_straight     allowed (contested, correct): The straight arrow in my lane allows it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. You may change to the left lane if
                        needed, but do not move to the right as it is bounded by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 597, 6.23 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A city street with a dedicated bicycle lane and a regular vehicle lane. My car is in
                        the vehicle lane, and a bicycle lane is to my right. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from a sidewalk/pedestrian area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from a bicycle lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in the
                        center of my lane.
Step 4  Cross-check     position: The lane count (2) and my position (1) are consistent with the left edge
                        line and the right lane line. | roles: The white solid lines correctly define the edge
                        and the lane divider. | markings: The straight arrow is consistent with the lane's
                        purpose and the solid boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid edge line prohibits moving to the left onto the sidewalk.
Step 5  Rule            right_boundary: The solid lane line prohibits changing into the bicycle lane on the
                        right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     prohibited (correct): prohibited by the solid edge line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid lane line
Step 6  go_straight     allowed (correct): allowed by the straight arrow
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Do not attempt to change lanes to the
                        left or right as the solid lines prohibit it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 795, 7.16 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings and trees on both sides. My car is in a lane
                        heading straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. A yellow
                        line on my left indicates a lane to my left, and a white line/curb on my right
                        indicates the edge of the roadway. | roles: The yellow solid line on the left and
                        white solid line on the right fit the roles of a lane line and an edge line
                        respectively. | markings: No markings are present in my lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are prohibited by the
                        solid yellow line, and moving to the right is prohibited by the edge line and curb.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 763, 6.02 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a sidewalk and parked cars on the right. The road ahead
                        appears to be a straight stretch with a clear lane for my car. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from a lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a raised curb separate my lane from a parking area/sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles (left lane
                        line, right edge line). | roles: The white solid lines and curb correctly identify the
                        lane boundaries. | markings: No markings are present to contradict the boundaries. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving into the parking area on
                        the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions ['leftmost lane,
                        but a lane line on the left']
Tokens                  in 2934, out 729, 6.37 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the right. Ahead, there is a
                        clear roadway with a blue overhead sign indicating lane directions. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line and a raised curb separate my lane from the sidewalk on the right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a lane
                        line on my left and an edge line on my right. | roles: The white lane line on the left
                        and yellow edge line on the right are standard for this region. | markings: The
                        straight arrow in my lane is consistent with the overhead sign showing a straight path
                        for the middle lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving onto the sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane which is designated for straight travel. You should
                        continue straight ahead; lane changes to the left or right are prohibited by the solid
                        markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 801, 5.95 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with a clear sky. Ahead, there is a wide intersection
                        or open area with traffic signals and a pedestrian crossing. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        dedicated lane or shoulder area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly identify the boundaries as
                        lane lines. | markings: No markings are present to contradict the boundaries. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 720, 5.84 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a central divider. The road ahead is straight with
                        buildings and trees on both sides. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from the sidewalk/parking area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A yellow line is painted in the center of my lane,
                        indicating a divider.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the lane to the
                        left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit crossing into the area to the
                        right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid boundary lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2934, out 680, 5.76 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the left and a sidewalk on the right. The
                        road continues straight ahead with a clear view of the lane ahead. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/pedestrian area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid white line on the left and a solid white line
                        on the right define the lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving onto the sidewalk on the
                        right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 694, 6.28 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a tram line in the center. My car is in a lane heading
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from a central tram/median area.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is next to a
                        sidewalk.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count and my position as the middle lane (2) are consistent with a
                        center line on the left and a lane line on the right. | roles: The yellow center line
                        and white lane line are standard for this road type. | markings: The straight arrow is
                        consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the tram/median
                        area to the left.
Step 5  Rule            right_boundary: The solid white lane line prohibits changing into the lane to the
                        right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 793, 22.4 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide intersection or junction ahead. The road is lined
                        with trees and buildings. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right, which is the
                        rightmost lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving to the right beyond the roadway
                        edge.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane_line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge_line on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. Lane changes to the left or right are
                        prohibited by the solid lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 582, 5.82 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a wide intersection ahead. My car is in a lane that
                        appears to be a dedicated turn lane or a lane with specific turn instructions. (lanes
                        3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the sidewalk/curb area on the right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_left (full): A large white arrow pointing straight and to the left.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles (lane line
                        on left, edge line on right). | roles: The white lane line and yellow edge line fit
                        the roles of a lane divider and a roadway edge. | markings: The straight-left arrow is
                        consistent with the lane's position and the surrounding markings. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow edge line prohibits moving onto the sidewalk/curb
                        area.
Step 5  Rule            arrow:straight_left: The arrow allows for both going straight and turning left.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid yellow edge line and
                        curb
Step 6  go_straight     allowed (correct): allowed by the straight-left arrow
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the straight-left arrow
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn left. Do not attempt to
                        change lanes to the left or right as both boundaries are solid.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_left'], missed ['arrow:straight_right', 'line:stop_line']), actions
                        False, unsafe ['turn_left'], citation None, contradictions []
Tokens                  in 2934, out 816, 6.33 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a tunnel or underpass ahead. My car is in one of the
                        center lanes. (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible on the right side of my
                        lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): left_boundary is a dashed line, which allows lane changes.
Step 6  change_right    allowed (WRONG, label not_determined): right_boundary is a dashed line, which allows
                        lane changes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane that allows for lane changes in both directions. Proceed straight
                        ahead; no specific turn markings are visible in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2934, out 704, 6.06 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway or expressway with a tunnel or overpass ahead. The road
                        is wide with several lanes moving in the same direction. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my left,
                        but my lane itself has no arrows or text.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 6  change_left     allowed (correct): left_boundary is dashed, allowing the move.
Step 6  change_right    prohibited (WRONG, label allowed): right_boundary is solid, prohibiting the move.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the third lane from the left. You may continue straight or change to the
                        left. Changing to the right is prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 722, 6.41 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with a wide intersection or large open area ahead. My
                        car is in one of the middle lanes. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible in the middle of my
                        lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the left lane if needed. Do not attempt to move
                        to the right as it is restricted by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2934, out 706, 6.65 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road with an overpass ahead. My car is in a lane bounded by a wall on the
                        right and a curb/hedge on the left. (lanes 1, mine 1, full)
Step 2  Left            A low hedge and a curb-like edge separate my lane from the area to the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid red wall and a sidewalk form the right boundary.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The curb/hedge prohibits moving to the left.
Step 5  Rule            right_boundary: The wall/curb prohibits moving to the right.
Step 6  change_left     prohibited (correct): prohibited by left_boundary (curb)
Step 6  change_right    prohibited (correct): prohibited by right_boundary (wall/curb)
Step 6  go_straight     allowed (contested, correct): allowed by no marking governing this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited by the physical boundaries (hedge and wall).
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 699, 75.22 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a large intersection with a pedestrian crossing
                        and traffic signals. The road is wide with multiple lanes of traffic moving in the
                        same direction. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a metal railing/fence separate my lane from the
                        sidewalk/pedestrian area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a lane
                        line on my left and an edge line on my right. | roles: The white dashed line on the
                        left is a standard lane line, and the solid line with a physical barrier on the right
                        is a standard edge line. | markings: The straight arrow in my lane is consistent with
                        the lane's purpose and the surrounding boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-through
                        traffic.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change to the left lane if
                        needed, but you must not move to the right as it is bounded by a solid line and a
                        physical barrier. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right', 'line:stop_line']), actions False, unsafe
                        ['change_left', 'go_straight'], citation None, contradictions []
Tokens                  in 2934, out 847, 7.4 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway under an overpass. The road continues straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:left_turn_waiting (insufficient): none; area:two_way_left_turn_lane
                        (insufficient): none
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both the left and right. | roles: The white dashed lines correctly
                        identify as lane lines between lanes of the same direction. | markings: No markings
                        are visible in my lane, which is consistent with a standard highway lane. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right as needed, as the dashed lines permit such maneuvers.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane'], missed []), actions True,
                        unsafe [], citation None, contradictions []
Tokens                  in 2934, out 783, 5.88 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway in China, with a clear view of the road ahead and a
                        guardrail on the right. The road appears to be a straight stretch with no immediate
                        intersection. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right, which is bounded by a
                        guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A blue circle with '60' inside is painted in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries (lane
                        line on left, edge line on right). | roles: The white dashed line on the left and
                        solid line on the right fit the roles of a lane line and an edge line respectively. |
                        markings: The speed limit marking is consistent with the lane's purpose. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and guardrail prohibit lane changes to the right.
Step 5  Rule            text:speed_limit: The speed limit for this section of the road is 60 km/h.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary and guardrail
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the third lane from the left. You may proceed straight or change to the
                        left. Changing to the right is prohibited by the solid line and guardrail. Observe the
                        60 km/h speed limit.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 839, 6.01 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus in the adjacent lane to the right. The road
                        continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 684, 5.88 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear blue sky. The road ahead is straight
                        with no immediate intersection or ramp visible. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left (2nd from the
                        right) is consistent with a white dashed line on the left and a solid white line on
                        the right. | roles: The white dashed line on the left correctly identifies a lane-
                        change possibility, and the solid white line on the right correctly identifies the
                        edge of the roadway. | markings: No markings are present in my lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right onto the shoulder
                        or beyond.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane if needed. Do not attempt to
                        change to the right as the solid line prohibits it.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 767, 7.44 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a median and a shoulder. The road ahead is
                        straight with several lanes of traffic moving in the same direction. (lanes 3, mine 2,
                        full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the shoulder/edge of the road.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a lane
                        line on my left and an edge line on my right. | roles: The white dashed line on the
                        left correctly identifies a lane-change possibility, and the solid white line on the
                        right correctly identifies the edge of the roadway. | markings: No markings were
                        observed in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line prohibits moving onto the shoulder or area beyond
                        the line.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if needed, but you should
                        not move to the right as it is the edge of the roadway. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 768, 13.14 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The road appears to be a
                        divided highway with a concrete barrier on the right. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a concrete barrier separate my lane from the right edge of the
                        roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may continue straight or
                        change to the left lane. Changing to the right is prohibited by the solid line and
                        barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 703, 6.21 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway under an overpass. The road continues straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line and a white line are visible, with a guardrail and a curb further
                        to the right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible on the pavement in my
                        lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow left_boundary
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid yellow
                        right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 690, 6.19 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a gantry overhead. The road continues straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 673, 13.55 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with overhead power lines and high-voltage towers.
                        The road ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane.; line:yield_line
                        (insufficient): No markings visible in my lane.; line:stop_yield (insufficient): No
                        markings visible in my lane.; line:crosswalk (insufficient): No markings visible in my
                        lane.; arrow:merge_left (insufficient): No markings visible in my lane.;
                        arrow:merge_right (insufficient): No markings visible in my lane.; arrow:two_way_left
                        (insufficient): No markings visible in my lane.; no_turn:left (insufficient): No
                        markings visible in my lane.; no_turn:right (insufficient): No markings visible in my
                        lane.; text:only (insufficient): No markings visible in my lane.; text:bus
                        (insufficient): No markings visible in my lane.; text:hov (insufficient): No markings
                        visible in my lane.; text:stop (insufficient): No markings visible in my lane.;
                        text:keep_clear (insufficient): No markings visible in my lane.; text:speed_limit
                        (insufficient): No markings visible in my lane.; symbol:hov_diamond (insufficient): No
                        markings visible in my lane.; symbol:bike (insufficient): No markings visible in my
                        lane.; symbol:other (insufficient): No markings visible in my lane.;
                        area:left_turn_waiting (insufficient): No markings visible in my lane.;
                        area:two_way_left_turn_lane (insufficient): No markings visible in my lane.; area:grid
                        (insufficient): No markings visible in my lane.; area:channelizing (insufficient): No
                        markings visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 6  change_left     allowed (correct): The left boundary is a dashed line, which allows lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid line, which prohibits
                        lane changes.
Step 6  go_straight     allowed (contested, correct): No markings govern this action, and it is allowed.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the left lane. Changing to the right lane is
                        prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'no_turn:left', 'no_turn:right', 'symbol:bike',
                        'symbol:hov_diamond', 'symbol:other', 'text:bus', 'text:hov', 'text:keep_clear',
                        'text:only', 'text:speed_limit', 'text:stop'], missed []), actions False, unsafe [],
                        citation None, contradictions ['go_straight allowed without the stop that the STOP or
                        停 marking in my lane requires']
Tokens                  in 2934, out 1121, 10.23 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a guardrail on the left and a paved
                        shoulder/curb area on the right. The road continues straight ahead. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to its left, which is bounded by a
                        guardrail.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right, which leads to a
                        shoulder.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a lane
                        line on my left and a lane line on my right. | roles: The white solid lines correctly
                        function as lane lines between lanes of the same direction. | markings: No markings
                        are present to contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 739, 5.9 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or carriageway with overhead signs. My car is in a lane heading
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an emergency
                        vehicle lane.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right into the emergency
                        lane.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left if needed, but you must not move into the emergency vehicle lane on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 2934, out 746, 5.53 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with overhead signs. My car is in a lane heading
                        straight. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an emergency
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 6  change_left     allowed (correct): left_boundary allows it
Step 6  change_right    prohibited (correct): right_boundary prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may change to the left if needed, but you are
                        prohibited from moving into the emergency lane on your right. Continue straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 684, 6.54 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the right. The road ahead is
                        straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is next to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left if necessary, but you are prohibited from moving to the right due to the solid
                        line and curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 753, 6.88 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an upcoming intersection or exit area. My car
                        is in a lane with clear markings ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        shoulder or exit lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in my
                        lane.; arrow:left (full): A large white arrow pointing left is painted in the lane to
                        my left.; arrow:right (full): A large white arrow pointing right is painted in the
                        lane to my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white dashed
                        line on my left and solid line on my right. | roles: The white dashed line on the left
                        and solid line on the right are standard for lane separation. | markings: The straight
                        arrow in my lane matches the lane's purpose. The left and right arrows in adjacent
                        lanes are consistent with their respective lane purposes. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the primary permitted
                        movement for this lane.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left if
                        necessary, but you are prohibited from changing lanes to the right due to the solid
                        line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed ['text:speed_limit']), actions
                        True, unsafe [], citation None, contradictions ['turn_left not_applicable although an
                        arrow shows it', 'turn_right not_applicable although an arrow shows it']
Tokens                  in 2934, out 909, 77.77 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overhead gantry containing traffic signals. The road
                        ahead appears to be a large intersection or a major junction. (lanes 4, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the yellow lane
                        lines on both sides. | roles: The yellow solid lines correctly identify the boundaries
                        between lanes of the same direction. | markings: The straight arrow is consistent with
                        the lane's purpose and the surrounding boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid yellow lines. Proceed straight through the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 771, 6.55 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median or divider on the right. The road continues
                        straight ahead with no immediate intersection visible. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a green-painted median/curb area on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a
                        dashed line on the left and a solid line on the right. | roles: The white dashed line
                        on the left correctly identifies a lane-change possibility, and the solid line on the
                        right correctly identifies an edge/median boundary. | markings: The straight arrow in
                        my lane is consistent with the lane's purpose and the surrounding boundaries. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the primary permitted
                        movement for this lane.
Step 6  change_left     allowed (contested, correct): allowed by the dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You can proceed straight ahead or change into the left
                        lane. Changing to the right is prohibited by the solid line and median.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 820, 5.67 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a tram line on the right. The car is in a lane heading
                        straight toward a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line and a tram track/curb area form the right boundary.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the yellow lane line
                        on my left and the edge line on my right. | roles: The yellow solid line on the left
                        correctly identifies a lane boundary, and the yellow solid line/curb on the right
                        identifies the edge of the roadway. | markings: No markings are present in my lane. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving to the right onto the
                        tram area.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow lane line on the left
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow edge line and curb on
                        the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 763, 7.02 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with a clear sky. The road continues straight ahead
                        with an intersection or junction visible in the distance. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is next to a
                        curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white lane line is visible to the left, and a white
                        lane line is visible to the right.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit changing into the area to the
                        right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 698, 5.31 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane that appears to
                        be a dedicated turn lane or a lane leading to a turn. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line with a dashed line next to it separates my lane from the lane to
                        my right.
                        yellow solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in the
                        center of my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries. |
                        roles: The yellow lines are consistent with lane dividers in a right-hand traffic
                        region. | markings: The straight arrow is consistent with the lane's path. | unseen:
                        None | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the permitted movement for
                        this lane.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Do not attempt to change lanes
                        to the left or right as the solid yellow lines prohibit it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 775, 6.76 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane or special lane on the left and a
                        sidewalk/curb on the right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from a lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line and a curb separate my lane from a sidewalk/parking area.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A large yellow arrow pointing straight ahead is painted in my
                        lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited by the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 724, 6.51 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The sun is low in the sky,
                        creating significant glare. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        bus lane or special lane.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the special lane to the
                        right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid lines. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 735, 6.44 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus in the center. The road appears to be a divided
                        boulevard with several lanes of traffic moving in the same direction. (lanes 3, mine
                        3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and a sidewalk
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; arrow:straight
                        (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line and curb prohibit moving to the right beyond the
                        roadway.
Step 6  change_left     allowed (correct): The left boundary is a dashed line, which allows a lane change.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid edge line and a curb,
                        which prohibits moving right.
Step 6  go_straight     allowed (correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane. Do
                        not attempt to move to the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['go_straight decided from an arrow that cannot be read']
Tokens                  in 2934, out 601, 43.2 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with an intersection ahead. My car is in a lane
                        heading straight or turning right. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        right-turn lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:right (full): A right-turn arrow is painted in my lane.
Step 4  Cross-check     position: The lane count and my position as the third lane from the left are
                        consistent with the presence of lane lines on both sides. | roles: The white solid
                        lines correctly identify the boundaries as lane lines. | markings: The right-turn
                        arrow in my lane is consistent with the lane's purpose and the solid lines. | unseen:
                        None | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:right: The arrow indicates that my lane is designated for turning right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     prohibited (contested, label allowed): prohibited
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      allowed: allowed
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to make a right turn at the upcoming intersection. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 776, 10.93 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city intersection with a crosswalk and several vehicles. The sun is
                        creating a significant glare in the upper left of the photo. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane or edge of the roadway.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): A white crosswalk is visible ahead across the intersection.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles; I am in
                        the middle of three lanes. | roles: The white dashed line on the left and solid line
                        on the right are consistent with lane markings in a multi-lane road. | markings: The
                        crosswalk is consistent with an intersection ahead. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows me to change into the lane to my left.
Step 5  Rule            right_boundary: The solid line prohibits me from changing into the lane to my right.
Step 5  Rule            line:crosswalk: The crosswalk indicates a pedestrian crossing area where I should be
                        prepared to stop.
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, label not_determined): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the left lane. Do not attempt to change into
                        the right lane as it is prohibited by the solid line.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 806, 53.44 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large overhead sign and a taxi to the left. The road
                        ahead appears to be a straight continuation or a large intersection. (lanes 3, mine 3,
                        full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line marks the edge of the roadway, next to a red-painted lane.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my left,
                        but my lane itself has no arrows or text.
Step 4  Cross-check     position: The lane count of 3 and my position as the rightmost lane (3) are consistent
                        with the white dashed line on my left and the yellow edge line on my right. | roles:
                        The white dashed line is a standard lane-change line, and the yellow solid line is a
                        standard edge line. | markings: No markings are present in my lane to contradict the
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid yellow edge line prohibits moving to the right beyond the
                        roadway.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change into the lane to
                        your left. Do not attempt to move to the right beyond the yellow line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 786, 6.89 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with a wide boulevard ahead. The road appears to be a one-way
                        street or a divided highway with multiple lanes moving in the same direction. (lanes
                        3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line and a curb separate my lane from the sidewalk/pedestrian area on
                        the right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A straight arrow pointing forward is painted in the center of
                        my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a lane
                        line on my left and an edge line on my right. | roles: The white lane line on the left
                        and yellow edge line on the right are standard for a middle lane in a right-hand
                        traffic system. | markings: The straight arrow in my lane is consistent with the
                        lane's purpose and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. You should continue straight ahead;
                        lane changes to the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 666, 6.41 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a central divider and side barriers. The road ahead
                        appears to be a straight stretch of a divided highway or boulevard. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Two parallel solid yellow lines are visible in the
                        lane to my left, but my lane itself has no markings.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The yellow solid lines correctly
                        identify the boundaries between lanes of the same direction. | markings: No markings
                        are present in my lane to contradict the boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow left_boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2934, out 755, 6.86 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the right and a wide intersection or large
                        road ahead. My car is in a lane with a straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a bus lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (2) are consistent with a dashed line on
                        the left and a solid line on the right. | roles: The white dashed line on the left and
                        solid line on the right are standard for lane separation. | markings: The straight
                        arrow in my lane is consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows me to change lanes to the left.
Step 5  Rule            right_boundary: The solid line prohibits me from changing lanes to the right into the
                        bus lane.
Step 5  Rule            arrow:straight: The arrow indicates that my lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left if
                        needed, but you are prohibited from moving into the bus lane on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 808, 6.04 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overpass ahead. My car is in a lane that appears to
                        have a straight-ahead arrow. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for a lane change to the left.
Step 5  Rule            right_boundary: The solid line prohibits a lane change to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left if
                        necessary, but you are prohibited from changing lanes to the right due to the solid
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 740, 6.52 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The car is in a lane heading
                        straight or turning left. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right, which is a dedicated
                        left-turn lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in my lane.; arrow:left (full):
                        A white left-turn arrow is painted in the lane to my right.; arrow:straight (full): A
                        white straight-ahead arrow is painted in the lane to my left.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries. |
                        roles: The white dashed line on the left and solid line on the right are consistent
                        with lane-line roles. | markings: The left-turn arrow in my lane is consistent with
                        the lane's purpose and the solid line separating it from the straight-ahead lane to
                        the left. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:left: The arrow indicates that a left turn is the intended movement for this
                        lane.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the left-turn arrow in my lane
Step 6  turn_left       allowed: allowed by the left-turn arrow in my lane
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to make a left turn at the upcoming intersection. You may change lanes
                        to the left if necessary, but do not attempt to move into the lane to your right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['line:stop_line']), actions False, unsafe
                        ['change_left'], citation None, contradictions ['go_straight prohibited although an
                        arrow shows it']
Tokens                  in 2934, out 904, 7.74 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane on the right. The road ahead is a straight
                        stretch with a bus stop area on the right. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a bus lane on the right.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is painted in the middle of my
                        lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: A solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: A solid white line prohibits changing lanes to the right into the bus
                        lane.
Step 5  Rule            line:stop_yield: The marking indicates a requirement to stop before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by solid white left_boundary
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by solid white right_boundary
Step 6  go_straight     stop_first (contested, label allowed): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight, but you should be prepared to stop
                        as indicated by the markings. Lane changes to the left or right are prohibited by the
                        solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 591, 4.87 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in China with an intersection ahead. My car is in a lane
                        heading straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible at the intersection.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The white dashed lines correctly
                        function as lane lines between lanes of the same direction. | markings: The stop line
                        is consistent with an approaching intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 5  Rule            line:stop_line: My car must come to a complete stop before entering the intersection.
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the dashed left_boundary
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the dashed right_boundary
Step 6  go_straight     stop_first (contested, label allowed): allowed as no markings prohibit it and it is
                        the default movement
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right as the lines are dashed. You must come to a
                        complete stop at the white stop line before proceeding straight through the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 2934, out 792, 22.15 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in China with an intersection ahead. My car is in a lane
                        moving forward. (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:yield_line (full): A white dashed line with an inverted triangle and a left-turn
                        arrow is visible ahead of my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white dashed
                        lines on both sides. | roles: The white dashed lines correctly function as lane lines
                        between lanes of the same direction. | markings: The yield line and left-turn arrow
                        are consistent with the lane's purpose and the dashed boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 5  Rule            line:yield_line: The yield line indicates a point where the driver should yield to
                        other traffic before proceeding.
Step 6  change_left     allowed (correct): The left boundary is a dashed line, which allows a lane change.
Step 6  change_right    allowed (correct): The right boundary is a dashed line, which allows a lane change.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight, and the lane
                        continues forward.
Step 6  turn_left       allowed: The yield line and arrow ahead indicate a left turn is possible.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is marked directly to the left or ahead of my lane.
Step 7  Reflect         consistent
Advice                  You can proceed straight or turn left at the upcoming intersection. Lane changes to
                        the left or right are permitted as the boundaries are dashed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:yield_line'], missed []), actions True, unsafe [], citation None,
                        contradictions ['turn_left decided without an arrow or prohibited-movement marking']
Tokens                  in 2934, out 828, 6.53 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with an intersection ahead. My car is in one of the
                        rightmost lanes. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a raised curb separate my lane from the sidewalk/pedestrian
                        area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead and slightly left.;
                        line:stop_yield (full): A white character '停' (stop) is painted in the lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
Step 5  Rule            line:stop_yield: The '停' marking requires a full stop before proceeding.
Step 6  change_left     allowed (contested, correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary and curb
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the '停' marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are permitted to change lanes to the left, but you must come to a complete stop
                        before proceeding straight due to the '停' marking. Do not move to the right as it is
                        bounded by a curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight', 'line:stop_yield'], missed ['text:other']), actions True, unsafe
                        [], citation None, contradictions []
Tokens                  in 2934, out 845, 7.97 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane heading
                        straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left if
                        necessary, but you are prohibited from changing lanes to the right due to the solid
                        line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 2934, out 733, 6.31 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the right. Ahead, there is a
                        wide intersection or open area with traffic signals. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from a median on the left.
                        white solid, curb yes, center_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk and a bike lane on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving to the right onto the
                        sidewalk/bike lane.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 735, 6.69 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings and trees on both sides. The road ahead is a straight
                        multi-lane street. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which ends in a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my right,
                        but my lane has no markings.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        yellow center line on my left and a white edge line on my right. | roles: The yellow
                        solid line correctly identifies a center line, and the white solid line with a curb
                        correctly identifies an edge line. | markings: No markings are present in my lane to
                        contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits changing into the lane to the
                        left.
Step 5  Rule            right_boundary: The solid white edge line and curb prohibit moving to the right onto
                        the sidewalk.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are prohibited by the
                        solid yellow line, and moving to the right is prohibited by the solid white line and
                        curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 763, 18.3 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the right. The road ahead
                        appears to be a straight stretch with a potential intersection or signalized area in
                        the distance. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from the sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving onto the sidewalk to the
                        right.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow lane line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 705, 6.63 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a large intersection with a pedestrian crosswalk.
                        The road is wide with several lanes of traffic moving in the same direction. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane or edge of the roadway.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        the boundaries between lanes of the same direction. | markings: The straight arrow in
                        my lane is consistent with the lane's purpose and the surrounding lane markings. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You are prohibited from
                        changing lanes to the left or right due to the solid white lines. Proceed straight
                        through the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 805, 6.34 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings and trees on both sides. The road ahead is
                        straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is next to a
                        curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the lane to the
                        left.
Step 5  Rule            right_boundary: The solid white edge line prohibits crossing into the area to the
                        right (curb/sidewalk).
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 681, 7.11 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test A | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a covered walkway or structure on the left and a building on
                        the right. The road ahead appears to be a straight stretch of a divided highway or a
                        large urban thoroughfare. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a metal railing/barrier form the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as 2 (rightmost) is consistent with a
                        white lane line on my left and an edge line on my right. | roles: The white solid line
                        on the left acts as a lane divider, and the white line/railing on the right acts as an
                        edge line. | markings: No markings are present to contradict the boundaries. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The edge line and barrier prohibit moving off the roadway to the
                        right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are prohibited by the
                        solid white line, and the right side is bounded by a physical barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 763, 19.1 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bike lane on the right. The road continues straight
                        ahead into a distant urban area. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a red-painted bike lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right into the bike lane.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left if needed, but you are prohibited from moving into the bike lane on your right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 740, 6.41 s
```
