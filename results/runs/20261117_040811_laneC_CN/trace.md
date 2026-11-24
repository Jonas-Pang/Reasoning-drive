# Reasoning of lane run 20261117_040811_laneC_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test C | gemma4:12b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a clear sky. Ahead, there is a wide intersection or open
                        area with several lanes of traffic moving in the same direction. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a shoulder/curb area
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white solid line on
                        the left correctly identifies a same-direction lane separation, and the white solid
                        line on the right correctly identifies the edge of the roadway. | markings: The
                        straight arrow in my lane is consistent with the lane's role as a through lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement for
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are discouraged/prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 853, 14.37 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test C | gemma4:12b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a divided median. The road ahead appears to be a straight
                        stretch of highway or a large thoroughfare. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, adjacent to a concrete barrier
                        and a shoulder.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white dashed line on my left and a white solid line on my right. | roles: The white
                        dashed line on the left correctly identifies a lane-to-lane separation, and the white
                        solid line on the right correctly identifies the edge of the roadway. | markings: No
                        markings were observed in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     allowed (correct): The white dashed line on the left allows for a lane change.
Step 6  change_right    prohibited (correct): The solid white line and curb on the right prohibit moving onto
                        the shoulder.
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight.
Step 6  turn_left       not_applicable: No markings or arrows govern this action.
Step 6  turn_right      not_applicable: No markings or arrows govern this action.
Step 6  u_turn          not_applicable: No markings or arrows govern this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed. Do not move onto the right shoulder.
                        Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 658, 14.83 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overhead gantry showing exit signs. My car
                        is in a lane heading forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway, which is
                        bordered by a guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white lines
                        correctly represent lane separation and the right edge of the roadway. | markings: No
                        markings are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are discouraged/prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 770, 21.79 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway with a bridge or elevated structure ahead.
                        The car is traveling in a lane that appears to be part of a multi-lane flow. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane
                        or a lane ending.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid white line is visible on the right, but no
                        specific arrows or words are in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a white
                        line on my left and a white line on my right. | roles: The white lines correctly
                        delineate same-direction traffic flows. | markings: No markings were observed in the
                        lane itself. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages crossing into the left lane.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            line:stop_line: No rule applies as no stop line was clearly identified.
Step 6  change_left     prohibited (contested, correct): The solid white line on the left discourages
                        crossing.
Step 6  change_right    prohibited (contested, correct): The solid white line on the right delineates the edge
                        of the roadway.
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight.
Step 6  turn_left       not_applicable: No markings or arrows allow a left turn.
Step 6  turn_right      not_applicable: No markings or arrows allow a right turn.
Step 6  u_turn          not_applicable: No markings or arrows allow a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are discouraged/prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 708, 13.82 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban roadway with high-rise buildings in the background.
                        The road appears to be a one-way street or a multi-lane thoroughfare with a median or
                        barrier on the right. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway, which is
                        adjacent to a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): A large white Chinese character '专' (special/exclusive) is painted
                        in the center of my lane.; text:other (full): A large white Chinese character '交'
                        (transport/traffic) is painted below the first character.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        a white lane line on my left and a white edge line on my right. | roles: The white
                        solid line on the left is a standard lane line, and the white solid line on the right
                        is a standard edge line. | markings: The Chinese characters are centered in the lane
                        and do not contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            text:other: The Chinese characters are used to regulate or guide traffic, but their
                        specific meaning is not defined in the provided US rules. [US-3B.20-01]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line and the
                        concrete barrier on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit straight
                        movement.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane with specific markings (Chinese characters) that likely designate a
                        special use for the lane. You may proceed straight but are prohibited from changing
                        lanes to the left or right due to the solid lines and the barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed ['text:bus']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 797, 23.71 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a concrete barrier on the left and a stone wall/curb
                        on the right. An overpass is visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A concrete barrier separates my lane from the lanes to the left.
                        none none, curb yes, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right, which is bounded by a
                        stone wall.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. The
                        concrete barrier acts as a center line separating opposing traffic flows. | roles: The
                        white solid line on the right correctly identifies a lane line, and the barrier
                        correctly identifies a center line. | markings: No markings are present in my lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The barrier serves as a separation of traffic traveling in opposite
                        directions. [US-3A.03-03-04]
Step 5  Rule            right_boundary: The solid white line discourages crossing into the adjacent lane.
                        [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the lane closest to the center barrier. You may proceed straight ahead.
                        Lane changes to the right are discouraged/prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 765, 13.2 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the left and a sidewalk/parking area on the
                        right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/parking area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on the left (lane_line) and a white line/curb on the right (edge_line). |
                        roles: The white solid line on the left correctly identifies a lane-line, and the
                        white solid line on the right correctly identifies an edge_line. | markings: The
                        straight arrow is consistent with the lane's role as a through lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane on
                        the left. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight ahead is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Do not attempt to change lanes to the left or right as the solid lines prohibit
                        such maneuvers.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 860, 53.28 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a median and trees on the right. An intersection or
                        large junction is visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        curb/median.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        line on the left is a standard lane line, and the white solid line on the right is a
                        standard edge line. | markings: The straight arrow is consistent with the lane's
                        forward path. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead as indicated by the arrow.
                        Lane changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 694, 14.39 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with trees and parked cars on the left. The road ahead
                        appears to be a straight continuation of the current path. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane or edge lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The white solid lines correctly
                        delineate lanes in the same direction of travel. | markings: The straight arrow is
                        consistent with the straight path of the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 671, 9.92 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching a large intersection. My car is
                        in one of the center lanes. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        lane-to-lane boundaries for same-direction traffic. | markings: No markings were
                        observed in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited: prohibited by the solid white left boundary line
Step 6  change_right    prohibited: prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 613, 20.2 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a large intersection or open area ahead. The car is
                        positioned in a lane with a white fence and a yellow-painted area to its left. (lanes
                        3, mine 2, full)
Step 2  Left            A yellow-painted area and a white metal fence separate my lane from the lane to the
                        left.
                        yellow none, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the center
                        of my lane.; text:other (partial): White Chinese characters are painted in the lane,
                        though they are partially obscured by the car in front.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow edge/fence on the left and a white dashed line on the right. | roles: The
                        yellow edge line and white dashed lane line fit the roles of an edge and a lane
                        separator respectively. | markings: The straight arrow is consistent with the lane's
                        purpose and the dashed line on the right. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The yellow edge line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the right lane is
                        permitted. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, label not_determined): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead or change into the right
                        lane. Changing to the left is prohibited by the yellow edge line and physical barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight', 'text:other'], missed ['symbol:other']), actions True, unsafe [],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 898, 55.0 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a clear sky. The road appears to be a divided highway or a
                        large urban thoroughfare with buildings and trees in the distance. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white lane line on my left and a white edge line on my right. | roles: The white solid
                        line on the left is a standard lane line, and the white solid line on the right is a
                        standard edge line. | markings: No markings are present in the lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are discouraged/prohibited by the solid white
                        markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 811, 16.1 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway passing under a bridge. The road ahead appears to be a continuous
                        stretch of roadway with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from a lane to my left, which is bounded by a
                        concrete barrier and a metal guardrail.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white lane-use arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is on my left and a white edge line is on my right. | roles: The
                        yellow solid line correctly identifies a center line (separation of opposite traffic)
                        and the white solid line identifies the right edge. | markings: The straight arrow is
                        consistent with the lane's role as a through lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line marking on a
                        two-way roadway, but here it delineates the separation of opposite traffic flows.
                        [US-3B.01-05]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow and the lack of
                        prohibiting markings
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 711, 16.28 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with overhead signs indicating different lane uses. The road
                        ahead is a straight stretch of highway. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an emergency
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3rd from left) are consistent with the
                        boundaries: a white dashed line on the left and a solid white line on the right. |
                        roles: The white dashed line on the left and solid white line on the right are
                        consistent with lane-to-lane separation. | markings: The straight arrow in my lane is
                        consistent with the 'Through Lane' designation on the overhead sign for this lane. |
                        unseen: None | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for a lane change to the left.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing to the right.
                        [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the dashed white line on the left
                        (US-3B.06-05-06).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white line on the right
                        (US-3B.06-05-06).
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow marking (US-3B.23-01).
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead or change lanes to the left.
                        Changing lanes to the right into the emergency lane is prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 901, 14.28 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes in the
                        same direction of travel. | markings: The straight arrow is consistent with a through
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line.
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk', 'line:stop_line']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 814, 19.05 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban intersection with multiple lanes of traffic. My car is positioned in a lane
                        approaching a large crosswalk and intersection. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): A white crosswalk is visible ahead across the intersection.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        white dashed line on the left and a solid white line on the right. | roles: The white
                        lines correctly delineate lanes of traffic moving in the same direction. | markings:
                        The crosswalk is consistent with an intersection approach. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            line:crosswalk: No specific rule provided for crosswalks in the list, but they
                        generally indicate a pedestrian crossing area.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the dashed white line on the left
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): Prohibited by the solid white line on the right
                        [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow or specific lane
                        marking.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or specific lane
                        marking.
Step 6  u_turn          not_applicable: Not applicable as there is no u-turn arrow or specific lane marking.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you should not change into the right
                        lane. Proceed straight through the intersection, being mindful of the crosswalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 908, 16.95 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a median separating opposing traffic. The road ahead appears
                        to be a straight stretch with an upcoming intersection or junction. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        median.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane.; line:yield_line (full): No
                        markings visible in my lane.; line:stop_yield (full): No markings visible in my lane.;
                        arrow:merge_left (full): No markings visible in my lane.; arrow:merge_right (full): No
                        markings visible in my lane.; arrow:two_way_left (full): No markings visible in my
                        lane.; no_turn:left (full): No markings visible in my lane.; no_turn:right (full): No
                        markings visible in my lane.; text:only (full): No markings visible in my lane.;
                        text:bus (full): No markings visible in my lane.; text:hov (full): No markings visible
                        in my lane.; text:stop (full): No markings visible in my lane.; text:keep_clear
                        (full): No markings visible in my lane.; text:speed_limit (full): No markings visible
                        in my lane.; symbol:hov_diamond (full): No markings visible in my lane.; symbol:bike
                        (full): No markings visible in my lane.; symbol:other (full): No markings visible in
                        my lane.; area:left_turn_waiting (full): No markings visible in my lane.;
                        area:two_way_left_turn_lane (full): No markings visible in my lane.; area:grid (full):
                        No markings visible in my lane.; area:channelizing (full): No markings visible in my
                        lane.; line:stop_line (full): No markings visible in my lane.; line:yield_line (full):
                        No markings visible in my lane.; line:stop_yield (full): No markings visible in my
                        lane.; line:crosswalk (full): No markings visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: No markings were observed in the lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'no_turn:left', 'no_turn:right', 'symbol:bike',
                        'symbol:hov_diamond', 'symbol:other', 'text:bus', 'text:hov', 'text:keep_clear',
                        'text:only', 'text:speed_limit', 'text:stop'], missed []), actions False, unsafe [],
                        citation in_pack_not_accepted, contradictions ['go_straight allowed without the stop
                        that the STOP or 停 marking in my lane requires']
Tokens                  in 8628, out 1269, 25.03 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a wide boulevard ahead. The road appears to be a
                        divided highway or a large multi-lane street with a median and landscaping. (lanes 4,
                        mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway, which is
                        bordered by a curb and landscaping.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid white line is visible on the right, and a solid
                        white line is on the left.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        the white lane line on my left and the edge line on my right. | roles: The white lines
                        correctly delineate same-direction traffic and the right edge of the roadway. |
                        markings: No specific arrows or words are visible in my lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the third lane from the left. You may proceed straight ahead. Lane changes
                        to the left or right are discouraged or prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 808, 13.93 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an intersection or junction ahead. The road is divided
                        by a median with landscaping. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        median.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in my
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight arrow is consistent with a
                        through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages crossing into the left lane.
                        [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages crossing into the right lane.
                        [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white lane line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are discouraged/prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 662, 12.36 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The road is lined with trees and
                        buildings. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        curb and a tree-lined area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white lane
                        line on my left and the edge line on my right. | roles: The white solid line on the
                        left is a standard lane line, and the white solid line on the right acts as an edge
                        line near a curb. | markings: The straight arrow in my lane is consistent with the
                        lane's role as a through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement for
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are discouraged/prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 844, 19.78 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with an intersection ahead. The traffic is moving
                        forward towards a signalized intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is occupied by a
                        bus.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both the left and right. | roles: The white solid lines correctly
                        delineate lanes of traffic moving in the same direction. | markings: The straight
                        arrow is consistent with the lane's role as a through lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white right boundary
                        line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 838, 17.52 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The road curves slightly to the
                        left. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which ends at a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a
                        yellow center line on the left and a white edge line on the right. | roles: The yellow
                        line on the left correctly identifies a center line (opposite traffic), and the white
                        line on the right correctly identifies an edge line. | markings: The straight arrow is
                        consistent with the lane's path. | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a single solid yellow line as a center
                        line in this context, but it generally separates opposite traffic. [null]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8628, out 654, 16.89 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with an overhead gantry and signs. The road ahead appears to be a
                        straight continuation of the highway. (lanes 4, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be an
                        exit or shoulder area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in my
                        lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight arrow is consistent with the
                        straight road ahead and the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. You may proceed straight ahead, but
                        lane changes to the left or right are discouraged or prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['text:other']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 674, 15.38 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The road appears to be a
                        divided highway or a large multi-lane thoroughfare. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be
                        the edge of the roadway or a shoulder.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the boundaries: a
                        white dashed line on my left and a solid white line on my right. | roles: The white
                        dashed line on the left correctly identifies a lane-line for same-direction traffic,
                        and the solid white line on the right correctly identifies an edge-line. | markings:
                        No markings are present, which is consistent with a standard through-lane. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings or geometry indicate a turn.
Step 6  turn_right      not_applicable: Not applicable as no markings or geometry indicate a turn.
Step 6  u_turn          not_applicable: Not applicable as no markings or geometry indicate a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not attempt to move to the
                        right beyond the solid white edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 861, 15.34 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test C | gemma4:12b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. The road appears to be a divided or
                        multi-lane thoroughfare with trees and a fence on the left. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        lane-to-lane boundaries for same-direction traffic. | markings: The straight arrow in
                        my lane is consistent with the straight-ahead movement allowed by the lane boundaries.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: The arrow indicates that going straight ahead is a permitted movement
                        in this lane. [US-3B.23-01]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are discouraged or prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 678, 49.88 s
```
