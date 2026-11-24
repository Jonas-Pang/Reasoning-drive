# Reasoning of lane run 20261117_231805_laneC_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus and a bicycle lane. An intersection is ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car and a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a bicycle symbol in the lane to the left. Photo 1
                        shows a bicycle symbol in the lane to the left.; area:grid (full): Photo 2 shows a
                        white box with a diagonal line through it in the lane to the right. Photo 1 shows this
                        same marking.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line on the left and a white solid line
                        on the right. | roles: The white dashed line on the left and white solid line on the
                        right fit the roles of lane lines. | markings: The bicycle symbol is in the leftmost
                        lane, and the grid marking is in the rightmost lane, consistent with the layout. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may cross the dashed line to
                        overtake after signaling. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            symbol:bike: No specific rule provided for the bike symbol in the adjacent lane.
                        [null]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road (applies to
                        the grid area in the right lane). [[IN-22.(1)viii]]
Step 6  change_left     allowed (correct): allowed by the dashed left boundary [IN-6(1)]
Step 6  change_right    prohibited (correct): prohibited by the solid right boundary [IN-6(4)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if necessary, but you must stay within your current
                        lane and are prohibited from moving into the right lane. Proceed straight ahead
                        through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:stop_line']), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 1040, 9.86 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction or pedestrian crossing ahead. My car is in a
                        lane that appears to be narrowing or merging into a central area. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a solid white line near my car, which then becomes a dashed white line
                        further ahead as it approaches a junction area.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on my right. Photo 2 shows this line is a solid white line
                        near my car, which then becomes a dashed white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2 shows a white triangle pointing forward in the center of
                        the lane ahead.
Step 4  Cross-check     close_up: The same in both photos. | position: The lane count and my lane position
                        agree with the boundary roles. The white lines on both sides define my lane. | roles:
                        The white solid/dashed lines correctly function as lane lines. | markings: The
                        triangle symbol is centered in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: I must drive within my lane and can only change lanes after signaling.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I must drive within my lane and can only change lanes after signaling.
                        [[IN-6(1)]]
Step 5  Rule            symbol:other: No specific rule for this triangle symbol is provided.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay within your lane as the solid lines near your car prohibit lane changes. You may
                        proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 6666, out 842, 7.37 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a city street with a multi-lane road ahead. There is a pedestrian
                        crossing and a bicycle lane ahead of the car. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; symbol:bike (full): Photo 1 shows a bicycle symbol in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle lane, index 2) agree with the white lines on both sides. | roles: The white
                        solid lines correctly function as lane lines between lanes of the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane's purpose. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to change lanes.
                        [[IN-6(4)]]
Step 5  Rule            arrow:straight: The driver shall use this lane for going straight. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 884, 8.36 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops on the left and buildings on the right. The road
                        ahead appears to be a straight stretch with a cycle lane on the left. (lanes 2, mine
                        2, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from a cycle lane. Photo 2 shows
                        the same double yellow line clearly.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a single white dashed line to my right. Photo 2 shows the same white
                        dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane in
                        Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a yellow edge line is on my left and a white lane line is
                        on my right. | roles: The yellow double solid line correctly acts as an edge line for
                        the cycle lane, and the white dashed line acts as a lane divider. | markings: No
                        markings were found in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the double longitudinal solid
                        yellow line. [IN-6(6)]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [IN-6(1)]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay within your lane. You may change to the right if safe, but you must not cross the
                        double yellow lines on your left into the cycle lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions True, unsafe [], citation
                        unlisted, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 6666, out 815, 8.82 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is approaching a city intersection with a pedestrian crossing. The road ahead
                        narrows into a single lane before the crossing. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left. Photo 2 shows a white line on the left that is
                        solid near the car and becomes a broken line further ahead before the intersection.
                        white solid_dashed (near line solid), curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right that
                        is solid near the car and becomes a broken line further ahead before the intersection.
                        white solid_dashed (near line solid), curb yes, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows white lines forming a box-like shape (grid) ahead of
                        the car.; line:crosswalk (full): Photo 1 shows a white pedestrian crossing (zebra)
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego lane (1)
                        agree with the boundaries: a white line on the left (edge line) and a white line on
                        the right (lane line). | roles: The white lines correctly identify the edge of the
                        road and the division between lanes. | markings: The grid area and crosswalk are
                        consistent with an approaching intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for white edge lines in this context.
Step 5  Rule            right_boundary: The driver shall drive within the lane. [IN-6(1)]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road (applies to
                        grid areas to prevent blocking junctions). [IN-22.(1)viii]
Step 5  Rule            line:crosswalk: The driver shall stop before the stop line preceding the pedestrian
                        crossing if a red light is shown. [IN-12(1)(a)]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your lane as you approach the intersection. Do not enter the grid area to
                        avoid blocking the junction, and be prepared to stop for pedestrians at the crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 975, 8.54 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with houses on the left and a sidewalk. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double red line on the left. Photo 2 shows the same double red line
                        clearly next to the car.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows the same white dashed
                        line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 shows a yellow 'BUS' marking and a yellow arrow in the lane
                        to the right.; arrow:merge_right (full): Photo 1 shows a yellow arrow pointing right
                        in the lane to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a double red line on the left (edge) and a white
                        dashed line on the right (lane line). | roles: The double red line correctly
                        identifies the left edge, and the white dashed line correctly identifies the right
                        lane boundary. | markings: The 'BUS' marking and right arrow are in the lane to the
                        right, not in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for double red lines in the provided text,
                        but they typically indicate a prohibition on stopping.
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        signaling. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change into the right lane.
                        Changing into the left lane is prohibited by the double red lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:merge_right', 'text:bus'], missed []), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 6666, out 872, 8.67 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a sidewalk/fence on the left.
                        The road ahead appears to be a straight stretch with multiple lanes of traffic. (lanes
                        4, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows the same solid white line clearly next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the lane to my right. Photo
                        2 shows this dashed white line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in
                        the lane to my right.; arrow:left (full): Photo 2 shows a white arrow pointing left in
                        the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2nd
                        from left) are consistent with the boundaries: a white line on my left and a dashed
                        line on my right. | roles: The white solid line on the left and dashed line on the
                        right are consistent with lane markings in a multi-lane road. | markings: The straight
                        arrow in my lane is consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may only change lanes after
                        signaling. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver may cross the broken line to overtake but must return to
                        the lane. [[IN-6(7)]]
Step 5  Rule            arrow:straight: The driver shall use this lane for straight movement. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight ahead movement. You may change into the lane
                        on your right as it is marked with a dashed line, but you should not cross the solid
                        white line to your left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions True, unsafe [], citation
                        unlisted, contradictions ['turn_left not_applicable although an arrow shows it']
Tokens                  in 6666, out 977, 9.01 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops and buildings on the right. The road ahead has
                        several lanes of traffic moving in the same direction as my car. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a white bicycle symbol in the lane to my left. Photo
                        2 shows a white bicycle symbol in the lane to my left.; symbol:bike (full): Photo 1
                        shows a white bicycle symbol in the lane to my left. Photo 2 shows a white bicycle
                        symbol in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The bicycle symbols are in the leftmost lane, which is
                        consistent with the lane markings for a cycle lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary [IN-6(1)]
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as needed, provided you signal and ensure safety. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 925, 8.25 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian crossing and a small traffic island ahead.
                        My car is in a lane that appears to be a dedicated turn lane or a lane leading to a
                        junction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line on the left. Photo 2 shows a white line on the left that is
                        solid near the car and becomes dashed further ahead. There is a raised curb to the
                        left of this line.
                        white solid_dashed (near line solid), curb yes, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right that
                        is solid near the car and becomes dashed further ahead. There is a small traffic
                        island/curb to the right of this line.
                        white solid_dashed (near line solid), curb yes, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows white lines forming a box-like shape or a dedicated
                        area ahead of my car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries. The lane is bounded by white lines on both sides. |
                        roles: The white lines correctly function as lane boundaries. | markings: The grid-
                        like markings ahead of my car define a specific area, likely a box junction or a
                        dedicated turn area. | unseen: none | result: consistent
Step 5  Rule            left_boundary: I must drive within the lane and only change lanes after signaling.
                        [IN-6(1)]
Step 5  Rule            right_boundary: I must drive within the lane and only change lanes after signaling.
                        [IN-6(1)]
Step 5  Rule            area:grid: I must not be stopped on the yellow box (or similar grid marking) if it
                        blocks traffic. [IN-22.(1)viii]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid part of the left boundary
                        line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid part of the right boundary
                        line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       allowed: allowed as no markings prohibit it
Step 6  turn_right      allowed: allowed as no markings prohibit it
Step 6  u_turn          allowed: allowed as no markings prohibit it
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay within your lane as the solid lines on both sides prohibit lane changes. Be
                        prepared to stop if the grid area ahead becomes congested.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:crosswalk']), actions None, unsafe [], citation unlisted,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 6666, out 750, 7.78 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test C | no answer
---------------------------------------------------------------------------------------------
Error                   The answer is incomplete (max_output_tokens). Raise api.max_output_tokens.

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops and pedestrians on the left. Ahead, there is a
                        junction or a wide area with multiple turn lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line as a solid white line near the car, which then becomes a dashed white line
                        further ahead. There is a red-painted curb on the far left.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line as a dashed white line near the car and further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:merge_left (full): Photo 2 shows a white arrow pointing left in the lane
                        to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line is on my left and a white line is on
                        my right. | roles: The white lines correctly function as lane lines between lanes of
                        the same direction. | markings: The straight arrow in my lane is consistent with the
                        lane's role and the surrounding markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken part of the line to overtake but must
                        return to the lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The driver shall use this lane while proceeding straight.
                        [[IN-8(1)(c)]]
Step 6  change_left     allowed (contested, correct): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left or right if safe, but you should not turn left from this lane as it is marked for
                        straight movement.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:merge_left', 'arrow:straight'], missed ['arrow:straight_left']), actions
                        False, unsafe [], citation unlisted, contradictions ['change_left allowed with the
                        solid line of a solid-and-broken pair nearer my lane']
Tokens                  in 6666, out 942, 13.55 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a sidewalk and buildings on the left and a sidewalk on
                        the right. There is a cyclist ahead in the lane to the left of mine. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (full): Photo 1 shows a white circular marking with a left
                        turn arrow on the road to the right of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle lane) is consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The two-way left-turn lane marking is to the right of my lane,
                        which is consistent with the road layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver may cross the broken line to overtake but must return to
                        the lane. [[IN-6(7)]]
Step 5  Rule            area:two_way_left_turn_lane: No specific rule provided for this marking in the list.
Step 6  change_left     allowed (correct): The left boundary is a broken line, which allows for a lane change
                        under [IN-6(7)].
Step 6  change_right    allowed (correct): The right boundary is a broken line, which allows for a lane change
                        under [IN-6(7)].
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the lane markings are dashed. No specific turn markings are present in your
                        lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 6666, out 768, 8.07 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian area on the left and a sidewalk on the
                        right. Ahead, there is a junction with turn lanes and a pedestrian crossing. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a red line on the left. Photo 2 shows two parallel red lines on the
                        left.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 1 shows a white arrow pointing straight ahead with a
                        small left-turn branch in my lane.; arrow:left (full): Photo 1 shows a white arrow
                        pointing left in the lane to my right.; arrow:right (full): Photo 1 shows a white
                        arrow pointing right in the lane to my right.
Step 4  Cross-check     close_up: The close-up confirms the double red line on the left and the white dashed
                        line on the right. The markings are consistent. | position: The lane count of 3 and my
                        position as 2 (middle) is consistent with the red edge line on the left and the white
                        dashed lane line on the right. | roles: The red line acts as an edge line (left) and
                        the white dashed line acts as a lane line (right). | markings: The straight-left arrow
                        in my lane is consistent with the lane's position and the surrounding turn lanes. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for red lines, but it functions as a
                        physical/painted edge of the roadway.
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        signaling. [[IN-6(1)]]
Step 5  Rule            arrow:straight_left: The driver shall use this lane while taking a left turn.
                        [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       allowed (correct): allowed
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane which allows you to go straight or turn left. You may
                        change into the right lane if necessary, but you should not change into the left area
                        marked by the red lines. Do not attempt to turn right from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions ['turn_right prohibited although an arrow shows it']
Tokens                  in 6666, out 998, 9.03 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street approaching a junction or a narrowing point. There are
                        buildings on both sides and a cyclist ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left. Photo 2 shows a white line on the left near
                        the car and a white line further ahead that appears to be part of a zigzag pattern.
                        white zigzag, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right near
                        the car and a white line further ahead that appears to be part of a zigzag pattern.
                        white zigzag, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show white zigzag lines across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries. The left boundary is an edge line (curb), and the
                        right boundary is a lane line. | roles: The white zigzag lines are consistent with a
                        restricted area or a specific road marking (like a pedestrian crossing approach). |
                        markings: The zigzag lines are consistent with the road layout. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: No specific rule provided for white zigzag edge lines in the provided
                        text.
Step 5  Rule            right_boundary: No specific rule provided for white zigzag lane lines in the provided
                        text.
Step 5  Rule            area:grid: No specific rule provided for zigzag markings in the provided text.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not attempt to change lanes as the zigzag
                        markings indicate a restricted area ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed ['line:crosswalk']), actions None, unsafe [], citation none,
                        contradictions []
Tokens                  in 6666, out 843, 8.92 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on both sides. The road ahead appears to be a
                        straight stretch with multiple lanes for traffic moving in the same direction. (lanes
                        3, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a red-painted line on the left edge. Photo 2 shows a
                        raised curb and a red-painted line on the left edge.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a white arrow in my lane pointing straight
                        ahead with a small branch to the left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (1)
                        are consistent with the left edge line and the right lane line. | roles: The red edge
                        line and white dashed lane line fit their roles as an edge line and a lane-change line
                        respectively. | markings: The straight-left arrow is consistent with the lane's
                        position and the dashed right boundary. | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for red edge lines, but it defines the
                        boundary of the roadway.
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes across the
                        dashed line after signaling. [[IN-6(1)]]
Step 5  Rule            arrow:straight_left: The driver shall use this lane while taking a left turn or going
                        straight as indicated by the arrow. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       allowed (correct): allowed
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You can proceed straight or turn left as indicated by
                        the lane markings. You may change into the lane to your right, but you are prohibited
                        from changing into the area to your left as it is bounded by a curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 734, 7.88 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is approaching a city intersection with a pedestrian crossing. The road ahead
                        has multiple lanes and a pedestrian crossing in the middle of the junction. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left. Photo 2 shows a white line on the left that is
                        solid near the car and becomes dashed further ahead.
                        white solid_dashed (near line solid), curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right that
                        is solid near the car and becomes dashed further ahead.
                        white solid_dashed (near line solid), curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white pedestrian crossing (zebra crossing)
                        ahead of my lane.; line:stop_line (full): Photo 1 shows a white line marking the end
                        of the lane before the crossing.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree with
                        the boundaries; the white lines on both sides indicate the edge of the roadway. |
                        roles: The white lines correctly function as edge lines for the lane. | markings: The
                        crosswalk and stop line are consistent with an approaching intersection. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: No specific rule for this edge line is provided in the list. [null]
Step 5  Rule            right_boundary: No specific rule for this edge line is provided in the list. [null]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians before turning left.
                        [IN-8(1)(f)]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians. [IN-8(2)(e)]
Step 5  Rule            line:stop_line: The vehicle shall stop before the stop line preceding the pedestrian
                        crossing. [IN-12(1)(a)]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     stop_first (contested, label allowed): stop_first
Step 6  turn_left       stop_first: stop_first
Step 6  turn_right      stop_first: stop_first
Step 6  u_turn          stop_first: stop_first
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before the white line at the pedestrian crossing.
                        Give way to any pedestrians crossing the road before proceeding in any direction.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 6666, out 986, 8.74 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bus lane on the left. My car is in the lane
                        to the right of the bus lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the bus lane. Photo 2 shows a
                        solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a red-painted line on the far right edge of the road. Photo 2 shows a
                        red-painted line next to my car and a red-painted line further ahead.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show 'BUS LANE' text and a bus symbol in the lane
                        to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white line on my left separates me from the bus lane, and
                        a red line on my right marks the edge. | roles: The white line is a lane line and the
                        red line is an edge line. | markings: The 'BUS LANE' marking is in the lane to my
                        left, which is consistent with the white line boundary. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to enter the bus lane.
                        [[IN-6(4)]]
Step 5  Rule            right_boundary: no marking governs this action [no marking governs this action]
Step 5  Rule            text:bus: No other vehicle of any other class shall be driven in the bus lane.
                        [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line and the bus lane
                        marking.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the red edge line and curb.
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane. Changing left into the bus lane is prohibited by the solid
                        white line and the bus lane markings. The red line on your right indicates the edge of
                        the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 911, 8.49 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane on the left and a general traffic lane for my
                        car. There is a cyclist ahead and a car parked or stopped on the right. (lanes 2, mine
                        2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the bus lane on the left.
                        Photo 2 shows this same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway or a divider for a parking/pedestrian area. Photo 2 shows this line clearly as
                        a solid white line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a bicycle symbol and a white circle with a bicycle
                        inside it in the lane to the left (the bus lane).; area:two_way_left_turn_lane
                        (partial): Photo 1 shows a white line and a bicycle symbol in the lane to the left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white line on my left separates me from the bus lane,
                        and a white line/curb on my right marks the edge. | roles: The white solid line on the
                        left acts as a lane line, and the white solid line on the right acts as an edge line.
                        | markings: The bicycle symbols are in the lane to the left, which is consistent with
                        it being a bus/cycle lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to enter the bus lane.
                        [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and not move onto the
                        curb/pedestrian area. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane. Do not attempt to move into the bus lane on your left or
                        onto the sidewalk on your right. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane', 'symbol:bike'], missed ['text:speed_limit']), actions
                        False, unsafe [], citation unlisted, contradictions []
Tokens                  in 6666, out 929, 8.09 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a pedestrian area on the left and a large truck on the
                        right. The road ahead shows multiple lanes with various markings and an intersection
                        or junction approaching. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a thick white line separating my lane from the lane to its left. Photo 2
                        shows this same white line clearly as a solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to its right. Photo 2
                        shows this line as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 1 shows a white arrow pointing left in the lane to my
                        left.; arrow:right (full): Photo 1 shows a white arrow pointing right in the lane to
                        my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle, index 2) agree with the white lane lines on both sides. | roles: The white
                        solid lines correctly function as lane lines between lanes of the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane's role and the
                        surrounding turn arrows. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            arrow:straight: The driver shall use this lane for going straight. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions ['turn_left prohibited although an arrow shows it',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 6666, out 943, 8.86 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test C | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a central lane
                        approaching a set of markings and a white van. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the one to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the one to my right. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in the lane to my left.;
                        arrow:straight (full): Photo 1 shows a white straight-ahead arrow in my lane.;
                        arrow:right (full): Photo 1 shows a white right-turn arrow in the lane to my right.;
                        area:grid (full): Photo 2 shows a white 'KEEP CLEAR' box (grid) ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's role. The grid ahead is a
                        'KEEP CLEAR' area. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            arrow:straight: The driver shall use this lane for going straight. [[IN-8(1)(c)]]
Step 5  Rule            area:grid: The driver shall not be stopped on the yellow box (or equivalent grid)
                        marked on the road. [[IN-22.(1)viii]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Do not change lanes or turn, as
                        the solid white lines and lane arrows restrict these movements.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid', 'arrow:left', 'arrow:right'], missed ['line:stop_line']), actions False,
                        unsafe [], citation unlisted, contradictions ['turn_left prohibited although an arrow
                        shows it', 'turn_right prohibited although an arrow shows it']
Tokens                  in 6666, out 1056, 9.19 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight stretch with multiple lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a dashed white line near my car and becomes a solid white line further
                        ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a dashed white line near my car and remains dashed further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:left_turn_waiting (insufficient): Photo 2 shows a white line marking a lane
                        boundary to the left, but no arrows or words are visible in my lane.
Step 4  Cross-check     close_up: The left boundary is dashed near the car and solid further ahead in Photo 1;
                        Photo 2 confirms the dashed pattern near the car. The right boundary is dashed in
                        both. | position: The lane count of 3 and my position as 2 (middle) is consistent with
                        the white lane lines on both sides. | roles: The white lines correctly function as
                        lane lines between lanes of the same direction. | markings: No specific markings are
                        clearly visible in my lane to contradict the boundaries. | unseen: None | result:
                        consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as needed, but
                        ensure you signal and check for safety. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:left_turn_waiting'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 858, 8.57 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops and trees on both sides. A bus and a van are
                        visible ahead in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car and a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line next to my car and a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows a white dashed line marking a box or area in the
                        center of the road.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle lane) is consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The grid area is consistent with the road layout. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road (interpreted
                        as the grid area here). [[IN-22.(1)viii]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the white dashed left_boundary
                        [IN-6(1)]
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as needed, but ensure you do not stop on the grid markings in the center of the
                        road.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 915, 8.34 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight stretch with a clear view of the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line as a broken white line near the car and a solid white line further ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line as a broken white line near the car and a solid white line further ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2 shows a thick white transverse line across the lane.
Step 4  Cross-check     close_up: The close-up (Photo 2) clearly shows the dashed pattern near the car and the
                        solid pattern further ahead for both boundaries. The stop line is clearly visible in
                        Photo 2. | position: The lane count of 3 and my position as lane 2 (middle) are
                        consistent with the white lane lines on both sides. | roles: The white lines correctly
                        function as lane lines separating traffic moving in the same direction. | markings:
                        The stop line is consistent with the urban setting and the lane's position. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver may cross the broken line to overtake but must return to
                        the lane. [[IN-6(7)]]
Step 5  Rule            line:stop_line: The driver shall stop before crossing the transverse stop line.
                        [[IN-7(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     stop_first (contested, label allowed): stop_first
Step 6  turn_left       stop_first: stop_first
Step 6  turn_right      stop_first: stop_first
Step 6  u_turn          stop_first: stop_first
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the immediate
                        markings are broken. However, you must come to a complete stop at the white transverse
                        line before proceeding with any movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 6666, out 917, 8.42 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with buildings on both sides. The road ahead appears to be a
                        multi-lane urban street with parked cars on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries (left edge line, right lane line). | roles: The yellow
                        edge line on the left and white dashed lane line on the right fit their roles. |
                        markings: No markings are present to contradict the boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a yellow edge line in this context, but
                        it defines the road boundary. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        signaling. [IN-6(1)]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed: allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left lane of the roadway. You may proceed straight or change into the
                        right lane. Changing to the left is prohibited as it is the road edge.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 777, 7.62 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane on the left and a dedicated lane for the car
                        on the right. Ahead, there is a pedestrian crossing and a bus stop area. (lanes 3,
                        mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a dashed white line next to my car and remains dashed further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a dashed line separating
                        my lane from a lane or area to the right. Photo 2 shows this line is a dashed white
                        line next to my car and remains dashed further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows a large white 'BUS' marking in the lane to the left of
                        my lane.; line:crosswalk (full): Photo 1 shows a white pedestrian crossing (zebra
                        crossing) ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white dashed line is on my left (separating me from the
                        bus lane) and a white dashed line is on my right (separating me from the far right
                        lane/area). | roles: The white dashed lines correctly function as lane lines. |
                        markings: The 'BUS' marking is in the lane to the left, which is consistent with the
                        lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            text:bus: No other vehicle of any other class shall be driven in that lane.
                        [[IN-6(3)]]
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the main traffic flow. You may change lanes to the
                        left or right as needed, but avoid entering the lane marked 'BUS' on your left.
                        Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk', 'text:bus'], missed []), actions True, unsafe [], citation
                        unlisted, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 6666, out 980, 8.31 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings on both sides. A bus is visible ahead in the distance.
                        The road has a marked area in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a sidewalk on the left. Photo 2 shows a raised curb
                        and a sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows a yellow box with a cross in it in the middle of the
                        lane.; text:bus (full): Photo 1 and Photo 2 show text 'BUS LANE' on the right side of
                        the road.
Step 4  Cross-check     close_up: the same in both photos | position: A lane line on the right and a curb on
                        the left agree with my lane being the leftmost lane of my direction (lane 1). | roles:
                        The curb acts as an edge line and the white line acts as a lane line separating my
                        lane from the bus lane. | markings: The grid area is in my lane, and the 'BUS LANE'
                        text is in the adjacent lane to the right. | unseen: none | result: consistent
Step 5  Rule            left_boundary: no passage covers this element
Step 5  Rule            right_boundary: The driver shall drive within the lane. [[IN-6(1)]]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road.
                        [[IN-22.(1)viii]]
Step 5  Rule            text:bus: No other vehicle of any other class shall be driven in that lane.
                        [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane and do not enter the bus lane to your right. Do not stop on
                        the yellow box grid ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 938, 13.28 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bicycle lane on the left and parked cars on the right.
                        A red bus is visible ahead in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the bicycle lane. Photo 2 shows a
                        solid white line next to the car and a dashed white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line next to the car and a dashed white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a bicycle symbol and a white line on the far left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle lane) is consistent with the white lane lines on both sides. | roles: The
                        white lines correctly function as lane lines separating my lane from the bicycle lane
                        on the left and the adjacent lane on the right. | markings: The bicycle symbol is in
                        the lane to the left, not in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as the solid lines on both sides prohibit lane changes.
                        Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 816, 7.57 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a junction or a pedestrian crossing
                        area. There are buildings and trees on both sides. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left. Photo 2 shows a white line on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows white diagonal lines forming a box-like pattern ahead
                        of the car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree; the
                        left boundary is an edge line (curb) and the right is a lane line. | roles: The white
                        solid lines correctly define the lane boundaries. | markings: The grid markings are
                        consistent with a junction/crossing area. | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for white edge lines, but it defines the left
                        limit of the roadway.
Step 5  Rule            right_boundary: The driver shall not drive on or over the solid white line.
                        [[IN-6(6)]]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box, and by extension, grid
                        markings often indicate areas to keep clear. [[IN-22.(1)viii]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay within your lane as the right boundary is a solid line. Proceed straight ahead,
                        ensuring you do not stop on the grid markings ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 660, 7.52 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops on both sides. The road ahead appears to continue
                        straight with a slight curve or intersection in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway or a boundary to a sidewalk/curb. Photo 2 shows this solid white line clearly
                        next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:left_turn_waiting (insufficient): No markings are visible in my lane in Photo 1
                        or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a dashed line on my left separates me from another
                        lane, and a solid line on my right marks the edge of the road. | roles: The white
                        dashed line on the left correctly functions as a lane line, and the solid white line
                        on the right correctly functions as an edge line. | markings: No markings were
                        observed in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The edge line defines the boundary of the drivable roadway. [no
                        passage]
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if safe, but you should
                        not move to the right as it is the edge of the road. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 845, 9.84 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a sidewalk on the left and a bicycle lane on the right.
                        Ahead, there is a junction or a change in road layout with various lane markings.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line and a raised curb on the left. Photo 2 shows a solid
                        white line and a raised curb on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a straight ahead arrow in my lane.; symbol:bike
                        (full): Photo 2 shows a bicycle symbol in the lane to the right.; arrow:left (full):
                        Photo 2 shows a left-turn arrow in the lane to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: an edge line on the left and a lane line on the right.
                        | roles: The white solid lines correctly define the edge of the roadway and the
                        separation from the right-hand lane. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose. The bicycle symbol and left turn arrow are in the
                        adjacent lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The edge line and curb define the left limit of the roadway. [null]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [IN-6(4)]
Step 5  Rule            arrow:straight: The arrow indicates that this lane is intended for straight-ahead
                        movement. [null]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed ['line:stop_line']), actions True, unsafe [], citation
                        unlisted, contradictions ['turn_left prohibited although an arrow shows it']
Tokens                  in 6666, out 936, 8.62 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a pedestrian crossing and a bus stop ahead. My car is
                        in a lane heading straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white dashed line across the lane ahead,
                        indicating a pedestrian crossing area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The crosswalk markings are consistent with the urban setting and the lane's
                        path. | unseen: none | result: consistent
Step 5  Rule            left_boundary: I am allowed to change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I am allowed to change lanes to the right after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            line:crosswalk: No specific rule provided for the crosswalk marking itself, but it
                        indicates a pedestrian area.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary [IN-6(1)]
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change lanes to the left or right as needed, provided you
                        signal. Be mindful of the pedestrian crossing ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 878, 8.4 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch with a junction or pedestrian crossing area visible in the distance.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line as a broken white line near the car and a solid white line further ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white stop line or yield line across the lane
                        further ahead.
Step 4  Cross-check     close_up: The left boundary is a dashed line near the car and solid further ahead in
                        both photos. The right boundary is solid in both. The stop line is visible in both. |
                        position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white lines correctly function as lane
                        lines separating lanes of the same direction. | markings: The stop line is consistent
                        with the approach to a junction/crossing. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to overtake.
                        [[IN-6(4)]]
Step 5  Rule            line:stop_line: The driver shall stop before crossing the transverse stop line.
                        [[IN-7(1)(a)]]
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     stop_first (contested, label allowed): stop_first
Step 6  turn_left       stop_first: stop_first
Step 6  turn_right      stop_first: stop_first
Step 6  u_turn          stop_first: stop_first
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if necessary, but you are
                        prohibited from changing to the right lane. You must come to a full stop at the white
                        line before proceeding with any movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 6666, out 905, 6.92 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrianized area or sidewalk to the right. There is
                        an intersection or junction ahead with some road markings and a pedestrian crossing.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white line next to my car and a white line further ahead. The line next to my car is
                        a solid white line. The line further ahead is a dashed white line.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a solid line. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead. There is
                        a raised curb and a metal fence to the right of this line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a bicycle symbol in the lane to my right. Photo 2
                        shows a bicycle symbol in the lane to my right.; line:stop_line (full): Photo 1 shows
                        a white line across the lane ahead. Photo 2 shows a white line across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on my left and a white line/curb on
                        my right. | roles: The white solid/dashed line on the left is a lane line; the white
                        solid line on the right with a curb is an edge line. | markings: The bicycle symbol is
                        in the adjacent lane, not my lane. The stop line is ahead of my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: no marking governs this action [no marking governs this action]
Step 5  Rule            line:stop_line: The driver shall stop before the stop line. [[IN-12(1)(a)]]
Step 6  change_left     allowed (correct): allowed by the broken part of the solid_dashed line [IN-6(7)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid edge line and curb
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the stop line [IN-12(1)(a)]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane as the line becomes
                        broken, but you must stop at the white line ahead before proceeding straight.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line', 'symbol:bike'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions ['change_left allowed with the solid line of a solid-and-
                        broken pair nearer my lane']
Tokens                  in 6666, out 1036, 8.44 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A residential street with a wide paved area ahead, possibly a small square or a wide
                        junction. My car is positioned in a lane facing forward. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a double dashed line on the left. Photo 2 shows a
                        raised curb and a double dashed line on the left.
                        white double_dashed, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a single white dashed line on the right. Photo 2 shows a single white
                        dashed line on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the boundaries: a curb/edge line on the left and a lane line on the right.
                        | roles: The white dashed lines and curb correctly identify the left edge and the
                        right lane divider. | markings: The straight arrow in my lane is consistent with the
                        lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule for a white dashed edge line and curb in this context.
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        signaling. [IN-6(1)]
Step 5  Rule            arrow:straight: The driver shall use this lane for straight movement. [IN-8(1)(c)]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. You may change to the right if
                        necessary, but you should not turn left, turn right, or perform a U-turn as indicated
                        by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 845, 7.2 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops on both sides. The road ahead appears to be a
                        continuous stretch of road with some parked cars and pedestrians. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white line next to my car and a white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a raised curb and a white line on the right. Photo 2 shows a raised curb
                        and a white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:keep_clear (full): Photo 2 shows a white 'KEEP CLEAR' text and a white box
                        marking in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white dashed line on my left indicates another lane
                        of my direction, and a white solid line with a curb on my right indicates the edge of
                        the roadway. | roles: The white dashed line on the left fits the role of a lane line,
                        and the white solid line with a curb on the right fits the role of an edge line. |
                        markings: The 'KEEP CLEAR' marking is consistent with the lane's position and the
                        surrounding urban environment. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The edge line and curb define the boundary of the roadway. [no
                        passage]
Step 5  Rule            text:keep_clear: The 'KEEP CLEAR' marking indicates that the area should not be
                        blocked by vehicles. [no passage]
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-lane road. You may change into the left lane
                        if safe, but you must not move onto the pavement or curb on your right. Ensure you do
                        not block the 'KEEP CLEAR' area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:keep_clear'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 923, 8.15 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and sidewalks on both sides. The road ahead
                        appears to be a straight stretch with multiple lanes for traffic moving in the same
                        direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car and a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway or a boundary to a sidewalk/cycle lane. Photo 2 shows a solid white line next
                        to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) is consistent with a dashed line on the left and a solid line on the
                        right. | roles: The white dashed line on the left correctly identifies a lane-line,
                        and the solid white line on the right correctly identifies an edge-line. | markings:
                        No markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: No specific rule for this edge line is provided in the list. [null]
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed lane line on the left
                        [IN-6(1)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if safe and signaled, but
                        you should not move to the right as it is the edge of the roadway. Proceed straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 874, 8.9 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bus lane on the left. The car is positioned
                        in the lane to the right of the bus lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the bus lane. Photo 2 shows
                        the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the lane to the right. Photo
                        2 shows the same dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows 'BUS LANE' text and a bus symbol in the lane to my
                        left.; area:grid (full): Photo 2 shows a white line and a yellow-bordered area marking
                        the start of the bus lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on my left separates me from the bus
                        lane, and a dashed line on my right separates me from the next lane. | roles: The
                        solid white line on the left correctly acts as a lane divider, and the dashed line on
                        the right correctly acts as a lane-change line. | markings: The 'BUS LANE' text and
                        symbols are correctly identified in the lane to the left, not in my lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to enter the bus lane.
                        [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver may cross the broken line to overtake or change lanes, but
                        must return to the lane. [[IN-6(7)]]
Step 5  Rule            text:bus: Only buses are permitted to drive in the lane marked 'BUS LANE'. [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You can move to the right lane if needed, but you must not
                        move into the bus lane on your left as it is marked with a solid line and 'BUS LANE'
                        text.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid', 'text:bus'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 775, 8.53 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a sidewalk and parked cars on the left. Ahead, the road
                        narrows or changes configuration with complex white markings. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a solid white line near the car, which then becomes a broken white line
                        further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line is a solid white line
                        near the car, which then becomes a broken white line further ahead.
                        white solid_dashed (near line solid), curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): Photo 1 and Photo 2 show white zigzag lines across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries (lane to the left, edge line to the right). | roles:
                        The white lines and curb correctly define the lane boundaries. | markings: The zigzag
                        lines are consistent with the road layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: no marking governs this action [none]
Step 5  Rule            symbol:other: no marking governs this action [none]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid line near the car,
                        prohibiting a lane change.
Step 6  change_right    prohibited (contested, correct): The right boundary is a curb, prohibiting a lane
                        change.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your current lane as the left boundary is solid near you and the right side is
                        bounded by a curb. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 687, 11.13 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane that appears to
                        be a dedicated turn lane or a lane leading to a turn. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white line next to my car and a white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a raised curb and a metal fence on the right. Photo 2 shows a raised
                        curb and a paved sidewalk area on the right.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 2 shows a white arrow pointing left in the lane to my left.
                        Photo 2 shows a white arrow pointing right in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree. The white line on my left separates me from the leftmost lane. The curb on my
                        right defines the edge of the roadway. | roles: The white solid line correctly acts as
                        a lane line, and the curb acts as an edge line. | markings: The right-turn arrow in my
                        lane is consistent with the lane's purpose and the right-hand boundary (curb). |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the white solid line to overtake or change
                        lanes. [[IN-6(4)]]
Step 5  Rule            right_boundary: no marking governs this action [no marking governs this action]
Step 5  Rule            arrow:right: The driver shall remain in this lane while taking a right turn.
                        [[IN-8(2)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     prohibited (correct): prohibited
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      allowed (correct): allowed
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated right-turn lane. You must remain in this lane and perform a
                        right turn at the upcoming intersection. Lane changes to the left or straight ahead
                        are prohibited by the solid line and the lane markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['leftmost lane, but
                        a lane line on the left']
Tokens                  in 6666, out 895, 8.76 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a bus lane on the left and a central median. The car is
                        positioned in a lane to the right of the bus lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the bus lane. Photo 2 shows a
                        solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show 'BUS LANE' text in the lane to the left of
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines. | markings: The 'BUS LANE' text is clearly in the
                        lane to the left, not in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid white line separating
                        my lane from the bus lane. [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over the solid white line separating
                        my lane from the lane to the right. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay within your current lane as both the left and right boundaries are solid white
                        lines. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 802, 7.41 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings and trees on both sides. The road ahead appears to be a
                        multi-lane urban street with parked cars on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows a solid white line on the
                        left, which is the edge of the roadway next to a sidewalk/curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line on the right. Photo 2 shows a dashed white line on
                        the right, separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the word 'BUS' in large yellow letters painted in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the boundaries: a white edge line is on my left and a dashed lane line is
                        on my right. | roles: The white solid line on the left acts as an edge line, and the
                        dashed line on the right acts as a lane line. | markings: The 'BUS' text indicates a
                        special lane, which is consistent with the edge line on the left and the lane line on
                        the right. | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a white edge line, but it defines the
                        boundary of the roadway.
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            text:bus: No other vehicle of any other class shall be driven in that lane.
                        [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     prohibited (contested, label allowed): prohibited
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  This is a bus lane; you should not drive in this lane unless you are driving a bus. If
                        you must move, you may change to the right, but you should not proceed straight or
                        turn from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed ['text:other']), actions True, unsafe [], citation unlisted,
                        contradictions ['go_straight, turn_left, turn_right, u_turn decided without an arrow
                        or prohibited-movement marking']
Tokens                  in 6666, out 904, 9.12 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops and pedestrians on both sides. The road ahead
                        appears to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken (dashed) line near the car and a solid line
                        further ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line as a solid white
                        line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: The left boundary is dashed near the car and solid further ahead in both
                        photos. The right boundary is solid in both. | position: The lane count of 3 and my
                        position as 2 (middle) is consistent with a lane line on my left and an edge line on
                        my right. | roles: The white dashed/solid line on the left acts as a lane divider, and
                        the white solid line on the right acts as an edge line. | markings: No markings are
                        present to contradict the boundaries. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken line to overtake but must return to the
                        lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The edge line defines the boundary of the drivable roadway. [no
                        marking governs this action]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken line near the car
                        [IN-6(7)]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change into the left lane to overtake as the line
                        is broken near your car, but you must return to your lane. Do not move to the right as
                        it is the edge of the road.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 872, 9.02 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane on the left and a parking area on the right.
                        The car is positioned in a lane in the middle of the road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the bus lane. Photo 2 shows a solid
                        white line next to the car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line next to the car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows 'BUS LANE' text and a bus symbol in the lane to the
                        left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries. A white line on the left separates me from the bus
                        lane, and a white line on the right separates me from the lane with the white van. |
                        roles: The white solid lines correctly function as lane lines between lanes of the
                        same direction. | markings: The 'BUS LANE' marking is in the lane to the left, which
                        is consistent with the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to enter the bus lane.
                        [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not cross the solid white line to enter the lane to
                        the right. [[IN-6(4)]]
Step 5  Rule            text:bus: Only buses are allowed to drive in the lane marked for a special purpose.
                        [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane. Lane changes to the left into the bus lane or to the right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 6666, out 899, 7.7 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch with some lane markings and a bicycle lane on the left. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car and a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line next to my car and a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a white bicycle symbol in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle lane) is consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The bike symbol is in the leftmost lane, which is consistent
                        with the layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the white dashed left_boundary
                        [IN-6(1)]
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as needed, and you are permitted to proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 855, 8.15 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops and trees on both sides. The road ahead appears
                        to be a straight stretch with a central divider or median area. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a solid line separating
                        my lane from a parking area or a sidewalk. Photo 2 shows this line as a solid white
                        line next to a raised curb/island.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree; the
                        white line on my left separates me from another lane, and the white line on my right
                        marks the edge of the roadway. | roles: The white solid line on the left acts as a
                        lane line, and the white solid line on the right with a curb acts as an edge line. |
                        markings: No markings are present in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the white solid line to overtake another
                        vehicle. [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over the solid line or the curb.
                        [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay within your lane as the solid white lines on both sides prohibit lane changes.
                        Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 6666, out 825, 7.55 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings on both sides. The road ahead has multiple
                        lanes with speed limit markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is solid near the car and becomes dashed further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line is dashed near the car and remains dashed further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a '20' speed limit circle in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) is consistent with a lane line on my left and a lane line on my right. |
                        roles: The white lines correctly function as lane lines between lanes of the same
                        direction. | markings: The speed limit marking is centered in my lane. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The driver may cross the broken part of the line to overtake but must
                        return to the lane. [[IN-6(7)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        signaling. [[IN-6(1)]]
Step 5  Rule            text:speed_limit: No specific rule passage provided for speed limit markings, but it
                        indicates a maximum speed.
Step 6  change_left     allowed (contested, correct): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as needed, but
                        ensure you signal and check for safety. Maintain a speed of 20 mph or less as
                        indicated by the road marking.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['change_left allowed
                        with the solid line of a solid-and-broken pair nearer my lane']
Tokens                  in 6666, out 865, 8.94 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops on both sides. Ahead, the road narrows into a
                        central area with zigzag markings, likely a pedestrian crossing or a restricted zone.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line as a solid white line near the car, which then becomes a zigzag pattern
                        further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this as a solid white line near
                        the car, which also becomes a zigzag pattern further ahead.
                        white solid_dashed (near line solid), curb yes, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 and Photo 2 show white zigzag lines across the road
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2,
                        the rightmost lane) agree with the boundaries: a white line is on my left and a white
                        line/curb is on my right. | roles: The white lines correctly function as a lane
                        divider on the left and an edge line on the right. | markings: The zigzag markings
                        (channelizing) are consistent with the narrowing of the road ahead. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: no marking governs this action [no marking governs this action]
Step 5  Rule            area:channelizing: no marking governs this action [no marking governs this action]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as the white lines on both sides indicate a designated path.
                        Proceed straight ahead, but be aware of the zigzag markings which indicate a
                        restricted area or pedestrian crossing ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 882, 8.46 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test C | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane on the left and a general traffic lane on the
                        right. A red double-decker bus is in the bus lane, and a silver van is in the lane to
                        the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the bus lane. Photo 2 shows
                        this same solid white line clearly next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line and a raised curb on the right. Photo 2 shows the
                        solid yellow line and the curb clearly.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white dashed line in the middle of my lane, and
                        a white arrow pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2,
                        the right lane) agree with the boundaries: a white line on my left separates me from
                        the bus lane, and a yellow line/curb on my right marks the edge. | roles: The white
                        solid line correctly acts as a lane line, and the yellow solid line with a curb
                        correctly acts as an edge line. | markings: The straight arrow and dashed line in my
                        lane are consistent with a standard through-lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The driver shall not cross the solid white line to enter the bus lane.
                        [[IN-6(4)]]
Step 5  Rule            right_boundary: The driver shall not park on the yellow line side of the road.
                        [[IN-22.(2)(j)]]
Step 5  Rule            arrow:straight: The driver should use this lane for straight movement. [[IN-8(1)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Do not attempt to change lanes to the left
                        into the bus lane or to the right onto the curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6666, out 906, 8.52 s
```
