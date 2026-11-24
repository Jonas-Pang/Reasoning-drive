# Reasoning of lane run 20261118_013050_laneA_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with other
                        vehicles in front. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow dashed line separating my lane from the lane to the left. Photo
                        2 shows the same yellow dashed line next to my car, with clear gaps between the
                        dashes.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the rightmost lane. Photo 2
                        shows the same white solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: the yellow
                        dashed line on the left and white solid line on the right are consistent with lane
                        boundaries in this context. | markings: there are no markings in my lane to conflict
                        with boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A yellow dashed line allows lane changes across it.
Step 5  Rule            right_boundary: A white solid line prohibits lane changes across it.
Step 6  change_left     allowed (correct): allowed by the yellow dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the white solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but you are prohibited from changing lanes to the
                        right. You can continue straight in your current lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 636, 9.59 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road in China with traffic moving forward; the road continues straight
                        ahead under an overpass. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a shoulder and a metal
                        guardrail. Photo 2 shows the solid white line next to my car and the guardrail further
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line and the white solid line
                        fits the role of an edge line | markings: no markings in my lane to check | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or
                        guardrail area.
Step 6  change_left     allowed (correct): allowed by the broken white lane line
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and the presence of a
                        guardrail
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and it
                        is the natural path of the lane
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the shoulder.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 686, 10.45 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, with a clear road ahead. (lanes
                        2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car, extending forward. Photo 2
                        shows the same white dashed line next to my car, with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line to the right of my car, with a metal guardrail
                        running parallel to it. Photo 2 shows the yellow solid line and the guardrail next to
                        my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a lane line on the left indicates another lane of my
                        direction, and an edge line on the right indicates the end of the roadway. | roles:
                        the white dashed line fits the role of a lane line, and the yellow solid line fits the
                        role of an edge line. | markings: there are no markings in my lane to check. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A yellow solid edge line and a guardrail prohibit leaving the roadway
                        to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (correct): prohibited by the yellow solid edge line and guardrail
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the right boundary
                        into the emergency lane or over the guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 3797, out 667, 30.81 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead on a bridge
                        or elevated roadway. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my car. Photo 2 shows this line is a single
                        solid yellow line next to my car and continues as a solid yellow line further ahead.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my car, with a physical barrier beyond it.
                        Photo 2 shows a single solid white line next to my car and continuing ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a yellow line on the left and a white edge line on the right
                        indicate the rightmost lane of a two-lane road. | roles: the yellow solid line on the
                        left acts as a lane separator (though yellow usually indicates no passing/center, in
                        some urban contexts it separates lanes), and the white solid line on the right is a
                        standard edge line. | markings: no markings are present in the lane. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing to change lanes.
Step 5  Rule            right_boundary: A solid white edge line and physical barrier prohibit leaving the
                        roadway to the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow left boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white right boundary and
                        physical barrier
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight; lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 677, 10.38 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with a
                        concrete barrier on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow dashed line separating my lane from the lane to the left. Photo
                        2 shows the same yellow dashed line next to my car, with several long dashes and gaps.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to a concrete barrier. Photo 2 shows the white
                        solid line and the concrete barrier immediately to the right of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show white Chinese characters '专用交' (part of
                        '公交专用' meaning Bus Only) painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a lane line on the left and an edge line on the right indicate
                        the rightmost lane. | roles: the yellow dashed line as a lane line and white solid
                        line as an edge line are consistent with the road layout. | markings: the 'Bus Only'
                        text indicates this is a reserved lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A yellow dashed line allows lane changes between lanes of the same
                        direction.
Step 5  Rule            right_boundary: A white solid edge line and concrete barrier prohibit leaving the
                        roadway to the right.
Step 5  Rule            text:bus: This lane is reserved for buses; ordinary cars are prohibited from driving
                        in it.
Step 6  change_left     allowed (contested, correct): allowed by the yellow dashed left boundary.
Step 6  change_right    prohibited (contested, label allowed): prohibited by the white solid right boundary
                        and concrete barrier.
Step 6  go_straight     prohibited (contested, label allowed): prohibited because the lane is marked as a bus-
                        only lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are currently in a bus-only lane. You should change left into the general traffic
                        lane immediately.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions ['go_straight decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 3797, out 738, 32.57 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an underpass. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a solid
                        white line immediately to the left of the lane, adjacent to a raised concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car, with a raised curb further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both left and right | roles: the solid white lines on both
                        sides fit the role of edge lines for a single-lane road | markings: no markings
                        present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white line which prohibits crossing
Step 6  change_right    prohibited (correct): the right_boundary is a solid white line which prohibits
                        crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight through the underpass; lane changes are
                        prohibited on both sides.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 599, 9.19 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a bus stop on the left and parked scooters on the
                        right; the road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car and continuing ahead. Photo 2
                        confirms a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and continuing ahead. Photo 2
                        confirms a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides | roles: the white solid lines on both sides fit the
                        role of edge lines for a single-lane road | markings: no markings in the lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area to the left.
Step 5  Rule            right_boundary: A solid white edge line and curb prohibit crossing into the area to
                        the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white edge line which prohibits
                        crossing
Step 6  change_right    prohibited (correct): the right_boundary is a solid white edge line and curb which
                        prohibits crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight; lane changes are prohibited on both
                        sides.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 600, 9.36 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 confirms a white
                        dashed line with several long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 confirms a white
                        dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed lines fit the role of lane lines separating lanes of the same direction |
                        markings: there are no markings in my lane to contradict | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (WRONG, label prohibited): the left_boundary is a white dashed line which
                        allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and it is allowed by
                        default
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 3797, out 628, 9.48 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with other
                        vehicles in front. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the roadway from a curb and hedge. Photo 2
                        confirms a solid white line next to the car, with a raised curb and hedge immediately
                        to its left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a solid edge line on the left and a dashed lane line on the right
                        indicate my lane is the leftmost of two lanes. | roles: the white solid edge line and
                        white dashed lane line fit their respective roles. | markings: there are no markings
                        in my lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or curb
                        area.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white edge line with a curb, which
                        prohibits leaving the roadway.
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line, which allows
                        changing lanes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane;
                        do not cross the left boundary into the curb area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 651, 7.46 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection with
                        traffic lights. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 confirms a white
                        dashed line with several long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 confirms a white
                        dashed line with several long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and my position in
                        lane 2 agree with having lane lines on both the left and right sides | roles: the
                        white dashed lines on both sides are consistent with lane lines separating lanes of
                        the same direction | markings: there are no markings in my lane to contradict the
                        boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed: the left boundary is a white dashed lane line, which allows lane changes
Step 6  change_right    allowed: the right boundary is a white dashed lane line, which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed by
                        default
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or change lanes to either the left or
                        right. Follow the traffic signals at the upcoming intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 628, 28.86 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a continuous yellow line next to a white fence. Photo 2 confirms a solid
                        yellow line immediately to the left of the lane, running alongside a white metal
                        fence.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the right. Photo 2 shows a dashed
                        white line next to the black car, with several long dashes and gaps visible.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and index 1 agree
                        with the left boundary being an edge line (yellow solid) and the right boundary being
                        a lane line (white dashed), implying there is at least one more lane to the right. |
                        roles: the yellow solid line on the left fits the role of an edge line/center line
                        separating traffic or the roadway edge; the white dashed line on the right fits the
                        role of a lane line. | markings: no markings are present in the lane to contradict
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing into the area to the left.
Step 5  Rule            right_boundary: A dashed white line allows lane changes to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow left boundary
Step 6  change_right    allowed (correct): allowed by the dashed white right boundary
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the solid yellow
                        line to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['symbol:other']), actions True, unsafe [], citation None, contradictions ['rightmost
                        lane, but a lane line on the right']
Tokens                  in 3797, out 679, 10.57 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road or highway bridge, heading straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, bordered by a concrete barrier. Photo 2
                        confirms a solid white line next to the car and a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, bordered by a concrete barrier. Photo 2
                        confirms a solid white line next to the car and a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; both sides are edge lines, meaning this is a single-lane section of
                        road. | roles: the white solid lines and concrete barriers fit the role of edge lines.
                        | markings: no markings are present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line and barrier prohibit leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: A solid white edge line and barrier prohibit leaving the roadway to
                        the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and concrete barrier on
                        the left.
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and concrete barrier on
                        the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and it
                        is the only available path.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight; lane changes are prohibited on both
                        sides due to the road boundaries.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 658, 10.09 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway under an overpass. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line on the left, next to a guardrail. Photo 2 confirms a
                        solid white line immediately to the left of the car, continuing forward.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right. Photo 2 shows a white dashed line with
                        long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a solid white edge line on the left and a dashed lane line on the
                        right indicate the leftmost lane of a multi-lane road. | roles: the white solid line
                        fits the role of an edge line, and the white dashed line fits the role of a lane line.
                        | markings: no markings present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or off the
                        roadway.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white edge line which prohibits
                        leaving the roadway
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line which allows
                        changing lanes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 623, 9.66 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, with a clear road ahead. (lanes
                        4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 confirms a white
                        dashed line with several long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 shows a white dashed
                        line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and my position in
                        lane 2 agree with having lane lines on both the left and right | roles: white dashed
                        lines are consistent with lane_line roles | markings: no markings present in my lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (WRONG, label prohibited): the left_boundary is a white dashed line which
                        allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 3797, out 592, 9.1 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car and further ahead. Photo 2 confirms a
                        white dashed line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car and further ahead. Photo 2 confirms a
                        white dashed line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows it as well.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries. | roles: the white
                        dashed lines on both sides fit the role of lane lines. | markings: the straight-ahead
                        arrow is consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): the left boundary is a white dashed lane line,
                        which allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): the right boundary is a white dashed lane line,
                        which allows lane changes.
Step 6  go_straight     allowed (correct): the straight-ahead arrow in my lane allows this movement.
Step 6  turn_left       prohibited (correct): the straight-ahead arrow in my lane prohibits turning left.
Step 6  turn_right      prohibited (correct): the straight-ahead arrow in my lane prohibits turning right.
Step 6  u_turn          prohibited (correct): the straight-ahead arrow in my lane prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left or
                        right if needed, but you cannot turn at the upcoming intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation None, contradictions []
Tokens                  in 3797, out 712, 10.06 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a wide intersection with a
                        crosswalk ahead. (lanes 4, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right. Photo 2 shows a broken white line next
                        to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a white zebra-style crosswalk across
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a solid white line on the left indicates the edge of the roadway,
                        making this the leftmost lane. | roles: the white solid line on the left fits the role
                        of an edge line, and the white dashed line on the right fits the role of a lane line.
                        | markings: the crosswalk is a standard marking across all lanes at an intersection. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or non-
                        roadway area.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 5  Rule            line:crosswalk: A crosswalk indicates a pedestrian crossing area where vehicles must
                        yield to pedestrians.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line (left_boundary).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line
                        (right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as there are no arrows in the lane to prohibit
                        it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or marking governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or marking governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or marking governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane,
                        but do not cross the solid line to the left. Be prepared to stop for pedestrians at
                        the crosswalk.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3797, out 755, 10.83 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight toward a
                        distant intersection or overpass. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: the
                        white dashed patterns for both boundaries fit the role of lane lines | markings: there
                        are no markings in my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed lane line, which allows lane
                        changes
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the boundaries do
                        not prohibit it
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 635, 9.53 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 confirms a white
                        dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 confirms a white
                        dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: the white
                        dashed patterns fit the role of lane lines separating traffic in the same direction. |
                        markings: there are no markings in my lane to contradict. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 628, 9.6 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection or a
                        junction with overhead signage. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns fit the role of lane lines | markings: there are no markings in my
                        lane to conflict with | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (contested, label prohibited): the left_boundary is a white dashed line, which
                        allows lane changes
Step 6  change_right    allowed (contested, correct): the right_boundary is a white dashed line, which allows
                        lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 618, 8.18 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, which then becomes a solid white
                        line further ahead. Photo 2 shows the white dashed line next to my car with several
                        long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right. | roles: the white
                        dashed lines fit the role of lane lines. | markings: the straight-ahead arrow is
                        consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (correct): the left boundary is a white dashed line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): the right boundary is a white dashed line, which allows lane
                        changes.
Step 6  go_straight     allowed (correct): the arrow in my lane points straight, which allows this movement.
Step 6  turn_left       prohibited (correct): the arrow in my lane points straight, which prohibits turning
                        left.
Step 6  turn_right      prohibited (correct): the arrow in my lane points straight, which prohibits turning
                        right.
Step 6  u_turn          prohibited (correct): the arrow in my lane points straight, which prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a straight-through lane. You may continue straight or change lanes if
                        needed; turning left or right from this lane is prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 722, 10.35 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection with
                        traffic signals overhead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns fit the role of lane lines | markings: there are no markings in my
                        lane to contradict | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line, which allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 615, 9.3 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a wide intersection or a
                        junction where the road curves slightly to the left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line that is solid near the car and continues as a solid line
                        ahead. Photo 2 confirms a single solid yellow line immediately to the left of the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of the car. Photo 2 shows a white
                        dashed line with clear gaps and dashes next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a center line on the left and a lane line on the right indicate
                        the car is in the second lane from the left (of the three lanes in its direction). |
                        roles: the yellow solid line fits the role of a center line, and the white dashed line
                        fits the role of a lane line. | markings: no markings are present in the lane to
                        contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): the left boundary is a solid yellow center line which prohibits
                        crossing it
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change to the right lane, but
                        you must not cross the solid yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 662, 10.07 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway in China, traveling straight ahead on a clear road.
                        (lanes 5, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 show large white characters painted across the
                        lane, which are part of a warning or guidance marking.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 5 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries. | roles: the white
                        dashed lines on both sides are consistent with lane_line roles. | markings: the text
                        markings are consistent with a highway environment. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            text:other: General road markings do not restrict the seven basic driving actions.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and the
                        lane does not end
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  You are in the second lane from the left. You may continue straight or change lanes to
                        the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 723, 10.62 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, heading straight toward a distant
                        overhead gantry. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns fit the role of lane lines | markings: there are no markings in my
                        lane to conflict with boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed lane line, which allows lane
                        changes
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and it is allowed by
                        default
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 630, 9.29 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line between my lane and the lane to the left. Photo 2
                        shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line between my lane and the lane to the right. Photo 2
                        shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane. Photo 1
                        confirms this arrow is in the center lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries. | roles: the white
                        dashed patterns for both boundaries fit the role of lane lines. | markings: the
                        straight-ahead arrow in the center lane is consistent with the boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight but prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited (correct): prohibited by the arrow:straight marking
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left or
                        right if needed, but you cannot turn at the next intersection from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3797, out 712, 10.1 s
```
