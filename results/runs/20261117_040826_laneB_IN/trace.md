# Reasoning of lane run 20261117_040826_laneB_IN

```text
idd__primary_d1_leftCamImgs_0000529 | lane | Test B | gemma4:12b | from cache
-----------------------------------------------------------------------------
Step 1  Scene           A narrow urban street in India with buildings and trees on both sides. The road ahead
                        is straight with some parked vehicles and a motorcycle in the distance. (lanes 2, mine
                        1, full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which is bordered by a
                        curb and parked motorcycles.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bordered by a
                        curb and a sidewalk.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) is consistent with
                        the left boundary being a lane line and the right boundary being a lane line. | roles:
                        The white solid lines correctly define the boundaries of the lane. | markings: No
                        markings are present, which is consistent with the clear lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited: prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay within your lane as the solid white lines on both sides prohibit lane changes.
                        You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5785, out 762, 19.65 s

idd__primary_d1_leftCamImgs_0000786 | lane | Test B | gemma4:12b | from cache
-----------------------------------------------------------------------------
Step 1  Scene           A narrow residential street with houses on both sides. The road ahead appears to be a
                        continuous lane with some parked vehicles and motorcycles. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from the sidewalk/curb area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from the sidewalk/curb area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none; line:yield_line (insufficient): none;
                        line:stop_yield (insufficient): none; arrow:left (insufficient): none; arrow:right
                        (insufficient): none; text:stop (insufficient): none; text:keep_clear (insufficient):
                        none; area:left_turn_waiting (insufficient): none; area:two_way_left_turn_lane
                        (insufficient): none
Step 4  Cross-check     position: The lane count and position are consistent with the edge lines on both
                        sides. | roles: The white solid lines correctly function as edge lines for a single
                        lane. | markings: No markings were observed in the lane. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: No specific rule for a white edge line is provided, but it defines the
                        road boundary. [null]
Step 5  Rule            right_boundary: No specific rule for a white edge line is provided, but it defines the
                        road boundary. [null]
Step 6  change_left     allowed (WRONG, label prohibited): no marking governs this action
Step 6  change_right    allowed: no marking governs this action
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  The lane is a standard single lane. You may proceed straight ahead. No lane changes or
                        turns are specifically marked.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane', 'arrow:left', 'arrow:right',
                        'line:stop_line', 'line:stop_yield', 'line:yield_line', 'text:keep_clear',
                        'text:stop'], missed []), actions False, unsafe ['change_left'], citation unlisted,
                        contradictions ['change_left allowed across a curb', 'change_right allowed across a
                        curb', 'go_straight decided from an arrow that cannot be read', 'go_straight allowed
                        without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 5785, out 767, 21.15 s

idd__primary_d1_leftCamImgs_0002250 | lane | Test B | gemma4:12b | from cache
-----------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in India with buildings and trees on both sides. The road
                        ahead appears to be a straight continuation of the current street. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left, which contains a yellow
                        auto-rickshaw.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A raised concrete curb and a solid white line separate my lane from the lane to my
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        lane line is on my left and an edge line/curb is on my right. | roles: The white solid
                        line on the left correctly identifies a lane divider, and the curb/line on the right
                        identifies the edge of the roadway. | markings: No markings were observed in my lane.
                        | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake another
                        vehicle. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not park on the kerb side where a solid line is
                        painted. [[IN-22.(2)(j)]]
Step 6  change_left     prohibited: prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane and proceed straight. Lane changes to the left or
                        right are prohibited by the solid markings and the curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5785, out 779, 21.23 s

idd__primary_d1_leftCamImgs_0002357 | lane | Test B | gemma4:12b | from cache
-----------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in India with buildings and parked motorcycles on the left.
                        The road ahead continues straight with several vehicles visible. (lanes 2, mine 1,
                        full)
Step 2  Left            A raised concrete curb separates the lane from a sidewalk where motorcycles are
                        parked.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the adjacent lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible in the center of my
                        lane.
Step 4  Cross-check     position: The lane count of 2 and my position as 1 (leftmost) is consistent with the
                        left curb and the right lane line. | roles: The left curb acts as an edge line and the
                        right solid white line acts as a lane line. | markings: The dashed line in the center
                        of the lane is not a stop/yield line but a lane divider; however, no specific markings
                        govern movements. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a curb, but it defines the edge of the
                        roadway.
Step 5  Rule            right_boundary: The solid white line prohibits crossing to the right to overtake
                        another vehicle. [[IN-6(4)]]
Step 5  Rule            line:stop_yield: No specific rule provided for a dashed line in the center of a lane.
Step 6  change_left     not_applicable: no marking governs this action
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your lane. Do not attempt to change lanes to the
                        right as the solid white line prohibits it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 5785, out 663, 8.46 s
```
