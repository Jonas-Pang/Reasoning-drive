# Reasoning of lane run 20261118_001322_laneA_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway in China with traffic moving forward; the road continues straight
                        ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road, followed by a metal
                        guardrail. Photo 2 shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane position
                        agree with the boundaries: a lane line on the left and an edge line on the right
                        indicate the rightmost lane of two. | roles: the white dashed line is a standard lane
                        line and the white solid line is a standard edge line. | markings: no markings in my
                        lane to conflict with boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows crossing for lane changes.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or off
                        the roadway.
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed lane line which permits lane
                        changes.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid edge line and there is
                        a guardrail.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight in this
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
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 819, 7.02 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road in China with traffic keeping right, heading towards a bridge or
                        overpass. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road, followed by a metal
                        guardrail. Photo 2 shows a solid white line next to my car and a metal guardrail
                        further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows changing lanes.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing it to leave the roadway.
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed lane line.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid edge line and there is
                        a guardrail.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but you cannot leave the road to the right due to the solid edge line and guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 767, 12.27 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The road is a multi-lane highway in China with traffic keeping to the right. My car is
                        in the rightmost travel lane, heading straight. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail. Photo 2
                        shows a solid white line next to my car and a metal guardrail further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a lane line on the left and an edge line on the right
                        indicate I am in the rightmost lane of a two-lane road. | roles: the white dashed line
                        fits the role of a lane line, and the white solid line fits the role of an edge line.
                        | markings: no markings in my lane, which is consistent with a highway travel lane. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line and guardrail prohibit leaving the roadway to
                        the right.
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed lane line.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid edge line and there is
                        a guardrail.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight in this
                        travel lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost travel lane. You may continue straight or change lanes to the
                        left, but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 853, 3.71 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with traffic keeping right; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line separating my lane from the lane to the left. Photo
                        2 shows a yellow broken line with long dashes and gaps next to my car.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a raised barrier. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a lane line on the left and an edge line on the right
                        indicate I am in the rightmost lane. | roles: the yellow dashed line is a lane line
                        and the white solid line is an edge line, which fits the roles. | markings: no
                        markings in my lane, consistent with boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A yellow dashed lane line allows changing lanes.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or over
                        the barrier.
Step 6  change_left     allowed (contested, label prohibited): allowed by the yellow dashed lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and the
                        physical barrier
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move to the right due to the solid edge line and barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 788, 2.78 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test A | gemma-4-31b-it
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The road is a multi-lane urban road with a concrete barrier on the right. My car is in
                        a lane that contains Chinese characters. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow broken line separating my lane from the lane to the left. Photo
                        2 shows the same yellow broken line next to my car, consisting of long dashes and
                        gaps.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to a concrete barrier. Photo 2 shows a white
                        solid line immediately to the right of my car, with a raised concrete barrier beside
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the Chinese characters '公交' (Gōngjiāo) painted in white
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a yellow dashed line on the left indicates another lane
                        of my direction, and a white solid line with a curb on the right indicates the edge of
                        the roadway. | roles: the yellow dashed line is a lane line and the white solid line
                        is an edge line, which fits their positions. | markings: the '公交' (bus) text indicates
                        this is a bus lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken line allows crossing for lane changes.
Step 5  Rule            right_boundary: A solid edge line and curb prohibit leaving the roadway to the right.
Step 5  Rule            text:bus: This lane is reserved for buses; ordinary cars are prohibited from using it.
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a dashed line.
Step 6  change_right    prohibited (contested, label allowed): prohibited: the right boundary is a solid line
                        and there is a concrete barrier.
Step 6  go_straight     prohibited (contested, label allowed): prohibited: the lane is marked as a bus lane
                        (text:bus), and my car is an ordinary car.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a reserved bus lane. You should change to the left lane
                        immediately as ordinary cars are prohibited from using this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left', 'go_straight decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 3798, out 944, 4.1 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test A | gemma-4-31b-it
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading towards an underpass. There is a concrete
                        barrier on the left and a wall on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a solid
                        white line and a raised concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a curb. Photo 2 shows a solid white line and
                        a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid edge line and barrier prohibit crossing to the left.
Step 5  Rule            right_boundary: A solid edge line and curb prohibit crossing to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid edge line and concrete barrier
Step 6  change_right    prohibited (correct): prohibited by the solid edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight through the underpass; lane changes are
                        prohibited on both sides.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 706, 11.59 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test A | gemma-4-31b-it
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a bus stop on the left and parked scooters on the
                        right. The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a bus stop area. Photo 2
                        shows the same solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a curb with parked scooters. Photo 2 shows
                        the solid white line and the raised curb next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundary roles; it is a single lane bounded by edge lines on both sides | roles:
                        the white solid lines correctly serve as edge lines for the roadway | markings: no
                        markings in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area beyond it.
Step 5  Rule            right_boundary: A solid white edge line and curb prohibit crossing into the area
                        beyond it.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts going straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 760, 7.21 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test A | gemma-4-31b-it
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with traffic moving forward; there is no immediate
                        intersection or ramp visible ahead. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the rightmost lane. Photo 2
                        shows a white solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; there are two lanes to the left and one to the right. | roles:
                        the white dashed line on the left and white solid line on the right are consistent
                        with lane-dividing roles. | markings: no markings are present in my lane, which is
                        consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid lane line prohibits changing lanes to the right.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid lane line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left, but you are prohibited from
                        changing lanes to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 3798, out 769, 2.83 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test A | gemma-4-31b-it
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with traffic keeping to the right. The road continues
                        straight ahead with no immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car and a raised curb further left. Photo
                        2 shows a solid white line next to my car and a raised curb to its left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car and continuing ahead. Photo 2 shows a
                        broken white line with one dash and one gap visible next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a white edge line and curb on the left indicate my lane
                        is the leftmost of my direction | roles: the white solid edge line and white dashed
                        lane line fit their respective roles | markings: no markings in my lane to check |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line and curb prohibit leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and curb
Step 6  change_right    allowed (correct): allowed by the broken white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right;
                        changing to the left is prohibited by the curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 809, 4.0 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road in China with traffic keeping to the right. The road continues
                        straight ahead toward a signalized intersection. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     allowed: The left boundary is a broken white lane line, which allows lane changes.
Step 6  change_right    allowed: The right boundary is a broken white lane line, which allows lane changes.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right. Follow the traffic signals at the intersection ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 752, 12.44 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading straight toward a distant
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a white fence. Photo 2 shows a solid yellow
                        line immediately to the left of the lane, bordered by a white fence.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        yellow edge line on the left indicates the leftmost lane of the direction | roles: the
                        yellow solid edge line and white dashed lane line fit their roles | markings: no
                        markings in lane, consistent with boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits crossing into the area to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line and physical fence
Step 6  change_right    allowed (correct): allowed by the white dashed lane line
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it and the lane
                        continues
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you cannot move to the left due to the solid line and fence.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['symbol:other']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 772, 3.89 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test A | gemma-4-31b-it
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road or highway, traveling straight ahead on a bridge or
                        elevated section. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, bordering a concrete barrier. Photo 2
                        shows the same solid white line immediately next to the car, with a concrete barrier
                        to its left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, bordering a concrete barrier. Photo 2
                        shows the same solid white line immediately next to the car, with a concrete barrier
                        to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides | roles: the white solid lines on both sides
                        correctly serve as edge lines for a single-lane road section | markings: no markings
                        in lane, consistent with the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and concrete barrier
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and concrete barrier
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts continuing straight in
                        the lane
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present
Step 7  Reflect         consistent
Advice                  Stay in your lane and continue straight. Lane changes are prohibited due to the solid
                        edge lines and barriers.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 798, 4.98 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test A | gemma-4-31b-it
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway passing under a bridge. (lanes 3, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to the car and a guardrail further left. Photo 2
                        shows a solid white line next to the car and a metal guardrail to its left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car. Photo 2 shows a broken white line
                        with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left into the
                        shoulder or off the roadway.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): The left boundary is a solid edge line, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (correct): The right boundary is a broken lane line, which allows changing to
                        the right lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane continues
                        forward.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right; do not cross the solid line on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 723, 2.9 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test A | gemma-4-31b-it
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, moving straight ahead. (lanes 3,
                        mine 1, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the shoulder/barrier. Photo 2 shows
                        a white dashed line next to my car, and further ahead it remains a white dashed line.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to my car, and further ahead it remains a white
                        dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed white edge line allows crossing to the shoulder or exiting the
                        roadway.
Step 5  Rule            right_boundary: A dashed white lane line allows changing into the adjacent lane.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the dashed white edge line
Step 6  change_right    allowed (correct): allowed by the dashed white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost through lane. You may continue straight or change lanes to the
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 3798, out 718, 3.65 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with an intersection ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundary roles as there are lane lines on both sides. | roles: the white
                        dashed lines correctly fit the role of lane lines. | markings: the straight-ahead
                        arrow is consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows crossing for a lane change.
Step 5  Rule            right_boundary: A white dashed lane line allows crossing for a lane change.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed left boundary.
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the white dashed right boundary.
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow in my lane.
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow in my lane.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow in my lane.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow in my lane.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn, change lanes now as the current
                        lane is for straight-through traffic only.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation None, contradictions []
Tokens                  in 3798, out 854, 15.17 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a crosswalk and an
                        intersection. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left edge of the road. Photo 2 shows the same
                        solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a white zebra-striped crosswalk across
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a white edge line on the left and a lane line on the right
                        indicate the leftmost lane of the direction. | roles: the white solid edge line and
                        white dashed lane line fit their roles. | markings: the crosswalk is consistent with
                        an intersection approach. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits leaving the roadway to the left.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 5  Rule            line:crosswalk: A crosswalk does not govern lane changes or turns, but requires
                        yielding to pedestrians.
Step 6  change_left     prohibited (correct): the left_boundary is a solid edge line which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (WRONG, label prohibited): the right_boundary is a dashed lane line which
                        allows changing lanes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: no arrow or prohibited-movement marking governs this action, so it is
                        not_applicable.
Step 6  turn_right      not_applicable: no arrow or prohibited-movement marking governs this action, so it is
                        not_applicable.
Step 6  u_turn          not_applicable: no arrow or prohibited-movement marking governs this action, so it is
                        not_applicable.
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane governs this action.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight or change to the right lane. Yield
                        to pedestrians at the crosswalk.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3798, out 914, 12.3 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with traffic keeping to the right; the road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane position
                        agree with the boundary roles as there are lane lines on both sides | roles: the white
                        dashed patterns fit the role of lane lines | markings: no markings in my lane,
                        consistent with boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 754, 3.41 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with traffic keeping right; the road continues
                        straight ahead toward a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a long white dash followed by a gap, then another dash.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the rightmost lane. Photo 2
                        shows a continuous solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; there is a lane to the left and a lane to the right. | roles: the
                        white dashed line on the left and white solid line on the right are consistent with
                        lane-separating roles in this context. | markings: no markings were found in my lane,
                        which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows crossing for lane changes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing for lane changes.
Step 6  change_left     allowed (correct): allowed by the broken white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it and the boundaries do
                        not restrict forward movement.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the left. Changing lanes to the right is
                        prohibited by the solid white line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 802, 10.22 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with traffic keeping right; the road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns are consistent with lane lines | markings: no markings in my lane,
                        consistent with boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (contested, label prohibited): allowed by the white dashed left boundary
Step 6  change_right    allowed (contested, correct): allowed by the white dashed right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts going straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 750, 5.19 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the rightmost lane. Photo 2
                        shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the two lane lines on either side | roles: the white dashed lines correctly serve
                        as lane lines | markings: the straight arrow is consistent with the lane boundaries |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing into the adjacent lane.
Step 5  Rule            right_boundary: A white dashed lane line allows changing into the adjacent lane.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow in my lane
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn, change to the appropriate lane
                        using the dashed lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 844, 16.07 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a signalized intersection.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white line separating my lane from a shoulder/median area, with a
                        metal fence/barrier next to it. Photo 2 shows the same white line and the metal
                        barrier immediately to the left of my car.
                        white dashed, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; the
                        left boundary is an edge line with a barrier, making my lane the leftmost lane of the
                        roadway. | roles: the white dashed lines fit the roles of edge line and lane line
                        respectively. | markings: no markings in my lane, which is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed edge line with a barrier prohibits leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: A dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the barrier and edge line
Step 6  change_right    allowed (correct): allowed by the dashed lane line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight or change to the right lane;
                        changing to the left is prohibited by the barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 780, 2.95 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road in China, approaching a wide open area or
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a yellow broken line with long dashes and gaps next to the car.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line. Photo 2 shows a white broken line with long dashes
                        and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; there are lanes to both the left and right | roles: the yellow line on
                        the left is a lane line (common in some Chinese city road configurations for specific
                        lane types) and the white line on the right is a standard lane line | markings: no
                        markings in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken yellow line allows lane changes.
Step 5  Rule            right_boundary: A broken white line allows lane changes.
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken yellow line, which
                        allows lane changes.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 3798, out 754, 7.16 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway in China with overhead gantry signs. My car is in one of the
                        through lanes. (lanes 6, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to my car and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car and a broken white line further
                        ahead. Photo 2 shows a broken white line with several long dashes and gaps next to my
                        car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or off the
                        roadway.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes into the adjacent lane.
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid edge line and there is
                        a curb, which prohibits leaving the roadway.
Step 6  change_right    allowed (correct): The right boundary is a broken lane line, which allows changing to
                        the right lane.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Do not cross the solid line on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['text:other']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 724, 3.68 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, heading straight on a clear road.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car and a continuous white line further
                        ahead. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car and continues as a broken white line
                        further ahead. Photo 2 shows a broken white line with visible dashes and gaps next to
                        the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego position agree
                        with the boundaries; a white edge line on the left and a lane line on the right
                        indicate the leftmost lane of a multi-lane road. | roles: the white solid edge line
                        and white dashed lane line fit their respective roles. | markings: no markings are
                        present in the lane, which is consistent with a highway environment. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or off the
                        roadway.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes into the adjacent lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line.
Step 6  change_right    allowed (correct): allowed by the broken white lane line.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right;
                        changing to the left is prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 810, 4.02 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test A | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with traffic keeping to the right; the road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with long dashes and clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with long dashes and clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right sides. | roles: the white
                        dashed patterns for both boundaries are consistent with lane lines separating traffic
                        in the same direction. | markings: the straight-ahead arrow in my lane is consistent
                        with the overhead sign showing three straight arrows for the three lanes. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows crossing for lane changes.
Step 5  Rule            right_boundary: A white dashed lane line allows crossing for lane changes.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left or right.
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary.
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary.
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow in my lane.
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow in my lane.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow in my lane.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow in my lane.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. Lane changes to the left or right are permitted.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3798, out 869, 7.57 s
```
