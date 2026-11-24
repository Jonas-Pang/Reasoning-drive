# Reasoning of lane run 20261117_153635_laneC_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection where a
                        red bus is stopped ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the curb. Photo 2 shows a solid red line next to the
                        car and further ahead.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line. Photo 2 shows a white dashed line next to the car
                        with several long dashes and gaps, continuing further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a bicycle symbol painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a red edge line on the left and a white lane line on the right
                        indicate the leftmost lane. | roles: the red solid edge line and white dashed lane
                        line fit their roles. | markings: the bicycle symbol is consistent with a lane that
                        may be shared or designated for cycles. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The red solid line indicates a restriction on stopping or parking, but
                        does not prohibit driving within the lane. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            symbol:bike: The bicycle symbol indicates the lane is shared with or designated for
                        cyclists. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a curb and a solid
                        red edge line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: the right boundary is a dashed white line,
                        which allows lane changes per [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane. Be
                        mindful of cyclists as indicated by the bicycle symbol in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation unlisted,
                        contradictions []
Tokens                  in 6489, out 928, 14.55 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction or
                        intersection where the road layout changes. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line separating the road from a cycle lane/shoulder on the left.
                        Photo 2 shows a white solid line next to the car, and further ahead it remains solid.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a white solid edge line on the left and a dashed lane line on the
                        right indicate the leftmost lane of a multi-lane road. | roles: the white solid line
                        fits the role of an edge line, and the white dashed line fits the role of a lane line.
                        | markings: no markings are present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across a broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    allowed (contested, label prohibited): allowed by the dashed white lane line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid line on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6489, out 683, 11.6 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with a
                        pedestrian crossing and a cycle lane ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to the car, which continues ahead. Photo 2
                        confirms a white dashed line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car, which continues ahead. Photo 2
                        confirms a white solid line. Further right is a curb and a metal barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane. Photo 1
                        confirms this arrow.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a lane line on the left and an edge line on the right indicate
                        the car is in the leftmost lane of a two-lane road. | roles: the white dashed line
                        fits the role of a lane line, and the white solid line next to a curb fits the role of
                        an edge line. | markings: the straight-ahead arrow is consistent with the lane's
                        position. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            arrow:straight: A straight-ahead arrow allows the vehicle to proceed straight. [null]
Step 6  change_left     allowed (correct): allowed by the white dashed lane line and [IN-6(1)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line and
                        [IN-6(6)]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this
                        movement
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this
                        movement
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this
                        movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane to go straight. You may change to the left lane if necessary, but do
                        not cross the solid line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 6489, out 761, 13.85 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with buildings on both sides. The road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid yellow lines along the left edge of the road. Photo 2 confirms
                        two solid yellow lines next to the car and continuing ahead.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating the lanes. Photo 2 shows a white dashed
                        line next to the car with visible gaps and dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; the
                        left boundary is an edge line and the right is a lane line, meaning my lane is the
                        leftmost of my direction. | roles: the yellow double solid line on the left fits the
                        role of an edge line (parking restriction), and the white dashed line on the right
                        fits the role of a lane line. | markings: no markings in my lane to check. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow edge line and
                        the presence of a curb [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the white dashed lane line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow governing this
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow governing this
Step 6  u_turn          prohibited: prohibited by the double solid yellow line on the left [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right if needed. Do not cross the double yellow
                        lines on the left or attempt a U-turn across them.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right', 'u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 6489, out 850, 13.27 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
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
                        the edge lines on both sides | roles: the white solid lines on both sides fit the role
                        of edge lines for a single-lane road | markings: the crosswalk is consistent with the
                        road layout | unseen: no | result: consistent
Step 5  Rule            left_boundary: The edge line marks the boundary of the roadway; crossing it is
                        prohibited as it leads to a sidewalk. [null]
Step 5  Rule            right_boundary: The edge line marks the boundary of the roadway; crossing it is
                        prohibited as it leads to a sidewalk. [null]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the left edge line and curb
Step 6  change_right    prohibited (contested, correct): prohibited by the right edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no turn arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no turn arrow in the lane
Step 6  u_turn          prohibited: prohibited by the solid edge lines on both sides [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight, ensuring you give way to any pedestrians on
                        the zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 6489, out 724, 12.82 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
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
                        from a parking area. | roles: the double red lines on the left are typical for UK 'no
                        stopping' edge lines; the white dashed line on the right is a standard lane separator.
                        | markings: no markings present in my lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The double red lines are a UK-specific marking prohibiting
                        stopping/parking; no provided Indian rule covers red lines, but as an edge line with a
                        curb, it prohibits leaving the roadway to the left. [null]
Step 5  Rule            right_boundary: The broken white line allows lane changes after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb and double red edge
                        lines.
Step 6  change_right    allowed (correct): allowed by the broken white line [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict forward movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right if needed. Do not cross the red lines on the left or
                        drive onto the sidewalk.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6489, out 699, 12.84 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, with buildings on the right
                        and a park area on the left. The road continues straight ahead. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line separating the road from a blue-painted cycle
                        lane/shoulder. Photo 2 confirms a solid white line next to the car, continuing
                        straight ahead.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the dashed lane line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Do not cross the solid white
                        line to the left into the cycle lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 767, 13.15 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road continues
                        straight ahead with shops and parked cars on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the right lane. Photo 2
                        shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 1 agree with having a lane line on the right and a lane line on the left
                        (indicating another lane of my direction exists there). | roles: the white dashed
                        lines fit the role of lane lines. | markings: no markings in my lane to check. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I may change lanes to the right after giving a proper signal.
                        [[IN-6(1)]]
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary and rule [IN-6(1)]
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary and rule [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no marking governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of a multi-lane road. You may proceed straight or change
                        lanes to the right if safe to do so.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 6489, out 675, 11.34 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a pedestrian crossing
                        (zebra crossing). (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left that is the edge of the roadway. Photo 2 shows
                        a white solid line next to the car, which continues as a solid line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a pedestrian crossing (zebra crossing)
                        consisting of wide white stripes across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a white solid edge line on the left and a white dashed lane line
                        on the right indicate the leftmost lane of a two-lane road. | roles: the white solid
                        edge line and white dashed lane line fit their respective roles. | markings: the
                        crosswalk is consistent with the urban road environment. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The solid edge line and curb prohibit leaving the roadway to the left.
                        [null]
Step 5  Rule            right_boundary: Lane changes to the right are allowed after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid edge line and curb
                        (left_boundary).
Step 6  change_right    allowed (contested, label prohibited): allowed by the dashed lane line
                        (right_boundary) per [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it.
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may proceed straight or change to the right lane, but
                        you must give way to pedestrians at the zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 758, 13.21 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. There is a
                        pedestrian crossing and a bicycle lane to the left. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from a bicycle lane. Photo 2
                        shows the same white dashed line next to my car, consisting of short dashes and gaps.
                        white dotted, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from another lane of traffic.
                        Photo 2 shows the same white dashed line next to my car, consisting of long dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a circular marking with the number
                        '20' painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; the left boundary is a special lane line for the cycle
                        lane, and the right is a lane line for the adjacent traffic lane. | roles: the white
                        dashed/dotted patterns fit the roles of lane and special lane boundaries. | markings:
                        the speed limit text is consistent with an urban road environment. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A dotted white line separating a cycle lane allows crossing into the
                        cycle lane if safe and necessary, though it is primarily a boundary. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            text:speed_limit: This is an informative marking indicating the speed limit of 20 mph.
                        [null]
Step 6  change_left     allowed (contested, label prohibited): allowed; the dotted white line
                        (special_lane_line) does not prohibit crossing, provided it is safe.
Step 6  change_right    allowed (correct): allowed; the dashed white line (lane_line) allows lane changes per
                        [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed; no marking prohibits continuing straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable; no marking governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and observe the 20 mph speed limit. Be mindful of the bicycle lane
                        to your left and the pedestrian crossing ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 971, 15.13 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with
                        shops on the left and a park area on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white line that is dashed near the car and becomes solid further
                        ahead. Photo 2 shows a white dashed line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line. Photo 2 shows a white dashed line with long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 and Photo 2 show a white arrow pointing straight and then
                        turning left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries, as the car is in
                        the rightmost lane of its direction. | roles: the white dashed lines fit the role of
                        lane lines separating traffic moving in the same direction. | markings: the left-turn
                        arrow is consistent with the lane's position and boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            arrow:left: The driver shall use this lane while taking a left turn. [[IN-8(1)(c)]]
Step 6  change_left     allowed (contested, correct): allowed by the dashed white left_boundary and rule
                        [IN-6(1)].
Step 6  change_right    allowed (correct): allowed by the dashed white right_boundary and rule [IN-6(1)].
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited by the arrow:left which only allows a
                        left turn.
Step 6  turn_left       allowed (correct): allowed by the arrow:left and rule [IN-8(1)(c)].
Step 6  turn_right      prohibited (correct): prohibited by the arrow:left which only allows a left turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this and
                        no specific prohibition is visible in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a left-turn lane. Use this lane to turn left at the intersection; if you
                        intend to go straight or turn right, you must change lanes.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:straight_left']), actions False, unsafe [], citation
                        unlisted, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 6489, out 953, 26.18 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road continues
                        straight ahead with no immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues as a solid white
                        line further ahead. Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing as a broken white line
                        further ahead. Photo 2 shows a broken white line with clear dashes and gaps next to
                        the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a solid edge line on the left and a dashed lane line on the
                        right. | roles: The white solid line on the left fits the role of an edge line; the
                        white dashed line on the right fits the role of a lane line. | markings: No markings
                        were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid white line. [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across the broken line after giving a
                        proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this, though crossing the left
                        boundary is prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Do not cross the solid white
                        line on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 838, 14.45 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with a pedestrian crossing
                        and a traffic island ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the left edge of the road next to the sidewalk. Photo 2
                        shows two red lines side by side (double red lines) along the curb.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the right lane. Photo 2
                        shows a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left_right (full): Photo 1 and Photo 2 show a white arrow in my lane pointing
                        both straight and left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a red edge line on the left and a white lane line on the right. |
                        roles: the red edge line and white dashed lane line fit their roles. | markings: the
                        straight-and-left arrow is consistent with the lane's position. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A continuous yellow line prohibits parking; while these are red, they
                        typically indicate no stopping in the UK, but the provided Indian rules only mention
                        yellow lines for parking. [IN-22.(2)(j)]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [IN-6(1)]
Step 5  Rule            arrow:left_right: The driver shall use this lane while taking a left turn, and it also
                        allows going straight. [IN-8(1)(c)]
Step 6  change_left     prohibited (contested, correct): prohibited by the red double solid edge line and
                        curb.
Step 6  change_right    allowed (correct): allowed by the white dashed lane line and rule [IN-6(1)].
Step 6  go_straight     allowed (correct): allowed by the arrow in my lane.
Step 6  turn_left       allowed (correct): allowed by the arrow in my lane and rule [IN-8(1)(c)].
Step 6  turn_right      prohibited (correct): prohibited by the arrow in my lane which does not show a right
                        turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to either go straight or turn left. You may change
                        lanes to the right if necessary.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left_right'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions ['go_straight allowed although no arrow shows it',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 6489, out 770, 9.47 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a stretch of road with a cyclist ahead and
                        a pedestrian crossing further forward. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line along the left edge of the road, next to a sidewalk.
                        Photo 2 confirms a single white solid line immediately to the left of the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white zigzag line on the right side of the lane. Photo 2 shows the
                        zigzag pattern clearly next to the car, consisting of several diagonal segments.
                        white zigzag, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a white transverse line (pedestrian
                        crossing) across the lane ahead of the cyclist.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: Zigzag lines in the UK typically indicate a no-parking/no-stopping
                        zone near a crossing; they do not prohibit lane changes but define the road edge.
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    allowed (contested, label prohibited): allowed as there is no solid line or curb
                        prohibiting it, though it is an edge boundary
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing forward
Step 6  turn_left       not_applicable: not_applicable as there is no left-turn arrow or intersection layout
                        allowing it
Step 6  turn_right      not_applicable: not_applicable as there is no right-turn arrow
Step 6  u_turn          prohibited: prohibited by the solid white line on the left [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be prepared to yield to pedestrians at the
                        upcoming crosswalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 6489, out 897, 14.32 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection. (lanes
                        3, mine 1, full)
Step 2  Left            Photo 1 shows a solid line along the left edge of the road next to a sidewalk. Photo 2
                        shows a solid red/pink line along the curb.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the next lane. Photo 2 shows
                        a white broken line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the left edge_line and right lane_line | roles: the red solid edge line and white
                        dashed lane line fit their roles | markings: the straight arrow is consistent with the
                        lane boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The red solid line on the curb prohibits parking [IN-22.(2)(j)] but
                        does not govern driving movements within the lane. [null]
Step 5  Rule            right_boundary: Lane changes across the broken line are allowed after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: A straight arrow allows the vehicle to proceed straight through the
                        intersection. [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the curb and solid edge line
Step 6  change_right    allowed (correct): allowed by the broken white lane line [IN-6(1)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow in the lane
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited by the straight arrow and the left curb
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this
                        movement, but the lane is for straight traffic
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow and the left curb
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions []
Tokens                  in 6489, out 706, 14.2 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a pedestrian crossing and a
                        junction. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line along the left edge of the road. Photo 2 shows the
                        same white solid line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line along the right edge of the road. Photo 2 shows the
                        same white solid line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a pedestrian crossing (zebra crossing)
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the edge lines on both sides | roles: the white solid lines on both sides fit the role
                        of edge lines for a single-lane road | markings: the crosswalk is consistent with the
                        road layout | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid line. [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single solid line. [[IN-6(6)]]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          prohibited: prohibited by the solid white edge lines [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight, ensuring you give way to any pedestrians on
                        the zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 6489, out 715, 12.53 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving behind several red buses. The
                        road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane on the left. Photo
                        2 confirms a single solid white line immediately to the left of my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a red line along the edge of the road next to a curb. Photo 2 shows this
                        red line and the adjacent raised curb.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The red edge line and curb mark the boundary of the roadway; crossing
                        it is prohibited by the physical curb. [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the physical curb and edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          prohibited: prohibited by the solid white line [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Do not cross the solid white line into
                        the bus lane or the curb on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 6489, out 757, 12.83 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. There is a bus
                        stopped in a lane to the left and other vehicles ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        confirms a single solid white line next to my car and continuing ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a grey curb and a metal railing on the right side of the road. Photo 2
                        shows the curb and the edge of the roadway next to my car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line/curb on the right |
                        roles: the white solid line fits the role of a lane line; the curb fits the role of an
                        edge line | markings: no markings in my lane to check | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The curb marks the edge of the roadway and prohibits leaving the road.
                        [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the physical curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          prohibited: prohibited by the solid white line [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white line to the left
                        or the curb to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe [], citation unlisted,
                        contradictions ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 6489, out 671, 11.21 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with
                        other vehicles ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating the road from the curb. Photo 2 shows a
                        white solid line next to my car, followed by a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line and the white solid line
                        with a curb fits the role of an edge line | markings: the straight arrow is consistent
                        with the lane boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive over the solid white line on the right. [[IN-6(6)]]
Step 5  Rule            arrow:straight: The arrow allows me to proceed straight ahead. [null]
Step 6  change_left     allowed (correct): allowed by the dashed white lane line and [IN-6(1)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        [IN-6(6)]
Step 6  go_straight     allowed (correct): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable as there is no left-turn
                        arrow in my lane
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as there is no right-turn
                        arrow in my lane
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as there is no U-turn arrow
                        in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane to go straight. You may change to the left lane if needed, but do
                        not cross the solid line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 749, 13.65 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with
                        traffic signals. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car and further ahead. Photo 2 shows a
                        white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car and further ahead. Photo 2 shows a
                        white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed lines fit the role of lane lines | markings: the straight-ahead arrow is
                        consistent with the lane boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: A straight-ahead arrow allows the vehicle to proceed straight through
                        the intersection. [null]
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary and [IN-6(1)]
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary and [IN-6(1)]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow in the lane
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        left turn
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        right turn
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as no marking governs this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, change to the
                        corresponding outer lanes.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 722, 12.94 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, with buildings and trees
                        lining the sides. The road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        confirms a solid white line immediately to the left of the car, extending forward.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right side of the road.
                        Photo 2 shows a series of white dashes and gaps immediately to the right of the car.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white solid line as a lane line and white dashed line as an edge line are
                        consistent with standard road markings. | markings: No markings were observed in the
                        lane. | unseen: No attributes were reported that were not seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the dashed white line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right if necessary; do not cross the solid white line
                        to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 824, 12.87 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with shops on both sides, heading towards a straight stretch
                        of road. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; both boundaries are edge lines, meaning my lane is the
                        only lane of my direction here. | roles: the white solid lines fit the role of edge
                        lines for a single-lane road. | markings: there are no markings in my lane to
                        contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white left boundary [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary
                        [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          prohibited: prohibited by the solid white boundaries [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 6489, out 652, 10.34 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road continues
                        straight ahead with no immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating the road from a parking/shoulder area on
                        the right. Photo 2 shows a white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not cross the white solid line to overtake.
                        [[IN-6(4)]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white lane line and
                        [IN-6(1)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict it
Step 6  turn_left       not_applicable: not_applicable as no arrows govern this action
Step 6  turn_right      not_applicable: not_applicable as no arrows govern this action
Step 6  u_turn          not_applicable: not_applicable as no arrows govern this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 659, 12.71 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward on a road with buildings on
                        both sides. The road ahead appears to be a standard urban street with no immediate
                        intersection or ramp visible. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line along the left edge of the road next to the curb. Photo 2
                        confirms a single solid yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line between my car and the oncoming traffic. Photo 2 also
                        shows no painted line on the right side of the lane.
                        none none, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left edge line and the right center line (implied by oncoming traffic). |
                        roles: the yellow solid edge line on the left fits the role of a curb-side boundary. |
                        markings: no markings present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A vehicle shall not be parked where there is a continuous yellow line
                        painted on the carriageway on the kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule provided for an unmarked center line; standard
                        driving rules apply.
Step 6  change_left     prohibited (contested, label not_determined): prohibited by the solid yellow edge line
                        and the presence of a curb [IN-6(6)]
Step 6  change_right    allowed (WRONG, label not_determined): allowed as there is no painted line or physical
                        barrier governing this action
Step 6  go_straight     allowed (contested, label not_determined): allowed as no marking restricts carrying on
                        straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or intersection is present
Step 6  turn_right      not_applicable: not_applicable as no arrow or intersection is present
Step 6  u_turn          allowed: allowed as there is no continuous solid line to prohibit it [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line to the left as it
                        is the edge of the roadway.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 6489, out 836, 17.19 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right edge of the road. Photo 2 shows a white
                        solid line next to my car, continuing straight ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a lane line, and the white solid line
                        fits the role of an edge line. | markings: No markings were found in my lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid white line to the right.
                        [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the white dashed lane line and rule
                        [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the white solid edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings in my lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        my lane.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        my lane.
Step 6  u_turn          not_applicable: Not applicable as there are no markings governing U-turns in this
                        stretch.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area ahead of or next to my
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 860, 13.24 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward. There is a yellow box junction
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a curb and a dashed white line along the edge of the road. Photo 2 shows
                        the same dashed white line next to the car, with several dashes and gaps visible.
                        white dashed, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a curb and a dashed white line along the right edge of the road. Photo 2
                        shows the dashed white line next to the car, with several dashes and gaps visible.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show a yellow box with a cross inside it across
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The edge of the road is marked; crossing it would mean leaving the
                        roadway. [null]
Step 5  Rule            right_boundary: The edge of the road is marked; crossing it would mean leaving the
                        roadway. [null]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road.
                        [[IN-22.(1)viii]]
Step 6  change_left     prohibited (contested, correct): governed by left_boundary; no rule prohibits it but
                        it is an edge line with a curb
Step 6  change_right    prohibited (WRONG, label not_determined): governed by right_boundary; no rule
                        prohibits it but it is an edge line with a curb
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop inside the yellow box junction
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 664, 23.51 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides. Ahead is a straight stretch of
                        road with a bus in the distance. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line separating the lane from a bicycle lane, and a
                        double yellow line at the edge of the road. Photo 2 shows the white dashed line next
                        to the car, consisting of long dashes and gaps.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating the lane from a parking area. Photo 2
                        shows the white dashed line next to the car, consisting of long dashes and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed line allows crossing for lane changes. [null]
Step 5  Rule            right_boundary: A dashed line allows crossing for lane changes. [null]
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white line
                        (special_lane_line) and the absence of a prohibiting rule.
Step 6  change_right    allowed (correct): allowed by the dashed white line (edge_line) and the absence of a
                        prohibiting rule.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no turn arrows or intersection markings in
                        view.
Step 6  turn_right      not_applicable: not_applicable as there are no turn arrows or intersection markings in
                        view.
Step 6  u_turn          not_applicable: not_applicable as there are no markings governing U-turns in this
                        stretch.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may proceed straight or change lanes across the dashed
                        lines if safe to do so.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 773, 12.01 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with a pedestrian crossing
                        and traffic signals ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road, separating the lane
                        from the sidewalk. Photo 2 confirms a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a cycle lane or parking area
                        on the right. Photo 2 shows a solid white line next to the car, which then forms a
                        triangular shape further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; it is a single lane bounded by edge lines. | roles: the white solid
                        lines fit the role of edge lines for a single-lane road. | markings: there are no
                        markings in the lane to contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white edge line prohibits crossing into the sidewalk. [null]
Step 5  Rule            right_boundary: The solid white edge line prohibits crossing into the adjacent area.
                        [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line and curb
                        (IN-6(6))
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line (IN-6(6))
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          prohibited: prohibited by the solid white edge lines (IN-8(3)(a)(iv))
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 6489, out 653, 10.88 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, with shops and buildings on
                        both sides. The road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the curb/parking area. Photo
                        2 shows a white solid line next to my car, and a red line further to the right near
                        the curb.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (2) agree with the boundaries: a lane line on the left and an edge line on the right.
                        | roles: the white dashed line fits the role of a lane line, and the white solid line
                        fits the role of an edge line. | markings: no markings in my lane to check. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid white line to the right.
                        [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white lane line and rule
                        [IN-6(1)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and rule
                        [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 699, 12.44 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with shops on the left, approaching an intersection. (lanes
                        2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and double yellow lines along the edge of the road. Photo
                        2 confirms the raised curb and the double yellow lines next to the car.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the right lane. Photo 2
                        shows a white dashed line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane.;
                        symbol:bike (full): Photo 2 shows a bicycle symbol painted in my lane, slightly ahead
                        of the arrow.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a curb and edge line on the left and a lane line on the
                        right indicate I am in the leftmost lane of a two-lane road. | roles: the yellow
                        double solid edge line and white dashed lane line fit their roles. | markings: the
                        straight arrow and bike symbol are consistent with a lane that allows going straight.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: Lane changes are allowed after giving a proper signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The arrow allows the car to go straight.
Step 5  Rule            symbol:bike: This is an informative marking indicating a cycle lane or shared space
                        and does not govern the seven actions.
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb and solid yellow edge
                        lines [IN-6(6)]
Step 6  change_right    allowed (contested, correct): allowed by the white dashed lane line [IN-6(1)]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable as there is no left-turn
                        arrow and the left boundary is a curb
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as there is no right-turn
                        arrow in my lane
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as there is no U-turn arrow
                        and it would require crossing a curb or lane line
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane to go straight. You may change to the right lane if needed, but do
                        not cross the left boundary as it is a curb with no-parking markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6489, out 1034, 16.15 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. There is an
                        intersection ahead with a pedestrian crossing. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the road edge/shoulder.
                        Photo 2 shows the same white broken line next to my car, with long dashes and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white transverse line across the road ahead of
                        the intersection, which is a pedestrian crossing.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a lane_line on the left and an edge_line on the right. |
                        roles: White dashed lines are consistent with both lane_line and edge_line roles. |
                        markings: The pedestrian crossing is consistent with the urban road environment. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: I shall drive within the lane and may change lanes after giving a
                        proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: A dashed edge line allows moving onto the shoulder/edge if safe and
                        not prohibited by other rules. [null]
Step 5  Rule            line:crosswalk: I shall give way to pedestrians at the crossing. [[IN-8(2)(e)]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed lane line, which permits
                        lane changes per [IN-6(1)].
Step 6  change_right    allowed (correct): allowed: the right boundary is a dashed edge line, which does not
                        prohibit leaving the lane.
Step 6  go_straight     allowed (contested, correct): allowed: no markings in my lane restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: there is no turn arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable: there is no turn arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable: there is no marking governing U-turns in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: there is no waiting area ahead of or next to my
                          lane.
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes. Be prepared to give way to pedestrians at
                        the crosswalk ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6489, out 950, 14.77 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road continues
                        straight ahead with buildings on both sides. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the curb on the right. Photo 2 shows a white
                        solid line and a raised curb forming the right edge of the road.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        with a curb fits the role of an edge line | markings: no markings in my lane to check
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid white line on the right.
                        [[IN-6(6)]]
Step 6  change_left     allowed (correct): allowed by the white dashed lane line and rule [IN-6(1)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line and rule
                        [IN-6(6)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 691, 13.25 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, heading towards a straight
                        stretch of road with buildings and a cinema on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to a raised curb and metal railing. Photo 2
                        confirms a white solid line immediately adjacent to a raised stone curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle with the number '20'
                        painted on the road surface in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        next to a curb fits the role of an edge line. | markings: the speed limit marking is
                        consistent with a standard urban lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I shall drive within the lane and may change lanes after giving a
                        proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid longitudinal line. [[IN-6(6)]]
Step 5  Rule            text:speed_limit: This is an informative marking indicating the speed limit and does
                        not govern the seven actions.
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed lane line, which permits
                        lane changes according to [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid line and
                        a curb, which prohibits crossing according to [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight, and the
                        boundaries do not restrict this movement.
Step 6  turn_left       not_applicable: not_applicable: there are no turn arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_right      not_applicable: not_applicable: there are no turn arrows or prohibited-movement
                        markings in my lane.
Step 6  u_turn          not_applicable: not_applicable: there are no markings governing U-turns in this
                        stretch, though the right boundary is solid.
Step 6  enter_waiting_areanot_applicable: not_applicable: there is no left-turn waiting area or two-way left-
                          turn lane present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid line on the right. Observe the 20 mph speed limit.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:speed_limit'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6489, out 1020, 19.96 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a T-junction or intersection ahead. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a grey curb separating the road from a sidewalk. Photo 2 shows the same
                        grey curb with a raised edge next to the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from a parking area or another
                        lane. Photo 2 shows a white dashed line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; a curb on the left and a dashed line on the right indicate a single
                        lane of travel in this direction. | roles: the white dashed line fits the role of a
                        lane line. | markings: no markings present in the lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway; driving over it is prohibited
                        by general road rules.
Step 5  Rule            right_boundary: Lane changes across the dashed line are allowed after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the physical curb (left_boundary).
Step 6  change_right    allowed (correct): allowed by the white dashed line (right_boundary) and rule
                        [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as no arrows govern this movement.
Step 6  turn_right      not_applicable: not_applicable as no arrows govern this movement.
Step 6  u_turn          allowed: allowed as there is no solid line prohibiting it at this location.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a single lane bounded by a curb on the left and a dashed line on the right.
                        You may change lanes to the right or proceed straight.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right', 'u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 6489, out 655, 8.62 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with shops on both sides, driving forward. The road ahead
                        appears clear with no immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a sidewalk on the left. Photo 2 confirms the raised
                        curb immediately next to the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a wide open asphalt area to the right with parked cars further ahead,
                        but no painted lines next to the car. Photo 2 shows no painted lines or curbs on the
                        right side of the lane.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the left boundary being a curb and the right boundary being an open edge. |
                        roles: The left boundary is a physical curb (edge_line) and the right is an unmarked
                        road edge (edge_line), which fits a single-lane road configuration. | markings: There
                        are no markings in the lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The physical curb prohibits leaving the lane to the left.
Step 5  Rule            right_boundary: No painted line or curb exists to prohibit changing to the right,
                        though general safety rules apply.
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb (left_boundary).
Step 6  change_right    allowed (correct): allowed as there is no marking or curb governing this action
                        (right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  u_turn          allowed: allowed as there are no solid lines prohibiting it.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the lane or move right if needed; avoid the curb on the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation none, contradictions ['change_right decided
                        with nothing marked on that side', 'u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 6489, out 661, 11.18 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, with buildings and shops on
                        both sides. The road continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, separating the driving lane from a
                        parking/stopping area where cars are parked. Photo 2 confirms a solid white line
                        immediately to the left of the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right, separating my lane from another lane
                        of traffic. Photo 2 shows a series of white dashes and gaps immediately to the right
                        of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a solid white edge line on the left and a dashed lane line on the
                        right indicate the car is in the leftmost driving lane of a two-lane road. | roles:
                        the white solid line on the left fits the role of an edge line for a parking area, and
                        the white dashed line on the right fits the role of a lane line. | markings: no
                        markings are present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across a broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the dashed lane line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right lane if needed. Do not cross the solid
                        white line on the left into the parking area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 707, 12.96 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving in a lane that is to the
                        right of a bus lane. The road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a single solid white line next to my car and continuing ahead.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a special lane line on the left and a lane line on the right
                        place my car in the second lane from the left. | roles: the solid white line correctly
                        identifies the boundary of a special lane (bus lane), and the dashed white line
                        correctly identifies a lane boundary. | markings: no markings are present in my lane.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: My car may not drive in the bus lane to the left. [[IN-6(3)]]
Step 5  Rule            right_boundary: I may change lanes to the right after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            left_boundary: I shall not drive over the solid white line. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)] and the
                        bus lane restriction [IN-6(3)]
Step 6  change_right    allowed (correct): allowed by the dashed white line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right if needed. Do not enter the bus lane to your
                        left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6489, out 719, 13.49 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road in the UK. The road ahead is straight with no
                        immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, separating the lane from a
                        sidewalk. Photo 2 shows the same white line next to my car, which is solid.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white zigzag line on the right side of the lane. Photo 2 shows the
                        zigzag pattern clearly next to my car.
                        white zigzag, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both left and right. | roles: the white solid line on the left
                        and white zigzag line on the right both fit the role of edge lines. | markings: there
                        are no markings in my lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white edge line and curb prohibit leaving the lane to the
                        left. [null]
Step 5  Rule            right_boundary: The zigzag edge line indicates a restriction on stopping or parking,
                        but does not govern lane changes for a moving vehicle in this context. [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line and curb
                        (left_boundary).
Step 6  change_right    allowed (contested, label prohibited): allowed as there is no solid line or curb
                        prohibiting it, though it is an edge boundary.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area exists.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the left boundary into the
                        sidewalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 650, 23.59 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with a
                        right-turn lane. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a raised curb and fence. Photo 2 confirms a
                        solid white line and a raised curb immediately to the right of my lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2 shows a white arrow pointing to the right in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a lane line on the left and an edge line on the right indicate my
                        lane is the second of two lanes. | roles: the white dashed line fits the role of a
                        lane line, and the white solid line with a curb fits the role of an edge line. |
                        markings: the right-turn arrow is consistent with the lane being a dedicated turn lane
                        at the edge of the road. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive over the solid white line or the curb. [[IN-6(6)]]
Step 5  Rule            arrow:merge_right: I shall remain in this lane while taking a right turn.
                        [[IN-8(2)(c)]]
Step 6  change_left     allowed (correct): allowed by the dashed white lane line and [IN-6(1)]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and [IN-6(6)]
Step 6  go_straight     prohibited (correct): prohibited by the right-turn arrow which restricts the lane to
                        right turns only
Step 6  turn_left       prohibited (correct): prohibited by the right-turn arrow
Step 6  turn_right      allowed (correct): allowed by the right-turn arrow and [IN-8(2)(c)]
Step 6  u_turn          prohibited: prohibited by the right-turn arrow
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated right-turn lane. To go straight or turn left, you must change
                        to the left lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:right']), actions True, unsafe [], citation
                        unlisted, contradictions ['go_straight, turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 6489, out 774, 14.13 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road continues
                        straight ahead with parked cars on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane on the left. Photo
                        2 confirms a solid white line immediately to the left of the car.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane to the right.
                        Photo 2 shows a white dash and gap immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a special lane line on the left and a lane line on the right
                        place the car in the second lane from the left. | roles: the solid white line on the
                        left correctly identifies the boundary of a special lane (bus lane), and the dashed
                        white line on the right correctly identifies a lane line. | markings: no markings are
                        present in my lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across a broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line [IN-6(6)] and the
                        fact that it is a bus lane [IN-6(3)].
Step 6  change_right    allowed (correct): allowed by the dashed white line [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no markings governing this movement in the
                        visible stretch.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane or move to the right lane if needed. Do not enter the bus
                        lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6489, out 864, 13.94 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, driving straight ahead. The road is
                        a single carriageway with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a single yellow line along the left edge of the road. Photo 2 confirms a
                        single solid yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a single white line separating the driving lane from a parking area.
                        Photo 2 shows a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the word 'BUS' painted in yellow in the lane. Photo 1
                        shows the word 'BUS' and a dashed line further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides | roles: the yellow edge line on the left and white
                        edge line on the right fit the role of roadway boundaries | markings: the 'BUS' text
                        indicates this is a bus lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: A solid white edge line marks the boundary of the driving lane.
Step 5  Rule            text:bus: No vehicle of any other class than the specified class (bus) shall be driven
                        in this lane. [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow edge line and curb
                        [IN-6(6)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [IN-6(6)]
Step 6  go_straight     prohibited (contested, label allowed): prohibited because the lane is marked for buses
                        only [IN-6(3)]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          prohibited: prohibited by the solid boundaries [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a bus lane; as an ordinary car, you are prohibited from driving in this
                        lane. You should move out of this lane if possible, though the boundaries here
                        prohibit lane changes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions False, unsafe [], citation unlisted,
                        contradictions ['go_straight, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 6489, out 763, 14.04 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
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
                        fits the role of an edge line. | markings: No markings were observed in the lane. |
                        unseen: No | result: consistent
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
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 872, 14.0 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road ahead
                        appears clear with no immediate intersection or ramp. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white solid line separating my lane from a bus lane. Photo 2 confirms
                        a white solid line immediately to the left of my car, extending forward.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with clear dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my position (2nd
                        from left) agree with the boundaries: a special lane line on the left and a lane line
                        on the right. | roles: the white solid line on the left fits the role of a special
                        lane boundary (bus lane), and the white dashed line on the right fits the role of a
                        lane line. | markings: no markings are present in my lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes after giving a proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the white solid line [IN-6(6)]
Step 6  change_right    allowed (correct): allowed by the white broken line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Do not enter the bus lane to your left, as
                        it is bounded by a solid white line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 6489, out 825, 12.78 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides, heading towards a distant
                        intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road next to the curb.
                        Photo 2 confirms a single solid yellow line immediately to the left of my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right side of the lane, only the asphalt surface.
                        Photo 2 also shows no painted line to the right of my car.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left edge line and the absence of a right boundary line. | roles: the yellow
                        solid edge line on the left fits the role of an edge line next to a curb. | markings:
                        there are no markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side; it does not prohibit driving within the lane. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule governs the absence of a marking on the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow line [IN-6(6)] and
                        [IN-6(4)]
Step 6  change_right    allowed (WRONG, label not_determined): allowed as there is no marking or curb
                        governing this action
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          prohibited: prohibited by the solid yellow line [IN-8(3)(a)(iv)]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right if necessary; do not cross the yellow line on the
                        left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 6489, out 669, 11.26 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in the UK, with a street lined by shops
                        and buildings. Ahead is a clear stretch of road with parked cars on the right. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left that is broken near the car and becomes solid
                        further ahead. Photo 2 shows a white broken line with long dashes and gaps next to the
                        car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a physical curb and a white line separating the lane from a parking
                        area. Photo 2 shows a white solid line and a raised concrete curb next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; a lane line on the left indicates another lane of the same direction,
                        and an edge line on the right indicates the road boundary. | roles: the white dashed
                        line on the left fits the role of a lane line, and the white solid line with a curb on
                        the right fits the role of an edge line. | markings: no markings are present in the
                        lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white lane line and rule
                        [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        in the lane.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        in the lane.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the solid line on
                        the right into the parking area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 6489, out 882, 16.96 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward. The road continues
                        straight ahead with buildings on both sides. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle containing the number
                        '20' painted in the middle of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries. | roles: the white
                        dashed patterns fit the role of lane lines. | markings: the speed limit marking is
                        consistent with a standard travel lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I may change lanes to the right after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            text:speed_limit: This is an informative marking indicating a speed limit and does not
                        govern the seven actions. [null]
Step 6  change_left     allowed (contested, correct): allowed by the white dashed left boundary and rule
                        [IN-6(1)]
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary and rule [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and the
                        lane does not end
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes as needed, observing the 20 mph speed limit indicated on the road.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 6489, out 771, 13.71 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides, approaching a stretch with
                        zigzag markings on the road. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line that starts as a straight line and then becomes a zigzag
                        pattern. Photo 2 shows the white zigzag line next to the car.
                        white zigzag, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line that starts as a straight line and then becomes a zigzag
                        pattern. Photo 2 shows the white zigzag line next to the car.
                        white zigzag, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; the left boundary is an edge line and the right is a
                        lane line, meaning there is another lane to the right. | roles: the white zigzag lines
                        are consistent with edge and lane markings in this context. | markings: no markings in
                        my lane to conflict with boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The edge line and curb prohibit leaving the roadway to the left.
Step 5  Rule            right_boundary: The driver shall not drive on or over a longitudinal solid line, which
                        includes the solid segments of the zigzag line. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the curb and edge line.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid segments of the zigzag line
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing straight.
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this.
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this.
Step 6  u_turn          prohibited: prohibited by the solid segments of the zigzag line [IN-8(3)(a)(iv)].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the zigzag lines to change lanes
                        or make a U-turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right', 'u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 6489, out 664, 12.08 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward. The road ahead is a straight
                        stretch with parked vehicles on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows no painted line on the left, only the side of a red bus. Photo 2 shows
                        no painted line on the left, only the side of the red bus.
                        none none, curb no, other, evidence full
Step 2  Right           Photo 1 shows a yellow line along the right edge of the road near the curb. Photo 2
                        shows a single solid yellow line next to the car and further ahead.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; there
                        is no left boundary line and a right edge line, consistent with a single-lane road |
                        roles: the yellow solid line on the right fits the role of an edge line (curb side) |
                        markings: no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: no specific rule for a missing boundary on the left
Step 5  Rule            right_boundary: parking is prohibited where there is a continuous yellow line on the
                        kerb side [[IN-22.(2)(j)]]
Step 6  change_left     allowed (correct): no marking governs this action
Step 6  change_right    prohibited (contested, correct): [IN-6(6)] prohibits driving over a solid line
Step 6  go_straight     allowed (contested, correct): no marking restricts carrying on straight
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          prohibited: [IN-8(3)(a)(iv)] prohibits U-turns across a continuous solid line
Step 6  enter_waiting_areanot_applicable: no waiting area exists
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line on the right or
                        attempt a U-turn across it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['change_left decided
                        with nothing marked on that side', 'u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 6489, out 636, 10.98 s
```
