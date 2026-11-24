# Reasoning of lane run 20261117_123758_laneA_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with a bus and a pedestrian crossing ahead. My car is in a
                        lane heading towards an intersection. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is a bus lane.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line separates the lane to my right
                        from the one further right.
Step 4  Cross-check     position: The lane count and my position (2nd from left) are consistent with the white
                        dashed line on my left and the solid line on my right. | roles: The white dashed line
                        on the left correctly identifies a lane-change possibility, and the solid line on the
                        right correctly identifies a boundary with a special lane (bus lane). | markings: No
                        specific arrows or words are in my lane, but the lane to my right is clearly a bus
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows me to change into the lane to my left.
Step 5  Rule            right_boundary: The solid line prohibits me from changing into the bus lane on my
                        right.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or change into the lane on your left. Do not move into the
                        bus lane on your right as it is prohibited by the solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed ['line:stop_line', 'symbol:bike']), actions True, unsafe
                        [], citation None, contradictions ['go_straight allowed without the stop that the STOP
                        or 停 marking in my lane requires']
Tokens                  in 2956, out 791, 7.17 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with a pedestrian crossing and a junction ahead. My
                        car is in the lane closest to the center of the road. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right, which is next to a
                        curb.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white dashed line and a white arrow pointing straight ahead
                        are visible in the lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows me to change into the lane to my left.
Step 5  Rule            right_boundary: The dashed line allows me to move toward the right edge of the road.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    allowed (contested, label prohibited): allowed by the dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight ahead. You may change lanes to
                        the left or right as the boundaries are dashed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        None, contradictions ['change_right allowed across a curb']
Tokens                  in 2956, out 755, 4.91 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with a multi-lane layout. Ahead is a junction with a
                        pedestrian crossing and a bus stop. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which has a bicycle
                        symbol.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.;
                        symbol:bike (full): A white bicycle symbol is in the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        dashed line on my left and a solid line on my right. | roles: The white dashed line on
                        the left and solid line on the right are standard for lane separation in this context.
                        | markings: The straight arrow in my lane is consistent with the lane's purpose. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for going straight
                        ahead.
Step 6  change_left     allowed (correct): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left if necessary, but you must not move into the bicycle lane to your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 843, 7.67 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street in the UK with buildings on both sides. The road ahead is
                        straight. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 689, 6.07 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with an intersection ahead. My car is in a lane approaching a
                        pedestrian crossing and a junction. (lanes 2, mine 1, full)
Step 2  Left            A white solid line separates my lane from the sidewalk on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): White lines forming a box-like shape or hatching at the junction.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The edge line prohibits moving to the left onto the sidewalk.
Step 5  Rule            right_boundary: The dashed lane line allows changing into the lane on the right.
Step 5  Rule            area:grid: The grid area indicates a keep clear zone or junction box.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (contested, label prohibited): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or change into the right lane. Do not move to the left as it
                        is bounded by a curb and solid line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:crosswalk']), actions None, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 716, 5.99 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with houses on the left and a sidewalk on the right.
                        The road ahead appears to be a continuous stretch of lanes. (lanes 3, mine 2, full)
Step 2  Left            A double red line on the road surface, with a curb and sidewalk to its left.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line to the right of my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries. The
                        double red line on the left indicates the edge of the roadway, and the dashed line on
                        the right separates my lane from the one to its right. | roles: The double red line
                        correctly serves as an edge line, and the white dashed line correctly serves as a lane
                        line. | markings: No specific arrows or words are visible in my lane to contradict the
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double red line prohibits stopping or parking on the edge of the
                        roadway.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes to the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change into the right lane.
                        Changing to the left is prohibited by the double red line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2956, out 767, 6.1 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with buildings on the right and a sidewalk/fence on
                        the left. The road continues straight ahead. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly identify the boundaries
                        between lanes of the same direction. | markings: The straight arrow is consistent with
                        the lane's purpose and the surrounding boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 785, 7.2 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street in the UK with shops on the right and a sidewalk on the
                        left. The road ahead continues straight with several lanes of traffic. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from a lane to my left, which appears to be a
                        cycle lane or a dedicated lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane to my right where cars are parked.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line separates the lanes to my left.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries. I am
                        in the middle lane of three lanes of traffic moving in my direction. | roles: The
                        white solid lines correctly define the boundaries of my lane as a lane-line between
                        other lanes of the same direction. | markings: No specific arrows or words are visible
                        in my lane to contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to my left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to my right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a middle lane. You may proceed straight ahead, but you are prohibited from
                        changing lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2956, out 784, 7.44 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian crossing ahead. My car is in a lane
                        approaching a junction or crossing. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        parking or stopping area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (full): A white line marking the start of a pedestrian crossing area.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles; I am in
                        the middle lane of three. | roles: The white solid lines correctly identify the
                        boundaries between lanes. | markings: The stop-yield line is consistent with the
                        pedestrian crossing ahead. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the area to the right.
Step 5  Rule            line:stop_yield: The marking requires a full stop before proceeding through the
                        crossing.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     stop_first (contested, label allowed): stop_first
Step 6  turn_left       stop_first: stop_first
Step 6  turn_right      stop_first: stop_first
Step 6  u_turn          stop_first: stop_first
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the marked line before proceeding through the
                        pedestrian crossing. Lane changes to the left or right are prohibited by the solid
                        white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        None, contradictions ['turn_left, turn_right, u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 2956, out 779, 7.3 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with a pedestrian crossing and a cycle lane on the
                        left. Ahead is a continuation of the road with a white van and a car in the adjacent
                        lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol is painted in the lane to my left.;
                        symbol:bike (full): A white bicycle symbol is painted in the lane to my left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly function
                        as lane lines between lanes of the same direction. | markings: The bicycle symbols are
                        in the leftmost lane, which is consistent with a dedicated cycle lane. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines. Be aware of the cycle lane to
                        your left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:bike'], missed ['text:speed_limit']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 2956, out 818, 7.23 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street in the UK with shops on the left and a park area on the
                        right. The road ahead appears to be a continuous stretch with a junction or turn-off
                        further ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which is next to a
                        sidewalk.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with having
                        a lane line on both my left and right. | roles: The white solid lines correctly
                        function as lane lines between lanes of the same direction. | markings: The straight
                        arrow in my lane is consistent with the lane's purpose and the surrounding boundaries.
                        | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation None, contradictions []
Tokens                  in 2956, out 801, 24.71 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with a sidewalk and buildings on the left and a
                        sidewalk and a tower on the right. The road ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is an edge lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my left,
                        but my lane has no arrows or text.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows me to change into the lane to my left.
Step 5  Rule            right_boundary: The solid line prohibits me from moving into the area to my right.
Step 6  change_left     allowed (correct): left_boundary is dashed, which allows a lane change.
Step 6  change_right    prohibited (WRONG, label allowed): right_boundary is solid, which prohibits a lane
                        change.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You can continue straight or change into the left lane. Do not attempt to move into
                        the lane on your right as it is restricted by a solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 735, 5.3 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with an intersection ahead. My car is in the middle
                        lane of three lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:left (full): A white arrow pointing left is painted in the lane to my left.;
                        arrow:right (full): A white arrow pointing right is painted in the lane to my right.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight ahead is the intended movement
                        for this lane.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed ['arrow:straight_left']),
                        actions False, unsafe [], citation None, contradictions ['turn_left not_applicable
                        although an arrow shows it', 'turn_right not_applicable although an arrow shows it']
Tokens                  in 2956, out 812, 7.31 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with a multi-lane road ahead. My car is in a lane that appears
                        to be the leftmost lane of the main roadway, adjacent to a sidewalk and a building.
                        (lanes 3, mine 1, full)
Step 2  Left            A white solid line separates my lane from the sidewalk and building on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:left_turn_waiting (full): A white dashed line curves to the left ahead,
                        indicating a turn lane or area.
Step 4  Cross-check     position: The lane count and my lane position agree; I am in the leftmost lane as
                        indicated by the edge line on my left and a lane line on my right. | roles: The white
                        solid edge line on the left and white dashed lane line on the right fit the roles of
                        an edge line and a lane-change line respectively. | markings: The left-turn waiting
                        area markings are consistent with the lane's position and the road layout. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid edge line prohibits moving further to the left onto the
                        sidewalk.
Step 5  Rule            right_boundary: The dashed lane line allows for a lane change to the right.
Step 5  Rule            area:left_turn_waiting: The area allows for waiting to perform a left turn.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid edge line and curb on the
                        left
Step 6  change_right    allowed (contested, label prohibited): allowed by the dashed lane line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       allowed: allowed by the left-turn waiting area markings
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areaallowed: allowed by the left-turn waiting area markings
Step 7  Reflect         consistent
Advice                  You can proceed straight or enter the left-turn waiting area to turn left. A lane
                        change to the right is permitted, but moving left is prohibited by the edge of the
                        road.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting'], missed ['line:crosswalk']), actions None, unsafe [],
                        citation None, contradictions ['turn_left decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 2956, out 862, 7.93 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with a multi-lane roadway ahead. My car is in a lane that
                        appears to be a straight-ahead lane. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A red line is painted on the ground next to a curb on my right.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows me to change lanes to the left.
Step 5  Rule            right_boundary: The red line and curb prohibit me from moving to the right onto the
                        sidewalk.
Step 5  Rule            arrow:straight: The arrow indicates that my lane is designated for going straight
                        ahead.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the red line and curb on the right
Step 6  go_straight     allowed (correct): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left if necessary, but do not move to the right as there is a red line and curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation None, contradictions []
Tokens                  in 2956, out 755, 5.57 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with an intersection ahead. My car is in a lane approaching a
                        pedestrian crossing and a junction. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight ahead and slightly to the
                        left.; line:stop_line (full): A white line across the lane before the intersection.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right.
Step 5  Rule            arrow:straight_left: The arrow allows going straight or turning slightly left.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to come to a complete stop before
                        the intersection.
Step 6  change_left     prohibited (contested, correct): prohibited by solid white left_boundary
Step 6  change_right    prohibited (contested, correct): prohibited by solid white right_boundary
Step 6  go_straight     stop_first (contested, label allowed): allowed by arrow:straight_left
Step 6  turn_left       stop_first: allowed by arrow:straight_left
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are permitted to go straight or turn slightly left, but you must come to a
                        complete stop at the white line before proceeding. Do not attempt to change lanes as
                        both boundaries are solid.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_left', 'line:stop_line'], missed ['line:crosswalk']), actions None,
                        unsafe [], citation None, contradictions ['leftmost lane, but a lane line on the
                        left']
Tokens                  in 2956, out 843, 7.52 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with a dedicated bus lane on the left. My car is in
                        the lane to the right of the bus lane. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A red-painted line and a white line form the edge of the roadway on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The words 'BUS LANE' are painted in the lane to my left.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the bus lane on the left.
Step 5  Rule            right_boundary: The edge line and curb prohibit moving off the roadway to the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Do not attempt to move into the bus lane on
                        your left, as it is restricted and separated by a solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 695, 5.71 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with a bus lane on the left and a car lane ahead.
                        The car is in the lane to the right of the bus lane. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        parking or restricted area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible further ahead in the
                        lane to the right.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the bus lane on the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane on the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left (into the bus lane)
                        or to the right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed ['text:speed_limit']), actions False, unsafe [], citation
                        None, contradictions ['rightmost lane, but a lane line on the right', 'go_straight
                        allowed without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 2956, out 705, 5.82 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with a pedestrian crossing and a junction ahead. My
                        car is in the middle lane of a three-lane roadway. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight ahead is the intended movement
                        for this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 722, 5.91 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with an intersection ahead. My car is in the middle
                        lane of a three-lane roadway. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:left (full): A white arrow pointing left is in the lane to my left.; arrow:right
                        (full): A white arrow pointing right is in the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the presence of
                        lane lines on both sides. | roles: The white dashed lines correctly function as lane
                        lines between lanes of the same direction. | markings: The straight arrow in my lane
                        is consistent with the dashed lane lines and the layout of the intersection. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows me to change into the left lane.
Step 5  Rule            right_boundary: The dashed line allows me to change into the right lane.
Step 5  Rule            arrow:straight: The arrow indicates that my lane is intended for going straight ahead.
Step 6  change_left     allowed (correct): allowed by the dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited (correct): prohibited by the arrow:straight marking (no left arrow in my
                        lane)
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking (no right arrow in my
                        lane)
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking (no u-turn arrow in my
                        lane)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  My lane is designated for going straight ahead. You may change lanes to the left or
                        right if necessary, as the boundaries are dashed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right'], missed ['line:stop_line']), actions True, unsafe [],
                        citation None, contradictions ['turn_left prohibited although an arrow shows it',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 2956, out 907, 8.29 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings and trees on both sides. The road ahead
                        appears to continue straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is next to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries. I am
                        in the middle lane of three lanes of traffic moving in the same direction. | roles:
                        The white dashed line on the left correctly identifies a lane-change possibility, and
                        the white solid line on the right correctly identifies the edge of the roadway. |
                        markings: No markings are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows me to change into the lane to my left.
Step 5  Rule            right_boundary: The solid line and curb prohibit me from moving into the area to my
                        right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed lane line on the left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid edge line and curb on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or move into the lane to your left. Do
                        not attempt to move to the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 771, 7.1 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with a bus stop and a pedestrian crossing on the
                        left. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead or change into the left lane. Do not attempt to change
                        into the right lane as it is prohibited by the solid line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 679, 5.21 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with a multi-lane layout. Ahead, there is a junction or a wide
                        crossing area with white markings. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which contains a
                        parked van.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): White lines forming a box or hatching area ahead of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a lane
                        line on my left and a lane line on my right. | roles: The white dashed line on the
                        left and solid line on the right are consistent with standard UK lane markings. |
                        markings: The grid area ahead is consistent with a junction or pedestrian crossing
                        area. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows me to change into the lane on my left.
Step 5  Rule            right_boundary: The solid line prohibits me from changing into the lane on my right.
Step 5  Rule            area:grid: The grid area indicates a zone where vehicles should not stop or park.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead or change into the left lane. Do not attempt to move
                        into the lane on your right as it is separated by a solid line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 809, 5.92 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with a multi-lane layout. The road ahead appears to be a
                        straight continuation or a junction with a pedestrian crossing. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which has a left-turn
                        arrow.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the presence of lane
                        lines on both sides. | roles: The white solid lines correctly function as lane lines
                        between lanes of the same direction. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose and the surrounding boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for going straight
                        ahead.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 776, 7.33 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with buildings on both sides. The road ahead appears
                        to continue straight with a slight curve. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the leftmost
                        lane of the direction.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible on the road surface
                        ahead, but it appears to be a lane divider rather than a marking within my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly function as lane dividers in a
                        UK context. | markings: No specific arrows or words are visible in my lane to
                        contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 761, 7.52 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street in the UK with a pedestrianized area or sidewalk to the
                        right. The road ahead continues straight. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        curb and a metal fence.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving to the right.
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
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left if necessary, but you must not move to the right as it is bounded by a solid line
                        and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 753, 6.37 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with buildings on both sides. The road ahead appears
                        to continue straight with no immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is a bus lane.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        area:grid (full): Red-painted area on the left side of the road, outside the leftmost
                        lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        a white dashed line on my left and a white solid line on my right. | roles: The white
                        dashed line on the left correctly identifies a lane-change possibility, and the white
                        solid line on the right correctly identifies a boundary with a special lane (bus
                        lane). | markings: The red area is outside my lane and does not conflict with my
                        lane's markings. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed line allows me to change into the lane to my left.
Step 5  Rule            right_boundary: The solid line prohibits me from changing into the bus lane on my
                        right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the lane on your left. Do not move into the
                        bus lane on your right as it is prohibited by the solid line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 795, 24.82 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK. My car is in a lane next to a bus lane, heading
                        towards a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A dashed white line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (full): A bus lane area is marked to the left of my lane
                        with 'BUS LANE' text and a solid white line.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        lane line on my left (separating me from the bus lane) and a dashed line on my right.
                        | roles: The solid white line on the left correctly identifies a lane boundary, and
                        the dashed line on the right correctly identifies a lane-change boundary. | markings:
                        The bus lane markings are to the left of my lane, which is consistent with the lane
                        boundary. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the bus lane on the left.
Step 5  Rule            right_boundary: The dashed white line allows changing into the lane on the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can continue straight or move into the lane on your right. Do not move into the
                        bus lane on your left as it is prohibited by the solid white line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 785, 6.87 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A residential street in the UK with a wide roadway and a sidewalk on both sides. The
                        road ahead appears to be a continuous street with parked cars on the left. (lanes 2,
                        mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left, which has parked cars.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the sidewalk on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): A white zigzag line is painted in the center of the road,
                        separating the two lanes.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. I am in
                        the right-hand lane of a two-lane road (driving on the left). | roles: The white solid
                        lines correctly identify the lane divider and the road edge. | markings: The zigzag
                        lines are common in the UK near pedestrian crossings or bus stops to indicate no
                        parking/stopping, which is consistent with the urban setting. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving onto the sidewalk.
Step 5  Rule            symbol:other: The zigzag markings indicate a restricted area where parking or stopping
                        is prohibited.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Do not attempt to change lanes or move onto
                        the sidewalk, as both boundaries are solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2956, out 806, 24.95 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with an intersection ahead. My car is in a lane
                        that appears to be a dedicated left-turn lane. (lanes 3, mine 1, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a raised curb separate my lane from the sidewalk/pedestrian
                        area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): A white arrow pointing left is painted in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid line and curb prohibit moving onto the sidewalk.
Step 5  Rule            arrow:left: The arrow indicates that this lane is for turning left.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by solid white line
Step 6  change_right    prohibited (contested, correct): prohibited by solid white line and curb
Step 6  go_straight     prohibited (correct): prohibited by left-turn arrow
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by left-turn arrow
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane specifically to perform a left turn at the upcoming intersection. Do not
                        attempt to go straight or change lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left'], missed ['arrow:right']), actions False, unsafe ['turn_left'], citation
                        None, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 2956, out 738, 6.04 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with a bus lane on the left and a parking area on the right. My car is
                        in the middle lane of a three-lane roadway. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the bus lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): The lane to my left is marked with 'BUS LANE' text and a solid white
                        line.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        lane line is on my left and an edge line is on my right. | roles: The white solid
                        lines correctly identify the lane boundary and the edge of the roadway. | markings:
                        The 'BUS LANE' text is in the lane to my left, which is consistent with the lane-line
                        boundary. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the bus lane on the left.
Step 5  Rule            right_boundary: The solid white line prohibits moving into the parking area on the
                        right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Do not attempt to change lanes to the left
                        into the bus lane or to the right into the parking area, as both boundaries are solid
                        lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 768, 6.93 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street in the UK with shops on both sides. The road ahead continues
                        straight. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (contested, correct): left_boundary is a solid line
Step 6  change_right    prohibited (WRONG, label allowed): right_boundary is a solid line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 685, 6.11 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a dedicated bus lane on the left. The road continues
                        straight ahead into a built-up area. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from a bus lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): The words 'BUS LANE' are painted in the lane to my left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the dashed lines on both sides. | roles: The white dashed lines correctly identify the
                        boundaries between lanes of the same direction. | markings: The 'BUS LANE' text is in
                        the lane to the left, which is consistent with the dashed line separating it from my
                        lane. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The dashed line allows me to change into the bus lane on the left.
Step 5  Rule            right_boundary: The dashed line allows me to change into the lane on the right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may go straight, change to the left lane (which is a
                        bus lane), or change to the right lane. Be mindful of the bus lane restrictions if you
                        move left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 773, 6.85 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with a multi-lane layout. My car is in a lane heading forward towards a
                        distant intersection or continuation of the road. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area or sidewalk on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right onto the
                        sidewalk or parking area.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and curb on
                        the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable as no left-turn arrow is present.
Step 6  turn_right      not_applicable: not_applicable as no right-turn arrow is present.
Step 6  u_turn          not_applicable: not_applicable as no u-turn arrow is present.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 2956, out 731, 6.41 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with a multi-lane layout. The road ahead appears to be a
                        straight continuation or a slight curve, with buildings on both sides. (lanes 3, mine
                        2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): A large '20' speed limit circle is painted in the center of
                        my lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the white lane lines
                        on both sides. | roles: The white solid lines correctly function as lane lines between
                        lanes of the same direction. | markings: The speed limit marking is centered in my
                        lane and does not conflict with the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            text:speed_limit: The marking indicates a maximum speed limit of 20 mph.
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as lane changes to the left or right are prohibited by the
                        solid white lines. Maintain a speed of 20 mph or less as indicated by the road
                        marking.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 791, 6.55 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street in the UK with a central hatched area. My car is in the lane
                        to the left of the central hatching. (lanes 3, mine 1, full)
Step 2  Left            A white solid line separates my lane from the sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white solid line separates my lane from a central hatched area.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white line marking the edge of the lane on the left.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The edge line prohibits moving further to the left onto the sidewalk.
Step 5  Rule            right_boundary: The solid lane line prohibits changing lanes to the right into the
                        hatched area.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2956, out 677, 6.27 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with trees lining the sidewalk. My car is in a lane
                        next to a red bus. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left where the bus is.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the roadway next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. A white
                        line on my left separates me from another lane of my direction, and a white line on my
                        right marks the edge of the road. | roles: The white solid lines correctly represent a
                        lane divider and an edge line in a UK context. | markings: The straight arrow in my
                        lane is consistent with the lane's purpose. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving onto the sidewalk to the
                        right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Do not attempt to change lanes to the
                        left or right as the solid lines prohibit it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 798, 7.8 s
```
