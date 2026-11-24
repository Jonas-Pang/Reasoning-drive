# Reasoning of lane run 20261117_015345_laneA_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a merging
                        area. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles
                        (left boundary is a lane_line, right boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The arrow pointing straight ahead is consistent with the lane markings and boundaries.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white lane
                        line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking shows an arrow pointing
                        straight ahead, and nothing restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane to govern this action, and no left-turn waiting area is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane to govern this action, and no right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are permitted to go straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 945, 14.98 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and the road continues ahead without an immediate
                        intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (solid) of both boundaries fit the role of a lane_line. |
                        markings: There are no markings in my lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited due to the solid white lane line on the
                        left boundary, which prohibits crossing it to change lanes.
Step 6  change_right    prohibited (correct): prohibited due to the solid white lane line on the right
                        boundary, which prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        restricting movement straight ahead.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane indicating a
                        turn left.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane indicating a
                        turn right.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane indicating a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 2930, out 805, 17.69 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a guardrail on the right side. Ahead, the road
                        continues straight. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right, and beyond
                        that is a metal guardrail.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): A green overhead sign indicating '行车道' (Carriageway) with a speed
                        limit of 80.; text:other (full): A green overhead sign indicating '行车道' (Carriageway)
                        with a speed limit of 80.; text:other (full): A green overhead sign indicating '应急车道'
                        (Emergency Lane) with a speed limit of 40.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        left boundary is a dashed white lane line, and the right boundary is a solid white
                        lane line, which fits the roles of lane_line. | markings: The overhead signs are
                        present and do not contradict the lane markings or boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line permits lane changes across it.
Step 5  Rule            right_boundary: A solid white lane line prohibits lane changes across it.
Step 5  Rule            text:other: The overhead signs provide information but do not restrict the immediate
                        movement of my car.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed white lane line,
                        which permits lane changes across it.
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited because the right boundary is a
                        solid white lane line, which prohibits lane changes across it.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in my lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a turn left.
Step 6  turn_right      not_applicable: Not applicable because there are no markings indicating a turn right.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a waiting
                          area.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid white
                        line. You may proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 1025, 158.44 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be a continuous stretch of road
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid yellow line marking the right boundary.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a white solid lane line, and the right boundary is a yellow solid lane
                        line, which fits the roles of lane_line. | markings: The solid yellow line on the
                        right boundary is interpreted as a line:stop_yield marking, which is consistent with
                        its appearance as a solid line near the end of the visible road segment. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes across it are
                        generally prohibited.
Step 5  Rule            right_boundary: A solid yellow lane line indicates that lane changes across it are
                        prohibited.
Step 5  Rule            line:stop_yield: The presence of a stop-and-yield line requires the vehicle to come to
                        a full stop before proceeding.
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white lane
                        line, and the rule states that lane changes across it are generally prohibited.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid yellow lane
                        line, and the rule states that lane changes across it are prohibited.
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
Step 7  Reflect         All actions are decided based on visible features, and no action is allowed when
                        prohibited by a rule.
Advice                  You should proceed straight in your current lane. Be aware that the solid yellow line
                        ahead requires you to stop and yield before proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation None,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 2930, out 994, 17.0 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test A | gemma4:e4b
------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead.; arrow:straight (full):
                        A white arrow pointing straight ahead, located in the lane to the right.;
                        arrow:straight (full): A white arrow pointing straight ahead, located in the lane to
                        the left.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (solid) of both boundaries fit the role of a lane_line. |
                        markings: The arrows in my lane (arrow:straight) agree with the boundaries, as they
                        indicate movement within the lane defined by the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     prohibited (contested, label allowed): prohibited: The left boundary is a solid white
                        lane line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (contested, label allowed): prohibited: The right boundary is a solid white
                        lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: The lane marking shows an arrow pointing
                        straight ahead, and no boundary prohibits it.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a permitted left
                        turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a permitted right
                        turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a left-turn waiting area
                          or a two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['text:bus']), actions None, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 993, 155.84 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with a bridge structure ahead, and the road continues
                        forward. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two lanes of my direction. | roles: The white solid lines on both
                        sides fit the role of lane_line. | markings: The absence of markings in my lane is
                        consistent with the boundaries defining the lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited due to the solid white lane line on the left boundary
                        and the rule that prohibits crossing solid lane lines.
Step 6  change_right    prohibited (correct): prohibited due to the solid white lane line on the right
                        boundary and the rule that prohibits crossing solid lane lines.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane governing this
                        action.
Step 6  turn_right      prohibited: prohibited due to the no_turn:right marking in my lane and the rule that
                        prohibits turning right.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane governing this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on visible features and their corresponding rules, and
                        no action is allowed despite a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight, but turning right is prohibited by the
                        marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 951, 22.33 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road stretching into the distance, and it appears to continue
                        without an immediate intersection or ramp visible ahead. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across the lane from bottom
                        to end.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes. | roles: The white solid lines fit the role of
                        lane_line. | markings: There are no arrows, words, or areas in my lane to contradict
                        the boundaries. | unseen: No attributes were reported that were not actually seen. |
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
Step 6  turn_right      prohibited: prohibited: The no_turn:right marking prohibits turning right from my
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
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 2930, out 948, 15.98 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a road sign indicating a turn or
                        continuation, but no immediate intersection is visible. (lanes 3, mine 2, full)
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
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        and the rule allows lane changes across it.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and the rule
                        allows lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing this action, and no waiting area is visible.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' in my lane prohibits turning
                        right.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing this action, and no waiting area is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        action is allowed.
Advice                  You may change lanes left or right, or proceed straight ahead. Turning right is
                        prohibited by the lane marking in your lane. Since you are in the middle lane, you
                        have flexibility for lane changes.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 2930, out 940, 14.19 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and the road continues ahead without an immediate
                        intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles (a
                        lane line on the left and a lane line on the right indicate my lane is in the middle
                        of three lanes). | roles: The color and pattern of both boundaries (white solid lines)
                        fit the role of a lane_line. | markings: There are no markings in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 6  change_left     prohibited (correct): prohibited due to the solid white lane line on the left
                        boundary, as per the rule for solid lane lines.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the solid white lane line on the
                        right boundary, as per the rule for solid lane lines.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane
                        restricting straight movement.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane indicating a
                        turn left.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane indicating a
                        turn right.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane indicating a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You should remain in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 828, 15.98 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead
                        without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles (a
                        lane line on both sides indicates an intermediate lane). | roles: The solid white
                        lines fit the role of lane_line. | markings: There are no markings in the lane to
                        check against the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 6  change_left     prohibited: prohibited due to the solid white lane line on the left boundary, which
                        prohibits crossing it to change lanes.
Step 6  change_right    prohibited: prohibited due to the solid white lane line on the right boundary, which
                        prohibits crossing it to change lanes.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane that
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no marked waiting areas or two-way
                          left-turn lanes visible.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight, as lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 793, 146.11 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead into
                        the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The left
                        boundary is a white solid lane_line, and the right boundary is a yellow solid
                        lane_line, which fits the role of lane_line. | markings: The absence of markings in my
                        lane is consistent with the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes across it are
                        prohibited.
Step 5  Rule            right_boundary: A solid yellow lane line indicates that lane changes across it are
                        prohibited.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid white lane_line
                        and the rule prohibits lane changes across it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right_boundary is a solid
                        yellow lane_line and the rule prohibits lane changes across it.
Step 6  go_straight     allowed (contested, label not_determined): allowed, because there are no markings in
                        my lane that prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable, because there are no markings in my lane that allow or
                        prohibit turning left.
Step 6  turn_right      prohibited: prohibited, because the no_turn:right marking in my lane prohibits turning
                        right.
Step 6  u_turn          not_applicable: not_applicable, because there are no markings in my lane that allow or
                        prohibit making a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by solid lines. You
                        are allowed to go straight, but turning right is prohibited by a marking in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed ['symbol:other']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 946, 15.65 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes going in the same
                        direction, and the road continues ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the visible lane area
                        ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The stop line is consistent with the lane boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must come to a complete stop
                        before proceeding, if required by a sign or signal.
Step 6  change_left     prohibited (correct): prohibited due to the solid white lane line on the left (Rule: A
                        solid white lane line prohibits crossing it to change lanes).
Step 6  change_right    prohibited (correct): prohibited due to the solid white lane line on the right (Rule:
                        A solid white lane line prohibits crossing it to change lanes).
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings prohibiting
                        straight movement in the lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or prohibited-movement
                        markings in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane as lane changes are prohibited by the solid white
                        lines. You may proceed straight ahead until the stop line, where you must stop if
                        required by traffic control.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 946, 16.14 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road passing under an overpass. My car is in one of the lanes
                        approaching the underpass. (lanes 3, mine 2, full)
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
Step 6  change_left     prohibited (correct): prohibited: The left_boundary is a solid white lane line, and
                        the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing this action.
Step 6  turn_right      prohibited: prohibited: The marking no_turn:right prohibits turning right from my
                        lane.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on visible markings or boundaries, and no action is
                        allowed against a prohibition.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You are allowed to proceed straight through the underpass, but turning right is
                        prohibited by the marking in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 928, 16.27 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test A | gemma4:e4b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with multiple lanes going in the same direction. Ahead,
                        the lanes continue into the distance. (lanes 4, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Text '小客车专用' and speed limit '80' are visible above the lane.;
                        text:other (full): Text '行车道' and speed limit '100' are visible above the lane.;
                        text:other (full): Text '行车道' and speed limit '100' are visible above the lane.;
                        text:other (full): Text '应急车道' and speed limit '60' are visible above the lane.
Step 4  Cross-check     position: The lane count (4) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The text markings are consistent with the lane structure, indicating lane designations
                        and speed limits. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            text:other: Lane designation and speed limit signs do not restrict movement actions.
Step 6  change_left     prohibited (correct): prohibited: The left_boundary is a solid white lane line, and
                        the rule states that a solid white lane line prohibits crossing it to change lanes.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule states that a solid white lane line prohibits crossing it to
                        change lanes.
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
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:other'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 1095, 22.91 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where traffic appears to
                        be moving through or approaching it. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The arrow pointing straight ahead in my lane agrees with the boundaries, as
                        it does not indicate a lane change or turn. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
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
                        prohibited-movement marking in my lane indicating a turn left.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a turn right.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left_turn_waiting area or
                          two_way_left_turn_lane visible.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight through the intersection.
                        Lane changes are prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk', 'line:stop_line']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 928, 17.85 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where traffic appears to
                        be moving across the frame. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, areas, or lines are visible
                        within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The lack of markings in the lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows for lane changes across it.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a white dashed line,
                        which allows lane changes.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a white dashed line,
                        which allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       allowed: allowed: No arrow or prohibited-movement marking in my lane prohibits turning
                        left.
Step 6  turn_right      prohibited: prohibited: The marking 'no_turn:right' prohibits turning right from my
                        lane.
Step 6  u_turn          allowed: allowed: No arrow or prohibited-movement marking in my lane prohibits
                        U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible ahead of my lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You may change lanes left or right, go straight, turn left, or make a U-turn, but
                        turning right is prohibited. Use the lane appropriate for your intended movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe
                        ['change_left', 'change_right'], citation None, contradictions []
Tokens                  in 2930, out 907, 18.29 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles (a
                        lane line on both sides indicates an intermediate lane). | roles: The white dashed
                        lines fit the role of lane_line. | markings: There are no markings in the lane to
                        check against boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows lane changes in the direction of
                        traffic.
Step 5  Rule            right_boundary: A broken white lane line allows lane changes in the direction of
                        traffic.
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and the rule
                        allows lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and the rule
                        allows lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings indicating a turn left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings indicating a turn right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You are allowed to change lanes left
                        or right, and you can proceed straight ahead. No specific lane usage is required for
                        turning movements.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 790, 21.08 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a continuation of the road, not an
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): White dashed lane markings are visible ahead in my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane_line. |
                        markings: The dashed line ahead is consistent with the lane markings observed. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left_boundary is a solid white lane
                        line, and the rule prohibits crossing it to change lanes.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane line, and the rule prohibits crossing it to change lanes.
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
Advice                  You should remain in your current lane to proceed straight. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 919, 14.2 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes going in the same
                        direction ahead. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): White dashed lines marking the lane boundaries.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop line marking is consistent with the lane boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding,
                        although no specific stop requirement is indicated by other markings.
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a white dashed
                        line, and the rule allows lane changes across it.
Step 6  change_right    allowed (contested, correct): allowed: The right boundary is a white dashed line, and
                        the rule allows lane changes across it.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
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
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 902, 23.87 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test A | gemma4:e4b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a junction or intersection where traffic
                        appears to be merging or continuing. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Two white arrows pointing straight ahead are painted on the
                        road surface.; line:stop_line (partial): A white dashed line is visible further ahead,
                        indicating a lane division or merge area.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The solid white lines on both sides fit the role
                        of lane_line. | markings: The straight arrows agree with the lane markings, and the
                        stop line is consistent with the lane markings. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 5  Rule            line:stop_line: The stop line indicates the designated stopping point for traffic in
                        this lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white lane
                        line, and the rule prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        lane line, and the rule prohibits crossing it.
Step 6  go_straight     allowed (correct): allowed: The lane marking shows an arrow pointing straight ahead,
                        and nothing restricts carrying on straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or
                          two-way left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no action is
                        allowed against a prohibition.
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 997, 21.53 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, there is a
                        junction or intersection visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, text, symbols, or specific markings are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The solid white lines on both sides fit the role
                        of lane_line. | markings: The absence of specific markings in my lane is consistent
                        with the boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing it to change lanes.
Step 5  Rule            no_turn:right: This marking prohibits turning right from my lane.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white lane
                        line, and the rule prohibits crossing it.
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
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 936, 16.09 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is an intersection where the road appears
                        to split or continue. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left edge of the lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line marking the right edge of the lane.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is not the leftmost or rightmost in a way that contradicts the count. | roles:
                        The left boundary is a white solid lane line, and the right boundary is a yellow solid
                        lane line, which fits the role of lane_line. | markings: There are no markings in my
                        lane to check against the boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: A solid white lane line indicates that lane changes across it are
                        prohibited.
Step 5  Rule            right_boundary: A solid yellow lane line indicates that lane changes across it are
                        prohibited.
Step 6  change_left     prohibited (correct): prohibited, because the left_boundary is a solid white lane line
                        and the rule prohibits lane changes across it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right_boundary is a solid
                        yellow lane line and the rule prohibits lane changes across it.
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
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed when prohibited.
Advice                  You must stay in your current lane as lane changes are prohibited by the solid lines
                        on both sides. You are allowed to proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['leftmost lane,
                        but a lane line on the left']
Tokens                  in 2930, out 863, 14.79 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road, and ahead there is a junction or area
                        where lanes are marked for different movements. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): White dashed lines indicating lane separation and movement
                        options ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (both are lane_lines). | roles: The white dashed lines fit the role of lane_line. |
                        markings: The stop line is consistent with the lane markings. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A broken white line allows lane changes across it.
Step 5  Rule            right_boundary: A broken white line allows lane changes across it.
Step 5  Rule            line:stop_line: The stop line indicates where vehicles must stop before proceeding
                        through the intersection or area ahead.
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed white line, which
                        permits lane changes.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed white line, which
                        permits lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in the lane
                        prohibiting straight movement.
Step 6  turn_left       not_applicable: Not applicable because there are no markings indicating a permitted
                        left turn.
Step 6  turn_right      not_applicable: Not applicable because there are no markings indicating a permitted
                        right turn.
Step 6  u_turn          not_applicable: Not applicable because there are no markings indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there are no markings indicating a designated
                          waiting area.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        actions are allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. You must stop
                        at the visible stop line before proceeding into the area ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['text:other']), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 2930, out 867, 16.09 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a long, straight road ahead, suggesting no immediate
                        intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, words, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The absence of markings is consistent with the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A dashed white lane line allows for lane changes across it.
Step 5  Rule            right_boundary: A dashed white lane line allows for lane changes across it.
Step 5  Rule            no_turn:right: This marking does not restrict any movement as it is not a prohibited
                        movement marking.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane line, which
                        allows lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane line, which
                        allows lane changes.
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
Step 7  Reflect         All actions are decided based on visible features and rules, and no prohibited action
                        is allowed.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turns, you should proceed cautiously if you intend to
                        turn.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 2930, out 951, 21.13 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test A | gemma4:e4b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road stretching into the distance, and it appears to continue
                        forward without an immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A overhead sign with three upward arrows is visible above my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left boundary is a lane line, right boundary is a lane line). | roles: The white
                        dashed lines fit the role of lane_line. | markings: The overhead arrow indicates
                        straight movement, which is consistent with the lane markings. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white lane line permits lane changes across it.
Step 5  Rule            right_boundary: A dashed white lane line permits lane changes across it.
Step 5  Rule            arrow:straight: The arrow indicates that proceeding straight ahead is permitted in
                        this lane.
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane line, which
                        permits lane changes.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white lane line, which
                        permits lane changes.
Step 6  go_straight     allowed (correct): allowed: The overhead arrow indicates straight movement is
                        permitted.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane.
Step 7  Reflect         All actions are decided based on visible markings and boundaries, and no prohibited
                        actions are allowed.
Advice                  You are in the middle lane, and you are permitted to go straight, change left, or
                        change right. No specific stopping or turning maneuvers are indicated by the lane
                        markings.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2930, out 889, 15.57 s
```
