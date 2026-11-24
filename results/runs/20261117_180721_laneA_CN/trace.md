# Reasoning of lane run 20261117_180721_laneA_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead on a clear
                        day. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a metal fence. Photo 2 confirms a solid
                        yellow line and a raised curb/barrier.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line. Photo 2 shows a white dashed line with clear gaps
                        next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a yellow edge line on the left and a white lane line on the right
                        indicate the leftmost lane of a two-lane road. | roles: the yellow solid edge line and
                        white dashed lane line fit their respective roles. | markings: there are no markings
                        in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits crossing into the shoulder or
                        barrier area.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow edge line and
                        physical barrier.
Step 6  change_right    allowed (contested, label prohibited): allowed by the white dashed lane line.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 624, 11.21 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with no
                        immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right edge of the road. Photo 2 shows a solid
                        yellow line next to my car, continuing as a solid line further ahead.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right | roles: the white
                        dashed line fits the role of a lane line, and the yellow solid line fits the role of
                        an edge line | markings: no markings in my lane to check | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid yellow edge line prohibits crossing into the shoulder or off
                        the roadway to the right.
Step 6  change_left     allowed (correct): the left boundary is a broken white line, which allows lane changes
Step 6  change_right    prohibited (contested, correct): the right boundary is a solid yellow line, which
                        prohibits crossing it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 643, 11.73 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. The road
                        continues forward with no immediate intersection or ramp visible. (lanes 3, mine 3,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to my car, which marks the edge of the roadway.
                        Photo 2 confirms a single white solid line and a raised curb immediately to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        the 3rd lane agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        with a curb fits the role of an edge line | markings: no markings were observed in my
                        lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and curb prohibit leaving the roadway to the
                        right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 666, 11.8 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, with an elevated highway
                        structure on the right and a fence on the left. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, continuing straight ahead. Photo 2
                        confirms a solid white line next to the car and a raised concrete curb/barrier to its
                        left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, with several dashes and gaps
                        visible. Photo 2 shows the same broken white line with a clear dash and gap next to
                        the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a solid white edge line on the left indicates the leftmost lane,
                        and a broken white line on the right indicates another lane of the same direction. |
                        roles: the white solid edge line and white dashed lane line fit their respective
                        roles. | markings: no markings are present in the lane to contradict boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line and curb prohibit leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white line and curb, which
                        prohibits leaving the roadway
Step 6  change_right    allowed (correct): the right_boundary is a dashed white line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the left boundary.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 656, 11.02 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, with a raised barrier and
                        fence on the left and an elevated highway structure on the right. The road continues
                        straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a raised curb and fence. Photo 2 confirms a
                        solid white line and a raised curb immediately to the left of the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries: a solid edge line on the left and a dashed lane line on the right
                        indicate my lane is the leftmost of two lanes. | roles: the white solid edge line and
                        white dashed lane line fit their respective roles. | markings: there are no markings
                        in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line and curb prohibit leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white line and curb, which
                        prohibits leaving the roadway.
Step 6  change_right    allowed (correct): the right_boundary is a dashed white line, which allows changing
                        lanes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 649, 12.19 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with
                        buildings and shops on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the roadway from a landscaped median.
                        Photo 2 shows the same solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right lane. Photo 2
                        shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a solid edge line on the left and a dashed lane line on the right
                        indicate my lane is the leftmost of two lanes. | roles: the white solid line on the
                        left fits the role of an edge line, and the white dashed line on the right fits the
                        role of a lane line. | markings: there are no markings in my lane to contradict. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the median.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
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
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane;
                        do not cross the left boundary into the median.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 639, 11.04 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead on a clear
                        stretch of road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line next to the car, which continues ahead. Photo 2
                        confirms a white solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line next to the car, which continues ahead. Photo 2
                        confirms a yellow solid line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a lane line on the left and a center line on the right indicate
                        the car is in the leftmost lane of its direction. | roles: the white solid lane line
                        and yellow solid center line fit their respective roles. | markings: there are no
                        markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: A solid yellow center line prohibits crossing into the opposite
                        direction of traffic.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line
                        (left_boundary)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow center line
                        (right_boundary)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane restricting
                        forward movement
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['leftmost lane,
                        but a lane line on the left']
Tokens                  in 3717, out 653, 11.73 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, passing under an elevated
                        highway structure. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line to the left of my car. Photo 2 shows a white broken
                        line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of my car. Photo 2 shows a white broken
                        line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns fit the role of lane lines | markings: no markings present in my lane
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed lane line which allows lane
                        changes
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane; you may continue straight or change lanes to the left or
                        right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 597, 11.7 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road or bridge, heading towards a city skyline with
                        high-rise buildings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my lane. Photo 2 shows this line is a solid
                        yellow line next to my car, and it remains solid further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this line is a
                        dashed white line next to my car, and it continues as a dashed white line further
                        ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a center line on the left and a lane line on the right place my
                        car in the second lane from the left of a three-lane road (where the leftmost lane is
                        a special lane or the road starts with a center line). | roles: the yellow solid line
                        fits the role of a center line; the white dashed line fits the role of a lane line. |
                        markings: no markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing into the opposite
                        direction or the adjacent special lane.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): the left boundary is a solid yellow line which
                        prohibits crossing it
Step 6  change_right    allowed (correct): the right boundary is a dashed white line which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change to the right lane, but
                        you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 674, 12.44 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a solid yellow line
                        next to the car and continuing ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 confirms a solid yellow line
                        next to the car and continuing ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows large white Chinese characters painted across the lane;
                        Photo 1 shows they are part of a 'BUS' lane marking.
Step 4  Cross-check     close_up: the same in both photos | position: The presence of center lines on both
                        sides indicates the car is in a special lane, likely a bus lane, separated from
                        general traffic. | roles: The yellow solid lines are consistent with the boundaries of
                        a reserved lane or a center-turn lane, but here they bound a single lane. | markings:
                        The 'BUS' text agrees with the yellow boundaries of a reserved lane. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing to change lanes.
Step 5  Rule            right_boundary: A solid yellow line prohibits crossing to change lanes.
Step 5  Rule            text:bus: This lane is reserved for buses; ordinary cars are prohibited from using it.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow left boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right boundary
Step 6  go_straight     allowed (contested, correct): allowed as no arrow prohibits it, though the lane is
                        reserved
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a reserved bus lane. You should not be in this lane and cannot change lanes
                        across the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 696, 11.45 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with other
                        vehicles in front. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left, which is the edge of the roadway. Photo 2
                        shows a white solid line next to the car and a metal fence/barrier further left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the left edge_line and right lane_line | roles: the white solid left boundary
                        fits an edge_line and the white dashed right boundary fits a lane_line | markings: no
                        markings in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left into the non-
                        roadway area.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid edge_line which prohibits crossing
                        it
Step 6  change_right    allowed (correct): the right_boundary is a dashed lane_line which allows changing
                        lanes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 616, 10.06 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an overpass or bridge.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a solid
                        white line immediately to the left of the lane, with a raised concrete barrier further
                        left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line. Photo 2 shows a white dashed line with clear gaps
                        next to the car, continuing further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the left edge_line and right lane_line | roles: the white solid edge line and
                        white dashed lane line fit their roles | markings: no markings in lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or barrier
                        area.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line and concrete
                        barrier
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed white lane line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3717, out 610, 11.09 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead under a
                        pedestrian overpass. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from another lane to the left.
                        Photo 2 shows the same white dashed line next to my car, with several long dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, bordering a fence. Photo 2 shows a
                        white solid line next to my car, continuing straight ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a lane line on the left and an edge line on the right indicate my
                        lane is the leftmost of two lanes in my direction. | roles: the white dashed line fits
                        the role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: there are no markings in my lane to contradict. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the shoulder or area
                        beyond the roadway.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the white solid edge line and the
                        presence of a curb/fence
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the right boundary.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 3717, out 657, 11.81 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, approaching an intersection with a channelized
                        right-turn area ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, which continues ahead. Photo 2
                        confirms a single solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, continuing ahead. Photo 2 confirms a
                        single solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 shows a channelizing area with diagonal white
                        stripes ahead of the lane. Photo 2 shows the start of this area.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge line on the right | roles: the yellow solid
                        line fits the role of a center line and the white solid line fits the role of an edge
                        line | markings: the channelizing area ahead is consistent with the road layout |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A solid white edge line prohibits leaving the roadway to the right.
Step 5  Rule            area:channelizing: Driving over a channelizing area is prohibited.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid yellow center line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): allowed as there are no arrows in the lane to prohibit
                        it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid lines on either side.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 3717, out 694, 12.85 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead under an
                        overpass. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a metal guardrail. Photo 2
                        shows the white solid line and the guardrail immediately to the right of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the 3rd lane agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        fits the role of an edge line | markings: no markings in my lane to check | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and guardrail prohibit leaving the roadway to
                        the right.
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the white dashed lane line
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line and guardrail
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move further right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 655, 11.38 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with other
                        vehicles in front. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line marking the edge of the roadway, followed by a raised
                        curb and a sidewalk. Photo 2 confirms the white solid line and the presence of a
                        raised curb immediately to the right of the line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        the 3rd lane agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        fits the role of an edge line | markings: no markings are present in my lane | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and a curb prohibit leaving the roadway to the
                        right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line and the raised curb
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the curb area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 686, 12.73 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with a
                        traffic signal ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a raised curb. Photo 2 confirms a solid white
                        line and a raised concrete curb immediately to the right of my lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane.
                        Photo 1 shows the same arrow further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        the 3rd lane agree with having a lane line on the left and an edge line on the right.
                        | roles: the white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: the straight-ahead
                        arrow is consistent with the lane's position and boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and curb prohibit leaving the roadway to the
                        right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed lane line on the left.
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line and raised curb on the
                        right.
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow in the lane.
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow in the lane.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow in the lane.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow in the lane.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn, change to a left lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 3717, out 745, 13.68 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car and continuing ahead. Photo 2
                        confirms a white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, which then becomes a solid white
                        line further ahead. Photo 2 shows a white dashed line with long dashes and gaps next
                        to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: the white dashed
                        lines fit the role of lane lines | markings: there are no markings in my lane to
                        conflict with | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (WRONG, label prohibited): the left_boundary is a white dashed line, which
                        allows lane changes
Step 6  change_right    allowed (WRONG, label prohibited): the right_boundary is a white dashed line next to
                        my car, which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may go straight or change lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation None,
                        contradictions []
Tokens                  in 3717, out 610, 10.32 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading towards a distant
                        intersection. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to the car and further ahead. Photo 2 confirms
                        a white dashed line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car and further ahead. Photo 2 confirms
                        a white dashed line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows it as well.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries. | roles: the white
                        dashed lines on both sides fit the role of lane lines. | markings: the straight-ahead
                        arrow is consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (correct): the left boundary is a white dashed lane line which allows lane
                        changes.
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line which allows lane
                        changes.
Step 6  go_straight     allowed (correct): the straight-ahead arrow in the lane allows this movement.
Step 6  turn_left       prohibited (correct): the straight-ahead arrow in the lane prohibits turning left.
Step 6  turn_right      prohibited (correct): the straight-ahead arrow in the lane prohibits turning right.
Step 6  u_turn          prohibited (correct): the straight-ahead arrow in the lane prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left or
                        right if needed, but you cannot turn at the intersection from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 713, 11.22 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line between my lane and the lane to the left. Photo 2
                        shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line between my lane and the lane to the right. Photo 2
                        shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows it as well.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right | roles: white dashed
                        lines are consistent with lane_line roles | markings: the straight-ahead arrow is
                        consistent with the lane boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed left_boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the white dashed right_boundary
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow in my lane
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a straight-through lane. You may continue straight or change lanes if
                        needed, but you cannot turn left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3717, out 708, 12.45 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car that continues ahead. Photo 2
                        confirms a white dashed line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car that continues ahead. Photo 2
                        confirms a white dashed line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both left and right | roles: white dashed lines are
                        consistent with lane_line roles | markings: no markings present in my lane | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (WRONG, label prohibited): the left_boundary is a white dashed line which
                        allows lane changes
Step 6  change_right    allowed (WRONG, label prohibited): the right_boundary is a white dashed line which
                        allows lane changes
Step 6  go_straight     allowed (correct): no marking governs this action
Step 6  turn_left       not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  turn_right      not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  u_turn          not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3717, out 583, 12.56 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead towards an
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues as the edge of the
                        roadway. Photo 2 confirms a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, separating it from another lane.
                        Photo 2 shows a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left_right (full): Photo 2 shows a white arrow pointing both straight and left.
                        Photo 1 confirms this arrow is in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a solid edge line on the left and a dashed lane line on the right
                        indicate the leftmost lane of two. | roles: the white solid edge line and white dashed
                        lane line fit their respective roles. | markings: the straight-and-left arrow is
                        consistent with the lane's position as the leftmost lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 5  Rule            arrow:left_right: The arrow allows the car to either go straight or turn left at the
                        intersection.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line and curb
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line
Step 6  go_straight     allowed (correct): allowed by the straight-and-left arrow
Step 6  turn_left       allowed (correct): allowed by the straight-and-left arrow
Step 6  turn_right      prohibited (correct): prohibited by the straight-and-left arrow
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited by the straight-and-left arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or turn left at the
                        intersection, or change lanes to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left_right'], missed ['arrow:straight_left']), actions False, unsafe
                        ['change_right'], citation None, contradictions ['go_straight allowed although no
                        arrow shows it', 'turn_right prohibited although an arrow shows it']
Tokens                  in 3717, out 713, 12.98 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        traffic signals ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line next to a white metal fence. Photo 2 confirms a white
                        solid line and a raised curb with a fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the right lane. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a white solid edge line on the left and a white dashed lane line
                        on the right indicate my lane is the leftmost of two lanes. | roles: the white solid
                        edge line and white dashed lane line fit their respective roles. | markings: there are
                        no markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or fence
                        area.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and physical fence.
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed white lane line.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane;
                        do not cross the left boundary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3717, out 634, 12.07 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an underpass beneath the
                        Dashan Bridge. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 confirms a white dashed line next to my car with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to a raised curb. Photo 2 shows a white solid
                        line and a raised stone curb forming the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2 shows a white right-turn arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        index 3 agree with having a lane line on the left and an edge line on the right. |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        with a curb fits the role of an edge line. | markings: the right-turn arrow is
                        consistent with being in the rightmost lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows lane changes to the left.
Step 5  Rule            right_boundary: A white solid edge line and curb prohibit leaving the roadway to the
                        right.
Step 5  Rule            arrow:merge_right: The right-turn arrow allows turning right and prohibits going
                        straight, turning left, or making a U-turn.
Step 6  change_left     allowed: allowed by the white dashed lane line on the left.
Step 6  change_right    prohibited: prohibited by the white solid edge line and raised curb on the right.
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited by the right-turn arrow in the lane.
Step 6  turn_left       prohibited (correct): prohibited by the right-turn arrow in the lane.
Step 6  turn_right      allowed (correct): allowed by the right-turn arrow in the lane.
Step 6  u_turn          prohibited (correct): prohibited by the right-turn arrow in the lane.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a right-turn-only lane. If you intend to go straight or turn left, you must
                        change to the left lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:right']), actions False, unsafe [], citation
                        None, contradictions ['go_straight, turn_left, turn_right, u_turn decided without an
                        arrow or prohibited-movement marking']
Tokens                  in 3717, out 741, 11.17 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead on a clear
                        stretch of road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues straight ahead.
                        Photo 2 confirms a solid white line immediately to the left of the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, consisting of several dashes and
                        gaps. Photo 2 shows a clear white dash and gap immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a solid white edge line on the left indicates the leftmost lane,
                        and a dashed lane line on the right indicates another lane to the right. | roles: the
                        white solid line on the left fits the role of an edge line, and the white dashed line
                        on the right fits the role of a lane line. | markings: there are no markings in the
                        lane to contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left into the
                        shoulder or barrier area.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white edge line which prohibits
                        crossing it.
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line which allows
                        changing lanes.
Step 6  go_straight     allowed (correct): no marking governs this action, and the boundaries do not restrict
                        it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): no marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): no marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 668, 11.21 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        traffic signals. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line next to a metal fence. Photo 2 confirms a white solid
                        line immediately to the left of the car, with a metal fence and a curb beside it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows it as well.; line:crosswalk (full): Photo 1 and Photo 2 show a white zebra
                        crosswalk across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the left edge_line and right lane_line | roles: the white solid edge_line and
                        white dashed lane_line fit their roles | markings: the straight arrow is consistent
                        with the lane boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A dashed white lane line allows crossing to the right for lane
                        changes.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight but prohibits turning
                        left, turning right, or making a U-turn.
Step 5  Rule            line:crosswalk: A crosswalk is a pedestrian crossing area and does not govern vehicle
                        movement directions.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge_line and curb
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed white lane_line
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed, but do
                        not cross the left boundary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions False, unsafe
                        ['change_right'], citation None, contradictions []
Tokens                  in 3717, out 769, 13.58 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a crosswalk and an
                        intersection. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 shows a
                        broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows it as well.; line:crosswalk (full): Photo 1 and Photo 2 show a white zebra
                        crosswalk across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a solid white line on the left indicates the edge of the roadway,
                        making my lane the leftmost. | roles: the white solid line on the left fits the role
                        of an edge line, and the white dashed line on the right fits the role of a lane line.
                        | markings: the straight-ahead arrow is consistent with the lane's position and
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left of the roadway.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight but prohibits turning
                        left, turning right, or making a U-turn.
Step 5  Rule            line:crosswalk: A crosswalk is a pedestrian crossing area and does not govern vehicle
                        movement actions other than yielding to pedestrians.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line (left_boundary).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line
                        (right_boundary).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (arrow:straight).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (arrow:straight).
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (arrow:straight).
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (arrow:straight).
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed, but do
                        not cross the solid line on the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 3717, out 824, 13.72 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, facing a yellow grid area (box junction) ahead of
                        an intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several short white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, separating the roadway from a
                        curb/sidewalk area. Photo 2 shows a solid yellow line next to my car and a raised
                        curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show a yellow grid area (box junction) across
                        the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a lane line on the left and an edge line on the right indicate my
                        lane is the rightmost of two lanes. | roles: the white dashed line fits the role of a
                        lane line, and the yellow solid line fits the role of an edge line. | markings: the
                        grid area is a standard box junction marking across the lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid yellow edge line and curb prohibit leaving the roadway to the
                        right.
Step 5  Rule            area:grid: Vehicles must not enter the grid area if the exit is blocked, to avoid
                        obstructing traffic.
Step 6  change_left     allowed (correct): allowed by the broken white lane line on the left.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid yellow edge line and
                        curb on the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no arrows prohibiting it and the
                        lane does not end.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no left-turn waiting area or two-way
                          left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but do
                        not enter the yellow grid area if the road ahead is blocked.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 778, 12.14 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, driving straight ahead on a multi-lane road.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a solid yellow line
                        next to the car and continuing ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line next
                        to the car with clear gaps and dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries: a center line on the left and a lane line on the right indicate
                        the car is in the leftmost lane of a two-lane road. | roles: the yellow solid line
                        fits the role of a center line, and the white dashed line fits the role of a lane
                        line. | markings: there are no markings in the lane to contradict the boundaries. |
                        unseen: no | result: consistent
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
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the yellow line to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['symbol:other']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 630, 12.21 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There is a
                        bus stop and a sidewalk to the right. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from a red-colored lane/shoulder,
                        with a raised curb further right. Photo 2 shows the white solid line next to my car
                        and the red pavement to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow in my lane pointing straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        the 3rd lane agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        fits the role of an edge line | markings: the straight arrow is consistent with the
                        lane boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the shoulder or red
                        lane.
Step 5  Rule            arrow:straight: The straight arrow allows going straight but prohibits turning left,
                        turning right, or making a U-turn.
Step 6  change_left     allowed: allowed by the white dashed lane line
Step 6  change_right    prohibited: prohibited by the white solid edge line and the raised curb
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the straight arrow in the lane
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow in the lane
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the straight arrow in the lane
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow in the lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may change to the left lane if needed, but
                        do not enter the red lane or shoulder on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation None, contradictions []
Tokens                  in 3717, out 735, 13.87 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with a truck
                        in front. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a solid
                        white line immediately to the left of the lane, bordering a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the left edge line and right lane line | roles: the white solid edge line and
                        white dashed lane line fit their roles | markings: no markings present in the lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the barrier area.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        concrete barrier
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed white lane line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the right lane. Do not
                        cross the left boundary into the barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3717, out 616, 11.53 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection with
                        traffic signals ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow dashed line separating my lane from the left lane. Photo 2
                        shows the same yellow dashed line next to my car, consisting of long dashes and gaps.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the right lane. Photo 2
                        shows the same white dashed line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane. Photo 1
                        confirms this arrow is located just before the intersection.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right. |
                        roles: the yellow dashed line on the left and white dashed line on the right are
                        consistent with lane-separating markings in this region. | markings: the straight-
                        ahead arrow is consistent with the lane's position and boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A dashed yellow line allows lane changes to the left.
Step 5  Rule            right_boundary: A dashed white line allows lane changes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight but prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (correct): allowed by the dashed yellow left boundary
Step 6  change_right    allowed (correct): allowed by the dashed white right boundary
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow in my lane
Step 6  turn_left       prohibited: prohibited by the straight-ahead arrow in my lane
Step 6  turn_right      prohibited: prohibited by the straight-ahead arrow in my lane
Step 6  u_turn          prohibited: prohibited by the straight-ahead arrow in my lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a straight-through lane. You may continue straight or change lanes if
                        needed, but you cannot turn left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 734, 12.29 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        traffic signals ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane;
                        Photo 1 confirms it is the only arrow in this lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right
                        boundaries. | roles: the white dashed lines on both sides are consistent with lane
                        lines separating lanes of the same direction. | markings: the straight-ahead arrow is
                        consistent with the lane's position and boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): the left boundary is a white dashed line, which
                        allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): the right boundary is a white dashed line, which
                        allows lane changes.
Step 6  go_straight     allowed (correct): the straight-ahead arrow in my lane allows this movement.
Step 6  turn_left       prohibited (correct): the straight-ahead arrow in my lane prohibits turning left.
Step 6  turn_right      prohibited (correct): the straight-ahead arrow in my lane prohibits turning right.
Step 6  u_turn          prohibited (correct): the straight-ahead arrow in my lane prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left or
                        right if needed, but you must not turn at the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation None,
                        contradictions []
Tokens                  in 3717, out 749, 11.68 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight ahead with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line to the left of my car. Photo 2 confirms a white
                        broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right of my car. Photo 2 confirms a white
                        solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right, placing my
                        car in the second lane from the left (middle lane). | roles: the white dashed line on
                        the left fits the role of a lane_line, and the white solid line on the right fits the
                        role of an edge_line. | markings: no markings were observed in my lane. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the shoulder or area
                        beyond the roadway.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane prohibiting
                        it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change to the left lane, but
                        do not cross the solid line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 689, 13.21 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. (lanes 4,
                        mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction.
                        Photo 2 confirms two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line. Photo 2 shows a white dashed line with clear gaps
                        next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left indicates I am in the
                        leftmost lane of my direction. | roles: the double yellow center line and white dashed
                        lane line fit their roles. | markings: there are no markings in my lane to contradict.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A white dashed line allows lane changes into the adjacent lane.
Step 6  change_left     prohibited (correct): the left boundary is a double solid yellow center line which
                        prohibits crossing it
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          prohibited: the left boundary is a double solid yellow center line which prohibits
                        U-turns
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the double yellow lines to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 3717, out 616, 11.43 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading straight. The road continues
                        forward with no immediate intersection or ramp visible. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line. Photo 2 shows two solid yellow lines side by side
                        next to the car and continuing ahead.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line. Photo 2 shows a white dashed line next to the car
                        with clear gaps and dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a center line on the left and a lane line on the right indicate
                        the leftmost lane of the direction. | roles: the double yellow center line and white
                        dashed lane line fit their roles. | markings: the straight arrow is consistent with
                        the boundaries and the road layout. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A white dashed line allows lane changes into the adjacent lane.
Step 5  Rule            arrow:straight: A straight arrow allows going straight and prohibits turning left,
                        turning right, or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line
Step 6  change_right    allowed (correct): allowed by the white dashed lane line
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the straight arrow in the lane
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited by the straight arrow in the lane
Step 6  turn_right      prohibited: prohibited by the straight arrow in the lane
Step 6  u_turn          prohibited: prohibited by the straight arrow in the lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed, but do
                        not cross the double yellow line to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left_u_turn']), actions False, unsafe ['go_straight'], citation None,
                        contradictions []
Tokens                  in 3717, out 697, 13.61 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead under an
                        overpass. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 confirms a white
                        dashed line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 confirms a white
                        dashed line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns fit the role of lane lines | markings: there are no markings in my
                        lane to conflict with | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line which allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line which allows lane changes
Step 6  go_straight     allowed (correct): no marking governs this action, and the lane does not end
Step 6  turn_left       not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  turn_right      not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  u_turn          not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the left or right lanes as
                        needed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 607, 11.59 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead under an
                        overpass on the left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: the
                        white dashed patterns fit the role of lane lines | markings: there are no markings in
                        my lane to conflict with boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (WRONG, label prohibited): the left_boundary is a white dashed line which
                        allows lane changes
Step 6  change_right    allowed (WRONG, label prohibited): the right_boundary is a white dashed line which
                        allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed by
                        default
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane; you may continue straight or change lanes to the left or
                        right as needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation None,
                        contradictions []
Tokens                  in 3717, out 625, 11.56 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards a distant
                        intersection. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns fit the role of lane lines | markings: there are no markings in my
                        lane to conflict with boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed lane line which allows lane
                        changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed lane line which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed by
                        default
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane that allows going straight or changing lanes to either side. Follow
                        the overhead signs to select the correct lane for your intended turn at the
                        intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 632, 11.56 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car and continuing ahead. Photo 2
                        confirms a white dashed line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car and continuing ahead. Photo 2
                        confirms a white dashed line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows it continuing towards the intersection.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right. | roles: the white
                        dashed lines on both sides are consistent with lane lines separating lanes of the same
                        direction. | markings: the straight-ahead arrow is consistent with the lane
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed left boundary
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the white dashed right boundary
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow in my lane
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a straight-through lane. You may continue straight or change lanes if
                        needed, but you cannot turn left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3717, out 700, 11.63 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left edge of the road. Photo 2 confirms a
                        solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the left edge line and right lane line | roles: the white solid edge line and
                        white dashed lane line fit their roles | markings: no markings in my lane | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing the boundary to leave the
                        roadway.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid white edge line which
                        prohibits leaving the roadway
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line which allows
                        changing lanes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight or change to the right lane, but do
                        not cross the left edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 595, 9.38 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, approaching an intersection. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a white solid line next to a white metal fence. Photo 2 confirms a white
                        solid line immediately to the left of the car, with the fence running parallel to it.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from a bicycle lane. Photo 2
                        shows the same white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; a white solid edge line on the left and a dashed line on the right
                        indicate a single vehicle lane next to a non-motorized lane. | roles: the white solid
                        line fits the role of an edge line (roadway boundary), and the white dashed line fits
                        the role of a lane line (separating vehicle and bicycle lanes). | markings: no
                        markings are present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area beyond it (the
                        fence/sidewalk).
Step 5  Rule            right_boundary: A dashed white line allows crossing into the adjacent lane (bicycle
                        lane) when safe to do so.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid white line, which
                        prohibits crossing it.
Step 6  change_right    allowed (WRONG, label not_determined): the right_boundary is a dashed white line,
                        which allows crossing it.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can proceed straight or move right into the bicycle lane if necessary, but do not
                        cross the solid line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3717, out 664, 11.44 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway in China, approaching an exit for Beijing West
                        (北原西路). (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car that becomes a solid white line
                        further ahead. Photo 2 shows the white dashed line immediately in front of my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: the white
                        dashed lines correctly fit the role of lane lines separating lanes of the same
                        direction. | markings: there are no markings in my lane to contradict. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (WRONG, label not_determined): the left boundary is a white dashed line, which
                        allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): the right boundary is a white dashed line next to
                        the car, which allows lane changes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3717, out 648, 10.94 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 confirms a white dashed line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 confirms a white dashed line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns fit the role of lane lines | markings: no markings were observed in my
                        lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line which allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the boundaries do
                        not restrict it
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 617, 10.62 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. (lanes 3,
                        mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, followed by a white solid line further
                        ahead. Photo 2 shows a solid yellow line immediately to the right of my car.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the Chinese characters '公交' (Bus) painted in yellow in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a lane line on the left and an edge line on the right
                        indicate I am in the rightmost lane. | roles: the white dashed line fits the role of a
                        lane line, and the yellow solid line fits the role of an edge line for a bus lane. |
                        markings: the '公交' text identifies this as a bus lane, which is consistent with the
                        yellow solid boundary on the right. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A solid yellow line prohibits crossing into the area to the right.
Step 5  Rule            text:bus: This lane is reserved for buses; ordinary cars are prohibited from driving
                        in it.
Step 6  change_left     allowed (contested, correct): allowed by the white dashed left boundary.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right boundary.
Step 6  go_straight     prohibited (contested, correct): prohibited because the lane is marked as a bus lane
                        (text:bus).
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane. You should change to the left lane immediately as
                        ordinary vehicles are prohibited from using this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions ['go_straight
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 3717, out 743, 12.79 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or expressway in China, heading straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: the
                        white dashed patterns fit the role of lane lines | markings: there are no markings in
                        my lane to conflict with | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed lane line which allows lane
                        changes
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line which allows lane
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
Tokens                  in 3717, out 626, 11.6 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway in China, traveling straight ahead on a clear road.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries. | roles: the
                        white dashed patterns for both boundaries are consistent with the role of lane lines.
                        | markings: there are no markings in my lane to conflict with the boundaries. |
                        unseen: no | result: consistent
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
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 640, 10.41 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, heading straight ahead on a clear
                        day. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: the
                        white dashed patterns fit the role of lane lines | markings: there are no markings in
                        my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed lane line which allows lane
                        changes
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line which allows lane
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
Tokens                  in 3717, out 626, 9.91 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban expressway in China, traveling straight
                        ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, which is the edge of the roadway. Photo
                        2 confirms a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line that is dashed near the car and becomes solid further
                        ahead. Photo 2 shows a dashed white line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a left edge line and a right lane line indicate the car is in the
                        leftmost lane of a two-lane road. | roles: the white solid left boundary fits the role
                        of an edge line, and the white dashed right boundary fits the role of a lane line. |
                        markings: there are no markings in the lane to contradict. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A dashed white lane line allows changing to the right lane.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white edge line which prohibits
                        crossing it
Step 6  change_right    allowed (WRONG, label prohibited): the right_boundary is a dashed white lane line
                        which allows changing lanes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3717, out 631, 11.74 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, with a clear road ahead and no
                        immediate intersections or ramps visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries. | roles: the
                        white dashed patterns for both boundaries are consistent with the role of lane_line. |
                        markings: there are no markings in my lane, which is consistent with a standard
                        highway lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and it is allowed by
                        default in a highway lane.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 650, 11.72 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, with a clear road ahead and no
                        immediate intersections or ramps. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 confirms a white
                        dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right of my car, with a guardrail further
                        right. Photo 2 shows a white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right, placing my
                        car in the second lane from the left (middle lane). | roles: the white dashed line
                        fits the role of a lane_line, and the white solid line fits the role of an edge_line.
                        | markings: no markings are present in my lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the shoulder or
                        leaving the roadway to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line on the left.
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and the
                        lane does not end.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change to the left lane, but
                        do not cross the solid line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 689, 12.4 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road or highway, traveling straight ahead on a curved
                        section of the road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues as the edge of the
                        roadway. Photo 2 confirms a solid white line immediately to the left of the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line | roles: the white solid edge line on the left and white dashed lane line on
                        the right fit their roles | markings: no markings present in the lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing the boundary to the left.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid white edge line which
                        prohibits crossing it
Step 6  change_right    allowed (WRONG, label prohibited): the right_boundary is a dashed white lane line
                        which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid line on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3717, out 633, 10.61 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road in China with traffic moving in the same direction; the road
                        continues straight ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a metal guardrail. Photo 2
                        shows the white solid line next to my car and the guardrail further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        index 3 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        fits the role of an edge line | markings: no markings in my lane to check | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and guardrail prohibit leaving the roadway to
                        the right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line and
                        guardrail
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 654, 11.67 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The road is a multi-lane highway in China, with traffic flowing straight ahead. My car
                        is in one of the lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the 2nd lane agree with having lane lines on both my left and right | roles: the white
                        dashed patterns fit the role of lane lines | markings: there are no markings in my
                        lane to contradict | unseen: no | result: consistent
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
Tokens                  in 3717, out 632, 9.95 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or urban expressway with sound barriers on
                        both sides. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: white
                        dashed lines are consistent with the role of lane lines | markings: no markings
                        present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows lane changes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows lane changes to the right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed lane line which allows changing
                        left
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line which allows
                        changing right
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 619, 10.78 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, moving straight ahead on a clear
                        road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a metal guardrail and a
                        sound barrier wall. Photo 2 shows the white solid line next to my car and the
                        guardrail immediately to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having a lane line on the left and an edge line on the right | roles: the
                        white dashed line fits the role of a lane line, and the white solid line fits the role
                        of an edge line | markings: no markings present in my lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and guardrail prohibit leaving the roadway to
                        the right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line and guardrail
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the left lane. Do not
                        cross the right boundary.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 656, 10.1 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading towards a slight curve
                        to the left. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a concrete barrier. Photo 2
                        shows the solid white line next to my car and the concrete barrier immediately to its
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane_line on the left and an edge_line on the right | roles: the white
                        dashed line fits the role of a lane_line and the white solid line fits the role of an
                        edge_line | markings: no markings in my lane to check | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and concrete barrier prohibit leaving the
                        roadway to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line and concrete barrier
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move right due to the barrier.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 661, 12.1 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road, likely a bridge or highway, with a blue bus ahead in
                        the same lane. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, followed by a metal guardrail. Photo 2
                        shows the solid white line next to the car and the guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail. Photo 2
                        shows the solid white line next to the car and the guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the edge lines on both sides | roles: the solid white lines on both sides
                        fit the role of edge lines for a single-lane road | markings: no markings present in
                        the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white edge line which prohibits
                        crossing
Step 6  change_right    prohibited (correct): the right_boundary is a solid white edge line which prohibits
                        crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and follow the vehicle ahead; lane changes are prohibited on both
                        sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 609, 11.19 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway in China, with a clear road stretching ahead. (lanes 4,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a solid
                        white line and a raised concrete barrier immediately to the left of my lane.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line. Photo 2 shows a white dashed line with clear gaps
                        between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a left edge line indicates I am in the leftmost lane. |
                        roles: the white solid edge line and white dashed lane line fit their respective
                        roles. | markings: there are no markings in my lane to contradict. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid white edge line and barrier prohibit leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        concrete barrier.
Step 6  change_right    allowed (correct): allowed by the dashed white lane line.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and the
                        lane does not end.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost through lane. You may continue straight or change to the right
                        lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 623, 12.41 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a single lane of travel in its direction, heading
                        towards a distant intersection or overpass. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the road from a raised curb and greenery.
                        Photo 2 confirms a solid white line next to the car and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a parking/stopping area
                        where vehicles are parked. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and index 1 agree
                        with the edge lines on both sides | roles: the solid white lines on both sides
                        correctly serve as edge lines for a single-lane road | markings: no markings present
                        in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the non-roadway area.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the parking/shoulder
                        area.
Step 6  change_left     prohibited (WRONG, label not_determined): the left_boundary is a solid white edge line
                        which prohibits crossing
Step 6  change_right    prohibited (WRONG, label not_determined): the right_boundary is a solid white edge
                        line which prohibits crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 610, 10.71 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road in China, traveling straight ahead. There is a
                        concrete barrier to the left and a curb to the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a continuous concrete barrier on the left. Photo 2 confirms the concrete
                        barrier is immediately next to the car.
                        none solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right that is dashed. Photo 2 shows the line next to
                        the car is a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the left boundary being an edge_line (barrier) and the right boundary being
                        a lane_line. | roles: the concrete barrier fits the role of an edge_line; the white
                        dashed line fits the role of a lane_line. | markings: no markings were observed in the
                        lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing a concrete barrier is prohibited.
Step 5  Rule            right_boundary: Crossing a white dashed line to change lanes is allowed.
Step 6  change_left     prohibited (correct): the left_boundary is a concrete barrier which prohibits leaving
                        the lane to the left.
Step 6  change_right    allowed (WRONG, label not_determined): the right_boundary is a white dashed line which
                        allows changing lanes to the right.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the right. Do not attempt to cross the
                        barrier on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['rightmost lane,
                        but a lane line on the right']
Tokens                  in 3717, out 631, 10.99 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a raised concrete curb and a hedge bordering the left side of the road.
                        Photo 2 confirms the presence of a continuous raised concrete curb immediately to the
                        left of my lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a curb on the left indicates my lane is the leftmost
                        lane. | roles: the white dashed line on the right fits the role of a lane line. |
                        markings: there are no markings in my lane to contradict. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The raised curb prohibits leaving the roadway to the left.
Step 5  Rule            right_boundary: The white dashed line allows lane changes to the right.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the raised curb
                        (left_boundary).
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the white dashed line
                        (right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 625, 9.41 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane urban road heading straight. There are no intersections or
                        ramps immediately ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the presence of edge lines on both sides | roles: the solid white lines on
                        both sides fit the role of edge lines for a single-lane road | markings: no markings
                        in the lane to contradict | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white edge line which prohibits
                        crossing
Step 6  change_right    prohibited (correct): the right_boundary is a solid white edge line which prohibits
                        crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes are prohibited on both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 594, 18.46 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a green-colored surface, heading towards a traffic
                        light. There is a physical barrier on the left and a sidewalk on the right. (lanes 1,
                        mine 1, full)
Step 2  Left            Photo 1 shows a continuous grey concrete barrier on the left. Photo 2 confirms a
                        raised concrete barrier immediately next to the car.
                        none solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating the lane from a sidewalk area. Photo 2
                        shows a white dashed line with short dashes and gaps.
                        white dotted, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge boundaries on both sides | roles: the concrete barrier on the left and
                        the dotted white line on the right both fit the role of edge lines | markings: no
                        markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The concrete barrier prohibits leaving the lane to the left.
Step 5  Rule            right_boundary: The dotted white edge line allows crossing into the adjacent area,
                        though it is a sidewalk.
Step 5  Rule            right_boundary: The dotted white edge line allows crossing into the adjacent area,
                        though it is a sidewalk.
Step 6  change_left     prohibited (correct): prohibited by the concrete barrier
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dotted white edge line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not attempt to move left due to the
                        concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3717, out 655, 12.93 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight ahead with
                        other vehicles in the same direction. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the road from a raised median with plants.
                        Photo 2 shows the same solid white line next to the car and the raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the road from a sidewalk. Photo 2 shows
                        the same solid white line next to the car and the sidewalk edge.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the edge lines on both left and right | roles: the white solid lines on
                        both sides fit the role of edge lines for a single-lane road | markings: there are no
                        markings in the lane to contradict | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the median.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the sidewalk.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white edge line which prohibits
                        crossing
Step 6  change_right    prohibited (WRONG, label allowed): the right_boundary is a solid white edge line which
                        prohibits crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 610, 10.05 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a city road with a single lane in its direction, bordered by a
                        median on the left and a sidewalk on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a raised curb and hedge. Photo 2 confirms a
                        solid white line and a raised curb immediately to the left of the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a paved area. Photo 2 shows
                        a solid white line next to the car, with a raised curb further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides | roles: the solid white lines on both sides fit the
                        role of edge lines for a single-lane road | markings: no markings present in the lane
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line and curb prohibit leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: A solid white edge line and curb prohibit leaving the roadway to the
                        right.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and curb on the left
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        curb on the right
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and it
                        is the only available path
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight; lane changes are prohibited on both
                        sides due to the road edges.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 661, 11.97 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead under an
                        overpass on the left. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 shows a
                        broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a solid white edge line on the left indicates the leftmost lane.
                        | roles: the white solid line on the left fits the role of an edge line, and the white
                        dashed line on the right fits the role of a lane line. | markings: no markings present
                        in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or non-
                        motorized area.
Step 5  Rule            right_boundary: A broken white lane line allows lane changes between lanes of the same
                        direction.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid white edge line which
                        prohibits crossing it
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 622, 10.63 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a narrow urban road, possibly a shared path or a service road, with
                        buildings and greenery on the right and a sidewalk on the left. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a sidewalk. Photo 2 shows
                        the same solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a paved area with greenery
                        and a curb. Photo 2 shows the same solid white line next to the car and a raised curb
                        further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white straight-ahead arrow painted
                        in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; it is a single lane bounded by edge lines on both sides. | roles: the
                        white solid lines fit the role of edge lines for a narrow road. | markings: the
                        straight-ahead arrow is consistent with the lane's direction. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the sidewalk.
Step 5  Rule            right_boundary: A solid white edge line and curb prohibit crossing to the right.
Step 5  Rule            arrow:straight: The straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line (left_boundary).
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb
                        (right_boundary).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (arrow:straight).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (arrow:straight).
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (arrow:straight).
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (arrow:straight).
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not attempt to change lanes or turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 726, 12.11 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, driving straight ahead in a single lane of
                        traffic. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a solid
                        white line and a raised concrete barrier immediately to the left of the lane.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a parking/stopping area.
                        Photo 2 shows a solid white line next to the car, with a raised curb and parked
                        vehicles further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the edge lines on both left and right boundaries | roles: the solid white
                        lines on both sides correctly serve as edge lines for a single-lane road | markings:
                        no markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line and barrier prohibit leaving the lane to the
                        left.
Step 5  Rule            right_boundary: A solid white edge line and curb prohibit leaving the lane to the
                        right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white line and barrier which
                        prohibits lane changes
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid white line and curb
                        which prohibits lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to either side are prohibited by
                        the solid edge lines and physical barriers.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 627, 10.99 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with traffic
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the road from a grassy area. Photo 2 shows
                        the same solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a parking or stopping area
                        where cars are lined up. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the car is in a single lane bounded by edge lines on both sides. |
                        roles: the white solid lines on both sides fit the role of edge lines. | markings:
                        there are no markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the non-road area.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the parking/stopping
                        area.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white edge line which prohibits
                        crossing it
Step 6  change_right    prohibited (correct): the right_boundary is a solid white edge line which prohibits
                        crossing it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 605, 12.57 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a metal fence and a solid white line along the left edge of the road.
                        Photo 2 confirms a solid white line next to the car and a metal fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right lane. Photo 2
                        shows a single white dash and gap next to the car, and further ahead it remains a
                        broken line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a solid white edge line on the left indicates my lane
                        is the leftmost lane. | roles: the white solid edge line and white dashed lane line
                        fit their respective roles. | markings: there are no markings in my lane to check. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label not_determined): the left_boundary is a solid white edge line
                        with a fence, which prohibits crossing it.
Step 6  change_right    allowed (correct): the right_boundary is a broken white lane line, which allows
                        changing lanes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 623, 12.08 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with other
                        vehicles and a scooter in view. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white metal fence and a solid white line along the left edge of the
                        road. Photo 2 confirms a solid white line next to the car and continuing ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from another lane to the right.
                        Photo 2 shows a white dashed line next to the car with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a solid edge line on the left and a dashed lane line on the right
                        indicate my lane is the leftmost of two lanes. | roles: the white solid line on the
                        left fits the role of an edge line, and the white dashed line on the right fits the
                        role of a lane line. | markings: there are no markings in my lane to contradict. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left into the
                        shoulder or fence area.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid white edge line which
                        prohibits crossing it.
Step 6  change_right    allowed (WRONG, label prohibited): the right_boundary is a dashed white lane line
                        which allows changing lanes.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane;
                        do not cross the left boundary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3717, out 659, 11.78 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings and trees on both sides, driving straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left edge of the road. Photo 2 shows the same
                        solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 shows the same
                        solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the edge lines on both sides | roles: the white solid lines on both sides fit the
                        role of edge lines | markings: there are no markings in the lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing to the right.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid white edge line which
                        prohibits crossing
Step 6  change_right    prohibited (WRONG, label not_determined): the right_boundary is a solid white edge
                        line which prohibits crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes are prohibited by the solid edge
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 581, 10.99 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, traveling straight ahead. There are no immediate
                        intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my lane, and further ahead it remains solid.
                        Photo 2 shows a solid white line immediately to the right of my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane_line on the left and an edge_line on the right | roles: the white
                        dashed line fits the role of a lane_line and the white solid line fits the role of an
                        edge_line | markings: no markings in my lane to check | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the area to the right
                        (bicycle lane/shoulder).
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost vehicle lane. You may go straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 665, 11.92 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, driving straight ahead on a road with trees on
                        both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow solid line on the left. Photo 2 shows the same yellow solid
                        line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a raised curb. Photo 2
                        shows the white solid line and the raised curb next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left and an edge line on the right
                        indicate a single lane of travel in my direction. | roles: the yellow solid center
                        line and white solid edge line fit their respective roles. | markings: there are no
                        markings in my lane to conflict with boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A solid white edge line and curb prohibit leaving the roadway to the
                        right.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid yellow center line
                        which prohibits crossing it.
Step 6  change_right    prohibited (correct): the right_boundary is a solid white edge line and curb which
                        prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 625, 11.8 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 confirms a white
                        dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 confirms a white
                        dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns fit the role of lane lines | markings: no markings present in my lane
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line which allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the boundaries do
                        not restrict it
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 614, 10.21 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, approaching a crosswalk and an intersection.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 confirms a solid white line next
                        to the car and continuing ahead.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car and a raised curb further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1 and Photo 2 show a white arrow pointing straight
                        and right.; line:crosswalk (full): Photo 1 and Photo 2 show a white zebra crosswalk
                        across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; it is a single lane bounded by edge lines. | roles: the white solid
                        lines fit the role of edge lines for a single-lane road. | markings: the straight-
                        right arrow is consistent with the lane's position. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A solid white edge line and curb prohibit crossing to the right.
Step 5  Rule            arrow:straight_right: The arrow allows going straight or turning right, but prohibits
                        turning left or making a U-turn.
Step 5  Rule            line:crosswalk: The crosswalk is for pedestrians and does not govern the car's
                        movement direction.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white left boundary
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white right boundary
                        and curb
Step 6  go_straight     allowed (correct): allowed by the straight-right arrow
Step 6  turn_left       prohibited (correct): prohibited by the straight-right arrow
Step 6  turn_right      allowed (correct): allowed by the straight-right arrow
Step 6  u_turn          prohibited (correct): prohibited by the straight-right arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane; you may proceed straight or turn right at the intersection. Do not
                        change lanes or turn left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 3717, out 746, 12.75 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead towards a
                        bridge or underpass. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow solid line next to my car and further ahead. Photo 2 confirms a
                        yellow solid line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car and further ahead. Photo 2 shows a
                        white dashed line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left and a lane line on the right
                        place my car in the second lane from the left of the roadway, but the first lane of my
                        direction is to my right. | roles: the yellow solid line fits the role of a center
                        line, and the white dashed line fits the role of a lane line. | markings: no markings
                        in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): the left boundary is a solid yellow center line
                        which prohibits crossing it
Step 6  change_right    allowed (WRONG, label not_determined): the right boundary is a white dashed lane line
                        which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change to the right lane, but
                        you must not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 647, 11.98 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling under an overpass. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, bordering a concrete wall. Photo 2
                        shows the same white solid line next to my car, and a raised concrete curb/barrier
                        immediately to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right | roles: the
                        white dashed line fits the role of a lane_line and the white solid line fits the role
                        of an edge_line | markings: no markings present in my lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows crossing for lane changes.
Step 5  Rule            right_boundary: A white solid edge line and curb prohibit crossing to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line and curb
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the right boundary
                        into the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 646, 10.66 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading straight toward a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from a shoulder or bicycle lane on
                        the right. Photo 2 shows a continuous white solid line next to my car, with a raised
                        curb visible further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right, as there is
                        one more lane to the left. | roles: the white dashed line fits the role of a lane_line
                        and the white solid line fits the role of an edge_line. | markings: no markings are
                        present in my lane to contradict boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the shoulder or
                        bicycle lane on the right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the solid white
                        line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 669, 10.62 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane road passing under a bridge, with a red wall on the right
                        and bushes on the left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a curb and bushes on the left. Photo 2 confirms a raised concrete curb
                        separating the road from the bushes.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a curb and a red wall on the right. Photo 2 shows a raised concrete curb
                        next to the road.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane position
                        agree with the boundaries; it is a single lane bounded by curbs on both sides | roles:
                        the role of edge_line fits the presence of curbs on both sides | markings: no markings
                        present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A raised curb prohibits leaving the lane to the left.
Step 5  Rule            right_boundary: A raised curb prohibits leaving the lane to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a curb which prohibits this action
Step 6  change_right    prohibited (correct): the right_boundary is a curb which prohibits this action
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in the current lane and follow the vehicle ahead; lane changes are prohibited due
                        to the curbs on both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 589, 11.94 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line and a metal guardrail/fence. Photo 2 shows the white
                        solid line and the metal fence immediately to the right of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2 shows a white right-turn arrow in my lane. Photo 1
                        confirms this arrow is the primary guidance for the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a lane line on the left and an edge line on the right indicate
                        the rightmost lane. | roles: the white dashed line fits the role of a lane line, and
                        the white solid line with a fence fits the role of an edge line. | markings: the
                        right-turn arrow is consistent with being in the rightmost lane. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A white solid line and curb prohibit leaving the roadway to the right.
Step 5  Rule            arrow:merge_right: The right-turn arrow allows turning right and prohibits going
                        straight, turning left, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed left boundary
Step 6  change_right    prohibited (correct): prohibited by the white solid right boundary and curb
Step 6  go_straight     prohibited (correct): prohibited by the right-turn arrow in the lane
Step 6  turn_left       prohibited (correct): prohibited by the right-turn arrow in the lane
Step 6  turn_right      allowed (correct): allowed by the right-turn arrow in the lane
Step 6  u_turn          prohibited (correct): prohibited by the right-turn arrow in the lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a right-turn-only lane. You must turn right at the intersection; if you
                        intend to go straight or turn left, you must change to the left lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:right', 'line:stop_line']), actions False,
                        unsafe ['change_left'], citation None, contradictions ['go_straight, turn_left,
                        turn_right, u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 3717, out 753, 13.53 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or arterial road under a bridge overpass,
                        with a clear road ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left edge of the roadway, next to a guardrail.
                        Photo 2 confirms a solid white line immediately to the left of the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a solid edge line on the left and a dashed lane line on the right
                        indicate my lane is the leftmost of two lanes. | roles: the white solid edge line and
                        white dashed lane line fit their respective roles. | markings: no markings are present
                        in the lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left of the roadway.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label allowed): the left_boundary is a solid white edge line which
                        prohibits crossing it
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 641, 9.13 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway in China, traveling straight ahead on a clear day.
                        (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the one to the left. Photo 2
                        confirms a white dashed line next to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a metal guardrail. Photo 2
                        shows a white solid line next to the car and a metal guardrail further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a blue circle with the number '60' painted in
                        white in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 3
                        agree with a lane line on the left and an edge line on the right | roles: the white
                        dashed line fits the role of a lane line, and the white solid line fits the role of an
                        edge line | markings: the speed limit marking is consistent with a highway lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A white solid edge line and guardrail prohibit leaving the roadway to
                        the right.
Step 5  Rule            text:speed_limit: The number indicates the recommended or maximum speed for the lane.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line on the left
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line and guardrail on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and it
                        is a highway lane
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or turn arrow
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or turn arrow
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or turn arrow
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the left lane if needed. Observe the speed limit
                        of 60 km/h indicated in the lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 742, 12.19 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with other
                        vehicles in the vicinity. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line to the left of my car. Photo 2 confirms a yellow
                        broken line with long dashes and gaps next to my car, extending further ahead.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of my car. Photo 2 confirms a white
                        broken line with long dashes and gaps next to my car, extending further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: the yellow
                        dashed line on the left and white dashed line on the right are consistent with lane
                        boundaries in this context. | markings: there are no markings in my lane to conflict
                        with boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: a broken yellow line allows lane changes across it.
Step 5  Rule            right_boundary: a broken white line allows lane changes across it.
Step 6  change_left     allowed (correct): allowed by the broken yellow lane line on the left.
Step 6  change_right    allowed (correct): allowed by the broken white lane line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and the
                        lane does not end.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change lanes to the left or right as
                        needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 656, 12.39 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, moving straight ahead on a clear
                        road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my car. Photo 2 confirms a white
                        dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my car. Photo 2 confirms a white
                        dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides | roles: white dashed
                        lines are consistent with lane_line roles | markings: no markings present in the lane
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line which allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the lane does not
                        end
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 614, 10.53 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, with a clear road ahead. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: the
                        white dashed pattern fits the role of a lane_line for both boundaries | markings:
                        there are no markings in my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line, which allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed by
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
Tokens                  in 3717, out 631, 9.49 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, heading straight on a clear day.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a concrete barrier. Photo 2
                        confirms a white solid line next to my car and a raised concrete barrier immediately
                        to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right | roles: the
                        white dashed line fits the role of a lane_line and the white solid line fits the role
                        of an edge_line | markings: no markings present in my lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and concrete barrier prohibit leaving the
                        roadway to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line, which allows lane changes
Step 6  change_right    prohibited (correct): the right_boundary is a white solid line and a concrete barrier,
                        which prohibits leaving the lane
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not attempt to move right as
                        there is a concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 649, 12.35 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban expressway passing under an overpass.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a continuous yellow line next to a metal guardrail. Photo 2 confirms a
                        solid yellow line and a metal guardrail immediately to the left of the lane.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the left edge line and right lane line | roles: the yellow solid edge line and
                        white dashed lane line fit their roles | markings: no markings present in the lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid yellow line and guardrail, which
                        prohibits crossing
Step 6  change_right    allowed (WRONG, label not_determined): the right_boundary is a white dashed line,
                        which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left boundary.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 600, 11.96 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, heading straight ahead with no
                        immediate intersections or ramps visible. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a metal guardrail. Photo 2 confirms a solid
                        white line and the presence of a metal barrier/guardrail immediately to the left of
                        the line.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a solid white edge line on the left indicates the leftmost lane.
                        | roles: the solid white edge line and dashed white lane line fit their respective
                        roles. | markings: no markings are present in the lane, which is consistent with a
                        highway environment. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left of the roadway.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and the physical
                        barrier.
Step 6  change_right    allowed (correct): allowed by the dashed white lane line.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and the
                        lane does not end.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right lane if needed. Do not cross the left
                        boundary due to the solid line and guardrail.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 655, 12.87 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, with a clear road ahead. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: the
                        white dashed patterns fit the role of lane lines | markings: there are no markings in
                        my lane to conflict with | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line, which allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the boundaries do
                        not prohibit it
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 628, 10.63 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway in China, traveling straight ahead on
                        a clear day. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a metal guardrail. Photo 2 confirms a solid
                        white line immediately to the left of the lane, with the guardrail running parallel.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a solid edge line on the left and a dashed lane line on the right
                        indicate the leftmost lane of a multi-lane road. | roles: the white solid line on the
                        left fits the role of an edge line, and the white dashed line on the right fits the
                        role of a lane line. | markings: there are no markings in the lane to contradict. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left of the roadway.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        the presence of a guardrail.
Step 6  change_right    allowed (correct): allowed by the dashed white lane line.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and the
                        lane continues forward.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right lane if needed. Do not cross the left
                        boundary due to the solid line and guardrail.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 683, 11.91 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The road is a multi-lane highway in China, with a clear path ahead and no immediate
                        intersections or ramps. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left edge of the roadway, next to a metal
                        guardrail. Photo 2 confirms a solid white line immediately to the left of my car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 1 agree with the left boundary being an edge_line and the right boundary being a
                        lane_line | roles: the white solid edge line and white dashed lane line fit their
                        respective roles | markings: no markings present in my lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing the boundary to the left.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): the left_boundary is a solid white edge line which prohibits
                        crossing it
Step 6  change_right    allowed (correct): the right_boundary is a dashed white lane line which allows
                        changing lanes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of the highway. You may continue straight or change to
                        the right lane, but do not cross the left edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 628, 11.89 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway in China, traveling straight ahead on a road with
                        overhead speed limit signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps
                        visible.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the rightmost lane. Photo 2
                        shows a white solid line next to my car, extending forward without gaps.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having a lane line on both the left and right boundaries | roles: the white
                        dashed line on the left and white solid line on the right are consistent with lane
                        lines | markings: no markings were observed in my lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows lane changes to the left.
Step 5  Rule            right_boundary: A white solid lane line prohibits lane changes to the right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed line, which allows lane changes
Step 6  change_right    prohibited (correct): the right boundary is a white solid line, which prohibits lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the lane does not
                        end
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane is present
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left, but you must not change lanes
                        to the right due to the solid white line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 641, 9.85 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with other
                        vehicles in adjacent lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: the
                        white dashed patterns for both boundaries are consistent with the role of lane lines |
                        markings: there are no markings in my lane to conflict with the boundaries | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left_boundary is a white dashed line, which allows lane changes
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the boundaries do
                        not prohibit it
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 633, 11.49 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test A | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway in China, traveling straight ahead on a clear day.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which continues ahead. Photo 2 shows a
                        white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows large white characters '60' painted across the
                        lane. Photo 1 shows these characters and further ahead a yellow speed limit marking
                        '100'.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right, as the rightmost
                        lane is index 3, but here the right boundary is an edge line, meaning my lane is the
                        rightmost lane (index 3). Correcting ego_lane_index to 3. | roles: the white dashed
                        line fits a lane_line role and the white solid line fits an edge_line role. |
                        markings: the speed limit markings are consistent with a highway environment. |
                        unseen: no | result: corrected ego_lane_index to 3
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the shoulder or off
                        the roadway to the right.
Step 5  Rule            text:speed_limit: Speed limit markings indicate the maximum allowed speed and do not
                        govern lane changes or turns.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line on the left.
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and no
                        arrows restricting movement.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid line on the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 816, 11.86 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection with
                        overhead traffic signals. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my car. Photo 2 shows this line is a double
                        solid yellow line next to my car, continuing as a double solid yellow line further
                        ahead.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my car. Photo 2 shows this line is a dashed
                        white line next to my car, continuing as a dashed white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left and a lane line on the right
                        place me in the second lane from the left of the overall road, but the first lane of
                        my direction if the leftmost lane is a turn lane, or the second if it is a through
                        lane. Given the double yellow line, my lane is the leftmost through lane of my
                        direction. | roles: the double yellow center line and dashed white lane line fit their
                        roles | markings: no markings in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits crossing to the left.
Step 5  Rule            right_boundary: A dashed white line allows crossing to the right for lane changes.
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow center line
Step 6  change_right    allowed (contested, label prohibited): allowed by the dashed white lane line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may continue straight or change to the right lane, but
                        you must not cross the double yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 697, 13.31 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China, with traffic flowing straight ahead; no immediate
                        intersection or ramp is visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car and continuing ahead. Photo 2
                        confirms a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car and continuing ahead. Photo 2
                        confirms a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed pattern fits the role of a lane_line for both boundaries | markings: no
                        markings were observed in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     allowed (contested, correct): the left_boundary is a dashed white line, which allows
                        lane changes
Step 6  change_right    allowed (correct): the right_boundary is a dashed white line, which allows lane
                        changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the lane does not
                        end
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 616, 10.17 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead with a bus in
                        the adjacent lane to the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of long white dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: the white
                        color and dashed/solid patterns fit the role of lane lines. | markings: there are no
                        markings in my lane to conflict with boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows crossing for lane changes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing for lane changes.
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken white lane line on the
                        left.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and the
                        lane does not end.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but you must not change lanes to the right due to
                        the solid line. You can continue straight in your current lane.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 675, 12.2 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards a distant
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow solid line to the left of my lane. Photo 2 confirms two
                        yellow solid lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my lane. Photo 2 shows a white
                        dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left means I am in the leftmost
                        lane of my direction | roles: the double yellow solid line fits the role of a center
                        line, and the white dashed line fits the role of a lane line | markings: there are no
                        markings in my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double yellow solid line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A white dashed line allows lane changes into the adjacent lane.
Step 6  change_left     prohibited (correct): the left_boundary is a double yellow solid line which prohibits
                        crossing it
Step 6  change_right    allowed (correct): the right_boundary is a white dashed line which allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the double yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 628, 10.71 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead towards a
                        distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a bus lane on the right.
                        Photo 2 shows the same solid white line next to my car.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries: a lane line on the left and a special lane line on the right
                        indicate my lane is the middle of three lanes of my direction. | roles: the white
                        dashed line fits the role of a lane line, and the white solid line fits the role of a
                        special lane line for the bus lane. | markings: there are no markings in my lane to
                        contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white line marking a special lane (bus lane) prohibits
                        changing lanes to the right.
Step 6  change_left     allowed (contested, label prohibited): the left boundary is a dashed white line, which
                        allows lane changes.
Step 6  change_right    prohibited (contested, correct): the right boundary is a solid white line marking a
                        special lane, which prohibits changing into it.
Step 6  go_straight     allowed (correct): no marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can stay in your lane or change to the left lane, but you must not enter the bus
                        lane to your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 670, 12.43 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There is a
                        bus stop area to the left and a sidewalk with trees to the right. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a yellow dashed line separating my lane from the lane to the left. Photo
                        2 confirms a yellow dashed line with clear gaps next to the car.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow dashed line separating my lane from the lane to the right.
                        Photo 2 shows a yellow dashed line with clear gaps next to the car.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 show yellow Chinese characters painted across
                        the lane on the right side, which read '慢' (slow).
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries. | roles: yellow
                        dashed lines are used as lane separators in some urban contexts in China, fitting the
                        role of lane_line. | markings: the 'slow' text is a warning and does not contradict
                        the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A dashed line allows crossing for lane changes.
Step 5  Rule            right_boundary: A dashed line allows crossing for lane changes.
Step 5  Rule            text:other: The 'slow' marking advises reducing speed but does not prohibit movements.
Step 6  change_left     allowed (contested, correct): the left boundary is a yellow dashed line, which allows
                        lane changes.
Step 6  change_right    allowed (contested, label prohibited): the right boundary is a yellow dashed line,
                        which allows lane changes.
Step 6  go_straight     allowed (contested, correct): no marking prohibits going straight, and the lane does
                        not end.
Step 6  turn_left       not_applicable: no arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: no arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: no arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right. Please follow the 'slow' marking and reduce your speed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 747, 12.88 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China during sunrise or sunset, with traffic moving ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows two solid yellow lines side by side. Photo 2 confirms two solid yellow
                        lines next to my car and continuing ahead.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line. Photo 2 shows a white dashed line next to my car
                        with clear gaps and dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries: a center line on the left and a lane line on the right place my
                        car in the second lane from the left of the roadway, but the first lane of my
                        direction since the yellow lines separate opposite traffic. | roles: the double solid
                        yellow line fits the role of a center line, and the white dashed line fits the role of
                        a lane line. | markings: no markings in my lane to contradict boundaries. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: Crossing a double solid yellow center line is prohibited.
Step 5  Rule            right_boundary: Crossing a white dashed lane line is allowed for lane changes.
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow center line
Step 6  change_right    allowed (correct): allowed by the white dashed lane line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the right lane. Do not cross the double yellow
                        lines to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 3717, out 640, 11.04 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, with traffic moving straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: the
                        white dashed patterns fit the role of lane lines | markings: there are no markings in
                        my lane to conflict with | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): the left boundary is a white dashed lane line, which allows lane
                        changes
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line, which allows lane
                        changes
Step 6  go_straight     allowed (correct): no marking governs this action, and the lane does not end
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 630, 18.87 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my lane. Photo 2 shows this line is a
                        double solid yellow line next to my car, continuing as a double solid yellow line
                        further ahead.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my lane. Photo 2 shows a white
                        dashed line next to my car with clear gaps between dashes, continuing as a dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a center line on the left and a lane line on the right place my
                        car in the second lane from the left of the roadway, but the first lane of my
                        direction since the yellow line separates opposite traffic. | roles: the double solid
                        yellow line fits the role of a center line, and the white dashed line fits the role of
                        a lane line. | markings: no markings in my lane to check. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A white dashed line allows lane changes into the adjacent lane of the
                        same direction.
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow center line
Step 6  change_right    allowed (correct): allowed by the white dashed lane line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the right. Do not cross the double yellow
                        line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 3717, out 677, 12.06 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a signalized intersection.
                        (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to the car and continuing ahead. Photo 2
                        confirms a white dashed line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car and continuing ahead. Photo 2
                        confirms a white dashed line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the presence of lane lines on both sides | roles: the white dashed lines fit the
                        role of lane lines | markings: no markings were observed in the lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (WRONG, label not_determined): the left boundary is a white dashed line which
                        allows lane changes
Step 6  change_right    allowed (WRONG, label not_determined): the right boundary is a white dashed line which
                        allows lane changes
Step 6  go_straight     allowed (contested, label not_determined): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a general-purpose lane. You may go straight or change lanes to the left or
                        right. Follow the traffic signals at the intersection.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 589, 18.28 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead on a clear
                        stretch of road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows two yellow lines side by side, one solid and one broken. Photo 2
                        confirms these are a solid yellow line and a broken yellow line side by side, with the
                        broken line closer to my lane.
                        yellow solid_dashed (near line dashed), curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line. Photo 2 shows a white broken line with long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries: a center line on the left and a lane line on the right place my
                        car in the second lane from the left of the three lanes in my direction. | roles: the
                        yellow solid-dashed center line and white dashed lane line fit their roles. |
                        markings: there are no markings in my lane to contradict. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid-dashed center line allows crossing the broken line for
                        overtaking or turning left, but prohibits crossing the solid line.
Step 5  Rule            right_boundary: A white dashed lane line allows lane changes to the right.
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a solid-
                        dashed center line with the dashed line nearest my lane.
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed lane line.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 672, 12.72 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. A bus stop
                        is visible on the left side of the road. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line separating my lane from the lane to the left. Photo
                        2 shows the same yellow broken line next to my car, consisting of long dashes and
                        gaps.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line on the right. Photo 2 shows a yellow solid line next
                        to my car, which continues as a solid line further ahead.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows a large yellow character '慢' (meaning 'slow') painted
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a lane line on the left and an edge line on the right
                        indicate I am in the rightmost lane of a two-lane road. | roles: the yellow dashed
                        line on the left is a lane line, and the yellow solid line on the right is an edge
                        line, which is consistent with the road layout. | markings: the 'slow' marking is a
                        warning and does not contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A yellow dashed line allows lane changes across it.
Step 5  Rule            right_boundary: A yellow solid line prohibits crossing it to leave the roadway.
Step 5  Rule            text:other: The 'slow' marking advises the driver to reduce speed but does not
                        prohibit any specific movement.
Step 6  change_left     allowed (contested, label prohibited): allowed by the yellow dashed left boundary
Step 6  change_right    prohibited (contested, correct): prohibited by the yellow solid right boundary
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but do
                        not cross the solid yellow line on the right. Please follow the 'slow' marking and
                        reduce your speed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 768, 13.72 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a green-colored surface, heading straight.
                        There are no intersections or ramps immediately ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, followed by a concrete barrier. Photo 2
                        shows the same solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a concrete barrier. Photo 2
                        shows the same solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the car is in a single lane bounded by edge lines on both sides |
                        roles: the white solid lines as edge lines fit the presence of concrete barriers |
                        markings: no markings in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing to the right.
Step 6  change_left     prohibited (contested, correct): the left_boundary is a solid white edge line which
                        prohibits crossing
Step 6  change_right    prohibited (contested, correct): the right_boundary is a solid white edge line which
                        prohibits crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes are prohibited due to the solid
                        edge lines and barriers.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 602, 10.32 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, which then becomes a solid white
                        line further ahead. Photo 2 shows the white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows it as well.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right. | roles: the white
                        dashed lines correctly serve as lane lines. | markings: the straight-ahead arrow is
                        consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight but prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (contested, label prohibited): allowed by the white dashed left boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow in my lane
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow in my lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. If you need to turn left or right,
                        you must change lanes.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 697, 12.22 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        overhead signs and traffic lights. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right. | roles: the white
                        dashed lines on both sides are consistent with lane lines separating lanes of the same
                        direction. | markings: the straight-ahead arrow is consistent with the lane
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (correct): the left boundary is a white dashed lane line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): the right boundary is a white dashed lane line, which allows lane
                        changes.
Step 6  go_straight     allowed (correct): the straight-ahead arrow in my lane allows this movement.
Step 6  turn_left       prohibited (correct): the straight-ahead arrow in my lane prohibits turning left.
Step 6  turn_right      prohibited (correct): the straight-ahead arrow in my lane prohibits turning right.
Step 6  u_turn          prohibited (correct): the straight-ahead arrow in my lane prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left or
                        right if needed, but you must not turn at the intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 729, 12.28 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: white
                        dashed lines are consistent with lane_line roles | markings: no markings were observed
                        in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (WRONG, label prohibited): the left_boundary is a white dashed line, which
                        allows lane changes
Step 6  change_right    allowed (WRONG, label prohibited): the right_boundary is a white dashed line, which
                        allows lane changes
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and the lane does not
                        end
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may go straight or change lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3717, out 621, 11.16 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line separating my lane from the lane to the right. Photo
                        2 shows a continuous yellow solid line next to my car.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; there is a lane to the left and a lane to the right. | roles: the
                        white dashed line is a standard lane line, and the yellow solid line is a lane line
                        (often used in China to separate lanes with different uses or to prohibit changes in
                        certain zones). | markings: no markings present in my lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A yellow solid line prohibits lane changes to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the yellow solid right
                        boundary
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  u_turn          not_applicable: not_applicable as there are no arrows
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left, but you are prohibited from
                        changing lanes to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 633, 11.93 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a crosswalk and an
                        intersection. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, which is the edge of the roadway. Photo
                        2 confirms a solid white line next to the car and a raised curb further left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a zebra-style crosswalk across the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the left edge_line and right lane_line | roles: the white solid left boundary is
                        an edge_line and the white dashed right boundary is a lane_line, which is consistent |
                        markings: the crosswalk is a standard marking across all lanes | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or curb
                        area.
Step 5  Rule            right_boundary: A broken white lane line allows lane changes into the adjacent lane.
Step 5  Rule            line:crosswalk: A crosswalk indicates a pedestrian crossing area; vehicles must yield
                        to pedestrians.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        curb
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the broken white lane line
Step 6  go_straight     allowed (contested, correct): allowed as there are no arrows prohibiting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight or change to the right lane, but do
                        not cross the left boundary. Be prepared to yield to pedestrians at the crosswalk.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 727, 12.48 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: the
                        white dashed pattern fits the role of a lane_line for both boundaries | markings:
                        there are no markings in my lane to check | unseen: no | result: consistent
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
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 617, 11.53 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards a distant intersection
                        with overhead lane guidance signs. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a raised curb. Photo 2
                        confirms a white solid line and a raised concrete curb immediately to the right of my
                        lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows white Chinese characters painted in the lane; Photo 1
                        shows they are part of a longer sequence. The characters are '公交专用道' (Bus Only Lane).
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 3
                        agree with a lane_line on the left and an edge_line on the right. | roles: the white
                        dashed line fits a lane_line role and the white solid line with a curb fits an
                        edge_line role. | markings: the 'BUS ONLY' text is consistent with the lane being a
                        special lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes between lanes of the same
                        direction.
Step 5  Rule            right_boundary: A white solid edge line and curb prohibit leaving the roadway to the
                        right.
Step 5  Rule            text:bus: This lane is reserved for buses; ordinary cars are prohibited from driving
                        in it.
Step 6  change_left     allowed (contested, correct): allowed by the white dashed left_boundary.
Step 6  change_right    prohibited (correct): prohibited by the white solid right_boundary and curb.
Step 6  go_straight     prohibited (contested, label allowed): prohibited because the lane is marked as a bus-
                        only lane (text:bus).
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are currently in a bus-only lane. You must change left into a general-purpose lane
                        immediately.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed ['text:other']), actions True, unsafe [], citation None,
                        contradictions ['go_straight decided without an arrow or prohibited-movement marking']
Tokens                  in 3717, out 762, 12.34 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test A | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane.
                        Photo 1 shows the same arrow.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right. | roles: the white
                        dashed lines on both sides are consistent with lane lines separating lanes of the same
                        direction. | markings: the straight-ahead arrow is consistent with the lane boundaries
                        and the general flow of traffic. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A white dashed line allows lane changes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a white dashed line, which
                        allows changing left.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a white dashed line, which
                        allows changing right.
Step 6  go_straight     allowed (correct): The straight-ahead arrow in my lane allows going straight.
Step 6  turn_left       prohibited (correct): The straight-ahead arrow in my lane prohibits turning left.
Step 6  turn_right      prohibited (correct): The straight-ahead arrow in my lane prohibits turning right.
Step 6  u_turn          prohibited (correct): The straight-ahead arrow in my lane prohibits making a U-turn.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight. You may change lanes to the left or
                        right if needed, but you cannot turn at the upcoming intersection from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 3717, out 739, 15.63 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, approaching an intersection with a white arrow in
                        the lane. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a raised curb. Photo 2 confirms a solid white
                        line and a raised curb immediately to the left of the lane.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line. Photo 2 shows a solid white line next to the car,
                        which continues as a solid line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the lane; Photo 1
                        shows it as well.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and index 1 agree
                        with the edge lines on both sides | roles: the solid white lines on both sides fit the
                        role of edge lines for a single-lane road or a dedicated lane | markings: the straight
                        arrow is consistent with the boundaries of a single lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line and curb prohibit leaving the lane to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits leaving the lane to the right.
Step 5  Rule            arrow:straight: The straight arrow allows going straight and prohibits turning left,
                        turning right, or making a U-turn.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and curb
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line
Step 6  go_straight     allowed (correct): allowed by the straight arrow
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight ahead; lane changes and turns are prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 679, 12.92 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a city street with buildings on both sides. The road ahead is straight with no
                        immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line extending from the bottom towards the distance.
                        Photo 2 confirms a solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car that continues ahead. Photo 2 shows a
                        white dashed line with clear gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge line on the right | roles: the yellow solid
                        line fits the role of a center line; the white dashed line fits the role of an edge
                        line | markings: no markings in my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A white dashed edge line allows crossing into the shoulder or parking
                        area if safe.
Step 6  change_left     prohibited (correct): the left_boundary is a solid yellow center line which prohibits
                        crossing
Step 6  change_right    allowed (correct): the right_boundary is a dashed white edge line which allows
                        crossing
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 606, 11.52 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards a distant
                        intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line and a raised curb on the right. Photo 2 confirms a
                        white solid line immediately next to a raised concrete curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white straight-ahead arrow further ahead in my
                        lane. Photo 2 shows the arrow more clearly.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right | roles: the white
                        dashed line fits a lane_line and the white solid line with a curb fits an edge_line |
                        markings: the straight arrow is consistent with the lane boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A white solid line and curb prohibit leaving the roadway to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed lane line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the white solid edge line and
                        curb
Step 6  go_straight     allowed (contested, correct): allowed by the straight-ahead arrow
Step 6  turn_left       prohibited: prohibited by the straight-ahead arrow
Step 6  turn_right      prohibited: prohibited by the straight-ahead arrow
Step 6  u_turn          prohibited: prohibited by the straight-ahead arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn, change to the left lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line']), actions False, unsafe ['change_left'],
                        citation None, contradictions []
Tokens                  in 3717, out 702, 11.35 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a crosswalk and an
                        intersection. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to my car that ends at a crosswalk, with a
                        raised curb and a sidewalk to the right. Photo 2 confirms the white solid line and the
                        raised curb immediately to the right of the lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane.
                        Photo 1 shows the arrow further ahead.; line:crosswalk (full): Photo 1 and Photo 2
                        show a white zebra-stripe crosswalk across my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        the 3rd lane agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line on the left fits the role of a lane line, and the white
                        solid line with a curb on the right fits the role of an edge line | markings: the
                        straight-ahead arrow is consistent with the lane's position and boundaries | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and curb prohibit leaving the roadway to the
                        right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 5  Rule            line:crosswalk: A crosswalk is a pedestrian crossing area and does not govern vehicle
                        movement actions other than yielding to pedestrians.
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the white dashed lane line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the white solid edge line and
                        raised curb
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but do
                        not cross the right boundary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 3717, out 828, 13.61 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in China. The road ahead is straight with no immediate
                        intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the opposite direction.
                        Photo 2 confirms a solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 confirms a solid white line
                        next to my car, and there is a raised curb further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left and an edge line on the right
                        indicate I am in the rightmost lane of a two-way road. | roles: the yellow solid
                        center line and white solid edge line fit their respective roles. | markings: there
                        are no markings in my lane to conflict with boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing the edge of the roadway
                        onto the curb or shoulder.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and the raised curb
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and the
                        lane does not end
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          prohibited: prohibited by the solid yellow center line
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 3717, out 646, 7.72 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a narrow urban road or bridge, flanked by barriers on both sides,
                        heading straight. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a concrete barrier on the left. Photo 2 confirms a continuous concrete
                        wall/barrier immediately next to the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a concrete barrier and railing on the right. Photo 2 shows a concrete
                        wall/curb immediately next to the car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the concrete barriers on both sides | roles: the concrete barriers correctly
                        serve as edge lines for a single-lane road | markings: no markings present, consistent
                        with a simple single-lane stretch | unseen: no | result: consistent
Step 5  Rule            left_boundary: A concrete barrier prohibits leaving the lane to the left.
Step 5  Rule            right_boundary: A concrete barrier prohibits leaving the lane to the right.
Step 6  change_left     prohibited (correct): prohibited by the left concrete barrier
Step 6  change_right    prohibited (correct): prohibited by the right concrete barrier
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and it
                        is the only available path
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersections in view
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersections in view
Step 6  u_turn          prohibited: prohibited by the narrow road and concrete barriers on both sides
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight; lane changes are impossible due to the
                        barriers.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 3717, out 607, 11.29 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test A | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line next to my car, with clear gaps between the dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from a red-colored bicycle lane.
                        Photo 2 shows the same white solid line next to my car, and a red painted area with a
                        bicycle symbol further right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane_line on the left and an edge_line on the right | roles: the white
                        dashed line fits the role of a lane_line and the white solid line fits the role of an
                        edge_line for a bicycle lane | markings: no markings in my lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the bicycle lane.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane, but do not enter the bicycle
                        lane on your right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3717, out 649, 10.54 s
```
