# Reasoning of lane run 20261118_000010_laneB_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues straight
                        ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line near the car, and further ahead, it appears to be a
                        solid yellow line. Photo 2 shows a solid yellow line near the car, and further ahead,
                        it appears to be a solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line near the car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line near the car, and further ahead, it
                        appears to be a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a dashed white line segment near the car, and
                        further ahead, it appears to be a dashed white line segment.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles: the left boundary is a center_line (separating
                        traffic flows in opposite directions), and the right boundary is an edge_line (marking
                        the right-hand edge of the direction of travel). | roles: The left boundary is yellow
                        and solid, fitting the role of a center_line separating opposing traffic. The right
                        boundary is white and solid, fitting the role of an edge_line. | markings: The stop
                        line marking is present in Photo 2 and appears consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing, but since this is a single solid yellow line, it prohibits vehicles in the
                        opposite direction from crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        yellow center_line, and [CN-6.1.1] prohibits crossing.
Step 6  change_right    allowed (contested, label prohibited): allowed, because the right boundary is a solid
                        white edge_line, and no rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in the lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in the lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in the lane, and no right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in the lane, and no U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because no left-turn waiting area or two-way left-
                          turn lane is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may proceed straight or change right, but changing
                        left is prohibited by the solid yellow center line. You must stop at the visible stop
                        line before proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 1154, 7.17 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with trees lining both sides, and a road ahead that appears
                        to continue straight, possibly leading to an intersection further down. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, and a broken white line further
                        ahead. Photo 2 shows a broken white line next to my car, and a broken white line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and a solid yellow line further
                        ahead. Photo 2 shows a solid yellow line next to my car, and a solid yellow line
                        further ahead.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The no-crossing centre line has three forms: double solid yellow,
                        broken-solid yellow and single solid yellow. It separates opposing traffic flows and
                        prohibits vehicles in both directions, or in one direction, from crossing.
                        [[CN-6.1.1]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white lane_line, and
                        [CN-5.2.3] permits lane changes on sections where crossable lane lines are used.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid yellow
                        edge_line, and [CN-6.1.1] implies prohibition of crossing a solid yellow line,
                        although this is an edge line, the solid nature restricts movement.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to proceed straight. You may change left
                        into the leftmost lane, but changing right is prohibited by the solid yellow line. No
                        specific stopping or turning instructions are visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 918, 6.57 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues straight
                        ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible further ahead. Photo 2: A white dashed line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible across the lane
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line). | roles: the color and pattern of both boundaries fit the role of a
                        lane_line (white dashed lines separating lanes in the same direction). | markings: the
                        stop line marking is consistent with the lane markings observed. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may change left or right as the lane lines are
                        broken. You may proceed straight ahead, but you must stop before the solid white stop
                        line visible ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 861, 7.29 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an elevated structure (likely a highway or overpass)
                        running parallel to the road ahead. The road continues into the distance, and there
                        are no immediate intersections or lane endings visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: The color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: The stop
                        line is present in my lane and is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a dashed white
                        lane_line, and [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibitions in
                        my lane, and the boundaries do not restrict going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted as the lane lines are
                        dashed. You may proceed straight, but you must stop before the visible stop line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 1122, 8.44 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an elevated structure (likely a bridge or overpass)
                        ahead. My car is in one of the lanes traveling forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white solid line near my car, and a white solid line further ahead.
                        Photo 2 shows a white solid line near my car, and a white solid line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line near my car, and a white solid line further ahead.
                        Photo 2 shows a white solid line near my car, and a white solid line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: The color (white) and
                        pattern (solid) of both boundaries fit the role of a lane_line. | markings: The lane
                        markings list is empty, which is consistent with the boundaries being the only
                        features. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited due to the left_boundary being a solid white
                        lane_line, which prohibits crossing.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the right_boundary being a solid
                        white lane_line, which prohibits crossing.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane that
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as both boundaries are solid white lane lines
                        prohibiting lane changes. You are permitted to proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 957, 6.91 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues straight, and there is no immediate intersection or ramp visible in the
                        close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes
                        within the same direction of travel). | roles: the white dashed lines fit the role of
                        lane_line. | markings: no markings were observed in the lane. | unseen: no attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict carrying on straight along
                        my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by the observed markings or lack thereof.
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right, and you may proceed straight ahead. No specific turn or
                        waiting area markings are present.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 850, 6.19 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a point
                        where lane configuration changes, as indicated by the markings. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a dashed white line next to my car, and Photo 2 shows a dashed white
                        line next to my car. Photo 1 shows a solid white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and Photo 2 shows a solid yellow
                        line next to my car. Photo 1 shows a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles: the left boundary is a lane_line (separating from
                        lane 1), and the right boundary is a center_line (separating from lane 3). | roles:
                        The left boundary is a white dashed lane_line, and the right boundary is a yellow
                        solid center_line, which fits the roles. | markings: The white arrow in my lane shows
                        a permitted movement, and this is consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: A no-crossing centre line has three forms: double solid yellow,
                        broken-solid yellow and single solid yellow, and it prohibits vehicles in both
                        directions, or in one direction, from crossing. [[CN-6.1.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a dashed
                        white lane_line, and while it is crossable, the arrow in my lane only permits straight
                        or right movement.
Step 6  change_right    allowed (contested, label prohibited): allowed, because the right boundary is a solid
                        yellow center_line, and the arrow in my lane permits movement to the right.
Step 6  go_straight     allowed (contested, correct): allowed, because the white arrow in my lane indicates
                        straight ahead movement.
Step 6  turn_left       prohibited: prohibited, because the white arrow in my lane does not show a left turn.
Step 6  turn_right      allowed: allowed, because the white arrow in my lane indicates a right turn.
Step 6  u_turn          prohibited: prohibited, because the white arrow in my lane does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings for a waiting area or
                          two-way left-turn lane in view.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight or turning right. You may
                        change right if necessary, but changing left is prohibited by the lane markings.
                        Proceed according to the arrow's indication.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['change_left prohibited across a broken lane
                        line']
Tokens                  in 8454, out 1081, 7.83 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road under an overpass, and the road continues straight ahead
                        into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing into the distance. Photo 2: A white
                        dashed line is visible next to my car. Further ahead, the line appears to be a white
                        dashed line continuing into the distance.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing into the distance. Photo 2: A white
                        dashed line is visible next to my car. Further ahead, the line appears to be a white
                        dashed line continuing into the distance.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: there are
                        no arrows, words, or areas painted in my lane, so they agree with each other and with
                        the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane_line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane restricting
                        straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn or prohibited U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. No
                        specific lane is required for any movement, and no stopping is required.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 857, 6.97 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane elevated highway or bridge. Ahead, the road continues straight,
                        leading towards a distant cityscape. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A yellow dashed line is visible to the left of my car, further ahead it
                        appears to be a yellow dashed line. Photo 2: A yellow dashed line is visible to the
                        left of my car, and further ahead it is also a yellow dashed line.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible to the right of my car, further ahead it
                        appears to be a white dashed line. Photo 2: A white dashed line is visible to the
                        right of my car, and further ahead it is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible across the lane
                        ahead of my car, indicating lane division.; line:stop_line (partial): Photo 2: A white
                        dashed line is visible across the lane ahead of my car, indicating lane division.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow dashed for center_line, white dashed for lane_line) | markings: the markings
                        (white dashed lines) are consistent with the boundaries (white dashed lane_line) |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Yellow longitudinal markings separate traffic flows in opposite
                        directions and mark the left-hand edge of the direction of travel and tidal lanes.
                        [[CN-4.3.2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed, and it is a solid white line. [[CN-6.4.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a yellow dashed
                        center_line, and [CN-4.3.2] permits crossing when safe.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and
                        [CN-5.2.1-2] permits crossing when safe.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight. You may change lanes left
                        or right as long as it is safe, as the lane markings are broken. No specific stopping
                        or turning maneuvers are indicated for your current lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 992, 7.24 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where the road continues and potentially turns. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to my car. Further ahead, this line
                        appears to continue as a solid white line. Photo 2: A solid white line is visible next
                        to my car. Further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A broken yellow line is visible next to my car. Further ahead, this line
                        appears to continue as a broken yellow line. Photo 2: A broken yellow line is visible
                        next to my car. Further ahead, this line continues as a broken yellow line.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2: A white arrow pointing straight ahead is visible
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left. The left boundary is a lane_line (white solid) and the right
                        boundary is a center_line (yellow dashed), which is consistent with my lane being the
                        middle lane. | roles: The left boundary (white solid) fits the role of a lane_line
                        separating traffic in the same direction. The right boundary (yellow dashed) fits the
                        role of a center_line separating traffic in opposite directions. | markings: The white
                        arrow in my lane indicates the allowed direction of travel, which is consistent with
                        the lane boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the lane line.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The crossable centre line means vehicles may cross the line to
                        overtake, turn or make a U-turn when this does not affect safety. [[CN-5.1.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        lane_line, and [CN-6.2.1] prohibits crossing from the solid side.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a broken yellow
                        center_line, and [CN-5.1.1] permits crossing when it does not affect safety.
Step 6  go_straight     allowed (contested, correct): allowed: The guide arrow in my lane shows straight
                        ahead, and [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       prohibited: prohibited: The guide arrow in my lane does not show a left turn, and
                        [CN-5.13.1] restricts movement to what is shown.
Step 6  turn_right      allowed: allowed: The guide arrow in my lane shows straight or right, and [CN-5.13.1]
                        indicates the direction of travel.
Step 6  u_turn          prohibited: prohibited: The guide arrow in my lane does not show a U-turn, and
                        [CN-5.13.1] restricts movement to what is shown.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight or turn right, and you may
                        change lanes to the right. You should not attempt to change left, turn left, or make a
                        U-turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 1185, 9.2 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a change
                        in road configuration where lanes converge or diverge. My car is in one of the lanes
                        near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, this line
                        appears to continue as a white dashed line. Photo 2: A white dashed line is visible
                        next to my car. Further ahead, this line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, this line
                        appears to continue as a white dashed line. Photo 2: A white dashed line is visible
                        next to my car. Further ahead, this line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible across the lane
                        ahead of my car, indicating a lane division or change area.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lane
                        separation). | roles: the color (white) and pattern (dashed) of both boundaries fit
                        the role of a lane_line. | markings: the white dashed line across the lane ahead is
                        consistent with a lane division/stop line indication. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [CN-5.2.3]
                        permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there is
                        a line ahead, you should prepare to stop or yield if necessary.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 8454, out 933, 6.87 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road. Ahead, there is an
                        overpass/intersection structure visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car. Further
                        ahead, this line appears to continue as a solid white line. Photo 2: A solid white
                        line is visible immediately to the left of my car. Further ahead, this line continues
                        as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible immediately to the right of my car. Further
                        ahead, this line continues as a solid yellow line. Photo 2: A solid yellow line is
                        visible immediately to the right of my car. Further ahead, this line continues as a
                        solid yellow line.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2: A solid yellow line is painted on the road surface
                        in my lane, indicating a lane boundary or restriction.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane_line (white, separating
                        lanes in the same direction), and the right boundary is an edge_line (yellow, marking
                        the edge of the roadway). | roles: The white solid line on the left fits the role of a
                        lane_line, and the yellow solid line on the right fits the role of an edge_line. |
                        markings: The solid yellow line observed in Photo 2 is interpreted as a stop-and-yield
                        line based on its appearance and context, which is consistent with the boundaries and
                        general road markings. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, but since this is yellow, it functions as a separation line for opposing
                        traffic or a general edge line in this context, and the solid yellow line prohibits
                        crossing into the adjacent lane. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: Vehicles shall stop completely before entering the intersection and
                        may proceed only after making sure it is safe. [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white
                        lane_line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid yellow
                        edge_line, and [CN-6.1] implies that a solid line prohibits crossing.
Step 6  go_straight     stop_first (contested, label allowed): stop_first: The marking line:stop_yield is
                        present in my lane, and [CN-6.5.1.1-2] mandates that vehicles shall stop completely
                        before entering the intersection.
Step 6  turn_left       stop_first: stop_first: The marking line:stop_yield is present in my lane, and
                        [CN-6.5.1.1-2] mandates that vehicles shall stop completely before entering the
                        intersection.
Step 6  turn_right      stop_first: stop_first: The marking line:stop_yield is present in my lane, and
                        [CN-6.5.1.1-2] mandates that vehicles shall stop completely before entering the
                        intersection.
Step 6  u_turn          stop_first: stop_first: The marking line:stop_yield is present in my lane, and
                        [CN-6.5.1.1-2] mandates that vehicles shall stop completely before entering the
                        intersection.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and all
                        actions are governed by the stop-and-yield line, which prohibits movement until a stop
                        is made.
Advice                  You must come to a complete stop before proceeding into the intersection, as indicated
                        by the stop-and-yield line. Lane changes are prohibited due to the solid lane line on
                        your left and the solid edge line on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 8454, out 1164, 9.66 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with a pedestrian overpass ahead. My car is in one of the
                        lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A yellow line is visible on the left side of my lane, further ahead. Photo 2:
                        A yellow line is visible on the left side of my lane, further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1: A white line is visible on the right side of my lane, further ahead. Photo 2:
                        A white line is visible on the right side of my lane, further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible in my lane, further
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow dashed for center_line, white dashed for lane_line) | markings: the markings
                        (line:stop_line) agree with the boundaries (no contradiction found) | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid side may not cross, but vehicles on the broken
                        side may cross, and a vehicle crossing the line must give way to vehicles travelling
                        normally. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a yellow dashed
                        center_line, and while a broken line may be crossed, the general context suggests
                        staying in the lane unless necessary for a turn.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a broken white
                        lane_line, and a broken line means it may be crossed.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or markings in my lane indicating
                        a permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or markings in my lane indicating
                        a permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or markings in my lane indicating
                        a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You may change right if necessary, and you may proceed straight ahead. You must stop
                        before the visible white dashed line if you intend to stop for any reason.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 899, 7.14 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic flowing in the same direction as my car.
                        Ahead, there is a junction or intersection where traffic flow is directed by signs.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the white
                        dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to my car. Further ahead, the solid
                        yellow line continues.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1: A white arrow pointing straight ahead is visible in my
                        lane.; arrow:right (full): Photo 1: A white arrow pointing right is visible in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The left boundary is a lane line
                        separating my lane from another lane of my direction (lane_line). The right boundary
                        is an edge line separating my lane from the roadside/parking area (edge_line). Since
                        there are two lanes, and my lane is the leftmost one (index 1), the left boundary
                        should be a center line or a lane line separating me from the lane to my left. Given
                        the context of two lanes, the left boundary is a lane line separating me from the lane
                        to my left, which is consistent with my lane being the leftmost lane if the lane to
                        the left is the other lane. The right boundary is an edge line. | roles: The left
                        boundary is a white dashed lane_line, which is consistent with separating lanes in the
                        same direction. The right boundary is a solid yellow edge_line, which is consistent
                        with marking the edge of the roadway. | markings: The arrows (straight and right) are
                        present in my lane and are consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and the
                        arrow pointing straight ahead indicates that straight ahead is a permitted direction
                        of travel. [[CN-5.13.1]]
Step 5  Rule            arrow:right: Guide arrows indicate the direction of travel for vehicles, and the arrow
                        pointing right indicates that turning right is a permitted direction of travel.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane_line, and
                        while broken lines may be crossed, the presence of a lane line suggests a defined lane
                        structure.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid yellow
                        edge_line, and the rule for edge lines does not prohibit lane changes into the
                        adjacent area, although the solid nature suggests caution.
Step 6  go_straight     allowed (contested, correct): allowed: The lane contains a white arrow pointing
                        straight ahead, and the rule for guide arrows permits the indicated movement.
Step 6  turn_left       prohibited: prohibited: There is no arrow or marking in the lane permitting a left
                        turn.
Step 6  turn_right      allowed: allowed: The lane contains a white arrow pointing right, and the rule for
                        guide arrows permits the indicated movement.
Step 6  u_turn          prohibited: prohibited: There is no arrow or marking in the lane permitting a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which allows you to go straight or turn right. You may
                        change right, but you must proceed with caution as the right boundary is a solid
                        yellow edge line. Do not attempt to turn left or make a U-turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:right', 'arrow:straight'], missed []), actions False, unsafe ['change_right'],
                        citation in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the
                        left', 'change_left prohibited across a broken lane line']
Tokens                  in 8454, out 1327, 9.23 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road. Ahead, there is a continuation of the
                        road structure, possibly leading to an interchange or another section of the highway.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it is also a
                        white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it is also a
                        white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white dashed line marking the lane
                        boundary on the left, and a white dashed line marking the lane boundary on the right.
                        Photo 2 shows the same white dashed lines.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: The color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: The lane
                        markings observed (dashed lines) are consistent with the boundary roles. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed white lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a dashed
                        white lane_line, and [CN-5.2.3] permits lane changes where crossable lane lines are
                        used.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane governing this action.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane governing this action.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and since both lane boundaries are dashed, you are
                        permitted to change lanes left or right if necessary. All movements, including going
                        straight, are allowed based on the visible markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 1126, 8.3 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, the
                        road continues straight, and there are traffic signals visible in the distance. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1: A broken white line is visible next to the car. Further ahead, the broken
                        white line continues. Photo 2: A broken white line is visible next to the car. Further
                        ahead, the broken white line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            left_boundary: On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes. [[CN-5.2.3]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white line, which allows
                        crossing according to [CN-5.2.1-2] and [CN-5.2.3].
Step 6  change_right    prohibited (correct): allowed: The right boundary is a solid white line, which
                        prohibits crossing according to [CN-4.2.2-a] (as a solid line, though this is an edge
                        line, the solid nature suggests restriction, but since it's an edge line, the primary
                        restriction is usually related to the edge itself, and the solid nature here implies a
                        firm boundary).
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern U-turns or
                        turning.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to proceed straight. You may change left
                        into the leftmost lane, but changing right into the rightmost lane is prohibited by
                        the solid white edge line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 919, 7.53 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, the road
                        continues straight, and there is a median/shoulder area to the right. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A broken white line is visible next to the car. Photo 2: A broken white line
                        is visible next to the car. Further ahead, the broken white line continues. Further
                        ahead, the broken white line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, the solid white line continues. Further ahead,
                        the solid white line continues.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2: A large white arrow pointing straight ahead is
                        visible in the lane. Photo 1: The arrow continues into the distance.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles: the left boundary is a lane_line separating it from
                        lane 1, and the right boundary is an edge_line. | roles: The white dashed line on the
                        left fits the role of a lane_line, and the white solid line on the right fits the role
                        of an edge_line. | markings: The arrow in the lane shows a direction of travel, which
                        is consistent with the lane boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a lane_line, and while it is
                        broken (crossable), the arrow in the lane does not permit a left change.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is an edge_line, and
                        the arrow in the lane permits movement in this direction.
Step 6  go_straight     allowed (correct): allowed: The arrow in the lane permits straight ahead movement, and
                        the boundaries do not prohibit it.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in the lane does not show a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in the lane shows straight or
                        right, permitting a right turn.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in the lane does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of the lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by the observed markings and rules.
Advice                  You are in the middle lane, which is marked to proceed straight or turn right. You may
                        change right if necessary, but you must not change left. Proceed straight or turn
                        right at the next intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight', 'line:stop_line']), actions False,
                        unsafe ['change_right', 'turn_right'], citation accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 8454, out 969, 7.34 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides. Ahead, the road
                        continues into what appears to be a wide intersection or a section with multiple
                        lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line remains a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2: White arrows pointing straight ahead are visible
                        in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line separating traffic flows in the same direction. | markings: The
                        white arrows in the lane agree with the boundaries, as they indicate movement within
                        the lane structure. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane_line, and
                        while this allows lane changes, the arrow in the lane does not permit a left change.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed
                        lane_line, and the arrow in the lane permits a right change.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking (arrow:straight_right) permits
                        going straight ahead.
Step 6  turn_left       prohibited: prohibited: The lane marking (arrow:straight_right) does not show a left
                        turn.
Step 6  turn_right      allowed: allowed: The lane marking (arrow:straight_right) permits turning right.
Step 6  u_turn          prohibited: prohibited: The lane marking (arrow:straight_right) does not show a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of the lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and all
                        actions are governed by the observed markings and rules.
Advice                  You are in the middle lane, which is marked to allow straight and right turns. You may
                        change right if necessary, but you cannot change left. You should proceed straight or
                        turn right at the next intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions ['change_left prohibited across a broken lane
                        line']
Tokens                  in 8454, out 926, 7.37 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely a highway or major arterial road, and there is a set
                        of traffic lights and buildings ahead, suggesting an intersection or a major junction
                        is approaching. My car is in the lane closest to the center of the visible lanes.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing, and
                        Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:straight_right (full): Photo 2 shows a white arrow pointing straight
                        ahead in the lane to my left.; arrow:straight_right (full): Photo 2 shows a white
                        arrow pointing straight ahead in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: the arrows in my lane
                        (arrow:straight_right) agree with the boundaries (dashed lines allow lane changes, but
                        the arrow restricts movement to straight ahead). | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow in my lane indicates straight ahead or straight right. [[CN-5.13.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow in the lane to my left indicates straight ahead or straight right.
                        [[CN-5.13.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow in the lane to my right indicates straight ahead or straight right.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The white dashed line on the left
                        boundary allows lane changes, but the arrow in my lane (arrow:straight_right)
                        restricts movement to straight ahead or straight right, which does not explicitly
                        permit a left change.
Step 6  change_right    allowed (correct): allowed: The white dashed line on the right boundary allows lane
                        changes, and the arrow in my lane (arrow:straight_right) permits straight ahead or
                        straight right, which includes a right change.
Step 6  go_straight     allowed (correct): allowed: The arrow in my lane (arrow:straight_right) permits
                        straight ahead, and the boundaries allow lane changes if needed.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in my lane (arrow:straight_right) does not
                        show a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in my lane
                        (arrow:straight_right) permits straight ahead or straight right.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane (arrow:straight_right) does not
                        show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are permitted to go straight or turn right, and you may change lanes to the right.
                        Lane changes to the left are prohibited by the lane markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight']), actions False, unsafe
                        ['turn_right'], citation accepted, contradictions ['change_left prohibited across a
                        broken lane line']
Tokens                  in 8454, out 1162, 8.05 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road with lane
                        markings indicating directions of travel. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car, and further ahead, it appears to be a white dashed line
                        continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Photo 2: A white dashed line
                        is visible next to my car, and further ahead, it appears to be a white dashed line
                        continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2: A white arrow pointing straight ahead is visible in my
                        lane.; arrow:right (full): Photo 2: A white arrow pointing right is visible in my
                        lane, further ahead.; arrow:left (full): Photo 2: A white arrow pointing left is
                        visible in the leftmost lane, further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: The color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: The
                        arrows (straight, right, left) are consistent with the lane structure and boundaries.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates straight ahead. [[CN-5.13.1]]
Step 5  Rule            arrow:right: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates right. [[CN-5.13.1]]
Step 5  Rule            arrow:left: Guide arrows indicate the direction of travel for vehicles, and this arrow
                        indicates left. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a dashed white
                        lane_line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed
                        white lane_line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  go_straight     allowed (correct): Allowed because the lane contains a guide arrow indicating straight
                        ahead, and [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       prohibited (correct): Prohibited because the guide arrow in my lane does not show a
                        left turn, and [CN-5.13.1] dictates the direction of travel.
Step 6  turn_right      allowed (WRONG, label prohibited): Allowed because the lane contains a guide arrow
                        indicating right, and [CN-5.13.1] indicates the direction of travel.
Step 6  u_turn          prohibited (correct): Prohibited because the guide arrow in my lane does not show a
                        U-turn, and [CN-5.13.1] dictates the direction of travel.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a waiting area in
                          my lane.
Step 7  Reflect         The boundaries and markings were settled in the close-up check, no action was allowed
                        against a rule, no action was decided without a governing feature, no action was
                        decided by a marking that does not govern it, and each reason leads to its action.
Advice                  You are in the middle lane, which allows you to go straight or turn right, and you may
                        change lanes left or right. You should use the middle lane for straight or right
                        turns, and the left lane for a left turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed ['line:stop_line']), actions False, unsafe
                        ['change_left', 'change_right', 'turn_right'], citation accepted, contradictions
                        ['turn_left prohibited although an arrow shows it']
Tokens                  in 8454, out 1368, 9.01 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where traffic appears to
                        be merging or changing lanes. My car is in one of the lanes near the bottom of the
                        photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line near my car, and Photo 2 shows a solid yellow line
                        near my car. Further ahead, Photo 1 shows a solid yellow line continuing, and Photo 2
                        shows a solid yellow line continuing.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line near my car, and Photo 2 shows a white dashed line
                        near my car. Further ahead, Photo 1 shows a white dashed line continuing, and Photo 2
                        shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow solid for center_line, white dashed for lane_line) | markings: the arrow in my
                        lane shows a movement (straight_right) that is consistent with the lane configuration
                        and boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid yellow center_line, and
                        [CN-6.1.1] prohibits crossing this line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, and [CN-5.2.1-2] permits crossing this line when changing lanes.
Step 6  go_straight     allowed (correct): allowed: The arrow in my lane shows straight ahead or right, and
                        [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in my lane does not show a left turn, and
                        [CN-5.13.1] dictates the direction of travel.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in my lane shows straight ahead
                        or right, and [CN-5.13.1] indicates the direction of travel.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane does not show a U-turn, and
                        [CN-5.13.1] dictates the direction of travel.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight or turn right. You may
                        change right into the adjacent lane if necessary, but changing left is prohibited by
                        the solid yellow line. Proceed according to the arrow indicating straight or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight']), actions False, unsafe
                        ['change_right', 'turn_right'], citation accepted, contradictions []
Tokens                  in 8454, out 970, 7.17 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a developed area, and ahead there is an intersection or a
                        merging area indicated by the road markings. My car is in one of the lanes near the
                        bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, the line appears
                        to continue as a white dashed line. Photo 2 shows a white dashed line next to my car,
                        and further ahead, the line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, the line appears
                        to continue as a white dashed line. Photo 2 shows a white dashed line next to my car,
                        and further ahead, the line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a large white arrow pointing up and to the
                        right in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: the arrow
                        in the lane is consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates straight or right movement. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a dashed white lane_line, which
                        permits lane changes, but the arrow in the lane only permits straight or right
                        movement.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, which permits lane changes, and the arrow in the lane permits straight or
                        right movement.
Step 6  go_straight     allowed (correct): allowed: The arrow in the lane permits straight movement, and the
                        boundaries do not prohibit going straight.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited: The arrow in the lane only permits
                        straight or right movement.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in the lane permits right
                        movement, and the boundaries do not prohibit turning right.
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited: The arrow in the lane only permits
                        straight or right movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is marked to go straight or turn right. You may
                        change right if necessary, but you must not change left. You should proceed straight
                        or turn right at the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight_left']), actions False, unsafe
                        ['change_right', 'turn_right'], citation accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 8454, out 919, 7.06 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where traffic appears to be slowing down or preparing to turn. My car is in one of the
                        lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line immediately to the left of my car, and further ahead,
                        this line continues as a solid white line. Photo 2 shows a solid white line
                        immediately to the left of my car, and further ahead, this line continues as a solid
                        white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line immediately to the right of my car, and further
                        ahead, this line continues as a broken white line. Photo 2 shows a broken white line
                        immediately to the right of my car, and further ahead, this line continues as a broken
                        white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the right boundary
                        of my lane, which is also the line further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white solid/dashed lines are consistent with lane_lines) | markings: the markings
                        (line:stop_line) agree with the boundaries (the stop line is located within the lane
                        defined by the boundaries) | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the lane line.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a broken white lane
                        line, and [CN-5.2.1-2] indicates it is a crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change right into the adjacent lane, and you may proceed straight ahead. You
                        must stop before the solid white line marked as the stop line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 949, 7.63 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road passing under an overpass. Ahead, the road continues under
                        the bridge structure. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible immediately to the left of my car. Further
                        ahead, this line appears to continue as a solid white line. Photo 2: A solid white
                        line is visible immediately to the left of my car. Further ahead, this line continues
                        as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A broken yellow line is visible immediately to the right of my car. Further
                        ahead, this line appears to continue as a broken yellow line. Photo 2: A broken yellow
                        line is visible immediately to the right of my car. Further ahead, this line continues
                        as a broken yellow line.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2: A large white arrow pointing straight ahead is
                        visible on the road surface in my lane.; arrow:right (full): Photo 2: A large white
                        arrow pointing to the right is visible on the road surface in my lane, to the right of
                        the straight arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (1) agree with the boundary roles: the left boundary is a lane_line (separating from
                        lane 2), and the right boundary is a center_line (separating from lane 3). | roles:
                        The left boundary is a solid white lane_line, and the right boundary is a dashed
                        yellow center_line, which fits their roles. | markings: The arrows (straight ahead and
                        right) are present in my lane and are consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the lane line.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing, but since this is a broken yellow line, it allows crossing under certain
                        conditions. [[CN-6.1.1]]
Step 5  Rule            arrow:straight_right: The guide arrow indicates that vehicles may travel straight
                        ahead. [[CN-5.13.1]]
Step 5  Rule            arrow:right: The guide arrow indicates that vehicles may turn right. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane_line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a broken yellow
                        center_line, and [CN-5.11.1] implies that a broken line may be crossed (though the
                        specific rule for this context is not explicitly stated, the broken nature suggests
                        permissiveness for lane changes).
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The lane marking includes an arrow
                        indicating straight ahead, and [CN-5.13.1] confirms this direction is allowed.
Step 6  turn_left       prohibited (correct): prohibited: There is no marking in my lane allowing a left turn,
                        and [CN-5.13.1] implies that if an arrow does not show a movement, it is prohibited.
Step 6  turn_right      allowed (correct): allowed: The lane marking includes an arrow indicating a right
                        turn, and [CN-5.13.1] confirms this direction is allowed.
Step 6  u_turn          prohibited (correct): prohibited: There is no marking in my lane allowing a U-turn,
                        and [CN-5.13.1] implies that if an arrow does not show a movement, it is prohibited.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         The decisions are consistent with the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You are permitted to go straight or turn right from your current lane. You may change
                        right into the adjacent lane, but changing left is prohibited by the solid white line.
                        Do not attempt to turn left or make a U-turn.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe ['change_right',
                        'go_straight'], citation accepted, contradictions ['leftmost lane, but a lane line on
                        the left']
Tokens                  in 8454, out 1156, 8.66 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection visible in the distance.
                        My car is in the rightmost lane visible near the bottom of the photo. (lanes 3, mine
                        3, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the intersection. Photo 2: A
                        white dashed line is visible next to my car. Further ahead, the line appears to be a
                        white dashed line continuing towards the intersection.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the intersection. Photo 2: A
                        white dashed line is visible next to my car. Further ahead, the line appears to be a
                        white dashed line continuing towards the intersection.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            left_boundary: A broken line means it may be crossed. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: The broken edge line has 60 cm segments and 30 cm gaps (also called a
                        "dense broken line"). [[CN-5.4.2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed
                        lane_line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed edge_line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  go_straight     allowed (correct): allowed: There are no markings in my lane to prohibit going
                        straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no markings in my
                        lane to govern turning left.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no markings in my
                        lane to govern turning right.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no markings in my
                        lane to govern U-turns or turning.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight through the
                        intersection. Since there are no specific markings for turns, you should proceed with
                        caution when turning.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 8454, out 928, 6.9 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where traffic appears to
                        be approaching a signalized crossing. My car is in one of the lanes near the bottom of
                        the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the intersection. Photo 2: A
                        white dashed line is visible next to my car. Further ahead, the line appears to be a
                        white dashed line continuing towards the intersection.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the intersection. Photo 2: A
                        white dashed line is visible next to my car. Further ahead, the line appears to be a
                        white dashed line continuing towards the intersection.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2: A white arrow pointing straight ahead is visible
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines separating lanes). | roles: The
                        white dashed lines fit the role of lane_line. | markings: The white arrow pointing
                        straight ahead is consistent with the lane markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane_line, which
                        permits lane changes, but the arrow in my lane only permits straight ahead or right.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed
                        lane_line, which permits lane changes, and the arrow in my lane permits straight ahead
                        or right.
Step 6  go_straight     allowed (correct): allowed: The arrow in my lane permits straight ahead, and the
                        boundaries do not prohibit going straight.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in my lane does not show a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in my lane permits straight
                        ahead or right.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by the visible markings and rules.
Advice                  You are in the middle lane, which allows you to go straight or turn right. You may
                        change right if necessary, but you must not change left. Proceed with caution towards
                        the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight', 'line:stop_line']), actions False,
                        unsafe ['change_right', 'turn_right'], citation accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 8454, out 936, 6.98 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        with traffic signals. My car is in the lane closest to the center of the road,
                        slightly to the right of the leftmost lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, and further ahead, it appears to be
                        a broken white line. Photo 2 shows a broken white line next to my car, and further
                        ahead, it appears to be a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and further ahead, it appears to be
                        a solid yellow line. Photo 2 shows a solid yellow line next to my car, and further
                        ahead, it appears to be a solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:straight_right (full): Photo 2 shows a white arrow pointing straight
                        ahead in the lane to the left of my lane.; arrow:straight_right (full): Photo 2 shows
                        a white arrow pointing straight ahead in the lane to the right of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed for lane_line, yellow solid for center_line). | markings: the arrows in
                        my lane (arrow:straight_right) agree with the boundaries (lane_line on left,
                        center_line on right). | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow in my lane indicates straight ahead or right. [[CN-5.13.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow in the lane to the left indicates straight ahead or right. [[CN-5.13.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow in the lane to the right indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a lane_line, and the arrow in
                        my lane only shows straight ahead or right, which does not permit a lane change to the
                        left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a center_line, and
                        the arrow in my lane shows straight ahead or right, which permits a lane change to the
                        right.
Step 6  go_straight     allowed (correct): allowed: The arrow in my lane shows straight ahead or right, and
                        nothing restricts carrying on straight along my lane.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in my lane only shows straight ahead or
                        right, which prohibits turning left.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in my lane shows straight ahead
                        or right, which permits turning right.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane only shows straight ahead or
                        right, which prohibits U-turns unless the arrow shows a turn toward the opposite
                        traffic, which it does not.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are permitted to go straight or turn right, and you may change lanes to the right.
                        Lane changes to the left are prohibited by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight', 'line:crosswalk',
                        'line:stop_line']), actions False, unsafe ['change_right', 'turn_right'], citation
                        accepted, contradictions ['change_left prohibited across a broken lane line']
Tokens                  in 8454, out 1139, 8.32 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in both directions. Ahead, there
                        is an intersection area marked with lane guidance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the line
                        appears to be a solid white line continuing into the intersection area. Photo 2: A
                        solid white line is visible next to the car. Further ahead, the line appears to be a
                        solid white line continuing into the intersection area.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Further ahead, the line
                        appears to be a solid yellow line continuing into the intersection area. Photo 2: A
                        solid yellow line is visible next to the car. Further ahead, the line appears to be a
                        solid yellow line continuing into the intersection area.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        no_turn:left (full): Photo 2: A large yellow 'X' marking is visible in the lane,
                        indicating a prohibition.; no_turn:right (full): Photo 2: A large yellow 'X' marking
                        is visible in the lane, indicating a prohibition.; no_turn:u_turn (full): Photo 2: A
                        large yellow 'X' marking is visible in the lane, indicating a prohibition.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left, which is consistent with having a lane line on the left and a
                        center line on the right. | roles: The left boundary is a solid white lane_line, and
                        the right boundary is a solid yellow center_line, which fits the roles. | markings:
                        The 'no_turn' markings are present in the lane and are consistent with the boundaries.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            no_turn:left: No U-turn and no turn markings are used at intersections or on sections
                        where U-turns or turns are prohibited. [[CN-6.11.1-2]]
Step 5  Rule            no_turn:right: No U-turn and no turn markings are used at intersections or on sections
                        where U-turns or turns are prohibited. [[CN-6.11.1-2]]
Step 5  Rule            no_turn:u_turn: No U-turn and no turn markings are used at intersections or on
                        sections where U-turns or turns are prohibited. [[CN-6.11.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane_line and
                        [CN-6.2.1] because the solid side may not cross the no-crossing lane line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow center_line and
                        [CN-6.1.1] because a single solid yellow line prohibits vehicles in both directions
                        from crossing.
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the no_turn:left, no_turn:right,
                        and no_turn:u_turn markings and [CN-6.11.1-2] because these markings prohibit turns,
                        which implies no straight movement is allowed if all turns are prohibited.
Step 6  turn_left       prohibited: prohibited by the no_turn:left marking and [CN-6.11.1-2] because this
                        marking prohibits turns.
Step 6  turn_right      prohibited: prohibited by the no_turn:right marking and [CN-6.11.1-2] because this
                        marking prohibits turns.
Step 6  u_turn          prohibited: prohibited by the no_turn:u_turn marking and [CN-6.11.1-2] because this
                        marking prohibits U-turns and turns.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane as lane changes are prohibited by solid lines.
                        All movements, including going straight, turning left, turning right, and U-turning,
                        are prohibited by the 'no turn' markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left', 'no_turn:right', 'no_turn:u_turn'], missed ['area:grid']), actions
                        False, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 1233, 9.25 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, there
                        is an intersection visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line near the car, and Photo 2 shows a solid yellow line
                        near the car. Further ahead, Photo 1 shows a solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line near the car, and Photo 2 shows a broken white line
                        near the car. Further ahead, Photo 1 shows a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow solid for center_line, white dashed for lane_line) | markings: the area:grid
                        marking is consistent with the boundaries and general road markings | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            area:grid: The grid marking shows an area where stopping for any reason is prohibited.
                        [[CN-6.8.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The right boundary is a broken white line,
                        which allows lane changes, and there is no marking prohibiting it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a broken white line, which allows
                        lane changes, and there is no marking prohibiting it.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in the lane to restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of the lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight, change left, or change
                        right. Be aware that the area immediately ahead of you is marked as a grid,
                        prohibiting stopping for any reason.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed ['symbol:other']), actions False, unsafe ['change_left'],
                        citation accepted, contradictions []
Tokens                  in 8454, out 864, 5.95 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a road section
                        leading towards what appears to be an intersection or a change in road configuration.
                        My car is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2 shows a white dashed line segment ahead of my
                        car, which is part of the lane boundary, not a marking within the lane.;
                        line:yield_line (insufficient): Photo 2 shows a white dashed line segment ahead of my
                        car, which is part of the lane boundary, not a marking within the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: the lane markings list is empty of
                        features within the lane, which is consistent with the boundaries being the primary
                        features. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 5  Rule            line:yield_line: The slow-and-yield line means that vehicles shall slow down or stop
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a dashed white
                        lane_line, and [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a dashed
                        white lane_line, and [CN-5.2.3] permits lane changes where crossable lane lines are
                        used.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable because there are no arrows
                        or prohibited-movement markings in my lane governing this action.
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable because there are no arrows or
                        prohibited-movement markings in my lane governing this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable because there are no arrows
                        or prohibited-movement markings in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific turn arrows or waiting areas, you should proceed straight unless you
                        intend to turn, in which case you must check for appropriate lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line', 'line:yield_line'], missed ['arrow:right']), actions False, unsafe
                        ['change_left', 'change_right', 'go_straight'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8454, out 1080, 7.88 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a section where the road appears to
                        continue straight, possibly leading to an intersection or another section of the road.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line near my car, and Photo 2 shows a solid white line
                        near my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo 2
                        shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line near my car, and Photo 2 shows a solid white line
                        near my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo 2
                        shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is a
                        lane_line, indicating my lane is between two lanes of the same direction) | roles: the
                        color and pattern of both boundaries (solid white) fit the role of a lane_line |
                        markings: there are no markings in my lane to check against the boundaries | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane_line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane_line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 813, 6.98 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection or a section where lane
                        guidance is present. My car is in the rightmost lane visible in the immediate
                        foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, this line
                        appears to continue as a white dashed line. Photo 2: A white dashed line is visible
                        next to my car. Further ahead, this line continues as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, this line
                        appears to continue as a white dashed line. Photo 2: A white dashed line is visible
                        next to my car. Further ahead, this line continues as a white dashed line.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 2: A white arrow pointing right is visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line). | roles: the white dashed line on the left fits the role of a lane_line,
                        and the white dashed line on the right fits the role of an edge_line. | markings: the
                        right arrow in my lane is consistent with the boundaries and markings. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:right: Guide arrows indicate the direction of travel for vehicles, and a right
                        arrow indicates travel to the right. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The white dashed line on the left is a
                        lane_line, and while it is broken, the right arrow in my lane only permits movement to
                        the right, not to the left.
Step 6  change_right    allowed (correct): allowed: The white dashed line on the right is an edge_line, and
                        the right arrow in my lane permits movement to the right.
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited: The right arrow in my lane only permits
                        movement to the right, not straight ahead.
Step 6  turn_left       prohibited (correct): prohibited: The right arrow in my lane only permits movement to
                        the right, not to the left.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The right arrow in my lane permits
                        movement to the right.
Step 6  u_turn          prohibited (correct): prohibited: The right arrow in my lane only permits movement to
                        the right, not a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You should only proceed by turning right or changing right into the adjacent lane. Do
                        not attempt to go straight or turn left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed ['arrow:straight']), actions False, unsafe ['turn_right'],
                        citation accepted, contradictions ['change_left prohibited across a broken lane line']
Tokens                  in 8454, out 932, 7.0 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, there is
                        an intersection or a major road crossing. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line appears to be a white dashed line.
                        Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line appears to be a white dashed line.
                        Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2: A white arrow pointing straight ahead is visible
                        in the lane. Photo 2: A white arrow pointing straight ahead is visible in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: the white
                        arrow pointing straight ahead in the lane agrees with the boundaries (dashed lines
                        allow lane changes, but the arrow restricts movement). | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white
                        lane_line, and [CN-5.2.1-2] permits the crossing of a broken white line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, and [CN-5.2.1-2] permits the crossing of a broken white line.
Step 6  go_straight     allowed (correct): allowed: The lane contains a guide arrow showing straight ahead,
                        and [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       prohibited (correct): prohibited: The lane contains a guide arrow that does not show a
                        left turn, and [CN-5.13.1] restricts movement to the directions shown.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The lane contains a guide arrow showing
                        straight or right, and [CN-5.13.1] indicates the direction of travel.
Step 6  u_turn          prohibited (correct): prohibited: The lane contains a guide arrow that does not show a
                        U-turn, and [CN-5.13.1] restricts movement to the directions shown.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          this lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight or turn right. You may
                        change lanes left or right as the lane lines are broken, but be mindful of the arrow
                        restricting turns. Use the middle lane for straight or right turns.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight']), actions False, unsafe
                        ['change_left', 'change_right', 'turn_right'], citation accepted, contradictions []
Tokens                  in 8454, out 1010, 7.68 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban or suburban area, and the road continues
                        straight ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing into the distance. Photo 2: The line next
                        to my car is a white dashed line. Further ahead, the line is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing into the distance. Photo 2: The line next
                        to my car is a white dashed line. Further ahead, the line is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes
                        within the same direction of travel) | roles: the white dashed lines fit the role of
                        lane_line separating traffic flows in the same direction | markings: there are no
                        markings in my lane to check against boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits the crossing of a broken white line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits the crossing of a broken white line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to restrict
                        going straight, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes to the left or right as the lane markings are broken white lines. You may
                        proceed straight ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 841, 6.5 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into the distance, appearing to be a straight section without an immediate
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid yellow line is visible next to the car. Photo 2: A solid yellow line
                        is visible next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A broken white line is visible next to the car. Photo 2: A broken white line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow solid for center_line, white dashed for lane_line) | markings: there are no
                        markings in my lane to check for agreement | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing (though this line is single solid). [[CN-6.1.1]]
Step 5  Rule            right_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing (though this
                        line is broken). [[CN-6.2.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The right boundary is a broken white line,
                        which permits crossing from the broken side, and [CN-5.2.3] permits lane changes where
                        crossable lane lines are used.
Step 6  change_right    allowed (correct): allowed: The right boundary is a broken white line, which permits
                        crossing from the broken side, and [CN-5.2.3] permits lane changes where crossable
                        lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight. You may change lanes to
                        the left or right as the lane markings permit, but you should proceed with caution as
                        you are in a multi-lane road.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 8454, out 929, 7.11 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, there is a
                        wide intersection or a section where the road widens/changes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A yellow dashed line is visible to the left of my lane, further ahead. Photo
                        2: A yellow dashed line is visible to the left of my lane, further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible to the right of my lane, further ahead. Photo
                        2: A white dashed line is visible to the right of my lane, further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible on the road surface
                        ahead of my car, indicating lane division.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow dashed for center_line, white dashed for lane_line) | markings: the markings
                        (a dashed line ahead) agree with the boundaries (dashed lines define the lanes) |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Yellow longitudinal markings separate traffic flows in opposite
                        directions and mark the left-hand edge of the direction of travel and tidal lanes.
                        [[CN-4.3.2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a yellow dashed
                        center_line, and [CN-5.1.1] permits crossing the crossable centre line when it does
                        not affect safety.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line as it is a broken white line.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: Nothing restricts carrying on straight
                        along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  u_turn          not_applicable (WRONG, label allowed): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. Since
                        there are no specific markings for turns or waiting areas, you should proceed straight
                        unless you intend to change lanes.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:left_u_turn', 'arrow:straight']), actions False,
                        unsafe ['change_left', 'go_straight'], citation accepted, contradictions []
Tokens                  in 8454, out 944, 7.22 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a stretch of
                        road leading towards what appears to be an intersection or a continuation of the road
                        with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Further ahead, the line
                        appears to be a white dashed line. Photo 2: A white dashed line is visible next to the
                        car. Further ahead, the line is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Further ahead, the line
                        appears to be a white dashed line. Photo 2: A white dashed line is visible next to the
                        car. Further ahead, the line is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2: A white arrow pointing straight ahead is visible
                        in the lane.; arrow:straight_right (full): Photo 2: A white arrow pointing straight
                        ahead is visible in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the arrows
                        in the lane agree with the boundaries (they are within the lane defined by the
                        boundaries). | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead or right. [[CN-5.13.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a dashed white
                        lane line, but the lane markings only indicate straight or right movement, not a lane
                        change to the left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane line, and the
                        lane markings allow for movement to the right.
Step 6  go_straight     allowed (correct): allowed: The lane markings show an arrow indicating straight ahead
                        or right, and there are no prohibitions against going straight.
Step 6  turn_left       prohibited (correct): prohibited: The lane markings only show arrows for straight
                        ahead or right, not a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The lane markings show an arrow indicating
                        straight ahead or right, and the right boundary is a dashed white lane line.
Step 6  u_turn          prohibited (correct): prohibited: The lane markings only show arrows for straight
                        ahead or right, not a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of the lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight or turn right. You may
                        change right into the right lane, but you cannot change left or make a left turn.
                        Proceed with caution based on the lane markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight']), actions False, unsafe
                        ['turn_right'], citation accepted, contradictions ['change_left prohibited across a
                        broken lane line']
Tokens                  in 8454, out 1023, 8.78 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an overpass on the left. Ahead, the road continues into
                        an urban area with buildings on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2: A solid white line is visible across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: the color (white) and
                        pattern (solid) of both boundaries fit the role of a lane_line. | markings: the solid
                        white line ahead is consistent with a stop line, which is a line across the lane. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane_line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane_line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane next to it.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines. You may proceed straight ahead, but you must come to a complete stop before the
                        solid white stop line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 921, 7.28 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, there is a
                        junction or area where lane directions are indicated by overhead signs. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line appears to be a white dashed line.
                        Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line appears to be a white dashed line.
                        Further ahead, the line appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1: A white dashed line is visible across the lane
                        ahead, indicating lane division. Photo 2: A white dashed line is visible across the
                        lane ahead, indicating lane division.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line. | markings: The visible white dashed line ahead is interpreted
                        as a stop line, which is consistent with the lane markings. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.3]
                        permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [CN-5.2.3]
                        permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane that prohibit
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          the lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and no
                        action is allowed against a rule from step 5.
Advice                  You are in the middle lane, which allows you to go straight, change left, or change
                        right. You should proceed with caution as the lane ahead has a stop line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 972, 7.81 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where traffic flow is managed by lane markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A yellow line separates my lane from the lane to the left. Photo 2: A yellow
                        dashed line separates my lane from the lane to the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white line separates my lane from the lane to the right. Photo 2: A white
                        dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2: A white arrow pointing straight ahead is visible
                        in my lane.; arrow:straight_right (full): Photo 2: A white arrow pointing straight
                        ahead is visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is yellow/lane_line, right boundary
                        is white/lane_line) | roles: the color and pattern of each boundary fit the role given
                        to it | markings: the arrows in my lane agree with the boundaries (they are within the
                        lane defined by the boundaries) | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross, but vehicles on the
                        broken-solid white line may cross, and a vehicle crossing the line must give way to
                        vehicles travelling normally. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead or right. [[CN-5.13.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a yellow dashed lane line, and
                        while a dashed line may be crossed, the arrow in my lane only permits straight or
                        right movement, which implies no lane change left is permitted.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and a broken line means it may be crossed, and the arrow permits straight or
                        right movement.
Step 6  go_straight     allowed (correct): allowed: The arrow in my lane permits straight ahead movement, and
                        the right boundary is a broken line allowing lane changes.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in my lane does not show a left turn
                        movement, and the left boundary is a yellow dashed lane line.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in my lane permits straight or
                        right movement, and the right boundary is a broken line allowing lane changes.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane does not show a U-turn
                        movement, and the left boundary is a yellow dashed lane line.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight or turning right. You may
                        change right if necessary, but turning left or making a U-turn is prohibited by the
                        lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight', 'line:stop_line']), actions False,
                        unsafe ['change_right', 'turn_right'], citation accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 8454, out 1015, 7.92 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. There are multiple lanes
                        visible in my direction near the bottom of the photo, and the road ahead leads into an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: The color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: The stop
                        line is present in my lane and is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-5.2.1-2] permits the crossing of a broken white line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane_line, and
                        [CN-5.2.1-2] permits the crossing of a broken white line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in my lane,
                        and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there is
                        a stop line ahead, you must stop before entering the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 1054, 7.19 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, there
                        is an intersection visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two lanes of the same direction) | roles: the color and pattern of both
                        boundaries (white dashed) fit the role of lane_line | markings: no markings were
                        listed, so this is consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [CN-5.2.1-2] permits crossing.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and
                        [CN-5.2.1-2] permits crossing.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict carrying on straight along
                        my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. No
                        specific turning movements are indicated or restricted in your lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 819, 5.78 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and ahead there is an exit ramp/junction.
                        My car is in the rightmost lane visible in the immediate foreground. (lanes 3, mine 3,
                        full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, this line
                        appears to be a white dashed line continuing towards the exit. Photo 2: A white dashed
                        line is visible next to my car. Further ahead, this line continues as a white dashed
                        line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, this line
                        continues towards the edge of the road/barrier. Photo 2: A white dashed line is
                        visible next to my car. Further ahead, this line continues towards the edge of the
                        road/barrier.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible on the road surface
                        ahead of my car, indicating lane division. This line extends into the distance.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (3) agree with the boundary roles: the left boundary is a lane_line separating my lane
                        from the middle lane, and the right boundary is an edge_line. | roles: The white
                        dashed line on the left fits the role of a lane_line, and the white dashed line on the
                        right fits the role of an edge_line. | markings: The visible dashed line ahead is
                        interpreted as a stop line, which is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and means vehicles may change lanes if it is a broken white line. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [CN-5.2.1-2] permits lane changes on a broken white line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed
                        edge_line, and [CN-5.4.2] permits the use of a broken edge line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by visible features or lack thereof according to the rules.
Advice                  You are in the rightmost lane, which is permitted to change left or right. You may
                        proceed straight ahead, but be aware of the stop line ahead, which requires you to
                        stop if you are yielding or waiting to proceed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 1017, 8.15 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a suburban or urban area, and ahead, the road continues
                        straight without an immediate intersection visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2 shows a white dashed line marking the lane
                        boundary to the left, and Photo 2 shows a white dashed line marking the lane boundary
                        to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        middle lane (index 2). The boundaries are lane lines, which is consistent with my lane
                        being one of three lanes in the same direction. | roles: The white dashed lines on
                        both sides are consistent with the role of a lane_line separating traffic flows in the
                        same direction. | markings: The only marking observed is a line that is too far ahead
                        or too indistinct to confirm its role as a stop line, but the boundaries are
                        consistent with lane lines. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.3]
                        permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [CN-5.2.3]
                        permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes, and lane changes are permitted as the
                        boundaries are dashed white lines. You may proceed straight, but you should be aware
                        of the potential stop line ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 1098, 8.24 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line next to my car, and a yellow solid line further
                        ahead. Photo 2 shows a yellow solid line next to my car, and a yellow solid line
                        further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        text:other (full): Photo 1 shows a white dashed line with the number '2' painted on it
                        in my lane. Photo 2 shows a white dashed line with the number '2' painted on it in my
                        lane.; text:other (full): Photo 1 shows a yellow solid line with the number '9'
                        painted on it in my lane. Photo 2 shows a yellow solid line with the number '9'
                        painted on it in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed for lane_line, yellow solid for center_line). | markings: the text
                        markings are located within my lane and do not contradict the boundaries. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: A no-crossing centre line has three forms: double solid yellow,
                        broken-solid yellow and single solid yellow, and it prohibits vehicles in both
                        directions, or in one direction, from crossing. [[CN-6.1.1]]
Step 5  Rule            text:other: No specific traffic rule passage covers the meaning of the painted numbers
                        in the lane. [null]
Step 5  Rule            text:other: No specific traffic rule passage covers the meaning of the painted numbers
                        in the lane. [null]
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a dashed line,
                        which permits crossing according to [CN-4.2.2-a].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        yellow line, which prohibits crossing according to [CN-6.1.1].
Step 6  go_straight     allowed (contested, label prohibited): allowed because there are no markings in my
                        lane prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane governing a
                        right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you are permitted to change left because the lane line
                        is dashed, but changing right is prohibited by the solid yellow line. You may proceed
                        straight ahead in this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed ['text:bus']), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8454, out 995, 7.09 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues into the distance with an overpass structure visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Further ahead, the solid white
                        line continues. Photo 2: A solid white line is visible next to the car. Further ahead,
                        the solid white line continues.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            left_boundary: On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes (though this line
                        is solid, implying prohibition). [[CN-5.2.3]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a solid white lane_line, and there is
                        no rule prohibiting a lane change from the broken side (though this line is solid, it
                        governs the boundary).
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, and there
                        is no rule prohibiting a lane change onto the shoulder/edge.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in my lane
                        that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you are permitted to change lanes left or right, as
                        well as proceed straight ahead. No specific stopping or turning instructions are
                        marked in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 854, 6.62 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, and Photo 2 shows a solid white line
                        next to the car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, and Photo 2 shows a solid white line
                        next to the car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows a solid white line continuing.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the stop_line marking is consistent with the boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white lane
                        line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge line, and no rule
                        prohibits crossing the edge line in this context.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of my lane or to its left.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may proceed straight ahead. You may change to the
                        right, but you must stop before the solid white line ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 864, 7.59 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight, and
                        there are vehicles visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            left_boundary: On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes (though this line
                        is solid, indicating prohibition). [[CN-5.2.3]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        lane_line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, and no rule
                        prohibits changing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change right into the adjacent lane, and you may proceed straight ahead.
                        Turning movements are not governed by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 818, 6.02 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road curves slightly to the
                        right and appears to lead towards an intersection or junction indicated by overhead
                        signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible further ahead. Photo 2: A white dashed line is
                        visible further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in Photo 2, and no markings are clearly visible further ahead
                        in Photo 1.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane line separating my lane
                        from the left lane, and the right boundary is a lane line separating my lane from the
                        right lane. | roles: The white dashed lines fit the role of a lane_line separating
                        traffic flows in the same direction. | markings: No contradictions found between the
                        observed markings and boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: No arrow in my lane restricts carrying on
                        straight along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane in view to govern this action.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed against a prohibition from step 5.
Advice                  You are in the middle lane of a multi-lane highway, and lane changes are permitted as
                        the lane lines are broken. You may proceed straight, but turning movements are not
                        explicitly governed by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 943, 8.49 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with trees lining both sides. Ahead, the road continues
                        straight into the distance, with no immediate intersection or ramp visible. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, Photo 1 shows a white dashed line. Photo 2
                        shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, Photo 1 shows a white dashed line. Photo 2
                        shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: there are
                        no markings in my lane to check against the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, and [CN-5.2.1-2]
                        permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes left or right,
                        and you may proceed straight ahead. No specific turn movements are indicated or
                        restricted in your lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 818, 6.31 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight with no immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows the line further ahead is also a white dashed line.
                        Photo 2 shows the line further ahead is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows the line further ahead is also a white dashed line.
                        Photo 2 shows the line further ahead is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings observed in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: The color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: No markings were listed, so there
                        is no agreement to check. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-5.2.1-2] permits crossing.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, and [CN-5.2.1-2] permits crossing.
Step 6  go_straight     allowed (contested, correct): allowed: No arrow or prohibited-movement marking governs
                        this action, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and since both lane boundaries are dashed, you are
                        permitted to change lanes left or right. All movements are allowed unless restricted
                        by an unseen sign or signal.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 1061, 7.64 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight,
                        possibly approaching an interchange or a section where lane configuration changes, as
                        suggested by the markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 2 shows a wide red/maroon painted area in my lane,
                        extending ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the
                        channelizing area is within my lane and does not contradict the boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            area:channelizing: Channelizing lines separating traffic in the same direction are
                        white and show that vehicles must follow the set path and may not drive on or across
                        the lines. [[CN-6.6.1-3]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed
                        lane_line, and [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway. You may change lanes left or
                        right, and you may proceed straight ahead. Be aware of the channelizing markings in
                        your lane, which indicate you must follow the designated path.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 947, 8.0 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, the
                        road continues straight, and there are no immediate intersections or ramps visible.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A broken white line is visible next to the car. Photo 2: A broken white line
                        is visible next to the car. Further ahead, the broken white line continues. Photo 2
                        shows the line further ahead continuing as a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, the solid white line continues. Photo 2 shows
                        the line further ahead continuing as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles: the left boundary is a lane_line (separating lane 1
                        and 2), and the right boundary is a lane_line (separating lane 2 and 3). | roles: The
                        left boundary is a broken white lane_line, and the right boundary is a solid white
                        lane_line, which fits the role of separating lanes in the same direction. | markings:
                        There are no arrows, words, or areas painted in my lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 5  Rule            left_boundary: On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes. [[CN-5.2.3]]
Step 6  change_left     allowed (correct): Allowed because the left boundary is a broken white lane_line,
                        which permits crossing according to [CN-5.2.1-2] and [CN-5.2.3].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited because the right boundary is a solid
                        white lane_line, which prohibits crossing according to [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        restricting straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: Not applicable because there are no markings in my lane governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable because there are no markings in my lane governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable because there are no markings in my lane governing this
                        action.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings in my lane governing
                          this action.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed against a prohibition from step 5.
Advice                  You are in the middle lane, which allows you to change left, but changing right is
                        prohibited by the solid white line. You may proceed straight ahead in this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 938, 6.87 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, the
                        road continues into the distance with an overpass visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A yellow line separates my lane from the adjacent lane on the left. Photo 2:
                        A yellow line separates my lane from the adjacent lane on the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white line marks the right edge of the travel lanes. Photo 2: A white line
                        marks the right edge of the travel lanes.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            left_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The broken edge line has 60 cm segments and 30 cm gaps (also called a
                        "dense broken line"). [[CN-5.4.2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed yellow lane_line, and
                        [CN-5.2.1-2] permits the crossable lane line to be crossed.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white edge_line, and
                        [CN-5.4.2] describes the broken edge line, which does not prohibit crossing.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern U-turns or
                        turning.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you are permitted to change lanes both left and right.
                        You may proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 881, 6.51 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. Ahead, the road continues straight into
                        the distance, with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to the car.
                        Further ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Further ahead, the white
                        dashed line continues. Photo 2: A white dashed line is visible next to the car.
                        Further ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction) | roles: the color and pattern of both
                        boundaries (white dashed) fit the role of lane_line | markings: there are no markings
                        in my lane to check against boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern U-turns or
                        turning.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right, and you may proceed straight ahead. No specific lane usage is mandated for your
                        intended movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 821, 5.65 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway with a clear view ahead, suggesting a long
                        stretch of road rather than an immediate intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line separating traffic flows in the same direction. | markings: The
                        stop line is visible in Photo 2 and is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a white dashed lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a white
                        dashed lane_line, and [CN-5.2.3] permits lane changes where crossable lane lines are
                        used.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibitions in
                        the lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no marked waiting areas or two-way
                          left-turn lanes visible.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by the observed features and rules.
Advice                  You are in the middle lane of a multi-lane highway, and lane changes are permitted as
                        the lane lines are broken. You may proceed straight, but you should be aware of the
                        stop line visible ahead, which indicates a point where you may need to stop to yield
                        or wait.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 1115, 7.21 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a curve in the road, not an intersection
                        or a ramp end. My car is in the rightmost lane visible near the bottom of the photo.
                        (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, and further ahead, it appears to be
                        a broken white line. Photo 2 shows a broken white line next to my car, and further
                        ahead, it is a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and further ahead, it is a solid
                        white line. Photo 2 shows a solid white line next to my car, and further ahead, it is
                        a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a dashed white line marking the lane boundary
                        near my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line). | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed line for lane_line, white solid line for edge_line). | markings: the
                        markings (line:stop_line) are consistent with the boundaries and each other. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white line, which allows
                        crossing according to [CN-4.2.2-a].
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white line, which
                        prohibits crossing according to [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or next to it.
Step 7  Reflect         consistent
Advice                  You may change left into the adjacent lane, but changing right is prohibited by the
                        solid white line. You may proceed straight ahead, but you must stop at the visible
                        stop line before proceeding.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 938, 7.14 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and the road continues straight ahead with
                        no immediate intersection or ramp visible. My car is in the rightmost lane of the
                        visible lanes in my direction. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check against boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            left_boundary: On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes. [[CN-5.2.3]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white
                        lane_line, and [CN-5.2.1-2] permits the crossing of a broken white line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        edge_line, and [CN-5.4.2] permits the use of a broken edge line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turns, you may proceed straight, but be aware of the lane
                        markings indicating lane separation.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 880, 7.03 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road, and ahead there is a continuation of
                        the road with multiple lanes. My car is in one of the lanes near the bottom of the
                        photo. (lanes 5, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 shows a speed limit sign above the lane, indicating
                        100, 80, 80, 60, 60. Photo 2 shows the lane markings, but no specific arrows or text
                        within the lane itself.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (5) and my lane position
                        (3) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: The color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: The speed
                        limit markings are consistent with the lane structure. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            text:speed_limit: Pavement speed limit markings show the speed limit of a lane and are
                        placed at the start of the lane and at other suitable places where the maximum speed
                        is limited. [[CN-5.14.2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the third lane, which allows you to go straight, change left, or change
                        right. Since there are no specific turn arrows, you can proceed straight or change
                        lanes as needed, keeping in mind the posted speed limits for your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:speed_limit'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 1164, 8.92 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there appears to be a junction or a section
                        where lane guidance is present. My car is in the lane closest to the left side of the
                        visible road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A yellow line is visible next to the car, and further ahead, it appears to be
                        a solid yellow line. Photo 2: The line next to the car is a yellow dashed line, and
                        the line further ahead is a solid yellow line.
                        yellow dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1: A white line is visible next to the car, and further ahead, it appears to be
                        a solid white line. Photo 2: The line next to the car is a white dashed line, and the
                        line further ahead is a solid white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 1: No specific markings like arrows, words, or areas
                        are clearly visible within my lane in the immediate foreground or further ahead.
Step 4  Cross-check     close_up: The pattern of the left boundary changes from dashed (Photo 2) to solid
                        (Photo 1) further ahead, and the pattern of the right boundary changes from dashed
                        (Photo 2) to solid (Photo 1) further ahead. Photo 1 decides changes further ahead. I
                        corrected the pattern of both boundaries further ahead to solid. The lane count (3)
                        and ego lane index (1) agree with the boundary roles (left boundary is an edge line,
                        right boundary is a lane line). The roles fit the colors and patterns (yellow edge
                        line on the left, white lane line on the right). The markings (stop line) are
                        consistent with the boundaries. No unseen attributes were reported. The result is
                        consistent. | position: consistent | roles: consistent | markings: consistent |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): prohibited: The left boundary is a yellow edge
                        line, and while the immediate line is dashed, the change is governed by the general
                        prohibition of crossing a solid line if it were solid, but since it is dashed, it is
                        allowed unless other markings prohibit it. However, the solid line further ahead
                        suggests a restriction, and the general rule for edge lines is permissive for changes
                        unless solid.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and a broken line means it may be crossed [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in my lane
                        that restrict going straight ahead.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and no
                        action is allowed against a rule from step 5.
Advice                  You are in the leftmost lane, which is bordered by a yellow edge line. You may change
                        right into the adjacent lane, and you may proceed straight ahead. You must stop at the
                        visible stop line before proceeding through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 1091, 9.86 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic flowing in the same direction. Ahead, the road
                        continues straight, and there is a visible intersection or change in road
                        configuration further down. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Further ahead, this solid
                        white line continues. Photo 2: A solid white line is visible next to the car. Further
                        ahead, this solid white line continues.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Further ahead, this solid
                        yellow line continues. Photo 2: A solid yellow line is visible next to the car.
                        Further ahead, this solid yellow line continues.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2: No specific arrows, words, symbols, areas, or
                        lines are visible within my lane in the close-up.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles: the left boundary is a lane_line separating my lane
                        from the left lane, and the right boundary is an edge_line. | roles: The left boundary
                        is a solid white lane_line, and the right boundary is a solid yellow edge_line, which
                        fits their roles. | markings: No markings were observed in my lane that contradict the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, but since this is yellow, it functions as a separation line for opposing
                        traffic or a general boundary, and the rule for yellow longitudinal markings applies
                        to separation of opposing traffic flows. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane_line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid yellow edge_line, and
                        while [CN-5.4.3] specifies white for the right edge line, the solid nature of the line
                        prohibits crossing into the adjacent area.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed against a prohibition from Step 5.
Advice                  You must stay in the middle lane to proceed straight ahead, as lane changes are
                        prohibited by the solid lines on both sides. Proceed with caution as you approach the
                        intersection ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 1016, 7.74 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a road section that appears to continue
                        straight, possibly leading to an intersection or a change in road configuration.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead, and Photo 2 shows a
                        solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and Photo 2 shows a solid yellow
                        line next to my car. Photo 1 shows a solid yellow line further ahead, and Photo 2
                        shows a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        no_turn:left (full): Photo 2; no_turn:right (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        second from the left (ego_lane_index=2). The left boundary is a lane_line (white
                        solid) and the right boundary is a center_line (yellow solid), which is consistent
                        with my lane being the middle lane. | roles: The left boundary is a white solid
                        lane_line, and the right boundary is a yellow solid center_line, which fits their
                        roles. | markings: The two no_turn markings (left and right) are present in my lane
                        and are consistent with the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            no_turn:left: No U-turn and no turn markings are used at intersections or on sections
                        where U-turns or turns are prohibited. [[CN-6.11.1-2]]
Step 5  Rule            no_turn:right: No U-turn and no turn markings are used at intersections or on sections
                        where U-turns or turns are prohibited. [[CN-6.11.1-2]]
Step 6  change_left     prohibited (correct): prohibited due to the solid white lane_line on the left, as per
                        [CN-6.2.1].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the solid yellow center_line on
                        the right, as per [CN-6.1.1].
Step 6  go_straight     prohibited (contested, label allowed): prohibited due to the no_turn:left and
                        no_turn:right markings in the lane, as per [CN-6.11.1-2].
Step 6  turn_left       prohibited: prohibited due to the no_turn:left marking in the lane, as per
                        [CN-6.11.1-2].
Step 6  turn_right      prohibited: prohibited due to the no_turn:right marking in the lane, as per
                        [CN-6.11.1-2].
Step 6  u_turn          prohibited: prohibited due to the no_turn:left and no_turn:right markings in the lane,
                        as per [CN-6.11.1-2].
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings for a waiting area in view.
Step 7  Reflect         consistent
Advice                  Your lane is restricted by solid markings, prohibiting any lane changes or movements
                        to turn or go straight. You must remain in this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left', 'no_turn:right'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 1237, 8.23 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a bridge or overpass
                        structure, suggesting the road continues forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (solid white lines on both sides indicate lane
                        separation). | roles: the color (white) and pattern (solid) of both boundaries fit the
                        role of lane_line. | markings: there are no markings in my lane to check against the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes and must stay in your lane as lane changes
                        are prohibited by the solid white lines. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 797, 8.95 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection area visible in the distance. My car is in the lane closest to the center
                        of the visible traffic flow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, and further ahead, the line appears
                        to continue as a broken white line. Photo 2 shows a broken white line next to my car,
                        and further ahead, the line continues as a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and further ahead, the line appears
                        to continue as a solid white line. Photo 2 shows a solid white line next to my car,
                        and further ahead, the line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 5  Rule            left_boundary: On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes. [[CN-5.2.3]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a broken white line,
                        which is a crossable lane line, and [CN-5.2.3] allows lane changes where such a line
                        is used.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white line, which is a
                        no-crossing lane line, and [CN-6.2.1] prohibits vehicles on the solid-line side from
                        crossing.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change left into the adjacent lane, but changing right is prohibited by the
                        solid white line. You may proceed straight ahead, but turning left, turning right, or
                        making a U-turn are not governed by any markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 8454, out 913, 6.57 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there appears to be a
                        continuation of the road, possibly leading to an intersection or a section where lane
                        configuration changes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it is a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction) | roles: the color and pattern of both
                        boundaries (white dashed) fit the role of lane_line | markings: there are no markings
                        in my lane to check against the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to restrict
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right as the lane lines are broken. You may proceed straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 8454, out 836, 6.17 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead, the road continues straight, possibly leading to
                        an intersection or a change in road configuration. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Photo 1 shows a solid white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows no markings in my lane. Photo 2 shows no
                        markings in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane_line (separating my
                        lane from the lane on the left), and the right boundary is a lane_line (separating my
                        lane from the lane on the right). | roles: The left boundary is a broken white
                        lane_line, and the right boundary is a solid white lane_line, which fits the role of
                        separating lanes in the same direction. | markings: There are no arrows, words, or
                        areas visible in my lane to check against the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a broken white
                        lane_line, and [CN-5.2.1-2] permits crossing the broken line.
Step 6  change_right    prohibited (correct): Prohibited because the right boundary is a solid white
                        lane_line, and [CN-6.2.1] prohibits vehicles on the solid-line side from crossing.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_right      not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  u_turn          not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  enter_waiting_areanot_applicable: Not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by the observed features and rules.
Advice                  You are in the middle lane, which allows you to change left if necessary, but changing
                        right is prohibited by the solid white line. You may proceed straight, but turning
                        movements are not explicitly permitted or prohibited by lane markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 1072, 7.5 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line immediately next to the car, and further ahead, this
                        line continues as a solid white line. Photo 2 shows a solid white line immediately
                        next to the car, and further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line immediately next to the car, and further ahead, this
                        line continues as a solid white line. Photo 2 shows a solid white line immediately
                        next to the car, and further ahead, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a broken white line segment in the lane ahead
                        of the car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: the color (white) and
                        pattern (solid) of both boundaries fit the role of a lane_line. | markings: the
                        line:stop_line is visible in Photo 2 and is consistent with the lane markings. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross. [[CN-6.2.1]]
Step 5  Rule            right_boundary: Vehicles on the solid-line side may not cross. [[CN-6.2.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        lane_line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        lane_line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane that prohibit
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          the lane or adjacent to it.
Step 7  Reflect         consistent
Advice                  You are in the middle lane and must not change lanes due to the solid white lines on
                        both sides. You may proceed straight ahead, but you must stop before the visible stop
                        line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 911, 7.61 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban area, and the road continues straight ahead with
                        no immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego lane index
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating two
                        lanes in the same direction). | roles: the color and pattern of both boundaries (white
                        dashed) fit the role of a lane_line. | markings: the arrow (straight_right) is present
                        in my lane and is consistent with the lane boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates straight or right travel. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane_line, and
                        while this allows lane changes, the arrow in my lane only permits straight or right
                        movement, which restricts a left change.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a white dashed
                        lane_line, and the arrow in my lane permits straight or right movement, which includes
                        the possibility of changing right.
Step 6  go_straight     allowed (correct): allowed: The arrow in my lane permits straight travel, and the
                        boundaries do not prohibit going straight.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in my lane only permits straight or right
                        movement, which prohibits a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in my lane permits straight or
                        right movement, which includes the possibility of turning right.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane only permits straight or right
                        movement, which prohibits a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the lane designated for straight or right movement. You may change right if
                        necessary, but you must not change left. You may proceed straight or turn right at the
                        next opportunity.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight']), actions False, unsafe
                        ['turn_right'], citation accepted, contradictions ['leftmost lane, but a lane line on
                        the left', 'change_left prohibited across a broken lane line']
Tokens                  in 8454, out 893, 6.5 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection where the road continues. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line next to my car. Photo 2 shows a solid yellow line
                        next to my car. Photo 1 shows a solid yellow line further ahead. Photo 2 shows a solid
                        yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Photo 1 shows a solid white line further ahead. Photo 2 shows a solid white
                        line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is
                        an edge_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow solid for center_line, white solid for edge_line) | markings: no markings were
                        listed, so there is no agreement to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid yellow center_line, and
                        [CN-6.1.4] prohibits crossing a single solid yellow line.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a solid white
                        edge_line, and no rule prohibits crossing a solid white edge_line.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict carrying on straight along
                        my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane next to it.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to proceed straight or change right. You
                        may change right as the right boundary is a solid white edge line, but you must stop
                        at the visible stop line if you are yielding or waiting to proceed.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 8454, out 894, 6.43 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues straight
                        ahead into the distance. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line, indicating my lane is between two lanes of the same direction) | roles: the
                        color and pattern of both boundaries fit the role of a lane_line (solid white lines
                        separating lanes in the same direction) | markings: there are no markings in my lane
                        to check against the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are permitted to proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 8454, out 779, 5.91 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a set of traffic
                        signs indicating lane directions, suggesting an approach to an intersection or a
                        change in lane configuration. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Photo 1 shows a solid white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and Photo 2 shows a solid yellow
                        line next to my car. Photo 1 shows a solid yellow line further ahead.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a blue overhead sign with three upward arrows,
                        one in the center lane (my lane).
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left, which is consistent with the boundaries: a lane line on the left
                        and an edge line on the right. | roles: The left boundary is a white lane line, and
                        the right boundary is a yellow edge line, which fits the roles. | markings: The
                        overhead arrow in my lane indicates straight travel, which is consistent with the lane
                        markings. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and an
                        arrow showing straight ahead indicates that vehicles may proceed straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a broken white lane
                        line, and while [CN-5.2.3] allows lane changes on broken-solid lines, the presence of
                        the straight arrow in my lane restricts movements to straight ahead.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a solid yellow edge line,
                        and there is no marking in my lane prohibiting a lane change to the right.
Step 6  go_straight     allowed (contested, correct): allowed, because the overhead arrow in my lane shows
                        straight ahead, and [CN-5.13.1] indicates this direction of travel is permitted.
Step 6  turn_left       prohibited: prohibited, because the overhead arrow in my lane does not show a left
                        turn, and [CN-5.13.1] dictates that an arrow not showing a movement prohibits it.
Step 6  turn_right      prohibited: prohibited, because the overhead arrow in my lane does not show a right
                        turn, and [CN-5.13.1] dictates that an arrow not showing a movement prohibits it.
Step 6  u_turn          prohibited: prohibited, because the overhead arrow in my lane does not show a U-turn,
                        and [CN-5.13.1] dictates that an arrow not showing a movement prohibits it.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings for a waiting area or
                          a two-way left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You are currently in the middle lane, which is designated for straight travel. You may
                        change to the right, but you must proceed straight ahead as turning left, right, or
                        making a U-turn is prohibited by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['change_left prohibited across a broken lane line']
Tokens                  in 8454, out 1207, 8.96 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection where the
                        road continues and potentially changes direction. My car is in one of the lanes near
                        the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction) | roles: the color and pattern of both
                        boundaries (white dashed) fit the role of lane_line | markings: there are no markings
                        in my lane to check against boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits crossing the crossable lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may change lanes left or right as the lane lines
                        are broken. All movements, including going straight, are permitted by the current
                        markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8454, out 831, 6.14 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car, and Photo 2 shows a dashed white
                        line next to my car. Photo 1 shows a solid white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and Photo 2 shows a solid yellow
                        line next to my car. Photo 1 shows a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line). | roles: the color and pattern of each boundary fit the role given to it
                        (dashed white line is a lane_line, solid yellow line is a center_line). | markings:
                        the stop line marking is consistent with the boundaries and general road markings. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The no-crossing centre line has three forms: double solid yellow,
                        broken-solid yellow and single solid yellow, and it prohibits vehicles in both
                        directions, or in one direction, from crossing. [[CN-6.1.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which means crossing is
                        permitted, but the rule for lane lines does not explicitly govern lane changes in this
                        context, so it is allowed.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid yellow line, which
                        prohibits crossing according to [CN-6.1.1].
Step 6  go_straight     allowed (contested, correct): The lane has no arrow, and the boundaries do not
                        prohibit going straight, so it is allowed.
Step 6  turn_left       not_applicable: The lane has no arrow and no waiting area, so it is not applicable.
Step 6  turn_right      not_applicable: The lane has no arrow and no prohibited-movement marking, so it is not
                        applicable.
Step 6  u_turn          not_applicable: The lane has no arrow and no prohibited-movement marking, so it is not
                        applicable.
Step 6  enter_waiting_areanot_applicable: There are no markings indicating a waiting area, so it is not
                          applicable.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and all
                        actions are governed by the observed features and rules.
Advice                  You are in the middle lane, and you may change left, but changing right is prohibited
                        by the solid yellow line. You may proceed straight ahead, but you must stop at the
                        solid white stop line before proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 1075, 8.08 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, the
                        road continues into a built-up area with street signs visible. (lanes 3, mine 1, full)
Step 2  Left            Photo 1: A yellow line is visible to the left of my car, near the bottom. Photo 2: A
                        yellow line is visible to the left of my car, near the bottom.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1: A white line is visible to the right of my car, near the bottom. Photo 2: A
                        white line is visible to the right of my car, near the bottom.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1: No specific markings like arrows, words, or
                        areas are visible directly in my lane in the immediate foreground. Photo 2: No
                        specific markings like arrows, words, or areas are visible directly in my lane in the
                        immediate foreground.
Step 4  Cross-check     close_up: the same in both photos | position: The left boundary is a center_line
                        (yellow), and the right boundary is a lane_line (white). Since there are three lanes
                        visible, and the left boundary is a center_line, my lane (index 1) is the leftmost
                        lane of my direction. This is consistent. | roles: The left boundary is yellow and
                        dashed, consistent with a center_line separating opposing traffic. The right boundary
                        is white and dashed, consistent with a lane_line separating lanes in the same
                        direction. | markings: No markings were listed in the lane, so this check is vacuously
                        true. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: Vehicles on the solid side may not cross, but vehicles on the broken
                        side may cross, and a vehicle crossing the line must give way to vehicles travelling
                        normally. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and vehicles may change lanes where
                        this line is present. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed yellow center_line, which
                        permits crossing when safe, as per [CN-6.1.3].
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, which permits crossing as per [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: No arrow prohibits going straight, and the
                        boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed against a prohibition.
Advice                  You are in the leftmost lane of three. You may change left or right, and you may
                        proceed straight ahead. Since there are no specific turn arrows, you may proceed
                        straight, but be aware of the lane markings for potential lane changes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 1004, 8.13 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with trees lining the sides. Ahead, there is a
                        junction or intersection where the road continues. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line next to my car, and Photo 2 shows a yellow line next to my
                        car. Further ahead, Photo 1 shows a yellow line continuing, and Photo 2 shows a yellow
                        line continuing.
                        yellow dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line next to my car, and Photo 2 shows a white line next to my
                        car. Further ahead, Photo 1 shows a white line continuing, and Photo 2 shows a white
                        line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 2, and no
                        markings are visible in my lane in Photo 1.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is edge_line, right boundary is
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow dashed edge_line on left, white dashed lane_line on right) | markings: no
                        markings were observed in my lane, so they agree with each other and with the
                        boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed edge_line, and [CN-5.4.6]
                        permits broken edge lines where roadside parking is allowed, implying lane changes are
                        generally permitted where the line is broken.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed lane_line,
                        and [CN-5.2.3] permits crossing a broken lane line where vehicles may change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: No arrow or prohibited-movement marking in my
                        lane restricts carrying on straight along my lane, and the boundaries do not govern
                        it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you are permitted to change left or right, as well as
                        proceed straight ahead. Since no specific turn arrows are present, you may proceed
                        straight, but you should be aware of the intersection ahead.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8454, out 946, 7.67 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there appears to be a
                        continuation of the road, possibly leading to an intersection or a change in road
                        configuration. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows the white dashed line continuing. Photo 2
                        shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Further ahead, Photo 1 shows the white dashed line continuing. Photo 2
                        shows the white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes in the same
                        direction) | roles: the color (white) and pattern (dashed) of both boundaries fit the
                        role of a lane_line | markings: there are no markings in my lane to check against
                        boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right, and you may proceed straight ahead. No specific turn or
                        waiting area markings govern your movements.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 818, 5.7 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road approaching an intersection. There are multiple lanes
                        visible in my direction of travel near the bottom of the photo. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line continuing. Photo 2 shows a
                        solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car. Photo 2 shows a solid yellow line
                        next to my car. Further ahead, Photo 1 shows a solid yellow line continuing. Photo 2
                        shows a solid yellow line continuing.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles: the left boundary is a lane_line (separating from
                        lane 1), and the right boundary is a center_line (separating from lane 3/opposite
                        traffic). | roles: The left boundary is a white solid lane_line, and the right
                        boundary is a yellow solid center_line, which fits the roles. | markings: The single
                        arrow in my lane shows a right turn, which is consistent with the lane markings. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a solid white lane_line
                        and [CN-6.2.1] prohibits crossing the solid-line side.
Step 6  change_right    prohibited (correct): prohibited, because the right boundary is a solid yellow
                        center_line and [CN-6.1.1] prohibits crossing.
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited, because the lane marking
                        (arrow:straight_right) does not show straight ahead, and [CN-5.13.1] dictates the
                        direction of travel.
Step 6  turn_left       prohibited (correct): prohibited, because the lane marking (arrow:straight_right) does
                        not show a left turn, and [CN-5.13.1] dictates the direction of travel.
Step 6  turn_right      allowed (correct): allowed, because the lane marking (arrow:straight_right) shows a
                        right turn, and [CN-5.13.1] indicates the allowed direction of travel.
Step 6  u_turn          prohibited (correct): prohibited, because the lane marking (arrow:straight_right) does
                        not show a U-turn, and [CN-5.13.1] dictates the direction of travel.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane to execute a right turn. Lane changes are
                        prohibited by the solid lines on both sides, and you are restricted to turning right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight prohibited although an arrow shows it']
Tokens                  in 8454, out 1137, 8.33 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway road, and ahead there is an overpass/bridge structure.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A broken white line is visible next to my car. Further ahead, the line
                        appears to be a broken white line continuing towards the overpass. Photo 2: A broken
                        white line is visible next to my car. Further ahead, the line continues as a broken
                        white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to my car. Further ahead, the line
                        appears to be a solid yellow line continuing towards the overpass. Photo 2: A solid
                        yellow line is visible next to my car. Further ahead, the line continues as a solid
                        yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible across the lane
                        ahead, indicating the lane boundary continues. This is the left boundary.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left. The left boundary is a lane_line (white dashed) and the right
                        boundary is a center_line (yellow solid), which is consistent with my lane being the
                        middle lane. | roles: The left boundary is a white dashed lane_line, and the right
                        boundary is a solid yellow center_line, which fits the roles assigned. | markings: The
                        only marking observed is a line that appears to be a stop line on the left boundary in
                        Photo 2, which is consistent with the lane boundary continuing ahead. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The no-crossing centre line has three forms: double solid yellow,
                        broken-solid yellow and single solid yellow, and it prohibits vehicles in both
                        directions, or in one direction, from crossing. [[CN-6.1.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken white lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited, as the right boundary is a solid yellow
                        center_line, and [CN-6.1.1] prohibits crossing this line.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane governing this action.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane governing this action.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight or change left. Changing
                        right is prohibited by the solid yellow center line. Proceed straight or change left
                        as needed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 1164, 8.71 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with a bridge ahead, and my car is in one of the lanes near
                        the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the bridge. Photo 2: A white
                        dashed line is visible next to my car. Further ahead, the line is a white dashed line
                        continuing towards the bridge.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the bridge. Photo 2: A white
                        dashed line is visible next to my car. Further ahead, the line is a white dashed line
                        continuing towards the bridge.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction) | roles: the color (white) and pattern
                        (dashed) of both boundaries fit the role of lane_line | markings: there are no
                        markings in my lane to check against the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific turn markings, you may proceed straight, but be aware of surrounding
                        traffic when changing lanes.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 832, 6.57 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection visible in the distance.
                        My car is in the lane closest to the left side of the visible lanes. (lanes 3, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to my car. Photo 2 shows a solid white line next
                        to my car. Further ahead, Photo 1 shows a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car. Photo 2 shows a broken white line
                        next to my car. Further ahead, Photo 1 shows a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        lane line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the lane line.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            left_boundary: The no-crossing lane line is placed on sections where crossing must be
                        prohibited, and vehicles on the solid-line side may not cross. [[CN-6.2.2]]
Step 5  Rule            right_boundary: On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes. [[CN-5.2.3]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited due to the solid white line on the left
                        boundary and [CN-6.2.1] which prohibits crossing from the solid-line side.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the broken white line on the right
                        boundary allows crossing, as per [CN-5.2.1-2] and [CN-5.2.3].
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to govern
                        turning movements.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to govern
                        U-turn movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane to govern
                          entering a waiting area.
Step 7  Reflect         consistent
Advice                  You may change right into the adjacent lane, and you may proceed straight ahead.
                        Turning movements are not governed by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 8454, out 880, 7.76 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an overpass/bridge structure. My car is
                        in one of the lanes near the bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the line appears to continue as a white
                        dashed line. Further ahead, the line appears to continue as a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, the line appears to continue as a solid white
                        line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            left_boundary: A broken line means it may be crossed. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited, and may be crossed
                        in an emergency when it is safe. [[CN-4.2.2-a]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a broken white line,
                        and [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white line, and
                        [CN-4.2.2-a] prohibits crossing a solid line unless in an emergency.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to restrict
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane of two lanes traveling in the same direction. You may change
                        left, but changing right is prohibited by the solid white line. You may proceed
                        straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 8454, out 885, 7.26 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely a bridge or overpass, leading towards an
                        intersection ahead. My car is in one of the lanes near the bottom of the photo. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to my car, and further ahead, it appears to be
                        a white broken line. Photo 2 shows a white broken line next to my car, and further
                        ahead, it appears to be a white broken line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to my car, and further ahead, it appears to be
                        a white broken line. Photo 2 shows a white broken line next to my car, and further
                        ahead, it appears to be a white broken line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 2 shows a white arrow pointing left in my lane,
                        further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: The color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: The arrows (straight ahead and
                        left) are present in my lane and are consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates straight ahead or right. [[CN-5.13.1]]
Step 5  Rule            arrow:left: Guide arrows indicate the direction of travel for vehicles, and this arrow
                        indicates a left turn. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a dashed white lane_line, and
                        the arrow in my lane does not permit a lane change to the left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, and the arrow in my lane permits movement to the right (straight or right).
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The arrow in my lane shows straight ahead,
                        and the boundaries do not prohibit going straight.
Step 6  turn_left       allowed (WRONG, label prohibited): allowed: The arrow in my lane shows a left turn,
                        and the boundaries do not prohibit turning left.
Step 6  turn_right      allowed (correct): allowed: The arrow in my lane shows straight or right, and the
                        boundaries do not prohibit turning right.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight, turn left, or turn right, and you may change lanes to the
                        right. Do not attempt to change lanes to the left or make a U-turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight_right'], missed ['arrow:right', 'line:stop_line']),
                        actions False, unsafe ['change_right', 'go_straight', 'turn_left'], citation accepted,
                        contradictions ['change_left prohibited across a broken lane line']
Tokens                  in 8454, out 1195, 7.19 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A dashed white line is visible ahead of the car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left_boundary is a lane_line, right_boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the line:stop_line is consistent with the lane markings | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        lane_line, and crossing a solid lane line is prohibited by [CN-6.2.1].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        edge_line, and crossing an edge line is prohibited by [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting to turn left or
                          right ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may proceed straight ahead. Lane changes are
                        prohibited by the solid lines on both sides, and there are no markings to indicate
                        specific turning movements.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 846, 3.86 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues into the distance, possibly towards an interchange or another section of the
                        highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2; text:speed_limit (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes in the same
                        direction) | roles: the color (white) and pattern (dashed) of both boundaries fit the
                        role of a lane_line | markings: the speed limit markings are consistent with the lane
                        markings and boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            text:speed_limit: Pavement speed limit markings show the speed limit of a lane and are
                        placed at the start of the lane and at other suitable places where the maximum speed
                        is limited. [[CN-5.14.2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.3]
                        permits lane changes on sections where crossable lane lines are used.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and [CN-5.2.3] permits lane changes on sections where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is currently marked for 60 km/h. You may change
                        lanes left or right as the dashed lines permit, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 8454, out 923, 6.51 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road. Ahead, the road continues straight, and
                        there is a bus lane/shoulder area to the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A broken white line is visible next to the car. Photo 2: A broken white line
                        is visible next to the car. Further ahead, the broken white line continues. Further
                        ahead, the broken white line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to the car. Photo 2: A solid yellow line
                        is visible next to the car. Further ahead, the solid yellow line continues. Further
                        ahead, the solid yellow line continues.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 2: A solid yellow line is visible immediately to
                        the right of the lane, which acts as a boundary. This is not a marking within the
                        lane.; line:stop_yield (insufficient): Photo 2: A solid yellow line is visible
                        immediately to the right of the lane, which acts as a boundary. This is not a marking
                        within the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed for lane_line, yellow solid for edge_line) | markings: no markings were
                        found within the lane to contradict the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white lane_line, which
                        permits lane changes according to [CN-5.2.3].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid yellow
                        edge_line, which prohibits crossing according to [CN-6.1.1] (interpreted as a no-
                        crossing line for the edge).
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted U-turn or prohibited U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          the lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to proceed straight ahead. Lane changes
                        to the left are permitted, but changing to the right is prohibited by the solid yellow
                        line. Be aware of the solid yellow line on your right, which suggests a boundary that
                        should not be crossed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 8454, out 1036, 7.96 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight, with a directional sign visible in the distance. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, Photo 1 shows a white dashed line
                        continuing. Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, Photo 1 shows a white dashed line
                        continuing. Photo 2 shows a white dashed line continuing.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes in the same
                        direction) | roles: the white dashed lines fit the role of lane_line separating
                        traffic in the same direction | markings: no markings were observed in the lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict carrying on straight along
                        my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway. You may change lanes to the left
                        or right, and you may proceed straight ahead. No specific lane usage is mandated for
                        turning or waiting.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 815, 6.56 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with traffic moving away from the camera.
                        Ahead, the road continues straight, possibly leading to an intersection or another
                        section of the highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes
                        within the same direction of travel) | roles: the white dashed lines fit the role of
                        lane_line | markings: no markings were observed in my lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern U-turns or
                        turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane road. You may change lanes left or right,
                        and you may proceed straight ahead. No specific lane usage is mandated by the markings
                        visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 802, 5.39 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight into the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white lane
                        line, and [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern a left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern a right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. No specific
                        lane usage is mandated by the markings visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 8454, out 693, 5.46 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road. Ahead, the road continues under an
                        overpass structure, suggesting a continuation of the current road segment rather than
                        an immediate intersection or ramp end. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line near the car, and Photo 2 shows a solid yellow line
                        near the car. Further ahead, Photo 1 shows the solid yellow line continuing, and Photo
                        2 shows the solid yellow line continuing.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line near the car, and Photo 2 shows a white line near the car.
                        Further ahead, Photo 1 shows the white line continuing, and Photo 2 shows the white
                        line continuing.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 1 or
                        Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is
                        an edge_line). | roles: the color and pattern of the boundaries fit the roles (yellow
                        solid for center_line, white solid for edge_line). | markings: no markings were
                        listed, so there is no agreement to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): allowed: The left boundary is a solid yellow center_line, and
                        [CN-4.2.2-a] permits crossing a broken line, but since this is solid, it is prohibited
                        unless in an emergency.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, and
                        [CN-5.4.2] permits edge lines to be solid, but no rule explicitly prohibits changing
                        into the adjacent lane based on this solid edge line alone, though it is generally
                        restricted by the nature of an edge line.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict carrying on straight along
                        my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No waiting area or two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You may proceed straight ahead. Changing right
                        into the adjacent lane is allowed, but changing left is prohibited by the solid yellow
                        center line. No specific stopping or turning maneuvers are marked for your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 942, 7.83 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues into the distance without an immediate intersection or lane end visible in
                        the close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines on both sides indicate lanes
                        within the same direction of travel) | roles: the white dashed lines fit the role of
                        lane_line | markings: no markings were observed in the lane | unseen: no attributes
                        were reported that were not seen | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: No markings restrict carrying on straight along
                        my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes left or right as the lane lines are broken, and you may proceed straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 8454, out 820, 6.45 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues straight into the distance without an immediate intersection or ramp
                        visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car, and a dashed white line further
                        ahead. Photo 2 shows a dashed white line next to my car, and a dashed white line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and a solid white line further ahead.
                        Photo 2 shows a solid white line next to my car, and a solid white line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundary roles: the left boundary is a lane_line separating my lane
                        from the left lane, and the right boundary is an edge_line marking the right edge of
                        the roadway. | roles: The left boundary (dashed white line) fits the role of a
                        lane_line, and the right boundary (solid white line) fits the role of an edge_line. |
                        markings: The stop line is located in my lane, and it is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed white line, which
                        means it may be crossed [CN-4.2.2-a].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white line, which means crossing is normally prohibited [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         The actions are consistent with the boundaries and markings settled in the close-up
                        check, and no rule prohibits an allowed action.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid white
                        edge line. You may proceed straight ahead, but you must stop at the stop line before
                        proceeding.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 1119, 8.2 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues into the distance without an immediate intersection or ramp visible. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (white dashed lines separating lanes in the same
                        direction) | roles: the color and pattern of both boundaries fit the role of a
                        lane_line | markings: there are no markings in my lane to check against boundaries |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane to govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane to govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane to govern U-turns or
                        turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane to govern entering
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway. You may change lanes to the left
                        or right, and you may proceed straight ahead. No specific lane usage is mandated by
                        the markings visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 8454, out 803, 5.78 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with guardrails on both sides, and it appears to be a
                        straight stretch of road ahead, not an intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: the stop_line marking is
                        consistent with the lane configuration. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white
                        lane_line, and [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in my lane,
                        and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a multi-lane highway, and you may change lanes left or
                        right, or proceed straight. You must stop at the visible stop line before proceeding.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 1035, 7.38 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving in the same direction. Ahead, the
                        road continues, possibly leading to an interchange or another section of the highway.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white dashed line marking the right
                        edge of the lane, and a white dashed line marking the left edge of the lane. Photo 2
                        shows the same white dashed lines.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: The color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: The lane
                        markings are minimal and do not contradict the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted as the lane lines are
                        dashed. You may proceed straight, but turning movements are not explicitly governed by
                        markings in this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 1092, 6.9 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection where the
                        road continues and potentially merges or changes lanes. My car is in one of the lanes
                        near the bottom of the photo. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line next to my car, and further ahead, it appears to be
                        a white broken line. Photo 2 shows a white broken line next to my car, and further
                        ahead, it appears to be a white broken line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to my car, and further ahead, it appears to be
                        a white broken line. Photo 2 shows a white broken line next to my car, and further
                        ahead, it appears to be a white broken line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2 shows a white dashed line across the lane,
                        which is the right boundary line, but no specific arrow or word is visible within my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction) | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of lane_line | markings: the markings observed (a dashed line)
                        are consistent with the boundaries, although the specific marking 'line:stop_line' is
                        not clearly visible as a distinct feature within the lane itself, but rather as a
                        feature of the boundary line in Photo 2. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane line, which
                        permits crossing according to [CN-5.2.1-2].
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane line, which
                        permits crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries permit lane changes if needed, which does not
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right as the lane lines are broken. You may proceed
                        straight ahead. No specific turn or waiting area markings govern your movements.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 8454, out 966, 6.79 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with traffic moving away from the camera.
                        Ahead, the road continues straight, and there are no immediate intersections or ramps
                        visible in the close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line, and Photo 2
                        shows a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Further ahead, Photo 1 shows a white dashed line, and Photo 2
                        shows a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes of the same direction). | roles: The color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: The grid
                        marking is located within my lane and is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            area:grid: The grid marking shows an area where stopping for any reason is prohibited.
                        [[CN-6.8.1-2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a dashed white lane_line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed, as the right boundary is a dashed white
                        lane_line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in my
                        lane, and boundaries do not govern going straight.
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane.
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane.
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The boundaries and markings were settled in the close-up check, no action was allowed
                        against a prohibition, no action was decided without a governing feature, no action
                        was decided by a marking that does not govern it, and each reason leads to its action.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Be aware that
                        the area marked with a grid in your lane prohibits stopping for any reason.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed ['text:speed_limit']), actions False, unsafe ['change_right'],
                        citation accepted, contradictions []
Tokens                  in 8454, out 1115, 7.91 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the lane closest
                        to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A broken white line is visible next to my car. Further ahead, the line
                        appears to be a broken white line continuing towards the intersection. Photo 2: A
                        broken white line is visible next to my car. Further ahead, the line appears to be a
                        broken white line continuing towards the intersection.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid yellow line is visible next to my car. Further ahead, the line
                        appears to be a solid yellow line continuing towards the intersection. Photo 2: A
                        solid yellow line is visible next to my car. Further ahead, the line appears to be a
                        solid yellow line continuing towards the intersection.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed for lane_line, yellow solid for center_line) | markings: there are no
                        markings in my lane to check for agreement | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: A no-crossing centre line has three forms: double solid yellow,
                        broken-solid yellow and single solid yellow. It separates opposing traffic flows and
                        prohibits vehicles in both directions, or in one direction, from crossing.
                        [[CN-6.1.1]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. It is generally used on two-lane two-way roads with limited sight distance
                        or where overtaking must be prohibited. [[CN-6.1.4]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a broken white
                        line, which allows crossing according to [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid yellow
                        line, which prohibits crossing according to [CN-6.1.4].
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane to restrict
                        going straight, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but changing to the right is prohibited by the solid
                        yellow line. You may proceed straight ahead, but turning left, turning right, or
                        making a U-turn are not explicitly allowed or prohibited by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 943, 7.75 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues straight, and there are no immediate intersections or ramps visible in the
                        close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, and further ahead, it appears to be
                        a broken white line. Photo 2 shows a broken white line next to my car, and further
                        ahead, it is a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and further ahead, it is a solid
                        yellow line. Photo 2 shows a solid yellow line next to my car, and further ahead, it
                        is a solid yellow line.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a dashed white line segment in my lane, and
                        further ahead, there is a dashed white line segment.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the line:stop_line marking is consistent with the boundaries and general
                        road markings | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a broken white
                        lane_line, which permits crossing according to [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        yellow edge_line, which prohibits crossing according to [CN-6.1.1] (interpreted as a
                        general prohibition for solid lines, though the specific rule for edge lines is
                        [CN-5.4.3] which doesn't explicitly prohibit, the solid nature implies restriction).
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to proceed straight. You may change left
                        if necessary, but changing right is prohibited by the solid yellow line. You must stop
                        at the visible stop line ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 974, 6.81 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, the
                        road continues into a built-up area, and there is no immediate intersection or ramp
                        visible in the close-up. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line near the bottom left. Photo 2 shows a yellow line near the
                        bottom left.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line near the bottom right. Photo 2 shows a white line near the
                        bottom right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible within my lane in Photo 2, and
                        no markings are visible further ahead in Photo 1.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow dashed for center_line, white dashed for lane_line) | markings: no markings
                        were listed, so this check is vacuously true | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles on the broken side may cross the line, while vehicles on the
                        solid side may not cross, but this line is dashed, so the rule for broken lines
                        applies. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed yellow
                        center_line, and the rule for broken lines allows crossing.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, and the rule for broken lines allows crossing.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three lanes traveling in the same direction. You may
                        change lanes to the left or right, and you may proceed straight ahead. No specific
                        turn or waiting area markings govern your movements.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 881, 6.35 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues straight, and there is a blue directional sign indicating an entrance ramp.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A yellow dashed line separates my lane from the lane to the left. Photo 2: A
                        yellow dashed line separates my lane from the lane to the left, visible near the
                        bottom of the close-up.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line marks the right edge of my lane. Photo 2: A solid white
                        line marks the right edge of my lane, visible near the bottom of the close-up.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2: A solid yellow line is visible near the bottom of
                        the close-up, separating my lane from the lane to the left.; line:stop_yield
                        (partial): Photo 2: A solid yellow line is visible near the bottom of the close-up,
                        separating my lane from the lane to the left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: the markings (line:stop_yield) are consistent with the boundaries and each
                        other | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a yellow dashed line, which,
                        when combined with the stop-and-yield line, implies restrictions on crossing, and the
                        stop-and-yield line mandates stopping before proceeding.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge line, and no rule
                        prohibits changing right.
Step 6  go_straight     stop_first (contested, label allowed): stop_first: The lane contains a stop-and-yield
                        line, which mandates stopping completely before entering the intersection.
Step 6  turn_left       prohibited: prohibited: The lane contains a stop-and-yield line, which mandates
                        stopping completely before entering the intersection, and there are no markings
                        allowing a left turn.
Step 6  turn_right      prohibited: prohibited: The lane contains a stop-and-yield line, which mandates
                        stopping completely before entering the intersection, and there are no markings
                        allowing a right turn.
Step 6  u_turn          prohibited: prohibited: The lane contains a stop-and-yield line, which mandates
                        stopping completely before entering the intersection, and there are no markings
                        allowing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You must stop completely before proceeding into the intersection. You may change
                        right, but all other movements, including going straight, must be done after stopping.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['change_left prohibited across a broken lane line', 'turn_left,
                        turn_right, u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 8454, out 1002, 7.17 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, there
                        is a pedestrian crossing and a section with marked lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow dashed line next to my car, and further ahead, it appears to be
                        a yellow dashed line. Photo 2 shows a yellow dashed line next to my car, and further
                        ahead, it appears to be a yellow dashed line.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the right boundary
                        of my lane.; line:stop_line (partial): Photo 2 shows a white dashed line marking the
                        right boundary of my lane, which appears to be a stop line.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is center_line, right boundary is
                        lane_line). | roles: the yellow dashed line on the left fits the role of a
                        center_line, and the white dashed line on the right fits the role of a lane_line. |
                        markings: the stop line marking is consistent with the right boundary line in Photo 2.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles on the broken side may cross the line, while vehicles on the
                        solid side may not cross, and a vehicle crossing the line must give way to vehicles
                        travelling normally. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a dashed
                        line, which permits crossing according to [CN-6.1.3].
Step 6  change_right    allowed (contested, label prohibited): allowed because the right boundary is a dashed
                        line, which permits crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): allowed because there are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable because there are no markings
                        in my lane governing a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable because there are no markings
                        in my lane governing a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable because there are no markings
                        in my lane governing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area in my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted in both directions as the
                        boundaries are dashed. You may proceed straight, but you must stop before the marked
                        stop line ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 952, 6.62 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection where the road continues and potentially merges/splits. My car is in one
                        of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car, and further ahead, it appears to be
                        a dashed white line. Photo 2 shows a dashed white line next to my car, and further
                        ahead, it appears to be a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and further ahead, it appears to be
                        a solid yellow line. Photo 2 shows a solid yellow line next to my car, and further
                        ahead, it appears to be a solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 2 shows a yellow hatched area with diagonal lines
                        across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        center_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed for lane_line, yellow solid for center_line) | markings: the
                        channelizing area is ahead of the lane and does not contradict the boundaries or lane
                        structure | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The no-crossing centre line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            area:channelizing: Channelizing lines show that vehicles must follow the set path and
                        may not drive on or across the lines. [[CN-6.6.1-3]]
Step 6  change_left     allowed (contested, correct): allowed: The left boundary is a dashed white lane_line,
                        and [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid yellow
                        center_line, and [CN-6.1.1] prohibits crossing this line in both directions.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane that govern turning movements.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane that govern turning movements.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane that govern turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or a two-
                          way left-turn lane in view.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight. You may change left if
                        necessary, but changing right is prohibited by the solid yellow line. Be aware of the
                        channelizing markings ahead, which require you to follow the designated path.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 949, 7.78 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection or a point where the
                        road configuration changes, as indicated by the markings. My car is in one of the
                        lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, and further ahead, it appears to be
                        a broken white line. Photo 2 shows a broken white line next to my car, and further
                        ahead, it appears to be a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line next to my car, and further ahead,
                        it appears to be a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a broken white
                        line, which means it may be crossed [CN-5.2.1-2].
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white line, but since no
                        specific rule prohibits crossing a solid edge line, and it is not a no-crossing lane
                        line, it is allowed as per general permissive nature of edge lines unless otherwise
                        restricted.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight [no marking governs this action].
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane that allow or
                        prohibit turning left [not_applicable].
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane that allow or
                        prohibit turning right [not_applicable].
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane that allow or
                        prohibit U-turns [not_applicable].
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane [not_applicable].
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to proceed straight. You may change lanes
                        to the left or right as the lane line is broken, but be aware that the right boundary
                        is a solid edge line. No specific turning movements are indicated or restricted in
                        your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 931, 6.54 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a suburban or urban area, and ahead there is a bus stop
                        or a section where traffic flow is managed, possibly leading to an intersection or a
                        designated stopping area. My car is in the rightmost lane visible in the direction of
                        travel. (lanes 3, mine 3, full)
Step 2  Left            Photo 1: A white dashed line separates my lane from the adjacent lane to the left.
                        Photo 2: A white dashed line separates my lane from the adjacent lane to the left,
                        visible just ahead of the car. The line further ahead is also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line marks the right edge of the roadway. Photo 2: A solid
                        white line marks the right edge of the roadway, visible just ahead of the car. The
                        line further ahead is also a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 1: A white dashed line is visible in the lane,
                        indicating lane separation. Photo 2: A white dashed line is visible in the lane,
                        indicating lane separation.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (3) agree with the boundary roles: the left boundary is a lane_line, and the right
                        boundary is an edge_line, consistent with my car being in the rightmost lane. | roles:
                        The white dashed line on the left fits the role of a lane_line, and the solid white
                        line on the right fits the role of an edge_line. | markings: The visible marking
                        (line:stop_yield) is present in both photos and is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: Vehicles shall stop completely before entering the intersection and
                        may proceed only after making sure it is safe. [[CN-6.5.1.1-2]]
Step 6  change_left     allowed (correct): prohibited: The left boundary is a white dashed lane_line, and
                        while [CN-4.2.2-a] allows crossing a broken line, the presence of the stop_yield line
                        ahead suggests caution, but the primary restriction is the lane line itself, which
                        allows crossing if safe, but the stop_yield line governs movement at the end of the
                        lane.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white solid edge_line, and
                        [CN-4.2.2-a] implies that crossing a solid line is normally prohibited, but since this
                        is an edge line, the rule for edge lines is less restrictive for changing into a
                        shoulder/edge, and no specific prohibition is given for changing right into the edge.
Step 6  go_straight     stop_first (WRONG, label allowed): stop_first: The lane contains a line:stop_yield
                        marking, which mandates that vehicles shall stop completely before entering the
                        intersection and may proceed only after making sure it is safe.
Step 6  turn_left       prohibited (correct): prohibited: There are no markings indicating a permitted left
                        turn in this lane.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted right turn in this lane.
Step 6  u_turn          prohibited (correct): prohibited: There are no markings indicating a permitted U-turn
                        in this lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a left-turn waiting
                          area or a two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, and you must stop completely before proceeding due to
                        the stop-and-yield line. Lane changes are permitted based on the markings, but you
                        should plan to stop before proceeding straight.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed ['arrow:straight']), actions False, unsafe [], citation
                        accepted, contradictions ['turn_left, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 8454, out 1112, 11.19 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in the same direction. Ahead, the
                        road continues into a more complex intersection area. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a yellow broken line next to my car, and a yellow broken line further
                        ahead. Photo 2 shows a yellow broken line next to my car, and a yellow broken line
                        further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and a white dashed line further
                        ahead. Photo 2 shows a white dashed line next to my car, and a white dashed line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it
                        (yellow dashed for center_line, white dashed for lane_line) | markings: the stop_line
                        marking agrees with the boundaries (it is located at the end of the lane) | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: Vehicles on the broken side may cross the line, while vehicles on the
                        solid side may not cross. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a yellow
                        dashed line, which permits crossing from the broken side [CN-6.1.3].
Step 6  change_right    allowed (correct): allowed because the right boundary is a white dashed line, which
                        permits crossing [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibitions in
                        my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. You must stop
                        at the solid white stop line before proceeding.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 1082, 7.79 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is an intersection where traffic
                        appears to be moving through or approaching a crossing area. My car is in one of the
                        lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the intersection. Photo 2: A
                        white dashed line is visible next to my car. Further ahead, the line appears to be a
                        white dashed line continuing towards the intersection.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the intersection. Photo 2: A
                        white dashed line is visible next to my car. Further ahead, the line appears to be a
                        white dashed line continuing towards the intersection.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2: A white dashed line is visible across the lane
                        ahead, indicating a lane division or boundary change further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: the visible
                        white dashed line ahead is interpreted as a stop line, which is consistent with the
                        lane markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed: allowed: The left boundary is a dashed white lane_line, and [CN-5.2.3]
                        permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed: allowed: The right boundary is a dashed white lane_line, and [CN-5.2.3]
                        permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right as the lane lines are broken. You may proceed
                        straight through the intersection, but you must stop before the marked stop line.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 970, 10.09 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a suburban or urban area, and ahead there is a road
                        section continuing forward, possibly leading to an intersection or another road
                        segment. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line next to my car, and Photo 2 shows a yellow line next to my
                        car. Further ahead, Photo 1 shows a solid white line marking the boundary of the lane
                        to the left, and Photo 2 shows this solid white line.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Further ahead, Photo 1 shows a solid white line continuing, and Photo
                        2 shows this solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2 shows a solid yellow line painted on the road
                        surface immediately to the left of my lane, which is the boundary line.;
                        line:stop_yield (partial): Photo 2 shows a solid white line painted on the road
                        surface immediately to the right of my lane, which is the boundary line.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is
                        an edge_line). | roles: the yellow dashed line on the left fits the role of a
                        center_line separating opposing traffic, and the solid white line on the right fits
                        the role of an edge_line. | markings: the markings listed are actually the boundary
                        lines themselves, not internal markings like arrows or text, but they are interpreted
                        as stop_yield lines based on the visual representation of solid lines near the lane
                        edge in Photo 2, which is a potential misinterpretation of the boundary line type;
                        however, the boundary lines are solid/dashed, not the stop_yield line structure (two
                        parallel solid lines with '停'). I will correct the markings to reflect the boundary
                        lines as they are the primary features governing movement. | unseen: no | result:
                        corrected
Step 5  Rule            left_boundary: Vehicles on the solid side may not cross, while vehicles on the broken
                        side may cross, and a vehicle crossing the line must give way to vehicles travelling
                        normally. [[CN-6.1.3]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: Vehicles shall stop completely before entering the intersection and
                        may proceed only after making sure it is safe. [[CN-6.5.1.1-2]]
Step 6  change_left     allowed (contested, label prohibited): prohibited: The left boundary is a yellow
                        dashed line, which, when interpreted as a center line, allows crossing from the broken
                        side, but the presence of a stop_yield line (interpreted from the boundary) suggests
                        caution, and the general rule for center lines allows crossing if safe, but the
                        stop_yield line takes precedence.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge line, and there
                        is no rule prohibiting crossing the edge line to the right.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked areas for waiting ahead of my
                          lane or a two-way left-turn lane directly to its left.
Step 7  Reflect         The boundaries and markings are consistent with the close-up view, and the actions are
                        derived from the interpreted rules, although the initial interpretation of the
                        boundary lines as stop_yield markings was corrected to reflect their actual role as
                        lane boundaries.
Advice                  You are in the middle lane, which allows you to proceed straight or change lanes to
                        the right. Be aware of the yellow dashed line on your left, which separates opposing
                        traffic, and the solid white edge line on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 8454, out 1182, 10.06 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection where the road continues and potentially merges/divides. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a solid white line next to my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line next to my car, and further ahead,
                        it appears to be a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and further ahead, it appears to be
                        a solid yellow line. Photo 2 shows a solid yellow line next to my car, and further
                        ahead, it appears to be a solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2 shows a solid yellow line marking the right
                        boundary, which acts as a center line.; line:yield_line (partial): Photo 2 shows
                        yellow markings ahead of my car, which appear to be part of a yield/stop area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        2nd from the left, which is consistent with having a lane line on the left and a
                        center line on the right. | roles: The left boundary is a solid white lane_line, and
                        the right boundary is a solid yellow center_line, which fits the roles. | markings:
                        The markings observed (solid yellow line/yield area) are consistent with the
                        boundaries and general road markings. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            line:stop_yield: Vehicles shall stop completely before entering the intersection and
                        may proceed only after making sure it is safe. [[CN-6.5.1.1-2]]
Step 5  Rule            line:yield_line: Vehicles shall slow down or stop before entering the intersection and
                        may proceed only after making sure it is safe. [[CN-6.5.2.1-2]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white
                        lane_line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid yellow
                        center_line, and [CN-6.1.1] prohibits vehicles from crossing.
Step 6  go_straight     stop_first (contested, label allowed): stop_first: The lane contains a line:stop_yield
                        marking, which turns all allowed movements into stop_first.
Step 6  turn_left       stop_first: stop_first: The lane contains a line:stop_yield marking, which turns all
                        allowed movements into stop_first.
Step 6  turn_right      stop_first: stop_first: The lane contains a line:stop_yield marking, which turns all
                        allowed movements into stop_first.
Step 6  u_turn          stop_first: stop_first: The lane contains a line:stop_yield marking, which turns all
                        allowed movements into stop_first.
Step 6  enter_waiting_areanot_applicable: not_applicable: No markings for a waiting area were observed in my
                          lane.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before proceeding into the intersection. Lane changes
                        are prohibited due to solid lines on both sides. Proceeding straight, turning left,
                        turning right, or making a U-turn is only permitted after stopping safely.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield', 'line:yield_line'], missed []), actions None, unsafe [], citation
                        accepted, contradictions ['turn_left, turn_right, u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 8454, out 1059, 7.92 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road. Ahead, the road continues straight,
                        with traffic visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, the solid white line continues. Photo 2 shows
                        the line further ahead is also solid white.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, the solid white line continues.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        middle lane (index 2). The left boundary is a lane_line, and the right boundary is an
                        edge_line, which is consistent with my lane being the middle lane. | roles: The left
                        boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The stop line is located ahead in my
                        lane, which is consistent with the lane boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid-line side may not cross the no-crossing lane
                        line. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white
                        lane_line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid white
                        edge_line, and [CN-4.2.2-a] implies that a solid line means crossing is normally
                        prohibited.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane next to it.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid lines on both sides, and there are no markings to indicate
                        turning or waiting areas.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 909, 6.25 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, there is a
                        junction or a section where lane guidance is present. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car. Photo 2 shows a broken white line
                        next to my car. Photo 1 shows a solid white line further ahead. Photo 2 shows a solid
                        white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car. Photo 2 shows a solid yellow line
                        next to my car. Photo 1 shows a solid yellow line further ahead. Photo 2 shows a solid
                        yellow line further ahead.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2; area:two_way_left_turn_lane (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        second from the left (ego_lane_index=2). The left boundary is a lane_line (white,
                        dashed) separating it from the leftmost lane, and the right boundary is an edge_line
                        (yellow, solid) separating it from the rightmost lane/shoulder area. This is
                        consistent. | roles: The left boundary is a white dashed lane_line, which fits the
                        role of separating lanes in the same direction. The right boundary is a solid yellow
                        edge_line, which fits the role of marking the edge of the roadway. | markings: The
                        arrow in my lane shows straight or right movement. The area marking indicates a two-
                        way left-turn lane directly to the left. This is consistent with the lane markings. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow in my lane shows straight or right movement. [[CN-5.13.1]]
Step 5  Rule            area:two_way_left_turn_lane: The left-turn waiting area line marks an area that left-
                        turning vehicles may enter in advance to wait for the left turn. [[CN-5.5.1-3]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a lane_line,
                        and the arrow in my lane does not show a left turn.
Step 6  change_right    allowed (correct): allowed, because the right boundary is an edge_line, and the arrow
                        in my lane shows straight or right movement.
Step 6  go_straight     allowed (correct): allowed, because the arrow in my lane shows straight or right
                        movement.
Step 6  turn_left       prohibited (correct): prohibited, because the arrow in my lane does not show a left
                        turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed, because the arrow in my lane shows
                        straight or right movement.
Step 6  u_turn          prohibited (correct): prohibited, because the arrow in my lane does not show a U-turn.
Step 6  enter_waiting_areaallowed: allowed, because the area:two_way_left_turn_lane marking is present and
                          allows entry to wait for a left turn.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight or turning right, and you may
                        enter the adjacent two-way left-turn lane to wait for a left turn. Lane changes to the
                        left are prohibited by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane', 'arrow:straight_right'], missed ['arrow:straight']),
                        actions False, unsafe ['turn_right'], citation accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 8454, out 1282, 9.94 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection or a section where lane
                        configuration changes, with a bridge visible ahead. There are multiple lanes in my
                        direction near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and further ahead, it appears to be
                        a white dashed line. Photo 2 shows a white dashed line next to my car, and further
                        ahead, it appears to be a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating my lane
                        is between two other lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of a lane_line. | markings: the white
                        arrow in my lane is consistent with the lane markings. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead and right. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a dashed white
                        lane_line, and the rule [CN-5.2.1-2] implies that while lane changes are possible, the
                        arrow in my lane restricts movement.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane_line, and the
                        rule [CN-5.2.1-2] permits lane changes where the line is broken.
Step 6  go_straight     allowed (correct): allowed: The arrow in my lane shows straight ahead, and the rule
                        [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in my lane does not show a left turn, and
                        the rule [CN-5.13.1] restricts movement to what is shown.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in my lane shows straight or
                        right, and the rule [CN-5.13.1] indicates the direction of travel.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane does not show a U-turn, and the
                        rule [CN-5.13.1] restricts movement to what is shown.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight or turn right, and you may
                        change right. You should proceed straight or turn right at the intersection ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight']), actions False, unsafe
                        ['turn_right'], citation accepted, contradictions ['change_left prohibited across a
                        broken lane line']
Tokens                  in 8454, out 995, 6.48 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, there is an
                        intersection where traffic lanes appear to diverge or change. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A broken white line is visible next to the car. Photo 2: A broken white line
                        is visible next to the car. Further ahead, Photo 1 shows a solid white line marking
                        the edge of the lane structure. Photo 2 shows a solid white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, Photo 1 shows a solid white line continuing to
                        mark the edge of the road. Photo 2 shows a solid white line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1: A white arrow pointing straight ahead is visible
                        in the lane. Photo 2: A white arrow pointing straight ahead is visible in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego lane index
                        (2) agree with the boundaries: the left boundary is a lane line separating it from the
                        left lane, and the right boundary is an edge line separating it from the right
                        lane/shoulder. | roles: The left boundary is a broken white lane line, and the right
                        boundary is a solid white edge line, which fits their roles. | markings: The straight-
                        ahead arrow is present in the lane and is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        in this case, it indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a broken white lane line, and
                        the rule [CN-5.2.1-2] allows lane changes, but the arrow only permits straight ahead,
                        which implies no lane change is intended or allowed by the arrow's restriction.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid white edge
                        line, and the rule [CN-5.4.1] defines this as the edge of the roadway, which does not
                        prohibit lane changes unless other markings do.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking is a white arrow pointing
                        straight ahead, and the rule [CN-5.13.1] indicates this direction of travel is
                        permitted.
Step 6  turn_left       prohibited: prohibited: The lane marking is a white arrow pointing straight ahead, and
                        the rule [CN-5.13.1] indicates that movements not shown by the arrow are prohibited.
Step 6  turn_right      prohibited: prohibited: The lane marking is a white arrow pointing straight ahead, and
                        the rule [CN-5.13.1] indicates that movements not shown by the arrow are prohibited.
Step 6  u_turn          prohibited: prohibited: The lane marking is a white arrow pointing straight ahead, and
                        the rule [CN-5.13.1] indicates that movements not shown by the arrow are prohibited,
                        and there is no exception for U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of the lane.
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane. While the lane line allows
                        lane changes, the arrow restricts you to going straight, so do not attempt to change
                        lanes or turn. No specific stopping area is marked.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed ['line:stop_line']), actions False, unsafe
                        ['change_right'], citation accepted, contradictions ['change_left prohibited across a
                        broken lane line', 'turn_right prohibited although an arrow shows it']
Tokens                  in 8454, out 1102, 9.13 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection area where lane markings are present. My car is in the rightmost lane
                        visible in the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a dashed white line next to my car, and further ahead, it appears to be
                        a dashed white line. Photo 2 shows a dashed white line next to my car, and further
                        ahead, it appears to be a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to my car, and further ahead, it appears to be
                        a solid yellow line. Photo 2 shows a solid yellow line next to my car, and further
                        ahead, it appears to be a solid yellow line.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Photo 2 shows a white dashed line marking the lane boundary
                        near my car.; line:stop_line (partial): Photo 1 shows a white dashed line marking the
                        lane boundary near my car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed for lane_line, solid yellow for edge_line) | markings: the markings
                        (line:stop_line) agree with each other and with the boundaries (it is located near the
                        end of the lane) | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed white lane_line,
                        which permits crossing when safe [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        yellow edge_line, which restricts crossing [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in my lane [no marking governs this action]
Step 6  turn_left       not_applicable: not_applicable because there are no markings indicating a permitted
                        left turn [not_applicable]
Step 6  turn_right      not_applicable: not_applicable because there are no markings indicating a permitted
                        right turn [not_applicable]
Step 6  u_turn          not_applicable: not_applicable because there are no markings indicating a permitted
                        U-turn [not_applicable]
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings for a waiting area
                          [not_applicable]
Step 7  Reflect         consistent
Advice                  You may change left if safe, but changing right is prohibited by the solid yellow edge
                        line. You may proceed straight ahead, but you must stop before the visible stop line
                        if you intend to stop or yield.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8454, out 993, 7.84 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection.
                        My car is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the intersection. Photo 2: A
                        white dashed line is visible next to my car. Further ahead, the line appears to be a
                        white dashed line continuing towards the intersection.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing towards the intersection. Photo 2: A
                        white dashed line is visible next to my car. Further ahead, the line appears to be a
                        white dashed line continuing towards the intersection.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: the color (white) and
                        pattern (dashed) of both boundaries fit the role of lane_line. | markings: there are
                        no arrows, words, or areas in my lane to check against the boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white lane
                        line, and [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white lane
                        line, and [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane restricting
                        straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn or prohibited U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a left-turn waiting
                          area or a two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may change left or right if necessary. All
                        movements are generally allowed unless restricted by traffic signals or signs not
                        visible in the image.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8454, out 862, 6.45 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and there is a road ahead that
                        appears to lead into an intersection or a section where lane configuration changes.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car, and Photo 2 shows a white dashed
                        line next to my car. Photo 1 shows a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundary roles (both boundaries are lane_lines, indicating adjacent
                        lanes in the same direction). | roles: the color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: the stop_line marking is
                        consistent with the lane configuration. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a dashed white lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (correct): allowed because the right boundary is a dashed white lane_line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibitions in
                        my lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane and may change left or right, or proceed straight. You
                        must stop at the visible stop line before proceeding.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 8454, out 1083, 7.84 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection indicated by traffic
                        signals and lane markings. My car is in the rightmost lane visible in the immediate
                        foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, and further ahead, it appears to be
                        a broken white line. Photo 2 shows a broken white line next to my car, and further
                        ahead, it appears to be a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and further ahead, it appears to be a
                        solid white line. Photo 2 shows a solid white line next to my car, and further ahead,
                        it appears to be a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows white arrows pointing straight ahead and to
                        the right in my lane. Photo 1 shows the same arrows further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it
                        (white dashed line is a lane_line, white solid line is an edge_line) | markings: the
                        arrows in my lane agree with the boundaries (the arrows indicate movement within the
                        lane defined by the boundaries) | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        the arrow shown indicates straight ahead and to the right. [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, label allowed): prohibited: The left boundary is a lane_line,
                        and the arrow in my lane does not permit a change to the left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is an edge_line, and
                        the arrow in my lane permits movement to the right (as part of straight_right).
Step 6  go_straight     allowed (contested, correct): allowed: The arrow in my lane permits straight ahead
                        movement.
Step 6  turn_left       prohibited: prohibited: The arrow in my lane does not show a left turn.
Step 6  turn_right      allowed: allowed: The arrow in my lane permits a right turn.
Step 6  u_turn          prohibited: prohibited: The arrow in my lane does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is marked to allow movement straight ahead or
                        turning right. You may change right if necessary, but you must adhere to the indicated
                        directions for straight or right turns.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['text:other']), actions False, unsafe
                        ['change_right'], citation in_pack_not_accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 8454, out 929, 6.85 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving in the same direction as my car.
                        Ahead, there is an intersection where the road continues. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a yellow broken line next to my car. Photo 2 shows a yellow broken line
                        next to my car. Photo 1 shows a solid white line further ahead. Photo 2 shows a solid
                        white line further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to my car. Photo 2 shows a white dashed line
                        next to my car. Photo 1 shows a white dashed line further ahead. Photo 2 shows a white
                        dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2; arrow:straight (full): Photo 2;
                        arrow:straight_left (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: The left boundary is a center_line
                        (yellow), and the right boundary is a lane_line (white). Since my lane is the leftmost
                        lane (index 1) and the left boundary is a center_line, this is consistent with my lane
                        being the leftmost lane of my direction. The right boundary is a lane_line, indicating
                        another lane to the right, which is consistent with having 3 lanes. | roles: The left
                        boundary is yellow and dashed, consistent with a center_line that may be crossed. The
                        right boundary is white and dashed, consistent with a crossable lane_line. | markings:
                        The arrows in Photo 2 show straight ahead, straight right, and straight left. These
                        arrows are within my lane (ego_lane_index=1). The arrows indicate the allowed
                        movements for this lane. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The crossable centre line means vehicles may cross the line to
                        overtake, turn or make a U-turn when this does not affect safety. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates travel straight or to the right. [[CN-5.13.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates travel straight ahead. [[CN-5.13.1]]
Step 5  Rule            arrow:straight_left: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates travel straight or to the left. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a yellow dashed center_line,
                        and while it is crossable, the lane markings indicate specific allowed movements that
                        do not include a lane change to the left.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed
                        lane_line, and [CN-5.2.1-2] permits crossing this line when changing lanes.
Step 6  go_straight     allowed (correct): allowed: The lane markings include an arrow indicating straight
                        ahead, and [CN-5.13.1] allows this movement.
Step 6  turn_left       allowed (WRONG, label prohibited): allowed: The lane markings include an arrow
                        indicating straight or left, and [CN-5.13.1] allows this movement.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The lane markings include an arrow
                        indicating straight or right, and [CN-5.13.1] allows this movement.
Step 6  u_turn          allowed (WRONG, label prohibited): allowed: The lane markings include an arrow
                        indicating straight or left, and [CN-5.13.1] allows this movement (as it shows a turn
                        toward the opposite traffic).
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a left-turn waiting
                          area or a two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which allows you to go straight, turn left, turn right,
                        or make a U-turn, and you may change right. You may change left only if the lane
                        markings permit it, but currently, they do not explicitly allow it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_left', 'arrow:straight_right'], missed ['line:stop_line']), actions
                        False, unsafe ['change_right', 'turn_left', 'turn_right', 'u_turn'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 1433, 10.23 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where the road continues and traffic flows in multiple directions. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line next to my car, and Photo 2 shows a broken white
                        line next to my car. Photo 1 shows a solid white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and Photo 2 shows a solid white line
                        next to my car. Photo 1 shows a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2; line:stop_line (full): Photo 2;
                        area:two_way_left_turn_lane (full): Photo 2
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is a
                        lane_line, indicating I am in the middle lane of 3 lanes). | roles: the color and
                        pattern of each boundary fit the role given to it (white dashed/solid lines are
                        lane_lines). | markings: the markings agree with each other and with the boundaries
                        (the two_way_left_turn_lane is to the left of my lane, and the arrow/stop_line are in
                        my lane). | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles.
                        [[CN-5.13.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 5  Rule            area:two_way_left_turn_lane: The left-turn waiting area line marks an area that left-
                        turning vehicles may enter in advance to wait for the left turn. [[CN-5.5.1-3]]
Step 6  change_left     prohibited (correct): prohibited due to the left boundary being a lane_line and the
                        arrow only showing straight or right.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a lane_line
                        and the arrow shows straight or right.
Step 6  go_straight     allowed (correct): allowed because the arrow shows straight ahead.
Step 6  turn_left       prohibited (correct): prohibited because the arrow does not show a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed because the arrow shows straight or right.
Step 6  u_turn          prohibited (correct): prohibited because the arrow does not show a U-turn.
Step 6  enter_waiting_areaallowed: allowed because there is a two_way_left_turn_lane directly to the left of
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is marked to go straight or turn right, and you may
                        enter the left-turn waiting area. You may change right, but you cannot change left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane', 'arrow:straight_right', 'line:stop_line'], missed
                        ['arrow:straight']), actions False, unsafe ['change_right', 'turn_right'], citation
                        accepted, contradictions ['change_left prohibited across a broken lane line']
Tokens                  in 8454, out 1222, 8.46 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a two-way street lined with buildings and trees, and the road continues
                        straight ahead into the distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1: A yellow line is visible on the left side of the road, near the bottom. Photo
                        2: A yellow line is visible on the left side of the road, near the bottom.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A white line is visible on the right side of the road, near the bottom. Photo
                        2: A white line is visible on the right side of the road, near the bottom.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is center_line, right boundary is
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 6  change_left     prohibited (correct): prohibited due to the solid yellow center line, which prohibits
                        crossing.
Step 6  change_right    allowed (correct): allowed as there is no marking prohibiting the change onto the
                        shoulder/edge.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting straight
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no markings governing this action.
Step 6  turn_right      not_applicable: not_applicable as there are no markings governing this action.
Step 6  u_turn          not_applicable: not_applicable as there are no markings governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as there are no markings governing this action.
Step 7  Reflect         consistent
Advice                  You are in the right lane for straight travel. You may change right if necessary, but
                        changing left is prohibited by the solid yellow center line. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 732, 5.72 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection visible in the distance.
                        My car is in the rightmost lane of the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line next to my car, and further ahead it is also a white
                        dashed line. Photo 2 shows a white dashed line next to my car, and further ahead it is
                        also a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and further ahead it is also a solid
                        white line. Photo 2 shows a solid white line next to my car, and further ahead it is
                        also a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check for agreement | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            left_boundary: On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes. [[CN-5.2.3]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        and [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid white line,
                        and [CN-5.4.2] permits the broken edge line (which is not present here, but the solid
                        line does not prohibit change) to be used, and there is no rule prohibiting the change
                        across a solid edge line in this context.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane that govern turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane that govern turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane that govern U-turns
                        or turning.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area in
                          my lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is an edge lane. You may change left or right,
                        and you may proceed straight. Since there are no specific turn arrows or waiting
                        areas, you should proceed straight or turn based on the intersection signals.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 8454, out 911, 7.91 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection or a major crossing area. There
                        are multiple lanes visible in my direction near the bottom of the photo. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing across the road. Photo 2: A white dashed
                        line is visible next to my car. Further ahead, the line appears to be a white dashed
                        line continuing across the road.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A white dashed line is visible next to my car. Further ahead, the line
                        appears to be a white dashed line continuing across the road. Photo 2: A white dashed
                        line is visible next to my car. Further ahead, the line appears to be a white dashed
                        line continuing across the road.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1: A white dashed line marking is visible across the lane
                        ahead of the car, indicating a crosswalk area. Photo 2: A white dashed line marking is
                        visible across the lane ahead of the car, indicating a crosswalk area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (both boundaries are lane_lines, indicating
                        separation between lanes in the same direction). | roles: The white dashed lines fit
                        the role of lane_line. | markings: The crosswalk marking is consistent with the lane
                        markings. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:crosswalk: No specific rule passage was found that dictates the action based on
                        the presence of a crosswalk marking.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed
                        lane_line, and [CN-5.2.1-2] permits crossing.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed
                        lane_line, and [CN-5.2.1-2] permits crossing.
Step 6  go_straight     allowed (correct): allowed: No arrow prohibits going straight, and the boundaries do
                        not prohibit it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: No arrow or prohibited-
                        movement marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: No arrow or prohibited-
                        movement marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: No arrow or prohibited-
                        movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up check, and no
                        action is allowed against a prohibition.
Advice                  You are in the middle lane, and you may change left or right as the lane lines are
                        broken. You may proceed straight through the intersection area, but be aware of the
                        crosswalk markings ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['arrow:straight', 'line:stop_line']), actions False,
                        unsafe ['change_left', 'change_right'], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 8454, out 959, 7.8 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, there
                        is a bus and traffic continuing forward, suggesting a continuous road section rather
                        than an immediate intersection or ramp end. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A solid yellow line is visible on the left side of my lane, separating
                        traffic flows in opposite directions. Photo 2: The solid yellow line next to my car is
                        clearly visible, and further ahead, it remains a solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible on the right side of my lane, separating
                        traffic flows in the same direction. Photo 2: The solid white line next to my car is
                        clearly visible, and further ahead, it remains a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a center_line, right boundary is a
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check against boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid yellow center_line, and
                        [CN-6.1.1] prohibits crossing.
Step 6  change_right    prohibited (correct): allowed: The right boundary is a solid white lane_line, and
                        [CN-6.2.1] prohibits crossing only on the solid-line side, but since the line is
                        solid, it prohibits crossing.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is permitted to proceed straight ahead. Lane changes
                        are prohibited by the solid lines on both sides.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8454, out 803, 6.59 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely a highway or major thoroughfare, and the road
                        continues straight ahead into the distance. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows no painted line immediately to the left of the car. Photo 2 shows no
                        painted line immediately to the left of the car.
                        none none, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line immediately to the right of the car. Photo 2 shows a
                        solid white line immediately to the right of the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (1) and ego_lane_index
                        (1) agree with the boundary roles (no line on left, line on right defining the edge of
                        the travel area). | roles: the role of the right boundary as a lane_line fits the
                        solid white line separating traffic flows in the same direction (or defining the edge
                        of the travel area if it's the only lane). | markings: no markings were listed, so
                        this check is vacuously true. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The boundary marks the edge of motor vehicle lanes or non-motorized
                        vehicle lanes, or the boundary between motor vehicle lanes and non-motorized vehicle
                        lanes. [[CN-5.4.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            right_boundary: On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes. [[CN-5.2.3]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary has no painted line, and no
                        marking governs this action.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid white line,
                        and no rule prohibits changing right across it.
Step 6  go_straight     allowed (contested, correct): allowed: No arrow or prohibited-movement marking in the
                        lane restricts carrying on straight along the lane.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in the lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane and can proceed straight or change right if necessary.
                        No specific stopping or turning restrictions are visible in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions ['rightmost lane, but a lane line on the right', 'change_left decided
                        with nothing marked on that side']
Tokens                  in 8454, out 820, 6.2 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a clear road
                        section with lane markings, not an intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1: A white dashed line is visible next to the car. Photo 2: A white dashed line
                        is visible next to the car. Further ahead, the white dashed line continues. Further
                        ahead, the white dashed line continues.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1: A solid white line is visible next to the car. Photo 2: A solid white line is
                        visible next to the car. Further ahead, the solid white line continues. Further ahead,
                        the solid white line continues.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2: A red painted area with a white bicycle symbol is visible
                        ahead of the car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count is 3, and my lane is the
                        second from the left (ego_lane_index: 2). The left boundary (lane_line) is on my left,
                        and the right boundary (edge_line) is on my right, which is consistent with my lane
                        being the middle lane. | roles: The left boundary is a white dashed lane_line, and the
                        right boundary is a solid white edge_line, which fits their roles. | markings: The
                        bicycle symbol is located within my lane, which is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            symbol:bike: The non-motorized vehicle symbol shows space for non-motorized vehicles
                        to travel or park. [[CN-5.15.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed lane_line, and
                        [CN-5.2.1-2] permits the crossable lane line to be used for lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid white
                        edge_line, and [CN-5.4.3] permits the use of the edge line as a boundary for lane
                        changes.
Step 6  go_straight     allowed (contested, correct): allowed: No arrow or prohibited-movement marking in my
                        lane restricts carrying on straight along my lane, and the boundaries do not govern
                        it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is designated for non-motorized vehicles ahead. You
                        may change left or right, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 8454, out 955, 7.82 s
```
