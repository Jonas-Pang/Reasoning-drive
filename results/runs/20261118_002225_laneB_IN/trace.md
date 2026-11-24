# Reasoning of lane run 20261118_002225_laneB_IN

```text
idd__primary_d1_leftCamImgs_0000529 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------
Step 1  Scene           A two-way urban road in India with buildings and trees on both sides; my car is
                        driving straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line on the left edge of the road. Photo 2 shows the same
                        white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right edge of the road. Photo 2 shows the same
                        white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The edge line marks the boundary of the roadway and does not prohibit
                        driving within the lane. [null]
Step 5  Rule            right_boundary: The edge line marks the boundary of the roadway and does not prohibit
                        driving within the lane. [null]
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    prohibited: prohibited by the solid white edge line [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along my lane
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes are prohibited by the solid edge
                        lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6654, out 750, 3.0 s

idd__primary_d1_leftCamImgs_0000786 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------
Step 1  Scene           A residential street in India with houses on both sides; the road continues straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road. Photo 2 shows the
                        same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line along the right edge of the road. Photo 2 shows the
                        same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid line. [IN-6(6)] "The
                        driver shall not drive on or over a single or double longitudinal solid line, or on a
                        painted traffic island except in case of obstructions on the road."
Step 5  Rule            right_boundary: The driver shall not drive on or over the solid line. [IN-6(6)] "The
                        driver shall not drive on or over a single or double longitudinal solid line, or on a
                        painted traffic island except in case of obstructions on the road."
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and rule [IN-6(6)]
Step 6  change_right    prohibited: prohibited by the solid white edge line and rule [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along my lane
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay within your lane and proceed straight; lane changes to either side are prohibited
                        by the solid edge lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6654, out 747, 2.9 s

idd__primary_d1_leftCamImgs_0002250 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------
Step 1  Scene           The car is on a city road in India, driving straight ahead on a road with buildings
                        and shops on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows no painted line on the left, only the edge of the road next to parked
                        vehicles and a sidewalk. Photo 2 also shows no painted line on the left.
                        none none, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a raised stone curb separating the road from a sidewalk. Photo 2 shows
                        the same raised stone curb immediately to the right of the car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: No specific rule prohibits driving within the lane boundaries. [null]
Step 5  Rule            right_boundary: The curb marks the edge of the roadway and prohibits driving over it.
                        [null]
Step 6  change_left     allowed: allowed: no marking prohibits leaving the lane to the left, provided it is
                        safe and follows general lane change rules [IN-6(1)].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a raised curb,
                        which is a physical barrier.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits continuing straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not drive over the curb on the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['change_left decided
                        with nothing marked on that side']
Tokens                  in 6654, out 752, 3.18 s

idd__primary_d1_leftCamImgs_0002357 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with buildings on both sides. There is a yellow
                        auto-rickshaw ahead in the same lane. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb separating the road from a sidewalk/parking area with
                        motorcycles. Photo 2 confirms the raised curb is immediately to the left of the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a raised curb separating the road from the opposite direction of
                        traffic. Photo 2 shows the same raised curb continuing along the right side of the
                        lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The raised curb marks the edge of the roadway and prohibits leaving the
                        road to the left. [null]
Step 5  Rule            right_boundary: The raised curb marks the edge of the roadway and prohibits leaving
                        the road to the right. [null]
Step 6  change_left     prohibited: prohibited by the raised curb (left_boundary).
Step 6  change_right    prohibited (contested, correct): prohibited by the raised curb (right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes are prohibited by the curbs on
                        both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 6654, out 759, 5.11 s
```
