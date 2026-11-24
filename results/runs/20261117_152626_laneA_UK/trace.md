# Reasoning of lane run 20261117_152626_laneA_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching an intersection with a red double-
                        decker bus ahead in the adjacent lane. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the curb. Photo 2 shows a solid red line next to the
                        curb.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line. Photo 2 shows a white dashed line with long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a bicycle symbol painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the left edge line and right lane line | roles: the red solid edge line and white
                        dashed lane line fit their roles | markings: the bicycle symbol is consistent with a
                        lane that may be shared or reserved for cycles | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid red edge line and curb prohibit leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: The white dashed lane line allows changing lanes to the right.
Step 5  Rule            symbol:bike: The bicycle symbol indicates the lane is shared with or reserved for
                        cyclists.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid red line and curb
                        which prohibits leaving the road
Step 6  change_right    allowed (WRONG, label prohibited): the right_boundary is a dashed white line which
                        allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking prohibits going straight
Step 6  turn_left       not_applicable: no arrow governs this action
Step 6  turn_right      not_applicable: no arrow governs this action
Step 6  u_turn          not_applicable: no arrow governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a lane shared with cyclists; you may go straight or change to the right
                        lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3642, out 657, 11.29 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential road in the UK, facing a junction or a narrowing of the
                        road where traffic is channeled. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line next to the car and a curb. Photo 2 shows a white dashed
                        line next to the car, followed by a solid white line further ahead that curves away
                        from the lane.
                        white dashed, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line next to the car and a curb further ahead. Photo 2 shows a
                        white dashed line next to the car, which then curves to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the car is in a single lane bounded by an edge line on the left and a
                        lane line on the right. | roles: the white dashed lines fit the role of lane and edge
                        markings in this context. | markings: there are no markings in the lane to contradict
                        the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white edge line with a curb prohibits crossing into the
                        sidewalk/curb area.
Step 5  Rule            right_boundary: A dashed white line allows lane changes if safe to do so.
Step 6  change_left     prohibited (contested, correct): the left boundary is an edge line with a curb, which
                        prohibits leaving the roadway
Step 6  change_right    allowed (contested, label prohibited): the right boundary is a dashed white line,
                        which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right if necessary; do not cross the left boundary into the
                        curb area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation None, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 3642, out 641, 11.29 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching an intersection with a bicycle lane
                        and a turn lane ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line next to the car that continues forward. Photo 2
                        confirms a white solid line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car, which then becomes a solid white
                        line further ahead. Photo 2 shows a white dashed line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows it as well.; symbol:bike (full): Photo 2 shows a bicycle symbol in a designated
                        area ahead of my lane; Photo 1 shows it as well.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the left boundary being an edge line and the right boundary being a lane line |
                        roles: the white solid left boundary fits an edge line and the white dashed right
                        boundary fits a lane line | markings: the straight arrow in my lane is consistent with
                        the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area to the left.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: The straight arrow allows going straight ahead and prohibits turning
                        left or right.
Step 5  Rule            symbol:bike: The bicycle symbol indicates a cycle lane and does not govern car
                        movements in my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        (left_boundary)
Step 6  change_right    allowed (correct): allowed by the dashed white lane line (right_boundary)
Step 6  go_straight     allowed (correct): allowed by the straight arrow (arrow:straight)
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow (arrow:straight)
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow (arrow:straight)
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow (arrow:straight)
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn right, change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 777, 13.34 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with buildings on both sides; the road continues straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid yellow lines along the left edge of the road. Photo 2 confirms
                        two solid yellow lines next to my car.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the opposite direction of
                        traffic. Photo 2 shows a white dashed line next to my car with clear gaps.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the right and an edge line on the left
                        indicate I am in the only lane for my direction. | roles: the double yellow edge line
                        and white dashed center line fit their roles for a UK single-carriageway road. |
                        markings: no markings in my lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines indicate no parking or waiting; crossing them to
                        leave the roadway is generally prohibited unless for specific access.
Step 5  Rule            right_boundary: A dashed center line allows crossing for overtaking or turning if it
                        is safe to do so.
Step 6  change_left     prohibited (contested, correct): the left boundary is a double yellow edge line with a
                        curb, prohibiting leaving the roadway.
Step 6  change_right    allowed (correct): the right boundary is a dashed center line, which allows crossing
                        for overtaking or turning.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to the right to
                        overtake or turn if the road ahead is clear.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 653, 12.42 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a junction with a pedestrian
                        crossing and a narrow road ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, next to a sidewalk. Photo
                        2 shows this line is a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line along the right edge of the road, next to a sidewalk. Photo
                        2 shows this line is a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a zebra crossing (white stripes)
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides | roles: the solid white lines on both sides fit the
                        role of edge lines for a single-lane road | markings: the crosswalk is consistent with
                        the road layout | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            line:crosswalk: A crosswalk requires yielding to pedestrians crossing the road.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid edge line which
                        prohibits leaving the roadway
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid edge line which
                        prohibits leaving the roadway
Step 6  go_straight     allowed (contested, correct): no marking prohibits going straight
Step 6  turn_left       not_applicable: no arrow or marking governs this action
Step 6  turn_right      not_applicable: no arrow or marking governs this action
Step 6  u_turn          not_applicable: no arrow or marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight, yielding to any pedestrians at the zebra
                        crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 686, 11.45 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with traffic moving on the left. The road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid red lines along the left edge of the road next to a curb.
                        Photo 2 confirms two solid red lines and a raised curb immediately to the left of my
                        car.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from a parking or stopping area
                        on the right. Photo 2 shows a series of short white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; the left boundary is an edge line and the right is a
                        lane line separating the driving lane from a parking area. | roles: the double red
                        lines on the left are typical UK 'no stopping' edge lines; the broken white line on
                        the right is a standard lane separator. | markings: no markings are present in my
                        lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double red lines indicate no stopping at any time; crossing the curb
                        into the sidewalk is prohibited.
Step 5  Rule            right_boundary: A broken white line allows crossing for lane changes or
                        entering/leaving the adjacent area.
Step 6  change_left     prohibited (contested, correct): the left boundary is a curb and double red lines,
                        which prohibits leaving the roadway to the left.
Step 6  change_right    allowed (correct): the right boundary is a broken white line, which allows changing to
                        the right.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may move to the right if necessary, but do
                        not stop or move to the left due to the double red lines and curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3642, out 678, 12.66 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead with
                        buildings on the right and a park area on the left. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the roadway from a blue-painted cycle
                        lane. Photo 2 confirms a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the lane to the right. Photo
                        2 shows a series of short white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a solid edge line on the left and a dashed lane line on the right
                        indicate the leftmost lane of the direction of travel. | roles: the white solid edge
                        line and white dashed lane line fit their respective roles. | markings: there are no
                        markings in my lane to conflict with. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the cycle lane or
                        shoulder.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line which
                        prohibits crossing it.
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line which allows
                        changing lanes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not enter the cycle lane on your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 646, 12.52 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city road in the UK with shops on the right and a sidewalk with a cyclist on the
                        left; the road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line separating the road from a cycle lane/shoulder.
                        Photo 2 shows the same white dashed line next to my car, consisting of long dashes and
                        gaps.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from a parking/stopping area
                        where cars are parked. Photo 2 shows the same white dashed line next to my car,
                        consisting of long dashes and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; my lane is the only main travel lane, bounded by edge lines on both
                        sides. | roles: the white dashed lines fit the role of edge lines separating the
                        travel lane from a cycle lane and a parking area. | markings: no markings in my lane
                        to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white edge line allows crossing to enter the adjacent area if
                        safe.
Step 5  Rule            right_boundary: A dashed white edge line allows crossing to enter the adjacent area if
                        safe.
Step 6  change_left     allowed (correct): allowed by the dashed white left boundary.
Step 6  change_right    allowed (correct): allowed by the dashed white right boundary.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area.
Step 7  Reflect         consistent
Advice                  You are in a single travel lane. You may proceed straight or move left or right across
                        the dashed lines if necessary and safe.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 655, 11.42 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with a pedestrian crossing ahead. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a white solid line along the left edge of the road. Photo 2 shows the
                        same white solid line next to my car and continuing forward.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line that separates my lane from the opposite direction of
                        traffic. Photo 2 shows this white solid line next to my car and continuing forward.
                        white solid, curb no, center_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a zebra crossing (white stripes)
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; I am in a single lane bounded by an edge line on the
                        left and a center line on the right. | roles: the white solid lines fit the roles of
                        edge line and center line respectively. | markings: the crosswalk is consistent with
                        the road layout. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing a solid edge line into the sidewalk/curb is prohibited.
Step 5  Rule            right_boundary: Crossing a solid center line into oncoming traffic is prohibited.
Step 5  Rule            line:crosswalk: Drivers must yield to pedestrians on the crossing.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid edge line with a curb,
                        which prohibits leaving the lane to the left.
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid center line, which
                        prohibits crossing into the opposite lane.
Step 6  go_straight     allowed (contested, correct): no marking prohibits going straight, and the boundaries
                        do not restrict forward movement.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no waiting area is present in my lane.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight, ensuring you yield to any pedestrians using
                        the zebra crossing ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 698, 12.75 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, traveling straight ahead. There are
                        no immediate intersections or ramps visible. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to the car, which continues ahead. Photo 2
                        confirms a white dashed line with several short dashes and gaps.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car, continuing ahead. Photo 2 shows a
                        white dashed line with short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a circular '20' speed limit marking
                        painted on the road surface in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; the
                        left boundary separates my lane from a cycle lane, and the right boundary separates it
                        from another traffic lane. | roles: the white dashed lines fit the roles of a special
                        lane line (cycle lane) and a lane line. | markings: the speed limit marking is
                        consistent with the urban environment. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows crossing into the cycle lane when safe to do
                        so.
Step 5  Rule            right_boundary: A dashed white line allows changing lanes to the right when safe to do
                        so.
Step 5  Rule            text:speed_limit: The marking indicates a maximum speed limit of 20 mph.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white left boundary
                        (special_lane_line).
Step 6  change_right    allowed (correct): allowed by the dashed white right boundary (lane_line).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and the
                        lane does not end.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection governing this
                        action.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection governing this
                        action.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area present.
Step 7  Reflect         consistent
Advice                  You are in a 20 mph zone. You may change lanes to the left or right if safe, but be
                        mindful of the cycle lane on your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3642, out 750, 12.67 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward. There is a junction or
                        intersection ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line next to the car, which then becomes a white dashed
                        line further ahead. Photo 2 shows a white solid line next to the car and a white
                        dashed line slightly further ahead.
                        white solid_dashed (near line solid), curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car and further ahead. Photo 2 shows a
                        white dashed line next to the car and further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left_u_turn (full): Photo 1 and Photo 2 show a white arrow in the lane that
                        points both straight and left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the left boundary is an edge line and the right is a lane line,
                        meaning there is another lane to the right. | roles: the white solid/dashed left
                        boundary and white dashed right boundary fit their roles as edge and lane lines. |
                        markings: the straight-and-left arrow is consistent with the lane's position. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line prohibits crossing; a dashed white line allows
                        crossing.
Step 5  Rule            right_boundary: A dashed white line allows lane changes.
Step 5  Rule            arrow:left_u_turn: The arrow allows the car to either go straight or turn left.
Step 6  change_left     prohibited (contested, label allowed): the left boundary is solid next to the car,
                        which prohibits crossing
Step 6  change_right    allowed (correct): the right boundary is dashed, which allows lane changes
Step 6  go_straight     allowed (correct): the arrow in the lane allows going straight
Step 6  turn_left       allowed (correct): the arrow in the lane allows turning left
Step 6  turn_right      prohibited (correct): the arrow in the lane does not show a right turn, prohibiting it
Step 6  u_turn          not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn left. You may change lanes to
                        the right, but do not cross the solid line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left_u_turn'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation None, contradictions ['rightmost lane, but a lane line on the right',
                        'go_straight allowed although no arrow shows it', 'u_turn not_applicable although an
                        arrow shows it']
Tokens                  in 3642, out 733, 19.73 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city road in the UK with buildings on the left and a residential area on the right;
                        the road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line next to the car, which continues ahead. Photo 2
                        confirms a dashed white line next to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        lane line on the right indicates another lane of the same direction to the right, and
                        an edge line on the left indicates the edge of the roadway. | roles: the white solid
                        line on the left fits the role of an edge line, and the white dashed line on the right
                        fits the role of a lane line. | markings: no markings in my lane to check. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid white edge line which
                        prohibits crossing it
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line which allows
                        changing lanes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may continue straight or change to the right lane if
                        needed; do not cross the solid line on your left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3642, out 645, 12.5 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a junction with traffic lights ahead.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red solid line next to the curb. Photo 2 confirms two red solid lines
                        running along the edge of the road next to the sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the right lane. Photo 2
                        shows a series of white dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left_right (full): Photo 1 and Photo 2 show a white arrow in my lane pointing
                        both straight and left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a red edge line on the left and a white lane line on
                        the right indicate I am in the leftmost lane of a two-lane road. | roles: the red
                        solid edge line and white dashed lane line fit their roles for a UK city road. |
                        markings: the straight-and-left arrow is consistent with being in the leftmost lane at
                        a junction. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The red solid edge line and curb prohibit leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: The white dashed line allows changing lanes to the right.
Step 5  Rule            arrow:left_right: The arrow allows the car to either go straight or turn left at the
                        end of the lane.
Step 6  change_left     prohibited (contested, correct): prohibited by the red solid edge line and curb
Step 6  change_right    allowed (correct): allowed by the white dashed lane line
Step 6  go_straight     allowed (correct): allowed by the straight-and-left arrow
Step 6  turn_left       allowed (correct): allowed by the straight-and-left arrow
Step 6  turn_right      prohibited (correct): prohibited by the straight-and-left arrow
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the left lane; you may proceed straight or turn left. You may change to the
                        right lane if needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left_right'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation None, contradictions ['go_straight allowed although no arrow shows it',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 3642, out 710, 10.9 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, facing forward. The road ahead appears to be a
                        single-lane stretch leading toward a junction or a narrowed section of the road.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, next to a sidewalk. Photo
                        2 shows this line is a single solid white line next to the car, continuing as a solid
                        line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right side that is broken into dashes. Photo 2 shows
                        the line next to the car is a broken white line with long dashes and gaps, continuing
                        as a broken line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left edge line and the right lane line, suggesting there is another lane to
                        the right. | roles: the white solid left boundary fits the role of an edge line, and
                        the white dashed right boundary fits the role of a lane line. | markings: no markings
                        were observed in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid edge line and curb,
                        which prohibits leaving the roadway
Step 6  change_right    allowed (contested, label prohibited): the right_boundary is a dashed lane line, which
                        allows changing lanes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may continue straight or change to the right lane if
                        needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation None, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 3642, out 664, 12.23 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a straight stretch with an intersection
                        further ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the curb. Photo 2 shows a solid white line
                        and a red curb line.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line. Photo 2 shows a broken white line with long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white straight-ahead arrow in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a white edge line on the left and a lane line on the
                        right indicate I am in the leftmost lane of a two-lane road. | roles: the white solid
                        edge line and white dashed lane line fit their roles. | markings: the straight-ahead
                        arrow is consistent with the lane's position. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing a solid edge line into the curb/sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a dashed lane line to change lanes is allowed.
Step 5  Rule            arrow:straight: The lane is designated for going straight.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid edge line and curb,
                        which prohibits leaving the roadway
Step 6  change_right    allowed (correct): the right_boundary is a dashed lane line, which allows changing
                        lanes
Step 6  go_straight     allowed (correct): the arrow:straight in my lane allows going straight
Step 6  turn_left       prohibited (WRONG, label allowed): the arrow:straight in my lane prohibits turning
                        left
Step 6  turn_right      prohibited (correct): the arrow:straight in my lane prohibits turning right
Step 6  u_turn          prohibited (correct): the arrow:straight in my lane prohibits U-turns
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn right, change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation None, contradictions []
Tokens                  in 3642, out 692, 14.12 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a pedestrian crossing and a
                        T-junction where the road ahead ends. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line along the left edge of the road. Photo 2 confirms a
                        white solid line next to the car, which continues forward.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line along the right edge of the road. Photo 2 confirms a
                        white solid line next to the car, which continues forward.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a zebra crossing (white stripes)
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides | roles: the white solid lines on both sides fit the
                        role of edge lines for a single-lane road | markings: the crosswalk is consistent with
                        the road layout | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing the boundary to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing the boundary to the right.
Step 5  Rule            line:crosswalk: Drivers must yield to pedestrians on the crosswalk.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line which
                        prohibits leaving the lane to the left
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid white edge line which
                        prohibits leaving the lane to the right
Step 6  go_straight     not_applicable (contested, label allowed): the road ahead ends at a T-junction, making
                        going straight not applicable
Step 6  turn_left       not_determined: no marking governs this action
Step 6  turn_right      not_determined: no marking governs this action
Step 6  u_turn          not_determined: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and be prepared to stop for pedestrians at the zebra crossing. Since
                        the road ends ahead, you will need to turn left or right at the junction.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 712, 12.71 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, traveling straight ahead. There are buses in the
                        lanes to the left. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a solid white line next to my car.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a red line along the edge of the road next to a curb. Photo 2 shows the
                        red line and the curb clearly.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a special lane line on the left and an edge line on the
                        right indicate I am in the rightmost lane of a two-lane road (where the left is a bus
                        lane). | roles: the solid white line fits the role of a special lane boundary, and the
                        red line fits the role of a road edge in the UK. | markings: no markings are present
                        in my lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line separating a general traffic lane from a bus lane
                        prohibits crossing into the bus lane.
Step 5  Rule            right_boundary: A solid red edge line and curb prohibit leaving the roadway to the
                        right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white special_lane_line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid red edge_line and curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the bus lane to your left or
                        cross the red line to your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 665, 11.72 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward. There is a bus stopped in a lane
                        to the left and other vehicles ahead in the same direction. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        confirms a solid white line next to my car and continuing ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a grey curb and a metal railing on the right side of the road. Photo 2
                        shows the curb and railing immediately to the right of my lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white solid line fits the role of a lane line, and the curb fits the role
                        of an edge line | markings: no markings in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: The curb and railing prohibit leaving the roadway to the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the curb and railing
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not change lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 3642, out 637, 10.33 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, facing straight ahead with other
                        vehicles in front. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the left curb area. Photo 2
                        shows the same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows the head of a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a white edge line on the left and a lane line on the
                        right indicate I am in the leftmost lane of a two-lane road. | roles: the white solid
                        edge line and white dashed lane line fit their roles. | markings: the straight arrow
                        in my lane is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or curb
                        area.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight arrow allows going straight ahead.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid white edge line which
                        prohibits crossing it
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line which allows
                        changing lanes
Step 6  go_straight     allowed (correct): the arrow:straight in my lane allows going straight
Step 6  turn_left       not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  turn_right      not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  u_turn          not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the left lane; you may continue straight or change to the right lane if
                        needed. Do not cross the solid white line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 703, 12.28 s

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
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        index 2 agree with having lane lines on both my left and right. | roles: the white
                        dashed lines fit the role of lane lines. | markings: the straight-ahead arrow is
                        consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left or right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed lane line which allows lane
                        changes.
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line which allows lane
                        changes.
Step 6  go_straight     allowed (correct): the straight-ahead arrow in my lane allows this movement.
Step 6  turn_left       prohibited (correct): the straight-ahead arrow in my lane prohibits turning left.
Step 6  turn_right      prohibited (correct): the straight-ahead arrow in my lane prohibits turning right.
Step 6  u_turn          not_applicable (WRONG, label prohibited): no marking governs this action, but the
                        straight-ahead arrow typically restricts it to the indicated direction.
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane; you may go straight or change lanes. To turn left or
                        right, you must change to the corresponding outer lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 712, 11.32 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward on a multi-lane road with
                        buildings and trees on the sides. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line extending ahead. Photo 2 shows the same solid white
                        line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line. Photo 2 shows a broken white line next to the car
                        with several short dashes and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a lane line on the left and an edge line on the right indicate
                        the rightmost lane of a two-lane road. | roles: the white solid line as a lane line
                        and white dashed line as an edge line are consistent with UK road markings. |
                        markings: no markings in the lane to contradict boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing to change lanes.
Step 5  Rule            right_boundary: A dashed white edge line allows crossing to the shoulder or parking
                        area if safe.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left.
Step 6  change_right    allowed (correct): allowed by the dashed white edge line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no turn arrow in the lane.
Step 6  turn_right      not_applicable: not_applicable as there is no turn arrow in the lane.
Step 6  u_turn          not_applicable: not_applicable as there is no u-turn arrow in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area ahead or to the left.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right to the shoulder; do not cross the solid white line to
                        the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 650, 10.4 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward on a road with buildings and
                        shops on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the curb. Photo 2 confirms a solid white line
                        running along the left edge of the roadway next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating the lane from a parking area or side
                        lane. Photo 2 shows a series of short white dashes with gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; a left edge line and a right lane line indicate a single lane of
                        travel in this direction. | roles: the white solid edge line on the left and white
                        dashed lane line on the right fit their roles. | markings: there are no markings in
                        the lane to contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the curb/sidewalk area.
Step 5  Rule            right_boundary: A dashed white line allows lane changes or moving into the adjacent
                        area if safe.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line and curb
Step 6  change_right    allowed (correct): allowed by the dashed white lane line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no turn arrow
Step 6  turn_right      not_applicable: not_applicable as there is no turn arrow
Step 6  u_turn          not_applicable: not_applicable as there is no u-turn arrow
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right if needed; do not cross the left boundary into
                        the sidewalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3642, out 636, 13.39 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead with
                        buildings on the left and trees on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows the edge of the roadway on the right, bordered by a curb and a line of
                        parked cars. Photo 2 shows a white solid line next to my car, followed by a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        with a curb fits the role of an edge line | markings: no markings in my lane to check
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and curb prohibit leaving the roadway to the
                        right.
Step 6  change_left     allowed (contested, label prohibited): the left boundary is a dashed lane line which
                        allows lane changes
Step 6  change_right    prohibited (WRONG, label allowed): the right boundary is a solid edge line and curb
                        which prohibits leaving the roadway
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of a two-lane road. You may continue straight or change
                        to the left lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 646, 12.68 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with buildings on both sides; the road continues
                        straight ahead with traffic moving in the same direction. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line along the left edge of the road next to the sidewalk.
                        Photo 2 shows the same yellow line close to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line between my lane and the area where other cars are
                        positioned. Photo 2 shows no painted line to the right of the car.
                        none none, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the left edge line and the absence of a right boundary line | roles: the yellow solid
                        edge line on the left fits the role of a road edge/parking restriction line |
                        markings: no markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits crossing into the sidewalk or
                        parking area.
Step 5  Rule            right_boundary: The absence of a line allows lane changes to the right if safe to do
                        so.
Step 6  change_left     prohibited (contested, label not_determined): the left_boundary is a solid yellow edge
                        line which prohibits leaving the roadway
Step 6  change_right    allowed (WRONG, label not_determined): the right_boundary has no marking and no curb,
                        allowing a lane change
Step 6  go_straight     allowed (contested, label not_determined): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in the lane or move to the right if necessary; do not cross the yellow line on
                        the left.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right', 'change_right decided with nothing marked on that side']
Tokens                  in 3642, out 615, 12.39 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward. Ahead is a clear stretch of road
                        with a bus lane to the left. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a white dashed line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line. Photo 2 shows a white dashed line next to the car.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a lane line on the left and an edge line on the right indicate
                        the rightmost lane of two. | roles: the white dashed lines fit the roles of lane line
                        and edge line. | markings: no markings in my lane to check. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed edge line allows moving onto the shoulder or adjacent
                        area to the right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the white dashed lane line
Step 6  change_right    allowed (correct): allowed by the white dashed edge line
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but be aware of the bus lane markings further ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 620, 11.22 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with buildings on both sides and parked cars along
                        the right edge. My car is in the single available driving lane. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a dashed white line separating the road from a sidewalk/parking area.
                        Photo 2 shows the same dashed white line next to my car, consisting of several short
                        white dashes and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a curb and sidewalk on the right. Photo 2 shows the curb and sidewalk
                        immediately to the right of my car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show a yellow box junction (grid) across the
                        lane ahead of my car.; text:other (full): Photo 2 shows the words 'LOADING ONLY'
                        painted in white on the road to the right of my lane, near the curb.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides. | roles: the white dashed line on the left and the
                        curb on the right both fit the role of edge lines for a single-lane road. | markings:
                        the grid area is across the lane, and the 'LOADING ONLY' text is outside my lane in
                        the parking area; these are consistent. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white edge line allows crossing to enter or leave the roadway.
Step 5  Rule            right_boundary: A curb prohibits driving onto the sidewalk.
Step 5  Rule            area:grid: Vehicles must not enter the box junction unless their exit is clear.
Step 5  Rule            text:other: The 'LOADING ONLY' marking governs the parking area to the right, not my
                        lane.
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white edge line.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the curb.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and it
                        is the only lane.
Step 6  turn_left       not_applicable: not_applicable as there is no turn arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no turn arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no u-turn arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no left-turn waiting area or two-way
                          left-turn lane.
Step 7  Reflect         consistent
Advice                  Stay in the current lane to go straight. Do not enter the yellow box junction unless
                        your exit is clear. The area to the right is for loading only.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 836, 20.59 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward. There is a bus ahead in the same
                        direction. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from a bicycle lane, and a solid
                        yellow line at the edge of the curb. Photo 2 shows the white dashed line next to my
                        car and the bicycle symbol and yellow line further left.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from a parking area. Photo 2
                        shows the white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the left boundary is a special lane line for the cycle lane, and the
                        right boundary separates the driving lane from parking. | roles: the white dashed
                        lines fit the roles of lane/special lane boundaries. | markings: no markings in my
                        lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows crossing into the cycle lane if safe to do
                        so.
Step 5  Rule            right_boundary: A dashed white line allows crossing into the parking area if safe to
                        do so.
Step 6  change_left     allowed (contested, label prohibited): the left boundary is a dashed white line, which
                        allows crossing
Step 6  change_right    allowed (correct): the right boundary is a dashed white line, which allows crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a single driving lane. You may proceed straight or change lanes if
                        necessary, but be mindful of the cycle lane to your left and parked cars to your
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3642, out 643, 11.44 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with a pedestrian crossing
                        and a traffic island ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, separating the lane from
                        the sidewalk. Photo 2 shows this line is a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from a traffic island/median. Photo 2
                        shows a solid white line next to the car, which continues ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; it is a single lane bounded by edges on both sides. | roles: the white
                        solid lines correctly serve as edge lines for the roadway. | markings: there are no
                        markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk/shoulder.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the traffic
                        island/median.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line and curb on
                        the left.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb on
                        the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and it
                        is the natural path of the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 642, 12.0 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with shops on both sides; the road continues straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a parking area with cars.
                        Photo 2 shows the same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a cycle lane. Photo 2 shows
                        the same solid white line next to my car.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; it is a single lane bounded by an edge line on the left
                        and a special lane line on the right | roles: the white solid lines fit the roles of
                        edge and special lane boundaries | markings: no markings in my lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the parking area.
Step 5  Rule            right_boundary: A solid white line separating a cycle lane prohibits crossing into the
                        cycle lane unless permitted by signs or for turning.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line which
                        prohibits crossing
Step 6  change_right    prohibited (WRONG, label allowed): the right_boundary is a solid white
                        special_lane_line which prohibits crossing into the cycle lane
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines to the left
                        or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 620, 10.88 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with shops on the left; the road continues
                        straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and double yellow lines along the left edge of the road.
                        Photo 2 confirms the raised curb and the double yellow lines next to my car.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the right lane. Photo 2
                        shows the same white dashed line next to my car, with several dashes and gaps visible.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white straight-ahead arrow in my
                        lane.; symbol:bike (full): Photo 2 shows a bicycle symbol painted in my lane, further
                        ahead of the arrow.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a curb and edge line on the left means I am in the
                        leftmost lane. | roles: the yellow double solid edge line and white dashed lane line
                        fit their roles. | markings: the straight arrow and bike symbol are consistent with a
                        lane that allows going straight. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The curb and double yellow lines mark the edge of the roadway; crossing
                        them to the left is prohibited.
Step 5  Rule            right_boundary: A dashed white line allows lane changes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead.
Step 5  Rule            symbol:bike: The bicycle symbol indicates a cycle lane or shared space, but does not
                        prohibit motor vehicles from going straight.
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb and edge line
Step 6  change_right    allowed (contested, correct): allowed by the dashed white lane line
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow and the left edge
                        boundary
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this
                        movement, but the lane is for straight traffic
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this
                        movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 777, 13.36 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city road in the UK with traffic keeping to the left. The road continues straight
                        ahead with a bus and other vehicles in the distance. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the road edge/shoulder.
                        Photo 2 shows the same white dashed line next to my car, consisting of long dashes and
                        gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed pattern fits both the lane_line and edge_line roles |
                        markings: no markings in my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed edge line allows moving onto the shoulder or leaving
                        the roadway to the right.
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
Tokens                  in 3642, out 630, 11.79 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead with
                        shops and buildings on both sides. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line marking the edge of the roadway, followed by a curb.
                        Photo 2 shows the white solid line and the raised curb immediately to the right of my
                        car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        with a curb fits the role of an edge line | markings: no markings in my lane to check
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and curb prohibit leaving the roadway to the
                        right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed line, which allows lane changes
Step 6  change_right    prohibited (WRONG, label allowed): the right boundary is a white solid line and a
                        curb, which prohibits leaving the roadway
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may continue straight or change
                        to the left lane if needed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 643, 11.86 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, driving forward with a clear stretch
                        of road ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 confirms a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to a raised curb and a metal fence. Photo 2
                        confirms a white solid line and a raised curb immediately to the right of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a circular marking with the number
                        '20' painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right | roles: the white
                        dashed line fits a lane_line role and the white solid line fits an edge_line role |
                        markings: the speed limit marking is consistent with the lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and curb prohibit leaving the roadway to the
                        right.
Step 5  Rule            text:speed_limit: The speed limit marking indicates the maximum speed allowed in this
                        area.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but do
                        not cross the right boundary. Observe the 20 mph speed limit.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:speed_limit'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3642, out 736, 13.87 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with buildings on both sides; the road continues straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a grey curb and a white line next to it. Photo 2 shows a raised grey
                        curb and a white solid line painted on the road just inside the curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from a parking area or another
                        lane. Photo 2 shows a white dashed line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a white solid edge line on the left and a dashed lane
                        line on the right indicate I am in the leftmost lane of my direction. | roles: the
                        white solid edge line and white dashed lane line fit their respective roles. |
                        markings: there are no markings in my lane to contradict. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid edge line and curb prohibit leaving the roadway to the left.
Step 5  Rule            right_boundary: A dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid edge line and curb which
                        prohibits leaving the road.
Step 6  change_right    allowed (correct): the right_boundary is a dashed lane line which allows changing
                        lanes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You can continue straight in your lane or change to the right. Do not cross the left
                        boundary into the curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3642, out 629, 11.26 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with shops on both sides; the road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a sidewalk with pedestrians and shops. Photo 2
                        confirms the raised curb immediately to the left of my car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a wide open asphalt area with parked cars further ahead, but no painted
                        lines are visible next to my car or in the immediate foreground. Photo 2 also shows no
                        painted lines to the right.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show a white word 'BUS' painted on the road
                        surface in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left curb and the absence of a right lane line. | roles: the left curb acts
                        as an edge_line; the right side is an open roadway edge. | markings: the 'BUS' text
                        indicates this is a bus lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing a raised curb is prohibited.
Step 5  Rule            right_boundary: Changing right is allowed as there is no physical barrier or painted
                        line prohibiting it.
Step 5  Rule            text:bus: This lane is reserved for buses; ordinary cars are prohibited from driving
                        in it during its operational hours.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a raised curb which prohibits
                        leaving the lane to the left.
Step 6  change_right    allowed (correct): the right_boundary has no markings or curbs that prohibit changing
                        right.
Step 6  go_straight     prohibited (contested, label allowed): the text:bus marking indicates this is a
                        reserved lane, prohibiting ordinary cars from using it to go straight.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane. You should change right into the general traffic lane
                        immediately.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation None, contradictions
                        ['change_right decided with nothing marked on that side', 'go_straight decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 3642, out 709, 10.69 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward on a street lined with shops and
                        parked cars. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the driving lane from a parking/stopping
                        area. Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the driving lane from a cycle lane. Photo
                        2 confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the car is in a single driving lane bounded by edge lines on both
                        sides. | roles: the solid white lines correctly serve as edge lines for the driving
                        lane. | markings: no markings are present in the lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the parking area.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the cycle lane.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white line which
                        prohibits crossing it
Step 6  change_right    prohibited (WRONG, label allowed): the right_boundary is a solid white line which
                        prohibits crossing it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines to the left
                        or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 601, 10.35 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city road in the UK with traffic keeping to the left. My car is in a lane with a bus
                        lane to its left. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a single solid white line next to my car.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the rightmost lane. Photo 2
                        shows a series of white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a special lane line on the left and a lane line on the
                        right place me in the second lane from the left. | roles: the solid white line for a
                        bus lane boundary and dashed white line for a lane change boundary fit their roles. |
                        markings: no markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line separating a general lane from a bus lane prohibits
                        crossing into the bus lane.
Step 5  Rule            right_boundary: A dashed white line allows lane changes into the adjacent lane.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white line separating a
                        bus lane, which prohibits crossing into it.
Step 6  change_right    allowed (correct): the right_boundary is a dashed white line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a general traffic lane. You may change lanes to the right, but you must not
                        enter the bus lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3642, out 645, 11.97 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with shops on the right; the road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road next to a sidewalk. Photo 2
                        shows this line is a solid white line next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line along the right edge of the road. Photo 2 shows this line
                        is a solid white line next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): Photo 1 and Photo 2 show white zigzag lines painted on both sides
                        of the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both left and right. | roles: the solid white edge lines fit
                        the role of roadway boundaries. | markings: the zigzag lines are typical for approach
                        to pedestrian crossings or parking restrictions and do not contradict the boundaries.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            symbol:other: Zigzag lines typically indicate a no-parking zone or approach to a
                        crossing and do not govern lane movement.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid edge line which
                        prohibits leaving the roadway.
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid edge line which
                        prohibits leaving the roadway.
Step 6  go_straight     allowed (contested, correct): no marking prohibits going straight in this single-lane
                        road.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines or
                        park in the zigzag marked areas.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 3642, out 695, 18.96 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with
                        traffic signals. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a raised curb and sidewalk. Photo 2 confirms
                        a solid white line and a raised curb immediately to the right of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2 shows a white arrow pointing right in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a lane line on the left and an edge line on the right
                        indicate I am in the rightmost lane of a two-lane road. | roles: the white dashed lane
                        line and white solid edge line fit their roles. | markings: the right-turn arrow in
                        the rightmost lane is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes across it.
Step 5  Rule            right_boundary: A solid white edge line and curb prohibit leaving the roadway to the
                        right.
Step 5  Rule            arrow:merge_right: The arrow indicates that the lane is for turning right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line on the left.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and raised
                        curb on the right.
Step 6  go_straight     prohibited (correct): prohibited by the right-turn arrow in my lane.
Step 6  turn_left       prohibited (correct): prohibited by the right-turn arrow in my lane.
Step 6  turn_right      allowed (correct): allowed by the right-turn arrow in my lane.
Step 6  u_turn          prohibited: prohibited by the right-turn arrow in my lane.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a right-turn only lane. If you intend to go straight or turn left, you must
                        change to the left lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:right']), actions True, unsafe [], citation
                        None, contradictions ['go_straight, turn_left, turn_right, u_turn decided without an
                        arrow or prohibited-movement marking']
Tokens                  in 3642, out 719, 12.72 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with traffic moving on the left. My car is in a
                        lane that continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a solid white line next to my car and continuing ahead.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from another lane. Photo 2 shows
                        a dashed white line next to my car with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a special lane line on the left and a lane line on the
                        right place me in the second lane from the left. | roles: the solid white line for a
                        bus lane and dashed white line for a lane change fit their roles. | markings: no
                        markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line separating a bus lane prohibits ordinary vehicles
                        from entering the bus lane.
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
Advice                  You are in the general traffic lane. You may go straight or change to the right lane,
                        but you must not enter the bus lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3642, out 643, 11.54 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A residential urban street in the UK with parked cars on the right and a bus lane on
                        the left; the road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from a bus lane. Photo 2 confirms
                        a single solid yellow line next to my car.
                        yellow solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the roadway from parked cars. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the word 'BUS' painted in yellow in the lane to the
                        left of my lane, but not in my lane. Photo 1 shows the word 'BUS' is in the left lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; my
                        lane is the only general traffic lane, bounded by a special lane line on the left and
                        an edge line on the right. | roles: the yellow solid line fits the role of a special
                        lane boundary (bus lane), and the white solid line fits the role of an edge line. |
                        markings: the 'BUS' text is in the adjacent special lane, not my lane, which is
                        consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing into the bus lane.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the parking/shoulder
                        area.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow special lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the bus lane to your left or the
                        parking area to your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3642, out 720, 13.05 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with shops on both sides; the road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a parking area with cars.
                        Photo 2 confirms a single solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a cycle lane. Photo 2
                        confirms a single solid white line next to my car.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; it is a single lane bounded by an edge line on the left and a special
                        lane line on the right | roles: the solid white lines fit the roles of edge and
                        special lane boundaries | markings: no markings in the lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the parking area.
Step 5  Rule            right_boundary: A solid white line separating a cycle lane prohibits crossing into the
                        cycle lane unless necessary or permitted by signs.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line which
                        prohibits crossing
Step 6  change_right    prohibited (WRONG, label allowed): the right_boundary is a solid white
                        special_lane_line which prohibits crossing into the cycle lane
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines to the left
                        or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 617, 10.57 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving straight ahead on a multi-lane street
                        with shops and parked cars on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane on the left. Photo
                        2 confirms a solid white line immediately to the left of the car.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the rightmost lane. Photo 2
                        shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show the words 'BUS LANE' painted in the lane to
                        the left of my lane, not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a special lane line on the left and a lane line on the right. | roles: the
                        solid white line on the left fits a special lane boundary, and the dashed white line
                        on the right fits a lane separator. | markings: the 'BUS LANE' text is in the adjacent
                        lane, which is consistent with the left boundary being a special_lane_line. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A solid white line marking a bus lane prohibits ordinary vehicles from
                        entering the bus lane.
Step 5  Rule            right_boundary: A dashed white line allows lane changes into the adjacent lane.
Step 5  Rule            text:bus: The bus lane is reserved for buses and authorized vehicles.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white special_lane_line and
                        the bus lane marking.
Step 6  change_right    allowed (correct): allowed by the dashed white lane_line.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right lane if needed; do not enter the bus lane to
                        your left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation None, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 3642, out 756, 12.91 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving on the left side of the road. The road
                        ahead appears to be a single-lane street with parked cars on the right. (lanes 1, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road next to a sidewalk.
                        Photo 2 confirms a single solid yellow line next to the curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, but parked cars and a curb further ahead.
                        Photo 2 shows no painted line next to the car.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the left edge line and the absence of a lane line on the right. | roles:
                        the yellow solid edge line on the left is consistent with UK parking restrictions on
                        the road edge. | markings: no markings are present in the lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid yellow edge line indicates parking restrictions; crossing it to
                        leave the roadway is generally prohibited unless for emergency or specific access.
Step 5  Rule            right_boundary: The absence of a line on the right indicates the edge of the drivable
                        area or a parking area.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid yellow edge line with a
                        curb, which prohibits leaving the roadway to the left
Step 6  change_right    allowed (WRONG, label not_determined): no marking governs this action
Step 6  go_straight     allowed (contested, correct): no marking restricts carrying on straight along the lane
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not cross the yellow line on the
                        left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 3642, out 652, 11.8 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving forward. The road ahead appears to be a
                        single lane in this direction, bordered by a parking area on the right. (lanes 1, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the opposite direction of
                        traffic. Photo 2 confirms a single solid white line next to my car.
                        white solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from a parking/stopping area on the
                        right. Photo 2 shows a solid white line next to my car, which then becomes a short
                        dashed line further ahead near a traffic island.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the center_line on the left and edge_line on the right | roles: the white solid
                        center_line and white edge_line fit their roles | markings: no markings in lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white center line prohibits crossing into the opposite lane of
                        traffic.
Step 5  Rule            right_boundary: A solid white edge line prohibits leaving the roadway into the parking
                        area.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white center line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          prohibited: prohibited by the solid white center line
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 3642, out 640, 12.02 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with buildings on both sides; the road continues straight
                        ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating the road from the sidewalk. Photo 2 shows
                        a white solid line next to my car, extending forward.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle with the number '20'
                        inside it painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line and the white solid line
                        fits the role of an edge line | markings: the speed limit marking is consistent with
                        the lane boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            text:speed_limit: The speed limit marking indicates the maximum speed allowed in this
                        area but does not govern lane movements.
Step 6  change_left     allowed (contested, correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line and the
                        presence of a curb
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of a two-lane road. You may go straight or change to the
                        left lane, but do not cross the right boundary into the sidewalk. Observe the 20 mph
                        speed limit.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 748, 12.7 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward. The road ahead appears to be a
                        single lane in this direction, though it is marked with zig-zag lines. (lanes 1, mine
                        1, full)
Step 2  Left            Photo 1 shows a white line that zig-zags along the left edge of the road next to a
                        sidewalk. Photo 2 confirms the white zig-zag pattern next to the car and the presence
                        of a raised curb.
                        white zigzag, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line that zig-zags along the right side of the lane. Photo 2
                        shows the white zig-zag line next to the car and a white car driving in the opposite
                        direction (since traffic is on the left, this is the center of the road).
                        white zigzag, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left edge line and right center line | roles: the white zig-zag lines are
                        consistent with UK road markings for approach to pedestrian crossings or hazards |
                        markings: no markings in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The left edge line and curb prohibit leaving the roadway to the left.
Step 5  Rule            right_boundary: The zig-zag center line prohibits overtaking or parking in this area.
Step 6  change_left     prohibited (contested, correct): the left_boundary is an edge_line with a curb, which
                        prohibits leaving the road
Step 6  change_right    prohibited (contested, correct): the right_boundary is a center_line with a zig-zag
                        pattern, which prohibits crossing into the opposite traffic lane
Step 6  go_straight     allowed (contested, correct): no marking prohibits going straight
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not overtake or cross the zig-zag lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3642, out 674, 11.57 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with traffic keeping to the left. My car is in a
                        single lane moving forward, with a red bus to the left and parked cars to the right.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to the bus. Photo 2 confirms a white dashed
                        line with visible gaps and dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line near the curb. Photo 2 shows a yellow solid line
                        running along the edge of the road next to a raised curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and index 1 agree
                        with a lane line on the left and an edge line on the right | roles: the white dashed
                        line fits a lane line and the yellow solid line fits a curb-side edge line | markings:
                        no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A yellow solid line at the edge of the road prohibits crossing into
                        the curb/parking area.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the yellow solid edge line and the
                        raised curb
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the yellow line to
                        the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 3642, out 639, 10.57 s
```
