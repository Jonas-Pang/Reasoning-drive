# Reasoning of lane run 20261117_015615_laneB_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road with an intersection ahead. My car is in a lane heading straight.
                        (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a white solid line on the right. | roles: The white dashed line
                        on the left correctly identifies a crossable lane line, and the white solid line on
                        the right correctly identifies a road edge line. | markings: The straight arrow in my
                        lane is consistent with the lane's function and the surrounding boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow [CN-5.13.1].
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow or marking.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or marking.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow or marking.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. You are permitted to change into
                        the left lane if necessary, but you must not move to the right of the solid white edge
                        line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 727, 13.76 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear sky. The road ahead appears to be a
                        straight stretch with a slight curve or merge point in the distance. (lanes 3, mine 2,
                        full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane, next to a paved shoulder and a
                        guardrail.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:straight (insufficient): No markings are
                        visible in my lane.; text:stop (insufficient): No markings are visible in my lane.;
                        area:left_turn_waiting (insufficient): No markings are visible in my lane.;
                        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white broken
                        line on my left and the white solid line on my right. | roles: The white broken line
                        on the left correctly identifies a lane-line, and the white solid line on the right
                        correctly identifies an edge-line. | markings: No markings were observed, which is
                        consistent with the lack of specific instructions in the lane. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the motor vehicle
                        lanes. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: no marking governs this action [null]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, which marks the
                        edge of the roadway [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in my lane allow or prohibit a left turn.
Step 6  turn_right      not_applicable: No markings in my lane allow or prohibit a right turn.
Step 6  u_turn          not_applicable: No markings in my lane allow or prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is visible to the left.
Step 7  Reflect         consistent
Advice                  You may change into the left lane as it is separated by a broken line. You should stay
                        within your lane and not move onto the shoulder to the right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line', 'text:stop'], missed []),
                        actions True, unsafe [], citation unlisted, contradictions ['go_straight decided from
                        an arrow that cannot be read', 'go_straight allowed without the stop that the STOP or
                        停 marking in my lane requires']
Tokens                  in 7595, out 930, 22.65 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a large overhead gantry sign. The road ahead
                        is clear of immediate intersections. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which is an edge lane
                        or a boundary to a shoulder/median.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (insufficient): none; no_turn:left (insufficient): none; text:only
                        (insufficient): none; text:bus (insufficient): none; text:hov (insufficient): none;
                        text:stop (insufficient): none; text:keep_clear (insufficient): none; text:speed_limit
                        (insufficient): none; symbol:hov_diamond (insufficient): none; symbol:bike
                        (insufficient): none; symbol:other (insufficient): none; area:left_turn_waiting
                        (insufficient): none; area:two_way_left_turn_lane (insufficient): none; area:grid
                        (insufficient): none; area:channelizing (insufficient): none; line:stop_line
                        (insufficient): none; line:yield_line (insufficient): none; line:stop_yield
                        (insufficient): none; line:crosswalk (insufficient): none
Step 4  Cross-check     position: The lane count (3) and my lane position (2) are consistent with the
                        boundaries: a white line on the left and a yellow line on the right. | roles: The
                        white line on the left is a lane line and the yellow line on the right is an edge
                        line, which is consistent with Chinese traffic rules. | markings: No markings were
                        observed in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid yellow line prohibits crossing into the area to the right.
                        [[CN-6.1.4]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid yellow edge line
                        [CN-6.1.4]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:straight', 'line:crosswalk', 'line:stop_line',
                        'line:stop_yield', 'line:yield_line', 'no_turn:left', 'symbol:bike',
                        'symbol:hov_diamond', 'symbol:other', 'text:bus', 'text:hov', 'text:keep_clear',
                        'text:only', 'text:speed_limit', 'text:stop'], missed []), actions False, unsafe [],
                        citation in_pack_not_accepted, contradictions ['go_straight decided from an arrow that
                        cannot be read', 'go_straight allowed without the stop that the STOP or 停 marking in
                        my lane requires']
Tokens                  in 7595, out 1039, 28.36 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch with a possible intersection or merging area in the distance. (lanes
                        3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to my right, which appears to be a
                        median or a separated lane.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white line on
                        the left and a yellow line on the right. | roles: The white line on the left is a lane
                        line, and the yellow line on the right is a center line, which is consistent with
                        Chinese traffic rules. | markings: The straight arrow in my lane is consistent with
                        the lane's role. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid yellow line prohibits crossing into the lane to the right.
                        [[CN-6.1.4] [mandatory] GB 5768.3-2025, section 6.1.4, page 44]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1,
                        表1, page 27]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          allowed: allowed by the straight or U-turn arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn if permitted by local signs. Lane
                        changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 823, 14.28 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a large building and a subway entrance on
                        the right. My car is in a lane that appears to be a special lane or a lane with
                        specific restrictions, heading towards a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane
                        or a lane next to a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): A white character '交' is painted in the center of my lane.;
                        text:other (full): A white character '车' is painted below the first character in my
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines are consistent with
                        lane lines and edge lines in a same-direction flow. | markings: The '交' and '车'
                        characters (likely part of '公交' or similar, but only '交' and '车' are clearly visible)
                        are consistent with a special lane marking. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway. [[CN-5.4.3]]
Step 5  Rule            text:other: The characters '交' and '车' indicate a specific lane use, likely a bus lane
                        or similar, but no specific rule for these characters is provided in the list.
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line
                        [CN-6.2.1]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane with specific markings ('交' and '车'). You may proceed straight but
                        are prohibited from changing lanes to the left or right due to the solid white lines.
                        Be aware of the lane's specific purpose indicated by the pavement text.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed ['text:bus']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 794, 25.68 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a physical barrier on the left and a wall/curb on the
                        right. An intersection or overpass is visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from a lane to the left, which is separated by a
                        concrete barrier.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane, next to a sidewalk/wall.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane.; line:yield_line
                        (insufficient): No markings visible in my lane.; line:stop_yield (insufficient): No
                        markings visible in my lane.; arrow:straight (insufficient): No markings visible in my
                        lane.; area:left_turn_waiting (insufficient): No markings visible in my lane.;
                        area:two_way_left_turn_lane (insufficient): No markings visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my position (1) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white solid line on
                        the left is a lane line; the white solid line on the right is an edge line. This is
                        consistent with Chinese traffic rules. | markings: No markings were observed in the
                        lane, which is consistent with the lack of specific movement instructions. | unseen:
                        No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: no marking governs this action [null]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line on the right [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line'], missed []), actions True,
                        unsafe [], citation unlisted, contradictions ['leftmost lane, but a lane line on the
                        left', 'go_straight decided from an arrow that cannot be read', 'go_straight allowed
                        without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 7595, out 840, 17.24 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees lining both sides. Ahead, the road continues
                        straight with several lanes visible. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is next to a
                        sidewalk/parking area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify lane boundaries
                        for traffic in the same direction. | markings: No markings are present, which is
                        consistent with a standard through-lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white line on the left [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white line on the right [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit straight
                        movement
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through-lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 785, 19.7 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or major junction ahead. The car is in a
                        lane moving forward. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a lane line on my
                        left and an edge line on my right. | roles: The white dashed line on the left and
                        white solid line on the right fit the roles of a crossable lane line and an edge line
                        respectively. | markings: The straight arrow in my lane is consistent with the lane's
                        forward direction. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lanes.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): The broken white line on the left allows a lane
                        change [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): The solid white edge line on the right prohibits
                        crossing into the area beyond [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): The straight arrow in my lane allows going straight
                        [CN-5.13.1].
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight ahead. You may change into the
                        lane on your left as it is marked with a broken line, but you should not move to the
                        right beyond the solid edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_left'], citation
                        accepted, contradictions []
Tokens                  in 7595, out 730, 14.88 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. The road ahead appears to be a
                        straight stretch with a slight curve or intersection in the distance. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane.; line:yield_line
                        (insufficient): No markings visible in my lane.; line:stop_yield (insufficient): No
                        markings visible in my lane.; arrow:straight (insufficient): No markings visible in my
                        lane.; text:stop (insufficient): No markings visible in my lane.;
                        area:left_turn_waiting (insufficient): No markings visible in my lane.;
                        area:two_way_left_turn_lane (insufficient): No markings visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white lines are
                        consistent with lane lines and edge lines for a road where traffic keeps to the right.
                        | markings: No markings were observed in my lane. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to my left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lanes.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line', 'text:stop'], missed []),
                        actions False, unsafe [], citation unlisted, contradictions ['go_straight decided from
                        an arrow that cannot be read', 'go_straight allowed without the stop that the STOP or
                        停 marking in my lane requires']
Tokens                  in 7595, out 853, 10.33 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a large intersection. The road is wide with
                        several lanes of traffic moving forward. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none; line:yield_line (insufficient): none;
                        line:stop_yield (insufficient): none; arrow:straight (insufficient): none; arrow:left
                        (insufficient): none; arrow:right (insufficient): none; text:stop (insufficient):
                        none; text:keep_clear (insufficient): none; area:left_turn_waiting (insufficient):
                        none; area:two_way_left_turn_lane (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 6  change_left     prohibited: prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited: prohibited by the solid white lane line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:left', 'arrow:right',
                        'arrow:straight', 'line:stop_line', 'line:stop_yield', 'line:yield_line',
                        'text:keep_clear', 'text:stop'], missed ['line:crosswalk']), actions None, unsafe [],
                        citation in_pack_not_accepted, contradictions ['go_straight decided from an arrow that
                        cannot be read', 'go_straight allowed without the stop that the STOP or 停 marking in
                        my lane requires']
Tokens                  in 7595, out 753, 20.65 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane that appears
                        to be a through lane or a turn lane approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight ahead and left.;
                        arrow:straight (full): A white arrow pointing straight ahead.; arrow:left (full): A
                        white arrow pointing left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify lane
                        boundaries for traffic in the same direction. | markings: The arrows in my lane
                        (straight and left) are consistent with the lane's function as a multi-directional
                        lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight_left: The arrow indicates that the lane allows for both straight ahead
                        and left turn movements. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right.
Step 6  go_straight     allowed (contested, label not_determined): allowed by the straight ahead arrow in my
                        lane.
Step 6  turn_left       allowed: allowed by the left turn arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn left from your current lane. Lane changes to
                        the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight', 'arrow:straight_left'], missed ['symbol:other']),
                        actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 722, 18.62 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane road with a clear view ahead towards a distant
                        intersection or overpass. My car is in one of the central lanes. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:straight (insufficient): No markings are
                        visible in my lane.; area:left_turn_waiting (insufficient): No markings are visible in
                        my lane.; area:two_way_left_turn_lane (insufficient): No markings are visible in my
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly identify as
                        lane lines separating traffic in the same direction. | markings: No markings were
                        observed, which is consistent with the clear pavement in the foreground. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side to the left lane.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side to the right
                        lane. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane where lane changes to the left or right are prohibited by solid
                        white lines. You should proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line'], missed []), actions True,
                        unsafe [], citation in_pack_not_accepted, contradictions ['go_straight decided from an
                        arrow that cannot be read', 'go_straight allowed without the stop that the STOP or 停
                        marking in my lane requires']
Tokens                  in 7595, out 782, 13.0 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road passing under a bridge. The road ahead appears to be a continuous
                        stretch of roadway. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in the center of my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is on my left and a white edge line is on my right. | roles: The
                        yellow solid line correctly identifies a center line (separating opposing traffic or a
                        special lane, but here it acts as a center line), and the white solid line correctly
                        identifies an edge line. | markings: The straight arrow is consistent with the lane's
                        purpose and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        to the left or right as both boundaries are solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 766, 14.82 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with overhead signs. The road ahead is a straight
                        stretch of highway. (lanes 4, mine 3, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.; line:yield_line (full): No
                        markings are visible in my lane.; line:stop_yield (full): No markings are visible in
                        my lane.; arrow:straight (full): No markings are visible in my lane.; text:stop
                        (full): No markings are visible in my lane.; text:keep_clear (full): No markings are
                        visible in my lane.; area:left_turn_waiting (full): No markings are visible in my
                        lane.; area:two_way_left_turn_lane (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly identify as lane lines
                        separating traffic in the same direction. | markings: No markings were observed in my
                        lane, which is consistent with a standard through lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line', 'text:keep_clear',
                        'text:stop'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 7595, out 812, 15.28 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. My car is in a
                        lane with a straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white lines correctly identify lane boundaries for
                        traffic in the same direction. | markings: The straight arrow is consistent with the
                        lane's position and the surrounding markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the left lane.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing into the right lane.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that my lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or change into the left lane. Changing into the right
                        lane is prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left'],
                        citation accepted, contradictions []
Tokens                  in 7595, out 659, 53.91 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is approaching a large multi-lane intersection in an urban area with high-rise
                        buildings. The road ahead is wide with multiple lanes of traffic. (lanes 3, mine 2,
                        full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the opposing traffic flow.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        area:grid (full): A white grid pattern is visible on the pavement ahead of my lane at
                        the intersection.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        a white lane line on my left and a yellow center line on my right. | roles: The white
                        dashed line on the left correctly identifies a same-direction lane line, and the solid
                        yellow line on the right correctly identifies a center line. | markings: The grid
                        marking is consistent with an intersection approach. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid yellow line prohibits me from crossing into the opposing
                        traffic flow. [[CN-6.1.4]]
Step 5  Rule            area:grid: The grid marking prohibits stopping for any reason in that area.
                        [[CN-6.8.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it and no arrow
                        restricts it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow or area is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow or area is present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn arrow or area is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you must not cross the yellow line to
                        the right. Do not stop on the grid markings at the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe
                        ['change_left'], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 733, 16.56 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and roadside greenery. An intersection or major
                        junction is visible in the distance with overhead signs. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white dashed
                        lines on both sides. | roles: The white dashed lines correctly identify as lane lines
                        between lanes of the same direction. | markings: No markings are present, which is
                        consistent with the clear lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line [CN-5.2.1-2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is a crossable
                        lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight, and the lane
                        continues forward.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the lane markings are broken white lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7595, out 803, 18.8 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The road is wide with several
                        lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:straight (insufficient): No markings are
                        visible in my lane.; text:stop (insufficient): No markings are visible in my lane.;
                        area:left_turn_waiting (insufficient): No markings are visible in my lane.;
                        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white lines correctly identify lane boundaries for
                        traffic in the same direction. | markings: No markings were observed in the lane,
                        which is consistent with the lack of specific movement restrictions. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing into the lane on my
                        right. [[CN-6.2.1]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white line, which
                        prohibits lane changes [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): No markings govern this action, and the lane is not a
                        special lane.
Step 6  turn_left       not_applicable: No markings govern this action.
Step 6  turn_right      not_applicable: No markings govern this action.
Step 6  u_turn          not_applicable: No markings govern this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may change into the lane on your left, but you are prohibited from changing into
                        the lane on your right. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:straight',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line', 'text:stop'], missed []),
                        actions False, unsafe [], citation accepted, contradictions ['go_straight decided from
                        an arrow that cannot be read', 'go_straight allowed without the stop that the STOP or
                        停 marking in my lane requires']
Tokens                  in 7595, out 843, 14.69 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or major junction ahead. The road is wide
                        with clear lane markings. (lanes 4, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is in the lane to my
                        right.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white dashed lines correctly identify
                        as crossable lane lines between lanes of the same direction. | markings: The straight
                        arrow in my lane is consistent with the lane's purpose and the surrounding markings. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane on my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change into the lane on my right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for travel straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        is a crossable lane line.
Step 6  change_right    allowed (contested, correct): The right boundary is a broken white line, which is a
                        crossable lane line.
Step 6  go_straight     allowed (contested, correct): The lane contains a straight ahead arrow.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. You are permitted to change lanes to
                        the left or right as needed, as both boundaries are broken white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 711, 13.05 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. There are several
                        lanes of traffic moving in the same direction. (lanes 4, mine 3, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line and a curb separate my lane from the sidewalk/curb on the right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight ahead and left.;
                        arrow:straight (full): A white arrow pointing straight ahead.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        a white dashed line on my left and a yellow solid line/curb on my right. | roles: The
                        white dashed line correctly identifies a lane-change possibility, and the yellow solid
                        line correctly identifies the right edge of the roadway. | markings: The straight and
                        straight-left arrows are consistent with the lane's position and the surrounding lane
                        markings. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane to my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The yellow edge line marks the left-hand edge of the direction of
                        travel (relative to the road's orientation) or the right-hand edge of the roadway, and
                        the solid pattern prohibits crossing it. [[CN-5.4.3]]
Step 5  Rule            arrow:straight_left: The arrow indicates that I am permitted to go straight or turn
                        left. [[CN-5.13.1]]
Step 5  Rule            arrow:straight: The arrow indicates that I am permitted to go straight. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid yellow edge line and curb
                        [CN-5.4.3].
Step 6  go_straight     allowed (correct): Allowed by the straight arrow marking [CN-5.13.1].
Step 6  turn_left       allowed (WRONG, label prohibited): Allowed by the straight-left arrow marking
                        [CN-5.13.1].
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable as there is no right-turn
                        arrow.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable as there is no U-turn arrow.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your current lane. You can change into the
                        lane to your left, but you are prohibited from moving to the right onto the sidewalk.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_left'], missed []), actions False, unsafe ['turn_left'], citation
                        accepted, contradictions []
Tokens                  in 7595, out 841, 59.78 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The traffic light is green. (lanes
                        3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is occupied by a
                        bus.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        as lane lines separating traffic in the same direction. | markings: The straight arrow
                        is consistent with the lane's role and the surrounding boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the right [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking [CN-5.13.1]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 675, 14.45 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching an intersection with a large open area and
                        buildings on the right. The road curves slightly to the left. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a yellow center
                        line on the left and a white lane line on the right. | roles: The yellow center line
                        correctly separates opposing traffic (or a left-turn lane) and the white line
                        separates same-direction traffic. | markings: The straight arrow is consistent with
                        the lane's path. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line prohibits crossing into the lane to the left.
                        [[CN-6.1.1] [mandatory] GB 5768.3-2025, section 6.1.1, page 41]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Lane changes to the left or
                        right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7595, out 744, 55.03 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overhead gantry and signs. The road ahead
                        appears to be a straight stretch of highway. (lanes 4, mine 3, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the lane to my left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a white edge line, which
                        marks the edge of the roadway [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): The lane contains a straight-ahead arrow [CN-5.13.1].
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change into the lane
                        to your left as it is marked with a broken line, but you should not move to the right
                        as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['text:other']), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 7595, out 666, 13.88 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear sky. The road ahead is straight with
                        several lanes of traffic. (lanes 4, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.; arrow:straight (full): No
                        markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white dashed lines on both sides. | roles: The white dashed lines correctly
                        identify as lane lines between lanes of the same direction. | markings: No markings
                        are present, which is consistent with a standard highway lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight, and the lane is a
                        standard through lane.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a standard through lane. You may change lanes to the left or right as
                        needed, and you are permitted to continue straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 7595, out 665, 12.08 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. The road appears to be a divided
                        boulevard with trees and a fence on the left. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The white dashed lines correctly
                        function as crossable lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the straight-ahead movement allowed by
                        the dashed boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change into the left lane.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change into the right lane.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        travel. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is a crossable
                        lane line.
Step 6  go_straight     allowed (correct): The lane contains a straight-ahead arrow and the boundaries are
                        dashed.
Step 6  turn_left       not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  turn_right      not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  u_turn          not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead or change lanes to the left
                        or right as the dashed white lines permit lane changes.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 689, 18.31 s
```
