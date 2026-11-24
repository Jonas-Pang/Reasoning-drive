# Reasoning of lane run 20261117_185904_laneA_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching an intersection with a red bus ahead
                        in the adjacent lane. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the left edge of the road next to the sidewalk. Photo 2
                        confirms a solid red line next to the car.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a bicycle symbol painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the left edge line and right lane line | roles: the red solid edge line and white
                        dashed lane line fit their roles | markings: the bicycle symbol is consistent with a
                        lane that can be used by cyclists | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing a solid edge line into the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a dashed lane line to change lanes is allowed.
Step 5  Rule            symbol:bike: The bicycle symbol indicates the lane is shared with or designated for
                        cyclists.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid edge line and curb,
                        which prohibits leaving the roadway
Step 6  change_right    allowed (WRONG, label prohibited): the right_boundary is a dashed lane line, which
                        allows changing lanes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane shared with cyclists; you may go straight or change to the right
                        lane, but do not cross the left boundary into the sidewalk.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3819, out 680, 12.41 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential road in the UK, facing a junction or a narrowing of the
                        road ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line next to the car and a curb. Photo 2 shows a white dashed
                        line next to the car and a raised curb.
                        white dashed, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car. Photo 2 shows a white dashed line
                        with several long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; the left boundary is an edge line and the right is a lane line,
                        implying another lane to the right. | roles: the white dashed patterns fit the roles
                        of edge and lane lines. | markings: no markings in my lane to check. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A dashed edge line with a curb prohibits crossing into the
                        sidewalk/curb area.
Step 5  Rule            right_boundary: A dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): the left boundary is a curb and edge line which
                        prohibits leaving the roadway
Step 6  change_right    allowed (contested, label prohibited): the right boundary is a dashed lane line which
                        allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the right lane. Do not cross the left boundary
                        into the curb area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation None, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 3819, out 611, 7.67 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on an urban road in the UK, facing a junction with a pedestrian crossing
                        and a cycle lane ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line on the left. Photo 2 shows the same white solid line
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the right lane. Photo 2
                        shows a white dashed line with several short dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows it continuing forward.; symbol:bike (full): Photo 2 shows a white bicycle symbol
                        in a designated area ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a solid edge line on the left and a dashed lane line on the right
                        indicate my lane is the leftmost of two lanes. | roles: the white solid edge line and
                        white dashed lane line fit their roles. | markings: the straight arrow is consistent
                        with the lane's position and the bike symbol ahead. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area to the left.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left or right.
Step 5  Rule            symbol:bike: The bicycle symbol indicates a cycle lane or area, which should be
                        avoided by motor vehicles.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        (left_boundary).
Step 6  change_right    allowed (correct): allowed by the dashed white lane line (right_boundary).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (arrow:straight).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (arrow:straight).
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (arrow:straight).
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (arrow:straight).
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane to go straight. You may change to the right lane if needed, but do
                        not cross the solid line on the left or enter the cycle area ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 809, 15.2 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a city street in the United Kingdom with buildings on both sides. The road
                        ahead is straight with no immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid yellow lines along the left edge of the road. Photo 2 confirms
                        two solid yellow lines next to my car and continuing ahead.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the opposite direction of
                        traffic. Photo 2 shows a white dashed line next to my car with visible gaps.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the right indicates my lane is the
                        leftmost of my direction in a two-way road. | roles: the double yellow edge line on
                        the left and the white dashed center line on the right fit their roles. | markings:
                        there are no markings in my lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines at the edge of the road indicate a parking
                        restriction and prohibit crossing the boundary to leave the roadway.
Step 5  Rule            right_boundary: A dashed center line allows crossing into the opposite lane for
                        overtaking or turning if it is safe to do so.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a double yellow edge line with a
                        curb, which prohibits leaving the roadway.
Step 6  change_right    allowed (correct): the right_boundary is a dashed center line, which allows crossing
                        into the opposite lane.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of a two-way road. You may proceed straight or overtake
                        to the right if safe, but do not cross the left boundary into the sidewalk area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 673, 8.16 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a junction with a pedestrian
                        crossing and bollards ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, following the curb. Photo
                        2 shows the same white line next to the car, which is solid.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line along the right edge of the road, following the curb. Photo
                        2 shows the same white line next to the car, which is solid.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a zebra crossing (white stripes)
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides | roles: the white solid lines on both sides fit the
                        role of edge lines | markings: the crosswalk is consistent with the road layout |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk/curb area.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the sidewalk/curb
                        area.
Step 5  Rule            line:crosswalk: Drivers must yield to pedestrians on the zebra crossing.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid edge line which
                        prohibits leaving the roadway
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid edge line which
                        prohibits leaving the roadway
Step 6  go_straight     allowed (contested, correct): no marking prohibits going straight
Step 6  turn_left       not_applicable: no arrow governs this action
Step 6  turn_right      not_applicable: no arrow governs this action
Step 6  u_turn          not_applicable: no arrow governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight, yielding to any pedestrians on the zebra
                        crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 676, 11.86 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with houses on the left and trees on the right. The
                        road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid red lines along the left edge of the road next to a curb.
                        Photo 2 confirms two solid red lines and a raised curb immediately next to my car.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from a parking or stopping area
                        on the right. Photo 2 shows a white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; the left boundary is an edge line and the right is a
                        lane line separating me from a parking area. | roles: the double red lines on the left
                        are typical UK edge lines for no stopping, and the white dashed line on the right is a
                        standard lane line. | markings: no markings in my lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Double red lines indicate no stopping at any time; crossing this
                        boundary to the left is prohibited by the curb and the road edge.
Step 5  Rule            right_boundary: A white dashed line allows lane changes if it is safe to do so.
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb and double red edge
                        lines
Step 6  change_right    allowed (correct): allowed by the white dashed lane line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection marking
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection marking
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may change to the right if necessary, but
                        do not stop or move to the left due to the double red lines and curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3819, out 682, 13.21 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead with
                        buildings on the right and a park area on the left. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the roadway from a blue-painted cycle
                        lane/shoulder. Photo 2 confirms this solid white line next to the car and extending
                        forward.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the lane to the right. Photo
                        2 shows a series of short white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a solid edge line on the left and a dashed lane line on the right
                        indicate the leftmost lane of a two-lane road. | roles: the white solid edge line and
                        white dashed lane line fit their respective roles. | markings: no markings are present
                        in my lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or cycle
                        lane.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line which
                        prohibits crossing it
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line which allows
                        changing lanes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid line on your left into the cycle lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 646, 10.88 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city road in the UK with shops on the right; the road continues straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line separating the road from a cycle lane/shoulder.
                        Photo 2 shows the same white dashed line next to my car, with several long dashes and
                        gaps.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from a parking/stopping area
                        where cars are parked. Photo 2 shows the same white dashed line next to my car, with
                        long dashes and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; my lane is the only main travel lane, bounded by edge lines on both
                        sides. | roles: the white dashed lines fit the role of edge lines separating the
                        travel lane from a cycle lane and a parking area. | markings: no markings in my lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white edge line allows crossing to enter or leave the
                        roadway/cycle lane.
Step 5  Rule            right_boundary: A dashed white edge line allows crossing to enter or leave the parking
                        area.
Step 6  change_left     allowed (correct): the left boundary is a dashed white line, which allows crossing.
Step 6  change_right    allowed (correct): the right boundary is a dashed white line, which allows crossing.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a single travel lane. You may proceed straight or move left or right across
                        the dashed lines if safe to do so.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 638, 12.94 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with a pedestrian crossing (Zebra crossing) ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road. Photo 2 confirms a
                        solid white line next to the car and continuing forward.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the opposite direction of
                        traffic. Photo 2 shows a solid white line next to the car and continuing forward.
                        white solid, curb no, center_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a zebra crossing (broad white stripes)
                        across the lane.; area:channelizing (full): Photo 1 and Photo 2 show zigzag white
                        lines on both sides of the lane approaching the crossing.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; a left edge line and a center line on the right indicate a single lane
                        road. | roles: the white solid lines fit the roles of edge line and center line. |
                        markings: the crosswalk and zigzag lines are consistent with a UK zebra crossing. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            right_boundary: A solid white center line prohibits crossing into the opposite lane of
                        traffic.
Step 5  Rule            line:crosswalk: Drivers must stop for pedestrians crossing or waiting to cross at a
                        zebra crossing.
Step 5  Rule            area:channelizing: Zigzag lines indicate the approach to a pedestrian crossing and
                        prohibit parking or overtaking.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line and curb.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white center line.
Step 6  go_straight     allowed (contested, correct): allowed as there are no arrows prohibiting it, but must
                        yield to pedestrians at the crosswalk.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection allowing a left
                        turn.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection allowing a right
                        turn.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow allowing a U-turn.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and prepare to stop for the pedestrian currently crossing the zebra
                        crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 785, 14.51 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, traveling forward. There are no
                        immediate intersections or ramps ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line separating the lane from a cycle lane, and further
                        ahead it remains dashed. Photo 2 shows the same white dashed line next to the car,
                        with several short dashes and gaps.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating the lane from the opposite traffic
                        direction. Photo 2 shows a white dashed line with gaps.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a circular '20' speed limit marking
                        painted on the road surface in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; the
                        left boundary is a special lane line for the cycle lane, and the right boundary is a
                        center line. | roles: the white dashed patterns fit the roles of a special lane line
                        and a center line in the UK. | markings: the speed limit marking is consistent with
                        the urban environment. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows crossing into the cycle lane if safe to do
                        so.
Step 5  Rule            right_boundary: A dashed white center line allows crossing into the opposite lane for
                        overtaking if safe and permitted.
Step 5  Rule            text:speed_limit: The marking indicates a maximum speed limit of 20 mph.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white special lane line
Step 6  change_right    allowed (correct): allowed by the dashed white center line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or intersection
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and observe the 20 mph speed limit. You may change lanes if
                        necessary and safe.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 725, 12.5 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a T-junction or intersection ahead. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line next to the car, which then becomes a white dashed
                        line further ahead. Photo 2 shows a white solid line next to the car and a white
                        dashed line slightly further ahead.
                        white solid_dashed (near line solid), curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car and further ahead. Photo 2 shows a
                        white dashed line next to the car and further ahead, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 1 and Photo 2 show a white arrow in my lane that
                        points both straight and left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; the
                        left boundary is an edge line and the right is a lane line, meaning there is another
                        lane to the right. | roles: the white solid/dashed edge line on the left and white
                        dashed lane line on the right fit their roles. | markings: the straight-left arrow is
                        consistent with the lane's position. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area to the left;
                        the dashed part allows it.
Step 5  Rule            right_boundary: A dashed white line allows lane changes to the right.
Step 5  Rule            arrow:straight_left: The arrow allows the car to go straight or turn left, and
                        prohibits turning right or making a U-turn.
Step 6  change_left     prohibited (contested, label allowed): the left boundary is solid next to the car,
                        which prohibits crossing it
Step 6  change_right    allowed (correct): the right boundary is dashed, which allows changing to the right
Step 6  go_straight     allowed (correct): the arrow in the lane allows going straight
Step 6  turn_left       allowed (correct): the arrow in the lane allows turning left
Step 6  turn_right      prohibited (correct): the arrow in the lane does not show a right turn, which
                        prohibits it
Step 6  u_turn          allowed (WRONG, label prohibited): the arrow allows a left turn in a left-keep system,
                        which also allows a U-turn
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn left. You may change lanes to
                        the right if needed, but do not cross the solid line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['u_turn'], citation None, contradictions ['rightmost lane,
                        but a lane line on the right']
Tokens                  in 3819, out 769, 23.77 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city road in the UK with traffic keeping left. The road continues straight ahead
                        with a cycle lane on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2 shows
                        the same solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 shows a
                        broken white line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; a solid white line on the left indicates the edge of the roadway for
                        traffic keeping left, and a dashed line on the right indicates another lane (a cycle
                        lane in this context). | roles: the white solid line on the left fits the role of an
                        edge line, and the white dashed line on the right fits the role of a lane line. |
                        markings: no markings in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left into the
                        shoulder or sidewalk.
Step 5  Rule            right_boundary: A broken white line allows crossing to the right to change lanes,
                        provided it is safe to do so.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid white line which
                        prohibits crossing it
Step 6  change_right    allowed (correct): the right_boundary is a dashed white line which allows crossing it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You can continue straight in your lane or change to the right into the cycle lane if
                        necessary. Do not cross the solid white line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3819, out 660, 11.67 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a junction with traffic lights and a
                        pedestrian crossing ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the left edge of the road next to the sidewalk. Photo 2
                        shows two red lines side by side running along the edge of the road.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the right lane. Photo 2
                        shows a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 1 and Photo 2 show a white arrow in my lane pointing
                        both straight and left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a red edge line on the left and a white lane line on
                        the right indicate I am in the leftmost lane of a two-lane road. | roles: the double
                        red edge line is a UK restriction marking, and the white dashed line is a standard
                        lane separator. | markings: the straight-left arrow is consistent with being in the
                        leftmost lane at a junction. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The double red lines indicate no stopping at any time; crossing this
                        boundary into the sidewalk is prohibited.
Step 5  Rule            right_boundary: The white dashed line allows lane changes when safe to do so.
Step 5  Rule            arrow:straight_left: The arrow allows the car to either go straight or turn left at
                        the end of the lane.
Step 6  change_left     prohibited (contested, correct): the left boundary is a curb and double red edge
                        lines, which prohibits leaving the roadway.
Step 6  change_right    allowed (correct): the right boundary is a dashed white line, which allows changing
                        lanes.
Step 6  go_straight     allowed (correct): the arrow in my lane allows going straight.
Step 6  turn_left       allowed (correct): the arrow in my lane allows turning left.
Step 6  turn_right      prohibited (correct): the arrow in my lane does not show a right turn, which prohibits
                        it.
Step 6  u_turn          allowed (WRONG, label prohibited): the arrow allows a left turn toward opposite
                        traffic, which also allows a U-turn in the UK.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the left lane; you may go straight, turn left, or change to the right lane.
                        Do not stop or park on the left due to the double red lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['u_turn'], citation None, contradictions []
Tokens                  in 3819, out 774, 15.4 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, facing forward. The road ahead appears to be a
                        single-lane stretch leading toward a junction or a narrowed section of the road.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road, next to a sidewalk.
                        Photo 2 confirms a solid white line immediately next to the car, continuing forward.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line along the right edge of the road, next to a sidewalk.
                        Photo 2 shows a solid white line immediately next to the car, continuing forward.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the presence of edge lines on both sides. | roles: the solid white lines on
                        both sides correctly serve as edge lines for a single-lane road. | markings: there are
                        no markings in the lane to contradict the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line which
                        prohibits leaving the roadway
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid white edge line which
                        prohibits leaving the roadway
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines on
                        either side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 640, 11.6 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, facing forward. The road continues straight
                        ahead towards an intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid line along the left edge of the road next to a sidewalk. Photo 2
                        shows a solid red line next to the curb.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a red edge line on the left and a white lane line on
                        the right indicate I am in the leftmost lane of a two-lane road. | roles: the red
                        solid edge line and white dashed lane line fit their roles. | markings: the straight
                        arrow in my lane is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid red edge line and curb prohibit leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: The dashed white lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: The straight arrow allows going straight and prohibits turning left,
                        turning right, or making a U-turn.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid red edge line and curb
Step 6  change_right    allowed (correct): allowed by the dashed white lane line
Step 6  go_straight     allowed (correct): allowed by the straight arrow
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited by the straight arrow
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn right, change to the right lane
                        across the dashed line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation None, contradictions []
Tokens                  in 3819, out 692, 12.98 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a pedestrian crossing and a
                        T-junction or intersection ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road, bordering a
                        sidewalk. Photo 2 confirms a solid white line next to the car, continuing forward.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, bordering a sidewalk. Photo 2 shows a
                        solid white line next to the car, continuing forward.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a zebra crossing (white stripes)
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides | roles: the solid white edge lines fit the role of
                        boundaries between the roadway and the sidewalk | markings: the crosswalk is
                        consistent with a single-lane city street | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing a solid edge line into the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a solid edge line into the sidewalk is prohibited.
Step 5  Rule            line:crosswalk: Drivers must yield to pedestrians on the crosswalk.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid edge line, which
                        prohibits leaving the roadway
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid edge line, which
                        prohibits leaving the roadway
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight, yielding to any pedestrians on the zebra
                        crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 673, 12.68 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, traveling straight ahead. There are buses in the
                        lanes to the left and ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a solid white line next to my car.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a red line along the edge of the road next to the sidewalk. Photo 2
                        shows the red line continuing next to my car.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a special lane line on the left and an edge line on the
                        right indicate I am in the rightmost lane of a two-lane road (where the left is a bus
                        lane). | roles: the solid white line fits the role of a special lane boundary, and the
                        red line fits the role of a road edge (red route). | markings: no markings in my lane
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line separating a general traffic lane from a bus lane
                        prohibits crossing into the bus lane.
Step 5  Rule            right_boundary: A solid red edge line and curb prohibit leaving the roadway to the
                        right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white special_lane_line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid red edge_line and curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the bus lane to your left or
                        cross the red line to your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 667, 13.51 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, traveling forward. A red double-decker bus is
                        stopped in a lane to the left, and a cyclist is ahead in the same lane as the bus.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        confirms a solid white line next to my car and continuing ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a grey curb and a metal railing on the right. Photo 2 shows the grey
                        curb and the railing immediately next to the road edge.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with a lane line on the left and an edge line on the right | roles: the
                        white solid line fits the role of a lane line, and the curb fits the role of an edge
                        line | markings: no markings in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: The curb and railing prohibit leaving the roadway to the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the curb and railing
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 3819, out 632, 11.83 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with
                        traffic keeping to the left. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the left edge of the road,
                        with red lines further left. Photo 2 shows a solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows the head of a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a white edge line on the left indicates my lane is the leftmost
                        of my direction. | roles: the solid white edge line and dashed white lane line fit
                        their roles. | markings: the straight arrow in my lane is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk area.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes into the adjacent lane.
Step 5  Rule            arrow:straight: A straight arrow allows going straight but prohibits turning left,
                        turning right, or making a U-turn.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid edge line which
                        prohibits leaving the roadway.
Step 6  change_right    allowed (correct): the right_boundary is a dashed lane line which allows changing
                        lanes.
Step 6  go_straight     allowed (correct): the arrow:straight in my lane allows going straight.
Step 6  turn_left       prohibited (correct): the arrow:straight in my lane prohibits turning left.
Step 6  turn_right      prohibited (correct): the arrow:straight in my lane prohibits turning right.
Step 6  u_turn          prohibited (correct): the arrow:straight in my lane prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn right, change to the right lane
                        across the dashed line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 719, 12.19 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a junction with traffic lights ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the left lane. Photo 2 shows
                        a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the right lane. Photo 2
                        shows a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows it continuing forward.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the middle lane agree with having lane lines on both left and right. | roles: white
                        dashed lines are correct for lane lines separating traffic in the same direction. |
                        markings: the straight-ahead arrow is consistent with a middle lane at a junction. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A white dashed line allows lane changes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left or right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): the right boundary is a white dashed line, which allows lane
                        changes.
Step 6  go_straight     allowed (correct): the arrow in my lane shows straight ahead, which allows this
                        movement.
Step 6  turn_left       prohibited (correct): the arrow in my lane only shows straight ahead, which prohibits
                        turning left.
Step 6  turn_right      prohibited (correct): the arrow in my lane only shows straight ahead, which prohibits
                        turning right.
Step 6  u_turn          prohibited (correct): the arrow in my lane only shows straight ahead, which prohibits
                        U-turns.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, change to the
                        corresponding outer lane before the junction.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 716, 13.02 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward on a road with buildings on the
                        left and trees on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line extending ahead. Photo 2 shows the same solid white
                        line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car and further ahead. Photo 2 shows a
                        broken white line with several short dashes and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a lane line on the left and an edge line on the right indicate
                        the rightmost lane of a two-lane road. | roles: the white solid line as a lane line
                        and white dashed line as an edge line are consistent with UK road markings. |
                        markings: no markings in the lane to contradict boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing to change lanes.
Step 5  Rule            right_boundary: A broken white edge line allows crossing to the shoulder or parking
                        area if safe.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line
Step 6  change_right    allowed (correct): allowed by the broken white edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right to the shoulder; lane changing to the left is
                        prohibited by the solid line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 627, 11.29 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing forward. The road ahead is a straight
                        stretch with buildings on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road, next to a sidewalk.
                        Photo 2 confirms a solid white line next to the car, with a raised curb immediately to
                        its left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from a parking area or side lane
                        on the right. Photo 2 shows a series of short white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left edge line and right lane line | roles: the white solid edge line on the
                        left and white dashed lane line on the right fit their roles | markings: no markings
                        in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            right_boundary: A dashed white line allows lane changes when safe to do so.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line with a
                        curb, which prohibits leaving the roadway
Step 6  change_right    allowed (correct): the right_boundary is a dashed white line, which allows changing
                        lanes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the right. Do not cross the solid white
                        line on the left into the sidewalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3819, out 634, 12.48 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the United Kingdom, driving forward. The road ahead
                        appears to be a straight stretch with parked cars on the right. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows the right edge of the roadway, where the asphalt meets a sidewalk area
                        with parked cars. Photo 2 shows a white line further ahead, but next to my car, there
                        is no painted line, only the edge of the road.
                        white dashed, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right | roles: the white
                        dashed line on the left fits the role of a lane line; the white dashed line on the
                        right fits the role of an edge line | markings: no markings in my lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed edge line allows crossing into the shoulder or parking
                        area if safe and legal.
Step 6  change_left     allowed (contested, label prohibited): allowed by the white dashed lane line
Step 6  change_right    allowed (correct): allowed by the white dashed edge line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of a two-lane road. You may continue straight or change
                        to the left lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 674, 12.49 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward with other vehicles ahead. The
                        road appears to be a single-carriageway urban street. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line along the left edge of the road next to the sidewalk.
                        Photo 2 confirms a single solid yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line between my lane and the oncoming traffic; the road
                        surface is wet and reflective. Photo 2 also shows no painted line to the right of the
                        car.
                        none none, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the left edge line and the right center line role | roles: the yellow solid
                        edge line on the left is consistent with UK parking restrictions at the curb; the
                        absence of a line on the right is common for narrow urban streets | markings: no
                        markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line indicates parking restrictions; crossing it to
                        the left is prohibited as it leads to the sidewalk.
Step 5  Rule            right_boundary: The absence of a line does not prohibit movement, but the role as a
                        center line means crossing it would enter the path of oncoming traffic.
Step 6  change_left     prohibited (contested, correct): the left boundary is a solid yellow edge line and a
                        curb, which prohibits leaving the roadway
Step 6  change_right    allowed: the right boundary is a center line; while no paint prohibits it, it is the
                        boundary to oncoming traffic
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and follow the traffic ahead. You may change right if safe to do so,
                        but do not cross the left boundary into the sidewalk.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 3819, out 686, 12.76 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, traveling forward. Ahead is a clear stretch of
                        road with a bus lane to the left. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a solid white line immediately to the left of my car.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the rightmost lane. Photo 2
                        shows a series of white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a special lane line on the left and a lane line on the right
                        place me in the second lane from the left. | roles: the solid white line for a bus
                        lane and dashed white line for a lane change fit their roles. | markings: no markings
                        in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line marking a bus lane prohibits ordinary vehicles from
                        entering it.
Step 5  Rule            right_boundary: A dashed white line allows lane changes into the adjacent lane.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white line marking a bus
                        lane, which prohibits entry for ordinary cars
Step 6  change_right    allowed (correct): the right_boundary is a dashed white line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane. You may continue straight or change to the right lane,
                        but you must not enter the bus lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3819, out 647, 12.8 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, facing a road with parked cars on both sides
                        and a red bus ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a dashed white line next to the car, which becomes a solid white line
                        further ahead near a junction. Photo 2 shows the dashed white line next to the car.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a curb and a sidewalk on the right. Photo 2 shows the curb and sidewalk
                        immediately next to the car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show a yellow box junction (grid) across the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the left boundary is an edge line and the right is a curb, meaning
                        this is a single-lane road. | roles: the white dashed line on the left and the curb on
                        the right fit the role of edge lines for a single-lane road. | markings: the grid area
                        is a standard box junction marking. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows crossing to enter or leave the roadway.
Step 5  Rule            right_boundary: A curb prohibits leaving the lane to the right.
Step 5  Rule            area:grid: Drivers must not enter the box junction unless their exit is clear.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white left boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the curb on the right
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You can proceed straight or move left across the dashed line. Do not enter the yellow
                        box junction unless your exit is clear.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 707, 22.77 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a straight stretch with a bus ahead and
                        parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to the car, and further ahead it remains
                        dashed. Photo 2 shows a white dashed line with several long dashes and gaps.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car, and further ahead it remains
                        dashed. Photo 2 shows a white dashed line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the left boundary separates my lane from a cycle lane, and the right
                        boundary separates it from a parking/traffic lane. | roles: the white dashed lines fit
                        the roles of a special lane line (cycle lane) and a lane line. | markings: no markings
                        in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed line allows crossing into the adjacent lane if safe.
Step 5  Rule            right_boundary: A white dashed line allows crossing into the adjacent lane if safe.
Step 6  change_left     allowed (contested, label prohibited): the left_boundary is a white dashed line, which
                        allows crossing.
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line, which allows crossing.
Step 6  go_straight     allowed (contested, correct): no marking governs this action.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You can proceed straight in your lane. Lane changes to the left or right are permitted
                        if safe, but be mindful of the cycle lane on the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3819, out 635, 11.9 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with a pedestrian crossing
                        and a traffic island ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road, separating the lane
                        from the sidewalk. Photo 2 confirms a solid white line next to the car and further
                        ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a traffic island/median.
                        Photo 2 shows a solid white line next to the car and further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides | roles: the solid white lines on both sides fit the
                        role of edge lines for a single-lane road | markings: no markings in the lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk/shoulder.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the traffic
                        island/median.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line which
                        prohibits crossing it
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid white edge line which
                        prohibits crossing it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 611, 12.59 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the United Kingdom, driving forward on a multi-lane road
                        with shops and buildings on both sides. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a solid white line next to my car, extending further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the roadside. Photo 2 shows a solid
                        white line next to my car, and further ahead it remains solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane_line on the left and an edge_line on the right | roles: the white
                        solid lines fit the roles of lane_line and edge_line | markings: no markings in my
                        lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing to change lanes.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing to leave the roadway.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white line which
                        prohibits lane changes
Step 6  change_right    prohibited (WRONG, label allowed): the right_boundary is a solid white edge line which
                        prohibits leaving the roadway
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight; lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 623, 12.12 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a city street in the United Kingdom. My car is in a lane facing a traffic
                        light, with a vehicle ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and double yellow lines along the left edge of the road.
                        Photo 2 confirms the raised curb and the double yellow lines next to my car.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with several long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        also shows it.; symbol:bike (full): Photo 2 shows a bicycle symbol painted across the
                        lane ahead of my car; Photo 1 also shows it.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a curb and edge line on the left indicate I am in the
                        leftmost lane. | roles: the yellow double solid edge line and white dashed lane line
                        fit their roles. | markings: the straight arrow is consistent with the lane's position
                        and boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The curb and double yellow lines mark the edge of the roadway and
                        prohibit parking; crossing them to the left is prohibited.
Step 5  Rule            right_boundary: A white dashed line allows lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight and prohibits turning left, turning
                        right, or making a U-turn.
Step 5  Rule            symbol:bike: The bicycle symbol indicates a cycle lane or shared space and does not
                        govern vehicle movements.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a curb and edge line, which
                        prohibits leaving the roadway to the left.
Step 6  change_right    allowed (contested, correct): the right_boundary is a dashed lane line, which allows
                        changing to the right.
Step 6  go_straight     allowed (correct): the arrow:straight marking allows going straight.
Step 6  turn_left       prohibited (correct): the arrow:straight marking prohibits turning left.
Step 6  turn_right      prohibited (correct): the arrow:straight marking prohibits turning right.
Step 6  u_turn          prohibited (correct): the arrow:straight marking prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn right, change to the right lane
                        across the dashed line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 813, 15.52 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, facing straight ahead with a bus and
                        other vehicles in the distance. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the right edge of the road.
                        Photo 2 shows the same white dashed line next to my car, with clear gaps between the
                        dashes.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right | roles: the white
                        dashed pattern fits both the lane_line and edge_line roles | markings: no markings in
                        my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed edge line allows moving onto the shoulder or edge of
                        the road to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line which allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line which allows moving to
                        the right
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 631, 10.5 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road in the UK, traveling forward. The road ahead
                        appears to be a straight stretch with shops on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the opposite direction of
                        traffic. Photo 2 shows the same white dashed line next to my car, consisting of long
                        dashes and gaps.
                        white dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car that eventually meets a curb. Photo 2
                        shows a white dashed line with long dashes and gaps next to my car, and a red line
                        along the curb further right.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a center line on the left and an edge line on the right indicate
                        a single lane for my direction. | roles: the white dashed center line and white dashed
                        edge line are consistent with the roles assigned. | markings: there are no markings in
                        my lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed center line allows crossing into the opposite lane for
                        overtaking or turning if safe to do so.
Step 5  Rule            right_boundary: A dashed edge line allows crossing to the side, but the presence of a
                        curb prohibits driving onto the sidewalk.
Step 6  change_left     allowed (correct): allowed by the dashed center line (left_boundary).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the raised curb (right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You can proceed straight or move left to overtake if safe. Do not drive onto the right
                        curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 699, 12.24 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead. The road
                        continues forward with no immediate intersection or ramp visible. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to a raised curb and metal railing. Photo 2
                        confirms a white solid line and a raised stone curb immediately to the right of my
                        lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle with the number '20'
                        painted on the road surface in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right. | roles: the white
                        dashed line fits the role of a lane line, and the white solid line with a curb fits
                        the role of an edge line. | markings: the speed limit marking is consistent with a
                        standard urban lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and curb prohibit leaving the roadway to the
                        right.
Step 5  Rule            text:speed_limit: The speed limit marking indicates the maximum speed allowed in this
                        area.
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed lane line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        edge line and a curb.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting it and
                        no arrows restricting movement.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you must not cross the right boundary. Observe the 20 mph speed limit.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:speed_limit'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 794, 12.6 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, facing a T-junction or intersection
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the curb. Photo 2 confirms a solid white line
                        running parallel to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a line of parked cars and no clear painted boundary next to my car.
                        Photo 2 shows no painted line on the right side, only the asphalt and parked vehicles.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the left edge line and the absence of a lane line on the right. | roles:
                        the solid white edge line on the left fits the role of an edge_line. | markings: there
                        are no markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk.
Step 5  Rule            right_boundary: No painted line is present, but parked cars physically restrict
                        movement to the right.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line which
                        prohibits crossing it
Step 6  change_right    allowed (correct): no marking governs this action
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be cautious of parked cars on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 3819, out 601, 12.57 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, facing forward with shops and sidewalks on both
                        sides. The road ahead appears to be a straight stretch of a two-way street. (lanes 1,
                        mine 1, full)
Step 2  Left            Photo 1 shows a curb and a sidewalk to the left of the lane. Photo 2 confirms a raised
                        stone curb immediately next to the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a wide open asphalt area to the right with no painted lines. Photo 2
                        also shows no paint or markings to the right of the car.
                        none none, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 show the word 'BUS STOP' painted on the road
                        surface in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the left boundary being a curb and the right boundary being an unmarked area
                        (likely a shared space or wide lane). | roles: The left boundary is a curb, fitting
                        the role of an edge_line. The right boundary has no paint, fitting a lane_line in a
                        low-marking urban environment. | markings: The 'BUS STOP' text is consistent with a
                        city street environment. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The curb prohibits leaving the roadway to the left.
Step 5  Rule            right_boundary: The absence of a solid line allows changing lanes to the right if
                        safe.
Step 5  Rule            text:other: The 'BUS STOP' marking indicates a zone for buses to stop, but does not
                        prohibit through traffic for other vehicles unless accompanied by signs.
Step 6  change_left     prohibited (contested, correct): prohibited by the left_boundary (curb).
Step 6  change_right    allowed (correct): allowed as the right_boundary has no prohibiting markings.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection immediately ahead.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection immediately ahead.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or intersection immediately ahead.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a lane with a bus stop marking; you may proceed straight or move to the
                        right, but do not cross the left curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation None, contradictions
                        ['rightmost lane, but a lane line on the right', 'change_right decided with nothing
                        marked on that side']
Tokens                  in 3819, out 771, 14.52 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward on a road with buildings and
                        shops on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a parking/stopping area with
                        red lines. Photo 2 confirms a solid white line immediately to the left of the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating the lane from the opposite direction of
                        traffic. Photo 2 shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; the
                        left boundary is an edge line and the right is a center line, meaning this is a single
                        lane for my direction. | roles: the solid white edge line and dashed white center line
                        fit their roles for a single-lane road in the UK. | markings: no markings present in
                        the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the adjacent area
                        (parking/shoulder).
Step 5  Rule            right_boundary: A dashed white center line allows crossing into the opposite lane for
                        overtaking or turning if safe to do so.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line
                        (left_boundary).
Step 6  change_right    allowed (correct): allowed by the dashed white center line (right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to the right if
                        necessary for overtaking or turning, but do not cross the solid white line to the
                        left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 826, 15.56 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling forward. A bus is stopped
                        in a bus lane to the left, and another vehicle is in the lane to the right. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a single solid white line next to my car and extending forward.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows several white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a special lane line on the left and a lane line on the right
                        indicate my lane is the first of the general traffic lanes. | roles: the solid white
                        line for a bus lane and dashed white line for a lane change fit their roles. |
                        markings: no markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line marking a bus lane prohibits ordinary vehicles from
                        entering the bus lane.
Step 5  Rule            right_boundary: A dashed white line allows lane changes into the adjacent lane.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white line marking a bus
                        lane, which prohibits entry for ordinary cars
Step 6  change_right    allowed (correct): the right_boundary is a dashed white line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not enter the bus lane to
                        your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 651, 13.45 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, driving forward on a street lined
                        with houses and shops. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, next to a sidewalk. Photo
                        2 shows this line is a solid white line immediately next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right side of the road. Photo 2 shows this line is a
                        solid white line next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both left and right | roles: the solid white edge lines fit the
                        role of roadway boundaries | markings: there are no markings in the lane | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid edge line which
                        prohibits leaving the roadway
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid edge line which
                        prohibits leaving the roadway
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 600, 19.23 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with
                        traffic lights. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a raised curb and a metal fence. Photo 2
                        confirms a solid white line and a raised curb immediately to the right of my lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 1 and Photo 2 show a white arrow in my lane pointing
                        to the right.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        with a curb fits the role of an edge line | markings: the right-turn arrow is
                        consistent with the lane being the rightmost lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line and curb prohibit leaving the roadway to the
                        right.
Step 5  Rule            arrow:merge_right: The right-turn arrow allows turning right and prohibits going
                        straight, turning left, or making a U-turn.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb
Step 6  go_straight     prohibited (correct): prohibited by the right-turn arrow
Step 6  turn_left       prohibited (correct): prohibited by the right-turn arrow
Step 6  turn_right      allowed (correct): allowed by the right-turn arrow
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited by the right-turn arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a right-turn only lane. If you intend to go straight or turn left, you must
                        change to the left lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:right']), actions False, unsafe [], citation
                        None, contradictions ['go_straight, turn_left, turn_right, u_turn decided without an
                        arrow or prohibited-movement marking']
Tokens                  in 3819, out 729, 13.83 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. My car is in a lane that continues
                        straight ahead, with a bus lane to its left. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a solid white line next to my car and continuing ahead.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from another lane of my
                        direction. Photo 2 shows a dashed white line next to my car with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a special lane line on the left and a lane line on the
                        right place me in the second lane from the left. | roles: the white solid line for a
                        bus lane and white dashed line for a lane change fit their roles. | markings: there
                        are no markings in my lane, which is consistent with the boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid white line separating a bus lane prohibits ordinary cars from
                        entering the bus lane.
Step 5  Rule            right_boundary: A dashed white line allows lane changes into the adjacent lane.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white line for a bus
                        lane, which prohibits entry for ordinary cars
Step 6  change_right    allowed (correct): the right_boundary is a dashed white line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a general traffic lane. You may go straight or change to the right lane,
                        but you must not enter the bus lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3819, out 657, 11.71 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A residential urban street in the UK with parked cars on the right and a bus lane on
                        the left; the road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from a bus lane. Photo 2 confirms
                        a solid yellow line next to my car and continuing ahead.
                        yellow solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the roadway from a parking area. Photo 2
                        shows a solid white line next to my car and continuing ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show the word 'BUS' painted in yellow in the lane
                        to the left of my lane, not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line marking a bus lane prohibits ordinary cars from
                        entering it.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the parking/shoulder
                        area.
Step 5  Rule            text:bus: The bus lane is reserved for buses and authorized vehicles.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow special_lane_line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge_line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; do not enter the bus lane on the left or the
                        parking area on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3819, out 666, 11.69 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward on a multi-lane road with shops
                        and buildings on both sides. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a solid white line next to my car, extending further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating the road from the sidewalk/parking area. Photo 2
                        shows a solid white line next to my car, with a red line painted parallel to it
                        further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a lane line on the left and an edge line on the right indicate I
                        am in the rightmost lane of a two-lane road. | roles: the white solid lane line and
                        white solid edge line fit their roles. | markings: no markings in my lane to check. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits changing lanes across it.
Step 5  Rule            right_boundary: A solid white edge line and the adjacent curb prohibit leaving the
                        roadway to the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and curb on
                        the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane prohibiting
                        it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 671, 13.27 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the United Kingdom, driving forward. The road ahead
                        appears to be a straight stretch with parked cars and buildings on the right. (lanes
                        2, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from a bus lane on the left. Photo 2
                        shows this line is a solid white line next to my car, extending further ahead.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the rightmost lane. Photo 2
                        shows a white dashed line next to my car with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show the words 'BUS LANE' painted in the lane to
                        the left of my lane, not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; my lane is the second from the left, bounded by a
                        special lane line on the left and a lane line on the right. | roles: the white solid
                        line on the left fits the role of a special lane boundary, and the white dashed line
                        on the right fits the role of a lane line. | markings: the 'BUS LANE' text is in the
                        adjacent lane, which is consistent with the left boundary being a special_lane_line. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line separating a special lane (bus lane) prohibits
                        crossing into that lane.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 5  Rule            text:bus: The bus lane is reserved for buses and authorized vehicles; ordinary cars
                        are prohibited from entering it.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white special_lane_line and
                        the bus lane restriction.
Step 6  change_right    allowed (correct): allowed by the dashed white lane line.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Do not enter the bus lane to
                        your left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation None, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 3819, out 785, 13.61 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward. The road ahead appears to be a
                        single-lane stretch with parked cars and a cyclist on the right. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a single yellow line along the left edge of the road next to a curb.
                        Photo 2 confirms a single yellow line and a raised curb immediately to the left of the
                        car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, only the road surface and parked cars.
                        Photo 2 also shows no painted line on the right side of the lane.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the left edge line and the absence of a lane line on the right. | roles:
                        the yellow solid edge line on the left fits the role of an edge line in the UK. |
                        markings: there are no markings in the lane to contradict. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid yellow edge line with a curb prohibits leaving the roadway to
                        the left.
Step 5  Rule            right_boundary: The absence of a line on the right does not prohibit moving right, but
                        the presence of parked cars and a cyclist may restrict it.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid yellow line and curb
                        which prohibits leaving the road
Step 6  change_right    allowed (correct): no marking governs this action
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be cautious of the cyclist and parked cars on
                        your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 3819, out 648, 10.99 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward. The road ahead appears to be a
                        single lane in this direction, separated from a parking/loading area on the right by a
                        small island. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line extending from the bottom towards the horizon. Photo
                        2 confirms a solid white line immediately next to the car.
                        white solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line that ends at a concrete island. Photo 2 shows a short white
                        line segment next to the car, followed by a raised concrete island with a blue
                        bollard.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge line/curb on the right | roles: the white
                        solid center line and white solid edge line fit their roles | markings: no markings in
                        lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white center line prohibits crossing into the opposite traffic
                        lane.
Step 5  Rule            right_boundary: A solid white edge line and raised curb prohibit leaving the roadway
                        to the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white center line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and raised
                        curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 644, 12.14 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom with buildings on both sides. The road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from a cycle lane or shoulder.
                        Photo 2 shows a white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle containing the number
                        '20' painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line and the white solid line
                        fits the role of an edge line | markings: the speed limit marking is consistent with
                        the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the area to the right.
Step 5  Rule            text:speed_limit: The speed limit marking indicates the maximum speed allowed in this
                        area.
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a white dashed lane
                        line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a white
                        solid edge line
Step 6  go_straight     allowed (contested, correct): allowed because no marking prohibits it and the lane
                        does not end
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane
Step 6  u_turn          not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may go straight or change to the
                        left lane, but you must not cross the solid white line to the right. Observe the 20
                        mph speed limit.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 771, 13.19 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, facing forward. The road ahead appears to be a
                        single lane in this direction, though it is marked with zig-zag lines. (lanes 1, mine
                        1, full)
Step 2  Left            Photo 1 shows a white line separating the road from the sidewalk. Photo 2 shows this
                        line is a solid white line next to the car, continuing as a solid white line further
                        ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating the road from the opposite direction of traffic.
                        Photo 2 shows this line is a solid white line next to the car, continuing as a solid
                        white line further ahead.
                        white solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left edge line and right center line | roles: the white solid lines fit the
                        roles of edge line and center line | markings: no markings in lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk area.
Step 5  Rule            right_boundary: A solid white center line prohibits crossing into the opposite lane of
                        traffic.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line which
                        prohibits crossing it
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid white center line which
                        prohibits crossing it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3819, out 626, 10.65 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward. The road ahead appears to be a
                        straight stretch with parked vehicles on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of the car. Photo 2 shows the same white
                        dashed line next to the car, with several long dashes and gaps visible.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line near the right edge of the road. Photo 2 shows a
                        yellow solid line next to the curb on the right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a lane line on the left indicates another lane of the same
                        direction, and an edge line on the right indicates the end of the roadway. | roles:
                        the white dashed line fits the role of a lane line, and the yellow solid line fits the
                        role of an edge line (parking restriction). | markings: no markings are present in the
                        lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A yellow solid line at the edge of the road prohibits crossing into
                        the curb area and usually indicates parking restrictions.
Step 5  Rule            no_turn:left: no marking governs this action
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the yellow solid right boundary and the
                        curb
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not move to the right as it
                        is the road edge with parking restrictions.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 3819, out 701, 13.48 s
```
