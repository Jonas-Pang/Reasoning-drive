# Reasoning of lane run 20261118_002122_laneA_UK

```text
lingoqa__evaluation_images_val_a1109658670fb29d13ac113d322c004c_2 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------
Step 1  Scene           A city road in the UK with traffic keeping left; my car is in a lane that appears to
                        be a through lane approaching an intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line at the edge of the roadway. Photo 2 shows a white
                        solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed lane line allows changing lanes.
Step 5  Rule            right_boundary: A solid edge line prohibits leaving the roadway to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (correct): allowed by the dashed lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid edge line
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left, change to the left lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 3820, out 798, 4.82 s

lingoqa__evaluation_images_val_f6d832c4b3279c6491278500918e792e_2 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------
Step 1  Scene           Urban road in the UK with traffic keeping left; the road continues straight ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the left lane. Photo 2 shows
                        a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a red line at the edge of the road. Photo 2 shows a double red line next
                        to my car and a curb.
                        other double_solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show circular markings with '20' inside
                        them across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A double red line at the edge of the road prohibits parking and
                        changing lanes to the right.
Step 5  Rule            text:speed_limit: The speed limit is 20 mph; this does not govern the seven actions.
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a dashed lane line.
Step 6  change_right    prohibited (contested, label allowed): prohibited: the right boundary is a double red
                        edge line and a curb.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of a two-lane road. You may continue straight or change
                        to the left lane, but you cannot move right due to the red line and curb. Observe the
                        20 mph speed limit.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['area:channelizing']), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3820, out 852, 3.5 s

lingoqa__train_27ca312fb6ce3cb70036e317c6c758ba_2 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with shops on the left and parked vehicles on the right; the
                        road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the edge of the road next to the sidewalk.
                        Photo 2 shows the same solid yellow line continuing next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line between my car and the parked vehicles on the right.
                        Photo 2 shows no painted line next to my car on the right.
                        none none, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line indicates a parking restriction; it does not
                        prohibit driving in the lane but prohibits crossing into the sidewalk.
Step 5  Rule            right_boundary: The absence of a line allows for movement into the space on the right
                        if safe and permitted.
Step 6  change_left     prohibited (contested, correct): prohibited by the curb and edge line
Step 6  change_right    allowed: allowed as there is no marking prohibiting it
Step 6  go_straight     allowed (contested, correct): allowed as no marking governs this action
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the left boundary into the
                        sidewalk.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right', 'change_right decided with nothing marked on that side']
Tokens                  in 3820, out 730, 3.83 s

lingoqa__train_d21bf5635928983657b67b4aa8a13fac_0 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching an intersection with traffic
                        signals. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road next to a curb.
                        Photo 2 confirms two solid yellow lines along the curb next to the car.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a curb and a pedestrian island to the right. Photo 2 shows the road edge
                        meeting a raised curb of a pedestrian island.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines indicate parking is prohibited; as an edge line
                        with a curb, it prohibits leaving the roadway to the left.
Step 5  Rule            right_boundary: The curb prohibits leaving the roadway to the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the curb and double yellow edge line
Step 6  change_right    prohibited (contested, correct): prohibited by the curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight through the intersection as indicated by the
                        green light.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3820, out 711, 3.03 s

lingoqa__train_dde41275b6a47da6fe2992ae2f1b7673_1 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a signalized intersection
                        with a bicycle symbol and stop lines ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the edge of the road next to a sidewalk. Photo 2
                        confirms a solid red line next to the car, followed by a red line further ahead.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to the car, with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white bicycle symbol painted across the lane.;
                        line:stop_line (full): Photo 2 shows a solid white line across the lane at the stop
                        line of the intersection.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a red edge line on the left and a white lane line on the right
                        indicate the leftmost lane of a two-lane road. | roles: the red edge line and white
                        dashed lane line fit their roles. | markings: the bicycle symbol and stop line are
                        consistent with an urban road intersection. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The red edge line and curb prohibit leaving the roadway to the left.
Step 5  Rule            right_boundary: The broken white line allows changing lanes to the right.
Step 5  Rule            symbol:bike: The bicycle symbol indicates a cycle lane or priority area but does not
                        prohibit motor vehicles from going straight.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to stop when the signal is red.
Step 6  change_left     prohibited (contested, correct): prohibited by the red edge line and curb.
Step 6  change_right    allowed (correct): allowed by the broken white lane line.
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it and the lane does not
                        end.
Step 6  turn_left       not_applicable: not_applicable as there is no turn arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no turn arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no turn arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right if needed. Stop at the white line when the
                        traffic signal is red.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3820, out 998, 4.42 s

lingoqa__train_e0b3b51abefa2478a7a13edb958e8f33_1 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           Urban road in the UK with buildings on both sides; my car is in a single lane heading
                        straight. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the edge of the road next to a sidewalk. Photo
                        2 confirms a solid white line and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, only parked vehicles. Photo 2 shows the
                        road surface extending to the parked vans without any markings.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid edge line marks the boundary of the roadway; crossing it is
                        prohibited.
Step 5  Rule            right_boundary: No marking is present, but the edge of the drivable road is defined by
                        the parked vehicles.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid edge line and curb
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the presence of parked vehicles and
                        the road edge
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the left edge line into the
                        sidewalk.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 3820, out 722, 26.09 s

lingoqa__train_e12d585d1cf304230d7d39744f0797cd_0 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           A two-lane urban road in the UK where traffic keeps left. My car is in the rightmost
                        lane of the two lanes moving in my direction. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a series of short white dashes with gaps of similar length next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the curb/parking area. Photo
                        2 shows a series of short white dashes with gaps next to my car.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A broken white edge line allows crossing to the right, though a curb
                        is present.
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a broken white
                        lane line.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white edge line.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of a two-lane road. You may continue straight or change
                        lanes to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions ['change_right
                        allowed across a curb']
Tokens                  in 3820, out 762, 28.06 s

lingoqa__train_f2b37a8b7f23380de3834e8165fd2620_1 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK where traffic keeps left. My car is in a single
                        lane of travel, with parked cars on the left and a sidewalk on the right. (lanes 1,
                        mine 1, full)
Step 2  Left            Photo 1 shows a line of parked cars and a curb. Photo 2 shows a white dashed line
                        separating the travel lane from the parked cars, with a curb further left.
                        white dashed, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line and a sidewalk. Photo 2 shows a white solid line separating
                        the travel lane from a parking/bicycle area, with a curb further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 show the word 'SLOW' painted across the lane in
                        white.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed edge line allows crossing if safe to do so, but here it
                        separates the lane from parked cars.
Step 5  Rule            right_boundary: A solid edge line prohibits crossing into the area to the right.
Step 5  Rule            text:other: The 'SLOW' marking advises the driver to reduce speed.
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a dashed line.
Step 6  change_right    prohibited: prohibited: the right boundary is a solid line.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and follow the 'SLOW' marking to reduce speed. Do not cross the
                        solid white line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions ['change_left
                        allowed across a curb']
Tokens                  in 3820, out 844, 3.24 s
```
