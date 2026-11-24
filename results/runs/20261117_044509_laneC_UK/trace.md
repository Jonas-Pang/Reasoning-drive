# Reasoning of lane run 20261117_044509_laneC_UK

```text
lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops and trees on both sides. The road ahead appears
                        to be a continuous stretch of road with a central area. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the center of the
                        road, but it is not within my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to move onto the
                        sidewalk or adjacent area. [[IN-6(4)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line and curb on the
                        right [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          prohibited: prohibited by the solid white line [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 5796, out 608, 6.26 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a lane
                        line on my left and an edge line on my right. | roles: The white solid lines correctly
                        function as a lane divider and an edge line. | markings: No markings were observed in
                        the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing to the left to overtake or
                        change lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The solid line and proximity to the curb prohibit driving over the
                        line or onto the sidewalk. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5796, out 628, 11.05 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings on both sides and a bus stop on the left. The road ahead
                        appears to be a continuous lane with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line marks the edge of the road next to a sidewalk and bus stop.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A row of parked cars defines the right side of the lane, with no visible painted line.
                        none none, curb no, other, evidence full
Step 3  Markings        line:stop_line (insufficient): none; line:yield_line (insufficient): none;
                        line:stop_yield (insufficient): none; arrow:merge_left (insufficient): none;
                        arrow:merge_right (insufficient): none; arrow:two_way_left (insufficient): none;
                        text:only (insufficient): none; text:bus (insufficient): none; text:hov
                        (insufficient): none; text:stop (insufficient): none; text:keep_clear (insufficient):
                        none; text:speed_limit (insufficient): none; text:other (insufficient): none;
                        symbol:hov_diamond (insufficient): none; symbol:bike (insufficient): none;
                        symbol:other (insufficient): none; area:left_turn_waiting (insufficient): none;
                        area:two_way_left_turn_lane (insufficient): none; area:grid (insufficient): none;
                        area:channelizing (insufficient): none; line:stop_line (insufficient): none;
                        line:yield_line (insufficient): none; line:stop_yield (insufficient): none;
                        line:crosswalk (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The driver is prohibited from parking on the yellow line on the kerb
                        side. [IN-22.(2)(j)]
Step 5  Rule            right_boundary: no marking governs this action
Step 6  change_left     not_applicable (contested, label not_determined): no marking governs this action
Step 6  change_right    not_applicable (WRONG, label not_determined): no marking governs this action
Step 6  go_straight     allowed (contested, label not_determined): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Proceed straight ahead in your current lane. Do not park on the yellow line to your
                        left.
Score                   lane False, boundaries {'left': True, 'right': None}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'symbol:bike', 'symbol:hov_diamond', 'symbol:other', 'text:bus',
                        'text:hov', 'text:keep_clear', 'text:only', 'text:other', 'text:speed_limit',
                        'text:stop'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 5796, out 1061, 7.91 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings on both sides. A bus is approaching in the distance, and
                        there is a pedestrian crossing ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from the sidewalk/pedestrian area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): A yellow box with a white cross is painted in the middle of the road
                        ahead.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) are consistent with
                        the left edge line and the right lane line. | roles: The white solid lines correctly
                        function as an edge line on the left and a lane line on the right. | markings: The
                        yellow box is a standard grid marking for a junction/crossing area. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a white solid edge line, but it defines
                        the boundary of the roadway.
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the adjacent lane to the
                        right. [[IN-6(4)]]
Step 5  Rule            area:grid: The vehicle shall not be stopped on the yellow box marked on the road.
                        [[IN-22.(1)viii]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid edge line and curb
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid lane line [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead. Do not cross the solid white line to your right to
                        change lanes, and do not stop on the yellow box ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5796, out 669, 11.36 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. A red bus is ahead in the
                        distance. (lanes 3, mine 2, full)
Step 2  Left            A white solid line separates my lane from a lane to the left, which contains a bicycle
                        symbol.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from a lane to the right where cars are parked.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol is painted in the lane to my left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly act as lane
                        dividers. | markings: The bicycle symbol is in the lane to the left, not in my lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white line to the left is prohibited. [[IN-6(4)]]
Step 5  Rule            right_boundary: Crossing the solid white line to the right is prohibited. [[IN-6(4)]]
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
Advice                  You are in the middle lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5796, out 618, 6.27 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A broken white line is visible in the lane to my left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) is consistent with a
                        lane line on my left and an edge line/curb on my right. | roles: The white solid lines
                        are consistent with lane markings in a UK urban setting. | markings: No markings are
                        clearly visible within my specific lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as the solid white lines on both sides prohibit lane
                        changes. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 5796, out 745, 6.93 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian crossing and a bus stop ahead. The car is
                        positioned in one of the lanes heading forward. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my left,
                        but no specific arrows or words are in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle lane) is consistent with a
                        lane line on my left and an edge line on my right. | roles: The white dashed line on
                        the left and solid line on the right are consistent with lane-to-lane and lane-to-edge
                        roles. | markings: No markings were observed in my lane to contradict the boundaries.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid line to overtake another vehicle.
                        [[IN-6(4)]]
Step 6  change_left     allowed (correct): Allowed by the dashed line on the left [IN-6(7)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid line on the right
                        [IN-6(4)].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow is present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn marking is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if necessary, but you must remain in your current
                        lane relative to the right boundary. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5796, out 849, 7.26 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A residential street or courtyard area with a wide paved surface. Ahead, there is a
                        junction or open area with several parked cars and a building. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from a pedestrian area/sidewalk on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as 1 (leftmost) is consistent with the
                        left edge line and the right lane line. | roles: The white solid lines correctly
                        function as an edge line and a lane line. | markings: The straight arrow is consistent
                        with the lane's purpose. | unseen: None | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a white solid edge line, but it defines
                        the boundary of the drivable area. [null]
Step 5  Rule            right_boundary: The driver shall not drive on or over the solid white line separating
                        the lanes. [IN-6(6)]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight movement.
                        [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line and curb
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane and proceed straight ahead. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5796, out 651, 6.37 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops on both sides. The road ahead appears to be a
                        continuous stretch of road with no immediate intersection visible. (lanes 3, mine 2,
                        full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk and trees.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a lane
                        line on my left and an edge line on my right. | roles: The white solid lines correctly
                        function as a lane line and an edge line. | markings: The straight arrow is consistent
                        with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white line to the left is prohibited. [[IN-6(4)]]
Step 5  Rule            right_boundary: Crossing the solid white line to the right is prohibited. [[IN-6(4)]]
Step 5  Rule            arrow:straight: The arrow indicates that this lane is intended for going straight
                        ahead. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [IN-8(1)(c)]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5796, out 675, 11.26 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with trees and buildings on both sides. The road ahead is straight with
                        parked cars on the right and a sidewalk on the left. (lanes 2, mine 1, full)
Step 2  Left            A white solid line separates my lane from the sidewalk/curb on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in the center of my
                        lane.; arrow:straight (full): A white arrow pointing straight ahead is in the lane to
                        my right.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) are consistent with
                        a white solid line on the left (edge) and a dashed line on the right (lane line). |
                        roles: The white solid line on the left correctly acts as an edge line, and the dashed
                        line on the right correctly acts as a lane line. | markings: The straight arrow in my
                        lane is consistent with the straight road ahead and the dashed lane line on the right.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a white solid edge line, but it defines
                        the boundary of the roadway.
Step 5  Rule            right_boundary: The driver may cross the broken line in order to overtake, but shall
                        return to his lane after completing the manoeuvre. [[IN-6(7)]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for straight movement.
Step 6  change_left     prohibited (contested, correct): no marking governs this action
Step 6  change_right    allowed (correct): allowed by the dashed line per [IN-6(7)]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may proceed straight ahead. You are permitted to change
                        into the right lane if necessary, as the boundary is a dashed line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['text:other']), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 5796, out 724, 6.87 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a cycle lane on the left and a main carriageway. The road
                        ahead appears to be a straight stretch with some buildings and parked cars. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from a cycle lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to its right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly define
                        the boundaries of my lane. | markings: The straight arrow is consistent with the
                        straight road ahead. | unseen: None | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white line to the left is prohibited. [[IN-6(4)]]
Step 5  Rule            right_boundary: Crossing the solid white line to the right is prohibited. [[IN-6(4)]]
Step 5  Rule            arrow:straight: The arrow indicates that this lane is intended for straight movement.
                        [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line on the left
                        [IN-6(4)]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white line on the
                        right [IN-6(4)]
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
Tokens                  in 5796, out 661, 6.66 s
```
