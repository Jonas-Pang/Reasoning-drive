# Reasoning of lane run 20261117_124251_laneC_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane on the left and a bus currently in the lane
                        to the right. An intersection is ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lines on both sides. | roles: The white solid lines correctly function as lane
                        dividers. | markings: The straight arrow is consistent with the lane's purpose. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            arrow:straight: The driver shall use this lane for going straight. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (correct): prohibited by the solid white line on the right [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking [IN-8(1)(c)]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line', 'symbol:bike']), actions False, unsafe
                        [], citation unlisted, contradictions []
Tokens                  in 5803, out 825, 7.13 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction or intersection ahead. My car is in a lane
                        that appears to be a dedicated turn lane or a lane leading into a junction. (lanes 3,
                        mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white arrow pointing left is painted in my lane.; arrow:straight
                        (full): A white arrow pointing straight ahead is painted in my lane.; arrow:right
                        (full): A white arrow pointing right is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with having
                        a lane line on both my left and right. | roles: The white solid lines correctly
                        function as lane lines between lanes of the same direction. | markings: The
                        combination of left, straight, and right arrows in my lane is consistent with a multi-
                        directional turn lane or a lane that allows multiple movements at the upcoming
                        junction. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: I must not cross the solid white line to overtake or change lanes.
                        [[IN-6(4)]]
Step 5  Rule            right_boundary: I must not cross the solid white line to overtake or change lanes.
                        [[IN-6(4)]]
Step 5  Rule            arrow:left: I should use this lane for a left turn. [[IN-8(1)(c)]]
Step 5  Rule            arrow:straight: No specific rule prohibits going straight if an arrow is present, but
                        the arrow indicates it is a permitted movement. [no marking governs this action]
Step 5  Rule            arrow:right: I should remain in this lane while taking a right turn. [[IN-8(2)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left boundary line
                        [IN-6(4)]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white right boundary line
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       allowed: allowed by the left arrow marking [IN-8(1)(c)]
Step 6  turn_right      allowed: allowed by the right arrow marking [IN-8(2)(c)]
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight, turn left, or turn right from your current lane as indicated
                        by the road markings. Do not attempt to change lanes before the junction as the solid
                        white lines prohibit it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed ['line:crosswalk']), actions
                        None, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 1075, 55.26 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. The road is wide with several
                        lanes of traffic moving forward. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which has a bicycle
                        symbol.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in the center of my
                        lane.; symbol:bike (full): A white bicycle symbol is in the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lines
                        on both sides. | roles: The white solid lines correctly function as lane dividers. |
                        markings: The straight arrow in my lane is consistent with the lane's purpose. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white line to the left is prohibited. [[IN-6(4)]]
Step 5  Rule            right_boundary: Crossing the solid white line to the right is prohibited. [[IN-6(4)]]
Step 5  Rule            arrow:straight: The arrow indicates that this lane is for straight movement.
                        [[IN-8(1)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [IN-8(1)(c)]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 862, 53.56 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops on the left and residential buildings on the right.
                        The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from a lane to the left, which is
                        adjacent to a sidewalk.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No arrows, words, or symbols are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        center line is on my left and a lane line is on my right. | roles: The yellow double
                        solid line correctly identifies a center line (separating opposing traffic or a
                        special lane), and the white solid line correctly identifies a lane divider. |
                        markings: No markings are present to contradict the boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the double longitudinal solid
                        yellow line. [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake another
                        vehicle. [[IN-6(4)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow line [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          prohibited: prohibited by the double solid yellow line [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane and proceed straight ahead. Lane changes to the
                        left or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 814, 52.53 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street with a pedestrian crossing ahead. The road appears to be a multi-lane
                        street with a junction or crossing area in the distance. (lanes 2, mine 1, full)
Step 2  Left            A white solid line separates my lane from the sidewalk/pedestrian area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white transverse line (stop line) is visible before the
                        pedestrian crossing.; area:channelizing (full): White diagonal lines (hatching) are
                        visible to the left of the lane ahead of the crossing.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) are consistent with
                        the left edge line and the right lane line. | roles: The white solid lines correctly
                        function as an edge line on the left and a lane line on the right. | markings: The
                        stop line and channelizing markings are consistent with a pedestrian crossing and a
                        junction area. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a white solid edge line, but it generally
                        marks the boundary of the drivable area. [null]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake another
                        vehicle. [IN-6(4)]
Step 5  Rule            line:stop_line: The driver shall stop the vehicle before the stop line preceding the
                        pedestrian crossing. [IN-12(1)(a)]
Step 5  Rule            area:channelizing: No specific rule provided for channelizing markings, but they
                        indicate a no-driving zone. [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line and curb.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line [IN-6(4)].
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the stop line [IN-12(1)(a)].
Step 6  turn_left       stop_first: stop_first due to the stop line [IN-12(1)(a)].
Step 6  turn_right      stop_first: stop_first due to the stop line [IN-12(1)(a)].
Step 6  u_turn          stop_first: stop_first due to the stop line [IN-12(1)(a)].
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the white line before the pedestrian crossing. Do
                        not attempt to change lanes as the lines are solid.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing', 'line:stop_line'], missed ['line:crosswalk']), actions None,
                        unsafe [], citation unlisted, contradictions ['turn_left, turn_right, u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 1010, 72.36 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with houses on the left and a sidewalk on the right. The road
                        ahead appears to be a straight continuation of the current street. (lanes 3, mine 2,
                        full)
Step 2  Left            A double solid red line separates my lane from the lane to my left.
                        other double_solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which has a bus stop
                        area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line separates the lane to my right
                        from the bus stop area.; area:grid (full): Yellow markings indicating a bus stop area
                        are visible to the right of my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall not drive over the double solid red line. [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            area:grid: The driver shall not park in a bus lane. [[IN-22.(2)(h)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid red line [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          prohibited: prohibited by the double solid red line [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane. Lane changes to the left or right are prohibited
                        by the solid line markings. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid', 'line:stop_yield'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions ['u_turn decided without an arrow or prohibited-movement
                        marking', 'go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 5803, out 671, 55.03 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a park/fence on the left. The
                        road ahead appears to be a straight continuation of the current street. (lanes 4, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly function
                        as lane lines between lanes of the same direction. | markings: The straight arrow is
                        consistent with the straight road ahead and the lane boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to change lanes.
                        [[IN-6(4)]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight movement.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 823, 52.38 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops and buildings on the right. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a lane to the left, which appears to be a
                        cycle lane or a dedicated lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area or a lane to the right where
                        cars are parked.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lines on both sides. | roles: The white solid lines correctly define the
                        boundaries of my lane. | markings: The straight arrow is consistent with the straight
                        road ahead and the lane boundaries. | unseen: None | result: consistent
Step 5  Rule            left_boundary: I am prohibited from crossing the solid white line to the left.
                        [[IN-6(4)]]
Step 5  Rule            right_boundary: I am prohibited from crossing the solid white line to the right.
                        [[IN-6(4)]]
Step 5  Rule            arrow:straight: The arrow indicates that this lane is intended for straight movement.
                        [[IN-8(1)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking [IN-8(1)(c)]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 849, 60.15 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian crossing ahead. My car is positioned in a
                        lane facing forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        parking or buffer zone.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible just before the pedestrian
                        crossing.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly function
                        as lane dividers. | markings: The stop line is correctly placed before the pedestrian
                        crossing. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: I am prohibited from crossing the solid white line to overtake or
                        change lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: I am prohibited from crossing the solid white line to the right.
                        [[IN-6(4)]]
Step 5  Rule            line:stop_line: I must stop before the stop line if a red light is displayed (though
                        no signal is visible, the line indicates a required stop point). [[IN-12(1)(a)]]
Step 6  change_left     prohibited (contested, correct): prohibited by solid white line [IN-6(4)]
Step 6  change_right    prohibited (contested, correct): prohibited by solid white line [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead but must stop at the white stop line before the
                        pedestrian crossing. Lane changes to the left or right are prohibited by the solid
                        white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 5803, out 841, 54.4 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian crossing and a cycle lane ahead. My car is
                        in a lane following a white van. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left, which contains a cycle
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is occupied by a
                        car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol is painted in the lane to my left.;
                        line:crosswalk (full): A white dashed line and a white solid line form a pedestrian
                        crossing ahead.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly act as lane
                        dividers. | markings: The bicycle symbol is in the adjacent lane, not my lane. The
                        crosswalk is ahead of my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: I am prohibited from crossing the solid white line to the left to
                        overtake. [[IN-6(4)]]
Step 5  Rule            right_boundary: I am prohibited from crossing the solid white line to the right to
                        overtake. [[IN-6(4)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as the solid white lines on both sides prohibit lane
                        changes. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk', 'symbol:bike'], missed ['text:speed_limit']), actions False, unsafe
                        [], citation unlisted, contradictions []
Tokens                  in 5803, out 797, 71.23 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with shops on the left and a sidewalk on the
                        right. Ahead, there is a junction or a wide area with several lanes of traffic. (lanes
                        3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:merge_left (full): A white arrow pointing left is painted in the lane to my
                        left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly function
                        as lane dividers and an edge line near the curb. | markings: The straight arrow in my
                        lane is consistent with the lane's purpose, and the left arrow in the adjacent lane is
                        consistent with its position. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the white solid line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the white solid line to move into the
                        adjacent area or sidewalk. [[IN-6(4)]]
Step 5  Rule            arrow:straight: The arrow indicates that this lane is intended for straight movement.
                        [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [IN-8(1)(c)]
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane which is designated for going straight ahead. Do not
                        attempt to change lanes to the left or right as the solid white lines prohibit it.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:merge_left', 'arrow:straight'], missed ['arrow:straight_left']), actions
                        False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 760, 12.01 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus stop and a pedestrian crossing ahead. The car is
                        positioned in a lane heading straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right, which appears to be a
                        bus lane or a dedicated lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible on the right side of
                        the lane ahead.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white dashed lines on both sides. | roles: The white dashed lines correctly
                        function as lane lines between lanes of the same direction. | markings: No specific
                        arrows or words are visible in my lane to contradict the boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver may cross the broken line to overtake but must return to
                        the lane. [[IN-6(7)]]
Step 6  change_left     allowed (correct): Allowed by the white dashed line [IN-6(7)].
Step 6  change_right    allowed (correct): Allowed by the white dashed line [IN-6(7)].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow is present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn marking is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked in my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the
                        boundaries are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 5803, out 815, 53.47 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. The car is positioned in one of
                        the lanes heading forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:left (full): A white arrow pointing left is painted in the lane to my left.;
                        arrow:right (full): A white arrow pointing right is painted in the lane to my right.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly function as
                        lane dividers. | markings: The straight arrow in my lane is consistent with the lane's
                        role as a through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white line to the left is prohibited. [[IN-6(4)]]
Step 5  Rule            right_boundary: Crossing the solid white line to the right is prohibited. [[IN-6(4)]]
Step 5  Rule            arrow:straight: The arrow indicates this lane is for straight movement. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [IN-8(1)(c)]
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited by the straight arrow marking
                        [IN-8(1)(c)]
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow marking [IN-8(1)(c)]
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow marking [IN-8(1)(c)]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to proceed straight ahead. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed ['arrow:straight_left']),
                        actions False, unsafe [], citation unlisted, contradictions ['turn_left prohibited
                        although an arrow shows it', 'turn_right prohibited although an arrow shows it']
Tokens                  in 5803, out 941, 53.88 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street with a multi-lane layout approaching an intersection. The road is lined
                        with brick buildings and a pub on the left. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which appears to be a
                        one-way or restricted lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:left (full): A white arrow pointing left is visible in the lane to my left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lines on both sides. | roles: The white solid lines correctly identify the
                        boundaries of my lane. | markings: The straight arrow in my lane is consistent with
                        the lane's purpose and the surrounding markings. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to change lanes.
                        [[IN-6(4)]]
Step 5  Rule            arrow:straight: The driver shall use this lane for going straight. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane [IN-8(1)(c)]
Step 6  turn_left       not_applicable: not_applicable as there is no left turn arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no right turn arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no u-turn arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['line:crosswalk']), actions None, unsafe [],
                        citation unlisted, contradictions ['turn_left not_applicable although an arrow shows
                        it']
Tokens                  in 5803, out 919, 58.23 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with a
                        lane line on my left and an edge line/curb on my right. | roles: The white solid lines
                        correctly function as a lane divider and an edge line. | markings: The straight arrow
                        is consistent with the lane's purpose and the surrounding boundaries. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white line to the left is prohibited. [[IN-6(4)]]
Step 5  Rule            right_boundary: Crossing the solid white line to the right is prohibited. [[IN-6(4)]]
Step 5  Rule            arrow:straight: The arrow indicates that this lane is intended for straight movement.
                        [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [IN-8(1)(c)]
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions []
Tokens                  in 5803, out 846, 53.75 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is approaching a T-junction or a crossroad in a town setting. A pedestrian
                        crossing is visible directly ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates my lane from a sidewalk/pedestrian area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from another lane of traffic on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white transverse line is painted across the lane before the
                        pedestrian crossing.; line:crosswalk (full): A white pedestrian crossing (zebra
                        crossing) is ahead.
Step 4  Cross-check     position: The lane count and position are consistent with the boundaries (edge line on
                        left, lane line on right). | roles: The white solid lines correctly define the
                        boundaries of the lane. | markings: The stop line and crosswalk are consistent with an
                        approach to an intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid white line on the left.
                        [IN-6(6)]
Step 5  Rule            right_boundary: The driver shall not drive on or over the solid white line on the
                        right. [IN-6(6)]
Step 5  Rule            line:stop_line: The driver shall stop the vehicle before the stop line preceding the
                        pedestrian crossing. [IN-12(1)(a)]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     stop_first (contested, label allowed): stop_first
Step 6  turn_left       stop_first: stop_first
Step 6  turn_right      stop_first: stop_first
Step 6  u_turn          stop_first: stop_first
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a full stop at the white line before the pedestrian crossing. Lane
                        changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['rightmost lane, but a lane line on the right', 'turn_left,
                        turn_right, u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 848, 7.98 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bus lane on the left. My car is in the lane
                        to the right of the bus lane. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid red line marks the edge of the roadway on the right.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The words 'BUS LANE' are painted in white on the lane to my left.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the left boundary
                        being a lane line and the right being an edge line. | roles: The white solid line
                        correctly identifies a lane boundary, and the red line correctly identifies the road
                        edge. | markings: The 'BUS LANE' text is in the lane to my left, which is consistent
                        with the lane markings. | unseen: None | result: consistent
Step 5  Rule            left_boundary: I am prohibited from crossing the solid white line into the bus lane.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: No specific rule provided for the red edge line, but it defines the
                        road boundary. [no passage]
Step 5  Rule            text:bus: Only buses are allowed in the lane to my left. [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the red edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane. You are prohibited from moving left into the bus lane due
                        to the solid white line and the 'BUS LANE' designation.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 5803, out 837, 56.73 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane on the left and a parked car on the right.
                        The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane with a parked car on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible further ahead in my
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) is consistent with a
                        white line on my left (bus lane) and a white line on my right (parking/outer lane). |
                        roles: The white solid lines correctly act as lane dividers. | markings: No specific
                        arrows or words are clearly visible in my lane to contradict the boundaries. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane as the solid white lines on both sides prohibit
                        lane changes. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed ['text:speed_limit']), actions False, unsafe [], citation
                        unlisted, contradictions ['go_straight allowed without the stop that the STOP or 停
                        marking in my lane requires']
Tokens                  in 5803, out 793, 53.27 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide intersection or junction ahead. The car is
                        positioned in a lane heading straight towards the junction. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly function as lane
                        dividers. | markings: The straight arrow is consistent with the lane's purpose and the
                        surrounding boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            arrow:straight: The arrow indicates that this lane is intended for straight-ahead
                        movement. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking [IN-8(1)(c)]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 832, 7.55 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in the middle lane of a
                        three-lane roadway. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 are consistent with the white
                        dashed lines on both sides. | roles: The white dashed lines correctly identify the
                        boundaries between lanes of the same direction. | markings: The straight arrow in my
                        lane is consistent with the lane's purpose and the dashed boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: I may cross the broken line to overtake, but must return to my lane.
                        [[IN-6(7)]]
Step 5  Rule            right_boundary: I may cross the broken line to overtake, but must return to my lane.
                        [[IN-6(7)]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane. [null]
Step 6  change_left     allowed (correct): Allowed by the dashed left boundary [IN-6(7)].
Step 6  change_right    allowed (correct): Allowed by the dashed right boundary [IN-6(7)].
Step 6  go_straight     allowed (correct): Allowed by the straight arrow marking.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable as there is no left turn
                        arrow in my lane.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable as there is no right turn
                        arrow in my lane.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable as there is no U-turn
                        marking.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left or
                        right as needed, provided it is safe to do so, as the lane markings are dashed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 685, 52.12 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No arrows, words, or symbols are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with a
                        lane line on my left and an edge line on my right. | roles: The white solid lines
                        correctly identify the lane boundaries. | markings: No markings are present to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to move into the
                        adjacent area. [[IN-6(4)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane as the solid white lines on both sides prohibit
                        lane changes. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 792, 53.05 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the left and a pedestrian crossing ahead.
                        The car is positioned in a lane heading straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white dashed lines on both sides. | roles: The white dashed lines correctly
                        identify lane boundaries for a multi-lane road. | markings: No markings were observed
                        in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver may cross the broken line to overtake but must return to
                        the lane. [[IN-6(7)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the white dashed line [IN-6(7)].
Step 6  change_right    allowed (correct): Allowed by the white dashed line [IN-6(7)].
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the
                        boundaries are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line', 'line:stop_yield', 'line:yield_line'], missed []), actions True,
                        unsafe [], citation unlisted, contradictions ['go_straight allowed without the stop
                        that the STOP or 停 marking in my lane requires']
Tokens                  in 5803, out 671, 58.49 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection or junction ahead. The car is positioned
                        in a central lane. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): White lines forming a box-like shape ahead of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white solid lines on both sides. | roles: The white solid lines correctly function as
                        lane lines separating traffic in the same direction. | markings: The grid area ahead
                        is consistent with a junction/intersection layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white line to the left is prohibited. [[IN-6(4)]]
Step 5  Rule            right_boundary: Crossing the solid white line to the right is prohibited. [[IN-6(4)]]
Step 5  Rule            area:grid: The vehicle shall not be stopped on the yellow box (grid area) marked on
                        the road. [[IN-22.(1)viii]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane as lane changes to the left or right are
                        prohibited by the solid white lines. Proceed straight through the junction, ensuring
                        you do not stop on the grid marking ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 5803, out 666, 54.83 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops on the left and a sidewalk. Ahead, there is a
                        junction or a continuation of the road with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which has a straight
                        arrow.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which has a left-turn
                        arrow.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A straight arrow pointing forward is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lines on both sides. | roles: The white solid lines correctly act as lane
                        dividers. | markings: The straight arrow in my lane is consistent with the straight-
                        ahead movement allowed by the solid lines. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left to
                        overtake. [[IN-6(4)]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[IN-6(4)]]
Step 5  Rule            arrow:straight: The straight arrow indicates that this lane is intended for straight-
                        ahead movement. [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          prohibited (correct): prohibited by the solid white line [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Do not attempt to change lanes
                        or perform a U-turn as the solid white lines prohibit these maneuvers.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 5803, out 690, 56.02 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. An intersection or junction is
                        ahead where the road continues straight. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible across the lane ahead.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with a
                        lane line on my left and an edge line/curb on my right. | roles: The white solid lines
                        and curb correctly define the boundaries of the middle lane. | markings: The stop line
                        is consistent with an upcoming junction/intersection. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the solid white line to the left is prohibited. [[IN-6(4)]]
Step 5  Rule            right_boundary: Crossing the solid white line to the right is prohibited. [[IN-6(4)]]
Step 5  Rule            line:stop_line: The vehicle must stop before the stop line if a red light is
                        displayed. [[IN-12(1)(a)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead but must stop at the white
                        stop line if the signal is red. Lane changes to the left or right are prohibited due
                        to the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 817, 55.15 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrianized area or sidewalk to the right. Ahead,
                        there is a junction or a wide crossing area with some markings. (lanes 3, mine 2,
                        full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/pedestrian area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:left (full): A white arrow pointing left is visible in the lane to my left.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        dashed line on the left indicates another lane of my direction, and a solid line on
                        the right indicates the edge of the roadway. | roles: The white dashed line on the
                        left and solid line on the right fit the roles of lane_line and edge_line
                        respectively. | markings: The straight arrow in my lane is consistent with the lane's
                        role as a through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        movement.
Step 6  change_left     allowed (correct): allowed by the dashed line [IN-6(7)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid edge line and curb
                        [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change to the left lane
                        if necessary, but you must stay within your lane and not move toward the right curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions ['turn_left not_applicable although an arrow shows it']
Tokens                  in 5803, out 904, 71.45 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch with a junction or intersection further ahead. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        cycle lane or a restricted lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No arrows, words, or symbols are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) is consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly define
                        the boundaries of the middle lane. | markings: No markings are present in the lane,
                        which is consistent with the lack of specific movement instructions. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to change lanes.
                        [[IN-6(4)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable as no left-turn arrow is present
Step 6  turn_right      not_applicable: not_applicable as no right-turn arrow is present
Step 6  u_turn          not_applicable: not_applicable as no u-turn arrow is present
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is marked
Step 7  Reflect         consistent
Advice                  You should stay in your current lane as the solid white lines on both sides prohibit
                        lane changes. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 828, 11.82 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the left and a dedicated lane for general
                        traffic. The car is in a lane next to a bus lane. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): A large 'BUS LANE' marking with a bus symbol is painted in the lane
                        to my left.; line:stop_line (insufficient): A white line is visible at the bottom of
                        the photo, but no specific arrows or words are in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        solid line on the left (separating from a bus lane) and a dashed line on the right
                        (separating from another lane). | roles: The solid white line on the left and dashed
                        white line on the right are standard for lane separation and lane-change permissions.
                        | markings: The 'BUS LANE' marking is in the lane to the left, which is consistent
                        with the solid line boundary. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the bus lane to overtake
                        or change lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The broken white line allows crossing into the lane on the right for
                        overtaking. [[IN-6(7)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the lane on your right. Do not cross the solid
                        white line into the bus lane on your left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line', 'text:bus'], missed []), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 5803, out 851, 57.17 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide sidewalk and trees on the left and a row of shops
                        on the right. The road ahead appears to be a straight stretch with parking areas on
                        both sides. (lanes 2, mine 2, full)
Step 2  Left            A white solid line separates my lane from a parking area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white solid line separates my lane from a parking area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): A white zigzag line is painted in the middle of my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 2 (rightmost) are consistent
                        with the white solid lines on both sides acting as edge lines for a central travel
                        lane. | roles: The white solid lines correctly function as edge lines for the travel
                        lane. | markings: The zigzag line is a common UK marking for pedestrian crossings or
                        restricted areas, consistent with the urban setting. | unseen: None | result:
                        consistent
Step 5  Rule            left_boundary: No specific rule provided for white solid edge lines, but standard
                        practice prohibits crossing into the parking area. [null]
Step 5  Rule            right_boundary: No specific rule provided for white solid edge lines, but standard
                        practice prohibits crossing into the parking area. [null]
Step 5  Rule            symbol:other: No specific rule provided for zigzag markings in the provided list.
                        [null]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Proceed straight ahead in your current lane. Do not attempt to change lanes into the
                        parking areas on either side as they are bounded by solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 819, 12.09 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane heading
                        towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A grey curb and a metal fence separate my lane from the sidewalk on the right.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): A white arrow pointing left is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white line on
                        my left and the curb on my right. | roles: The white solid line correctly identifies a
                        lane-line, and the curb correctly identifies an edge-line. | markings: The left-turn
                        arrow in my lane is consistent with the lane's purpose. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: I am prohibited from crossing the solid white line to overtake or
                        change lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: No specific rule provided for a curb/fence boundary, but it defines
                        the edge of the drivable area.
Step 5  Rule            arrow:left: I should use this lane for making a left turn. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line [IN-6(4)]
Step 6  change_right    prohibited (contested, correct): prohibited by the curb/fence boundary
Step 6  go_straight     prohibited (correct): prohibited by the left-turn arrow [IN-8(1)(c)]
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the left-turn arrow [IN-8(1)(c)]
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane specifically to perform a left turn at the upcoming intersection. Do not
                        attempt to change lanes or go straight from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:right']), actions False, unsafe ['turn_left'], citation
                        unlisted, contradictions []
Tokens                  in 5803, out 845, 60.06 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops and trees on both sides. The road ahead appears to
                        be a straight continuation of the current street. (lanes 3, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area or sidewalk on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The text 'BUS LANE' is painted in my lane on the left side.
Step 4  Cross-check     position: The lane count of 3 and my position as the rightmost lane (3) are consistent
                        with the white line on my left and the edge line on my right. | roles: The white solid
                        line on the left acts as a lane divider, and the white solid line on the right acts as
                        an edge line, which is consistent with the layout. | markings: The 'BUS LANE' text is
                        clearly within my lane, identifying it as a special lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not park on the kerb side where a solid line is
                        painted. [[IN-22.(2)(j)]]
Step 5  Rule            text:bus: No vehicle of any other class shall be driven in this lane as it is marked
                        for a special purpose (bus lane). [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     prohibited (contested, label allowed): prohibited
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  My lane is a designated bus lane, which prohibits my car from entering or using it. I
                        should move into a standard traffic lane to proceed straight.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        ['go_straight decided without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 851, 55.17 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No arrows, words, or symbols are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        having a lane line on both my left and right. | roles: The white solid lines correctly
                        function as lane lines between lanes of the same direction. | markings: No markings
                        are present to contradict the boundaries. | unseen: No attributes were reported that
                        were not visible. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane as the solid white lines on both sides prohibit
                        lane changes. You are permitted to proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 785, 54.51 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): The word 'BUS' is painted in the lane to my left.; line:stop_yield
                        (partial): There is a white dashed line across the lane ahead, possibly a pedestrian
                        crossing or stop line.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both the left and right. | roles: The white dashed lines correctly
                        function as lane lines between lanes of the same direction. | markings: The 'BUS' text
                        is in the adjacent lane, not my lane. The dashed line ahead is consistent with a
                        crossing or stop line. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver may cross the broken line to overtake but must return to
                        the lane. [[IN-6(7)]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left boundary [IN-6(7)]
Step 6  change_right    allowed (correct): allowed by the dashed right boundary [IN-6(7)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the
                        boundaries are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_yield', 'text:bus'], missed []), actions True, unsafe [], citation
                        unlisted, contradictions ['go_straight allowed without the stop that the STOP or 停
                        marking in my lane requires']
Tokens                  in 5803, out 838, 55.17 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area or sidewalk on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (insufficient): No arrows, words, or symbols are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a lane
                        line on my left and an edge line on my right. | roles: The white solid lines correctly
                        define the boundaries for a middle lane and a right-side edge. | markings: No markings
                        were observed in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white line to the left is prohibited. [[IN-6(4)]]
Step 5  Rule            right_boundary: Driving over the solid line or onto the curb/parking area is
                        prohibited. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line and curb on the
                        right [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 5803, out 778, 53.72 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): A white circle with the number 20 inside is painted in the
                        center of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lines on both sides. | roles: The white solid lines correctly function as lane
                        lines between lanes of the same direction. | markings: The speed limit marking is
                        centered in my lane and does not conflict with the boundaries. | unseen: None |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            text:speed_limit: No specific rule provided for the 20 speed limit marking other than
                        general compliance.
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right due to the solid white lines. Observe the 20
                        mph speed limit indicated on the road.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 686, 6.8 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops on both sides. The road ahead appears to be a
                        continuous stretch of road with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): A white zigzag line is painted on the road surface in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        having a lane line on both my left and right. | roles: The white solid lines correctly
                        function as lane lines between lanes of the same direction. | markings: The zigzag
                        lines are a common urban marking and do not contradict the lane boundaries. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            symbol:other: No specific rule provided for zigzag markings in the provided text.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay within your current lane as the solid white lines on both sides
                        prohibit lane changes. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 788, 8.62 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees and buildings on the right. The road ahead appears
                        to be a continuous stretch of road with parked cars on the right. (lanes 2, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which is occupied by a
                        red bus.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of my lane, with a curb and sidewalk beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the center
                        of my lane.
Step 4  Cross-check     position: The lane count (2) and my position (2) are consistent with the boundaries: a
                        white line on my left separates me from another lane, and a white line on my right
                        marks the edge. | roles: The white solid lines correctly function as a lane line and
                        an edge line. | markings: The straight arrow is consistent with the lane's purpose and
                        the surrounding boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight-ahead
                        movement.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line on the right
                        [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 850, 8.21 s
```
