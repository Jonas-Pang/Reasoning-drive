# Reasoning of lane run 20261117_215534_laneC_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with a
                        red bus ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the curb. Photo 2 shows a solid red line next to the
                        car and further ahead.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line. Photo 2 shows a white dashed line next to the car
                        with several long dashes and gaps, continuing further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a red edge line on the left and a white lane line on the right
                        indicate the leftmost lane of a multi-lane road. | roles: the red solid edge line and
                        white dashed lane line fit their roles. | markings: no markings in my lane to check. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The red solid line and curb mark the edge of the roadway; crossing it
                        is prohibited as it leads to the sidewalk. [null]
Step 5  Rule            right_boundary: The white dashed line allows lane changes after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the red solid edge line and curb (not
                        covered by provided rules, but defined as the roadway edge).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the white dashed lane line and
                        [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict it.
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe ['change_right'],
                        citation unlisted, contradictions []
Tokens                  in 6666, out 656, 12.37 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road in the UK, approaching a pedestrian crossing and a
                        junction. Traffic keeps to the left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a white broken line with several dashes and gaps next to the car.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line that becomes solid further ahead. Photo 2 shows a
                        white broken line with several dashes and gaps next to the car.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 and Photo 2 show a white transverse line across the
                        lane ahead of the car, preceding a pedestrian crossing.; line:crosswalk (full): Photo
                        1 and Photo 2 show a zebra crossing (white stripes) across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white edge line allows crossing to the left if safe and
                        permitted by other rules. [null]
Step 5  Rule            right_boundary: A broken white center line allows crossing to the right for overtaking
                        if safe. [null]
Step 5  Rule            line:stop_line: The driver shall stop before the stop line if the traffic signal is
                        red. [[IN-12(1)(a)]]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a broken line,
                        and no rule prohibits crossing it here.
Step 6  change_right    allowed (contested, label prohibited): allowed: the right boundary is a broken line,
                        and no rule prohibits crossing it for overtaking.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Proceed straight, but be prepared to stop at the stop line and give way to pedestrians
                        at the zebra crossing. Check the traffic signal ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 988, 9.96 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching an intersection with a bicycle lane
                        and a turning lane ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line next to the car, which continues ahead. Photo 2
                        confirms a white solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car, which ends as it meets a curb. Photo
                        2 shows a white solid line next to the car and a raised curb further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a lane line on the left and an edge line on the right indicate
                        the car is in the leftmost lane of a two-lane road. | roles: the white solid lines fit
                        the roles of lane line and edge line. | markings: the straight arrow is consistent
                        with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 5  Rule            arrow:straight: A straight arrow allows the vehicle to proceed straight ahead. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the white solid lane line [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line and curb
                        [IN-6(6)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow in the lane
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow in the lane
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow in the lane
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow in the lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight ahead. Lane changes are prohibited by the solid
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 6666, out 722, 13.23 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with buildings on the left and right. The road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid yellow lines along the left edge of the road. Photo 2 confirms
                        two solid yellow lines next to the car and continuing ahead.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the opposite traffic. Photo
                        2 shows a white dashed line next to the car with several long dashes and gaps.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: Lane changes are allowed across a broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a double solid
                        yellow line and a curb, and [IN-6(6)] prohibits driving over solid lines.
Step 6  change_right    allowed (correct): allowed: the right boundary is a dashed white line, which allows
                        crossing for overtaking per [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You can proceed straight or change lanes to the right to overtake. Do not cross the
                        double yellow lines on the left or park along the curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 804, 13.12 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a junction with a pedestrian
                        crossing ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, next to a sidewalk. Photo
                        2 shows this line is a single solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line along the right edge of the road. Photo 2 shows this line
                        is a single solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a zebra crossing (white stripes)
                        across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the edge lines on both sides | roles: the white solid lines on the edges fit the role
                        of edge lines | markings: the crosswalk is consistent with the road layout | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The edge line marks the boundary of the roadway; crossing it is
                        prohibited as it leads to a sidewalk. [null]
Step 5  Rule            right_boundary: The edge line marks the boundary of the roadway; crossing it is
                        prohibited as it leads to a sidewalk. [null]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line and curb
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight, ensuring you give way to any pedestrians on
                        the zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 709, 11.83 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, driving forward. The road ahead is
                        straight with no immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid red lines along the left edge of the road next to a curb.
                        Photo 2 confirms two solid red lines and a raised curb immediately to the left of my
                        car.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from a parking/stopping area on
                        the right. Photo 2 shows a white broken line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; the
                        left boundary is an edge line and the right is a lane line separating the driving lane
                        from a parking area. | roles: the red double solid lines on the left act as an
                        edge/parking restriction, and the white dashed line on the right acts as a lane
                        separator. | markings: no markings in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The red double lines are a UK-specific parking restriction and do not
                        govern driving movements within the lane, but the curb prohibits leaving the road.
                        [null]
Step 5  Rule            right_boundary: The broken white line allows changing lanes after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb and the red double
                        solid lines which mark the edge of the carriageway.
Step 6  change_right    allowed (correct): allowed by the broken white line according to [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or move to the right. Do not cross the red lines or the curb
                        on the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6666, out 696, 13.11 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the United Kingdom. The road
                        continues straight ahead with no immediate intersection or ramp visible. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the roadway from a blue-painted cycle
                        lane/shoulder. Photo 2 confirms a single solid white line next to the car, continuing
                        straight ahead.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of short white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a solid edge line on the left and a dashed lane line on the
                        right. | roles: The white solid line on the left fits the role of an edge line; the
                        white dashed line on the right fits the role of a lane line. | markings: No markings
                        were found in my lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid white line. [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across the broken line after giving a
                        proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right lane if needed. Do not cross the solid white
                        line on the left into the cycle lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 842, 13.32 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road continues
                        straight ahead with shops and parked cars on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the opposite direction of
                        traffic. Photo 2 shows the same white broken line next to my car, consisting of long
                        dashes and gaps.
                        white dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from another lane of the same
                        direction. Photo 2 shows this white broken line next to my car, consisting of long
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a center_line on the left and a lane_line on the right. |
                        roles: The white dashed pattern fits both the center_line and lane_line roles for a
                        multi-lane road. | markings: No markings were observed in my lane. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: A white dashed center line allows crossing for overtaking or turning,
                        provided it is safe. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed center line, which does not
                        prohibit crossing for overtaking or turning.
Step 6  change_right    allowed (correct): allowed: the right boundary is a dashed lane line, and rule
                        [IN-6(1)] allows lane changes with a signal.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right
                        after signaling.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 854, 13.56 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a pedestrian crossing
                        (zebra crossing). (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line that zig-zags as it approaches the crossing. Photo 2
                        shows the line next to the car is a white solid line.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line that zig-zags as it approaches the crossing. Photo 2
                        shows the line next to the car is a white solid line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show wide white stripes across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single solid longitudinal
                        line. [[IN-6(6)]]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at uncontrolled pedestrian
                        crossings. [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the white solid left boundary [IN-6(6)]
Step 6  change_right    prohibited (contested, correct): prohibited by the white solid right boundary
                        [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          prohibited: prohibited by the solid boundaries [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be prepared to stop and give way to the
                        pedestrian currently crossing the road.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['rightmost
                        lane, but a lane line on the right', 'u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 6666, out 855, 12.75 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road ahead
                        appears to be a straight stretch with a bicycle lane to the left. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from a bicycle lane. Photo 2
                        shows the same white dashed line next to my car, consisting of short dashes and gaps.
                        white dotted, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from another lane of traffic.
                        Photo 2 shows the same white dashed line next to my car, consisting of long dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a circular marking with the number
                        '20' painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and ego_lane_index agree
                        with the boundaries; a special lane line on the left and a lane line on the right
                        indicate my lane is the first of two general traffic lanes. | roles: The white dotted
                        line on the left fits the role of a special lane boundary (bicycle lane), and the
                        white dashed line on the right fits the role of a lane line. | markings: The speed
                        limit marking is consistent with an urban road environment. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A dotted white line separating a bicycle lane allows crossing for lane
                        changes if safe. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            text:speed_limit: This is an informative marking indicating the speed limit and does
                        not govern the seven actions. [null]
Step 6  change_left     allowed (contested, label prohibited): allowed: the dotted white boundary to the
                        bicycle lane allows crossing if safe.
Step 6  change_right    allowed (correct): allowed: the dashed white lane line allows lane changes per
                        [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  You are in the left lane of the main carriageway. You may proceed straight or change
                        lanes to the left or right if safe to do so; please observe the 20 mph speed limit
                        indicated on the road.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 1000, 15.88 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with a
                        left-turn lane ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a white broken line with long dashes and gaps next to the car.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line. Photo 2 shows a white broken line with long dashes
                        and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 and Photo 2 show a white arrow pointing straight and then
                        turning left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; there are lane lines on both sides, meaning my lane is the second
                        of at least two lanes. | roles: the white color and dashed/solid_dashed patterns fit
                        the role of lane lines. | markings: the left-turn arrow is consistent with the lane's
                        position and boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            arrow:left: The driver shall use this lane while taking a left turn. [[IN-8(1)(c)]]
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken line next to the
                        car, which [IN-6(7)] allows crossing for overtaking.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken line, which [IN-6(1)]
                        allows crossing after signaling.
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited: the lane arrow only shows a left turn,
                        prohibiting other movements.
Step 6  turn_left       allowed (correct): allowed: the lane arrow explicitly allows a left turn per
                        [IN-8(1)(c)].
Step 6  turn_right      prohibited (correct): prohibited: the lane arrow does not show a right turn.
Step 6  u_turn          allowed (WRONG, label prohibited): allowed: a left-turn arrow in a left-keep system
                        allows a U-turn unless prohibited by a sign.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You are in a left-turn lane. You should use this lane to turn left at the
                        intersection; going straight is prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:straight_left']), actions False, unsafe ['u_turn'],
                        citation unlisted, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 6666, out 963, 26.98 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road continues
                        straight ahead with no immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the curb, and further ahead it remains a
                        solid white line. Photo 2 shows a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right lane. Photo 2
                        shows a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a solid edge line on the left and a broken lane line on the right
                        indicate my lane is the leftmost of two lanes in my direction. | roles: the white
                        solid edge line and white dashed lane line fit their respective roles. | markings: no
                        markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid white line. [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across the broken line after giving a
                        proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane if
                        needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 659, 12.29 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction with a
                        pedestrian crossing and a cycle lane ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red solid line along the edge of the road next to the sidewalk. Photo
                        2 confirms two red solid lines running parallel to the curb.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white arrow pointing straight ahead with a smaller
                        branch pointing left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a red edge line on the left and a white lane line on the right
                        indicate the leftmost lane of a multi-lane road. | roles: the red solid edge line and
                        white dashed lane line fit their respective roles. | markings: the arrow allows both
                        straight and left movements, which is consistent with the lane's position. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The red solid line is a UK-specific no-stopping marking; it does not
                        prohibit driving within the lane. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            arrow:left: The driver shall use this lane while taking a left turn; it also allows
                        going straight as it is a combined arrow. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a curb and edge
                        line.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line [IN-6(1)].
Step 6  go_straight     allowed (correct): allowed: the arrow in the lane allows straight movement.
Step 6  turn_left       allowed (correct): allowed: the arrow in the lane allows left turns [IN-8(1)(c)].
Step 6  turn_right      prohibited (correct): prohibited: the arrow in the lane does not show a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: no arrow or marking governs
                        U-turns here.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may proceed straight or turn left. You may change to the
                        right lane if necessary.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:straight_left']), actions False, unsafe [], citation
                        unlisted, contradictions ['go_straight allowed although no arrow shows it']
Tokens                  in 6666, out 956, 14.35 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a narrow stretch with a cyclist ahead and
                        a pedestrian crossing further forward. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line along the left edge of the road, next to a sidewalk.
                        Photo 2 confirms a single white solid line immediately to the left of the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white zigzag line on the right side, separating the lane from a
                        parking/stopping area. Photo 2 shows the zigzag pattern clearly next to the car.
                        white zigzag, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a pedestrian crossing (zebra crossing)
                        ahead of the car.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: Zigzag lines indicate a no-stopping zone near a pedestrian crossing;
                        they do not prohibit lane changes but prohibit parking/stopping.
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white line
                        [IN-6(6)]
Step 6  change_right    allowed (contested, label prohibited): allowed: the zigzag line is an edge marking for
                        a no-stopping zone, not a lane boundary prohibiting movement
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be prepared to stop and give way to
                        pedestrians at the zebra crossing ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 881, 14.72 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection. (lanes
                        3, mine 1, full)
Step 2  Left            Photo 1 shows a curb and a solid line along the left edge of the road. Photo 2 shows a
                        raised curb and a solid red/pink line next to the car.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the next lane. Photo 2 shows
                        a white broken line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the left edge_line and right lane_line | roles: the solid edge line on the left
                        and dashed lane line on the right fit their roles | markings: the straight arrow is
                        consistent with the lane boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The curb and solid edge line prohibit leaving the roadway to the left.
                        [null]
Step 5  Rule            right_boundary: Lane changes to the right are allowed after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            arrow:straight: The straight arrow allows going straight and prohibits turning left or
                        right. [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the curb and solid edge line
Step 6  change_right    allowed (correct): allowed by the dashed lane line [IN-6(1)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited by the straight arrow
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions []
Tokens                  in 6666, out 674, 12.46 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a pedestrian crossing and a
                        junction. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line along the left edge of the road, separating the lane
                        from the sidewalk. Photo 2 shows the same white solid line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which then becomes a broken line
                        further ahead. Photo 2 shows a white solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a pedestrian crossing (zebra crossing)
                        consisting of white stripes across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the left is an edge line and the right is a lane line, suggesting a
                        single lane in this direction at this point. | roles: the white solid lines fit the
                        roles of edge and lane lines. | markings: the crosswalk is consistent with the urban
                        environment. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The edge line marks the boundary of the roadway; crossing it is
                        prohibited as it leads to the sidewalk. [null]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the left edge line and curb.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight, ensuring you give way to any pedestrians on
                        the zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['rightmost
                        lane, but a lane line on the right']
Tokens                  in 6666, out 732, 12.04 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, facing straight ahead with buses in
                        the adjacent lane and ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a single solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a red line along the edge of the road next to a curb. Photo 2 shows this
                        red line and the raised curb clearly.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my position (2)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white solid line fits the role of a lane line; the red line and curb fit
                        the role of an edge line. | markings: no markings in my lane to check. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The red edge line and curb prohibit leaving the roadway to the right.
                        [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the curb and edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white line to the left
                        or the curb to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 785, 12.6 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, where traffic keeps left. Ahead is a
                        clear stretch of road with a cyclist and other vehicles. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        confirms a single solid white line next to the car and continuing ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a grey curb and a metal railing on the right. Photo 2 shows the raised
                        grey curb immediately to the right of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right | roles: the white
                        solid line fits the role of a lane line; the curb fits the role of an edge line |
                        markings: no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The curb marks the edge of the roadway and prohibits leaving the road.
                        [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the physical curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          prohibited: prohibited by the solid white line [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white line to the left
                        or the curb to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe [], citation unlisted,
                        contradictions ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 6666, out 654, 12.0 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with
                        other vehicles ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the road from the sidewalk/curb. Photo 2
                        shows the same solid white line next to the car and further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line next to the car with several long dashes and gaps,
                        continuing further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows the head of a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a solid edge line on the left and a broken lane line on the right
                        indicate my lane is the leftmost of two lanes. | roles: the white solid edge line and
                        white dashed lane line fit their respective roles. | markings: the straight arrow is
                        consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across a broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: A straight arrow allows the vehicle to proceed straight through the
                        intersection. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [IN-6(1)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow in the lane
Step 6  turn_left       prohibited (correct): prohibited because the arrow in the lane only shows straight
Step 6  turn_right      prohibited (correct): prohibited because the arrow in the lane only shows straight
Step 6  u_turn          prohibited (correct): prohibited because the arrow in the lane only shows straight
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed, but do
                        not cross the solid line on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 741, 12.83 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test C | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, facing a straight stretch with a
                        white van ahead. There are no immediate intersections or ramps visible. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the left lane. Photo 2 shows
                        a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the right lane. Photo 2
                        shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the middle lane (index 2) agree with having a lane line on both my left and right. |
                        roles: the white dashed lines are consistent with lane lines separating traffic moving
                        in the same direction. | markings: the straight-ahead arrow is consistent with the
                        lane's position and boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I may change lanes to the right after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            arrow:straight: The arrow allows me to go straight.
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary and [IN-6(1)]
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary and [IN-6(1)]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow in my lane
Step 6  turn_left       prohibited (correct): prohibited because the arrow in my lane only shows straight
                        ahead
Step 6  turn_right      prohibited (correct): prohibited because the arrow in my lane only shows straight
                        ahead
Step 6  u_turn          prohibited (correct): prohibited because the arrow in my lane only shows straight
                        ahead
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change lanes to the left or right if needed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 728, 11.92 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward with buildings and
                        trees on both sides. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line extending ahead. Photo 2 shows a solid white line
                        next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line. Photo 2 shows a broken white line with several
                        short dashes and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a lane line on the left and an edge line on the right indicate
                        the rightmost lane of a two-lane road. | roles: the white solid line as a lane line
                        and white dashed line as an edge line are consistent with UK road markings. |
                        markings: no markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The rule regarding not crossing solid lines for overtaking does not
                        apply to this dashed line. [[IN-6(4)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the dashed white line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right if necessary; do not cross the solid white line
                        to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 685, 11.61 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with shops on both sides, heading towards a straight stretch
                        of road. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road. Photo 2 shows a
                        continuous solid yellow line next to the curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, only the road surface and parked cars.
                        Photo 2 shows no painted line on the right.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a yellow edge line on the left and no line on the right
                        indicate a single-lane road where the left side is the curb/edge. | roles: the yellow
                        solid line on the left fits the role of an edge line (parking restriction). |
                        markings: no markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule governs this boundary as there is no paint or curb.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed as there is no marking governing this action
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid yellow line on the
                        left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 6666, out 648, 11.9 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, with buildings on the left
                        and trees on the right. The road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the right edge of the road.
                        Photo 2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed pattern fits both the lane_line and edge_line roles. |
                        markings: No markings were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: A white dashed edge line generally allows crossing into the shoulder
                        or parking area if safe and permitted. [null]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a white dashed
                        lane line, which allows lane changes per [IN-6(1)].
Step 6  change_right    allowed (correct): allowed: the right boundary is a white dashed edge line, which does
                        not prohibit leaving the lane.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left
                        if needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 846, 16.43 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward. The road is wet and there are
                        buildings on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line along the left edge of the road next to the curb. Photo 2
                        confirms a single yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line to the right of the car, only other vehicles. Photo 2
                        also shows no painted line on the right.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The single lane count and index 1 agree
                        with the left edge line and the absence of a right boundary line. | roles: The yellow
                        solid edge line on the left fits the role of an edge line next to a curb. | markings:
                        No markings are present in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A vehicle shall not be parked where there is a continuous yellow line
                        installed or painted on the carriageway on the kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule governs the absence of a line on the right.
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid yellow line
                        and there is a curb, and [IN-6(6)] prohibits driving over a solid line.
Step 6  change_right    allowed: allowed: no marking governs this action.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right if necessary. Do not cross the yellow line on the left
                        or park there.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 6666, out 825, 12.59 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction where a bus
                        lane is present on the left. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the bus lane. Photo 2 shows
                        the same white broken line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the rightmost lane. Photo 2
                        shows the same white broken line next to my car, with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with the boundaries; I have a lane line on my left and a lane line on my
                        right, meaning there are lanes to both sides of me (though the left is a special
                        lane). | roles: The white dashed lines fit the role of lane lines. | markings: No
                        markings were found in my lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: I may change lanes across this broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: I may change lanes across this broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the white dashed left boundary and
                        rule [IN-6(1)].
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary and rule [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane restricting
                        it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        in my lane.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        in my lane.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area ahead of or next to my
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of a multi-lane road. You may continue straight or
                        change lanes to the left or right as needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6666, out 860, 13.46 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, facing a road with parked cars on both sides
                        and a red bus ahead. There is a yellow box junction ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a curb and a dashed white line next to the curb. Photo 2 shows the same
                        dashed white line next to the curb, consisting of several short white dashes and gaps.
                        white dashed, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a curb and a dashed white line next to the curb. Photo 2 shows the same
                        dashed white line next to the curb, consisting of several short white dashes and gaps.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show a yellow box with a cross inside it painted
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the edge lines on both sides | roles: the white dashed lines next to curbs
                        fit the role of edge lines | markings: the yellow box area is consistent with a city
                        street environment | unseen: no | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a dashed white edge line; it generally
                        marks the edge of the carriageway. [null]
Step 5  Rule            right_boundary: No specific rule provided for a dashed white edge line; it generally
                        marks the edge of the carriageway. [null]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road.
                        [[IN-22.(1)viii]]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a dashed line and
                        there is no rule prohibiting crossing it to the curb area if safe.
Step 6  change_right    allowed (correct): allowed: the right boundary is a dashed line and there is no rule
                        prohibiting crossing it to the curb area if safe.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can proceed straight. Do not stop inside the yellow box junction ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions ['change_left
                        allowed across a curb', 'change_right allowed across a curb']
Tokens                  in 6666, out 765, 25.12 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides. Ahead is a clear stretch of
                        road with a bus in the distance. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line separating the lane from a bicycle lane, and a solid
                        yellow line at the curb. Photo 2 shows a white dashed line with long dashes and gaps,
                        and a solid yellow line next to the curb.
                        white dashed, curb yes, special_lane_line, evidence full
Step 2  Right           Photo 1 shows no painted line, only parked cars along the right side of the road.
                        Photo 2 also shows no painted line next to the car.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 and Photo 2 show a bicycle symbol to the left of my lane,
                        but it is not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows crossing for lane changes, provided it is
                        safe. [null]
Step 5  Rule            right_boundary: No marking governs this boundary. [null]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a dashed line,
                        which permits crossing.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: there is no painted line, but the area
                        is occupied by parked cars and the road edge.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow in my lane governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow in my lane governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can proceed straight or change left into the cycle lane if safe. Avoid moving
                        right due to parked vehicles.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb', 'change_right decided with
                        nothing marked on that side']
Tokens                  in 6666, out 818, 13.44 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with a pedestrian crossing
                        and traffic signals ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line along the left edge of the road, separating the lane
                        from the sidewalk. Photo 2 confirms a white solid line next to the car, which
                        continues forward.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from a right-turn lane. Photo 2
                        shows a white solid line next to the car, which continues forward.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 and Photo 2 show a white transverse line across the
                        lane before the pedestrian crossing.; line:crosswalk (full): Photo 1 and Photo 2 show
                        a zebra crossing (white stripes) across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The edge line and curb prohibit leaving the roadway to the left. [null]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 5  Rule            line:stop_line: The driver shall stop before the stop line if the traffic signal is
                        red. [[IN-12(1)(a)]]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the left edge line and curb.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it.
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement.
Step 6  u_turn          prohibited: prohibited by the solid white lane line [IN-8(3)(a)(iv)].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Stop before the stop line if the signal is red
                        and give way to pedestrians at the crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions None, unsafe [], citation
                        unlisted, contradictions ['rightmost lane, but a lane line on the right', 'u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 6666, out 966, 15.7 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, with shops and buildings on
                        both sides. The road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, separating the roadway from a
                        parking/shoulder area. Photo 2 shows this white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a lane line, and the white solid line
                        fits the role of an edge line. | markings: No markings are present in the lane, which
                        is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a dashed lane
                        line, which allows lane changes per [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid edge
                        line, and crossing it is prohibited by [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the roadway. You may continue straight or change to
                        the left lane, but do not cross the solid white line on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 882, 15.28 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on the left. Ahead is a straight stretch of
                        road with a vehicle in front. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a yellow line along the edge of the road. Photo 2
                        confirms a raised curb and two yellow solid lines side by side next to the car.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the right lane. Photo 2
                        shows a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white straight-ahead arrow in my
                        lane.; symbol:bike (full): Photo 2 shows a bicycle symbol painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a lane line on the right and an edge line on the left
                        indicate I am in the leftmost lane. | roles: the yellow double solid line on the left
                        fits the role of an edge line (no parking), and the white dashed line on the right
                        fits the role of a lane line. | markings: the straight arrow and bike symbol are
                        consistent with a lane that allows going straight. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: Lane changes are allowed after giving a proper signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 5  Rule            symbol:bike: This is an informative marking indicating a cycle lane or shared space
                        and does not govern the seven actions.
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a raised curb and
                        double solid yellow line [IN-6(6)].
Step 6  change_right    allowed (contested, correct): allowed: the right boundary is a white dashed line
                        [IN-6(1)].
Step 6  go_straight     allowed (correct): allowed: the arrow in the lane shows straight ahead.
Step 6  turn_left       prohibited (correct): prohibited: the arrow in the lane only shows straight ahead.
Step 6  turn_right      prohibited (correct): prohibited: the arrow in the lane only shows straight ahead.
Step 6  u_turn          prohibited (correct): prohibited: the arrow in the lane only shows straight ahead.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed, but do
                        not stop or park on the left side due to the double yellow lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 1063, 15.57 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving on the left. Ahead is a clear
                        stretch of road with other vehicles and pedestrians on the sidewalk. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a red line along the curb on the far left, and a white broken line
                        separating my lane from the next. Photo 2 shows the white broken line next to my car,
                        consisting of several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of my lane. Photo 2 shows this line
                        next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 1 agree with having a lane line on the right and a curb/edge on the left (though
                        the red line is an edge marking, the white broken line to the right confirms I am in
                        the left lane of two) | roles: the white dashed lines fit the role of lane lines |
                        markings: no markings in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a dashed lane line on the left, but
                        generally allows lane changes if safe. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            left_boundary: Overtaking from the left is permitted on a multi-lane road if safe.
                        [[IN-14(2)(a)]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed line and there is a marked
                        lane to the left (though it appears to be a bus lane/parking area, the boundary itself
                        is permissive)
Step 6  change_right    allowed (correct): allowed: the right boundary is a dashed line, and [IN-6(1)] allows
                        lane changes with a signal
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts going straight
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may continue straight or change lanes to the right if
                        needed. Be mindful of the red line on the far left, which typically indicates no
                        stopping in the UK.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 6666, out 813, 16.48 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road ahead
                        appears to be a straight stretch with buildings on both sides. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the curb on the far left, and a white broken line
                        separating my lane from the lane to the right. Wait, the prompt says traffic keeps
                        left. My lane is the leftmost lane. To my left is the curb. Photo 1 shows a red line
                        on the curb. Photo 2 shows the red line on the curb next to my car.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with several long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 1 agree with the left boundary being an edge line (curb) and the right boundary
                        being a lane line. | roles: The red solid line on the curb is an edge line; the white
                        dashed line is a lane line. This is consistent. | markings: No markings were found in
                        my lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The red line on the curb is not covered by the provided Indian rules,
                        but as an edge line/curb, it prohibits leaving the roadway to the left. [null]
Step 5  Rule            right_boundary: I may change lanes to the right after giving a proper signal.
                        [[IN-6(1)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a curb/edge line.
Step 6  change_right    allowed (correct): allowed: the right boundary is a white dashed lane line, which
                        allows lane changes per [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right.
                        Do not cross the left curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 891, 14.2 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, heading towards a straight
                        stretch of road with buildings and a cinema on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to a raised curb and metal railing. Photo 2
                        shows a white solid line and a raised curb immediately to the right of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle with the number '20'
                        painted on the road surface in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        next to a curb fits the role of an edge line | markings: the speed limit text is
                        consistent with a standard urban lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid white line. [[IN-6(6)]]
Step 5  Rule            text:speed_limit: This is an informative marking indicating the speed limit and does
                        not govern the seven actions. [null]
Step 6  change_left     allowed (correct): allowed: the left boundary is a white dashed lane line, which
                        allows lane changes per [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        line and a curb, which prohibits crossing per [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in my lane restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: there are no turn arrows or waiting areas governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable: there are no turn arrows or waiting areas governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable: there are no turn arrows or waiting areas governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: there is no waiting area or two-way left-turn lane
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid line on the right. Observe the 20 mph speed limit.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:speed_limit'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 999, 14.1 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a stretch of road with parked cars on the
                        right and a sidewalk on the left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a grey raised curb separating the road from the sidewalk. Photo 2
                        confirms the presence of a raised grey curb next to the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating the driving lane from a parking area.
                        Photo 2 shows a white dashed line with several long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; a curb on the left and a dashed line on the right indicate a single
                        lane with a parking area to the right. | roles: the white dashed line fits the role of
                        a lane line separating the driving lane from a parking/stopping area. | markings: no
                        markings in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The raised curb marks the edge of the roadway and prohibits driving
                        onto the sidewalk.
Step 5  Rule            right_boundary: The dashed line allows lane changes after giving a proper signal.
                        [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb (left_boundary) which
                        defines the edge of the road.
Step 6  change_right    allowed (correct): allowed by the white dashed line (right_boundary) and rule
                        [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may proceed straight or move to the right into the
                        parking area if needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6666, out 683, 12.26 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with shops on both sides, heading towards a distant
                        intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a sidewalk with pedestrians and shops. Photo 2 shows
                        the same raised curb immediately to the left of the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a wide open asphalt area to the right with parked cars further ahead,
                        but no painted lines are visible. Photo 2 shows only asphalt to the right of the car
                        with no markings.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a curb on the left and no lane line on the right. | roles: The
                        roles fit: the left boundary is a physical curb (edge), and the right side is an open
                        road edge. | markings: No markings were found in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The physical curb prohibits leaving the roadway to the left. [null]
Step 5  Rule            right_boundary: No painted line or curb exists to the right, allowing movement into
                        the adjacent space. [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the physical curb (left_boundary).
Step 6  change_right    allowed (correct): allowed as there is no marking or curb governing this action
                        (right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking
                        governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a single lane bounded by a curb on the left. You may proceed straight or
                        move to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 6666, out 823, 13.25 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, with buildings and shops on
                        both sides. The road ahead appears to be a straight stretch with no immediate
                        intersection or ramp. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a parking/stopping area where
                        cars are parked. Photo 2 confirms a single solid white line immediately to the left of
                        my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane to the right.
                        Photo 2 shows a series of white dashes and gaps immediately to the right of my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the boundaries: a solid edge line on the left and a dashed lane line on the
                        right. | roles: The white solid line on the left acts as an edge line for the
                        roadway/parking area, and the white dashed line on the right acts as a lane separator.
                        | markings: No markings are present in my lane, which is consistent with the
                        boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across a broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the dashed white lane line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Do not cross the solid white
                        line to the left into the parking area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 858, 16.32 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, where traffic keeps left. The road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white solid line next to the car that continues ahead. Photo 2
                        confirms a single white solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car and further ahead. Photo 2 shows a
                        white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; there is a lane to the left and a lane to the right. | roles: the
                        white solid and dashed lines fit the role of lane lines in a multi-lane road. |
                        markings: no markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across a broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the white solid line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the white dashed line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs it
Step 6  turn_right      not_applicable: not_applicable as no arrow governs it
Step 6  u_turn          not_applicable: not_applicable as no arrow governs it
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may continue straight or change
                        to the lane on your right, but you must not cross the solid line to the left into the
                        bus lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6666, out 658, 12.38 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, driving forward. The road ahead is
                        straight with no immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, which is a continuous
                        solid line. Photo 2 confirms this is a single solid white line next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right side that is zigzagged. Photo 2 shows the
                        zigzag pattern clearly next to the car, consisting of diagonal segments.
                        white zigzag, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [IN-6(6)]
Step 5  Rule            right_boundary: Zigzag lines typically indicate a no-parking/no-stopping zone near a
                        crossing, but do not prohibit driving within the lane.
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white line,
                        and rule [IN-6(6)] prohibits driving over it.
Step 6  change_right    allowed (contested, label prohibited): allowed: the right boundary is a zigzag line
                        which does not prohibit lane departure according to the provided rules, though it is
                        an edge line.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white line on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 800, 25.07 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with a
                        right-turn lane. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a raised curb and a sidewalk to the right. Photo 2 confirms the presence
                        of a raised curb and a metal railing separating the road from the sidewalk.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 1 and Photo 2 show a white arrow pointing to the right in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my position (2nd
                        from left) agree with having a lane line on the left and an edge line/curb on the
                        right. | roles: the white dashed line fits the role of a lane line; the curb fits the
                        role of an edge line. | markings: the right-turn arrow is consistent with being in the
                        rightmost lane of a two-lane road. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: The curb prohibits leaving the roadway to the right. [null]
Step 5  Rule            arrow:right: I shall remain in this lane while taking a right turn. [[IN-8(2)(c)]]
Step 6  change_left     allowed (correct): allowed by the white dashed lane line [IN-6(1)]
Step 6  change_right    prohibited (contested, correct): prohibited by the raised curb
Step 6  go_straight     prohibited (correct): prohibited by the right-turn arrow which restricts the lane to
                        right turns only
Step 6  turn_left       prohibited (correct): prohibited by the right-turn arrow
Step 6  turn_right      allowed (correct): allowed by the right-turn arrow [IN-8(2)(c)]
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited by the right-turn arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a dedicated right-turn lane. Use this lane to turn right at the
                        intersection; if you intend to go straight or turn left, you must change to the left
                        lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 759, 13.36 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with buildings and trees on both sides,
                        proceeding straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane on the left. Photo
                        2 confirms a solid white line immediately to the left of the car.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane to the right.
                        Photo 2 shows a white dash and gap immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a special lane line on the left and a lane line on the right
                        place the car in the second lane from the left. | roles: the white solid line for a
                        bus lane and white dashed line for a lane separator fit their roles. | markings: no
                        markings are present in my lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes after giving a proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the dashed white line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Do not enter the bus lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6666, out 796, 13.54 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, driving forward. The road ahead is
                        straight with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a single yellow line along the left edge of the road. Photo 2 confirms a
                        single solid yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, only parked cars. Photo 2 shows no painted
                        line next to the car.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the word 'BUS' painted in yellow in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule for a non-existent line; it marks the edge of the
                        drivable surface.
Step 5  Rule            text:bus: Vehicles of other classes than those specified for the special lane shall
                        not be driven in that lane. [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid yellow line
                        and there is a curb [IN-6(6)]
Step 6  change_right    allowed (correct): allowed: there is no painted line or curb governing this action
Step 6  go_straight     prohibited (contested, label allowed): prohibited: the lane is marked as a bus lane
                        and my car is an ordinary car [IN-6(3)]
Step 6  turn_left       prohibited: prohibited: the lane is marked as a bus lane and my car is an ordinary car
                        [IN-6(3)]
Step 6  turn_right      prohibited: prohibited: the lane is marked as a bus lane and my car is an ordinary car
                        [IN-6(3)]
Step 6  u_turn          prohibited: prohibited: the lane is marked as a bus lane and my car is an ordinary car
                        [IN-6(3)]
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane, which is prohibited for ordinary cars. You should
                        change right immediately to exit the bus lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions True, unsafe [], citation unlisted,
                        contradictions ['change_right decided with nothing marked on that side', 'go_straight,
                        turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 6666, out 921, 14.39 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, with shops and buildings on
                        both sides. The road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, separating the roadway from a
                        parking/shoulder area. Photo 2 shows this white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a lane line, and the white solid line
                        fits the role of an edge line. | markings: No markings are present in the lane, which
                        is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a dashed lane
                        line, which allows lane changes per [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid edge
                        line, and crossing it is prohibited by [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the roadway. You may continue straight or change to
                        the left lane, but do not cross the solid white line on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 882, 15.28 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, where traffic keeps to the
                        left. The road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a single solid white line next to my car, extending further ahead.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a special_lane_line on the left and a lane_line on the right
                        place my car in the second lane from the left. | roles: the white solid line correctly
                        identifies the boundary of a special lane (bus lane), and the white dashed line
                        correctly identifies a lane separator. | markings: no markings are present in my lane.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across a broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)] and the
                        fact that it bounds a bus lane [IN-6(3)].
Step 6  change_right    allowed (correct): allowed by the dashed white line [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right if needed. Do not enter the bus lane to your
                        left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6666, out 865, 13.19 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides, proceeding straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road next to the curb.
                        Photo 2 confirms a single solid yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right side of the lane. Photo 2 also shows no
                        painted line on the right side.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being
                        unknown/absent. | roles: the yellow solid line on the left fits the role of an
                        edge_line (curb side). | markings: there are no markings in the lane to contradict. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 6  change_left     prohibited (contested, correct): the left boundary is a solid yellow line, and
                        [IN-6(6)] prohibits driving over a solid longitudinal line.
Step 6  change_right    allowed (correct): no marking governs this action
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          prohibited: the left boundary is a solid yellow line, and [IN-8(3)(a)(iv)] prohibits
                        U-turns across a continuous solid line.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid yellow line on the left
                        or park along it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 6666, out 621, 9.43 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a city road with shops and buildings on both sides. Ahead is a
                        clear stretch of road with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line separating my lane from a parking/shoulder area on
                        the left. Photo 2 confirms a single white solid line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line that ends as it meets a raised concrete island/curb.
                        Photo 2 shows a white solid line next to the car, followed by a raised concrete curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the white solid edge line [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line and raised
                        curb [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          prohibited: prohibited by the solid lines on both sides [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to either side are prohibited due
                        to solid edge lines and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 6666, out 776, 12.54 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road continues
                        straight ahead with buildings on both sides. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle containing the number
                        '20' painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        index 2 agree with having lane lines on both my left and right | roles: white dashed
                        lines are consistent with lane_line roles | markings: the speed limit marking is
                        consistent with a standard travel lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I may change lanes to the right after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            text:speed_limit: This is an informative marking indicating a speed limit and does not
                        govern the seven actions. [null]
Step 6  change_left     allowed (contested, correct): allowed by the white dashed left boundary and [IN-6(1)]
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary and [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and no
                        arrows restricting movement
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes as needed, observing the 20 mph speed limit indicated on the road.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 776, 13.16 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides, approaching a stretch of road
                        with zigzag markings. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line that starts as a straight edge and then becomes a zigzag
                        pattern. Photo 2 shows the white zigzag line next to the car and the straight edge
                        further back.
                        white zigzag, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line that starts as a straight edge and then becomes a zigzag
                        pattern. Photo 2 shows the white zigzag line next to the car and the straight edge
                        further back.
                        white zigzag, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the left boundary is an edge line and the right is a lane line,
                        meaning there is another lane to the right. | roles: the white zigzag lines are
                        consistent with edge and lane markings in this context. | markings: no markings in the
                        lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The left edge of the road is marked by a zigzag line and a curb,
                        prohibiting leaving the roadway to the left. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a solid line; however, zigzag
                        lines are typically informative of no-parking/no-stopping zones rather than
                        prohibiting lane changes unless they are solid. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the curb and edge line
Step 6  change_right    allowed (contested, label prohibited): allowed by the white line, provided a signal is
                        given as per [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or signal to change to the right. The zigzag lines indicate a zone
                        where stopping or parking is prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6666, out 727, 13.9 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test C | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward. The road ahead is a straight
                        stretch with parked vehicles on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows no painted line on the left, only the side of a red bus. Photo 2 shows
                        no painted line on the left, just the asphalt next to the bus.
                        none none, curb no, unknown, evidence full
Step 2  Right           Photo 1 shows a yellow line along the right edge of the road near the curb. Photo 2
                        shows a single solid yellow line next to the car and continuing ahead.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the absence of a left lane line and the presence of a right edge line | roles:
                        the yellow solid line on the right fits the role of an edge line (curb side) |
                        markings: no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: no specific rule for an unmarked left boundary
Step 5  Rule            right_boundary: parking is prohibited where there is a continuous yellow line on the
                        kerb side [[IN-22.(2)(j)]]
Step 6  change_left     allowed (correct): no marking governs this action
Step 6  change_right    prohibited (contested, correct): the right boundary is a solid yellow line and a curb,
                        which prohibits crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line on the right as
                        it marks the curb edge.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['change_left decided
                        with nothing marked on that side']
Tokens                  in 6666, out 623, 11.5 s
```
