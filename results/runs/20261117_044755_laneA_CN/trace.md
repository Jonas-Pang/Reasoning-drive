# Reasoning of lane run 20261117_044755_laneA_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road stretching into the distance, and it appears to continue
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the adjacent lane on the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the adjacent lane on the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The yellow solid lines fit the role of lane_line.
                        | markings: The absence of markings in my lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the left_boundary, as a solid yellow
                        line prohibits crossing into the adjacent lane.
Step 6  change_right    prohibited (contested, correct): prohibited by the right_boundary, as a solid yellow
                        line prohibits crossing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed, as there are no markings restricting carrying
                        on straight along my lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  turn_right      prohibited: prohibited by the no_turn:right marking, as this marking prohibits turning
                        right from my lane.
Step 6  u_turn          not_applicable: not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid yellow
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 928, 5.81 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with trees lining both sides, and the road continues ahead
                        into the distance without an immediate intersection or ramp visible. (lanes 2, mine 1,
                        full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid yellow line is visible on the right side of the
                        lane, extending into the distance.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a white solid lane line, and the right boundary is a yellow solid lane
                        line, which fits the roles of lane_line. | markings: The solid yellow line on the
                        right is consistent with the right boundary being a lane line, and it is interpreted
                        as a yield line. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid yellow lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_yield: The presence of a yield line requires my car to stop before the line
                        and yield to other traffic before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited due to the solid white lane line on the
                        left boundary and the rule that a solid lane line prohibits crossing it.
Step 6  change_right    prohibited (contested, correct): prohibited due to the solid yellow lane line on the
                        right boundary and the rule that a solid lane line prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibitions in
                        the lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stop before the solid yellow line on the right and yield to traffic before
                        proceeding. You are restricted from changing lanes in either direction.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left', 'go_straight allowed
                        without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 2930, out 1013, 6.4 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a wide
                        open area ahead. My car is in one of the lanes near the bottom of the photo. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): There are no lane-use arrows, text, symbols, or specific
                        markings visible across my lane from bottom to end.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in a lane between others). | roles: The solid
                        white lines fit the role of lane_line. | markings: The absence of markings is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane governing
                        this action.
Step 6  turn_right      prohibited: prohibited, because the marking no_turn:right prohibits this movement.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane governing
                        this action.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 927, 5.77 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with an elevated structure overhead. The
                        road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles (a
                        lane line on both sides indicates an intermediate lane). | roles: The white dashed
                        lines fit the role of lane_line. | markings: There are no markings in the lane to
                        check against boundaries. | unseen: No attributes were reported that were not seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line permits lane changes in the direction of
                        traffic.
Step 5  Rule            right_boundary: A broken white lane line permits lane changes in the direction of
                        traffic.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        which permits lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, which permits
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a turn left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a turn right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no
                        prohibited action is allowed.
Advice                  You are in the middle lane, and lane changes are permitted in both directions. You may
                        proceed straight, but you should use the appropriate lane if you intend to turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 2930, out 794, 4.9 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an elevated structure (likely a bridge or overpass)
                        ahead. My car is in one of the lanes moving forward. (lanes 3, mine 2, full)
Step 2  Left            There is a metal guardrail separating my lane from the area to the left.
                        none none, curb no, edge_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line, indicating my
                        lane is between two other lanes/edges. | roles: The right boundary is a solid white
                        line, which fits the role of a lane line separating my lane from the next lane to the
                        right. | markings: The lack of markings in my lane is consistent with the boundaries
                        observed. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The edge line allows my car to travel along the boundary of the
                        roadway.
Step 5  Rule            right_boundary: The solid white line prohibits my car from crossing into the adjacent
                        lane to the right.
Step 5  Rule            no_turn:right: No movement is prohibited by this marking as it was not seen.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is an edge line, and
                        there is no marking prohibiting a lane change.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        line, and the rule prohibits crossing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You are in the middle lane; you may proceed straight or change left, but you must not
                        change right due to the solid white line. No specific stopping or turning areas are
                        marked in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions ['change_left decided with nothing marked on that side']
Tokens                  in 2930, out 1028, 6.23 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two lanes of my direction. | roles: The color (white) and pattern
                        (solid) of both boundaries fit the role of a lane_line. | markings: There are no
                        markings in my lane to contradict the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane to allow or
                        prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable, because there are no markings in my lane to allow or
                        prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane to allow or
                        prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings in my lane indicating
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['leftmost lane,
                        but a lane line on the left']
Tokens                  in 2930, out 827, 5.09 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an overpass or bridge
                        structure. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken yellow line separating my lane from the lane to the right.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The left
                        boundary is a solid white lane_line, and the right boundary is a dashed yellow
                        lane_line, which fits their roles. | markings: The stop line is consistent with the
                        lane boundaries and does not contradict any other marking. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A broken yellow lane line permits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white lane_line, and
                        the rule prohibits crossing it to change lanes.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a dashed yellow
                        lane_line, and the rule permits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: There is no left-turn waiting area or two-way left-turn lane
                          directly to the left of my lane.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed against a prohibition.
Advice                  You may change right into the adjacent lane, or proceed straight ahead. You must stop
                        before the solid white line at the end of your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 979, 5.9 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road under an overpass, and the road continues ahead. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible across the lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The lack of markings in the lane is consistent with the boundaries defining
                        the lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in the lane governing
                        this action.
Step 6  turn_right      prohibited: prohibited, because the no_turn:right marking prohibits this movement.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in the lane governing
                        this action.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings in the lane governing
                          this action.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed against a prohibition.
Advice                  You must stay in your current lane to proceed straight, as lane changes and right
                        turns are prohibited by the solid white lines and markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 905, 5.86 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road, and the road continues ahead without an
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid yellow line marking the boundary with the left
                        lane.; line:stop_yield (partial): A solid white line marking the boundary with the
                        right lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The left
                        boundary is yellow solid, consistent with a lane_line in many jurisdictions, and the
                        right boundary is white solid, consistent with a lane_line. | markings: The markings
                        observed are the boundary lines themselves, which are interpreted as stop/yield lines
                        based on the provided list, although they are primarily lane dividers. The
                        interpretation of these lines as stop/yield lines is based on the provided list's
                        structure, but they function as lane dividers here. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: A solid white line prohibits crossing into the adjacent lane.
Step 5  Rule            line:stop_yield: The presence of a stop/yield line requires the vehicle to come to a
                        complete stop before proceeding.
Step 6  change_left     prohibited (contested, correct): prohibited due to the solid yellow line on the left
                        boundary and the rule that a solid yellow line prohibits crossing into the adjacent
                        lane.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the solid white line on the right
                        boundary and the rule that a solid white line prohibits crossing into the adjacent
                        lane.
Step 6  go_straight     stop_first (contested, label allowed): stop_first because the lane contains a
                        line:stop_yield, which turns all allowed movements into stop_first.
Step 6  turn_left       stop_first: stop_first because the lane contains a line:stop_yield, which turns all
                        allowed movements into stop_first.
Step 6  turn_right      stop_first: stop_first because the lane contains a line:stop_yield, which turns all
                        allowed movements into stop_first.
Step 6  u_turn          stop_first: stop_first because the lane contains a line:stop_yield, which turns all
                        allowed movements into stop_first.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane ahead.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed despite a prohibition.
Advice                  You must come to a complete stop before proceeding in any direction, as indicated by
                        the stop/yield line. Lane changes to the left or right are prohibited by the solid
                        lane lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 2930, out 1082, 6.65 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a change
                        in road configuration. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The solid white lines on both sides fit the role
                        of lane_line. | markings: The lack of markings in the lane is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white lane
                        line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid white lane
                        line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' in my lane prohibits turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the lane
                        marking.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 933, 5.88 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a change
                        in road configuration, though the exact nature is unclear due to the bright sunlight.
                        (lanes 2, mine 1, partial)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two visible lanes. | roles: The left boundary is a solid
                        white lane line, and the right boundary is a dashed white lane line, which fits the
                        roles of lane_line. | markings: There are no arrows, words, or areas in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        the rule states that a solid white lane line prohibits crossing it to change lanes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane line, and the
                        rule states that a dashed white lane line permits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane next to it.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed when prohibited by a rule.
Advice                  You may change right into the adjacent lane, or proceed straight ahead. Turning right
                        is prohibited by a marking in your lane, and you should use the right boundary line to
                        change lanes.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 2930, out 995, 6.25 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway with traffic moving forward. My car is in
                        one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (solid) of both boundaries fit the role of a lane_line. |
                        markings: The stop line is consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates the furthest point my car can proceed before
                        stopping.
Step 6  change_left     prohibited (contested, correct): prohibited, because the left_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited, because the right_boundary is a solid white lane
                        line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibitions in
                        my lane and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibitions in my lane
                        and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibitions in my lane
                        and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibitions in my lane
                        and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines. You may proceed straight ahead until the stop line, after which you must stop.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 958, 5.68 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with a pedestrian overpass ahead. My car is in one of the
                        lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a yellow dashed line separating my lane from the lane to the right.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left boundary is a lane line, right boundary is a lane line). | roles: The left
                        boundary is white dashed, consistent with a lane line. The right boundary is yellow
                        dashed, consistent with a lane line. | markings: There are no arrows, words, or areas
                        in my lane to contradict the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line permits lane changes across it.
Step 5  Rule            right_boundary: A yellow dashed lane line permits lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a white dashed lane line,
                        which permits lane changes.
Step 6  change_right    allowed (contested, label prohibited): Allowed because the right boundary is a yellow
                        dashed lane line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      prohibited: Prohibited because the marking 'no_turn:right' is present in my lane.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. However, you
                        are prohibited from turning right from your current lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 905, 5.68 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where traffic appears to
                        be moving forward and potentially turning. My car is in one of the lanes near the
                        bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the adjacent lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A blue overhead sign with two upward arrows pointing straight
                        ahead.; arrow:left (full): A blue overhead sign with a left-pointing arrow.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a white dashed lane line, and the right boundary is a solid yellow lane
                        line, which fits the roles of lane_line. | markings: The overhead arrows indicate
                        allowed movements (straight and left) and are consistent with the lane markings. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed lane line allows lane changes across it when safe.
Step 5  Rule            right_boundary: A solid yellow lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: This marking allows my car to proceed straight ahead.
Step 5  Rule            arrow:left: This marking allows my car to turn left.
Step 6  change_left     allowed (WRONG, label not_determined): allowed: The left boundary is a dashed lane
                        line, and the rule allows lane changes across it when safe.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited: The right boundary is a solid
                        yellow lane line, and the rule prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: The overhead arrow indicates straight movement,
                        and the boundaries do not prohibit it.
Step 6  turn_left       allowed: allowed: The overhead arrow indicates a left turn, and the boundaries do not
                        prohibit it.
Step 6  turn_right      not_applicable: not_applicable: There is no marking or boundary governing a right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There is no marking or boundary governing a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes to the left if safe, but changing right is prohibited by the
                        solid yellow line. You are permitted to go straight or turn left at the intersection
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 1031, 6.55 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road. Ahead, the road continues, and there
                        are overhead signs indicating speed limits for the lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Speed limit sign showing 120 km/h above the leftmost lane.;
                        text:speed_limit (full): Speed limit sign showing 90 km/h above the middle lane (my
                        lane).; text:speed_limit (full): Speed limit sign showing 100 km/h above the rightmost
                        lane.; text:speed_limit (full): Speed limit sign showing 80 km/h above the middle lane
                        (my lane).; text:speed_limit (full): Speed limit sign showing 100 km/h above the
                        rightmost lane.; text:speed_limit (full): Speed limit sign showing 60 km/h above the
                        rightmost lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The speed limit signs are placed above the lanes and do not contradict the
                        lane markings or boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes into the adjacent lane.
Step 5  Rule            right_boundary: A broken white line allows for lane changes into the adjacent lane.
Step 5  Rule            text:speed_limit: The speed limit signs indicate the maximum permissible speed for the
                        respective lane.
Step 6  change_left     allowed (WRONG, label not_determined): Allowed because the left boundary is a broken
                        white line, which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a broken
                        white line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a turn left.
Step 6  turn_right      not_applicable: Not applicable because there are no markings indicating a turn right.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no
                        prohibited action is allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Pay attention
                        to the posted speed limits for your lane, which is currently 90 km/h.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:speed_limit'], missed []), actions False, unsafe ['change_right'], citation
                        None, contradictions []
Tokens                  in 2930, out 1136, 7.1 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuous stretch of road with no
                        immediate intersection visible. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane line (indicating a lane to the left), and the right boundary
                        is a lane line (indicating a lane to the right). | roles: The left boundary is a
                        dashed white lane line, and the right boundary is a solid white lane line, which fits
                        the roles of lane_line. | markings: The lane markings list is empty of specific
                        markings, which is consistent with the boundaries defining the lane. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line permits lane changes across it.
Step 5  Rule            right_boundary: A solid white lane line prohibits lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed lane line, and the
                        rule permits lane changes across it.
Step 6  change_right    prohibited (correct): Prohibited because the right boundary is a solid lane line, and
                        the rule prohibits lane changes across it.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibitions in
                        the lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You are in the middle lane; you may change left, but changing right is prohibited by
                        the solid white line. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 990, 6.42 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead, the road continues straight without an immediate
                        intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No specific lane markings like arrows, text, or stop lines are
                        visible within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The absence of specific markings in the lane is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            no_turn:right: This marking does not prohibit any movement as it is not a prohibited
                        movement marking.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and the rule allows lane changes across it.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and the rule allows lane changes across it.
Step 6  go_straight     allowed (correct): allowed: Nothing restricts carrying on straight along my lane, and
                        the boundaries do not govern it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You are permitted to change lanes left or right,
                        and you may proceed straight ahead. No specific lane usage is mandated by the markings
                        visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight', 'line:stop_line']), actions False, unsafe
                        ['change_left', 'change_right'], citation None, contradictions []
Tokens                  in 2930, out 911, 6.06 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with several tall buildings in the background. Ahead,
                        the road continues straight, and there is no immediate intersection or ramp visible.
                        (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or stop/yield lines
                        are visible within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles (a
                        lane line on both sides indicates an intermediate lane). | roles: The white dashed
                        lines fit the role of lane_line. | markings: The absence of specific markings in the
                        lane is consistent with the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            no_turn:right: This marking indicates no specific movement restriction is present in
                        the lane.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a white dashed
                        line, which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a white
                        dashed line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a turn left is
                        possible or required.
Step 6  turn_right      not_applicable: Not applicable because there are no markings indicating a turn right
                        is possible or required.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a U-turn is
                        possible or required.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You are in the middle lane, and lane changes are permitted in both directions. You may
                        proceed straight, but you should be aware of surrounding traffic when changing lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 2930, out 907, 6.17 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        possibly leading to an intersection or another section of the highway. (lanes 3, mine
                        2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The absence of markings in my lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  go_straight     allowed (correct): allowed: Nothing restricts carrying on straight along my lane, and
                        the boundaries do not govern it.
Step 6  turn_left       allowed (WRONG, label prohibited): allowed: No arrow or prohibited-movement marking in
                        my lane prohibits it, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      prohibited (correct): prohibited: The marking 'no_turn:right' prohibits turning right
                        from my lane.
Step 6  u_turn          allowed (WRONG, label prohibited): allowed: No arrow or prohibited-movement marking in
                        my lane prohibits it, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may change lanes left or right, go straight, turn left, or make a U-turn, but
                        turning right is prohibited by the marking in your lane. Use the lane appropriate for
                        your intended movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight']), actions False, unsafe ['turn_left',
                        'u_turn'], citation None, contradictions []
Tokens                  in 2930, out 950, 5.98 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a stretch of road continuing forward,
                        possibly leading to an intersection or another section of the road. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane to
                        the right.; arrow:straight (full): A white arrow pointing straight ahead is painted in
                        the lane to the left.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane lines on both sides). | roles: The white dashed lines on both sides fit the role
                        of lane_line. | markings: The arrows in my lane (straight ahead) agree with the
                        boundaries (dashed lines allow lane changes). | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a dashed white
                        line, which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed
                        white line, which permits lane changes.
Step 6  go_straight     allowed (correct): Allowed because the lane marking shows an arrow pointing straight
                        ahead.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no marking
                        indicating a turn left.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there is no marking
                        indicating a turn right.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no marking
                        indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        actions are allowed.
Advice                  You may change lanes left or right, and you are permitted to go straight ahead in your
                        current lane. No specific turning movements are indicated for your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 2930, out 1052, 6.34 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a merging
                        area. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The left
                        boundary is yellow solid, consistent with a lane line in a right-hand traffic country.
                        The right boundary is white solid, consistent with a lane line. | markings: The stop
                        line is present and is consistent with the lane boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: A solid white line prohibits crossing into the adjacent lane.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a solid yellow line and
                        the rule prohibits crossing into the adjacent lane.
Step 6  change_right    prohibited (correct): prohibited, because the right boundary is a solid white line and
                        the rule prohibits crossing into the adjacent lane.
Step 6  go_straight     allowed (correct): allowed, because there are no arrows or prohibitions in the lane,
                        and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable, because there are no arrows
                        or prohibitions in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable, because there are no arrows
                        or prohibitions in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there are no arrows
                        or prohibitions in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must stop at the solid white line ahead. You are restricted from changing lanes in
                        either direction. You may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 2930, out 961, 6.08 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        merging area ahead. My car is in one of the lanes near the bottom of the photo. (lanes
                        3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted on the
                        road surface.; arrow:merge_right (full): A large white arrow pointing to the right is
                        painted on the road surface.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The arrows (straight and merge_right) are present in the lane and are
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            arrow:straight: This arrow allows my car to proceed straight ahead.
Step 5  Rule            arrow:merge_right: This arrow indicates that traffic in this lane must merge to the
                        right.
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white line, and the rule
                        allows lane changes across it.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a broken white line, but the
                        lane marking 'arrow:merge_right' indicates traffic must merge right, which implies
                        this lane is ending or merging into the right lane.
Step 6  go_straight     allowed (correct): allowed: The lane marking 'arrow:straight' allows proceeding
                        straight ahead.
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable: There are no markings
                        indicating a permitted left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The lane marking 'arrow:merge_right'
                        indicates a permitted movement to the right.
Step 6  u_turn          not_applicable (WRONG, label allowed): not_applicable: There are no markings
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change left, proceed straight, or turn right. Be aware that the lane marking
                        indicates traffic in this lane must merge to the right ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:merge_right', 'arrow:straight'], missed ['arrow:straight_left']), actions
                        False, unsafe ['turn_right'], citation None, contradictions ['change_right prohibited
                        across a broken lane line', 'turn_right allowed although no arrow shows it']
Tokens                  in 2930, out 1014, 6.41 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where traffic appears to
                        be moving through or approaching it. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The color (white) and pattern
                        (solid) of both boundaries fit the role of a lane line. | markings: There are no
                        markings in my lane to check against the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a solid white lane
                        line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited, because the right boundary is a solid white lane
                        line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should proceed straight in your current lane. Lane changes are prohibited by the
                        solid white lines on both sides.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 2930, out 869, 5.43 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road under an overpass, and the road continues ahead. (lanes 2,
                        mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead.; arrow:straight
                        (partial): A large white arrow pointing straight ahead, partially visible.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The arrows in my lane (straight ahead) agree with the boundaries (solid lines restrict
                        lane changes, but the arrow governs movement). No contradictions found. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited: prohibited, because the left_boundary is a solid white lane line and the
                        rule prohibits crossing it.
Step 6  change_right    prohibited: prohibited, because the right_boundary is a solid white lane line and the
                        rule prohibits crossing it.
Step 6  go_straight     allowed (correct): allowed, because the lane_markings include an arrow pointing
                        straight ahead.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        marking indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable, because there is no arrow or
                        marking indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        marking indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must remain in this lane to proceed straight ahead, as lane changes are prohibited
                        by the solid white lines. No specific stopping or turning instructions are visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 970, 5.91 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a curve or a section where the road
                        continues. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The absence of markings in my lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            no_turn:right: This marking does not prohibit any movement as it is not a prohibited
                        movement marking.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and the rule allows lane changes across it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  go_straight     allowed (correct): allowed: Nothing restricts carrying on straight along my lane, and
                        the boundaries do not govern it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible features and rules, and no prohibited action
                        is allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turns, you may proceed with caution.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight']), actions False, unsafe ['change_left'],
                        citation None, contradictions []
Tokens                  in 2930, out 918, 5.79 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road ahead, and it appears to be leading towards an intersection
                        or a continuation of the road. My car is in one of the lanes near the bottom of the
                        photo. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): Two white dashed lines are visible in the distance,
                        indicating lane separation.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop line is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a dashed white
                        line, which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed
                        white line, which permits lane changes.
Step 6  go_straight     allowed (correct): Allowed because there are no markings in the lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there are no markings
                        indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there are no markings
                        indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there are no markings
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        actions are allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. You must stop
                        at the visible stop line before proceeding through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 2930, out 885, 5.65 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane to
                        the left of mine.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles
                        (left boundary is a lane line, right boundary is an edge line). | roles: The left
                        boundary is a dashed white lane line, and the right boundary is a solid white edge
                        line, which fits their roles. | markings: The arrows in my lane show straight
                        movement, which is consistent with the lane markings and boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line permits lane changes across it.
Step 5  Rule            right_boundary: A solid white edge line indicates the boundary of the roadway.
Step 5  Rule            arrow:straight: The arrow in my lane permits movement straight ahead.
Step 5  Rule            arrow:straight: The arrow in the adjacent lane permits movement straight ahead.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a dashed lane
                        line, which permits lane changes.
Step 6  change_right    prohibited (correct): Prohibited because the right boundary is a solid edge line,
                        which restricts movement beyond the roadway edge.
Step 6  go_straight     allowed (correct): Allowed because the arrow in my lane permits straight movement.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        marking indicating a left turn is permitted or prohibited.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        marking indicating a right turn is permitted or prohibited.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        marking indicating a U-turn is permitted or prohibited.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You are in the rightmost lane, which permits going straight ahead. You may change left
                        into the adjacent lane, but changing right is prohibited by the solid edge line. No
                        specific instructions are given for turning.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left'],
                        citation None, contradictions []
Tokens                  in 2930, out 1017, 6.7 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane city street with trees lining the sides. Ahead, the road
                        continues into the distance, and there is a marked crosswalk visible. (lanes 3, mine
                        2, full)
Step 2  Left            There is a yellow broken line separating my lane from the lane to the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           There is a yellow broken line separating my lane from the lane to the right.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A yellow dashed line marking the lane boundary to the left.;
                        line:stop_line (partial): A yellow dashed line marking the lane boundary to the
                        right.; line:stop_line (partial): Yellow dashed lines indicating lane division across
                        the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (both are lane_lines, indicating adjacent lanes). | roles: The yellow dashed lines fit
                        the role of lane_line. | markings: The stop lines are consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken yellow line allows lane changes across it.
Step 5  Rule            right_boundary: A broken yellow line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a yellow dashed line, which
                        permits lane changes.
Step 6  change_right    allowed (WRONG, label not_determined): Allowed because the right boundary is a yellow
                        dashed line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      not_applicable: Not applicable because there are no markings indicating a permitted
                        right turn.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no
                        prohibited action is allowed.
Advice                  You are in the middle lane and can change left or right if necessary. You may proceed
                        straight ahead, but be mindful of the crosswalk ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['area:grid']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 966, 6.15 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. The road
                        continues into the distance without an immediate intersection or ramp visible. (lanes
                        2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the adjacent lane on the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a solid yellow lane
                        line, which fits their roles. | markings: The stop line is present at the end of the
                        lane, which is consistent with the lane boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes across it are
                        prohibited.
Step 5  Rule            right_boundary: A solid yellow lane line indicates that lane changes across it are
                        prohibited.
Step 5  Rule            line:stop_line: The stop line indicates that vehicles must come to a complete stop
                        before entering the intersection or stopping area.
Step 6  change_left     prohibited (correct): prohibited due to the solid white lane line on the left boundary
                        and the rule that prohibits lane changes across it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the solid yellow lane line on the
                        right boundary and the rule that prohibits lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed because there are no arrows or prohibitions in
                        the lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibitions in the
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibitions in the
                        lane, and no right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibitions in the
                        lane, and no U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stop at the solid white line ahead. You are restricted to staying in this
                        lane, as lane changes are prohibited by the solid lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['symbol:other']), actions False, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 993, 6.15 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an elevated structure on the left. Ahead, the road
                        continues, and there are vehicles in adjacent lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane to
                        the right.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits their roles. | markings: The arrow in my lane shows straight
                        movement, which is consistent with the lane markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow in my lane permits going straight ahead.
Step 5  Rule            arrow:straight: The arrow in the adjacent lane permits going straight ahead.
Step 6  change_left     prohibited: Prohibited by the solid white line on the left boundary, as per the rule
                        for solid lane lines.
Step 6  change_right    allowed: Allowed by the dashed white line on the right boundary, as per the rule for
                        dashed lane lines.
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed by the white arrow in my lane, as per the
                        rule for lane-use arrows.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable, as there is no arrow or
                        marking indicating a left turn is possible.
Step 6  turn_right      not_applicable (WRONG, label allowed): Not applicable, as there is no arrow or marking
                        indicating a right turn is possible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable, as there is no arrow or
                        marking indicating a U-turn is possible.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there are no markings for a waiting area or two-
                          way left-turn lane ahead.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may proceed straight or change right into the adjacent lane. Changing left is
                        prohibited by the solid white line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation None, contradictions []
Tokens                  in 2930, out 1012, 6.11 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a section with traffic control markings,
                        possibly leading to an intersection or a change in lane configuration. (lanes 2, mine
                        1, full)
Step 2  Left            There is a concrete barrier separating my lane from the area to the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, text, symbols, areas, or lines are
                        visible within my lane in the photographed section.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge line (barrier), and the right boundary is a lane line
                        separating it from another lane. | roles: The right boundary is a solid white line,
                        which fits the role of a lane_line separating my lane from the adjacent lane. |
                        markings: The lack of markings in my lane is consistent with the boundaries observed.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The concrete barrier acts as a physical edge, prohibiting movement
                        beyond it.
Step 5  Rule            right_boundary: The solid white line indicates the boundary of my lane, and crossing
                        it to enter the adjacent lane is prohibited.
Step 5  Rule            no_turn:right: No specific movement is prohibited by this marking as it is not clearly
                        visible or applicable in the lane.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited: The left boundary is a concrete
                        barrier, and the rule for an edge line prohibits movement beyond it.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white line, and the
                        rule for a lane_line prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action, and no waiting area is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action, and no waiting area is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action, and no waiting area is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You should stay in your current lane to proceed straight. Lane changes to the left or
                        right are prohibited by the physical barrier and the solid white line, respectively.
                        No specific stopping or turning instructions are visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 1030, 6.34 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road ahead, and there is an overpass structure visible in the
                        distance. My car is in one of the lanes near the bottom of the photo. (lanes 3, mine
                        2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in a middle lane). | roles: The white dashed
                        lines fit the role of lane_line. | markings: The absence of markings in my lane is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white line, and the rule
                        allows lane changes across it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a broken white line, and the rule
                        allows lane changes across it.
Step 6  go_straight     allowed (correct): allowed: Nothing restricts carrying on straight along my lane, and
                        the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible features, and no action is allowed when
                        prohibited by a rule.
Advice                  You may change lanes left or right, or proceed straight ahead. Turning right is
                        prohibited by the lane marking. Since there are no specific markings for turning left
                        or U-turning, these movements are not explicitly governed by markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight']), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 944, 5.47 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an overpass ahead. My car is in one of the lanes in the
                        foreground. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white dashed arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane lines on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The straight arrow in my lane is consistent with the lane markings. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a white dashed
                        line, which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a white
                        dashed line, which permits lane changes.
Step 6  go_straight     allowed (correct): Allowed because the lane marking shows a straight arrow, and no
                        other marking prohibits it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no marking
                        indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there is no marking
                        indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no marking
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes left or right, and you are permitted to go straight ahead in this
                        lane. No specific stopping or turning instructions are visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation None,
                        contradictions []
Tokens                  in 2930, out 870, 5.38 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The lack of markings in my lane is consistent with the boundaries defining
                        the lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white lane
                        line, and the rule prohibits crossing it to change lanes.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane next to it.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 955, 6.21 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): Double solid yellow lines marking the center of the road
                        ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color
                        (yellow) and pattern (solid) of both boundaries fit the role of a lane_line. |
                        markings: The double solid yellow lines ahead are consistent with the lane markings
                        observed. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid yellow lane line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: A solid yellow lane line prohibits crossing into the adjacent lane.
Step 5  Rule            line:stop_yield: The presence of a stop/yield line in the lane requires the car to
                        come to a complete stop before proceeding.
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid yellow lane
                        line and the rule prohibits crossing into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right_boundary is a solid
                        yellow lane line and the rule prohibits crossing into the adjacent lane.
Step 6  go_straight     stop_first (contested, label allowed): stop_first, because the line:stop_yield marking
                        requires the car to come to a complete stop before proceeding.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before proceeding straight ahead. Lane changes to the
                        left or right are prohibited by the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 949, 5.94 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road stretching into the distance, and it appears to continue
                        forward without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The stop line is consistent with the lane boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     prohibited (correct): prohibited: The left_boundary is a solid white lane line, and
                        the rule prohibits crossing it to change lanes.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule prohibits crossing it to change lanes.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: Nothing restricts carrying on straight
                        along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         consistent
Advice                  You must stop at the solid white line ahead. You are restricted to proceeding straight
                        in your current lane, as lane changes are prohibited by the solid white lines on both
                        sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['arrow:left_u_turn', 'arrow:straight']), actions False,
                        unsafe ['go_straight'], citation None, contradictions []
Tokens                  in 2930, out 932, 5.54 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The solid white lines fit the role of lane_line. |
                        markings: The absence of markings is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white lane
                        line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (correct): allowed: Nothing restricts carrying on straight along my lane, and
                        the boundaries do not govern it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  turn_right      prohibited (correct): prohibited: The marking no_turn:right prohibits turning right
                        from my lane.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible markings or boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by a
                        marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 2930, out 926, 6.08 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an overpass on the left. Ahead, the road continues into
                        a built-up area. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The lack of markings in my lane is consistent with the boundaries defining
                        the lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited: The left_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited: The right_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible markings or boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 947, 6.46 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road stretching into the distance, and ahead there is a road sign
                        indicating lane usage ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, text, symbols, areas, or lines are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left boundary is a lane line, right boundary is a lane line). | roles: The color and
                        pattern of the boundaries fit their roles (white dashed line for lane_line on the
                        left, white solid line for lane_line on the right). | markings: The lack of markings
                        in my lane is consistent with the boundaries defining the lane. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A solid white line prohibits lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, and the rule
                        allows lane changes across it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        line, and the rule prohibits lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible features and their corresponding rules, and
                        no prohibited action is allowed.
Advice                  You may change lanes to the left, but changing to the right is prohibited by the solid
                        white line. You may proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 959, 5.99 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues straight into a built-up area. (lanes 3, mine 2, full)
Step 2  Left            There is a dashed white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a dashed white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane to
                        the right.; arrow:straight (full): A white arrow pointing straight ahead is painted in
                        the lane to the left.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane lines on both sides). | roles: The color and pattern of both boundaries (white
                        dashed lines) fit the role of lane_line. | markings: The arrows in my lane (straight
                        ahead) agree with the boundaries (dashed lines allow lane changes). | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white lane line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white lane line allows for lane changes across it.
Step 5  Rule            arrow:straight: The arrow in my lane indicates that going straight ahead is permitted.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a dashed white
                        lane line, which permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed
                        white lane line, which permits lane changes.
Step 6  go_straight     allowed (correct): Allowed because the arrow in my lane shows straight ahead, and no
                        other marking prohibits it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        marking indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        marking indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        marking indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes left or right, and you are permitted to go straight ahead. No
                        specific lane is required for these movements.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 2930, out 988, 5.5 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in one of
                        the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        across my lane from the bottom to the end.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left boundary is a lane line, right boundary is a lane line). | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits their roles. | markings: The absence of markings in my lane is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the solid white lane line on the left
                        (element_rules).
Step 6  change_right    allowed (correct): Allowed by the dashed white lane line on the right (element_rules).
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings restricting
                        straight movement in my lane (no marking governs this action).
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a permitted
                        left turn (not_applicable).
Step 6  turn_right      prohibited: Prohibited by the no_turn:right marking in my lane (element_rules).
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a permitted
                        U-turn (not_applicable).
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no marked waiting area or two-way
                          left-turn lane visible (not_applicable).
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may change right into the adjacent lane, or proceed straight ahead. Turning left
                        or turning right is prohibited from your current lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 934, 5.8 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection.
                        (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries
                        defining the lane. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white lane
                        line, and the rule prohibits crossing it to change lanes.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited: The right_boundary is a solid
                        white lane line, and the rule prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must stay in your lane as lane changes are prohibited by the solid white lines.
                        You are allowed to go straight, but turning right is prohibited by the marking in your
                        lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 934, 5.68 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and ahead there is an exit ramp indicated
                        by overhead signs. My car is in one of the lanes traveling forward. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in a middle lane). | roles: The white dashed
                        lines fit the role of lane_line. | markings: The absence of markings in my lane is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (WRONG, label not_determined): allowed: The left boundary is a white dashed
                        line, and the rule allows lane changes across it.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and the rule allows lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing this action.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible markings or boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may change lanes left or right, or proceed straight ahead. Turning right is
                        prohibited from your current lane. Use the lane appropriate for your intended exit.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 2930, out 933, 5.88 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and the road continues straight ahead with no immediate
                        intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries
                        defining the lane. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking indicates no specific movement restriction is present in
                        my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white lane
                        line, and the rule prohibits crossing it to change lanes.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action, and no waiting area is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action, and no waiting area is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action, and no waiting area is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible features, and no action is allowed when
                        prohibited by a rule.
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 978, 6.08 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuation of the road,
                        possibly leading to an intersection or another section of the road. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid white line marking the lane boundary on the left.;
                        line:stop_yield (partial): A solid yellow line marking the lane boundary on the
                        right.; arrow:straight (full): A white painted arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The left
                        boundary is solid white, consistent with a lane_line. The right boundary is solid
                        yellow, consistent with a lane_line. | markings: The white arrow pointing straight
                        ahead is consistent with the lane markings. The presence of stop_yield markings on
                        both boundaries is noted. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes across it are
                        generally prohibited.
Step 5  Rule            right_boundary: A solid yellow lane line indicates that lane changes across it are
                        generally prohibited.
Step 5  Rule            line:stop_yield: The presence of a stop-and-yield line requires the vehicle to come to
                        a complete stop before proceeding.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (contested, label allowed): prohibited, because the left boundary is a
                        solid white lane_line and the rule prohibits lane changes across it.
Step 6  change_right    prohibited (contested, correct): prohibited, because the right boundary is a solid
                        yellow lane_line and the rule prohibits lane changes across it.
Step 6  go_straight     stop_first (contested, label prohibited): allowed, because the arrow:straight marking
                        permits it, and the stop_yield line requires stopping first.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or marking indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or marking indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or marking indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before proceeding straight ahead in this lane. Lane
                        changes to the left or right are prohibited by the solid lane lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:stop_yield'], missed ['text:bus']), actions None, unsafe [],
                        citation None, contradictions []
Tokens                  in 2930, out 1092, 6.0 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with a clear view ahead, suggesting a
                        continuous stretch of road rather than an immediate intersection or ramp end. (lanes
                        3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: a
                        lane line on the left and a lane line on the right confirms my lane is in the middle
                        of three lanes. | roles: The solid white lines on both sides fit the role of
                        lane_line. | markings: The absence of markings in my lane is consistent with the
                        boundaries defining the lane. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white lane
                        line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' in my lane prohibits this
                        movement.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane to proceed straight, as lane changes are
                        prohibited by the solid white lines. Turning right is prohibited by the lane marking.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 934, 6.15 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a long, straight road ahead, suggesting continuous
                        travel rather than an immediate intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A dashed white line marking the separation between my lane
                        and the lane to the right.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: a
                        lane line on the left and a lane line on the right confirms my lane is in the middle
                        of three lanes. | roles: The white solid lines fit the role of lane_line. | markings:
                        The dashed line observed is identified as a stop line, which is consistent with the
                        lane markings. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding,
                        although this is typically for intersections, here it marks the end of the visible
                        lane markings.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibitions in
                        my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings indicating a turn left.
Step 6  turn_right      not_applicable: not_applicable, because there are no markings indicating a turn right.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed against a prohibition.
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes to the
                        left or right are prohibited by the solid white lines marking the lane boundaries.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 947, 5.85 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a clear view ahead, and the road continues straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The absence of markings in the lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane next to it.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Turning right
                        is prohibited in this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 905, 5.56 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and the road continues ahead without an
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane division ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop line is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates the end of the travel lane before a stopping
                        point, though no specific stop action is mandated by this line alone.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and the rule allows lane changes across it.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and the rule allows lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a turn left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a turn right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes left or right as the lane markings are broken. You may proceed
                        straight ahead, but be aware of the stop line ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 2930, out 894, 5.78 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with trees lining both sides. The road continues straight
                        ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The absence of markings is consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' prohibits turning right.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible features, and no action is allowed when
                        prohibited by a rule.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Turning right
                        is prohibited by the lane marking, and there are no markings governing left turns or
                        U-turns.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 908, 6.19 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a barrier on the right side. Ahead, the road
                        continues straight. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right, followed by
                        a metal guardrail.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a dashed lane line, and the right boundary is a solid lane line, which
                        fits the roles. | markings: There are no markings in the lane to check against the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows for lane changes across it.
Step 5  Rule            right_boundary: A solid white lane line prohibits lane changes across it.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed lane line, and the rule
                        allows for lane changes across it.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid lane line, and the
                        rule prohibits lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but changing to the right is prohibited by the solid
                        white line. You may proceed straight ahead in your current lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 873, 5.43 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and the road continues ahead without an
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two other lanes. | roles: The solid white lines on both sides fit the
                        role of lane_line. | markings: The stop line is consistent with the lane boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates the furthest point my car can proceed before
                        stopping, if required by a signal or sign.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited, because the right boundary is a solid white lane
                        line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibitions in
                        my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibitions in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibitions in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibitions in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 955, 5.8 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with multiple lanes going in the same direction ahead. My
                        car is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, words, symbols, areas, or lines are visible
                        across my lane from the bottom to the end.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The color and pattern of both boundaries (white,
                        dashed) fit the role of a lane_line. | markings: The absence of markings in my lane is
                        consistent with the boundaries defining the lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows for lane changes across it.
Step 5  Rule            right_boundary: A broken white lane line allows for lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a broken white lane line,
                        which permits lane changes.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a broken white lane line,
                        which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a turn left is
                        possible.
Step 6  turn_right      prohibited: Prohibited because the marking 'no_turn:right' is present in my lane.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a U-turn is
                        possible.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. However, you
                        are prohibited from turning right from your current lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 910, 5.57 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a barrier on the right side. Ahead, the road
                        continues straight. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right, and beyond
                        that is a metal guardrail.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: a
                        lane line on the left and a lane line on the right indicate my lane is in the middle.
                        | roles: The left boundary is a dashed lane line, and the right boundary is a solid
                        lane line, which fits the roles of lane_line. | markings: The absence of markings in
                        my lane is consistent with the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A solid white line prohibits lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed lane line, and a
                        broken line allows lane changes across it.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited because the right boundary is a solid
                        lane line, and a solid line prohibits lane changes across it.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        restricting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      prohibited: Prohibited because the marking 'no_turn:right' in my lane prohibits
                        turning right.
Step 6  u_turn          not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid white
                        line. You may proceed straight, but turning right is prohibited by the marking in your
                        lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 937, 6.0 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and the road continues straight ahead into
                        the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (solid) of both boundaries fit the role of a lane_line. |
                        markings: The stop line is visible ahead, which is consistent with the lane markings.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding, if required by a sign or signal.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibitions in
                        the lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 954, 5.67 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway with a clear view ahead, suggesting a
                        continuous stretch of road rather than an immediate intersection or ramp. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane division ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop line is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates the point where the vehicle must stop if
                        required by a signal or sign.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed white line, which
                        permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a dashed
                        white line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a turn left.
Step 6  turn_right      not_applicable: Not applicable because there are no markings indicating a turn right.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        actions are allowed.
Advice                  You are in the middle lane of a multi-lane highway. You are permitted to change lanes
                        left or right, and you may proceed straight ahead. Be aware of the stop line ahead,
                        which may require you to stop if traffic signals or signs dictate.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 2930, out 898, 5.67 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with multiple lanes visible in my direction, and the road
                        continues ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane division ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop line is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, and the rule
                        allows lane changes across it.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white line,
                        and the rule allows lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a permitted left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a permitted right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a left-turn waiting area
                          or a two-way left-turn lane.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no
                        prohibited action is allowed.
Advice                  You may change lanes left or right as the lane markings are broken. You may proceed
                        straight ahead, but you must stop before the visible stop line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 2930, out 891, 5.76 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and the road continues ahead without an
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles (a
                        lane line on both sides indicates an intermediate lane). | roles: The white solid
                        lines fit the role of lane_line. | markings: The absence of markings is consistent
                        with the boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     prohibited (correct): prohibited: The left_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited: The right_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits the movement to the right.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are permitted to continue going straight ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 917, 6.21 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and the road continues ahead into the
                        distance. (lanes 5, mine 3, full)
Step 2  Left            There is no visible painted line or curb on the left side of my lane in the visible
                        stretch.
                        none none, curb no, unknown, evidence insufficient
Step 2  Right           There is a white dashed lane line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (5) and ego_lane_index (3) are consistent with the
                        boundaries: the right boundary is a lane line, and the left boundary is not a lane
                        line, suggesting my lane is not the leftmost lane. | roles: The right boundary is a
                        white dashed lane line, which fits the role of a lane_line. | markings: The absence of
                        markings in my lane is consistent with the boundaries and the general road context. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: No rule applies as there is no visible boundary.
Step 5  Rule            right_boundary: A dashed lane line permits lane changes into or out of the adjacent
                        lane.
Step 5  Rule            no_turn:right: This marking indicates no specific movement restriction is present in
                        my lane.
Step 6  change_left     allowed (correct): allowed: The left boundary has no visible line, and there is no
                        marking prohibiting a lane change to the left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane line, and the
                        rule permits lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a turn left is
                        possible.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a turn right is
                        possible.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a U-turn is possible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the third lane of five. You are permitted to change lanes both left and
                        right, and you may proceed straight ahead. No specific turning movements are indicated
                        or permitted from your current lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        ['change_left decided although that side cannot be seen']
Tokens                  in 2930, out 928, 6.18 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and the road continues ahead without an immediate
                        intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The white solid lines fit the
                        role of lane_line. | markings: The absence of markings is consistent with the
                        boundaries defining the lane. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited: The left boundary is a solid
                        white lane line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited: The right boundary is a solid
                        white lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' in my lane prohibits turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the lane
                        marking.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 950, 5.92 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection visible in
                        the distance. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The color (white) and pattern
                        (solid) of both boundaries fit the role of a lane_line. | markings: There are no
                        markings in my lane to contradict the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 6  change_left     prohibited (correct): prohibited due to the solid white lane line on the left
                        boundary, which prohibits crossing it to change lanes.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited due to the solid white lane line
                        on the right boundary, which prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        restricting movement straight ahead.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane indicating a
                        permitted turn left.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane indicating a
                        permitted turn right.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 2930, out 822, 4.92 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with a pedestrian overpass ahead. My car is in one of the
                        lanes moving forward. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: a
                        lane line on the left means another lane exists on the left, and a lane line on the
                        right means another lane exists on the right. | roles: The color (white) and pattern
                        (solid) of both boundaries fit the role of a lane_line. | markings: There are no
                        markings in my lane to contradict the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited, because the left_boundary is a
                        solid white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited, because the right_boundary is a
                        solid white lane line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane to allow or
                        prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable, because there are no markings in my lane to allow or
                        prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane to allow or
                        prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings in my lane indicating
                          a waiting area.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['leftmost lane,
                        but a lane line on the left']
Tokens                  in 2930, out 826, 5.01 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a bridge or overpass structure. (lanes
                        3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane in the
                        visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white, solid) fit the role of a lane_line. | markings:
                        There are no arrows, words, or areas in my lane to contradict the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited: The left_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited: The right_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible markings or boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 938, 20.51 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection visible in
                        the distance. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: There are no arrows, words, or areas in my lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited: The left_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited: The right_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane next to it.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 943, 6.09 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries
                        defining the lane. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited due to the solid white lane line on the left
                        (element_rules).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the solid white lane line on the
                        right (element_rules).
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings restricting
                        straight movement in my lane (no marking governs this action).
Step 6  turn_left       not_applicable: not_applicable because there are no markings indicating a permitted
                        left turn (no marking governs this action).
Step 6  turn_right      prohibited: prohibited due to the no_turn:right marking in my lane (element_rules).
Step 6  u_turn          not_applicable: not_applicable because there are no markings indicating a permitted
                        U-turn (no marking governs this action).
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible (no marking governs this action).
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by a
                        marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 933, 5.92 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a change
                        in road configuration. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The absence of markings in my lane is consistent with the boundaries defining the
                        lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited: The left_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited: The right_boundary is a solid
                        white lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible features and their corresponding rules, and
                        no action is allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 954, 6.27 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 2, mine 1, full)
Step 2  Left            There is a concrete barrier/retaining wall separating the road from the elevated
                        structure on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the travel lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the right edge of the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is an edge line, suggesting my
                        lane is one of the lanes in the direction of travel. | roles: The left boundary is a
                        physical edge (curb/barrier), and the right boundary is a painted edge line, which
                        fits the roles assigned. | markings: The single marking observed is a line that
                        appears to be a stop line, which is consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The physical barrier on the left defines the edge of the roadway and
                        prohibits driving beyond it.
Step 5  Rule            right_boundary: The solid white line on the right defines the edge of the roadway and
                        prohibits crossing it into the adjacent area.
Step 5  Rule            line:stop_line: The stop line indicates where a vehicle must come to a complete stop
                        before proceeding, if required by a sign or signal.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a physical
                        barrier/retaining wall, and the rule for an edge line prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        line, and the rule for a solid edge line prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid lines and barriers on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 1007, 6.4 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two lanes of my direction. | roles: The white dashed lines fit the
                        role of lane_line. | markings: The straight arrow in my lane is consistent with the
                        lane boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white line on the left allows for lane changes into the
                        adjacent lane on the left.
Step 5  Rule            right_boundary: A broken white line on the right allows for lane changes into the
                        adjacent lane on the right.
Step 5  Rule            arrow:straight: The straight arrow in my lane allows my car to proceed straight ahead.
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a dashed white
                        line, which permits lane changes.
Step 6  change_right    allowed (contested, label prohibited): Allowed because the right boundary is a dashed
                        white line, which permits lane changes.
Step 6  go_straight     allowed (correct): Allowed because the lane marking shows a straight arrow, and no
                        other marking prohibits it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no marking
                        indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there is no marking
                        indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no marking
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes left or right, and you are permitted to go straight ahead. No
                        specific stopping or turning areas are marked in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 2930, out 915, 5.54 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two lanes. | roles: The white solid lines on both sides fit the role
                        of lane_line. | markings: The absence of markings in my lane is consistent with the
                        boundaries defining the lane. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid white lane line
                        and the rule prohibits crossing it.
Step 6  change_right    prohibited (contested, correct): prohibited, because the right_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane governing
                        this action.
Step 6  turn_right      prohibited: prohibited, because the marking no_turn:right prohibits this movement.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane governing
                        this action.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings in my lane governing
                          this action.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by the
                        marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions ['leftmost lane,
                        but a lane line on the left']
Tokens                  in 2930, out 915, 5.94 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries
                        defining the lane. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid white lane line
                        and the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited, because the right_boundary is a solid white lane
                        line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        restricting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane governing
                        this action.
Step 6  turn_right      prohibited: prohibited, because the marking no_turn:right prohibits this movement.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane governing
                        this action.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings in my lane governing
                          this action.
Step 7  Reflect         All actions are decided based on visible features, and no action is allowed when a
                        rule prohibits it.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by the
                        marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 930, 6.11 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection indicated by
                        the overhead sign. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): An overhead sign with three upward arrows is visible ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The solid
                        white line on the left fits the role of a lane_line, and the solid yellow line on the
                        right fits the role of a lane_line. | markings: The overhead arrow indicates straight
                        movement, which is consistent with the lane markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid yellow lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited: The left boundary is a solid
                        white lane line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid yellow
                        lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: The overhead arrow indicates straight movement
                        is permitted in this lane.
Step 6  turn_left       not_applicable: not_applicable: There is no marking indicating a permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There is no marking indicating a permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There is no marking indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You should remain in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid lines on both sides. No specific stopping or turning
                        instructions are visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 924, 5.79 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuous stretch of road with no
                        immediate intersection visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The stop line marking is consistent with the lane markings. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding,
                        although no explicit stop sign is visible.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited, because the right_boundary is a solid white lane
                        line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibitions in
                        the lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 948, 5.85 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left edge of the travel lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across the lane ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is a solid white
                        edge_line, and the right boundary is a dashed white lane_line, which fits the roles
                        assigned. | markings: There are no markings in the lane to check against the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white edge line indicates the boundary of the roadway.
Step 5  Rule            right_boundary: The broken white lane line permits lane changes into the adjacent
                        lane.
Step 5  Rule            no_turn:right: No movement is prohibited by this marking as it was not seen.
Step 6  change_left     allowed (correct): allowed: The left boundary is an edge_line, and there is no marking
                        prohibiting a lane change.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: The right boundary is a dashed
                        lane_line, and the rule permits lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of two. You are permitted to change left or right, and
                        you may proceed straight. No specific lane usage is required for turning movements as
                        no arrows are present.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 948, 6.31 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead with
                        traffic moving in the same direction as my car. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits the roles of lane_line. | markings: The absence of markings in my
                        lane is consistent with the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white lane
                        line, and the rule states that a solid white lane line prohibits crossing it to change
                        lanes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white lane
                        line, and the rule states that a dashed white lane line permits crossing it to change
                        lanes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed when prohibited by a rule.
Advice                  You may change right into the adjacent lane, or proceed straight ahead. Turning left
                        or U-turning is not applicable based on current markings, and turning right is
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 997, 6.05 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane from the bottom to the end.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries
                        defining the lane. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white lane
                        line, and the rule prohibits crossing it to change lanes.
Step 6  change_right    prohibited (correct): prohibited: The right_boundary is a solid white lane line, and
                        the rule prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed when prohibited by a rule.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 969, 6.44 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road with traffic
                        moving in both directions. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The solid white lines on both sides fit the role
                        of lane_line. | markings: The lack of markings in the lane is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white lane
                        line, and the rule prohibits crossing it to change lanes.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane next to it.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 916, 5.61 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and there is no immediate
                        intersection or ramp visible ahead, just traffic continuing forward. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two other lanes. | roles: The solid white lines on both sides fit the
                        role of lane_line. | markings: The straight arrow in my lane agrees with the
                        boundaries; it indicates movement within the lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited: The left boundary is a solid
                        white lane line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited: The right boundary is a solid
                        white lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (correct): allowed: The lane marking shows a straight arrow, and nothing
                        restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_right', 'line:stop_line']), actions False,
                        unsafe [], citation None, contradictions []
Tokens                  in 2930, out 934, 5.97 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with traffic moving away from the camera.
                        The road continues into the distance with buildings visible in the background. (lanes
                        3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The lack of markings in my lane is consistent with the boundaries defining
                        the lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the left_boundary because a solid
                        white lane line prohibits crossing it to change lanes.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the right_boundary because a
                        solid white lane line prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed because nothing restricts carrying on straight
                        along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane.
Step 6  turn_right      prohibited: prohibited by the no_turn:right marking because this marking prohibits
                        turning right from my lane.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane next to it.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by the
                        marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 949, 5.99 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an overpass ahead. My car is in the rightmost lane
                        visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles
                        (left boundary is a lane line, right boundary is an edge line). | roles: The white
                        dashed line on the left fits the role of a lane_line, and the solid white line on the
                        right fits the role of an edge_line. | markings: The absence of markings in my lane is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            right_boundary: A solid white line marks the edge of the roadway and prohibits
                        crossing it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed white line, which
                        permits lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited because the right boundary is a solid
                        white line, which prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      prohibited: Prohibited because the marking 'no_turn:right' in my lane forbids turning
                        right.
Step 6  u_turn          not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on visible features, and no action is allowed against a
                        prohibition.
Advice                  You may change left into the adjacent lane, proceed straight, but turning right is
                        prohibited by a marking in your lane. Use the rightmost lane for straight travel if
                        you do not intend to change lanes.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 927, 5.82 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road stretching into the distance, and it appears to continue
                        straight ahead without an immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The absence of markings in my lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     allowed (correct): allowed: The left_boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  change_right    prohibited (correct): prohibited: The no_turn:right marking in my lane prohibits the
                        movement to the right.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The no_turn:right marking in my lane prohibits the movement to
                        the right.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You are in the middle lane, and you are allowed to change left, but changing right is
                        prohibited by a marking. You may proceed straight, but turning right is prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        ['change_right prohibited across a broken lane line']
Tokens                  in 2930, out 925, 5.81 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an overpass ahead. My car is in one of the lanes near
                        the bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            There is no visible painted line or curb on the left side of my lane.
                        none none, curb no, edge_line, evidence insufficient
Step 2  Right           There is a solid white painted line separating my lane from the adjacent lane on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        right boundary is a lane_line, indicating another lane to the right, and the left
                        boundary is an edge_line (or none), indicating the left edge of the road. | roles: The
                        right boundary is a solid white lane_line, which fits its role. The left boundary has
                        no visible markings, fitting its role as an edge_line (or lack thereof). | markings:
                        There are no markings in my lane, so there are no internal contradictions. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: No rule is provided for the left boundary, which appears to be the edge
                        of the roadway.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 6  change_left     not_applicable (WRONG, label prohibited): not_applicable
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You are in the leftmost lane of two lanes. You may proceed straight, but changing
                        right is prohibited by the solid white line. No specific stopping or turning
                        instructions are visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 785, 4.98 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in one of
                        the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the lane division ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop line is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white lane line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white lane line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white lane
                        line, which allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white lane
                        line, which allows lane changes.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: Nothing in my lane restricts carrying on
                        straight along my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or waiting
                        area indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable: There is no arrow or
                        prohibited-movement marking indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes left or right, or proceed straight through the intersection. You
                        must stop before the visible stop line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:right']), actions False, unsafe ['change_left', 'change_right',
                        'go_straight'], citation None, contradictions []
Tokens                  in 2930, out 889, 5.49 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a clear view ahead, and the road continues into the
                        distance. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the lane division ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop line is consistent with the lane markings and boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed lane line on the left allows my car to change lanes to the
                        left if safe.
Step 5  Rule            right_boundary: A dashed lane line on the right allows my car to change lanes to the
                        right if safe.
Step 5  Rule            line:stop_line: The stop line indicates the furthest point my car may proceed before
                        stopping, although no specific stop requirement is indicated by other markings.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed lane line, which
                        permits lane changes.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed lane line, which
                        permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a turn left.
Step 6  turn_right      not_applicable: Not applicable because there are no markings indicating a turn right.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        actions are allowed.
Advice                  You are in the middle lane of a three-lane highway. You may change lanes left or
                        right, or proceed straight ahead, as the lane markings permit these movements.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 897, 3.36 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with multiple lanes visible ahead, and the road continues
                        into the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): A speed limit marking of 60.; text:speed_limit (full): A
                        speed limit marking of 80.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The speed limit markings are consistent with the lane markings. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed lane line on the left permits lane changes into the adjacent
                        lane.
Step 5  Rule            right_boundary: A dashed lane line on the right permits lane changes into the adjacent
                        lane.
Step 5  Rule            text:speed_limit: The speed limit marking indicates the maximum allowed speed in this
                        lane.
Step 5  Rule            text:speed_limit: The speed limit marking indicates the maximum allowed speed in this
                        lane.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a white dashed line, which
                        permits lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed because the right boundary is a white
                        dashed line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a turn left.
Step 6  turn_right      not_applicable: Not applicable because there are no markings indicating a turn right.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no
                        prohibited actions are allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Be mindful of
                        the posted speed limits of 60 and 80.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 2930, out 952, 5.54 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a wide open area, possibly leading to an
                        intersection or another section of the road. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The lack of markings in my lane is consistent with the boundaries defining
                        the lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white lane
                        line, and the rule prohibits crossing it to change lanes.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 941, 5.93 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a clear view ahead, and the road continues straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The absence of markings in my lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            no_turn:right: This marking does not restrict any movement as it is not a prohibited
                        movement marking.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible features and rules, and no prohibited action
                        is allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turns, you can proceed as normal for your intended
                        movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 920, 5.74 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The absence of markings in my lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line on the left allows for lane changes into the
                        adjacent lane.
Step 5  Rule            right_boundary: A broken white line on the right allows for lane changes into the
                        adjacent lane.
Step 5  Rule            no_turn:right: This marking does not govern any of the seven actions as it is not a
                        lane-use arrow or prohibited-movement marking in the context of the seven actions.
Step 6  change_left     allowed (correct): allowed: The left_boundary is a white dashed line, and the rule
                        allows lane changes.
Step 6  change_right    allowed (correct): allowed: The right_boundary is a white dashed line, and the rule
                        allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on the observed features and their corresponding rules.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turns, you should proceed with caution.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 982, 5.75 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a long, straight road ahead, suggesting continuous
                        travel rather than an immediate intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: a
                        lane line on the left and a lane line on the right confirms my lane is in the middle
                        of three lanes. | roles: The white dashed lines on both sides fit the role of
                        lane_line. | markings: The absence of markings in my lane is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes in either direction.
Step 5  Rule            right_boundary: A broken white line allows for lane changes in either direction.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white line, which allows
                        lane changes.
Step 6  change_right    prohibited (correct): prohibited: The marking 'no_turn:right' in my lane prohibits
                        changing right.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may change lanes to the left, but changing right is prohibited by the lane
                        marking. You may proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        ['change_right prohibited across a broken lane line']
Tokens                  in 2930, out 934, 6.23 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road. Ahead, the road continues under an
                        overpass structure. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: a
                        yellow solid line on the left indicates another lane to the left, and a white solid
                        line on the right indicates another lane to the right. | roles: The yellow solid line
                        on the left fits the role of a lane_line, and the white solid line on the right fits
                        the role of a lane_line. | markings: The lack of markings in the lane is consistent
                        with the boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: A solid white line prohibits crossing into the adjacent lane.
Step 5  Rule            no_turn:right: This marking prohibits turning right from this lane.
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a solid yellow line and
                        the rule prohibits crossing into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited, because the right boundary is a
                        solid white line and the rule prohibits crossing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings indicating a turn left.
Step 6  turn_right      prohibited: prohibited, because the lane marking indicates no_turn:right.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You must remain in your current lane to proceed straight, as lane changes and right
                        turns are prohibited by the solid lines and markings. No specific stopping or waiting
                        areas are indicated.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 935, 5.57 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. The road
                        continues ahead without an immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The absence of markings in my lane is consistent with the boundaries defining the
                        lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited: The left_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible features, and no action is allowed when a
                        rule prohibits it.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by the
                        marking in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 954, 6.49 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with multiple lanes going straight ahead. My car is in
                        the rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a dashed white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the travel lane, followed by a
                        concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, or specific markings are
                        visible within my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles
                        (left boundary is a lane line, right boundary is an edge line). | roles: The left
                        boundary is a dashed white lane line, and the right boundary is a solid white edge
                        line next to a curb, which fits the roles. | markings: The absence of specific
                        markings in my lane is consistent with the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white lane line permits lane changes across it.
Step 5  Rule            right_boundary: A solid white edge line next to a curb indicates the boundary of the
                        roadway.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed white lane line,
                        which permits lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited because the right boundary is a solid
                        white edge line next to a curb, which restricts movement beyond the lane.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      prohibited: Prohibited because the marking 'no_turn:right' in my lane forbids turning
                        right.
Step 6  u_turn          not_applicable: Not applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may change left into the adjacent lane, but turning right is prohibited by a
                        marking in your lane. You may proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 933, 5.84 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a barrier separating it from the opposing traffic.
                        The road continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            There is a metal guardrail separating my lane from the adjacent lane.
                        none none, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the travel lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line dividing the lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a lane line, and the right boundary is an edge line, which fits the
                        observed features. | markings: The dashed line is observed, and it is consistent with
                        the lane structure. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: The lane line on the left indicates that there is another lane of
                        traffic to the left.
Step 5  Rule            right_boundary: The solid white edge line on the right marks the boundary of the
                        roadway.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding,
                        although no specific stopping action is mandated by this line alone.
Step 6  change_left     allowed (WRONG, label not_determined): Allowed, as the left boundary is a lane line
                        and no prohibition is visible.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is an edge line and no prohibition
                        is visible.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in the
                        lane.
Step 6  turn_left       not_applicable: Not_applicable, as there are no markings indicating a turn left.
Step 6  turn_right      not_applicable: Not_applicable, as there are no markings indicating a turn right.
Step 6  u_turn          not_applicable: Not_applicable, as there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on the observed features and rules, and no prohibited
                        action is allowed.
Advice                  You are in the left lane of two lanes. You may change left or right, or proceed
                        straight. Be aware of the stop line ahead, which indicates a stopping point.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_left decided
                        with nothing marked on that side']
Tokens                  in 2930, out 918, 5.94 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a guardrail on the right side. The road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right, followed
                        by a metal guardrail.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): White dashed lane markings indicating lane separation.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left boundary is a lane_line, right boundary is a lane_line). | roles: The white
                        dashed lines fit the role of lane_line. | markings: The stop line marking is
                        consistent with the lane markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding, if
                        required by other signs or signals.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and the rule allows lane changes across it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing in my lane restricts carrying on
                        straight along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane next to it.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no
                        prohibited action is allowed.
Advice                  You may change lanes left or right, or proceed straight ahead. Since there is a stop
                        line visible, be prepared to stop if required by traffic conditions or signs not
                        visible in the photo.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 2930, out 939, 6.11 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with an overpass ahead. My car is in one of the lanes in
                        the direction of travel. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane in the
                        visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: There are no markings in my lane to contradict the boundaries. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line on the left allows for lane changes into the
                        adjacent lane.
Step 5  Rule            right_boundary: A broken white line on the right allows for lane changes into the
                        adjacent lane.
Step 5  Rule            no_turn:right: This marking does not apply as no specific movement is prohibited in my
                        lane.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, which allows
                        lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane next to it.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no
                        prohibited action is allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific turn markings, you can proceed as normal for turning movements.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 2930, out 924, 5.4 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries
                        defining the lane. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane governing
                        this action.
Step 6  turn_right      prohibited: prohibited, because the marking no_turn:right prohibits this movement.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane governing
                        this action.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings in my lane governing
                          this action.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by the
                        lane marking.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 925, 5.84 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or road, and the road continues straight ahead into the
                        distance. (lanes 2, mine 1, full)
Step 2  Left            There is no visible painted line or curb on the left side of my lane.
                        none none, curb no, edge_line, evidence insufficient
Step 2  Right           There is a white dashed lane line on the right side of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): A large white painted symbol showing the number '60' in the center
                        of the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        right boundary is a lane_line, indicating another lane to the right, and the left
                        boundary is an edge_line (or no line), indicating the left edge of the road. | roles:
                        The right boundary is white and dashed, fitting the role of a lane_line separating
                        lanes of the same direction. The left boundary has no visible markings, fitting the
                        role of an edge_line. | markings: The text marking '60' is present in the lane and
                        does not contradict the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since there is no visible line or curb, there are no restrictions or
                        permissions governed by this boundary.
Step 5  Rule            right_boundary: The dashed white line allows for lane changes into the adjacent lane.
Step 5  Rule            text:other: The text marking '60' does not govern any of the seven actions, but serves
                        as advisory information.
Step 6  change_left     not_applicable (WRONG, label allowed): not_applicable
Step 6  change_right    allowed (WRONG, label prohibited): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no
                        prohibited action is allowed.
Advice                  You are in the left lane of a two-lane road. You are allowed to change right into the
                        adjacent lane, and you can proceed straight. The marking '60' is advisory information.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed ['text:speed_limit']), actions False, unsafe ['change_right'],
                        citation None, contradictions []
Tokens                  in 2930, out 889, 5.76 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in one of
                        the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a yellow broken line separating my lane from the lane to the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           There is a yellow dashed line separating my lane from the lane to the right.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates an intermediate lane). | roles: The yellow dashed
                        lines fit the role of lane_line. | markings: The absence of markings in my lane is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken yellow line allows lane changes across it.
Step 5  Rule            right_boundary: A broken yellow line allows lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (contested, label prohibited): Allowed because the left boundary is a yellow
                        dashed line, which permits lane changes.
Step 6  change_right    allowed (contested, label prohibited): Allowed because the right boundary is a yellow
                        dashed line, which permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      prohibited: Prohibited because the marking 'no_turn:right' is present in my lane.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes left or right, or proceed straight ahead. Turning right is
                        prohibited from your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 876, 5.88 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues straight, and there is a small sign visible in the distance. (lanes 3, mine
                        2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: a
                        lane line on the left and a lane line on the right indicate my lane is in the middle
                        of three lanes. | roles: The left boundary is a dashed white lane line, and the right
                        boundary is a solid white lane line, which fits the roles of lane_line. | markings:
                        The absence of markings in my lane is consistent with the boundaries defining the
                        lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line permits lane changes across it.
Step 5  Rule            right_boundary: A solid white lane line prohibits lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (contested, correct): Allowed, because the left boundary is a dashed white
                        lane line, and a broken line permits lane changes across it.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited, because the right boundary is a solid
                        white lane line, and a solid line prohibits lane changes across it.
Step 6  go_straight     allowed (contested, correct): Allowed, because there are no markings in my lane
                        restricting straight movement.
Step 6  turn_left       not_applicable: Not_applicable, because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      prohibited: Prohibited, because the marking 'no_turn:right' prohibits turning right
                        from my lane.
Step 6  u_turn          not_applicable: Not_applicable, because there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed when prohibited by a rule.
Advice                  You are in the middle lane; you may change left, but changing right is prohibited by
                        the solid white line. You may proceed straight, but turning right is prohibited by the
                        'no_turn:right' marking.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 974, 5.89 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuous stretch of road with no
                        immediate intersection visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line marking the right boundary of my lane.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible within my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The left boundary is a white
                        solid lane line, and the right boundary is a yellow solid lane line, which fits the
                        roles of lane_line. | markings: There are no arrows, words, or areas in my lane to
                        check against the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes across it are
                        prohibited.
Step 5  Rule            right_boundary: A solid yellow lane line indicates that lane changes across it are
                        prohibited.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (contested, correct): prohibited by the left_boundary, as a solid white
                        lane line prohibits lane changes across it.
Step 6  change_right    prohibited (contested, correct): prohibited by the right_boundary, as a solid yellow
                        lane line prohibits lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed, as there are no markings in my lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable, as there are no markings in my lane governing this
                        action.
Step 6  turn_right      prohibited: prohibited by the no_turn:right marking, as this marking prohibits turning
                        right from my lane.
Step 6  u_turn          not_applicable: not_applicable, as there are no markings in my lane governing this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid lines.
                        You are allowed to go straight, but turning right is prohibited by the marking in your
                        lane.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['no_turn:right'], missed []), actions None, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 945, 6.05 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues straight, and there are some road signs visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries
                        defining the lane. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid white lane line
                        and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right_boundary is a solid
                        white lane line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      prohibited: prohibited, because the marking no_turn:right prohibits turning right.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings in my lane indicating
                          a waiting area.
Step 7  Reflect         All actions are decided based on visible features, and no action is allowed when
                        prohibited by a rule.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the lane
                        marking.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 933, 5.81 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, there
                        is a complex intersection area with traffic signals and overhead signs. (lanes 3, mine
                        2, full)
Step 2  Left            The left boundary is marked by a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           The right boundary is marked by a solid yellow line.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the lane boundary.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane line (indicating a lane to the left), and the right boundary
                        is a lane line (indicating a lane to the right). | roles: The left boundary is a solid
                        white lane line, and the right boundary is a solid yellow lane line; these roles fit
                        the observations. | markings: The stop line is located at the end of the lane,
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes across this line
                        are prohibited.
Step 5  Rule            right_boundary: A solid yellow lane line indicates that lane changes across this line
                        are prohibited.
Step 5  Rule            line:stop_line: The stop line requires the vehicle to come to a complete stop before
                        proceeding into the intersection.
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white lane line and the rule prohibits lane changes across it.
Step 6  change_right    prohibited (contested, correct): prohibited, because the right boundary is a solid
                        yellow lane line and the rule prohibits lane changes across it.
Step 6  go_straight     allowed (correct): allowed, because there are no arrows or prohibitions in the lane,
                        and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the stop line before proceeding. Lane changes to
                        the left or right are prohibited by the solid lane lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 2930, out 975, 6.21 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Yellow arrows pointing straight ahead are painted on the road
                        surface in the foreground.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two other lanes. | roles: The white solid lines fit the role of
                        lane_line. | markings: The straight arrow in my lane agrees with the boundaries, as it
                        does not conflict with the lane lines. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (contested, label allowed): prohibited: The left boundary is a solid white
                        lane line, and the rule prohibits crossing it to change lanes.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid white lane
                        line, and the rule prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking shows an arrow pointing
                        straight ahead, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a permitted turn
                        left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a permitted turn
                        right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a left-turn waiting area
                          or a two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 936, 5.6 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a bridge or overpass structure,
                        suggesting the road continues forward. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two other lanes. | roles: The solid white lines on both sides fit the
                        role of lane_line. | markings: There are no arrows, words, or areas in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (contested, correct): prohibited due to the solid white line on the left
                        boundary and the rule that prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the solid white line on the right
                        boundary and the rule that prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      prohibited: prohibited due to the 'no_turn:right' marking in my lane and the rule that
                        prohibits turning right.
Step 6  u_turn          not_applicable: not_applicable because there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed despite a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by a
                        marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 930, 5.63 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The solid white lines fit the role of lane_line. |
                        markings: The lack of markings in the lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white lane
                        line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (correct): allowed: Nothing restricts carrying on straight along my lane, and
                        the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits the movement to the right.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 2930, out 916, 20.4 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where the road appears to split or continue. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible within my lane in the
                        visible stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The solid white lines on both
                        sides fit the role of lane_line. | markings: There are no arrows, words, or areas in
                        my lane to contradict the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (contested, correct): prohibited due to the solid white line on the left
                        boundary and the rule that prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the solid white line on the right
                        boundary and the rule that prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed because there is no arrow in my lane prohibiting
                        it, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane governing this action.
Step 6  turn_right      prohibited: prohibited due to the 'no_turn:right' marking in my lane and the rule that
                        prohibits turning right.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by solid white
                        lines. You are allowed to go straight, but turning right is prohibited by a marking in
                        your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 952, 5.9 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in one of
                        the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (both are lane_lines). | roles: The white dashed lines fit the role of lane_line. |
                        markings: There are no markings in my lane to check against boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows for lane changes across it.
Step 6  change_left     allowed (WRONG, label not_determined): allowed: The left_boundary is a white dashed
                        line, and the rule allows lane changes across it.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: The right_boundary is a white dashed
                        line, and the rule allows lane changes across it.
Step 6  go_straight     allowed (contested, label not_determined): allowed: Nothing restricts carrying on
                        straight along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, or proceed straight ahead. Since there are no
                        specific markings for turning, you should proceed with caution when turning.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 850, 19.8 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be a distant intersection or
                        area with traffic control signs. My car is in one of the lanes near the bottom of the
                        photo. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, or specific markings are
                        visible within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles (a
                        lane line on both sides indicates an intermediate lane). | roles: The yellow solid
                        lines fit the role of lane_line. | markings: The absence of specific markings is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: A solid yellow line prohibits crossing into the adjacent lane.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (contested, correct): prohibited, because the left_boundary is a solid
                        yellow line and the rule prohibits crossing into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right_boundary is a solid
                        yellow line and the rule prohibits crossing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane governing a
                        left turn.
Step 6  turn_right      prohibited: prohibited, because the marking no_turn:right prohibits turning right.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid yellow
                        lines. You are allowed to proceed straight, but turning right is prohibited by the
                        marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 931, 6.2 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): There are no arrows, words, symbols, areas, or lines painted
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a white solid lane line, and the right boundary is a yellow solid lane
                        line, which fits the roles of lane_line. | markings: The absence of markings in my
                        lane is consistent with the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes across it are
                        prohibited.
Step 5  Rule            right_boundary: A solid yellow lane line indicates that lane changes across it are
                        prohibited.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (contested, correct): prohibited due to the solid white lane line on the
                        left boundary and the rule that solid white lane lines prohibit lane changes.
Step 6  change_right    prohibited (contested, correct): prohibited due to the solid yellow lane line on the
                        right boundary and the rule that solid yellow lane lines prohibit lane changes.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        restricting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      prohibited: prohibited due to the no_turn:right marking in my lane and the rule that
                        this marking prohibits turning right.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed when prohibited by a rule.
Advice                  You must stay in your current lane as lane changes are prohibited by solid lines. You
                        are allowed to proceed straight, but turning right is prohibited by a marking in your
                        lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 1003, 6.32 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with a green painted surface ahead, and it appears to
                        continue straight ahead without an immediate intersection or ramp visible. (lanes 2,
                        mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A yellow dashed line painted on the road surface, indicating
                        lane division.; line:stop_line (partial): A yellow dashed line painted on the road
                        surface, indicating lane division.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes in this direction. | roles: The color (white) and pattern (solid) of both
                        boundaries fit the role of a lane_line. | markings: The markings observed are lines on
                        the road surface, which are consistent with the lane boundaries and do not contradict
                        the lane structure. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding,
                        although this is not a standard stop sign.
Step 6  change_left     prohibited (contested, correct): prohibited, because the left_boundary is a solid
                        white lane_line and the rule prohibits crossing it.
Step 6  change_right    prohibited (contested, correct): prohibited, because the right_boundary is a solid
                        white lane_line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibitions in
                        the lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibitions in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 1031, 6.18 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with trees lining the sides, and the road continues ahead
                        into the distance. My car is in one of the lanes near the bottom of the photo. (lanes
                        3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A solid white arrow pointing straight ahead is painted in my
                        lane.; arrow:merge_right (full): A solid white arrow pointing right is painted in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left boundary is a lane line, right boundary is a lane line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The arrows (straight and merge_right) are present in my lane and are
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: This arrow allows my car to proceed straight ahead.
Step 5  Rule            arrow:merge_right: This arrow allows my car to merge right into the adjacent lane.
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white lane
                        line, and the rule prohibits crossing it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white lane line, but the
                        arrow:merge_right allows merging right.
Step 6  go_straight     allowed (correct): allowed: The arrow:straight allows proceeding straight ahead.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow:merge_right allows movement to
                        the right, which can include a turn right if the road geometry permits.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a designated
                          waiting area.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may proceed straight or merge right into the adjacent lane. Changing left is
                        prohibited by the solid white line on your left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed []), actions False, unsafe ['turn_right'], citation
                        None, contradictions ['turn_right allowed although no arrow shows it']
Tokens                  in 2930, out 1009, 6.23 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an overpass ahead. My car is in one of the lanes
                        approaching the overpass. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane to
                        the right.; arrow:straight (full): A white arrow pointing straight ahead is visible in
                        the lane to the left.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The arrows in my lane (straight ahead) agree with the boundaries (solid
                        lines restrict lane changes, but the arrow dictates movement). The arrows in adjacent
                        lanes are consistent with the lane structure. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the left
                        (Rule: A solid white lane line prohibits crossing it to change lanes).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        right (Rule: A solid white lane line prohibits crossing it to change lanes).
Step 6  go_straight     allowed (correct): allowed by the white arrow pointing straight ahead in my lane
                        (Rule: The arrow indicates that proceeding straight ahead is permitted in this lane).
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable (No arrow or prohibited-
                        movement marking in my lane indicates a turn left).
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable (No arrow or prohibited-
                        movement marking in my lane indicates a turn right).
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable (No arrow or prohibited-
                        movement marking in my lane indicates a U-turn).
Step 6  enter_waiting_areanot_applicable: not_applicable (No left-turn waiting area or two-way left-turn lane
                          is visible).
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You should remain in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines. No specific stopping or turning maneuvers are
                        indicated.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 1073, 6.31 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road stretching into the distance, and it appears to continue
                        forward without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): An arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): An arrow pointing straight ahead is visible in the lane to the
                        left.; arrow:straight (full): An arrow pointing straight ahead is visible in the lane
                        to the right.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The arrows in my lane (straight ahead) agree with the boundaries (lane lines) and the
                        other lane markings (also straight ahead). | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid white lane line
                        and the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited, because the right_boundary is a solid white lane
                        line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because the arrow:straight in my lane permits
                        going straight ahead.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or marking indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or marking indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or marking indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line']), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 2930, out 1085, 6.19 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        section where lanes converge/diverge. My car is in one of the lanes near the bottom of
                        the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The lack of markings in my lane is consistent with the boundaries defining
                        the lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the left_boundary because it is a
                        solid white lane line and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the right_boundary because it
                        is a solid white lane line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        restricting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_right      prohibited: prohibited by the no_turn:right marking because the rule prohibits the
                        movement to the right.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on visible features, and no action is allowed when a
                        rule prohibits it, except for the right turn which is explicitly prohibited.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to go straight, but turning right is prohibited by the marking
                        in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 961, 6.19 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in one of the lanes
                        near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, text, symbols, areas, or lines are
                        visible across my lane from the bottom to the end.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (both boundaries are lane lines). | roles: The white dashed lines fit the role of
                        lane_line. | markings: The lack of markings in my lane is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (WRONG, label not_determined): allowed: The left boundary is a dashed white
                        line, which allows lane changes.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: The right boundary is a dashed white
                        line, which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible markings or boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Turning right
                        is prohibited from your current lane. Since there are no specific markings for turning
                        left or U-turning, these movements are not explicitly governed by markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed ['line:crosswalk']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 2930, out 929, 5.82 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, text, symbols, areas, or lines are
                        visible within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color and pattern of the boundaries fit their roles: the left boundary is a solid
                        white lane_line, and the right boundary is a dashed white lane_line. | markings: The
                        lane markings list is empty of specific markings, which is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A dashed white lane line permits crossing it to change lanes.
Step 5  Rule            no_turn:right: No specific movement is prohibited by the observed markings in my lane.
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white lane_line, and
                        the rule prohibits crossing it.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane_line, and the rule
                        permits crossing it.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No marking governs this action, and there is no waiting area or two-
                        way left-turn lane.
Step 6  turn_right      not_applicable: No marking governs this action, and there is no waiting area or two-
                        way left-turn lane.
Step 6  u_turn          not_applicable: No marking governs this action, and there is no waiting area or two-
                        way left-turn lane.
Step 6  enter_waiting_areanot_applicable: No marking governs this action, as there is no left-turn waiting
                          area or two-way left-turn lane visible.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You may change right into the adjacent lane, or proceed straight ahead. Do not attempt
                        to change left, as the lane line is solid.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 962, 6.47 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a set of traffic signals indicating an
                        intersection or a point where traffic flow is regulated. (lanes 3, mine 2, full)
Step 2  Left            There is a dashed white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a dashed white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): White dashed lines indicating lane separation ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (dashed lines indicate adjacent lanes). | roles: The white dashed lines fit the role
                        of lane_line. | markings: The stop line is consistent with the lane markings. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white lane line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white lane line allows for lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding.
Step 6  change_left     allowed (contested, correct): allowed: The left boundary is a dashed white lane line,
                        which allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white lane
                        line, which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing in my lane restricts carrying on
                        straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        actions are allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. You must stop
                        at the visible stop line before proceeding through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['text:other']), actions False, unsafe ['change_right'],
                        citation None, contradictions []
Tokens                  in 2930, out 898, 6.03 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the lane division ahead.;
                        line:stop_line (full): A white dashed line marking the lane division ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop lines are consistent with the lane markings and boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and the rule allows lane changes across it.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and the rule allows lane changes across it.
Step 6  go_straight     allowed (correct): allowed: There are no arrows in the lane, and the boundaries do not
                        prohibit going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        actions are allowed.
Advice                  You may change lanes left or right as the lane markings are broken. You may proceed
                        straight ahead, but you must stop before the visible stop line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe ['change_left', 'change_right'],
                        citation None, contradictions []
Tokens                  in 2930, out 927, 5.32 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where the road continues
                        and other traffic moves. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two lanes of my direction. | roles: The white solid lines fit the role
                        of lane_line. | markings: The straight arrow in my lane is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid white lane line
                        and the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited, because the right_boundary is a solid white lane
                        line and the rule prohibits crossing it.
Step 6  go_straight     allowed (correct): allowed, because the arrow:straight marking permits proceeding
                        straight ahead.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane governing this action, and no left-turn waiting
                        area is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane governing this action, and no right-turn arrow
                        is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; no action is allowed
                        against a prohibition, and all decisions are governed by visible features.
Advice                  You should stay in your current lane to proceed straight through the intersection.
                        Lane changes are prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 2930, out 958, 5.92 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a city street with buildings on both sides, and the road continues ahead into
                        the distance. (lanes 2, mine 1, full)
Step 2  Left            There is no visible painted line or curb on the left side of my lane in the visible
                        stretch.
                        none none, curb no, edge_line, evidence insufficient
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        the right boundary is a lane_line and the left boundary is an edge_line. | roles: The
                        right boundary is a solid white lane_line, and the left boundary is an edge_line,
                        which is consistent. | markings: There are no markings in my lane, so there are no
                        internal contradictions. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The lack of a painted line or curb on the left means there is no
                        specific painted restriction governing lane changes to the left.
Step 5  Rule            right_boundary: The solid white line on the right prohibits crossing it to change
                        lanes to the right.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary has no painted line or
                        curb, and there are no markings governing this action.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        lane_line, and the rule for a solid line prohibits crossing it to change lanes to the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change lanes to the left. You are prohibited from changing
                        lanes to the right due to the solid white line. No specific stopping or turning
                        instructions are visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation None, contradictions
                        ['change_left decided although that side cannot be seen']
Tokens                  in 2930, out 919, 5.49 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits the movement to the right.
Step 6  change_left     prohibited (correct): prohibited due to the solid white line on the left boundary and
                        the rule that a solid lane line prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited due to the solid white line on
                        the right boundary and the rule that a solid lane line prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        restricting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  turn_right      prohibited: prohibited due to the no_turn:right marking in my lane and the rule that
                        this marking prohibits the movement to the right.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing
                        turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on visible features, and no action is allowed when
                        prohibited by a rule.
Advice                  You must stay in your current lane as lane changes are prohibited by solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by a
                        marking in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed ['line:stop_line']), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 2930, out 928, 5.53 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection or crossing area ahead. My
                        car is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the lane division ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop line is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection.
Step 6  change_left     allowed (WRONG, label not_determined): allowed: The left boundary is a white dashed
                        line, and the rule allows lane changes across it.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: The right boundary is a white dashed
                        line, and the rule allows lane changes across it.
Step 6  go_straight     allowed (correct): allowed: Nothing in my lane restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible features and their corresponding rules, and
                        no prohibited action is allowed.
Advice                  You may change lanes left or right, or proceed straight through the intersection. You
                        must stop before the visible stop line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 915, 5.89 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: a
                        lane line on the left and a lane line on the right indicates my lane is in the middle
                        of three lanes. | roles: The solid white lines on both sides fit the role of
                        lane_line. | markings: The absence of markings in my lane is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid white lane line
                        and the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited, because the right_boundary is a solid white lane
                        line and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        restricting straight movement.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane governing
                        this action.
Step 6  turn_right      prohibited: prohibited, because the marking no_turn:right prohibits this movement.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane governing
                        this action.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there are no markings in my lane governing
                          this action.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by the
                        marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 925, 5.48 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and the road continues into the distance with no immediate
                        intersection or ramp visible. (lanes 1, mine 1, full)
Step 2  Left            There is a concrete barrier/retaining wall on the left side of the lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is a metal guardrail separating the lane from the adjacent structure on the
                        right.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (1) and ego_lane_index (1) agree with the boundary roles
                        (both are edge_lines). | roles: The left boundary is a concrete barrier (edge_line)
                        and the right boundary is a guardrail (edge_line), which fits the roles. | markings:
                        There are no markings in the lane, so there are no contradictions. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The concrete barrier defines the edge of the roadway on the left.
Step 5  Rule            right_boundary: The guardrail defines the edge of the roadway on the right.
Step 6  change_left     not_applicable (WRONG, label prohibited): not_applicable: There is no painted line or
                        curb on the left to govern a lane change.
Step 6  change_right    not_applicable (WRONG, label prohibited): not_applicable: There is no painted line or
                        curb on the right to govern a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         All actions are decided based on the lack of governing markings or boundaries, which
                        is consistent with the observations.
Advice                  You are in a single lane, and you are permitted to proceed straight ahead. No lane
                        changes or turns are governed by markings in this view.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 880, 5.21 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a marked area with a bicycle symbol,
                        suggesting a transition or dedicated area, but no immediate intersection or ramp is
                        visible. (lanes 2, mine 1, full)
Step 2  Left            There is no visible painted line or curb on the left side of my lane.
                        none none, curb no, edge_line, evidence insufficient
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A red painted area with a white bicycle symbol is visible ahead in
                        the right portion of my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        right boundary is a lane_line, indicating another lane to the right, and the left
                        boundary is an edge_line (or none), indicating the left edge of the road. | roles: The
                        right boundary is solid white, fitting the role of a lane_line separating lanes of the
                        same direction. The left boundary has no markings, fitting the role of an edge_line. |
                        markings: The bicycle symbol is located in my lane and does not contradict the
                        boundaries or other markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: No specific rule is provided for the left boundary, which appears to be
                        the edge of the roadway.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to enter the adjacent
                        lane.
Step 5  Rule            symbol:bike: The bicycle symbol indicates that this area is designated for bicycles,
                        which may restrict or govern the use of this lane for motor vehicles.
Step 6  change_left     not_applicable (WRONG, label allowed): not_applicable
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no
                        prohibited action is allowed.
Advice                  You should proceed straight in your current lane. Changing right is prohibited by the
                        solid white line, and the area ahead is marked for bicycles.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 899, 5.5 s
```
