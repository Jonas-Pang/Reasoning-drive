# Reasoning of lane run 20261117_040824_laneA_IN

```text
idd__primary_d1_leftCamImgs_0000529 | lane | Test A | gemma4:12b | from cache
-----------------------------------------------------------------------------
Step 1  Scene           A narrow urban street with buildings and trees on both sides. The road ahead appears
                        to continue straight. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a dirt/paved shoulder
                        beyond.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as 2 (rightmost) is consistent with a
                        lane line on my left and an edge line on my right. | roles: The white solid lines
                        correctly identify a lane divider and a road edge. | markings: No markings were
                        observed in the lane. | unseen: No attributes were reported that were not visible. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line marks the edge of the roadway and prohibits
                        moving onto the shoulder.
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited: prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or onto the right
                        shoulder are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2938, out 732, 29.56 s

idd__primary_d1_leftCamImgs_0000786 | lane | Test A | gemma4:12b | from cache
-----------------------------------------------------------------------------
Step 1  Scene           A narrow residential street with trees and houses on both sides. My car is in a lane
                        facing forward towards a slight curve or continuation of the road. (lanes 2, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the road, next to a sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane on the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving onto the sidewalk or
                        shoulder on the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white lane_line on the left
Step 6  change_right    prohibited: prohibited by the solid white edge_line and curb on the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2938, out 705, 29.07 s

idd__primary_d1_leftCamImgs_0002250 | lane | Test A | gemma4:12b | from cache
-----------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in India with traffic moving on the left side. Ahead is a
                        continuous stretch of road with buildings and parked vehicles on both sides. (lanes 2,
                        mine 1, full)
Step 2  Left            A raised curb and a wall/fence separate my lane from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The curb prevents moving further to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 6  change_left     prohibited: prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the right are prohibited by
                        the solid white line, and the curb on your left marks the edge of the roadway.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2938, out 683, 28.25 s

idd__primary_d1_leftCamImgs_0002357 | lane | Test A | gemma4:12b | from cache
-----------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street in India where traffic drives on the left. Ahead is a
                        continuous stretch of road with buildings and parked motorcycles on the left. (lanes
                        2, mine 1, full)
Step 2  Left            A raised concrete curb separates my lane from a sidewalk and parked motorcycles.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:left_turn_waiting (insufficient): none; area:two_way_left_turn_lane
                        (insufficient): none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: consistent |
                        result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway and prohibits moving further
                        left.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 6  change_left     prohibited: prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the right are prohibited by
                        the solid white line, and the left side is bounded by a curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane'], missed []), actions None,
                        unsafe [], citation None, contradictions []
Tokens                  in 2938, out 717, 8.06 s
```
