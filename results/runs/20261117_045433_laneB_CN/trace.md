# Reasoning of lane run 20261117_045433_laneB_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and there is a road ahead that
                        appears to continue straight, possibly leading to an intersection further down. (lanes
                        3, mine 2, full)
Step 2  Left            There is a yellow solid line near the bottom, followed by a yellow dashed line further
                        ahead, and then a curb/barrier structure.
                        yellow solid_dashed (near line solid), curb yes, edge_line, evidence full
Step 2  Right           There is a white dashed line visible ahead of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (partial): A white dashed line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is an edge line (yellow, indicating the left edge of the direction of
                        travel), and the right boundary is a lane line (white, separating lanes in the same
                        direction). | roles: The left boundary is yellow and solid/dashed, fitting the role of
                        an edge line on the left side of the direction of travel (CN-5.4.3). The right
                        boundary is white and dashed, fitting the role of a crossable lane line (CN-5.2.1-2).
                        | markings: The white dashed line observed in the right boundary is consistent with a
                        lane line. The marking observed in the lane (line:crosswalk) is consistent with the
                        lane markings. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:crosswalk: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a yellow solid_dashed edge line,
                        and CN-4.2.2-a permits crossing a broken line.
Step 6  change_right    allowed (contested, label prohibited): Allowed, as the right boundary is a white
                        dashed lane line, and CN-5.2.1-2 indicates it is a crossable lane line.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited markings
                        in the lane, and nothing restricts carrying on straight along the lane.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed against a prohibition.
Advice                  You are in the middle lane, and you may change left or right as the lane markings
                        permit. You may proceed straight ahead, but you should be aware of the crosswalk
                        marking ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['change_left allowed across a curb', 'change_left allowed with the
                        solid line of a solid-and-broken pair nearer my lane']
Tokens                  in 7591, out 1147, 7.43 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        section where lane configuration changes, and my car is in one of the lanes near the
                        bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a yellow broken line separating my lane from the adjacent lane on the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           There is a yellow dashed line separating my lane from the adjacent lane on the right.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): A yellow dashed line marking the right edge of the lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles, as
                        both boundaries are lane_lines. | roles: The yellow dashed lines fit the role of
                        lane_lines separating traffic flows in the same direction, as per CN-4.3.2. |
                        markings: The partial observation of a yellow dashed line near the right boundary is
                        consistent with the boundary role, although the marking list is sparse. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_yield: Vehicles shall stop completely before entering the intersection and
                        may proceed only after making sure it is safe. [[CN-6.5.1.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a yellow dashed line, and CN-4.2.2-a
                        states a broken line means it may be crossed.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a yellow dashed
                        line, and CN-4.2.2-a states a broken line means it may be crossed.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there is
                        a stop-and-yield line visible, you must come to a complete stop before entering the
                        intersection and proceed only when safe.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 7591, out 1082, 6.45 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a wide
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two lanes of the same direction. | roles: The color (white) and
                        pattern (solid) of both boundaries fit the role of a lane_line. | markings: The stop
                        line is consistent with the lane boundaries and the general road layout. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left_boundary is a solid
                        white lane_line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right_boundary is a solid
                        white lane_line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no left-turn waiting area or two-way left-turn lane is
                        visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines. You may proceed straight through the intersection, but you must stop before the
                        solid white stop line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1049, 6.29 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an elevated structure (likely a highway or overpass)
                        running parallel to the right side. Ahead, the road continues straight, and there is
                        no immediate intersection visible. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line marking the lane boundary to the
                        left.; line:stop_line (insufficient): A white dashed line marking the lane boundary to
                        the right.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles, as
                        both boundaries are lane_lines. | roles: The color (white) and pattern (dashed) of
                        both boundaries fit the role of a lane_line. | markings: The reported markings
                        (stop_line) are not clearly visible or identifiable as such in the lane itself, and
                        the lane markings do not contradict the boundaries. | unseen: The specific markings
                        like stop lines are not clearly visible in the lane itself. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed line, and [CN-4.2.2-a]
                        permits crossing a broken line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited markings in
                        the lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you should proceed straight unless you intend to
                        turn, in which case you must check for appropriate lanes.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1110, 6.64 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an elevated structure (likely a bridge or overpass)
                        ahead. My car is in one of the lanes traveling forward. (lanes 3, mine 2, full)
Step 2  Left            There is a metal barrier separating the lane from the roadside area.
                        none none, curb no, edge_line, evidence partial
Step 2  Right           There is a white solid line marking the right edge of the lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings visible in the lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is an edge line, consistent with
                        being an interior lane. | roles: The right boundary is a white solid line, which fits
                        the role of an edge line. | markings: There are no markings in the lane to contradict
                        the boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The carriageway edge line marks the edge of motor vehicle lanes or non-
                        motorized vehicle lanes, or the boundary between motor vehicle lanes and non-motorized
                        vehicle lanes. [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle
                        lanes or non-motorized vehicle lanes, or the boundary between motor vehicle lanes and
                        non-motorized ve"
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so its meaning is not
                        determined by the provided rules. [null]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is an edge line, and no
                        rule prohibits changing left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white solid line, and no rule
                        prohibits changing right.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of three. You may change left or right, and you may proceed
                        straight ahead. Since there are no specific markings for turns, you should proceed
                        with caution.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1013, 6.68 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection where the road continues and other lanes are visible. (lanes 2, mine 1,
                        full)
Step 2  Left            There is a solid white line marking the left edge of the travel lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the photographed section.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is a solid white
                        edge_line, and the right boundary is a dashed white lane_line, which fits the roles
                        assigned. | markings: The lack of markings in my lane is consistent with the
                        boundaries defining the lane structure. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow, but since this is white, it functions as a general edge line marking.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is a broken white line. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers the general absence of a right-turn
                        prohibition marking in this context. [null]
Step 6  change_left     prohibited (WRONG, label allowed): allowed: The left boundary is a solid white
                        edge_line, and [CN-4.2.2-a] permits crossing a solid line in an emergency when safe,
                        but generally, the solid line prohibits crossing, so it is not explicitly allowed for
                        a standard lane change.
Step 6  change_right    allowed (correct): allowed: The right boundary is a broken white lane_line, and
                        [CN-4.2.2-a] states a broken line means it may be crossed.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible to govern this action.
Step 7  Reflect         The actions are consistent with the observations and rules; specifically, the right
                        boundary allows lane changes, while the left boundary's solid nature restricts
                        standard lane changes.
Advice                  You may change right into the adjacent lane, or proceed straight ahead. Do not attempt
                        to change left, as the solid white line prohibits it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1092, 7.34 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line marking the edge of the roadway on the right side.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the stop line for the intersection
                        ahead.; line:stop_line (full): A solid yellow line marking the edge of the roadway on
                        the right.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a broken white lane_line, which fits the role. The right boundary is
                        a solid yellow edge_line, which fits the role. | markings: The stop line is visible
                        ahead, and the right boundary line is consistent with the edge line role. No
                        contradictions were found. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken white lane_line, and
                        [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    prohibited (contested, correct): Prohibited, as the right boundary is a solid yellow
                        edge_line, and [CN-5.4.3] defines the edge line.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not_applicable, as there are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: Not_applicable, as there are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: Not_applicable, as there are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there are no markings indicating a left-turn
                          waiting area or a two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is suitable for proceeding straight or turning
                        right if permitted by signals. Lane changes to the left are permitted as the lane line
                        is broken, but be aware of the solid yellow edge line on your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1119, 7.82 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road under an overpass, and there is a continuation of the road
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a crossable
                        lane line separating traffic in the same direction. | markings: There are no markings
                        in my lane to contradict the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits the crossing of a crossable lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits the crossing of a crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed against a prohibition.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you may turn left or right if the road ahead
                        allows it.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1032, 6.96 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane elevated road or bridge, and ahead there is a continuation of the
                        road structure, not an intersection or ramp end visible in the immediate view. (lanes
                        3, mine 2, full)
Step 2  Left            There is a yellow solid line separating my lane from the adjacent lane on the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a white solid line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A solid yellow line runs along the left boundary, and
                        a solid white line runs along the right boundary.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        yellow line on the left indicates another lane to the left, and the white line on the
                        right indicates the edge of the roadway. | roles: The yellow solid line on the left
                        fits the role of a lane_line separating traffic in the same direction, and the white
                        solid line on the right fits the role of an edge_line. | markings: The marking listed
                        is a general description of the boundaries, not a specific arrow, word, or area within
                        the lane, so it is consistent with the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the left_boundary, as it is a solid
                        yellow lane_line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not
                        cross.
Step 6  change_right    allowed (correct): Allowed because the right_boundary is a solid white edge_line, and
                        no rule prohibits changing right across an edge line.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibited-
                        movement markings in the lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules, as the prohibition on
                        changing left is derived from the solid yellow lane line, and other actions are
                        correctly marked as not applicable due to the lack of governing markings.
Advice                  You may change right into the adjacent lane, or proceed straight ahead. You must stop
                        completely before entering the intersection if the line ahead is a stop-and-yield
                        line, as indicated by the marking.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 7591, out 1151, 8.69 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the adjacent lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is no painted line visible to the right of my lane in the immediate stretch.
                        none none, curb no, edge_line, evidence partial
Step 3  Markings        no_turn:right (full): There are no arrows, words, symbols, areas, or lines painted
                        within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line (or none,
                        which is consistent with being the rightmost lane). | roles: The left boundary is a
                        broken white lane line, which fits the role of separating traffic in the same
                        direction and allowing crossing if it is a crossable lane line, or prohibiting
                        crossing if it is a no-crossing lane line. The right boundary has no line, fitting the
                        role of an edge line if the road edge is not marked. | markings: The lane markings
                        list is empty of specific markings, which is consistent with the observation that
                        nothing is painted in the lane. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers the general absence of a right-turn
                        prohibition marking in the lane. [null]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken white lane line, which
                        according to [CN-5.2.1-2] is a crossable lane line.
Step 6  change_right    allowed (contested, label prohibited): Allowed, as the right boundary has no painted
                        line and no curb, and no marking prohibits it.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable, as there is no arrow or prohibited-movement marking in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable, as there is no arrow or prohibited-movement marking in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable, as there is no arrow or prohibited-movement marking in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed against a prohibition, and all decisions are based on visible features.
Advice                  You may change lanes to the left or right, and you may proceed straight ahead. Since
                        there are no specific markings for turning, you should proceed with caution towards
                        the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1152, 7.24 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be a multi-lane road leading towards an intersection or a section
                        where lane configuration changes, with my car positioned in one of the lanes near the
                        bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            There is a yellow broken line on the left side of my lane.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           There is a white broken line on the right side of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        yellow dashed line on the left acts as a center_line separating opposing traffic, and
                        the white dashed line on the right acts as a lane_line separating my lane from another
                        lane in the same direction. | roles: The yellow dashed line on the left fits the role
                        of a center_line separating opposing traffic, and the white dashed line on the right
                        fits the role of a lane_line separating traffic in the same direction. | markings: The
                        lack of specific markings in my lane is consistent with the boundaries defining the
                        lane structure. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: On a broken-solid yellow line, vehicles on the solid side may not
                        cross; vehicles on the broken side may cross, and a vehicle crossing the line must
                        give way to vehicles travelling normally. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers the general absence of a right turn
                        prohibition marking in my lane. [null]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a yellow dashed
                        center_line, and [CN-6.1.3] permits crossing from the broken side.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed lane_line, and
                        [CN-5.2.1-2] indicates it is a crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes both left and right, and you may proceed straight ahead. Since
                        there are no specific turn markings, turning left, right, or making a U-turn is not
                        governed by markings in your lane.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe ['change_left'], citation unlisted, contradictions []
Tokens                  in 7591, out 1095, 6.8 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes traveling in the same
                        direction ahead, leading towards what appears to be an intersection or a section where
                        lane guidance is present. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the right edge of my lane.;
                        line:stop_line (partial): A solid white line marking the right edge of my lane,
                        further ahead.; line:stop_line (partial): A solid white line marking the right edge of
                        my lane, further ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line (indicating a lane to the left), and the right
                        boundary is a lane line (indicating a lane to the right). | roles: The color (white)
                        and pattern (solid) of both boundaries fit the role of a lane_line. | markings: The
                        markings observed are solid white lines, which are consistent with lane lines and stop
                        lines. No contradictions were found between the markings and the boundaries. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white lane_line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (correct): The right boundary is a solid white lane_line, and [CN-6.2.1]
                        mandates that vehicles on the solid-line side may not cross.
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
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines. You are permitted to proceed straight ahead, but you must stop before the
                        visible stop lines if you intend to yield or wait.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1183, 6.92 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with a bridge ahead, and the road continues into the
                        distance. My car is in the lane closest to the center of the visible road. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (full): There are no arrows, words, symbols, areas, or lines painted
                        within my lane visible from the bottom to the end of the lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The absence of markings in my lane is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers the general absence of a right-turn
                        prohibition marking in this context. [null]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white lane_line, and
                        [CN-6.2.1] prohibits vehicles on the solid-line side from crossing.
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge_line, and
                        [CN-4.2.2-a] implies that crossing a solid line is normally prohibited.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No marking governs this action, and the boundaries do not govern it.
Step 6  turn_right      not_applicable: No marking governs this action, and the boundaries do not govern it.
Step 6  u_turn          not_applicable: No marking governs this action, and the boundaries do not govern it.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         The actions are consistent with the rules derived from the observed markings and
                        boundaries.
Advice                  You should proceed straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid lane and edge lines, respectively. No specific
                        stopping or waiting areas are marked.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 989, 6.52 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line marking the edge of the roadway on the right side.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead.; arrow:straight (full):
                        A white arrow pointing straight ahead.; arrow:straight (full): A white arrow pointing
                        straight ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a dashed white lane line, which fits the role of separating lanes in
                        the same direction. The right boundary is a solid yellow edge line, which fits the
                        role of marking the edge of the roadway. | markings: The three white 'straight' arrows
                        are consistent with the lane markings and do not contradict the boundaries. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, but since this is yellow, it functions as a separation line for opposing
                        traffic or a general edge line. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and the
                        straight arrow indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label not_determined): Allowed, as the left boundary is a broken white
                        lane line, which permits crossing from the broken side.
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited, as the right boundary is a solid
                        yellow edge line, which generally prohibits crossing unless it is an emergency stop
                        lane.
Step 6  go_straight     allowed (contested, correct): Allowed, as the lane markings include a white arrow
                        pointing straight ahead, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane indicating a left turn.
Step 6  turn_right      not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane indicating a right turn.
Step 6  u_turn          not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observed markings and rules, and no action is
                        decided without the governing feature.
Advice                  You are in the rightmost lane, which is designated for straight travel. You may change
                        left into the adjacent lane, but changing right is prohibited by the solid yellow edge
                        line. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1129, 7.51 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or elevated road, and ahead there is a bridge structure
                        overhead, suggesting the road continues forward. My car is in one of the lanes on this
                        elevated structure. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific lane markings (arrows, text, symbols, areas,
                        or lines like stop/yield) are visible within my lane in the immediate foreground or
                        ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles: I
                        have a lane line on both the left and right, indicating I am between two lanes of my
                        direction. | roles: The white dashed lines fit the role of a crossable lane line
                        separating traffic flows in the same direction. | markings: There are no markings in
                        my lane to contradict the boundaries or each other. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     allowed (WRONG, label not_determined): allowed: The left boundary is a dashed line,
                        and [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes to the left or right are permitted as the
                        lane markings are broken. You may proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1054, 7.47 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where the road
                        continues. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no arrows, words, or areas in
                        my lane to check against the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No rule passage specifically governs the absence of a 'no_turn:right'
                        marking in this context.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid white
                        edge_line, and [CN-5.4.3] defines the edge line on the right side of the direction of
                        travel as white, but no rule prohibits changing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight through the
                        intersection. Since there are no specific markings for turns, you should proceed with
                        caution when turning.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1049, 7.0 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The white arrow pointing straight ahead
                        in my lane is consistent with the lane markings and boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and a
                        straight arrow indicates travel straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): prohibited: The left boundary is a dashed white
                        lane_line, and [CN-5.2.1-2] indicates it is a crossable lane line, but no specific
                        rule prohibits the change, however, the presence of a lane_line suggests a change is
                        possible if not restricted by other markings.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid white
                        edge_line, and [CN-5.4.3] indicates it is a white edge line, which does not prohibit
                        changing right unless other markings apply.
Step 6  go_straight     allowed (correct): allowed: The lane marking is an arrow:straight, and [CN-5.13.1]
                        indicates this allows travel straight ahead.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane governing this action, and no left-turn waiting
                        area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane governing this action, and no left-turn waiting
                        area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane governing this action, and no left-turn waiting
                        area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is marked to proceed straight ahead. You may
                        change left or right, but you should be aware that the lane to your left is separated
                        by a crossable lane line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 7591, out 1111, 6.96 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is no painted line visible to the right of my lane in the immediate foreground.
                        none none, curb no, edge_line, evidence partial
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible on the road
                        surface.; arrow:straight (full): A white arrow pointing straight ahead is visible on
                        the road surface further ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line (or none,
                        which is consistent with being the rightmost lane). | roles: The left boundary is a
                        dashed white lane line, which fits the role of separating traffic in the same
                        direction (CN-5.2.1-2). The right boundary has no line, which is consistent with being
                        the edge of the road or shoulder. | markings: The straight arrows in my lane agree
                        with the boundaries; they indicate the allowed movement within the lane defined by the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and the
                        arrow seen indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a broken white
                        lane line, and CN-5.2.1-2 permits crossing the lane line.
Step 6  change_right    not_determined (WRONG, label prohibited): Not determined because the right boundary
                        has no painted line, and no marking governs this action.
Step 6  go_straight     allowed (contested, correct): Allowed because the lane marking shows a white arrow
                        pointing straight ahead, and CN-5.13.1 indicates this direction of travel.
Step 6  turn_left       not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observed markings and rules, and no action is
                        decided without the governing feature.
Advice                  You are in the rightmost lane, which allows you to go straight or change left. Since
                        there is no specific instruction for turning right, you should proceed straight or
                        change left if necessary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1130, 7.74 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely a highway or major arterial road, and there is a
                        road ahead leading towards what appears to be an intersection or a continuation of the
                        road with traffic signals. (lanes 3, mine 2, full)
Step 2  Left            The left boundary is marked by a solid white line, and beyond it, there is a metal
                        guardrail.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           The right boundary is marked by a broken white line, and beyond it, there is a
                        grassy/dirt shoulder area.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): There are white dashed lines marking the lane
                        boundaries ahead.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line separating my
                        lane from another lane to the right. | roles: The left boundary is a solid white edge
                        line, and the right boundary is a dashed white lane line, which fits the roles
                        assigned. | markings: The lane markings observed (dashed lines) are consistent with
                        the boundaries, but the stop line observation is insufficient to confirm its exact
                        placement relative to the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow, but since this is white, it indicates a motor/non-motor separation line or a
                        single-lane two-way road edge line. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a solid white edge line, and there
                        is no rule prohibiting a lane change from the solid side.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a broken white lane line, and
                        [CN-4.2.2-a] states a broken line means it may be crossed.
Step 6  go_straight     allowed (correct): Allowed, as there are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable, as there are no arrows or
                        prohibited-movement markings in my lane, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable, as there are no arrows or
                        prohibited-movement markings in my lane, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable, as there are no arrows or
                        prohibited-movement markings in my lane, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed while a rule prohibits it.
Advice                  You are in the middle lane, and you may change left or right, or proceed straight.
                        Since there are no specific turn markings, you can proceed straight or turn if the
                        intersection allows it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1145, 7.61 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a section with lane markings indicating
                        movement restrictions or guidance. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane to
                        my left.; arrow:straight (full): A white arrow pointing straight ahead is painted in
                        the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        color and pattern of both boundaries (white dashed lines) fit the role of a lane line
                        separating lanes of the same direction. | markings: The arrows in my lane (straight
                        ahead) agree with the boundaries (lane lines allow lane changes if permitted by the
                        line type, and the arrow dictates movement). The arrows in adjacent lanes are
                        consistent with the lane lines. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and a
                        straight arrow indicates travel straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a broken white line,
                        which is a crossable lane line, and the arrow in my lane allows straight movement,
                        which permits lane changes if not restricted by other markings.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a broken white line,
                        which is a crossable lane line, and the arrow in my lane allows straight movement,
                        which permits lane changes if not restricted by other markings.
Step 6  go_straight     allowed (correct): allowed: The arrow in my lane shows straight ahead, and the
                        boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane indicating a turn left.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane indicating a turn right.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a left-turn waiting
                          area or a two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and all three lanes are marked to proceed straight ahead.
                        Lane changes are permitted as the lane lines are broken white lines, but you should
                        proceed straight if that is your intended movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 7591, out 1162, 7.76 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the stop line for the intersection.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a dashed white lane line, which fits the role of separating lanes in
                        the same direction. The right boundary is a solid white edge line, which fits the role
                        of marking the edge of the roadway. | markings: The stop line is present at the end of
                        the lane, which is consistent with the lane boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed, as the left boundary is a broken white
                        lane line, which permits crossing according to [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited, as the right boundary is a solid white edge line,
                        which does not explicitly prohibit lane changes but the solid nature suggests a
                        defined boundary.
Step 6  go_straight     allowed (correct): Allowed, as there are no markings in the lane prohibiting straight
                        movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not_applicable, as there are no arrows or
                        prohibited-movement markings in the lane governing this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not_applicable, as there are no arrows or
                        prohibited-movement markings in the lane governing this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not_applicable, as there are no arrows or
                        prohibited-movement markings in the lane governing this action.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observed markings and rules; no action is allowed
                        against a prohibition, and all decisions are based on visible features.
Advice                  You may change left into the adjacent lane, and you may proceed straight ahead. You
                        must stop before the solid white line at the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe ['change_left'],
                        citation accepted, contradictions []
Tokens                  in 7591, out 1047, 6.78 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            There is a white broken line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is no painted line visible to the right of my lane in the immediate stretch.
                        none none, curb no, edge_line, evidence partial
Step 3  Markings        arrow:straight_right (full): A large white arrow pointing straight ahead and to the
                        right is painted on the pavement.; arrow:straight (full): A large white arrow pointing
                        straight ahead is painted on the pavement.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line (or none,
                        which is consistent with being the rightmost lane). | roles: The white dashed line on
                        the left fits the role of a lane_line separating traffic in the same direction. |
                        markings: The arrows are consistent with the lane configuration, indicating allowed
                        movements for the lane. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates straight or right movement. [[CN-5.13.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates straight movement. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The white dashed line on the left is a
                        crossable lane line, but the presence of the arrow:straight_right and arrow:straight
                        suggests the lane is designated for straight/right movement, and changing left would
                        violate the implied lane function.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary has no painted line and
                        no curb, and there is no marking prohibiting a lane change.
Step 6  go_straight     allowed (correct): allowed: The arrow:straight is present, and no marking prohibits
                        going straight.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited: There is no arrow indicating a left
                        turn, and no waiting area is present.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow:straight_right is present, and
                        no marking prohibits turning right.
Step 6  u_turn          not_applicable (WRONG, label allowed): not_applicable: There is no arrow indicating a
                        U-turn, and no marking prohibits it, but the lane markings do not explicitly allow it.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observed markings and rules; the lane markings
                        govern the movements, and the boundaries govern lane changes.
Advice                  You are in the rightmost lane, which is designated for straight or right turns. You
                        may change right if necessary, but turning left or making a U-turn is prohibited by
                        the lane markings. Proceed straight or turn right at the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'arrow:straight_right'], missed ['arrow:straight_left']), actions
                        False, unsafe ['change_right', 'turn_right'], citation accepted, contradictions
                        ['change_left prohibited across a broken lane line']
Tokens                  in 7591, out 1181, 7.57 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no arrows, words, or areas in
                        my lane to contradict the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed, as the left boundary is a dashed
                        lane_line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    prohibited (correct): Prohibited, as the right boundary is a solid edge_line, and
                        [CN-4.2.2-a] prohibits crossing a solid line.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane restricting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not_applicable, as there are no markings in my lane governing a left
                        turn.
Step 6  turn_right      not_applicable: Not_applicable, as there are no markings in my lane governing a right
                        turn.
Step 6  u_turn          not_applicable: Not_applicable, as there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observed markings and the cited rules.
Advice                  You may change lanes to the left if necessary, but changing right is prohibited by the
                        solid edge line. You may proceed straight ahead, but turning left, right, or making a
                        U-turn is not governed by any specific marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1041, 7.14 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an underpass/bridge structure. There are
                        multiple lanes visible in my direction ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible on the
                        pavement.; arrow:straight (full): A white arrow pointing straight ahead is visible on
                        the pavement.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a crossable
                        lane line separating traffic flows in the same direction. | markings: The straight
                        arrows are consistent with the lane markings and do not contradict the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and a
                        straight arrow indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed: Allowed because the left boundary is a broken white lane line, and [CN-5.2.3]
                        permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed: Allowed because the right boundary is a broken white lane line, and
                        [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (correct): Allowed because the lane contains a white arrow pointing straight
                        ahead, and [CN-5.13.1] indicates this direction of travel.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there are no markings
                        indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label allowed): Not applicable because there are no markings
                        indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there are no markings
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a left-turn waiting
                          area or a two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and rules, and no prohibited action
                        is allowed.
Advice                  You are in the middle lane, and lane changes are permitted as the lane lines are
                        broken. You are permitted to go straight ahead in this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1030, 6.29 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        section where lane guidance is present. My car is in the lane closest to the center of
                        the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the boundary to the left.;
                        line:stop_line (partial): A white dashed line marking the boundary to the right.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles, as
                        both boundaries are lane_lines. | roles: The white dashed lines fit the role of
                        lane_line, as they separate traffic flows in the same direction. | markings: The stop
                        lines are located at the end of the visible lane stretch, consistent with the
                        boundaries defining the lane. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a broken white line,
                        and [CN-5.2.1-2] permits crossing the lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a broken white line, and
                        [CN-5.2.1-2] permits crossing the lane line.
Step 6  go_straight     allowed (correct): allowed: There are no arrows or prohibited-movement markings in my
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you should proceed straight unless you intend to
                        turn, in which case you must check for appropriate turning lanes ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe ['change_left'],
                        citation accepted, contradictions []
Tokens                  in 7591, out 1120, 7.28 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        section where lane configuration changes ahead. My car is in the rightmost lane
                        visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            There is a white broken line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is no painted line visible to the right of my lane in the immediate foreground,
                        but there is a physical barrier/curb structure further ahead.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane to
                        the left of mine.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line/curb. |
                        roles: The left boundary is a white dashed line, consistent with a crossable lane line
                        [CN-5.2.1-2]. The right boundary is an edge line, consistent with the road edge. |
                        markings: The arrows show straight movement, which is consistent with the lane
                        markings and boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates straight ahead. [[CN-5.13.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed because the left boundary is a broken line,
                        which means it may be crossed [CN-4.2.2-a].
Step 6  change_right    not_determined (WRONG, label prohibited): Not determined because the right boundary is
                        an edge line with a curb, and no specific rule governs changing into the area beyond
                        the curb.
Step 6  go_straight     allowed (correct): Allowed because the arrow in my lane shows straight ahead
                        [CN-5.13.1].
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed against a prohibition.
Advice                  You may change left into the adjacent lane, and you are permitted to go straight ahead
                        in your current lane. Since there are no specific markings for turning, you should
                        proceed straight or change lanes as needed for your intended movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1181, 7.42 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the lane closest
                        to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line indicating the lane boundary.;
                        arrow:straight_right (full): A white arrow pointing straight ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a crossable
                        lane line separating traffic in the same direction. | markings: The white arrow
                        pointing straight ahead is present in my lane and is consistent with the lane
                        markings. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates straight ahead or to the right. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a white dashed lane line, and
                        while this line is crossable, the arrow in my lane only permits straight or right
                        movement.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and the arrow in my lane permits movement to the right.
Step 6  go_straight     allowed (correct): allowed: The arrow in my lane permits straight movement, and the
                        boundaries do not prohibit going straight.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in my lane does not show a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in my lane permits movement to
                        the right.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn right, or change right into the adjacent lane. Do not
                        attempt to turn left or change left. You must stop at the visible stop line before
                        proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight', 'line:crosswalk']), actions False,
                        unsafe ['change_right', 'turn_right'], citation accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 7591, out 1060, 7.06 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where the road appears to continue. (lanes 2, mine 1, full)
Step 2  Left            There is a yellow solid line on the left side of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           There is a white dashed line on the right side of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:channelizing (full): There are yellow dashed lines painted across the road ahead,
                        indicating a transition or merging area.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        yellow solid line on the left acts as a center_line separating traffic flows, and the
                        white dashed line on the right acts as a lane_line separating my lane from another
                        lane. | roles: The yellow solid line on the left fits the role of a center_line
                        separating opposing traffic flows, and the white dashed line on the right fits the
                        role of a lane_line separating traffic flows in the same direction. | markings: The
                        channelizing area ahead is consistent with the lane markings and boundaries,
                        indicating a change in lane configuration ahead. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            area:channelizing: Channelizing lines show that vehicles must follow the set path and
                        may not drive on or across the lines. [[CN-6.6.1-3]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        yellow center_line, and [CN-6.1.1] prohibits crossing.
Step 6  change_right    allowed (WRONG, label not_determined): allowed, because the right boundary is a broken
                        white lane_line, and [CN-5.2.1-2] indicates it is a crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change right into the adjacent lane, and you may proceed straight ahead. Do
                        not attempt to change left, as the center line is solid yellow. Be aware of the
                        channelizing markings ahead, which indicate a change in lane configuration.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing'], missed ['area:grid']), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1109, 6.5 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and there is a clear road ahead
                        leading into what appears to be an intersection or a continuation of the road. (lanes
                        3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the adjacent lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken yellow line separating my lane from the adjacent lane to the right.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane to
                        the right.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line (separating from lane 1), and the right boundary is a
                        lane line (separating from lane 3). | roles: The left boundary is solid yellow, which
                        is consistent with a lane line separating traffic flows in opposite directions or
                        prohibiting crossing from the left side if it were a center line, but here it
                        functions as a lane line. The right boundary is dashed yellow, consistent with a lane
                        line that may be crossed. | markings: The white arrow in my lane shows straight ahead,
                        which is consistent with the lane markings. The arrows in adjacent lanes are also
                        consistent with their respective lanes. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: On a broken-solid yellow line, vehicles on the solid side may not
                        cross; vehicles on the broken side may cross, and a vehicle crossing the line must
                        give way to vehicles travelling normally. [[CN-6.1.3]]
Step 5  Rule            right_boundary: On a broken-solid yellow line, vehicles on the solid side may not
                        cross; vehicles on the broken side may cross, and a vehicle crossing the line must
                        give way to vehicles travelling normally. [[CN-6.1.3]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates straight ahead. [[CN-5.13.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow lane line, and [CN-6.1.3]
                        states that vehicles on the solid side may not cross.
Step 6  change_right    allowed (correct): The right boundary is a dashed yellow lane line, and [CN-6.1.3]
                        states that vehicles on the broken side may cross.
Step 6  go_straight     allowed (contested, correct): The white arrow in my lane shows straight ahead, and
                        [CN-5.13.1] indicates this direction of travel.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and [CN-5.13.1] does not restrict turning left.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and [CN-5.13.1] does not restrict turning right.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and [CN-5.13.1] does not restrict U-turns.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or two-way left-turn lane is visible ahead
                          of my lane, so this action is not applicable.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and the reasons
                        correctly reference the governing elements and rules.
Advice                  You are currently in the middle lane. You may change right into the lane on the right,
                        or continue straight ahead. Turning left, right, or performing a U-turn is not
                        governed by markings in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['symbol:other']), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1278, 7.82 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the lane
                        closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane to
                        my left.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The arrows in my lane show straight
                        ahead, which is consistent with the lane markings and boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles.
                        [[CN-5.13.1]]
Step 6  change_left     allowed: Allowed because the left boundary is a dashed lane_line, and [CN-5.2.1-2]
                        permits the crossable lane line to be used where vehicles may change lanes.
Step 6  change_right    allowed: Allowed because the right boundary is an edge_line, and there is no rule
                        prohibiting a lane change onto the shoulder/beyond.
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed because the arrow in my lane shows straight
                        ahead, and [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane governing this action.
Step 6  turn_right      not_applicable (WRONG, label allowed): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane governing this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You may change lanes left or right, and you are permitted to go straight ahead. Since
                        there are no specific turn arrows or waiting areas, you can proceed with straight
                        movement or lane changes as needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation accepted, contradictions []
Tokens                  in 7591, out 1077, 7.09 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        section where lane guidance is present. My car is in the lane closest to the left side
                        of the visible road structure. (lanes 3, mine 1, full)
Step 2  Left            There is a concrete barrier/curb separating my lane from the left side.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white lane line separating my lane from the adjacent lane to the
                        right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line marking the boundary with the
                        adjacent lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line (barrier), and the right boundary is a lane_line
                        (separating from another lane). | roles: The left boundary is a physical curb/barrier,
                        fitting the edge_line role. The right boundary is a broken white line, fitting the
                        lane_line role. | markings: The only visible marking is the right boundary line, which
                        is consistent with the lane_line role. No arrows, words, or areas are clearly visible
                        within my lane. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: Where a non-motorized lane is needed and there is no separating
                        facility between it and the motor vehicle lanes, a motor/non-motor separation line
                        shall be provided. [[CN-5.4.5]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label not_determined): allowed: The left boundary is an edge_line with
                        a curb, and no marking prohibits a lane change.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a broken white
                        lane_line, and [CN-5.2.1-2] permits crossing a broken lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane to restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no right-turn guidance is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no U-turn guidance is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, and you may change left or right, or proceed straight.
                        Since there are no specific markings for turning, you should proceed with caution to
                        the intersection ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions ['change_left allowed across a curb']
Tokens                  in 7591, out 1094, 6.83 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an overpass/bridge structure, suggesting
                        the road continues forward. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (full): There are no arrows, words, symbols, areas, or lines painted
                        within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a broken white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The absence of markings in the lane is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers the general absence of a right-turn
                        restriction marking in the lane. [null]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken white lane_line, and
                        [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a solid white edge_line, and
                        there is no rule prohibiting a lane change onto the edge line.
Step 6  go_straight     allowed (correct): Allowed, as there are no arrows or prohibited-movement markings in
                        my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there is no arrow or prohibited-movement marking in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turns, you may proceed straight, but be aware of the road
                        edge on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight']), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1055, 6.61 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the middle
                        lane.; arrow:straight (full): A white arrow pointing straight ahead is visible in the
                        leftmost lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a broken white lane line, and the right boundary is a solid white
                        edge line, which fits their roles. | markings: The arrows in each lane indicate
                        straight movement, which is consistent with the lane markings. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and the
                        arrow seen indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): Prohibited by the left boundary, as the broken white lane line
                        allows crossing only from the broken side, but the arrow in my lane only permits
                        straight movement.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the right boundary, as the solid white
                        edge line does not prohibit lane changes, and the arrow in my lane only permits
                        straight movement.
Step 6  go_straight     allowed (correct): Allowed because the arrow in my lane shows straight ahead, and no
                        boundary prohibits it.
Step 6  turn_left       prohibited (correct): Prohibited because the arrow in my lane only shows straight
                        ahead.
Step 6  turn_right      prohibited (correct): Prohibited because the arrow in my lane only shows straight
                        ahead.
Step 6  u_turn          prohibited (correct): Prohibited because the arrow in my lane only shows straight
                        ahead.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the rules, as the lane arrow restricts movements to
                        straight ahead, and the boundaries govern lane change possibilities.
Advice                  You should stay in your lane to go straight ahead, as the lane arrow restricts
                        movement to straight. While the right boundary allows lane changes, the arrow
                        prohibits any movement other than going straight.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        ['change_left prohibited across a broken lane line']
Tokens                  in 7591, out 1097, 6.89 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        section where lane configuration changes ahead. My car is in the lane closest to the
                        center of the visible traffic flow. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no arrows, words, or areas in
                        my lane to contradict the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a dashed lane_line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited, as the right boundary is a solid
                        edge_line, and [CN-4.2.2-a] implies that a solid line prohibits crossing.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane restricting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not_applicable, as there are no markings in my lane governing a left
                        turn.
Step 6  turn_right      not_applicable: Not_applicable, as there are no markings in my lane governing a right
                        turn.
Step 6  u_turn          not_applicable: Not_applicable, as there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid edge
                        line. You may proceed straight ahead, but turning left, right, or making a U-turn is
                        not governed by any visible markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1048, 7.25 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera, and it appears to
                        be leading towards a distant intersection or open area. (lanes 3, mine 2, full)
Step 2  Left            There is a yellow solid line separating my lane from the adjacent lane on the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a double solid yellow line separating my lane from the adjacent lane on the
                        right.
                        yellow double_solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): A double solid yellow line marking the right boundary.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is a lane line (separating from lane 1), and the right boundary is a
                        lane line (separating from lane 3). | roles: The left boundary is a yellow solid line,
                        which functions as a lane line separating traffic in the same direction, although
                        yellow lines typically separate opposing traffic or mark the left edge of travel in
                        some contexts; however, given the context of adjacent lanes, it functions as a lane
                        line. The right boundary is a double solid yellow line, which functions as a lane
                        line. | markings: The marking 'line:stop_yield' is listed, but it is associated with
                        the right boundary line, not explicitly within the lane markings area as a separate
                        feature, though it is part of the boundary description. The double solid yellow line
                        on the right boundary is the feature that corresponds to the stop-and-yield line
                        concept, but the marking list only captures the line itself. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (correct): The left boundary is a yellow solid line, and [CN-6.2.1]
                        prohibits vehicles on the solid-line side from crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a double solid yellow line,
                        and [CN-6.1.2] prohibits vehicles in both directions from crossing.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or two-way left-turn lane is visible ahead
                          of my lane.
Step 7  Reflect         All actions are decided based on the observed markings and rules, and no action is
                        allowed when prohibited.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid lines
                        on both sides. You may proceed straight ahead, but you must come to a complete stop
                        before entering the intersection due to the stop-and-yield line on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 7591, out 1189, 7.64 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection in the distance. My car is
                        in the rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a broken yellow line separating my lane from the adjacent lane to the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid yellow line marking the center of the road ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a yellow dashed lane line, which fits the role of separating traffic
                        flows in opposite directions or marking the left-hand edge of the direction of travel
                        (though here it separates same-direction traffic, which is unusual for a yellow line,
                        but it is a lane line). The right boundary is a solid white edge line, which fits the
                        role of marking the edge of the roadway. | markings: The solid yellow line ahead is
                        interpreted as a stop-and-yield line, which is consistent with the general markings
                        seen. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): Prohibited by the left boundary, as it is a yellow
                        dashed lane line, and the rule for no-crossing lane lines applies to the solid side,
                        but since my side is dashed, the rule [CN-6.2.3] suggests I may cross, however, the
                        yellow color suggests opposing traffic separation, and the general rule for yellow
                        lines suggests caution.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a solid white edge line, and
                        there is no rule prohibiting crossing the edge line in this context.
Step 6  go_straight     stop_first (WRONG, label prohibited): Stop_first, because the marking line:stop_yield
                        is present in my lane, which turns all allowed movements into stop_first.
Step 6  turn_left       stop_first (WRONG, label allowed): Stop_first, because the marking line:stop_yield is
                        present in my lane, which turns all allowed movements into stop_first.
Step 6  turn_right      stop_first: Stop_first, because the marking line:stop_yield is present in my lane,
                        which turns all allowed movements into stop_first.
Step 6  u_turn          stop_first: Stop_first, because the marking line:stop_yield is present in my lane,
                        which turns all allowed movements into stop_first.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there are no markings indicating a waiting area
                          or two-way left-turn lane ahead of my lane.
Step 7  Reflect         The actions are consistent with the observations, as the presence of line:stop_yield
                        mandates stop_first for all movements, and the boundaries govern lane changes.
Advice                  You must come to a complete stop before the stop-and-yield line before proceeding
                        straight, turning left, turning right, or making a U-turn. You may change lanes to the
                        right, but be cautious of the yellow dashed line on your left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed ['arrow:left_u_turn', 'arrow:straight']), actions False,
                        unsafe ['change_left', 'go_straight'], citation in_pack_not_accepted, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 7591, out 1192, 7.92 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection in an urban environment. My
                        car is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in the middle lane of three). | roles: The
                        solid white lines fit the role of a lane_line separating traffic in the same
                        direction. | markings: The lack of visible markings in my lane is consistent with the
                        boundaries defining the lane. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so its allowance or
                        prohibition cannot be determined based on the provided rules. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white
                        lane_line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane_line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  go_straight     allowed (correct): allowed: Nothing restricts carrying on straight along my lane, and
                        the boundaries do not govern it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane, and no left-turn waiting area or two-way left-
                        turn lane is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane, and no left-turn waiting area or two-way left-
                        turn lane is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane, and no left-turn waiting area or two-way left-
                        turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight ahead, but turning movements are not
                        governed by any visible markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight']), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1062, 7.53 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an overpass on the left. Ahead, the road continues
                        straight, and there are buildings on the right side. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane division.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The left
                        boundary is solid white, fitting the role of a lane_line. The right boundary is dashed
                        white, fitting the role of a lane_line. | markings: The stop line is visible, and it
                        is consistent with the lane markings. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a broken white lane
                        line, and [CN-5.2.1-2] permits crossing.
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
Step 7  Reflect         consistent
Advice                  You may change right into the adjacent lane, or proceed straight ahead. You must stop
                        before the visible stop line if you intend to stop for any reason.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1032, 7.24 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a white broken line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is no painted line visible to the right of my lane.
                        none none, curb no, edge_line, evidence partial
Step 3  Markings        arrow:straight_right (full): A blue overhead sign with white arrows indicating
                        straight ahead and right.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line (or none,
                        which is consistent with the rightmost lane). | roles: The white dashed line on the
                        left fits the role of a lane_line separating traffic in the same direction. |
                        markings: The overhead arrow indicates allowed movements, and this is consistent with
                        the lane structure. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (correct): Allowed because the left boundary is a broken line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    not_determined (WRONG, label allowed): Not determined because the right boundary has
                        no painted line and no curb, and no marking governs this action.
Step 6  go_straight     allowed (contested, correct): Allowed because the overhead arrow indicates straight
                        ahead, and [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       not_applicable: Not applicable because there is no marking indicating a left turn is
                        possible.
Step 6  turn_right      allowed: Allowed because the overhead arrow indicates right, and [CN-5.13.1] indicates
                        the direction of travel.
Step 6  u_turn          not_applicable: Not applicable because there is no marking indicating a U-turn is
                        possible.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings for a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the observed markings and rules, and no action is
                        decided without the governing feature.
Advice                  You may change left, go straight, or turn right from your current lane. Since the
                        right boundary is not marked, changing right is not determined by markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1016, 7.07 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is no painted line visible to the right of my lane; the edge of the road is
                        visible.
                        none none, curb no, edge_line, evidence partial
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane to
                        the left of mine.; arrow:straight (full): A white arrow pointing straight ahead is
                        painted in the leftmost lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a dashed white lane line, which fits the role of separating lanes in
                        the same direction. The right boundary has no line, fitting the edge line role. |
                        markings: The arrows in my lane show straight ahead, which is consistent with the lane
                        markings. The lane markings are consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and the
                        arrow in my lane indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed, as the left boundary is a broken white
                        lane line, and [CN-5.2.1-2] permits the crossable lane line to separate lanes of the
                        same direction.
Step 6  change_right    not_applicable (WRONG, label prohibited): Not applicable, as the right boundary is an
                        edge line with no painted line to govern a lane change.
Step 6  go_straight     allowed (correct): Allowed, as the arrow in my lane shows straight ahead, and
                        [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable, as there is no arrow or
                        prohibited-movement marking in my lane governing this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable, as there is no arrow or
                        prohibited-movement marking in my lane governing this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable, as there is no arrow or
                        prohibited-movement marking in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is marked for going straight ahead. You may
                        change left into the adjacent lane if necessary, but you cannot change right. Proceed
                        straight ahead or change left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1143, 6.87 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the lane closest
                        to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (partial): A white dashed line marking the lane boundary to the left.;
                        line:stop_line (partial): A white solid line marking the right edge of the lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits the roles. | markings: The markings (a dashed line and a solid
                        line) are consistent with the boundaries, although the specific markings listed are
                        generic and do not contradict the boundaries. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: By form, road markings fall into four classes, including lines: solid
                        or broken lines on the pavement, on curbs or on vertical surfaces. [[CN-4.2.3-a]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken line, which means it may
                        be crossed.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited, as the right boundary is a solid line,
                        which means crossing is normally prohibited.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane.
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; no action is allowed
                        against a prohibition, and all decisions are based on visible features.
Advice                  You may change lanes to the left, but changing to the right is prohibited by the solid
                        white edge line. You may proceed straight through the intersection, but you should be
                        aware of the stop line ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1167, 7.53 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible in my lane from the bottom to
                        the end of the lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in the middle lane of three). | roles: The
                        color and pattern of both boundaries (solid white lines) fit the role of a lane_line
                        separating lanes in the same direction. | markings: The lack of markings in my lane is
                        consistent with the boundaries defining the lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this marking as it was not seen. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white
                        lane_line, and [CN-6.2.1] prohibits vehicles on the solid-line side from crossing.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited: The right_boundary is a solid
                        white lane_line, and [CN-6.2.1] prohibits vehicles on the solid-line side from
                        crossing.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1013, 6.58 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or freeway, and ahead there is an exit ramp indicated by
                        a overhead sign. My car is in the rightmost lane visible in the immediate foreground.
                        (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (partial): A dashed white line extends across the lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The dashed white line observed is
                        consistent with a lane marking, and it does not contradict the boundaries. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: By form, road markings fall into four classes, and lines are solid or
                        broken lines on the pavement, on curbs or on vertical surfaces. [[CN-4.2.3-a]]
Step 6  change_left     allowed (WRONG, label not_determined): Allowed, as the left boundary is a broken line,
                        and [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed, as the right boundary is a solid
                        edge_line, but no specific rule prohibits changing right onto the shoulder/beyond the
                        edge line.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you should proceed with caution regarding the
                        exit ramp ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1070, 6.83 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a clear road section with no immediate
                        intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a broken white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The white arrow pointing straight ahead
                        in my lane is consistent with the lane markings and boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and a
                        straight arrow indicates travel straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): Allowed because the left boundary is a broken white lane_line, and
                        [CN-5.2.1-2] permits the crossing of a broken lane line.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited because the right boundary is a solid
                        white edge_line, and while no specific rule prohibits changing onto an edge line, the
                        solid line suggests a defined boundary.
Step 6  go_straight     allowed (contested, correct): Allowed because the lane marking shows a white arrow
                        pointing straight ahead, and [CN-5.13.1] indicates this direction of travel is
                        permitted.
Step 6  turn_left       not_applicable: Not_applicable because there is no marking in my lane that permits or
                        prohibits a left turn.
Step 6  turn_right      not_applicable: Not_applicable because there is no marking in my lane that permits or
                        prohibits a right turn.
Step 6  u_turn          not_applicable: Not_applicable because there is no marking in my lane that permits or
                        prohibits a U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable because there are no markings for a left-turn waiting
                          area or a two-way left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight ahead. You may change left
                        into the adjacent lane, but changing right is restricted by the solid edge line. No
                        specific instructions are given for turning.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1041, 6.45 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a suburban or urban area, and ahead there is a
                        continuation of the road, possibly leading to an intersection or a change in road
                        configuration. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the adjacent lane on the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the adjacent lane on the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is between two lanes of the same direction. | roles: The color (yellow) and
                        pattern (solid) of both boundaries fit the role of a lane_line separating traffic
                        flows in the same direction, as per CN-6.2.1, although CN-6.2.1 specifies white for
                        no-crossing lane lines, the yellow solid line suggests a prohibition on crossing based
                        on CN-6.1. | markings: The white arrows pointing straight ahead are consistent with
                        the lane markings and do not contradict the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and in
                        this case, they indicate straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, label allowed): prohibited, because the left boundary is a
                        solid yellow lane_line and CN-6.2.1 prohibits crossing on the solid-line side.
Step 6  change_right    prohibited (contested, correct): prohibited, because the right boundary is a solid
                        yellow lane_line and CN-6.2.1 prohibits crossing on the solid-line side.
Step 6  go_straight     allowed (contested, label prohibited): allowed, because the lane marking shows a white
                        arrow pointing straight ahead, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by the solid yellow
                        lines. You are permitted to proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['text:bus']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1166, 7.12 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an overpass or bridge structure,
                        suggesting the road continues forward. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible across the lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no arrows, words, or areas in
                        the lane to contradict the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-5.2.1-2] permits the crossable lane line to be crossed.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, and
                        [CN-5.4.1] defines the edge line, but no rule prohibits crossing it in the visible
                        stretch.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turns, you may proceed straight, but be aware of the lane
                        boundaries.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1071, 7.15 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes traveling in the same
                        direction ahead. The road continues straight ahead into the distance. (lanes 3, mine
                        2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): Two parallel solid white lines are visible in the distance,
                        likely marking the end of the current section or a guide lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits the roles. | markings: The visible marking (line:stop_line) is
                        consistent with the lane markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white lane_line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a solid white edge_line, and
                        no rule prohibits changing right onto the shoulder/beyond.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right, but changing left is prohibited by the solid
                        white lane line. You should be aware of the stop line visible ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1042, 6.38 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes traveling in the same
                        direction ahead. The road continues into the distance without an immediate
                        intersection visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid white line marking the right edge of the lane.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The single marking observed (a solid
                        white line at the end) is consistent with the boundaries and does not contradict them.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white lane_line and [CN-6.2.1] prohibits vehicles on the solid-line side from
                        crossing.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a solid white edge_line, and
                        no rule prohibits crossing the edge line in this context.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right, but changing left is prohibited by the solid
                        white lane line. You should be aware of the solid white line at the end of your lane,
                        which indicates a stopping point.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1046, 6.29 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes traveling in the same
                        direction ahead. The road continues into the distance, and there is no immediate
                        intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line marking the separation between
                        lanes.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (both are lane_lines, indicating adjacent lanes). | roles: The white dashed lines fit
                        the role of a crossable lane line separating traffic in the same direction. |
                        markings: The single line marking observed is too indistinct to confirm if it is a
                        stop line or another marking, but it does not contradict the lane boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [CN-5.2.1-2] permits crossing the lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and [CN-5.2.1-2] permits crossing the lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited markings in
                        my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed against a prohibition.
Advice                  You may change lanes left or right as the lane lines are broken, and you may proceed
                        straight ahead. Since there are no specific markings for turns, you should proceed
                        with caution.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1065, 7.06 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with trees lining both sides. Ahead, the
                        road continues into the distance, and there is no immediate intersection or ramp
                        visible. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, words, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (dashed) of both boundaries fit the role of a lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries
                        defining the lane. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers the absence of a prohibited movement
                        marking in my lane. [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken line, and [CN-5.2.1-2]
                        permits the crossable lane line to be crossed.
Step 6  change_right    allowed (correct): allowed: The right boundary is a broken line, and [CN-5.2.1-2]
                        permits the crossable lane line to be crossed.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting to turn left or
                          a two-way left-turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you may proceed straight or turn right, but
                        turning left is not governed by any specific marking in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1069, 7.41 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible across my lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in the middle lane of three). | roles: The
                        color and pattern of both boundaries (white dashed lines) fit the role of a crossable
                        lane line separating lanes of the same direction. | markings: There are no arrows,
                        words, or areas in my lane to contradict the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No rule passage specifically covers the absence of a prohibited
                        movement marking in this context.
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white line, and [CN-5.2.1-2]
                        permits the crossing of a crossable lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a broken white line,
                        and [CN-5.2.1-2] permits the crossing of a crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting to turn left or
                          a two-way left-turn lane directly to the left.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you may turn left or right if the road ahead
                        allows it.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1043, 8.05 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road, and ahead there is a section of road that
                        appears to continue straight, possibly leading to an intersection or another section
                        of the road. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the travel lanes, beyond which
                        there is a barrier/shoulder.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): A white dashed line marking the separation between lanes.;
                        line:stop_line (full): A solid white line marking the right edge of the travel lanes.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        white dashed line on the left fits the role of a lane_line, and the solid white line
                        on the right fits the role of an edge_line. | markings: The markings observed (dashed
                        line, solid line) are consistent with the boundaries and do not contradict each other.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits crossing the lane line.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white line, and
                        [CN-4.2.2-a] implies that a solid line prohibits crossing (though this is an edge
                        line, the solid nature suggests restriction).
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which allows you to go straight. You may change left
                        because the lane line is dashed, but changing right is prohibited by the solid edge
                        line. Since there are no turn markings, you can proceed straight without needing to
                        stop for a turn.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1206, 7.17 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes traveling in the same
                        direction ahead. The road continues into the distance without an immediate
                        intersection visible. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the travel lanes.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (partial): A dashed white line marking the separation between lanes.;
                        line:crosswalk (partial): A dashed white line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The markings observed are dashed white
                        lines, which are consistent with lane markings. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: By form, road markings fall into four classes, including lines: solid
                        or broken lines on the pavement, on curbs or on vertical surfaces. [[CN-4.2.3-a]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, and
                        [CN-5.4.3] dictates the edge line on the right side of the direction of travel shall
                        be white, but no rule prohibits changing into the area beyond it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you may proceed straight or turn if safe, but
                        you should be aware of the lane separation markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1142, 7.35 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with an overpass ahead. My car is in the
                        rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a yellow broken line separating my lane from the adjacent lane to the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the yellow dashed line on the left indicates another lane to the left, and the white
                        solid line on the right indicates the edge of the roadway. | roles: The yellow dashed
                        line on the left fits the role of a lane_line separating traffic in the same
                        direction, and the white solid line on the right fits the role of an edge_line. |
                        markings: There are no arrows, words, or areas in my lane to check against the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers the general absence of a right-turn
                        restriction marking in this context. [null]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a yellow dashed line, which means
                        it may be crossed [CN-4.2.2-a].
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a solid white edge line, and no
                        rule prohibits changing right into the shoulder/beyond the edge line.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane restricting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings in my lane governing a left
                        turn.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings in my lane governing a right
                        turn.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the observations and rules; no action is allowed
                        against a prohibition, and all decisions are based on visible features.
Advice                  You are in the rightmost lane, which allows you to go straight or change left or
                        right. Since there are no specific lane control markings, you should proceed with
                        caution, keeping in mind the yellow dashed line allows lane changes to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1055, 7.26 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway with multiple lanes heading in the same
                        direction, and it appears to continue straight ahead into the distance. (lanes 3, mine
                        2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line marking the separation between
                        lanes.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left boundary is a lane line, right boundary is a lane line). | roles: The color and
                        pattern of both boundaries (white dashed lines) fit the role of a lane_line. |
                        markings: The lane markings observed (a white dashed line) are consistent with the
                        boundaries, although the specific marking listed (line:stop_line) is not clearly
                        visible or identifiable as such. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits crossing the lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you should proceed with caution.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1040, 6.64 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway with a clear view ahead, suggesting a
                        continuous stretch of road rather than an immediate intersection or ramp end. My car
                        is in the rightmost lane visible in the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): A white dashed line marking the separation between lanes.;
                        line:crosswalk (full): A white dashed line marking the separation between lanes.;
                        line:crosswalk (full): A white dashed line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a white dashed lane line, which fits the role of separating traffic
                        in the same direction. The right boundary is a solid white edge line, which fits the
                        role of marking the edge of the roadway. | markings: The lane markings observed are
                        white dashed lines, which are consistent with lane lines, and they do not contradict
                        the boundaries or each other. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: Road markings fall into four classes, and lines are solid or broken
                        lines on the pavement, on curbs or on vertical surfaces. [[CN-4.2.3-a]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken white lane line, which
                        permits crossing according to [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited, as the right boundary is a solid white edge line,
                        which implies the edge of the roadway.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited markings
                        in my lane, and the boundaries do not restrict going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited markings in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited markings in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited markings in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed against a prohibition, and all decisions are based on visible features.
Advice                  You may change lanes to the left, and you are permitted to proceed straight ahead.
                        Changing to the right is prohibited by the solid edge line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1187, 7.06 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        section where the road configuration changes. My car is in the lane closest to the
                        center of the visible road. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A dashed white line runs down the center of the road,
                        separating the lanes.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a dashed white lane line, and the right boundary is a solid white
                        edge line, which fits their roles. | markings: The dashed white line observed is
                        interpreted as a stop line, which is a line across the lane. This marking is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane line, and
                        [CN-5.2.1-2] permits the crossable lane line to be crossed.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid white edge
                        line, but no rule prohibits changing right across this line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there is
                        a stop line ahead, you must stop before entering the intersection if you intend to
                        turn or if required by traffic control not visible here.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1071, 7.26 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and the road continues ahead without an
                        immediate intersection or end visible in the frame. My car is in the center of the
                        visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific arrows, words, symbols, areas, or lines are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in a lane between two other lanes). | roles:
                        The white dashed lines fit the role of a crossable lane line separating traffic in the
                        same direction. | markings: There are no markings in my lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No rule passage specifically governs the absence of a prohibited
                        movement marking in this context.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed lane
                        line, and [CN-5.2.1-2] permits crossing the lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and [CN-5.2.1-2] permits crossing the lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in a lane that allows lane changes in both directions, and you may proceed
                        straight. Since there are no specific markings for turning, you should follow general
                        road rules for turning.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1046, 7.49 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and ahead there is a continuation of the
                        road with multiple lanes. (lanes 5, mine 3, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): White dashed line marking the lane boundary to the
                        left.; line:stop_line (insufficient): White dashed line marking the lane boundary to
                        the right.
Step 4  Cross-check     position: The lane count (5) and my lane position (3) agree with the boundary roles
                        (lane lines on both sides). | roles: The white dashed lines fit the role of a
                        crossable lane line separating traffic in the same direction. | markings: The lane
                        markings listed are just the lane boundaries, which are consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a dashed line, and [CN-5.2.3]
                        allows lane changes where crossable lane lines are used.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed line, and [CN-5.2.3]
                        allows lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane.
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane.
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules, as the dashed lines permit
                        lane changes and no markings restrict straight movement.
Advice                  You may change lanes left or right as the lane lines are broken, and you may proceed
                        straight ahead. Use the lane markings and signs to determine the appropriate lane for
                        your intended movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1042, 6.93 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is an intersection where the road
                        continues. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no markings in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers the absence of a right-turn prohibition
                        marking. [null]
Step 6  change_left     prohibited (WRONG, label not_determined): The left boundary is a solid white
                        lane_line, and [CN-6.2.1] prohibits vehicles on the solid-line side from crossing.
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a solid white edge_line,
                        and [CN-5.4.3] indicates the edge line is white, but no rule explicitly prohibits
                        changing right based on this line alone.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No marking governs this action, and there is no left boundary line to
                        govern it.
Step 6  turn_right      not_applicable: No marking governs this action, and there is no right boundary line to
                        govern it.
Step 6  u_turn          not_applicable: No marking governs this action, and there is no boundary line to
                        govern it.
Step 6  enter_waiting_areanot_applicable: No marking governs this action as there is no left-turn waiting area
                          or two-way left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; no action is allowed when
                        prohibited, and all decisions are based on visible features.
Advice                  You are in the left lane, and lane changes to the left are prohibited by the solid
                        white line. You may proceed straight or change right, but you should be aware of the
                        intersection ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7591, out 1011, 6.88 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection where the
                        road continues. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no markings in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A single solid white lane line prohibits vehicles on the solid-line
                        side from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane_line, and
                        [CN-6.2.1] prohibits vehicles on the solid-line side from crossing.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: There is no marking governing this
                        action, and the right boundary is a solid white edge_line, which does not prohibit
                        lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         All actions are decided based on the observed features and the cited rules, and no
                        prohibited action is allowed.
Advice                  You may change right, go straight, or proceed as normal, but you are prohibited from
                        changing left. Since there are no specific markings for turns, you should proceed with
                        caution towards the junction.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7591, out 1044, 6.9 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards a bridge structure ahead. My car is in one
                        of the lanes near the bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The absence of markings in my lane is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers the absence of a right turn restriction
                        marking in my lane. [null]
Step 6  change_left     prohibited (WRONG, label not_determined): allowed: The left boundary is a solid white
                        lane_line, and [CN-6.2.1] states that vehicles on the solid-line side may not cross,
                        but since the line is solid, it prohibits crossing, which means changing left is
                        prohibited.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: The right boundary is a solid white
                        edge_line, and [CN-5.4.3] states that an edge line on the right side of the direction
                        of travel shall be white, which does not prohibit changing right.
Step 6  go_straight     allowed (contested, correct): allowed: No marking governs this action, and the
                        boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right, but changing left is prohibited by the solid
                        white lane line. Since there are no specific turn markings, you can proceed as usual.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7591, out 1074, 7.03 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        section where lane guidance is present. My car is in one of the lanes near the bottom
                        of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a yellow solid line separating my lane from the adjacent lane on the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a white solid line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A white solid line marking the end of the current lane
                        structure ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        yellow solid line on the left indicates another lane to the left, and the white solid
                        line on the right indicates the edge of the roadway. | roles: The yellow solid line on
                        the left fits the role of a lane_line separating traffic in the same direction, and
                        the white solid line on the right fits the role of an edge_line. | markings: The stop
                        line is consistent with the lane structure ahead. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a yellow solid line and
                        [CN-6.2.1] prohibits vehicles on the solid-line side from crossing.
Step 6  change_right    allowed (WRONG, label prohibited): allowed, because the right boundary is a white
                        solid edge line, and no rule prohibits changing right across an edge line.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right, but changing left is prohibited by the solid
                        yellow line. You must stop at the solid white line ahead if you intend to stop or
                        yield.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1064, 8.66 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific lane markings like arrows, text, or areas
                        are visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no markings in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No rule passage specifically governs the absence of a right-turn
                        restriction in this context. [null]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed, as the left boundary is a broken line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    prohibited (correct): Prohibited, as the right boundary is a solid line, and
                        [CN-4.2.2-a] prohibits crossing a solid line (unless in an emergency).
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane restricting
                        straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: Not_applicable, as there are no markings indicating a permitted left
                        turn.
Step 6  turn_right      not_applicable: Not_applicable, as there are no markings indicating a permitted right
                        turn.
Step 6  u_turn          not_applicable: Not_applicable, as there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid edge
                        line. You may proceed straight ahead, but turning left, right, or making a U-turn is
                        not explicitly permitted by the visible markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1011, 7.06 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and there is a road ahead that
                        appears to continue straight, possibly leading to an intersection or another section
                        of the road. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (solid) of both boundaries fit the role of a lane_line. |
                        markings: The lack of markings in my lane is consistent with the boundaries defining
                        the lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this marking, but since it is not
                        visible, it does not restrict movement. [null]
Step 6  change_left     prohibited (correct): Prohibited by the left_boundary because it is a solid white
                        lane_line, and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the right_boundary because it is a
                        solid white lane_line, and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines on both sides. You are permitted to proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1046, 6.74 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        section where lane configuration changes ahead. My car is in the lane closest to the
                        center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific arrows, words, symbols, areas, or lines are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no markings in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No rule passage specifically governs the absence of a 'no_turn:right'
                        marking in this context. [null]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed, as the left boundary is a broken line, and
                        [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited, as the right boundary is a solid
                        line, and [CN-4.2.2-a] implies that a solid line prohibits crossing (though this is an
                        edge line, the solid nature restricts movement beyond it).
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane restricting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings indicating a permitted or
                        prohibited left turn.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings indicating a permitted or
                        prohibited right turn.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings indicating a permitted or
                        prohibited U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed against a prohibition, and all decisions are based on visible features.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid edge
                        line. You may proceed straight ahead, but turning left, right, or making a U-turn is
                        not governed by any visible markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1057, 7.47 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where the road
                        continues. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no markings in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not seen. [null]
Step 6  change_left     prohibited (WRONG, label allowed): allowed: The left boundary is a solid white
                        lane_line, and [CN-6.2.1] states that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, and
                        [CN-5.4.3] states that an edge line on the right side of the direction of travel shall
                        be white, which does not prohibit changing right.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You may change right, go straight, or proceed as normal, but changing left is
                        prohibited by the solid white lane line. Since there are no specific markings for
                        turns, you should proceed with caution at the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7591, out 1052, 6.76 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a junction or
                        intersection where the road continues and potentially changes direction. (lanes 2,
                        mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The white arrow in my lane indicates a
                        permitted direction of travel, which is consistent with the lane markings. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane_line, and
                        [CN-6.2.1] prohibits vehicles on the solid-line side from crossing.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a solid white
                        edge_line, and there is no rule prohibiting a lane change based on this boundary.
Step 6  go_straight     allowed (correct): allowed: The arrow in my lane indicates straight ahead or right,
                        and [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in my lane only indicates straight ahead
                        or right, and [CN-5.13.1] restricts the direction of travel.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed: The arrow in my lane indicates straight
                        ahead or right, and [CN-5.13.1] indicates the direction of travel.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane only indicates straight ahead
                        or right, and [CN-5.13.1] restricts the direction of travel.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a left-turn waiting area
                          or a two-way left-turn lane in view.
Step 7  Reflect         consistent
Advice                  You may change right, go straight, or turn right. You must not change left, turn left,
                        or make a U-turn. The lane markings indicate you should proceed straight or turn
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight']), actions False, unsafe
                        ['turn_right'], citation accepted, contradictions ['leftmost lane, but a lane line on
                        the left']
Tokens                  in 7591, out 1052, 6.76 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where the road appears
                        to continue or change direction. (lanes 2, mine 1, full)
Step 2  Left            There is a yellow solid line separating my lane from the adjacent lane on the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a white solid line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        yellow solid line on the left indicates another lane to the left, and the white solid
                        line on the right indicates the edge of the roadway. | roles: The yellow solid line on
                        the left fits the role of a lane_line separating traffic in the same direction, and
                        the white solid line on the right fits the role of an edge_line. | markings: There are
                        no arrows, words, or areas in my lane to check against the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not seen. [null]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a yellow solid line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a white solid
                        edge line, and no rule prohibits changing right across an edge line.
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
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right into the adjacent lane. Changing left is
                        prohibited by the solid yellow line. Since no specific turn markings are visible,
                        turning left or right is not governed by lane markings.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation unlisted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 7591, out 1051, 6.94 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a clear road
                        section leading towards what appears to be an intersection or a continuation of the
                        road. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (solid) of both boundaries fit the role of a lane_line. |
                        markings: The lack of markings in my lane is consistent with the boundaries defining
                        the lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: A single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so its effect is
                        determined by the general rules. [null]
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid white lane_line
                        and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    prohibited (correct): prohibited, because the right_boundary is a solid white
                        lane_line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines on both sides. You are permitted to proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 7591, out 1035, 6.93 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the lane
                        closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line marking the right edge of the travel lane.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A blue overhead sign with three upward arrows is visible ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a broken white lane line, and the right boundary is a solid yellow
                        edge line, which fits their roles. | markings: The overhead arrow indicates straight
                        movement, which is consistent with the lane markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and the
                        upward arrow indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label not_determined): allowed: The left boundary is a broken white
                        lane line, and [CN-5.2.1-2] permits the crossable lane line to separate traffic flows
                        in the same direction.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid yellow
                        edge line, and [CN-6.1.1] implies that solid lines prohibit crossing, although this is
                        an edge line, the solid nature restricts movement.
Step 6  go_straight     allowed (contested, correct): allowed: The overhead arrow indicates straight ahead,
                        and [CN-5.13.1] confirms this direction of travel.
Step 6  turn_left       not_applicable: not_applicable: There is no marking in my lane that governs turning
                        left.
Step 6  turn_right      not_applicable: not_applicable: There is no marking in my lane that governs turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There is no marking in my lane that governs U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a left-turn waiting area
                          or a two-way left-turn lane in my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but changing right is prohibited by the solid yellow
                        edge line. You are permitted to go straight ahead, but turning left, right, or making
                        a U-turn is not governed by any markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1061, 7.09 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where the road appears
                        to continue or change direction. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a crossable
                        lane line separating traffic in the same direction. | markings: The lack of specific
                        markings in the lane is consistent with the boundaries defining the lane. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed line, and [CN-5.2.1-2]
                        permits crossing the lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed line, and
                        [CN-5.2.1-2] permits crossing the lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted as the boundaries are
                        dashed. You may proceed straight, but turning left, right, or making a U-turn is not
                        governed by any specific marking in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1040, 6.82 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is no painted line visible to the right of my lane; the lane appears to end near
                        the shoulder/curb area.
                        none none, curb no, edge_line, evidence partial
Step 3  Markings        line:stop_line (full): A solid white line marking the stop line is visible ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line (or the end
                        of the road). | roles: The left boundary is a broken white line, consistent with a
                        crossable lane line [CN-5.2.1-2]. The right boundary has no line, consistent with an
                        edge_line where no marking is present. | markings: The stop line is present ahead,
                        which governs the stopping action. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken white line, which means
                        crossing is permitted [CN-4.2.2-a].
Step 6  change_right    not_determined (correct): Not determined, as the right boundary has no painted line
                        and no curb, leaving the action undecided.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed while a rule prohibits it.
Advice                  You may change lanes to the left, and you are permitted to go straight ahead. You must
                        stop at the solid white stop line before proceeding through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1098, 7.57 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        indicated by lane markings and street signs. (lanes 2, mine 1, full)
Step 2  Left            There is a yellow solid line on the left side of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           There is a white broken line on the right side of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        yellow solid line on the left acts as a center_line, and the white broken line on the
                        right acts as a lane_line separating my lane from the adjacent lane. | roles: The
                        yellow solid line on the left fits the role of a center_line separating opposing
                        traffic flows, and the white broken line on the right fits the role of a lane_line
                        separating traffic flows in the same direction. | markings: The white arrow pointing
                        straight ahead in my lane agrees with the boundaries; it indicates the allowed
                        movement within the lane. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and a
                        straight arrow indicates travel straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The yellow solid line on the left acts
                        as a center_line, and [CN-6.1.1] prohibits crossing.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The white broken line on the right acts as
                        a lane_line, and [CN-5.2.1-2] permits crossing.
Step 6  go_straight     allowed (contested, correct): allowed: The white arrow pointing straight ahead in my
                        lane indicates travel straight ahead, and [CN-5.13.1] defines this direction.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing this action, and there is no left-turn waiting area or two-way left-
                        turn lane.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing this action, and there is no left-turn waiting area or two-way left-
                        turn lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing this action, and there is no left-turn waiting area or two-way left-
                        turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is restricted from changing left due to the solid
                        yellow center line. You may change right into the adjacent lane, or proceed straight
                        ahead. No specific waiting area is marked for turning.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1113, 6.76 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with trees lining the sides, and an intersection is
                        visible ahead. My car is in one of the lanes near the bottom of the photo. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a yellow broken line separating my lane from the lane to the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible across the lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the yellow dashed line on the left indicates a lane to the left, and the white dashed
                        line on the right indicates a lane to the right. | roles: The yellow dashed line on
                        the left is consistent with a lane_line separating traffic in the same direction, and
                        the white dashed line on the right is consistent with a lane_line separating traffic
                        in the same direction. | markings: There are no arrows, words, or areas in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a dashed line, and [CN-5.2.1-2]
                        permits crossing the lane line.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed, as the right boundary is a dashed line,
                        and [CN-5.2.1-2] permits crossing the lane line.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in the lane
                        restricting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings in the lane governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings in the lane governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings in the lane governing this
                        action.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You are in the middle lane, and lane changes are permitted as the lane lines are
                        broken. You may proceed straight, but be aware of the stop line ahead if you need to
                        stop.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7591, out 1034, 6.66 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a stretch of
                        road leading towards what appears to be an intersection or a continuation of the road
                        with buildings on the right. (lanes 3, mine 2, full)
Step 2  Left            There is no visible painted line or curb on the left side of my lane in the visible
                        stretch.
                        none none, curb no, unknown, evidence insufficient
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the right edge of my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        right boundary is a lane_line, and the left boundary is unknown/no line, suggesting my
                        lane is not the leftmost or rightmost defined by lines, but the right boundary
                        confirms it is not the rightmost lane if the right boundary is a lane line. | roles:
                        The right boundary is white and dashed, which is consistent with a crossable lane line
                        ([CN-5.2.1-2]). The left boundary has no visible markings, which is consistent with an
                        unknown role. | markings: The marking observed is a white dashed line, which is
                        interpreted as a stop line in the list, but based on the visual evidence (a dashed
                        line near the end of the visible road), it is more likely a lane line or a guide line,
                        not a stop line, as stop lines are typically solid white ([CN-6.4.1-2]). I will treat
                        the visible dashed line as a lane line for the purpose of lane change rules, but note
                        the ambiguity. | unseen: I did not report any attribute I did not actually see. |
                        result: corrected
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary has no visible line, so no marking
                        prohibits a lane change to the left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane line, and
                        [CN-5.2.1-2] permits crossing the lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no left-turn waiting areas or two-way
                          left-turn lanes visible.
Step 7  Reflect         The actions are consistent with the observations, noting the ambiguity of the final
                        dashed line marking.
Advice                  You may change lanes both left and right, and you may proceed straight ahead. Since
                        there are no specific markings for turning, you should proceed with caution if you
                        intend to turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['change_left decided although that side cannot be seen']
Tokens                  in 7591, out 1102, 7.31 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the lane
                        closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted on the road.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a broken white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The white arrow pointing straight ahead
                        is consistent with the lane markings and boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and a
                        straight arrow indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited: The left boundary is a broken
                        white lane_line, and [CN-5.2.1-2] states it is a crossable lane line, but no specific
                        rule prohibits the change, however, the lane line indicates a change may be needed,
                        and the arrow only permits straight.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: The right boundary is a solid white
                        edge_line, and [CN-5.4.3] states the edge line on the right side of the direction of
                        travel shall be white, which does not prohibit changing right.
Step 6  go_straight     allowed (correct): allowed: The lane marking is an arrow:straight, and [CN-5.13.1]
                        indicates this allows straight ahead movement.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane governing this action, and no left-turn waiting
                        area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane governing this action, and no left-turn waiting
                        area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane governing this action, and no left-turn waiting
                        area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; the arrow governs the
                        straight movement, and the boundaries do not prohibit the right change.
Advice                  You are permitted to go straight or change right, but changing left is prohibited by
                        the lane line configuration. Since there are no specific markings for turning, you
                        should proceed straight or change right if necessary.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_right', 'line:stop_line']), actions False,
                        unsafe [], citation accepted, contradictions ['change_left prohibited across a broken
                        lane line']
Tokens                  in 7591, out 1133, 7.86 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards a bridge or overpass structure ahead. My car
                        is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific lane markings like arrows, text, or areas
                        are visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in the middle lane of three). | roles: The
                        solid white lines fit the role of a lane_line separating traffic in the same
                        direction. | markings: The lack of visible markings in my lane is consistent with the
                        boundaries defining the lane. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so its allowance or
                        prohibition cannot be determined based on the provided rules. [null]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the left_boundary because the solid
                        white line prohibits crossing according to [CN-6.2.1].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the right_boundary because the
                        solid white line prohibits crossing according to [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines on both sides. You are allowed to proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1024, 6.73 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an overpass ahead, and my car is in one of the lanes
                        approaching the overpass. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a crossable
                        lane line separating traffic in the same direction. | markings: The lack of specific
                        markings in my lane is consistent with the boundaries defining the lane structure. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so its meaning is not
                        determined by the provided rules. [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits the crossing of a broken white line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits the crossing of a broken white line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted as the lane lines are
                        broken. You may proceed straight, but turning movements are not governed by any
                        specific markings in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1050, 6.71 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection in the distance. My car is
                        in the lane closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: The lack of specific markings in
                        my lane is consistent with the boundaries defining the lane. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so its allowance or
                        prohibition cannot be determined based on the provided rules. [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white line, and [CN-5.2.1-2]
                        permits crossing the crossable lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a broken white line,
                        and [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You are in a lane that allows lane changes in both directions, and you may proceed
                        straight ahead. Since there are no specific markings for turning, you should proceed
                        straight unless you intend to turn, in which case you must check for appropriate
                        turning lanes or signals.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1069, 6.67 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an overpass/bridge structure ahead. My car
                        is in one of the lanes near the bottom of the photo. (lanes 2, mine 1, full)
Step 2  Left            There is no visible painted line or curb on the left side of my lane in the visible
                        stretch.
                        none none, curb no, unknown, evidence insufficient
Step 2  Right           The right boundary is defined by a solid white line separating my lane from an
                        adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings (arrows, text, symbols, areas, or
                        lines) are visible within my lane in the photo.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        right boundary is a lane_line, indicating another lane to the right, and the left
                        boundary has no line, suggesting it is the leftmost lane or the edge of the
                        road/shoulder. | roles: The right boundary is white and solid, which is consistent
                        with a lane line separating traffic in the same direction, although the specific rule
                        for a solid white lane line is not fully detailed in the provided passages for this
                        context. | markings: There are no markings in my lane to check against the boundaries.
                        | unseen: I did not report any attribute I did not actually see. | result: consistent
Step 5  Rule            left_boundary: No rule passage applies to the left boundary as no line or curb was
                        observed. [null]
Step 5  Rule            right_boundary: A no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 5  Rule            no_turn:right: No specific rule passage applies to the absence of a prohibited
                        movement marking in my lane. [null]
Step 6  change_left     not_applicable (WRONG, label prohibited): not_applicable
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         All actions are decided based on the observed features and rules, and no prohibited
                        action is allowed.
Advice                  You are in the leftmost lane and should proceed straight ahead. Lane changes to the
                        right are prohibited by the solid white lane line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 917, 6.44 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the lane
                        closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane to
                        my left.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a broken white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The arrows in my lane show straight
                        ahead, which is consistent with the lane markings and boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates straight ahead. [[CN-5.13.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed, as the left boundary is a broken white
                        lane_line, and [CN-5.2.1-2] permits the crossable lane line to separate traffic flows
                        in the same direction.
Step 6  change_right    prohibited (correct): Prohibited, as the right boundary is a solid white edge_line,
                        and while no specific rule prohibits changing onto the shoulder, the solid line
                        suggests a defined edge.
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed, as the arrow in my lane shows straight
                        ahead, and [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not_applicable, as there is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label allowed): Not_applicable, as there is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not_applicable, as there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which permits going straight ahead. You may change left
                        into the adjacent lane, but changing right is prohibited by the solid edge line. No
                        specific stopping or waiting areas are marked.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right', 'line:stop_line']), actions False, unsafe
                        ['change_left', 'go_straight'], citation accepted, contradictions []
Tokens                  in 7591, out 1134, 6.8 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes traveling in the same
                        direction ahead. The road continues straight ahead into the distance. (lanes 3, mine
                        2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the boundary between my lane and
                        the lane to my right.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a crossable
                        lane line separating traffic in the same direction. | markings: The stop line marking
                        is located at the end of the visible lane area, consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits crossing the lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed against a prohibition.
Advice                  You may change lanes left or right as the lane lines are broken, and you may proceed
                        straight. Since there is a stop line visible ahead, you should prepare to stop if
                        required by an intersection or traffic control not visible in the photo.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1074, 4.03 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway with multiple lanes traveling in the same
                        direction ahead. The road continues into the distance without an immediate
                        intersection visible. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): A speed limit marking of 80 is painted on the lane.;
                        text:speed_limit (full): A speed limit marking of 60 is painted on the lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (both boundaries are lane lines, indicating adjacent lanes in the same direction). |
                        roles: The color (white) and pattern (dashed) of both boundaries fit the role of a
                        lane_line. | markings: The speed limit markings are placed within the lane and do not
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            text:speed_limit: Pavement speed limit markings show the speed limit of a lane and are
                        placed at the start of the lane and at other suitable places where the maximum speed
                        is limited. [[CN-5.14.2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken line, and [CN-5.2.1-2]
                        permits crossing the crossable lane line.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed, as the right boundary is a broken line,
                        and [CN-5.2.1-2] permits crossing the crossable lane line.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in the lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings indicating a turn left.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings indicating a turn right.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You may change lanes left or right as the lane lines are broken, and you may proceed
                        straight ahead. Be mindful of the posted speed limits of 80 and 60.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 7591, out 1055, 6.89 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a road section that appears to continue,
                        possibly leading to an intersection or a change in road configuration, with a bus
                        visible in the right lane. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line (indicating a lane to the left), and the right
                        boundary is a lane line (indicating a lane to the right). | roles: The color and
                        pattern of both boundaries (solid white lines) fit the role of a lane line separating
                        lanes in the same direction. | markings: There are no arrows, words, or areas in my
                        lane to contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a solid white lane line, and no
                        rule prohibits crossing from the broken side (though this line is solid, the rule for
                        solid lines prohibits crossing, but since no specific prohibition is given for a solid
                        lane line in this context, and it is not a no-crossing line, it is not prohibited by
                        the boundary itself, but the rule [CN-6.2.1] applies to no-crossing lines, which this
                        is not explicitly stated to be, so it is not prohibited by the boundary).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited, as the right boundary is a solid white
                        lane line, and [CN-6.2.1] applies to no-crossing lane lines, which this is not
                        explicitly stated to be, but the solid line generally prohibits crossing.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings indicating a permitted turn
                        left.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings indicating a permitted turn
                        right.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; the solid lane lines
                        restrict lane changes, and the lack of arrows/areas leaves turns and waiting area
                        entry as not applicable.
Advice                  You are in the middle lane; you may proceed straight ahead. Lane changes to the left
                        are permitted, but changing right is prohibited by the solid white lane line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1113, 8.28 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a clear view ahead, suggesting a straight road
                        section rather than an immediate intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white solid line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (full): There are no arrows, words, symbols, areas, or lines painted
                        within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        white dashed line on the left fits the role of a crossable lane_line (CN-5.2.1-2), and
                        the white solid line on the right fits the role of an edge_line (CN-5.4.3). |
                        markings: The absence of markings in the lane is consistent with the boundaries
                        defining the lane. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage applies to the absence of a right-turn
                        prohibition marking in this context. [null]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken line, which means it may
                        be crossed (CN-4.2.2-a).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited, as the right boundary is a solid line,
                        which means crossing is normally prohibited (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in the lane
                        restricting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings indicating a permitted or
                        prohibited left turn.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings indicating a permitted or
                        prohibited right turn.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings indicating a permitted or
                        prohibited U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed against a prohibition, and all decisions are based on visible features.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid edge
                        line. You are permitted to go straight ahead in your current lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1038, 6.76 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera, and a continuation
                        of the road is visible ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A broken white line marking the right edge of my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (dashed) of both boundaries fit the role of a lane_line. |
                        markings: The line marking observed is a broken white line, which is consistent with
                        the lane boundaries, although the specific marking 'line:stop_line' is applied to the
                        right boundary line which is dashed, not solid as required for a stop line. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane_line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing in view restricts carrying on straight
                        along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there is
                        no stop line clearly visible in your lane, you do not need to stop unless required by
                        an intersection ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1029, 6.42 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway with multiple lanes traveling in the same
                        direction ahead. The road continues into the distance without an immediate
                        intersection or end. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line marking the separation between
                        lanes.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (dashed) of both boundaries fit the role of a lane_line. |
                        markings: The single marking observed (a white dashed line) is consistent with the
                        boundaries, although its specific role as a stop line is not fully confirmed by the
                        visual evidence. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-5.2.1-2]
                        permits crossing the lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and [CN-5.2.1-2] permits crossing the lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you may proceed straight or change lanes to
                        prepare for a turn if the road ahead allows it.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1075, 7.03 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road under an overpass. Ahead, the road
                        continues, and there is a visible merging/exit area to the right. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the adjacent area/lane to the
                        right.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid yellow line runs along the right boundary, and
                        a dashed white line runs along the left boundary, with no other markings visible in
                        the immediate lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a white dashed lane_line, which fits the role. The right boundary is
                        a solid yellow edge_line, which fits the role. | markings: The observed markings
                        (solid yellow line on the right, dashed white line on the left) are consistent with
                        the roles assigned to the boundaries. The reported line:stop_line is not clearly
                        visible or identifiable as a stop line. | unseen: No attributes were reported that
                        were not actually seen, although the stop line marking is not clearly visible. |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed, as the left boundary is a broken white
                        lane_line, and [CN-5.2.1-2] permits the crossable lane line to separate traffic flows
                        in the same direction.
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited, as the right boundary is a solid
                        yellow edge_line, and [CN-6.1.1] implies that solid lines prohibit crossing (though
                        this rule is primarily for center lines, the solid nature of the edge line suggests
                        restriction).
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; the right boundary's solid
                        nature restricts lane changes, and the lack of markings dictates the other movements.
Advice                  You are in the middle lane; you may change left, but changing right is prohibited by
                        the solid yellow line. You may proceed straight, but turning left, right, or making a
                        U-turn is not governed by any visible markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1227, 7.47 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road, and ahead there is a continuation of the
                        road, not an intersection or ramp end visible in the immediate lane. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a white broken line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line (separating from lane 1) and the right boundary is a
                        lane_line (separating from lane 3). | roles: The color (white) and pattern (dashed) of
                        both boundaries fit the role of a lane_line. | markings: The lack of visible markings
                        in my lane is consistent with the boundaries defining the lane. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No rule passage specifically governs this element as it was not
                        observed.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a broken white
                        lane_line, and [CN-5.2.1-2] permits the crossing of a broken lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a broken white lane_line, and
                        [CN-5.2.1-2] permits the crossing of a broken lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you may proceed straight, but be aware of
                        surrounding traffic when changing lanes.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1072, 7.46 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes traveling in the same
                        direction ahead. The road continues straight ahead into the distance. (lanes 3, mine
                        2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings observed in the lane.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no arrows, words, or areas in
                        the lane to contradict the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white lane_line, and
                        [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, and
                        [CN-5.4.3] defines the edge line on the right side of the direction of travel as
                        white.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may change left or right, or proceed straight
                        ahead. Since there are no specific markings for turns, you may proceed straight or
                        change lanes as needed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1057, 6.88 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes traveling in the same
                        direction ahead. The road continues into the distance without an immediate
                        intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): A broken white line is visible in the lane to the left
                        of my lane, indicating a lane boundary.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The only listed marking is insufficient
                        to check against boundaries or other markings. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: No specific rule passage was found that governs this marking.
Step 6  change_left     prohibited (WRONG, label not_determined): The left boundary is a solid white
                        lane_line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (correct): The right boundary is a solid white edge_line, and [CN-5.4.3]
                        mandates that the edge line on the right side of the direction of travel shall be
                        white, but no rule prohibits changing right.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or two-way left-turn lane is visible ahead
                          of my lane.
Step 7  Reflect         All actions are decided based on the observed features and the cited rules, and no
                        action is allowed against a prohibition.
Advice                  You may proceed straight or change right, but changing left is prohibited by the solid
                        white lane line. Since there are no turn markings, you may proceed straight or turn if
                        the intersection allows it.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1065, 6.93 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a clear view ahead, suggesting a long stretch of
                        road rather than an immediate intersection or ramp end. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): There are no lane-use arrows, words, symbols, areas, or lines
                        painted within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a crossable
                        lane line separating traffic in the same direction. | markings: The absence of
                        markings in my lane is consistent with the boundaries defining the lane. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers the general absence of a prohibited
                        movement marking in this context. [null]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and [CN-5.2.1-2] permits crossing the lane line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-5.2.1-2] permits crossing the lane line.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you may proceed straight, but you should be
                        aware of the lane markings indicating that lane changes are permitted.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1041, 7.01 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway, and ahead there is an elevated structure
                        or overpass, suggesting continued travel on the road. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or lines are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line (separating from lane 1), and the right boundary is a
                        lane_line (separating from lane 3). | roles: The white dashed lines fit the role of a
                        crossable lane_line, as per CN-5.2.1-2. | markings: The lack of markings in my lane is
                        consistent with the boundaries defining the lane structure. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, but since no marking
                        governs the action, it is not restricted by a marking. [null]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken line, and CN-5.2.1-2
                        permits crossing.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed, as the right boundary is a broken line,
                        and CN-5.2.1-2 permits crossing.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in my
                        lane, and boundaries do not govern going straight.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings indicating a turn left is
                        possible or restricted.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings indicating a turn right is
                        possible or restricted.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings indicating a U-turn is
                        possible or restricted.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the observations, as the broken lane lines permit lane
                        changes, and the absence of directional markings allows straight travel.
Advice                  You are in the middle lane of a multi-lane highway, and lane changes are permitted as
                        the lane lines are broken. You may proceed straight, but turning movements are not
                        governed by markings in this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1040, 6.91 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the lane
                        closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible in my lane from the bottom to
                        the end of the lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a broken white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no arrows, words, or areas in
                        my lane to contradict the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this marking as it was not seen. [null]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken line, and [CN-4.2.2-a]
                        permits crossing a broken line.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited, as the right boundary is a solid line,
                        and [CN-4.2.2-a] prohibits crossing a solid line.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane restricting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings in my lane governing a left
                        turn.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings in my lane governing a right
                        turn.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings in my lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid white
                        edge line. You may proceed straight ahead, but turning left, right, or making a U-turn
                        is not governed by any visible markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1022, 6.56 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test B | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a marked area that appears to be an
                        intersection approach or a designated zone. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): A large white marking showing the number '60' is painted on
                        the road surface.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles
                        (both are lane_lines). | roles: The white dashed lines fit the role of a crossable
                        lane line separating lanes in the same direction. | markings: The speed limit marking
                        is consistent with the lane markings and boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            text:speed_limit: Pavement speed limit markings show the speed limit of a lane and are
                        placed at the start of the lane and at other suitable places where the maximum speed
                        is limited. [[CN-5.14.2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white line, and [CN-5.2.1-2]
                        permits the crossing of a broken lane line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a broken white line,
                        and [CN-5.2.1-2] permits the crossing of a broken lane line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibitions in the lane, and
                        no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibitions in the lane, and
                        no right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibitions in the lane, and
                        no U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and rules, and no prohibited action
                        is allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. The speed
                        limit for this lane is 60. You should use the lane appropriate for your intended
                        movement, as no specific lane guidance is present.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 7591, out 1051, 6.97 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the lane closest
                        to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line marking the right edge of my lane.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): There are no lane-use arrows, words, symbols, areas, or
                        lines painted within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a broken white lane_line, and the right boundary is a solid yellow
                        edge_line, which fits the roles. | markings: The lack of markings in the lane is
                        consistent with the boundaries defining the lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a broken white
                        lane_line, and [CN-5.2.1-2] permits crossing.
Step 6  change_right    prohibited (contested, correct): Prohibited, as the right boundary is a solid yellow
                        edge_line, and [CN-6.1.1] implies that solid lines prohibit crossing (though this is
                        an edge line, the solid nature restricts movement).
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in the lane
                        restricting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not_applicable, as there are no markings in the lane governing a left
                        turn.
Step 6  turn_right      not_applicable: Not_applicable, as there are no markings in the lane governing a right
                        turn.
Step 6  u_turn          not_applicable: Not_applicable, as there are no markings in the lane governing a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         The actions are consistent with the observed markings and rules, and no action was
                        decided without the governing feature.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid yellow
                        edge line. You may proceed straight ahead, but turning left, right, or making a U-turn
                        is not governed by any markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1073, 7.23 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into a section with visible traffic control signs. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the photographed section.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a broken white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no markings in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not clearly
                        observed. [null]
Step 6  change_left     allowed (contested, correct): Allowed, as the left boundary is a broken line, and
                        [CN-5.2.1-2] permits crossing the lane line.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited, as the right boundary is a solid line,
                        and [CN-4.2.2-a] implies that a solid line prohibits crossing (though this is an edge
                        line, the solid nature restricts movement beyond it).
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in my
                        lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings indicating a turn left is
                        possible or restricted.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings indicating a turn right is
                        possible or restricted.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings indicating a U-turn is
                        possible or restricted.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed against a prohibition, and all decisions are based on visible features.
Advice                  You are in the middle lane, which allows you to go straight. You may change left into
                        the adjacent lane, but changing right is prohibited by the solid edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1047, 7.26 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a stretch of road leading towards what
                        appears to be an intersection or a continuation of the road with other traffic. (lanes
                        3, mine 2, full)
Step 2  Left            There is a yellow broken line marking the left boundary of my lane.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           There is a yellow dashed line marking the right boundary of my lane.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles,
                        as both boundaries are lane lines separating traffic in the same direction. | roles:
                        The yellow dashed lines fit the role of a lane line separating traffic flows in the
                        same direction, as per CN-5.2.1-2, although CN-5.2.1-2 specifies a broken white line
                        for crossable lane lines, and CN-4.3.2 specifies yellow lines separate opposing
                        traffic flows, which contradicts the role of a lane line separating same-direction
                        traffic if the yellow line is interpreted as a center line, but given the context of
                        multiple lanes in one direction, it functions as a lane divider. | markings: The lack
                        of markings in my lane is consistent with the boundaries being simple lane dividers. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so its meaning is not
                        determined by the provided rules. [null]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a dashed line,
                        and CN-4.2.2-a states a broken line means it may be crossed.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed line,
                        and CN-4.2.2-a states a broken line means it may be crossed.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting to turn left or
                          a two-way left-turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you may turn left or right if the road ahead
                        allows it.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['no_turn:right'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7591, out 1152, 7.38 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving forward. Ahead, there appears to be an
                        intersection or a change in road configuration. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid yellow line is visible in the distance, separating
                        opposing traffic.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The solid yellow line observed in the
                        distance is consistent with a boundary marking for opposing traffic, although its
                        exact role (stop_yield vs. center_line) is ambiguous without clearer context, but it
                        is noted as a marking. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white
                        lane_line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, but no rule
                        prohibits changing right across this line.
Step 6  go_straight     allowed (contested, correct): allowed: No arrow in my lane restricts carrying on
                        straight along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may change left or right as the lane line is
                        broken. You may proceed straight, but be aware of the stop-and-yield line ahead, which
                        requires you to stop completely before entering the intersection if you intend to turn
                        or proceed through it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe ['change_left'], citation
                        accepted, contradictions ['go_straight allowed without the stop that the STOP or 停
                        marking in my lane requires']
Tokens                  in 7591, out 1055, 6.98 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a yellow broken line separating my lane from the adjacent lane to the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the stop line for the intersection.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the yellow dashed line on the left indicates another lane to the left, and the white
                        solid line on the right indicates the edge of the roadway. | roles: The yellow dashed
                        line fits the role of a lane_line separating traffic in the same direction, and the
                        white solid line fits the role of an edge_line on the right side of the direction of
                        travel. | markings: The stop line is consistent with the lane boundaries and the
                        general road layout. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a yellow
                        dashed line, which is a crossable lane line, and [CN-5.2.3] allows lane changes where
                        such lines are used.
Step 6  change_right    prohibited (contested, correct): Prohibited, as the right boundary is a solid white
                        edge line, and while no specific rule prohibits changing onto the curb/shoulder, the
                        solid line suggests a fixed boundary.
Step 6  go_straight     allowed (correct): Allowed, as there are no arrows or prohibited-movement markings in
                        my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no right-turn arrow is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You are in the rightmost lane, which is suitable for proceeding straight or turning
                        right if permitted by signals. You must stop at the solid white stop line before
                        entering the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1090, 6.92 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a continuation
                        of the road, not an intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the adjacent lane on the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (partial): Yellow dashed lines are painted across the road ahead,
                        indicating lane division.; line:crosswalk (partial): Yellow dashed lines are painted
                        across the road ahead, indicating lane division.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is solid yellow, which is consistent with a lane line separating traffic
                        flows in opposite directions if it were a center line, but since it's a lane line,
                        it's a lane line separating same-direction traffic, and the color yellow suggests it
                        might be a center line or a special lane line, but based on the context of lane_line,
                        it's a lane line. The right boundary is solid white, consistent with an edge_line. |
                        markings: The crosswalk markings are present across the lane, but they do not
                        contradict the boundaries or each other. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: Road markings fall into four classes, including lines: solid or broken
                        lines on the pavement, on curbs or on vertical surfaces. [[CN-4.2.3-a]]
Step 6  change_left     prohibited (contested, label allowed): The left boundary is a solid yellow lane_line,
                        and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a solid white edge_line,
                        and [CN-5.4.3] mandates that the edge line on the right side of the direction of
                        travel shall be white, which does not prohibit a lane change.
Step 6  go_straight     allowed (contested, correct): There are no arrows or prohibited-movement markings in
                        my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: There are no arrows or prohibited-movement markings in my lane, and
                        there is no left-turn waiting area or two-way left-turn lane, so it is not applicable.
Step 6  turn_right      not_applicable: There are no arrows or prohibited-movement markings in my lane, and
                        there is no left-turn waiting area or two-way left-turn lane, so it is not applicable.
Step 6  u_turn          not_applicable: There are no arrows or prohibited-movement markings in my lane, and
                        there is no left-turn waiting area or two-way left-turn lane, so it is not applicable.
Step 6  enter_waiting_areanot_applicable: There is no left-turn waiting area or two-way left-turn lane, so it
                          is not applicable.
Step 7  Reflect         All actions are decided based on the observed markings and rules, and no action is
                        allowed when prohibited.
Advice                  You are in the middle lane, and you are prohibited from changing left due to the solid
                        yellow lane line. You may change right, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1214, 7.5 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the lane
                        closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the stop line for the intersection.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a dashed white lane line, and the right boundary is a solid white
                        edge line, which fits their roles. | markings: The stop line is located at the end of
                        the lane, consistent with the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a broken line,
                        and [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid line, and
                        [CN-4.2.2-a] prohibits crossing a solid line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but changing to the right is prohibited by the solid
                        white edge line. You may proceed straight through the intersection, but turning left,
                        turning right, or making a U-turn is not governed by any specific marking in your
                        lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1041, 6.34 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection where the
                        road continues and potentially merges or changes direction. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line (separating from lane 1), and the right boundary is a
                        lane_line (separating from lane 3). | roles: The color (white) and pattern (solid) of
                        both boundaries fit the role of a lane_line. | markings: The lack of visible markings
                        in my lane is consistent with the boundaries defining the lane. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so its allowance or
                        prohibition cannot be determined based on the provided rules. [null]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the left_boundary, as it is a solid
                        white lane_line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the right_boundary, as it is a solid
                        white lane_line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  go_straight     allowed (correct): Allowed because there are no arrows or prohibited-movement markings
                        in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines on both sides. You are permitted to proceed straight ahead through the junction.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed ['arrow:straight']), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 7591, out 1074, 8.71 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where the road appears to widen or change configuration. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the stop line is visible ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The left
                        boundary is a solid white lane_line, and the right boundary is a dashed white
                        lane_line, which fits the roles of separating lanes in the same direction. | markings:
                        The stop line is present ahead, which is consistent with the lane markings. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The broken white lane line means that the lane may be crossed.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white lane_line and [CN-6.2.1] prohibits vehicles on the solid-line side from
                        crossing.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a broken white lane_line and
                        [CN-5.2.1-2] means it may be crossed.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change right into the adjacent lane, or proceed straight ahead. You must stop
                        at the solid white line before entering the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7591, out 1034, 6.76 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in one of the lanes
                        near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the stop line.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (both are lane_lines). | roles: The white dashed lines fit the role of a crossable
                        lane line separating traffic in the same direction. | markings: The stop line is
                        consistent with the lane markings and boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label not_determined): allowed: The left boundary is a broken line,
                        and [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: The right boundary is a broken line,
                        and [CN-5.2.3] permits lane changes where crossable lane lines are used.
Step 6  go_straight     allowed (contested, label not_determined): allowed: Nothing restricts carrying on
                        straight along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. You should
                        stop at the marked stop line before proceeding through the intersection.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 977, 7.94 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards what appears to be an intersection or a
                        section where lanes converge/diverge. My car is in the rightmost lane visible near the
                        bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a yellow broken line separating my lane from the lane to the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line marking the right edge of the travel lanes, followed by a
                        red painted area.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): A yellow dashed line marking the boundary with the lane to
                        the left.; line:stop_yield (partial): A yellow dashed line marking the boundary with
                        the lane to the left.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        yellow dashed line on the left fits the role of a lane_line separating traffic in the
                        same direction, and the solid yellow line on the right fits the role of an edge_line.
                        | markings: The markings observed are lines that define the boundaries, and the
                        interpretation of the lines as stop_yield lines is based on their appearance near the
                        foreground, though the specific markings are not fully clear as stop_yield lines. |
                        unseen: I did not report any attribute I did not actually see, although the specific
                        nature of the foreground lines is partially obscured. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a yellow dashed lane_line,
                        and [CN-4.2.2-a] states a broken line means it may be crossed.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid yellow edge_line, and
                        [CN-6.1.1] implies that a solid line prohibits crossing, though this is an edge line.
Step 6  go_straight     allowed (contested, correct): There are no arrows or prohibitions in my lane, and the
                        boundaries do not govern going straight.
Step 6  turn_left       not_applicable: There are no arrows or prohibitions in my lane, and there is no left-
                        turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: There are no arrows or prohibitions in my lane, and there is no left-
                        turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: There are no arrows or prohibitions in my lane, and there is no left-
                        turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: There is no left-turn waiting area or two-way left-turn lane visible
                          ahead of my lane.
Step 7  Reflect         The actions are consistent with the observations and rules, noting that the right
                        boundary is an edge line, not a lane line, and the foreground markings are interpreted
                        as stop_yield lines.
Advice                  You are in the rightmost lane, which is suitable for proceeding straight or turning
                        right if permitted by signs. Be prepared to stop completely before entering the
                        intersection due to the stop-and-yield line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 7591, out 1238, 7.93 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test B | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line marking the edge of the roadway on the right side.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (partial): Yellow dashed lines marking the lane boundaries in the
                        distance.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a white dashed lane line, which fits the role of a lane_line. The
                        right boundary is a solid yellow line, which fits the role of an edge_line. |
                        markings: The crosswalk marking is visible in the distance and does not contradict the
                        boundaries or lane structure. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: No specific rule passage was found that dictates the action based on
                        the presence of a crosswalk marking.
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a broken line,
                        which means it may be crossed [CN-4.2.2-a].
Step 6  change_right    prohibited (contested, correct): Prohibited, as the right boundary is a solid line,
                        which means crossing is normally prohibited [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane
                        [CN-4.2.2-a].
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible [CN-5.13.1].
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible [CN-5.13.1].
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible [CN-5.5.1-3].
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed when a rule prohibits it.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid yellow
                        edge line. You may proceed straight ahead, but you should be aware of the crosswalk
                        markings ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1154, 7.74 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a section of road that appears to
                        continue straight, possibly leading to an intersection or another section of the road.
                        (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Two parallel yellow lines with white arrows pointing straight
                        ahead are visible in the lane ahead.; arrow:straight (full): Two parallel yellow lines
                        with white arrows pointing straight ahead are visible in the lane ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line (indicating a lane to the left), and the right
                        boundary is a lane line (indicating a lane to the right). | roles: The color and
                        pattern of both boundaries (solid white lines) fit the role of a lane line separating
                        lanes of the same direction. | markings: The arrows in my lane (straight ahead) agree
                        with the boundaries, as they indicate the allowed movement within the lane defined by
                        the boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and in
                        this case, they indicate straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white lane line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    prohibited (contested, correct): prohibited, because the right boundary is a solid
                        white lane line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  go_straight     allowed (contested, correct): allowed, because the lane marking shows an arrow
                        indicating straight ahead and [CN-5.13.1] indicates the direction of travel.
Step 6  turn_left       prohibited: prohibited, because there is no marking allowing a left turn in my lane
                        and the boundaries do not permit it.
Step 6  turn_right      prohibited: prohibited, because there is no marking allowing a right turn in my lane
                        and the boundaries do not permit it.
Step 6  u_turn          prohibited: prohibited, because there is no marking allowing a U-turn in my lane and
                        the boundaries do not permit it.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are permitted to proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1078, 6.37 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera, leading towards
                        what appears to be an intersection or a section where lane configuration changes
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane to
                        the right.; arrow:straight (full): A white arrow pointing straight ahead is visible in
                        the lane to the left.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line (indicating a lane to the left), and the right
                        boundary is a lane line (indicating a lane to the right). | roles: The color and
                        pattern of the boundaries fit their roles: the left boundary is a broken white lane
                        line, and the right boundary is a solid white lane line. | markings: The arrows in my
                        lane (straight ahead) agree with the boundaries and other markings; they indicate the
                        allowed movement for my lane. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and the
                        arrow in my lane shows that straight ahead is the indicated direction of travel.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the left boundary, as it is a broken
                        white lane line, which allows crossing from the broken side, but the lane line itself
                        governs lane change actions, and the rule for the left boundary is permissive for
                        crossing from the broken side, but the arrow in my lane only permits straight ahead.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the right boundary, as it is a solid
                        white lane line, which prohibits vehicles on the solid-line side from crossing.
Step 6  go_straight     allowed (correct): Allowed by the arrow in my lane, as the guide arrow indicates
                        straight ahead.
Step 6  turn_left       prohibited (correct): Prohibited by the arrow in my lane, as the guide arrow only
                        indicates straight ahead.
Step 6  turn_right      prohibited (correct): Prohibited by the arrow in my lane, as the guide arrow only
                        indicates straight ahead.
Step 6  u_turn          prohibited (correct): Prohibited by the arrow in my lane, as the guide arrow only
                        indicates straight ahead.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there are no markings for a waiting area or two-
                          way left-turn lane in my lane.
Step 7  Reflect         Consistent, as the lane change actions are governed by the boundaries and the movement
                        actions are governed by the lane arrow, and the reasons correctly reflect these
                        governing features.
Advice                  You should stay in your current lane to proceed straight ahead, as the lane arrow only
                        permits this movement. Lane changes to the left or right are prohibited by the lane
                        markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 7591, out 1182, 8.18 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection, and my car is in one of the
                        lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane to
                        my right.; arrow:straight (full): A white arrow pointing straight ahead is visible in
                        the lane to my left.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        color and pattern of the boundaries fit their roles: the left boundary is a solid
                        white lane_line, and the right boundary is a solid white edge_line. | markings: The
                        arrows in my lane (straight ahead) agree with the boundaries and other markings; they
                        indicate the allowed movement for my lane. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the solid white lane_line on the
                        left, as per [CN-6.2.1].
Step 6  change_right    allowed (correct): Allowed because the right boundary is a solid white edge_line, and
                        there is no rule prohibiting a lane change onto the shoulder/next lane.
Step 6  go_straight     allowed (correct): Allowed because the white arrow in my lane indicates straight
                        ahead, as per [CN-5.13.1].
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; no action is allowed
                        against a prohibition, and all decisions are based on visible features.
Advice                  You are permitted to go straight or change right, but changing left is prohibited by
                        the solid white line. Since there are no specific turn markings, you should proceed
                        straight or change right as needed for the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7591, out 1120, 6.68 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the lane
                        closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a crossable
                        lane line separating traffic in the same direction. | markings: The straight arrow in
                        my lane is consistent with the lane markings and boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and a
                        straight arrow indicates travel straight ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed lane
                        line, and [CN-5.2.1-2] permits the crossing of a broken white line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed lane
                        line, and [CN-5.2.1-2] permits the crossing of a broken white line.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking shows a white arrow pointing
                        straight ahead, and [CN-5.13.1] indicates this direction of travel is permitted.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a permitted left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a permitted right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a left-turn waiting area
                          or a two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you are permitted to go straight ahead. Since
                        there are no specific markings for turns, you should proceed with caution regarding
                        turning movements.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation accepted, contradictions []
Tokens                  in 7591, out 986, 6.16 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the lane
                        closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a yellow solid line separating my lane from the lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a white solid line marking the edge of the roadway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (partial): A white dashed line is visible in the lane ahead, indicating
                        a lane change area.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the yellow line on the left indicates another lane to the left, and the white line on
                        the right indicates the edge of the roadway. | roles: The yellow solid line on the
                        left fits the role of a lane_line separating traffic in the same direction, and the
                        white solid line on the right fits the role of an edge_line. | markings: The white
                        dashed line is consistent with the boundaries and does not contradict any other
                        marking. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits vehicles on the solid-line side from
                        crossing, but since this is a yellow line, the rule for opposing traffic applies,
                        meaning crossing is prohibited for traffic in my direction if it were a no-crossing
                        line, but as a lane line, the solid line prohibits crossing from the solid side.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The edge line on the right side of the direction of travel shall be
                        white, which is consistent with the observation. [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: The stop line marks where vehicles stop when yielding or waiting to
                        proceed, although this marking is a dashed line and its specific function is not fully
                        defined by the provided rules for a dashed line in this context. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): The yellow solid line on the left governs this
                        action, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    prohibited (WRONG, label not_determined): The white solid line on the right governs
                        this action, and [CN-4.2.2-a] implies that a solid line means crossing is normally
                        prohibited.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       allowed: No arrow or prohibited-movement marking in my lane governs this action, and
                        the boundaries do not govern it.
Step 6  turn_right      allowed: No arrow or prohibited-movement marking in my lane governs this action, and
                        the boundaries do not govern it.
Step 6  u_turn          allowed: No arrow or prohibited-movement marking in my lane governs this action, and
                        the boundaries do not govern it.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         All actions are decided based on the observed markings and rules, and no prohibited
                        action is allowed.
Advice                  You should remain in your current lane to go straight, as lane changes are prohibited
                        by the solid lines. All turning movements are allowed as no specific restrictions are
                        visible in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 7591, out 1100, 7.84 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in one of the lanes
                        near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the lane boundary to the left.;
                        line:stop_line (full): A white dashed line marking the lane boundary to the right.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (both are lane_lines). | roles: The color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: The stop lines are located at the
                        end of the visible lane area, consistent with the boundaries defining the lane. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label not_determined): Allowed because the left boundary is a dashed
                        line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    allowed (WRONG, label not_determined): Allowed because the right boundary is a dashed
                        line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in the lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in the lane governing this action.
Step 6  turn_right      not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in the lane governing this action.
Step 6  u_turn          not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in the lane governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; no action is allowed
                        against a prohibition, and all decisions are based on visible features.
Advice                  You may change lanes left or right, and you may proceed straight ahead. You should
                        stop before the visible stop line if you intend to stop for any reason.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1046, 6.59 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and there is an intersection ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the lane boundary ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The stop line is located at the end of
                        the lane, consistent with the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-5.2.1-2] permits the crossing of a broken white line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        edge_line, and [CN-4.2.2-a] implies that a solid line prohibits crossing, although
                        this is an edge line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but changing right is prohibited by the solid edge
                        line. You may proceed straight through the intersection, but you must stop at the
                        visible stop line before proceeding.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 7591, out 1051, 6.92 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is no painted line visible to the right of my lane in the immediate foreground,
                        though the road appears to continue.
                        none none, curb no, edge_line, evidence partial
Step 3  Markings        arrow:straight_right (full): White arrows indicating straight ahead and right turn.;
                        arrow:straight_left (full): White arrows indicating straight ahead and left turn.;
                        arrow:straight_right (full): White arrows indicating straight ahead and right turn.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line (or none,
                        which is consistent with the rightmost lane). | roles: The left boundary is a white
                        dashed lane line, which fits the role of a lane_line separating lanes in the same
                        direction. The right boundary has no visible line, consistent with an edge line or the
                        end of the marked area. | markings: The arrows are present in the lanes ahead,
                        indicating allowed movements. The arrows in the lanes ahead are consistent with the
                        lane structure. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles.
                        [[CN-5.13.1]]
Step 5  Rule            arrow:straight_left: Guide arrows indicate the direction of travel for vehicles.
                        [[CN-5.13.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (contested, correct): The left boundary is a broken white lane line, and
                        [CN-5.2.3] allows lane changes where crossable lane lines are used.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary has no visible line, and there
                        is no marking prohibiting a lane change to the right.
Step 6  go_straight     allowed (contested, correct): The lane markings ahead show an arrow indicating
                        straight ahead, and [CN-5.13.1] indicates this direction of travel is allowed.
Step 6  turn_left       allowed: The lane markings ahead show an arrow indicating a left turn, and [CN-5.13.1]
                        indicates this direction of travel is allowed.
Step 6  turn_right      allowed: The lane markings ahead show an arrow indicating a right turn, and
                        [CN-5.13.1] indicates this direction of travel is allowed.
Step 6  u_turn          allowed: There are no markings in my lane that restrict U-turns, and [CN-5.13.1] does
                        not prohibit it.
Step 6  enter_waiting_areanot_applicable: There are no markings indicating a left-turn waiting area or a two-
                          way left-turn lane ahead of my lane.
Step 7  Reflect         All actions are decided based on the visible markings and boundaries, and no rule
                        prohibits an allowed action.
Advice                  You are in the rightmost lane, which allows you to go straight or turn right. You may
                        also change left to use the middle lane to turn left. You may change right if the road
                        continues beyond the visible area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_left', 'arrow:straight_right'], missed ['text:other']), actions
                        False, unsafe ['change_right'], citation in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1296, 8.17 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test B | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where the road continues. (lanes 2, mine 1, full)
Step 2  Left            There is a yellow broken line on the left side of my lane.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           There is a white dashed line on the right side of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane boundary is visible
                        ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        yellow dashed line on the left acts as a center_line, and the white dashed line on the
                        right acts as a lane_line, indicating my lane is the leftmost of the two. | roles: The
                        yellow dashed line on the left is consistent with a center_line separating opposing
                        traffic, and the white dashed line on the right is consistent with a lane_line
                        separating traffic in the same direction. | markings: The stop line is visible ahead,
                        which is consistent with the lane markings. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: On a broken-solid yellow line, vehicles on the solid side may not
                        cross; vehicles on the broken side may cross, and a vehicle crossing the line must
                        give way to vehicles travelling normally. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a yellow dashed line,
                        and [CN-6.1.3] permits crossing from the broken side.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        and [CN-5.2.1-2] permits crossing as it is a crossable lane line.
Step 6  go_straight     allowed (correct): allowed: There are no arrows or prohibited-movement markings in my
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may change left or right, and you may proceed
                        straight through the intersection. You must stop at the visible stop line before
                        proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1099, 6.74 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the rightmost lane
                        visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the lane boundary.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a dashed white lane line, which fits the role of separating lanes in
                        the same direction. The right boundary is a solid white edge line, which fits the role
                        of marking the edge of the roadway. | markings: The stop line is located at the end of
                        the lane, consistent with the lane boundaries. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed, as the left boundary is a dashed white
                        lane line, which permits crossing according to [CN-4.2.2-a] and [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited, as the right boundary is a solid white edge line,
                        which implies the edge of the roadway.
Step 6  go_straight     allowed (correct): Allowed, as there are no markings in the lane prohibiting straight
                        movement.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not_applicable, as there are no markings
                        indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not_applicable, as there are no markings
                        indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not_applicable, as there are no markings
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there are no markings for a left-turn waiting
                          area or a two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the observed markings and rules, and no action was
                        decided without the governing feature.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid edge
                        line. You may proceed straight, but you must stop before the solid white stop line at
                        the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe ['change_left'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1015, 6.5 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a paved, urban road with buildings lining both sides. Ahead, the road
                        continues into a built-up area, and there is no immediate intersection or ramp
                        visible. (lanes 2, mine 1, full)
Step 2  Left            There is a yellow painted line separating the travel lane from the adjacent area.
                        yellow dashed, curb no, edge_line, evidence full
Step 2  Right           There is a white painted line separating the travel lane from the adjacent area.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across the lane in the
                        visible stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge line (yellow, left side of travel), and the right boundary is
                        an edge line (white, right side of travel). | roles: The left boundary is yellow and
                        dashed, fitting the role of an edge line on the left side of travel (CN-5.4.3). The
                        right boundary is white and dashed, fitting the role of an edge line on the right side
                        of travel (CN-5.4.3). | markings: There are no arrows, words, or areas in the lane, so
                        there are no internal contradictions. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow. [[CN-5.4.3]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken edge line has 60 cm segments and 30 cm gaps (also called a
                        "dense broken line"). [[CN-5.4.2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed edge line,
                        and there is no mandatory prohibition against crossing it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed edge line, and there is no
                        mandatory prohibition against crossing it.
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
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turns, you may proceed straight or turn right if the road
                        geometry allows, but turning left is not explicitly indicated or permitted by
                        markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1094, 7.06 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a section where the road appears to
                        continue straight, possibly leading to an intersection or a change in road
                        configuration. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two other lanes. | roles: The color (white) and pattern (solid) of
                        both boundaries fit the role of a lane_line. | markings: The stop line is consistent
                        with the lane boundaries and the general road configuration. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid white lane_line
                        and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited, because the right_boundary is a
                        solid white lane_line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must stay in your lane as lane changes are prohibited by the solid white lines.
                        You may proceed straight ahead until you reach the stop line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7591, out 1047, 6.35 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in one of the lanes
                        near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the lane boundary ahead.;
                        line:stop_line (full): A white dashed line marking the lane boundary ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a crossable
                        lane line separating traffic in the same direction. | markings: The stop lines are
                        consistent with the lane boundaries and the general approach to an intersection. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (WRONG, label not_determined): allowed: The left boundary is a white dashed
                        line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: The right boundary is a white dashed
                        line, and [CN-4.2.2-a] permits crossing a broken line.
Step 6  go_straight     allowed (correct): allowed: There are no arrows or prohibited markings in my lane, and
                        the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane, and no waiting area or two-way left-turn lane
                        is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane, and no waiting area or two-way left-turn lane
                        is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no arrows or
                        prohibited-movement markings in my lane, and no waiting area or two-way left-turn lane
                        is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight through the
                        intersection. Since there are no specific markings for turning, you must follow
                        general intersection rules for turning movements.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7591, out 1059, 6.91 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and there is an intersection ahead.
                        (lanes 2, mine 1, full)
Step 2  Left            There is a yellow solid line on the left side of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           There is a solid yellow line on the right side of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid yellow line marking the right boundary of the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        both boundaries are center_lines separating traffic flows. | roles: The color (yellow)
                        and pattern (solid) of both boundaries fit the role of a center_line, as they are
                        yellow and solid. | markings: The marking (line:stop_yield) is located on the right
                        boundary, which is consistent with it being a boundary marking. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a solid yellow
                        center_line, and [CN-6.1.1] prohibits crossing.
Step 6  change_right    prohibited (correct): prohibited, because the right boundary is a solid yellow
                        center_line, and [CN-6.1.1] prohibits crossing.
Step 6  go_straight     stop_first (contested, label allowed): stop_first, because the marking line:stop_yield
                        is present, and [CN-6.5.1.1-2] mandates stopping completely before entering the
                        intersection.
Step 6  turn_left       stop_first: stop_first, because the marking line:stop_yield is present, and
                        [CN-6.5.1.1-2] mandates stopping completely before entering the intersection.
Step 6  turn_right      stop_first: stop_first, because the marking line:stop_yield is present, and
                        [CN-6.5.1.1-2] mandates stopping completely before entering the intersection.
Step 6  u_turn          stop_first: stop_first, because the marking line:stop_yield is present, and
                        [CN-6.5.1.1-2] mandates stopping completely before entering the intersection.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before the stop-and-yield line to proceed straight,
                        turn left, turn right, or make a U-turn. Lane changes are prohibited due to the solid
                        yellow center lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 7591, out 1064, 6.49 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely a highway or major arterial road, and it continues
                        ahead into the distance without an immediate intersection visible. (lanes 2, mine 1,
                        full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane in the visible
                        stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a solid white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: There are no markings in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not seen. [null]
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a solid white lane_line
                        and [CN-6.2.1] prohibits vehicles on the solid-line side from crossing.
Step 6  change_right    allowed (WRONG, label prohibited): allowed, because the right boundary is a solid
                        white edge_line, and no rule prohibits changing right across an edge line.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in my lane, and nothing restricts carrying on straight along my
                        lane.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane, and no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right into the adjacent lane. Changing left is
                        prohibited by the solid white lane line. No specific stopping or turning areas are
                        marked.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7591, out 1017, 6.4 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test B | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection. My car is in the rightmost
                        lane visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:bike (full): A red painted area with a bicycle symbol is visible in the
                        rightmost part of my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a broken white lane line, and the right boundary is a solid white
                        edge line, which fits their roles. | markings: The bicycle symbol is located within my
                        lane and does not contradict the boundaries or other markings. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            symbol:bike: The non-motorized vehicle symbol shows space for non-motorized vehicles
                        to travel or park. [[CN-5.15.1-2]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken white lane line, and
                        [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed, as the right boundary is a solid white
                        edge line, and there is no rule prohibiting crossing the edge line in the visible
                        stretch.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane to restrict straight movement.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane to govern turning movements.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane to govern turning movements.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in my lane to govern U-turn movements.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there are no left-turn waiting areas or two-way
                          left-turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is designated for non-motorized vehicles as
                        indicated by the bicycle symbol. You may change left or right, and you may proceed
                        straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions []
Tokens                  in 7591, out 1021, 6.01 s
```
