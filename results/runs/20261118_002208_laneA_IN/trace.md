# Reasoning of lane run 20261118_002208_laneA_IN

```text
idd__primary_d1_leftCamImgs_0000529 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------
Step 1  Scene           A narrow residential street in India where traffic keeps to the left. The road is
                        straight ahead with parked motorcycles on the left side. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road. Photo 2 shows a solid
                        white line next to my car, continuing forward.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line along the right edge of the road. Photo 2 shows a solid
                        white line next to my car, continuing forward.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line marks the boundary of the roadway; crossing it
                        to leave the road is generally discouraged but not strictly prohibited unless it's a
                        curb.
Step 5  Rule            right_boundary: A solid white edge line marks the boundary of the roadway; crossing it
                        to leave the road is generally discouraged but not strictly prohibited unless it's a
                        curb.
Step 6  change_left     allowed (WRONG, label prohibited): the left_boundary is a solid edge line, allowing
                        leaving the roadway
Step 6  change_right    allowed: the right_boundary is a solid edge line, allowing leaving the roadway
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in the single lane and proceed straight. Be mindful of parked vehicles on the
                        left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 3807, out 740, 16.36 s

idd__primary_d1_leftCamImgs_0000786 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------
Step 1  Scene           A residential road in India where traffic keeps to the left. The road is a narrow two-
                        way street with houses on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left edge of the road. Photo 2 shows the same
                        solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 shows the same
                        solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line marks the boundary of the roadway; crossing it
                        is generally prohibited.
Step 5  Rule            right_boundary: A solid white edge line marks the boundary of the roadway; crossing it
                        is generally prohibited.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line on the left
Step 6  change_right    prohibited: prohibited by the solid white edge line on the right
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the white edge lines on either
                        side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3807, out 723, 2.6 s

idd__primary_d1_leftCamImgs_0002250 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------
Step 1  Scene           A city road in India where traffic keeps to the left. My car is in a single lane
                        moving forward on a road with a physical divider to the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows the edge of the roadway meeting a sidewalk/parking area with no painted
                        line. Photo 2 shows the same area next to my car with no painted line.
                        none none, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a raised concrete divider separating the directions of traffic. Photo 2
                        shows a raised stone/concrete curb immediately to the right of my lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The edge of the roadway allows driving but not leaving the road unless
                        for parking or turning.
Step 5  Rule            right_boundary: A raised curb prohibits crossing or changing lanes to the right.
Step 6  change_left     allowed: no marking governs this action
Step 6  change_right    prohibited (contested, correct): the right boundary is a raised curb which prohibits
                        crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      prohibited: the right boundary is a raised curb which prohibits crossing
Step 6  u_turn          prohibited: the right boundary is a raised curb which prohibits crossing
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not attempt to cross the raised curb on the
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions ['change_left decided with
                        nothing marked on that side', 'turn_right, u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 3807, out 716, 15.81 s

idd__primary_d1_leftCamImgs_0002357 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------
Step 1  Scene           A two-way urban road in India where traffic keeps to the left. My car is in the left
                        lane, facing forward with a rickshaw and parked motorcycles ahead. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a raised curb and a sidewalk with parked motorcycles. Photo 2 shows the
                        same raised curb immediately to the left of my car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a raised curb separating my lane from the opposite direction of traffic.
                        Photo 2 shows the same raised curb immediately to the right of my car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A raised curb prohibits leaving the roadway to the left.
Step 5  Rule            right_boundary: A raised curb prohibits crossing into the opposite traffic lane.
Step 6  change_left     prohibited: prohibited by the raised curb on the left boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the raised curb on the right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes are prohibited by the curbs on
                        both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3807, out 717, 2.86 s
```
