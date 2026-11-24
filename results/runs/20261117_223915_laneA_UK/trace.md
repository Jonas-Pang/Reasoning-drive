# Reasoning of lane run 20261117_223915_laneA_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street with multiple lanes of traffic. Ahead, there is a junction with a bus
                        and a bicycle lane marking. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a bicycle symbol and a bicycle lane marking to the
                        left of my lane.; area:grid (full): Photo 1 shows a white dashed line and a white
                        solid line forming a box-like area to the right of my lane, which appears to be a turn
                        lane or a separate lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The bicycle symbol is in the lane to the left, and the grid-
                        like markings are to the right, consistent with the lane layout. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            symbol:bike: Indicates a dedicated lane for bicycles.
Step 5  Rule            area:grid: Indicates a restricted area or a specific lane configuration ahead.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You can move into the left or right lanes as needed, as
                        both boundaries are dashed. Proceed straight ahead into the junction.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:stop_line']), actions False, unsafe ['change_right'],
                        citation None, contradictions []
Tokens                  in 3819, out 956, 7.93 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with an intersection ahead. My car is in a lane that
                        appears to be a dedicated turn lane or a lane leading into a junction. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is solid white near the car and becomes dashed further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is solid white near the car and becomes dashed further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 1 shows a white triangle pointing forward in the center of
                        my lane.; area:grid (full): Photo 1 shows white lines forming a box/grid area ahead of
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the white lane lines on both sides. | roles: The white lines correctly
                        function as lane lines between lanes of the same direction. | markings: The triangle
                        and grid markings are consistent with a junction approach. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid portion prohibits lane changes to the left, while the dashed
                        portion allows them.
Step 5  Rule            right_boundary: The solid portion prohibits lane changes to the right, while the
                        dashed portion allows them.
Step 5  Rule            symbol:other: The triangle is a directional indicator but does not strictly govern
                        lane movements.
Step 5  Rule            area:grid: The grid indicates a keep clear or junction area.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as lane changes are prohibited by the solid lines
                        immediately ahead. Proceed straight toward the junction, observing the grid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid', 'symbol:other'], missed ['line:crosswalk']), actions None, unsafe [],
                        citation None, contradictions []
Tokens                  in 3819, out 923, 8.25 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street with an intersection ahead. My car is in a lane with multiple markings
                        and a bicycle lane to its right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from a bicycle lane. Photo 2 shows a
                        white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; symbol:bike (full): Photo 1 shows a white bicycle symbol in the lane to my
                        right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating my lane from others. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the bicycle lane to the
                        right.
Step 5  Rule            arrow:straight: The arrow indicates that going straight is the intended movement for
                        this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to proceed straight ahead. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 845, 7.64 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with shops on the left and buildings on the right.
                        The road ahead appears to continue straight. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line on the left. Photo 2 shows a double yellow line on
                        the left.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a double yellow edge line is on my left and a white
                        lane line is on my right. | roles: The double yellow line correctly identifies the
                        left edge of the roadway, and the white line separates my lane from the lane to my
                        right. | markings: No markings are present to contradict the boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The double yellow line indicates a no-parking/no-waiting zone at the
                        edge of the road.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the right are prohibited by
                        the solid white line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 782, 6.79 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with an intersection ahead. My car is in a lane approaching a
                        pedestrian crossing and a junction. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left. Photo 2 shows a white line on the left.
                        white solid_dashed (near line dashed), curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white pedestrian crossing (zebra crossing)
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1,
                        leftmost) agree with the boundaries: a white line on my left is an edge line (curb
                        present), and a white line on my right is a lane line. | roles: The white solid-dashed
                        lines correctly identify the edge of the roadway on the left and the lane divider on
                        the right. | markings: The crosswalk is consistent with the intersection ahead. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The edge line prohibits moving further to the left onto the sidewalk.
Step 5  Rule            right_boundary: The dashed line allows for a lane change to the right.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires the driver to yield to pedestrians.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (contested, label prohibited): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the right lane if needed. Be prepared to stop
                        for pedestrians at the zebra crossing ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 818, 7.22 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with traffic keeping to the left. Ahead, there is a
                        continuous stretch of road with some vehicles and a sidewalk on the left. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and double red lines on the left. Photo 2 shows the same
                        double red lines and a raised curb clearly.
                        other solid_dashed (near line solid), curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows the same white dashed
                        line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows a yellow box marking on the right side of the road
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a red edge line is on my left and a white lane line is
                        on my right. | roles: The red lines correctly identify the left edge of the roadway,
                        and the white dashed line correctly identifies the right lane boundary. | markings:
                        The grid area is to the right of my lane and does not conflict with my lane's
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double red lines and curb prohibit stopping or parking on the left
                        side of the road.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            area:grid: The yellow box ahead requires that the area remains clear of stationary
                        vehicles.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left-hand lane. You may proceed straight or change to the right lane if
                        needed. Do not attempt to move further left as it is the edge of the roadway marked
                        with red lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 864, 8.76 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with buildings on the right and a sidewalk/fence on
                        the left. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 2 shows a white arrow pointing left in the lane to my
                        left.; arrow:right (full): Photo 2 shows a white arrow pointing right in the lane to
                        my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose and the solid
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed []), actions False, unsafe [],
                        citation None, contradictions ['turn_left prohibited although an arrow shows it',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 3819, out 905, 8.58 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street in the UK with traffic keeping to the left. There is a
                        bicycle lane on the far left and several lanes of traffic ahead. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a white bicycle symbol in the lane to my left.;
                        symbol:bike (full): Photo 1 shows a white bicycle symbol in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white dashed line is on my left and a white dashed line
                        is on my right. | roles: The white dashed lines correctly function as lane lines
                        between lanes of the same direction. | markings: The bicycle symbols are in the lane
                        to the left, which is consistent with the bicycle lane boundary. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as needed, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 866, 7.22 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian crossing and a small traffic island ahead.
                        My car is in a lane that appears to be a dedicated turn or stop area before a
                        crossing. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left. Photo 2 shows a white line on the left that is
                        solid near the car and becomes dashed further ahead. There is a raised curb to the
                        left of this line.
                        white solid_dashed (near line solid), curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right that
                        is solid near the car and becomes dashed further ahead. There is no curb on the right.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows a white line forming a box-like shape around the lane
                        area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent. The left boundary is an edge line (curb), and the right boundary is a lane
                        line separating my lane from the lane to its right. | roles: The white lines correctly
                        define the boundaries of the lane. | markings: The grid-like markings indicate a
                        restricted area or a specific lane configuration for the crossing. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The edge line and curb prohibit moving further to the left.
Step 5  Rule            right_boundary: The solid line near the car prohibits a lane change to the right.
Step 5  Rule            area:grid: The grid marking indicates a restricted area, typically for stopping or
                        keeping clear.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane. Lane changes to the left or right are prohibited by the
                        solid lines near your car. Proceed straight through the area, being mindful of the
                        pedestrian crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:crosswalk']), actions None, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 878, 7.47 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with a pedestrian crossing and a cycle lane on the
                        left. Ahead, there is a junction or a continuation of the road with a white van in the
                        lane directly ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white bicycle symbol inside a circle on the road
                        surface to the right of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white line on my left separates me from another lane,
                        and a white line on my right marks the edge of the roadway. | roles: The white solid
                        line on the left is a lane line, and the white solid line on the right is an edge
                        line. | markings: The bike symbol is in the adjacent lane, not my lane. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid white line marks the edge of the roadway and prohibits
                        moving onto the shoulder or sidewalk.
Step 5  Rule            symbol:bike: Indicates a cycle lane, which is not my lane.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:bike'], missed ['text:speed_limit']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 3819, out 861, 7.0 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with shops on the left and a sidewalk on the right. The road
                        ahead has multiple lanes and an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        a white line with some yellow dashed markings next to it.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:merge_left (full): Photo 2 shows a white arrow pointing left in the lane
                        to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries. The lane to the left has a left-turn arrow, and my
                        lane has a straight arrow. | roles: The white lines correctly define the lane
                        boundaries. | markings: The straight arrow in my lane matches the lane's purpose, and
                        the left arrow in the adjacent lane is consistent with its position. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid-dashed line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for going straight
                        ahead.
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid and solid-dashed lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:merge_left', 'arrow:straight'], missed ['arrow:straight_left']), actions
                        False, unsafe [], citation None, contradictions ['change_left prohibited with the
                        broken line of a solid-and-broken pair nearer my lane']
Tokens                  in 3819, out 688, 10.1 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK. The car is in a lane heading straight ahead, with a
                        sidewalk and buildings on the left and a sidewalk on the right. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a white circular marking with a bicycle symbol on
                        the right side of the road, ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The bike symbol is in a separate lane to the right and does not conflict
                        with my lane's boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            symbol:bike: Indicates a cycle lane or area for bicycles.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as needed, and you can proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 861, 8.15 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with an intersection ahead. My car is in the middle
                        lane of three lanes moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white straight arrow in my lane.; arrow:left
                        (full): Photo 1 shows a white left-turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle) is consistent with the white dashed lines on both sides. | roles: The white
                        dashed lines correctly function as lane lines between lanes of the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane's purpose. The
                        left turn arrow is in the adjacent lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for going straight
                        ahead.
Step 6  change_left     allowed (contested, label prohibited): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited by the arrow:straight marking
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left or right as needed, but you should not attempt to turn left or right from this
                        lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['arrow:straight_left']), actions False,
                        unsafe [], citation None, contradictions ['turn_left prohibited although an arrow
                        shows it']
Tokens                  in 3819, out 910, 7.4 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with a multi-lane layout approaching an intersection. My car
                        is in a lane that appears to be a dedicated cycle lane or a shared lane with specific
                        markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a solid white line next to my car, which then becomes a dashed white line
                        further ahead as it curves.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on my right. Photo 2 shows this line is a solid white line
                        next to my car, which then becomes a dashed white line further ahead as it curves.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows white zigzag lines on the left and right of my lane,
                        and a white line separating the lane from the one to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. I am in the middle lane of three lanes of traffic
                        moving in the same direction. | roles: The white lines correctly serve as lane lines
                        between lanes of the same direction. | markings: The zigzag lines and lane markings
                        are consistent with a designated area (likely a cycle lane or pedestrian-priority
                        zone) ahead of the intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid part of the line prohibits changing lanes to the left.
Step 5  Rule            right_boundary: The solid part of the line prohibits changing lanes to the right.
Step 5  Rule            area:grid: The zigzag markings indicate a pedestrian-priority zone where parking and
                        overtaking are restricted.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as lane changes are prohibited by the solid lines. Proceed
                        straight through the intersection, being mindful of the pedestrian-priority zone
                        marked by the zigzag lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:crosswalk']), actions None, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 898, 7.66 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with buildings on both sides. The road ahead
                        continues straight with multiple lanes of traffic. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a red line on the left. Photo 2 shows a raised curb
                        with a solid red line painted on the edge.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white dashed line next to my car and a white solid line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 1 and Photo 2 show a white arrow in my lane pointing
                        straight ahead and slightly to the left.
Step 4  Cross-check     close_up: The close-up confirms the red line and the dashed nature of the white line
                        next to my car. The arrow is clearly visible in both. | position: The lane count of 3
                        and my position as the leftmost lane (1) is consistent with the red line/curb on my
                        left and a lane line on my right. | roles: The red line acts as an edge line, and the
                        white dashed line acts as a lane divider. | markings: The straight-left arrow is
                        consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The red line and curb prohibit moving to the left.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes to the right.
Step 5  Rule            arrow:straight_left: The arrow allows going straight or turning slightly left, and
                        prohibits turning right or making a U-turn.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       allowed (correct): allowed
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or turn slightly left as indicated by the lane arrow. You may
                        change into the lane to your right, but you are prohibited from moving left across the
                        red line or turning right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 883, 8.44 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with an intersection ahead. My car is in a lane approaching a
                        pedestrian crossing and a junction. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left. Photo 2 shows a white line on the left near
                        the car and a white line further ahead.
                        white solid_dashed (near line dashed), curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right near
                        the car and a white line further ahead.
                        white solid_dashed (near line dashed), curb yes, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead and
                        slightly right in the lane ahead.; arrow:right (full): Photo 1 shows a white arrow
                        pointing right in the lane to the right.; line:stop_line (full): Photo 1 shows a white
                        line across the lane at the pedestrian crossing.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries (left edge line, right lane line). | roles: The white
                        solid-dashed lines correctly identify the left edge and the right lane divider. |
                        markings: The straight arrow in my lane and the stop line are consistent with the road
                        layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The edge line marks the boundary of the roadway.
Step 5  Rule            right_boundary: The dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to stop before the pedestrian
                        crossing.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (contested, label prohibited): allowed
Step 6  go_straight     stop_first (contested, label allowed): stop_first
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left-hand lane. You must come to a full stop at the white line before
                        the pedestrian crossing. You are permitted to go straight ahead or change into the
                        right lane, but turning left or right is prohibited by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:right', 'arrow:straight', 'line:stop_line'], missed ['line:crosswalk']),
                        actions None, unsafe [], citation None, contradictions ['change_right allowed across a
                        curb', 'turn_right prohibited although an arrow shows it']
Tokens                  in 3819, out 967, 8.76 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a dedicated bus lane on the left. My car is in the lane
                        to the right of the bus lane. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the bus lane. Photo 2 shows a
                        solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, and a red-painted curb/line further
                        right. Photo 2 shows a solid white line next to my car and a red line further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show 'BUS LANE' text and a bus symbol in the lane
                        to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree. The white line on my left separates me from the bus lane, and the white
                        line/red curb on my right marks the edge of the roadway. | roles: The white solid line
                        on the left is a lane line; the white solid line and red curb on the right are edge
                        lines. | markings: The 'BUS LANE' marking is in the lane to my left, which is
                        consistent with the solid white line separating it from my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the bus lane on the left.
Step 5  Rule            right_boundary: The solid white line and red curb prohibit moving onto the sidewalk or
                        area to the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight. Do not attempt to move into the bus
                        lane on your left or onto the sidewalk on your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 841, 7.81 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with a bus lane on the left and a bicycle lane
                        ahead. My car is in a lane next to the bus lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the bus lane. Photo 2 shows a
                        thick solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car. Further ahead, the line appears to end or transition near a bicycle lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (partial): Photo 1 shows a bicycle symbol and a circular
                        arrow symbol in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent. The white line on my left separates me from the bus lane, and the white
                        line on my right separates me from the bicycle lane. | roles: The white solid lines
                        correctly function as lane lines. | markings: The bicycle markings are in the lane to
                        the right, not in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the bus lane on the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the bicycle lane on the
                        right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane. Lane changes to the left into the bus lane or to the right
                        into the bicycle lane are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed ['text:speed_limit']), actions False, unsafe
                        [], citation None, contradictions []
Tokens                  in 3819, out 814, 6.68 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK with an intersection ahead. My car is in a lane
                        that appears to have a dedicated turn area or a specific lane configuration for
                        turning. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a solid white line near my car and becomes a dashed white line further
                        ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a dashed white line near my car and remains dashed further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in my lane.; arrow:right
                        (full): Photo 1 shows a white right-turn arrow in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. The white line on my left separates me from the
                        leftmost lane, and the white line on my right separates me from the rightmost lane. |
                        roles: The white lines correctly function as lane lines. | markings: The left-turn
                        arrow in my lane is consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid part of the line prohibits a lane change to the left, while
                        the dashed part allows it.
Step 5  Rule            right_boundary: The dashed line allows a lane change to the right.
Step 5  Rule            arrow:left: The arrow indicates that this lane is for turning left.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited
Step 6  turn_left       allowed (WRONG, label prohibited): allowed
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to turn left at the upcoming intersection. Lane changes to the left are
                        prohibited by the solid line, but a change to the right is permitted.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right'], missed ['arrow:straight']), actions False, unsafe
                        ['turn_left'], citation None, contradictions ['turn_right prohibited although an arrow
                        shows it']
Tokens                  in 3819, out 902, 8.38 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test A | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane that appears
                        to have a straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 2 shows a white arrow pointing left in the lane to my
                        left.; arrow:right (full): Photo 2 shows a white arrow pointing right in the lane to
                        my right.; text:only (full): Photo 2 shows a white line across the lane ahead of my
                        car with the word 'ONLY' written inside it.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2nd
                        from left) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The straight arrow in my lane matches the 'ONLY' marking ahead,
                        indicating a dedicated straight-through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that this lane is for going straight ahead.
Step 5  Rule            text:only: The 'ONLY' marking reinforces that the lane is designated for the movement
                        indicated by the arrow.
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to proceed straight ahead. Lane changes to the left or right are
                        permitted as the boundaries are dashed, but the lane is specifically designated for
                        straight-through traffic.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right', 'text:only'], missed ['line:stop_line']), actions True,
                        unsafe [], citation None, contradictions ['turn_left prohibited although an arrow
                        shows it', 'turn_right prohibited although an arrow shows it']
Tokens                  in 3819, out 1018, 7.54 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings and trees on both sides. The road ahead
                        appears to continue straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a dashed line (broken) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a dashed line (broken) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 1 shows a white line in the center of my lane,
                        but no arrows or words are visible in the lane itself.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: No specific arrows or words are present to contradict the lane boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes to the right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the lane markings are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 3819, out 809, 7.15 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops on both sides. The road ahead appears to be a
                        continuous stretch of road with multiple lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with short dashes and small gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line with short dashes and small gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 2 shows a white dashed line across the lane
                        ahead of my car, but no arrows or words are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle lane) is consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: No specific arrows or words are visible to govern movements. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the boundaries are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 3819, out 821, 7.28 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings and trees on both sides. The road continues
                        straight ahead into a distant urban area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 1 shows a white dashed line across the lane
                        ahead of my car, indicating a lane change area or a break in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle lane) is consistent with white dashed lines on both sides. | roles: The white
                        dashed lines correctly function as lane lines between lanes of the same direction. |
                        markings: The dashed line across the lane ahead is consistent with a lane-change or
                        lane-break area. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the boundaries are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 3819, out 821, 7.57 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with buildings on both sides. The road ahead appears to be a
                        multi-lane street with parked cars on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent. The yellow line on the left is the edge of the roadway, and the white
                        dashed line on the right separates my lane from the adjacent lane. | roles: The yellow
                        edge line and white dashed lane line fit their respective roles. | markings: No
                        markings are present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow line marks the edge of the roadway and prohibits
                        crossing onto the pavement.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed: allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or change into the right lane. Do not attempt to move
                        left across the solid yellow line.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3819, out 769, 7.04 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane on the left and a bike lane on the right. The
                        car is in a central lane heading straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 shows a
                        solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from a bike lane. Photo 2 shows a
                        dashed white line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows 'BUS LANE' text and a bus symbol in the lane to the
                        left.; symbol:bike (full): Photo 2 shows a white line and a bike symbol in the lane to
                        the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on the left separates me from the bus
                        lane, and a dashed line on the right separates me from the bike lane. | roles: The
                        white solid line on the left and dashed line on the right fit the roles of lane lines.
                        | markings: The 'BUS LANE' text and bike symbol are in the adjacent lanes, not my
                        lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the bus lane on the left.
Step 5  Rule            right_boundary: The dashed white line allows changing into the bike lane on the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane. Changing left into the bus lane is
                        prohibited by the solid line, but a lane change to the right is permitted by the
                        dashed line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike', 'text:bus'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 866, 7.86 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with a bus lane on the right and a grid-marked area ahead. My car is in
                        the lane to the left of the bus lane. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a sidewalk on the left. Photo 2 shows a raised curb
                        and a sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the bus lane. Photo 2 shows a
                        solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows a large white grid (box) with an X across it in the
                        middle of the road.; text:bus (full): Photo 1 shows 'BUS ONLY' text and a bus symbol
                        in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: A lane line on my right means another
                        lane of my direction on my right. A curb on my left means my lane is the leftmost of
                        my direction. | roles: The solid white line on the right correctly acts as a lane
                        line. The curb on the left correctly acts as an edge line. | markings: The grid area
                        is in my lane. The bus markings are in the adjacent lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The curb prohibits moving further to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the bus lane on the
                        right.
Step 5  Rule            area:grid: The grid area indicates a keep clear zone where vehicles should not stop.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Do not move into the bus lane on your right,
                        as it is restricted. Be mindful of the grid area ahead, which is a keep-clear zone.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 906, 11.84 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus and parked cars. The road ahead appears to be a
                        continuous stretch of urban road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to its left. Photo 2 shows
                        this same white line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to its right. Photo 2
                        shows this white line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a bicycle symbol and a white line on the far left,
                        but these are in the lane to my left, not my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle lane) is consistent with white dashed lines on both sides. | roles: The white
                        dashed lines correctly function as lane lines between lanes of the same direction. |
                        markings: No markings are present in my lane; the bike symbol is in the adjacent lane.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes to the right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white left_boundary
Step 6  change_right    allowed (correct): allowed by the dashed white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the lane markings are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 811, 6.67 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with a multi-lane layout. Ahead, there is a junction with
                        various lane markings and a white van parked or stopped on the right. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is solid and white near the car, then becomes dashed further ahead before
                        the junction.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is solid and white near the car, then becomes dashed further ahead before
                        the junction.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows white lines forming a box/grid pattern ahead of my
                        lane, indicating a keep clear or restricted area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the white lane lines on both sides. | roles: The white lines correctly
                        function as lane lines separating lanes of the same direction. | markings: The grid
                        markings are consistent with the junction layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid part of the line prohibits lane changes, while the dashed
                        part allows them.
Step 5  Rule            right_boundary: The solid part of the line prohibits lane changes, while the dashed
                        part allows them.
Step 5  Rule            area:grid: The grid marking indicates a keep clear area where vehicles should not
                        stop.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes are prohibited where the lines
                        are solid near your car.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 842, 6.96 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street in the UK with shops on both sides. The road ahead continues
                        straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right. Photo 2 shows a white solid line next
                        to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a dashed line on my left and a solid line on my
                        right. | roles: The white dashed line on the left correctly functions as a lane line,
                        and the white solid line on the right functions as an edge line. | markings: No
                        markings are present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line prohibits moving onto the pavement or shoulder to
                        the right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right edge line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may move into the left lane if needed, but do not move
                        to the right as it is the edge of the roadway. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 810, 7.43 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with a multi-lane layout. Ahead, there is a junction or a
                        change in lane configuration with a bicycle lane and a turn lane. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white line next to my car and a white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a white line next to my car and a white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:right (full): Photo 2 shows a white arrow pointing right in the lane to
                        my right.; symbol:bike (full): Photo 2 shows a bicycle symbol in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating the three lanes. | markings: The straight
                        arrow in my lane is consistent with the lane's purpose, and the right turn arrow/bike
                        symbol are in the adjacent lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for going straight
                        ahead.
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
                        ['arrow:right'], missed ['line:stop_line']), actions True, unsafe [], citation None,
                        contradictions ['turn_right prohibited although an arrow shows it']
Tokens                  in 3819, out 926, 8.36 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a pedestrian crossing and a bus stop ahead. My car is in
                        the middle lane of a three-lane roadway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my lane. Photo 2 shows a white dashed
                        line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my lane. Photo 2 shows a white
                        dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:left_turn_waiting (insufficient): No markings visible in my lane in Photo 1 or
                        Photo 2.; area:two_way_left_turn_lane (insufficient): No markings visible in my lane
                        in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: No markings were observed in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as needed, and
                        you can proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'area:two_way_left_turn_lane'], missed []), actions True,
                        unsafe [], citation None, contradictions []
Tokens                  in 3819, out 668, 7.14 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with buildings on both sides. The road ahead
                        continues straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a dashed white line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a dashed white line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white line across the lane ahead, but no arrows
                        or words are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The stop line ahead is consistent with the lane's end or a control point. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes to the left.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes to the right.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to stop before proceeding.
Step 6  change_left     allowed (correct): allowed by the dashed white left_boundary
Step 6  change_right    allowed (correct): allowed by the dashed white right_boundary
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the line:stop_line
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the
                        boundaries are dashed. You must come to a full stop at the white line ahead before
                        proceeding straight.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3819, out 864, 8.36 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrianized area or sidewalk to the right. The road
                        ahead appears to be a continuous stretch of lanes with some markings indicating
                        specific lane uses. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a bicycle symbol in the lane to my right. Photo 2
                        shows a bicycle symbol in the lane to my right.; symbol:bike (full): Photo 1 shows a
                        bicycle symbol in the lane to my left. Photo 2 shows a bicycle symbol in the lane to
                        my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle lane) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The bicycle symbols are in the adjacent lanes, not my lane. No
                        markings are in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The white dashed line allows for lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the
                        boundaries are dashed. Note that the lanes to your immediate left and right are marked
                        for bicycles.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 889, 8.15 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A residential street in the UK with a T-junction or small intersection ahead. My car
                        is in the left-hand lane of a two-way road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a sidewalk to the left. Photo 2 shows a raised curb
                        and a double dashed line (white) next to the curb.
                        white dashed, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the boundaries: a curb/edge line on the left and a lane line on the right.
                        | roles: The white dashed edge line on the left and solid lane line on the right fit
                        the roles of edge line and lane line respectively. | markings: The straight arrow in
                        my lane is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed edge line allows for movement onto the sidewalk/curb if
                        necessary, but generally marks the road boundary.
Step 5  Rule            right_boundary: The solid white line prohibits changing lanes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for going straight
                        ahead.
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight ahead in your current lane. Do not attempt to change lanes to the
                        right as the solid white line prohibits it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions ['change_left allowed across a curb']
Tokens                  in 3819, out 839, 6.55 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with shops on both sides. The road ahead is a multi-lane street with a
                        designated area for pedestrians and a clear lane for my car. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line separating my lane from a sidewalk/pedestrian area on the
                        left. Photo 2 shows a solid white line next to the car and a raised curb further
                        ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a dashed white line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:keep_clear (full): Photo 2 shows a white rectangular box with the words 'KEEP
                        CLEAR' inside it.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries: a white line on the left marks the edge of the
                        roadway, and a dashed line on the right separates my lane from the next lane. | roles:
                        The white solid edge line on the left and the dashed lane line on the right fit their
                        respective roles. | markings: The 'KEEP CLEAR' marking is centered in the lane and
                        does not conflict with the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white edge line prohibits crossing onto the sidewalk.
Step 5  Rule            right_boundary: The dashed white lane line allows for lane changes to the right.
Step 5  Rule            text:keep_clear: The 'KEEP CLEAR' marking indicates that the area should not be
                        blocked by vehicles.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead or change to the right lane if needed. Do not block the
                        area marked 'KEEP CLEAR' and do not move to the left onto the sidewalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:keep_clear'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 871, 7.3 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK with traffic keeping to the left. There is a clear
                        road ahead with several lanes and a sidewalk on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a dashed white line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on my right, which appears to be the edge of the
                        roadway. Photo 2 shows this line is solid white next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 1 shows a white dashed line further ahead in my
                        lane, which appears to be a lane divider.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree. The white dashed line on my left separates me from the leftmost lane. The solid
                        white line on my right is the edge of the road. | roles: The white dashed line on the
                        left is a lane line; the solid white line on the right is an edge line. | markings:
                        The dashed line ahead in my lane is a lane divider, not a stop/yield line. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The dashed white line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid white edge line prohibits moving onto the sidewalk or
                        shoulder to the right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white lane line on the
                        left
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the left lane. Do not move to the right as it is
                        the edge of the roadway.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 3819, out 844, 8.09 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a dedicated bike lane on the left. My car is in the lane
                        immediately to the right of the bike lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the bike lane. Photo 2 shows
                        a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the lane to my right. Photo
                        2 shows a dashed white line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows 'BUS LANE' text and a bike symbol in the lane to my
                        left.; symbol:bike (full): Photo 2 shows a bike symbol in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position (2nd
                        from left) agree with the boundaries: a solid white line on my left separates me from
                        the bike lane, and a dashed white line on my right separates me from the next lane. |
                        roles: The white solid line on the left and dashed line on the right correctly
                        identify the lane boundaries. | markings: The 'BUS LANE' and bike symbol are in the
                        lane to my left, not in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the bike lane to the left.
Step 5  Rule            right_boundary: The dashed white line allows changing into the lane to the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the lane on your right. Do not move into the
                        bike lane on your left as it is marked as a bus/bike lane and separated by a solid
                        line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike', 'text:bus'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 869, 7.68 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with a sidewalk and parked cars on the left. The road ahead has multiple
                        lanes and a designated area for parking or stopping. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line and a raised curb on the left. Photo 2 shows a white line
                        and a raised curb next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white line with a zigzag pattern next to the car.
                        white zigzag, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows white zigzag lines and a white line forming a bay on
                        the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the left edge line and right lane line. | roles: The white solid edge
                        line and white zigzag lane line fit the roles of edge and lane boundaries. | markings:
                        The zigzag lines and grid-like markings indicate a parking or restricted area on the
                        right. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The edge line and curb prohibit moving to the left.
Step 5  Rule            right_boundary: The zigzag line prohibits lane changes into the area on the right.
Step 5  Rule            area:grid: The markings indicate a restricted area, likely for parking or no-stopping.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight. Do not move into the area on the right
                        marked with zigzag lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 650, 10.16 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane that appears
                        to be a dedicated turn lane or a lane with specific directional markings. (lanes 3,
                        mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a raised curb and a metal fence on the right. Photo 2 shows a raised
                        curb and a paved sidewalk area.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white arrow pointing left in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree. The white dashed line on my left separates me from the lane to my left. The
                        curb on my right marks the edge of the roadway. | roles: The white dashed line is a
                        standard lane line. The curb is a standard edge line. | markings: The left-turn arrow
                        in my lane is consistent with the lane's purpose as a turn lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The curb prohibits moving to the right onto the sidewalk.
Step 5  Rule            arrow:left: The arrow indicates that the lane is for turning left.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the right_boundary (curb)
Step 6  go_straight     prohibited (correct): prohibited by the arrow:left marking
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the arrow:left marking
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the arrow:left marking
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited by the arrow:left marking
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane specifically for making a left turn at the upcoming intersection. Do not
                        attempt to go straight or turn right from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:right']), actions False, unsafe ['turn_left'], citation
                        None, contradictions []
Tokens                  in 3819, out 865, 8.19 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with multiple lanes of traffic. My car is in a lane that is part of a
                        multi-lane roadway with a bus lane to its left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the bus lane. Photo 2 shows a
                        solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to its right. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show 'BUS LANE' text in the lane to the left of
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree with the boundary roles. I am in the middle lane of three lanes of traffic
                        moving in the same direction. | roles: The white solid lines correctly function as
                        lane lines between lanes of the same direction. | markings: The 'BUS LANE' text is in
                        the lane to my left, which is consistent with the solid white line separating it from
                        my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the bus lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight. Lane changes to the left into the bus
                        lane or to the right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 809, 7.73 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings and trees on both sides. The road ahead appears to be a
                        multi-lane street with parked cars on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line and a raised curb on the left. Photo 2 shows a solid
                        white line and a raised curb on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line on the right. Photo 2 shows a dashed white line on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows 'BUS' in yellow paint in the lane to the left.;
                        area:two_way_left_turn_lane (full): Photo 1 shows a dashed white line and a left-turn
                        arrow in the lane to the left.
Step 4  Cross-check     close_up: the same in both photos | position: A lane line on my right means another
                        lane of my direction on my right. A curb on my left means my lane is the leftmost of
                        my direction. This is consistent with my lane being index 1. | roles: The white solid
                        line on the left acts as an edge line, and the dashed white line on the right acts as
                        a lane line. | markings: The 'BUS' text and the two-way left-turn lane are in the lane
                        to my left, not in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid edge line prohibits moving to the left onto the sidewalk or
                        the bus lane.
Step 5  Rule            right_boundary: The dashed lane line allows changing into the lane on the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You can proceed straight or change
                        into the lane on your right. Do not move left into the bus lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane', 'text:bus'], missed ['text:other']), actions True,
                        unsafe [], citation None, contradictions []
Tokens                  in 3819, out 880, 8.49 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street in the UK with shops on both sides. The road ahead continues
                        straight with several lanes of traffic. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with a dashed line on the left and a solid line on the
                        right. | roles: The white dashed line on the left correctly identifies a lane line,
                        and the solid white line on the right correctly identifies an edge line. | markings:
                        No markings are present to contradict the boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid edge line and curb prohibit moving to the right onto the
                        sidewalk.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by no marking governing this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may move into the left lane if needed, but you must
                        stay within the roadway as the right side is a solid edge line. Proceed straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 823, 7.4 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane on the left. The car is in a lane heading
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the bus lane. Photo 2 shows a solid
                        white line next to the car and a dashed white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a dashed white line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 shows 'BUS LANE' text and a bus symbol in the lane to the
                        left.; line:stop_yield (partial): Photo 1 shows a white line marking the end of the
                        bus lane area.
Step 4  Cross-check     close_up: The left boundary is solid next to the car and dashed further ahead; Photo 2
                        confirms the solid line near the car and Photo 1 shows the transition to dashed. |
                        position: The lane count is 3. My lane is the middle one (index 2). The left boundary
                        is a lane line separating me from the bus lane. The right boundary is a lane line
                        separating me from the rightmost lane. | roles: The white lines correctly function as
                        lane lines between lanes of the same direction. | markings: The 'BUS LANE' text is in
                        the lane to the left, not in my lane. No markings are in my lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid line prohibits crossing into the bus lane.
Step 5  Rule            right_boundary: The dashed line allows crossing into the lane on the right.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You can proceed straight or move into the right lane. Do
                        not move into the bus lane on your left as it is restricted by a solid line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_yield', 'text:bus'], missed []), actions True, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 3819, out 893, 7.52 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the UK. Ahead, there is a junction or a change in road
                        layout with some vehicles and a cyclist visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in my lane further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on my left and a solid white
                        line on my right. | roles: The white dashed line on the left and solid white line on
                        the right fit the roles of lane lines in a UK context. | markings: The left-turn arrow
                        in my lane is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:left: The arrow indicates that the lane is for turning left.
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     prohibited (contested, label allowed): prohibited
Step 6  turn_left       allowed: allowed
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to turn left at the upcoming junction. Lane changes to the right are
                        prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 826, 6.45 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with multiple lanes of traffic. The road ahead appears to be a straight
                        continuation of the current street. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line and a raised curb/island to my right. Photo 2 shows a solid
                        white line next to my car, followed by a raised curb/island.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2,
                        the rightmost lane) agree with the boundaries: a lane line is on my left and an edge
                        line/curb is on my right. | roles: The white solid line on the left is a lane line,
                        and the white solid line with a curb on the right is an edge line. | markings: No
                        markings are present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line and curb prohibit moving to the right.
Step 5  Rule            area:grid: The grid marking indicates a keep clear area.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are prohibited by the
                        solid white line, and the curb on your right prevents moving further right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 847, 8.03 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with multiple lanes of traffic. The road ahead appears to be a straight
                        continuation of the current street with a speed limit of 20 mph. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is solid and white near the car, and it remains solid further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is solid and white near the car, and it remains solid further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a large '20' speed limit circle painted in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        the middle lane (2) are consistent with the white lane lines on both sides. | roles:
                        The white solid lines correctly function as lane lines separating traffic moving in
                        the same direction. | markings: The '20' speed limit marking is consistent with the
                        urban environment and the lane's purpose. | unseen: none | result: consistent
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
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines. Observe the 20 mph speed limit.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 859, 6.91 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with a multi-lane layout. Ahead, there is a complex intersection with
                        zigzag markings and a white van in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a solid white line near the car, which then becomes a zigzag pattern
                        further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a solid white line near the car, which then becomes a zigzag pattern
                        further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 shows zigzag white lines across the road ahead of my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and my lane position
                        agree. I am in the middle lane of three lanes of traffic moving in the same direction.
                        | roles: The white lines correctly serve as lane lines between lanes of the same
                        direction. | markings: The zigzag markings are consistent with a pedestrian crossing
                        area or a restricted zone ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits changing into the lane to the left.
Step 5  Rule            right_boundary: The solid white line prohibits changing into the lane to the right.
Step 5  Rule            area:channelizing: The zigzag markings indicate a restricted area, typically near a
                        pedestrian crossing, where lane changes are prohibited.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as lane changes are prohibited by the solid white lines and
                        the zigzag markings ahead. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 851, 7.07 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test A | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with traffic keeping to the left. A red bus is in the lane to
                        my left, and a van is parked or stopped in a lane to my right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the bus lane. Photo 2 shows a white
                        line with a dashed pattern next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane with the van. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on my left (lane 1) and a white line
                        on my right (lane 3). | roles: The white dashed line on the left and solid line on the
                        right correctly define the boundaries of my lane. | markings: The straight arrow in my
                        lane is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The dashed line allows for lane changes to the left.
Step 5  Rule            right_boundary: The solid line prohibits lane changes to the right.
Step 5  Rule            arrow:straight: The arrow indicates that the lane is intended for going straight
                        ahead.
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change into the left
                        lane if necessary, but you are prohibited from changing into the right lane. Do not
                        attempt to turn left, right, or perform a U-turn from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 3819, out 863, 7.03 s
```
