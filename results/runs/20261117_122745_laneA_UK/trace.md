# Reasoning of lane run 20261117_122745_laneA_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a junction with a red bus and other
                        vehicles ahead. (lanes 2, mine 1, full)
Step 2  Left            A red line is painted along the edge of the road next to the sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The red solid
                        edge line and white dashed lane line fit their respective roles. | markings: There are
                        no markings in my lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: The red edge line and curb prohibit leaving the roadway to the left.
Step 5  Rule            right_boundary: The white dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a red solid edge line and
                        curb, which prohibits leaving the road.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a white dashed lane line,
                        which allows lane changes.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the right lane. Do not cross the red line on
                        the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe ['change_right'],
                        citation None, contradictions []
Tokens                  in 2956, out 610, 10.68 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with traffic keeping to the left; the road
                        continues straight ahead with some lane markings and a white van approaching from the
                        opposite direction. (lanes 1, mine 1, full)
Step 2  Left            A grey concrete curb separates the road from a sidewalk and a cycle lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left curb (edge) and right
                        dashed line (center). | roles: The white dashed line is consistent with a center line
                        in the UK. | markings: No markings are present in the lane. | unseen: No attributes
                        were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a dashed center line is allowed for overtaking or turning if
                        safe to do so.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a dashed center line,
                        which allows crossing into the opposite lane when safe.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to overtake if
                        the road ahead is clear.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 612, 8.68 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on an urban road in the UK, facing a junction with buildings and
                        pedestrians ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from a cycle lane and the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the white dashed
                        line on the left and the solid edge line on the right. | roles: The white dashed line
                        fits the role of a lane line, and the white solid line fits the role of an edge line.
                        | markings: The straight arrow is consistent with the lane boundaries. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows lane changes to the left.
Step 5  Rule            right_boundary: A solid white line prohibits crossing into the cycle lane or onto the
                        curb.
Step 5  Rule            arrow:straight: The straight arrow allows going straight and prohibits turning left or
                        right.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows lane
                        changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white line and a
                        curb, which prohibits crossing.
Step 6  go_straight     allowed (correct): The straight arrow in my lane allows this movement.
Step 6  turn_left       prohibited (correct): The straight arrow in my lane prohibits turning left.
Step 6  turn_right      prohibited (correct): The straight arrow in my lane prohibits turning right.
Step 6  u_turn          prohibited (correct): The straight arrow in my lane prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left, change to the left lane
                        across the dashed line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 666, 10.59 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with shops on the left and houses on the right; the
                        road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Two solid yellow lines separate the roadway from the sidewalk on the left.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           A dashed white line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the left edge line and right
                        center line. | roles: The double yellow edge line and dashed white center line fit
                        their roles for a UK road. | markings: There are no markings in my lane to contradict.
                        | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mark the edge of the carriageway and prohibit
                        parking/stopping; crossing them to leave the road is prohibited.
Step 5  Rule            right_boundary: A dashed white center line allows crossing for overtaking or turning
                        if safe to do so.
Step 6  change_left     prohibited (contested, correct): The left boundary is a double yellow edge line with a
                        curb, which prohibits leaving the roadway.
Step 6  change_right    allowed (correct): The right boundary is a dashed white center line, which allows
                        crossing into the opposite lane for overtaking or turning.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane to go straight. You may cross the center line to the right to
                        overtake or turn if the road is clear.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 615, 9.55 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a junction with a pedestrian
                        crossing and a narrow road ahead. (lanes 1, mine 1, full)
Step 2  Left            A raised stone curb separates the road from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A raised stone curb separates the road from the sidewalk on the right.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): A series of short, white dashed lines forming a pedestrian
                        crossing across the lane.
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the presence of curbs on
                        both sides. | roles: The curbs correctly serve as edge boundaries for a single-lane
                        road. | markings: The crosswalk is a standard marking across the lane and does not
                        contradict the boundaries. | unseen: No attributes were reported without being
                        visible. | result: consistent
Step 5  Rule            left_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 5  Rule            line:crosswalk: The car must yield to pedestrians crossing the road.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the lane to the left.
Step 6  change_right    prohibited (contested, correct): The right boundary is a curb, which prohibits leaving
                        the lane to the right.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight, and the lane
                        continues forward.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight, yielding to any pedestrians on the
                        crosswalk.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 647, 8.8 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with houses on the left and parked vehicles on the
                        right; the road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Two solid red lines are painted along the left edge of the roadway next to the
                        sidewalk.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from a parking area where cars are stopped.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and the right
                        lane line separating the driving lane from parking. | roles: The double red lines on
                        the left act as an edge line (no stopping), and the dashed white line on the right
                        acts as a lane line. | markings: There are no markings in my lane to contradict the
                        boundaries. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: Double red lines indicate no stopping at any time and prohibit crossing
                        the boundary to the left.
Step 5  Rule            right_boundary: A dashed white line allows lane changes to the right if safe to do so.
Step 6  change_left     prohibited (contested, correct): The left boundary is a double solid red edge line
                        with a curb, which prohibits leaving the lane to the left.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows changing to
                        the right.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may move to the right to overtake parked
                        vehicles if there is sufficient space and it is safe to do so.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 2956, out 656, 11.28 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead with
                        buildings on the right and a park area on the left. (lanes 3, mine 1, full)
Step 2  Left            A solid white line separates the roadway from a blue-painted bicycle lane and a curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A dashed white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 agree with the left boundary being
                        an edge_line and the right boundary being a lane_line. | roles: The solid white edge
                        line and dashed white lane line fit their respective roles. | markings: There are no
                        markings in my lane to contradict. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the bicycle lane or
                        shoulder.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white edge line, which
                        prohibits crossing it.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: No arrow governs this action.
Step 6  u_turn          not_applicable: No arrow governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not enter the bicycle lane on your left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 615, 9.41 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city road in the United Kingdom with shops on the right; the road continues straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            A white dashed line separates my lane from a cycle lane or shoulder on the left.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from a parking area or opposite traffic lane on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 are consistent with the boundaries; the left
                        is an edge line and the right is a lane line (though it looks like a parking
                        boundary). | roles: The white dashed patterns fit the roles of edge and lane lines. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white edge line allows crossing into the adjacent area if
                        safe.
Step 5  Rule            right_boundary: A dashed white line allows changing lanes or crossing into the
                        adjacent area if safe.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight in your lane or change lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 2956, out 590, 10.63 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with a pedestrian crossing ahead. (lanes 1, mine 1,
                        full)
Step 2  Left            A grey concrete curb separates the road from a sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        line:crosswalk (full): A zebra crossing with white stripes across the road.
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the left curb and right center
                        line. | roles: The white dashed line is consistent with a center line in the UK. |
                        markings: The crosswalk is a standard road feature and does not contradict boundaries.
                        | unseen: No attributes were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a dashed center line is allowed for overtaking or turning if
                        safe.
Step 5  Rule            line:crosswalk: Vehicles must stop for pedestrians crossing the road.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a dashed center line,
                        which allows crossing into the opposite lane if safe.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight, and the lane does
                        not end.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight, but be prepared to stop for the pedestrian
                        currently using the zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 632, 11.04 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road in the UK, traveling forward with a residential
                        area and shops on the right. (lanes 1, mine 1, full)
Step 2  Left            A white dashed line separates my lane from a cycle lane on the left.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a special lane
                        line on the left and a center line on the right. | roles: The white dashed patterns
                        for both the special lane line and center line are consistent with UK road markings. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being visible. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows crossing into the cycle lane when safe and
                        permitted.
Step 5  Rule            right_boundary: A dashed white center line allows crossing into the opposite lane for
                        overtaking when safe and permitted.
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed white line, which
                        allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a dashed white center line, which allows
                        crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight in your lane. You can change lanes to the left or right if
                        necessary and safe to do so.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['text:speed_limit']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 602, 10.71 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city road in the UK with shops on the left; the road continues straight ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight ahead with a branch to the
                        left.
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with a lane line on the
                        left and an edge line on the right. | roles: The white dashed line fits a lane line
                        and the white solid line fits an edge line. | markings: The straight-and-left arrow is
                        consistent with the lane boundaries. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows crossing for lane changes.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk.
Step 5  Rule            arrow:straight_left: This arrow allows the vehicle to either go straight or turn left
                        at the end of the lane.
Step 6  change_left     allowed (contested, correct): The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line and a
                        curb, which prohibits leaving the roadway.
Step 6  go_straight     allowed (correct): The arrow in my lane allows going straight.
Step 6  turn_left       allowed (correct): The arrow in my lane allows turning left.
Step 6  turn_right      prohibited (correct): The arrow in my lane does not show a right turn, prohibiting it.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action, but the
                        arrow does not explicitly allow it.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or turn left. You may change to the left lane if needed, but
                        do not cross the right boundary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 678, 18.99 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A two-way urban road in the UK with buildings on the left and a sidewalk on the right;
                        the road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A white dashed line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the edge of the roadway next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the center line on the left and
                        edge line on the right. | roles: The white dashed center line and white solid edge
                        line fit their roles for a single-lane road in this direction. | markings: There are
                        no markings in my lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed center line allows crossing for overtaking or turning if safe.
Step 5  Rule            right_boundary: A solid edge line prohibits crossing into the sidewalk or shoulder
                        area.
Step 6  change_left     allowed (correct): The dashed center line allows crossing into the opposite lane for
                        overtaking or turning.
Step 6  change_right    prohibited (WRONG, label allowed): The solid edge line and curb prohibit crossing to
                        the right.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight in this lane.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight or move left to overtake if the road is clear; do not cross
                        the solid line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 595, 10.03 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a T-junction or intersection ahead. (lanes
                        2, mine 1, full)
Step 2  Left            A solid red line is painted along the left edge of the roadway, separating it from the
                        sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 agree with the left edge line
                        and right lane line. | roles: The red solid edge line and white dashed lane line fit
                        their roles. | markings: The straight arrow is consistent with the lane boundaries. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Crossing a solid edge line into the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a dashed lane line to change lanes is allowed.
Step 5  Rule            arrow:straight: The lane is designated for going straight.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid red edge line, which
                        prohibits leaving the roadway.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane line, which allows
                        changing lanes.
Step 6  go_straight     allowed (correct): The straight arrow in the lane allows going straight.
Step 6  turn_left       prohibited (WRONG, label allowed): The straight arrow in the lane prohibits turning
                        left.
Step 6  turn_right      prohibited (correct): The straight arrow in the lane prohibits turning right.
Step 6  u_turn          prohibited (correct): The straight arrow in the lane prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn right, change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation None, contradictions []
Tokens                  in 2956, out 641, 10.56 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, facing forward with a road ahead that appears
                        to be a single lane in this direction. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a sidewalk/parking area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a bicycle lane on the right.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and right
                        special lane line. | roles: The solid white lines fit the roles of edge line and
                        special lane line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk or parking
                        area.
Step 5  Rule            right_boundary: A solid white line separating a bicycle lane prohibits crossing into
                        the bicycle lane.
Step 6  change_left     prohibited (contested, correct): The left_boundary is a solid white edge line which
                        prohibits crossing it.
Step 6  change_right    prohibited (contested, correct): The right_boundary is a solid white special_lane_line
                        which prohibits crossing into the bicycle lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 595, 10.65 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, facing straight ahead towards a
                        distant intersection. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates the roadway from a sidewalk with a metal railing.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A dashed white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        an edge_line and the right boundary being a lane_line. | roles: The solid white edge
                        line and dashed white lane line are consistent with their roles. | markings: The
                        straight-ahead arrow is consistent with the lane's boundaries. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Crossing a solid white edge line to enter the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a dashed white lane line to change lanes is allowed.
Step 5  Rule            arrow:straight: The lane is designated for going straight.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white edge line, which
                        prohibits leaving the roadway.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane line, which allows
                        changing lanes to the right.
Step 6  go_straight     allowed (correct): The lane contains a straight-ahead arrow, which allows going
                        straight.
Step 6  turn_left       prohibited (WRONG, label allowed): The lane contains a straight-ahead arrow, which
                        prohibits turning left.
Step 6  turn_right      prohibited (correct): The lane contains a straight-ahead arrow, which prohibits
                        turning right.
Step 6  u_turn          prohibited (correct): The lane contains a straight-ahead arrow, which prohibits
                        U-turns.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present in the photo.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn right, change to the rightmost
                        lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation None, contradictions []
Tokens                  in 2956, out 680, 11.09 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a pedestrian crossing and a
                        T-junction or intersection ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from the sidewalk and parked cars.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from the opposite direction of traffic.
                        white solid, curb no, center_line, evidence full
Step 3  Markings        line:crosswalk (full): A zebra crossing with white stripes across the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and right
                        center line. | roles: The white solid lines fit the roles of edge line and center line
                        in a narrow city street. | markings: The crosswalk is a standard marking across the
                        lane. | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Crossing a solid white edge line into the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a solid white center line into oncoming traffic is
                        prohibited.
Step 5  Rule            line:crosswalk: Drivers must yield to pedestrians on the zebra crossing.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white edge line, which
                        prohibits leaving the lane to the left.
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white center line,
                        which prohibits leaving the lane to the right.
Step 6  go_straight     allowed (contested, correct): No arrow restricts going straight, and the lane
                        continues forward.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in the lane.
Step 7  Reflect         consistent
Advice                  Stay in your lane and be prepared to stop for pedestrians at the zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 642, 11.4 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, looking ahead at a stretch of road with buses in
                        the left lane. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the bus lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A solid red line marks the edge of the roadway on the right.
                        other solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        special lane line on the left and an edge line on the right. | roles: The solid white
                        line fits the role of a special lane boundary, and the red line fits the role of a
                        roadway edge. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A solid white line separating a special lane prohibits crossing into
                        that lane.
Step 5  Rule            right_boundary: A solid edge line prohibits leaving the roadway to the right.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid special lane line, which
                        prohibits crossing into the bus lane.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid edge line, which
                        prohibits leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; do not enter the bus lane on the left or cross
                        the red line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 609, 9.96 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in the United Kingdom with buildings on both sides; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A grey metal railing and a curb form the right edge of the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with a lane line on the
                        left and an edge line on the right. | roles: The solid white line is a standard lane
                        line; the curb/railing is a standard edge boundary. | markings: There are no markings
                        in my lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: The curb and railing prohibit leaving the roadway to the right.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line, which
                        prohibits lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb and railing, which
                        prohibits leaving the road.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to the left are prohibited by the
                        solid white line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2956, out 584, 10.07 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, facing straight ahead with other
                        vehicles in front. (lanes 2, mine 1, full)
Step 2  Left            A double red solid line is visible on the far left, separated from my lane by a white
                        dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 are consistent with having a
                        lane line on my right and a lane line on my left. | roles: The white dashed lines on
                        both sides are consistent with lane lines separating traffic in the same direction. |
                        markings: The straight-ahead arrow is consistent with the lane boundaries. | unseen:
                        No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows changing lanes to the left.
Step 5  Rule            right_boundary: A dashed white line allows changing lanes to the right.
Step 5  Rule            arrow:straight: The arrow allows going straight ahead but prohibits turning left or
                        right from this lane.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows lane
                        changes.
Step 6  go_straight     allowed (correct): The arrow in my lane explicitly allows going straight.
Step 6  turn_left       prohibited (correct): The arrow in my lane only shows straight, prohibiting turns.
Step 6  turn_right      prohibited (correct): The arrow in my lane only shows straight, prohibiting turns.
Step 6  u_turn          prohibited (correct): No marking governs a U-turn, but the straight arrow prohibits
                        it.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change lanes to the left or right if needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 2956, out 671, 11.59 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a T-junction or intersection ahead. (lanes
                        3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both my left and right. | roles: The white dashed lines are consistent with lane
                        lines in the UK. | markings: The straight arrow is consistent with a central lane in a
                        three-lane configuration. | unseen: No attributes were reported without being visible.
                        | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows changing lanes to the left.
Step 5  Rule            right_boundary: A dashed white line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight arrow allows going straight and prohibits turning left or
                        right from this lane.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows lane
                        changes.
Step 6  go_straight     allowed (correct): The straight arrow in my lane allows this movement.
Step 6  turn_left       prohibited (correct): The straight arrow in my lane prohibits turning left.
Step 6  turn_right      prohibited (correct): The straight arrow in my lane prohibits turning right.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action, but the
                        straight arrow typically restricts it to straight movement.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, change to the
                        corresponding outer lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 655, 11.1 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom with buildings and shops on the left and
                        trees on the right; the road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway next to a sidewalk with trees.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk area.
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed white line, which
                        allows lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line and a
                        curb, which prohibits leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may continue straight or change
                        to the left lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 617, 10.86 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, looking ahead at a stretch of road with a bus
                        lane to the left. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from a bus lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the right edge of the roadway.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        lane line on the left and an edge line on the right. | roles: The white dashed
                        patterns fit the roles of a lane line and an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows crossing for lane changes.
Step 5  Rule            right_boundary: A dashed white edge line allows crossing to the shoulder or edge of
                        the road.
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed white line, which
                        allows lane changes.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes. Note that the lane to your left is a bus
                        lane; check local signage for restrictions before entering it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 596, 10.3 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           An urban road in the United Kingdom with traffic keeping to the left; the road ahead
                        leads to a junction with a pedestrian crossing and a traffic signal. (lanes 1, mine 1,
                        full)
Step 2  Left            A solid white line separates the lane from a sidewalk and a cycle lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a parking area and the opposite traffic
                        direction.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): A white zig-zag line pattern across the lane before the
                        crossing.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the edge lines on both sides. |
                        roles: The solid white lines on both sides fit the role of edge lines for a single-
                        lane road. | markings: The zig-zag lines are consistent with a pedestrian crossing
                        area in the UK. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk or cycle
                        lane.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the parking area or
                        opposite lane.
Step 5  Rule            line:crosswalk: Zig-zag lines indicate a pedestrian crossing area where stopping is
                        prohibited unless for pedestrians.
Step 6  change_left     prohibited (contested, correct): The left_boundary is a solid white edge line, which
                        prohibits crossing it.
Step 6  change_right    prohibited (contested, correct): The right_boundary is a solid white edge line, which
                        prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop or park in the zig-zag area before
                        the pedestrian crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2956, out 691, 11.26 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with shops on the left; the road continues straight ahead.
                        (lanes 2, mine 1, full)
Step 2  Left            A raised curb separates the road from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge and the right boundary being a lane line. | roles: The white dashed line
                        is consistent with a lane line separating traffic in the same direction. | markings:
                        The straight arrow is consistent with the lane's path. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a dashed white line to change lanes is allowed.
Step 5  Rule            arrow:straight: The lane is designated for going straight.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (contested, correct): The right boundary is a dashed white line, which allows
                        changing lanes.
Step 6  go_straight     allowed (correct): The straight arrow in my lane allows this movement.
Step 6  turn_left       prohibited (correct): The straight arrow in my lane prohibits turning left.
Step 6  turn_right      prohibited (correct): The straight arrow in my lane prohibits turning right.
Step 6  u_turn          prohibited (correct): The straight arrow in my lane prohibits a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn right, change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 2956, out 638, 10.9 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with buildings on both sides; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from another lane of my direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with a lane line on the
                        left and an edge line on the right. | roles: The white dashed line fits the role of a
                        lane line, and the white solid line fits the role of an edge line. | markings: There
                        are no markings in my lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk to the right.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows lane
                        changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line and a
                        curb, which prohibits leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the left lane. Do not
                        cross the solid line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 610, 10.58 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, heading towards a straight stretch
                        with buildings and a cinema on the right. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from a sidewalk and a metal railing.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: The white dashed line fits a lane line and the
                        white solid line fits an edge line. | markings: There are no markings in my lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A dashed white line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows lane
                        changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line and a
                        curb, which prohibits leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the left lane. Do not
                        cross the solid line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 618, 8.45 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from another lane of my direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway, with a parking/stopping area to the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the white dashed
                        line on the left and the white solid edge line on the right. | roles: The white dashed
                        line fits the role of a lane line, and the white solid line fits the role of an edge
                        line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the area to the right.
Step 6  change_left     allowed (contested, label prohibited): The white dashed lane line allows changing to
                        the left.
Step 6  change_right    prohibited (WRONG, label allowed): The white solid edge line prohibits changing to the
                        right.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the solid white
                        line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 593, 18.24 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city road in the UK with buildings on the left and trees on the right; the road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane to the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A dashed white line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        special lane line on the left and a center line on the right. | roles: The solid white
                        line for a bus lane and dashed white line for a center line fit their roles. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A solid white line marking a bus lane prohibits ordinary vehicles from
                        entering it.
Step 5  Rule            right_boundary: A dashed white center line allows crossing for overtaking or turning
                        if safe to do so.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line marking a bus
                        lane, which prohibits entry.
Step 6  change_right    allowed (correct): The right boundary is a dashed white center line, which allows
                        crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right if necessary; do not enter the bus lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 601, 10.32 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with shops on the right; the road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A grey concrete curb separates the road from a sidewalk and parked cars.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A grey concrete curb separates the road from a sidewalk with shops and scooters.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the presence of curbs on
                        both sides. | roles: The curbs correctly serve as edge boundaries for a single-lane
                        road. | markings: There are no markings in the lane to contradict the boundaries. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    prohibited (contested, correct): The right boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not drive onto the sidewalks on
                        either side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 564, 18.03 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom with traffic keeping to the left. The road
                        continues straight ahead towards a signalized intersection. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A grey raised curb and a metal fence form the right edge of the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight and slightly right is painted
                        in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with a lane line on the
                        left and an edge line on the right. | roles: The white dashed line fits the role of a
                        lane line, and the curb fits the role of an edge line. | markings: The straight arrow
                        is consistent with the lane boundaries and the road layout. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A curb prohibits leaving the roadway to the right.
Step 5  Rule            arrow:straight: The straight arrow allows going straight ahead.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows lane
                        changes.
Step 6  change_right    prohibited (contested, correct): The right boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  go_straight     allowed (WRONG, label prohibited): The arrow in my lane allows going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      prohibited (WRONG, label allowed): The arrow in my lane only shows straight,
                        prohibiting turns.
Step 6  u_turn          not_applicable: No marking governs this action, but the arrow only allows straight.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction; you may go straight or change to the
                        left lane. Do not attempt to turn right from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation None, contradictions []
Tokens                  in 2956, out 672, 10.94 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city road in the United Kingdom with traffic moving on the left; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the roadside parking area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the left boundary
                        being a lane line and the right boundary being an edge line. | roles: The white dashed
                        line fits the role of a lane line, and the white solid line fits the role of an edge
                        line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows crossing for lane changes.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the roadside area.
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed white line, which
                        allows lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which prohibits crossing.
Step 6  go_straight     allowed (contested, correct): No marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change into the left lane. Do not cross the solid white
                        line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 597, 9.51 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a city street in the United Kingdom with shops on both sides; the road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from another lane of my direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway, with a sidewalk and shops beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk area.
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed white line, which
                        allows lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line and a
                        curb, which prohibits leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the left lane. Do not
                        cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 624, 10.76 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with traffic moving on the left; the road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from a bus lane to the left.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        special lane line on the left and a center line on the right. | roles: The white
                        dashed patterns fit the roles of a special lane boundary and a center line in this
                        context. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed line allows changing into the adjacent lane, but the bus lane
                        is reserved for buses.
Step 5  Rule            right_boundary: A dashed center line allows crossing into the opposite lane for
                        overtaking or turning if safe, but not for lane-keeping.
Step 5  Rule            no_turn:left: Not applicable as no such marking exists.
Step 6  change_left     prohibited (contested, correct): The left boundary is a dashed line, but it leads into
                        a reserved bus lane, making the change prohibited for an ordinary car.
Step 6  change_right    allowed (correct): The right boundary is a dashed center line, which allows crossing
                        into the opposite lane for overtaking or turning.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane to go straight. Do not enter the bus lane to your left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 665, 11.57 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with shops on both sides; the road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a red-paved area on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a parking/stopping area on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the presence of edge lines on
                        both sides. | roles: The solid white lines on both sides fit the role of edge lines
                        for a single-lane road. | markings: There are no markings in the lane to contradict
                        the boundaries. | unseen: No attributes were reported without being visible. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the area to the right.
Step 6  change_left     prohibited (contested, correct): The left_boundary is a solid white edge line which
                        prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): The right_boundary is a solid white edge line which
                        prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to either side are prohibited by
                        the solid white edge lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 589, 10.2 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A white circle containing the number 20 is painted across the
                        lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: The speed limit marking is consistent with the road type and boundaries. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the sidewalk or
                        shoulder.
Step 5  Rule            text:speed_limit: The speed limit marking indicates the maximum speed allowed but does
                        not govern lane movements.
Step 6  change_left     allowed (contested, correct): The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white line and a
                        curb, which prohibits leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight, and the lane does
                        not end.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may continue straight or change
                        to the left lane, but do not cross the solid line on the right. Observe the 20 mph
                        speed limit.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 703, 11.32 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a city street in the United Kingdom with buildings on both sides; the road
                        continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            A white solid line separates the roadway from the sidewalk/parking area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 (leftmost) agree with the left
                        boundary being an edge line and the right boundary being a lane line. | roles: The
                        white solid edge line and white dashed lane line are consistent with their roles. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk area.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes into the adjacent lane.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid edge line, which
                        prohibits leaving the roadway.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a dashed lane line, which
                        allows changing lanes.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the left lane; you may continue straight or change to the right lane if
                        needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2956, out 610, 10.61 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a city street in the United Kingdom with traffic keeping to the left; the road
                        continues straight ahead with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            I see a red double-decker bus on my left, but no painted line or curb is visible
                        between my car and the bus.
                        none none, curb no, unknown, evidence full
Step 2  Right           There is a solid yellow line on the right, separating the lane from a parking area
                        with a curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as 1 are consistent with the right
                        boundary being an edge line; the left boundary is obscured by a bus, but no lane line
                        is visible. | roles: The solid yellow line on the right is consistent with a parking
                        restriction edge line in the UK. | markings: There are no markings in my lane to
                        contradict. | unseen: I have not reported any attributes I did not see. | result:
                        consistent
Step 5  Rule            left_boundary: No painted line is visible; lane change is governed by general traffic
                        safety and the presence of other vehicles.
Step 5  Rule            right_boundary: A solid yellow edge line prohibits parking and typically prohibits
                        crossing into the parking area.
Step 5  Rule            no_turn:left: Not applicable as no such marking exists.
Step 6  change_left     allowed (correct): no marking governs this action
Step 6  change_right    prohibited (contested, correct): the solid yellow edge line and curb prohibit crossing
                        into the parking area
Step 6  go_straight     allowed (contested, correct): no marking prohibits going straight
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line on the right into
                        the parking area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['change_left decided with
                        nothing marked on that side']
Tokens                  in 2956, out 640, 12.11 s
```
