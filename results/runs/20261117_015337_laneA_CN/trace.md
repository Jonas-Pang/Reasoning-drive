# Reasoning of lane run 20261117_015337_laneA_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with an intersection ahead. My car is in one of the
                        rightmost lanes. (lanes 3, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the roadway, with a curb and a grassy area
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line and curb prohibit moving to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change to the left if needed,
                        but you must stay within the roadway as the right side is a solid edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 745, 12.42 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear sky. The road continues straight ahead
                        with no immediate intersection visible. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the shoulder/edge of the road.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line prohibits moving onto the shoulder or area beyond
                        it.
Step 6  change_left     allowed (correct): left_boundary allows it
Step 6  change_right    prohibited (correct): right_boundary prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change to the left lane. Do
                        not move to the right as it is bounded by a solid line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 686, 15.41 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway in China with overhead green directional signs. My car is in a
                        lane heading forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the shoulder/edge of the road.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries (lane
                        line on left, edge line on right). | roles: The white solid lines correctly identify
                        the lane-line and edge-line roles. | markings: No markings are present to contradict
                        the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving onto the shoulder to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane_line on the left
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge_line on
                        the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 731, 41.65 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bridge or elevated structure ahead. The car is in a
                        lane moving forward towards a distant intersection or continuation of the road. (lanes
                        3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        shoulder or a restricted area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A yellow arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving into the area to the right.
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
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 733, 12.15 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large intersection or junction ahead. My car is in a
                        lane that appears to be a dedicated turn lane or a special lane near a junction.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from the sidewalk/pedestrian area on
                        the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (full): A large white character '停' (stop) is painted in the center of
                        my lane.; arrow:straight (full): A white arrow pointing straight ahead is visible
                        behind the stop character.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane line
                        on my left and the edge line on my right. | roles: The white solid lines and curb
                        correctly define the lane boundaries. | markings: The '停' character and straight arrow
                        are consistent with a lane that requires a stop before proceeding straight. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            line:stop_yield: The '停' character requires my car to come to a complete stop before
                        proceeding.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the permitted movement for
                        this lane.
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line on the
                        left
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line and
                        curb on the right
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the '停' marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight, but you must come to a complete stop
                        at the '停' marking before proceeding. Do not attempt to change lanes to the left or
                        right as both boundaries are solid.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:stop_yield'], missed ['text:bus']), actions None, unsafe [],
                        citation None, contradictions []
Tokens                  in 2934, out 942, 45.15 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a concrete barrier on the left and a stone wall/curb on
                        the right. An overpass is visible ahead. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to the left, which is separated by
                        a concrete barrier.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway next to a stone wall and curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree; I am in the rightmost lane of my
                        direction. | roles: The white solid line on the left is a lane line, and the white
                        solid line on the right is an edge line. | markings: No markings are present in my
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving off the roadway to the
                        right.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it and it is not a merge
                        or special lane.
Step 6  turn_left       not_applicable: not_applicable as there is no left-turn arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no right-turn arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no u-turn arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 807, 13.32 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with a bus stop on the left and a sidewalk with parked scooters
                        on the right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line is next to a solid white edge line, which is next to a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white edge line and curb prohibit moving to the right onto
                        the sidewalk.
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
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 726, 14.07 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a large intersection ahead. My car is in one of the
                        right-hand lanes. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from the sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible on the left side of my
                        lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the left lane. Do not attempt to move to the
                        right as it is bounded by a curb and solid line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2934, out 695, 14.51 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. The road ahead appears to be a
                        straight stretch with multiple lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane
                        or shoulder area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) is consistent with a
                        lane line on my left and an edge line on my right. | roles: The white solid lines are
                        consistent with lane and edge boundaries in a right-hand traffic system. | markings:
                        No markings were observed in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving into the area to the right.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 737, 9.49 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which appears to be a
                        turn lane or edge lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 6  change_left     allowed: left_boundary allows it
Step 6  change_right    prohibited: right_boundary prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the left lane if needed. Do not attempt to
                        change to the right lane as it is prohibited by the solid line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        None, contradictions []
Tokens                  in 2934, out 696, 39.74 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a pedestrian area to the left. The road
                        ahead appears to be a straight stretch with a potential intersection or signalized
                        area in the distance. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from a two-way left-turn lane or median area to
                        the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in the
                        center of my lane.; text:other (full): Chinese characters are painted on the road
                        surface in my lane, likely indicating lane usage or restrictions.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries
                        (center line on left, lane line on right). | roles: The yellow solid line on the left
                        and white solid line on the right fit their respective roles. | markings: The straight
                        arrow and text are consistent with a through-lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the area to the left.
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the primary permitted
                        movement for this lane.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, label not_determined): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as the solid lines prohibit it. Continue straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight', 'text:other'], missed ['symbol:other']), actions False, unsafe [],
                        citation None, contradictions []
Tokens                  in 2934, out 851, 18.57 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a clear sky. The road ahead appears to be a straight stretch
                        or a wide intersection area. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a concrete curb separate my lane from the right edge of the
                        roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right off the
                        roadway.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 679, 13.64 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road passing under a bridge. The road appears to be a divided highway or
                        a large urban thoroughfare. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to its left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right, which is the edge of
                        the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles (yellow
                        line on left, white line on right). | roles: The yellow solid line on the left and
                        white solid line on the right fit the roles of a lane line and an edge line
                        respectively. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line marks the edge of the roadway and prohibits
                        moving further to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
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
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 789, 18.84 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test A | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway in China with overhead signs. My car is in a lane heading
                        straight forward. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly function as lane lines between
                        lanes of the same direction. | markings: No markings are present to contradict the
                        boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit it
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
Tokens                  in 2934, out 727, 16.09 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for a lane change to the left.
Step 5  Rule            right_boundary: The dashed line allows for a lane change to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (WRONG, label prohibited): left_boundary is a dashed line, which allows a lane
                        change.
Step 6  change_right    allowed (WRONG, label prohibited): right_boundary is a dashed line, which allows a
                        lane change.
Step 6  go_straight     allowed (correct): arrow:straight indicates straight movement is allowed.
Step 6  turn_left       not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  turn_right      not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  u_turn          not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left or
                        right as needed, as the lane markings are dashed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation None, contradictions []
Tokens                  in 2934, out 752, 15.77 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban intersection in China. My car is in a lane approaching a large
                        intersection with crosswalks and multiple turn lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible across the lane before the
                        intersection.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line prohibits changing into the lane to the right.
Step 5  Rule            line:stop_line: My car must come to a complete stop before entering the intersection.
Step 6  change_left     prohibited (correct): prohibited by solid white left_boundary
Step 6  change_right    prohibited (correct): prohibited by solid yellow right_boundary
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to line:stop_line
Step 6  turn_left       stop_first: stop_first due to line:stop_line
Step 6  turn_right      stop_first: stop_first due to line:stop_line
Step 6  u_turn          stop_first: stop_first due to line:stop_line
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the white line before proceeding. Lane changes to
                        the left or right are prohibited by the solid boundary lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions True, unsafe [], citation None, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 2934, out 771, 17.98 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide boulevard layout. Ahead, there is a large
                        intersection or junction with overhead signage. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        landscaped median.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        the white dashed line on my left and solid line on my right. | roles: The white dashed
                        line on the left and solid line on the right are consistent with standard lane
                        markings. | markings: No markings are visible in my lane. | unseen: None. | result:
                        consistent
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
Advice                  You may proceed straight or change to the left lane. Changing to the right lane is
                        prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 737, 15.77 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide boulevard and trees on both sides. The road
                        continues straight ahead. (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white dashed lines on both sides. | roles: The white dashed lines correctly
                        identify the boundaries as lane lines. | markings: No markings were observed in the
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): The left boundary is a dashed line, which allows a lane change.
Step 6  change_right    allowed (correct): The right boundary is a dashed line, which allows a lane change.
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in my lane govern a left turn.
Step 6  turn_right      not_applicable: No markings in my lane govern a right turn.
Step 6  u_turn          not_applicable: No markings in my lane govern a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  You are in a standard through-lane. You may proceed straight or change lanes in either
                        direction as the lane markings are dashed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 761, 15.97 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with an intersection or junction ahead. My car is in
                        one of the right-hand lanes. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from a sidewalk/median area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:left (full): A white arrow pointing left is painted in the lane to my left.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid right_boundary and curb
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change to the left if
                        necessary, but you must not move to the right as it is bounded by a solid line and a
                        curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions None, unsafe [], citation None,
                        contradictions ['turn_left not_applicable although an arrow shows it']
Tokens                  in 2934, out 793, 12.7 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test A | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road approaching a large intersection. My car is in one of the lanes
                        heading forward. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line and a curb separate my lane from the sidewalk/curb area.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead and slightly left.;
                        arrow:left (full): A white arrow pointing left.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries (lane
                        line on left, edge line on right). | roles: The white lane line and yellow edge line
                        fit their respective roles. | markings: The arrows in my lane indicate the allowed
                        movements at the intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid yellow line and curb prohibit moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead.
Step 5  Rule            arrow:left: The arrow allows turning left.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line and curb
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the left turn arrow marking
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or turn left from your current lane. Do not attempt to change
                        lanes to the left or right as both boundaries are solid.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe ['turn_left'], citation None,
                        contradictions []
Tokens                  in 2934, out 852, 17.16 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with an intersection ahead. The traffic light is
                        green for the forward direction. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is occupied by a
                        bus.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
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
Advice                  You are in a lane designated for going straight. You may change lanes to the left if
                        necessary, but you are prohibited from changing lanes to the right due to the solid
                        line. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 746, 16.78 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with an intersection ahead. The road curves slightly
                        to the right. (lanes 4, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead and slightly right.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
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
Advice                  You are in a lane designated for going straight. Lane changes to the left or right are
                        prohibited by the solid lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2934, out 713, 15.17 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overhead gantry showing multiple exit
                        options. My car is in a lane that appears to be a dedicated lane for a specific exit
                        or direction. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right, which appears to be a
                        shoulder or a different exit lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): A large white arrow pointing straight ahead with a slight
                        turn to the right.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the presence of lane
                        lines on both sides. | roles: The white solid lines correctly function as lane lines
                        between lanes of the same direction. | markings: The straight-right arrow is
                        consistent with the lane's purpose as an exit lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is intended for going straight
                        or turning slightly right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      allowed: allowed
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight or follow the slight right turn as
                        indicated by the lane markings. Lane changes to the left or right are prohibited by
                        the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['text:other']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 2934, out 799, 19.43 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a gantry ahead. The road is wide and open.
                        (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): left_boundary is a dashed line, which allows lane changes.
Step 6  change_right    allowed (correct): right_boundary is a dashed line, which allows lane changes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a standard highway lane. You are permitted to go straight, change lanes to
                        the left or right, and there are no specific turn restrictions visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2934, out 692, 13.03 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. The road appears to be a divided
                        boulevard with trees on both sides. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left if necessary, but you are prohibited from changing lanes to the right due to the
                        solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2934, out 744, 14.16 s
```
