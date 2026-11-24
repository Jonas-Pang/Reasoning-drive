# Reasoning of lane run 20261117_044746_laneC_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test C | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be a multi-lane roadway, possibly a highway or major arterial road,
                        with traffic moving away from the camera. Ahead, the road continues, and there is a
                        slight curve or transition visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the end of the visible lane
                        markings ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two other lanes. | roles: The color (white) and pattern (solid) of
                        both boundaries fit the role of a lane_line, indicating separation between lanes
                        traveling in the same direction. | markings: The stop line marking is consistent with
                        the lane boundaries, indicating the end of the current travel area. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control device. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white lane_line and [US-3B.06-05-06] states that crossing the lane line markings is
                        discouraged.
Step 6  change_right    prohibited (correct): prohibited, because the right boundary is a solid white
                        lane_line and [US-3B.06-05-06] states that crossing the lane line markings is
                        discouraged.
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
Advice                  You should remain in your current lane to proceed straight, as lane changes are
                        discouraged by the solid white lines. You must stop at the visible stop line ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1111, 18.26 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test C | gemma4:e4b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues straight, and there is a barrier/fence on the right side. (lanes 2, mine 1,
                        full)
Step 2  Left            There is no visible painted line or curb on the left side of my lane in the visible
                        stretch.
                        none none, curb no, unknown, evidence insufficient
Step 2  Right           The right boundary is defined by a painted white line separating my lane from an
                        adjacent lane, and beyond that, there is a concrete barrier/curb.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the edge of the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        the right boundary is a lane_line and the left boundary is unknown/no line. | roles:
                        The right boundary is white and solid, fitting the role of a lane_line separating
                        traffic in the same direction, although the specific rule for this configuration is
                        not fully determined without more context on the road type. | markings: The solid
                        white line marking is consistent with the right boundary's solid white line, and it is
                        interpreted as a stop line, which is a specific type of line marking. | unseen: The
                        specific nature of the left boundary (e.g., shoulder, median) is unseen. | result:
                        consistent
Step 5  Rule            left_boundary: No rule passage applies to the unseen left boundary. [null]
Step 5  Rule            right_boundary: When used, white markings for longitudinal lines shall delineate the
                        separation of traffic flows in the same direction. [[US-3B.06-01]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     not_applicable (WRONG, label allowed): not_applicable
Step 6  change_right    allowed (WRONG, label prohibited): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         The actions are consistent with the observations and rules, as the right boundary
                        allows lane changes, and the stop line governs the stopping requirement.
Advice                  You may change right into the adjacent lane, and you may proceed straight. Be aware of
                        the solid white line marking ahead, which indicates a required stopping point.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        unlisted, contradictions ['change_right allowed across a curb']
Tokens                  in 8624, out 952, 18.07 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, the road
                        continues into the distance with no immediate intersection or ramp visible. (lanes 3,
                        mine 2, full)
Step 2  Left            The left boundary is marked by a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           The right boundary is marked by a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid white line marking the edge of the lane.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is a lane line (indicating a lane to the left), and the right boundary
                        is a lane line (indicating a lane to the right). | roles: The color (white) and
                        pattern (solid) of both boundaries fit the role of a lane line separating lanes
                        traveling in the same direction. | markings: The lane marking observed (a solid white
                        line) is consistent with the boundaries, although its specific function (stop line) is
                        not fully determined by the boundaries alone. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line marking is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line marking is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control device. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white lane line and [US-3B.06-05-06] states that crossing the lane line marking is
                        discouraged.
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited, because the right boundary is a
                        solid white lane line and [US-3B.06-05-06] states that crossing the lane line marking
                        is discouraged.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited-
                        movement markings in the lane to restrict movement, and the boundaries do not govern
                        going straight.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight, as lane changes are
                        discouraged by the solid white lines. No specific stopping or turning maneuvers are
                        governed by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1101, 21.76 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into a built-up area, and there is a barrier separating the lanes from the
                        right side. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the adjacent lane on the right,
                        and beyond that, there is a metal barrier.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid yellow line marking the right boundary.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a center_line. | roles: The
                        left boundary is white dashed, consistent with a lane_line [US-3B.06-05-06]. The right
                        boundary is yellow solid, consistent with a center_line [US-3B.01-01] and
                        [US-3B.01-04]. | markings: The solid yellow line on the right boundary is interpreted
                        as a yield line marking based on the visual evidence, which is a potential
                        contradiction as yield lines are typically white triangles [US-3B.19-10]. However,
                        given the context of the right boundary being a center line, I will proceed with the
                        boundary role and note the marking as a potential misinterpretation or local
                        variation, but the primary governing feature for the right side is the yellow solid
                        line acting as a center line. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is broken white, crossing the lane line markings with
                        care is not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The center line markings on two-lane, two-way roadways shall be one of
                        the specified types, and the solid yellow line indicates a no-passing zone for traffic
                        adjacent to the solid line. [[US-3B.01-04]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles to indicate the point at which the yield is
                        intended or required to be made. [[US-3B.19-10]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a white dashed
                        line, meaning crossing the lane line markings with care is not discouraged or
                        prohibited [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): Prohibited, as the right boundary is a solid yellow
                        line, which functions as a center line indicating a no-passing zone for traffic
                        adjacent to the solid line [US-3B.01-04].
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane, and nothing restricts carrying on straight along my lane [no
                        marking governs this action].
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on the observed markings and rules, and no action is
                        allowed when a rule prohibits it, nor is any action decided without a governing
                        feature.
Advice                  You may change lanes to the left, but changing right is prohibited by the solid yellow
                        center line. You may proceed straight through the intersection, but be aware of the
                        yield line marking on the right side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 8624, out 1300, 23.63 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there is a clear continuation of the road, not an
                        intersection or ramp end visible in the immediate lane area. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane division.;
                        line:stop_line (partial): A white dashed line marking the lane division.;
                        arrow:straight (full): A white arrow pointing straight ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (white dashed lines indicate separation between lanes of the same direction). | roles:
                        The white dashed lines fit the role of lane_line, indicating permissive crossing
                        between lanes of the same direction. | markings: The white arrow pointing straight
                        ahead is consistent with the lane markings and boundaries, and the stop lines are
                        present at the end of the visible lane area. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings is permitted
                        with care. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings is permitted
                        with care. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control signal. [[US-3B.19-01-02]]
Step 5  Rule            arrow:straight: Lane-use arrow markings indicate the mandatory or permissible
                        movements in certain lanes. [[US-3B.23-01]]
Step 6  change_left     allowed (contested, correct): Allowed because the left boundary is a white dashed
                        line, and [US-3B.06-05-06] permits crossing with care.
Step 6  change_right    allowed (contested, correct): Allowed because the right boundary is a white dashed
                        line, and [US-3B.06-05-06] permits crossing with care.
Step 6  go_straight     allowed (contested, correct): Allowed because the lane has a white arrow pointing
                        straight ahead, and [US-3B.23-01] indicates permissible movements.
Step 6  turn_left       not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking indicating a left turn is allowed or prohibited.
Step 6  turn_right      not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking indicating a right turn is allowed or prohibited.
Step 6  u_turn          not_applicable: Not applicable because there is no arrow or prohibited-movement
                        marking indicating a U-turn is allowed or prohibited.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules, as the permissive nature
                        of the dashed lines and the straight arrow govern the allowed movements.
Advice                  You may change lanes left or right as the dashed lines permit crossing with care. You
                        are permitted to go straight ahead, but you should be aware of the stop line ahead,
                        which indicates where you must stop if a traffic control device requires it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:stop_line'], missed ['text:bus']), actions None, unsafe [],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1203, 24.41 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane divided highway with traffic moving away from the camera. Ahead,
                        there is an overpass structure and the road continues into the distance. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a concrete barrier separating my lane from the adjacent lane on the left.
                        none none, curb yes, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the travel lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A solid white line marking the right edge of the lane.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is a lane line separating it from another lane, and the right boundary
                        is an edge line. | roles: The right boundary is a solid white line, which fits the
                        role of an edge line. The left boundary is a concrete barrier, which functions as a
                        lane line. | markings: The single marking observed is a solid white line, which is
                        consistent with the right boundary's description, but its role as a stop line is not
                        fully confirmed by context. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: When used, white markings for longitudinal lines shall delineate the
                        separation of traffic flows in the same direction. [[US-3A.03-03-04]]
Step 5  Rule            right_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a lane line, and
                        there is no marking prohibiting a lane change.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is an edge line, and
                        there is no marking prohibiting a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning movements.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning movements.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane that govern turning movements.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked areas for waiting for a left
                          turn or a two-way left-turn lane directly to the left.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a multi-lane highway, and you are permitted to change
                        lanes left or right, or proceed straight ahead. No specific stopping or turning
                        maneuvers are governed by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions ['change_left allowed across a curb']
Tokens                  in 8624, out 1061, 18.03 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. The road continues
                        into the distance with trees lining both sides, and there is no immediate intersection
                        or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left edge of the travel lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           There is a broken white line marking the separation between lanes.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the end of the lane.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line separating my
                        lane from another lane. | roles: The left boundary is solid white, consistent with an
                        edge line, and the right boundary is dashed white, consistent with a lane line
                        allowing crossing. | markings: The stop line is visible at the end of the lane, which
                        is consistent with the lane structure. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: Right edge line pavement markings, if used, shall consist of a normal
                        width solid white line to delineate the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: Where crossing the lane line markings with care is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is an edge line, and
                        there is no marking prohibiting a lane change.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a broken white lane
                        line, and [US-3B.06-05-06] permits crossing the lane line markings with care.
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
Advice                  You may change lanes left or right, and you may proceed straight. Since there is a
                        stop line visible ahead, you must stop before it if required by a traffic control
                        device.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1095, 22.8 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into the distance with some traffic signals visible. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to my right, and beyond
                        that, there is a paved shoulder.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): There are no arrows, words, symbols, areas, or lines painted
                        across my lane from the bottom to the end.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles: a
                        lane line on the left and a lane line on the right indicate my lane is in the middle
                        of three lanes. | roles: The solid white lines fit the role of lane_line, indicating
                        separation between lanes traveling in the same direction. | markings: The absence of
                        markings in my lane is consistent with the boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            no_turn:right: No specific rule passage covers the general absence of markings in the
                        lane. [null]
Step 6  change_left     prohibited (correct): The left boundary is a solid white lane_line, and
                        [US-3B.06-05-06] states that crossing the lane line markings is discouraged.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white lane_line, and
                        [US-3B.06-05-06] states that crossing the lane line markings is discouraged.
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
Step 7  Reflect         All actions are decided based on the observed features and the applicable rules, and
                        no action is allowed when prohibited.
Advice                  You should stay in your current lane to proceed straight. Lane changes to the left or
                        right are discouraged by the solid white lane lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8624, out 1070, 18.4 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into the distance without an immediate intersection or ramp visible. (lanes
                        3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the adjacent lane to the right.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, words, symbols, areas, or lines are
                        visible within my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a center line. | roles:
                        The left boundary is a solid white lane line, and the right boundary is a solid yellow
                        center line, which fits their roles. | markings: There are no markings in my lane to
                        check against the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The center line markings on undivided two-way roadways with four or
                        more lanes for moving motor vehicle traffic always available shall be the two-
                        direction no-passing zone markings consisting of normal width double solid yellow
                        lines, although only a single solid yellow line is visible here. [[US-3B.01-06]]
Step 5  Rule            no_turn:right: No specific rule passage covers the absence of a right turn prohibition
                        marking in my lane. [null]
Step 6  change_left     prohibited (correct): The left boundary is a solid white lane line, and
                        [US-3B.06-05-06] states that crossing the lane line markings is discouraged.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid yellow center line,
                        and [US-3B.01-06] implies a restriction on crossing the center line markings.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No marking governs this action, and there is no left-turn waiting area
                        or two-way left-turn lane.
Step 6  turn_right      not_applicable: No marking governs this action, and there is no right-turn arrow or
                        prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: No marking governs this action, and there is no U-turn arrow or
                        prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: No marking governs this action, and there is no left-turn waiting
                          area or two-way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes to the left or right are discouraged or
                        prohibited by the solid lines. You may proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8624, out 1052, 15.91 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a traffic signal
                        and what appears to be an intersection or a continuation of the road with other
                        traffic. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane-use arrows, words, symbols, areas, or lines are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line (indicating a lane to the left), and the right
                        boundary is a lane line (indicating a lane to the right). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of a lane line separating
                        lanes traveling in the same direction. | markings: The lack of visible markings in my
                        lane is consistent with the boundaries defining the lane structure. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line marking is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line marking is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            no_turn:right: No specific rule passage covers the absence of a prohibited movement
                        marking in this context. [null]
Step 6  change_left     prohibited: The left boundary is a solid white lane line, and [US-3B.06-05-06] states
                        that crossing the lane line marking is discouraged.
Step 6  change_right    prohibited: The right boundary is a solid white lane line, and [US-3B.06-05-06] states
                        that crossing the lane line marking is discouraged.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action, and there is no waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: There is no marked waiting area or two-way left-turn lane visible
                          ahead of my lane.
Step 7  Reflect         All actions are decided based on the observed boundaries and markings, and no action
                        is allowed against a prohibition.
Advice                  You are in the middle lane, and while lane changes are discouraged by the solid white
                        lines, you are permitted to proceed straight ahead. Since no specific turn markings
                        are present, you may proceed straight, but be aware of the traffic signal ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 8624, out 1090, 21.98 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the adjacent lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the adjacent lane to the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid yellow line marking the boundary with the left
                        lane.; line:stop_yield (partial): A solid yellow line marking the boundary with the
                        right lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane line (separating from lane 1) and the right boundary is a lane
                        line (separating from lane 3). | roles: The color (yellow) and pattern (solid) of both
                        boundaries fit the role of a lane line separating traffic flows in the same direction,
                        as per US-3B.06-05-06, although the specific rule for yellow lane lines in same-
                        direction traffic is not explicitly detailed in the provided passages, the solid
                        nature suggests restriction. | markings: The markings listed are the boundaries
                        themselves, which are interpreted as stop/yield lines based on the provided list,
                        which is a potential contradiction as boundaries are lines, not the specific
                        stop/yield markings listed. The presence of solid yellow lines suggests a restriction,
                        which aligns with the general function of solid lines. | unseen: No attributes were
                        reported that were not actually seen. | result: corrected
Step 5  Rule            left_boundary: Where crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_yield: Yield lines shall consist of a row of solid white isosceles triangles
                        pointing toward approaching vehicles extending across approach lanes to indicate the
                        point at which the yield is intended or required to be made. [[US-3B.19-10]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid yellow line, and while
                        the specific rule for yellow lane lines in same-direction traffic is not fully
                        defined, the solid nature suggests a restriction.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid yellow
                        line, and while the specific rule for yellow lane lines in same-direction traffic is
                        not fully defined, the solid nature suggests a restriction.
Step 6  go_straight     allowed (contested, label not_determined): allowed: Nothing restricts carrying on
                        straight along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The action decisions are based on the observed boundaries and markings, but the
                        interpretation of the solid yellow lines as 'stop_yield' markings is inconsistent with
                        the visual evidence and the provided rules, leading to an uncertain basis for the
                        'prohibited' actions.
Advice                  You should proceed straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid yellow lane lines. No specific stopping or turning
                        maneuvers are governed by markings in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed ['symbol:other']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 8624, out 1298, 28.15 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or freeway with multiple lanes traveling in the same
                        direction ahead. The road continues into the distance with buildings visible on the
                        right side. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the end of the visible lane
                        markings ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two other lanes. | roles: The color (white) and pattern (solid) of
                        both boundaries fit the role of a lane_line, indicating separation between lanes
                        traveling in the same direction. | markings: The stop line marking is consistent with
                        the lane boundaries; it is a line across the lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control device. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (correct): Prohibited by the left_boundary because it is a solid white
                        lane_line, and crossing lane lines is discouraged ([US-3B.06-05-06]).
Step 6  change_right    prohibited (correct): Prohibited by the right_boundary because it is a solid white
                        lane_line, and crossing lane lines is discouraged ([US-3B.06-05-06]).
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight. Since there is a stop line
                        visible ahead, you must stop before this line if a traffic control device requires it.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1089, 16.87 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road passing under an overpass. There are multiple lanes visible
                        in my direction ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the edge of the lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (left_boundary is a lane_line, right_boundary is a lane_line). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line. | markings:
                        The stop line marking is consistent with the lane boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is discouraged, the lane line
                        markings shall consist of a normal width solid white line. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (correct): prohibited: The left_boundary is a solid white lane_line, and
                        [US-3B.06-05-06] indicates that crossing is discouraged.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right_boundary is a solid white
                        lane_line, and [US-3B.06-05-06] indicates that crossing is discouraged.
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
Advice                  You should remain in your current lane to proceed straight through the underpass. Lane
                        changes are prohibited by the solid white lines on both sides.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1057, 19.44 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with traffic moving away from the camera. Ahead, there
                        are lane markings indicating different types of lanes, including a through lane and an
                        emergency vehicle lane. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): White text marking '小客车专用' (Private Car Only) and speed limit '80';
                        text:other (full): White text marking '行车道 Through Lane' and speed limit '100';
                        text:other (full): White text marking '行车道 Through Lane' and speed limit '80';
                        text:other (full): White text marking '应急车道 Emergency Vehicle Lane' and speed limit
                        '60'
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is between two other lanes. | roles: The white dashed lines fit the role of
                        lane_line, as they delineate traffic flows in the same direction [US-3B.06-05-06]. |
                        markings: The text markings are placed within the lanes and do not contradict the
                        boundary markings; they serve as guidance/restriction information. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed white, crossing the lane line markings with
                        care is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed white, crossing the lane line markings with
                        care is permitted. [[US-3B.06-05-06]]
Step 5  Rule            text:other: Word markings on the pavement are used for the purpose of regulating,
                        warning, or guiding traffic. [[US-3B.20-01]]
Step 5  Rule            text:other: Word markings on the pavement are used for the purpose of regulating,
                        warning, or guiding traffic. [[US-3B.20-01]]
Step 5  Rule            text:other: Word markings on the pavement are used for the purpose of regulating,
                        warning, or guiding traffic. [[US-3B.20-01]]
Step 5  Rule            text:other: Word markings on the pavement are used for the purpose of regulating,
                        warning, or guiding traffic. [[US-3B.20-01]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed, as the left boundary is a dashed white
                        lane line, and crossing is permitted [US-3B.06-05-06].
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed white lane line, and
                        crossing is permitted [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane prohibiting
                        straight movement, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable, as there are no markings indicating a turn left.
Step 6  turn_right      not_applicable: Not applicable, as there are no markings indicating a turn right.
Step 6  u_turn          not_applicable: Not applicable, as there are no markings indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there are no waiting areas or two-way left-turn
                          lanes visible.
Step 7  Reflect         All actions are decided based on the observed markings and boundaries, and no action
                        is allowed when a rule prohibits it.
Advice                  You are in the middle lane, which is designated as a Through Lane. You may change left
                        or right as the lane lines are dashed, but be aware of the lane designations: the left
                        lane is for private cars only, and the right lane is the emergency vehicle lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:other'], missed []), actions False, unsafe ['change_left'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1396, 23.66 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, there is
                        an intersection where the lane markings indicate a possible turn or continuation.
                        (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: a
                        lane line on both sides indicates my lane is between two other lanes. | roles: The
                        color and pattern of both boundaries (solid white lines) fit the role of lane_line
                        separating traffic flowing in the same direction. | markings: The arrow pointing
                        straight ahead is within my lane and is consistent with the lane boundaries. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line marking is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line marking is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a solid white lane_line
                        and [US-3B.06-05-06] states that crossing the lane line marking is discouraged.
Step 6  change_right    prohibited (correct): prohibited, because the right boundary is a solid white
                        lane_line and [US-3B.06-05-06] states that crossing the lane line marking is
                        discouraged.
Step 6  go_straight     allowed (correct): allowed, because the lane marking shows an arrow pointing straight
                        ahead and [US-3B.23-01] indicates that lane-use arrows indicate permissible movements.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane governing this action, and no left-turn waiting
                        area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane governing this action, and no left-turn waiting
                        area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane governing this action, and no left-turn waiting
                        area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight through the intersection.
                        Lane changes to the left or right are discouraged by the solid white lane lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk', 'line:stop_line']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1083, 21.64 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is an intersection where traffic
                        appears to be moving through or approaching it. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): There are white dashed lines marking the boundaries of my
                        lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (both are lane_lines). | roles: The color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: The stop line marking is
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since crossing the lane line markings is not discouraged or prohibited,
                        the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white
                        lane_line, and [US-3B.06-05-06] permits crossing the lane line markings.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed white
                        lane_line, and [US-3B.06-05-06] permits crossing the lane line markings.
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
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there is
                        a stop line visible, you must stop before the line if a stop is required by a traffic
                        control device.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions False, unsafe ['change_left', 'change_right'],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1071, 21.38 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with multiple lanes traveling in the same
                        direction ahead. The road continues straight ahead into the distance. (lanes 3, mine
                        2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is a lane line (indicating a lane to the left), and the right boundary
                        is a lane line (indicating a lane to the right). | roles: The color (white) and
                        pattern (solid) of both boundaries fit the role of a lane line separating traffic
                        flowing in the same direction. | markings: The stop line is located at the end of the
                        lane, which is consistent with the lane boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: White markings delineating the separation of traffic lanes that have
                        the same direction of travel are used for lane lines. [[US-3B.06-01]]
Step 5  Rule            right_boundary: White markings delineating the separation of traffic lanes that have
                        the same direction of travel are used for lane lines. [[US-3B.06-01]]
Step 5  Rule            line:stop_line: Stop lines consist of solid white lines extending across approach
                        lanes to indicate the point at which the stop is intended or required to be made.
                        [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white lane line, and solid lines discourage or prohibit crossing [US-3A.04-01].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white lane line, and solid lines discourage or prohibit crossing [US-3A.04-01].
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
Advice                  You must stay in your lane as both boundaries are solid white lane lines. You may
                        proceed straight ahead until you reach the stop line, where you must stop.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1091, 19.61 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera, and it appears to
                        be approaching an area with overhead signage indicating traffic flow directions.
                        (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line is visible in the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles
                        (white lane lines separating lanes of the same direction). | roles: The solid white
                        lines fit the role of lane_line, indicating separation of traffic flows in the same
                        direction. | markings: The visible dashed line ahead is interpreted as a stop line,
                        which is consistent with the lane markings. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control device. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid white
                        lane_line, and [US-3B.06-05-06] states that crossing the lane line markings is
                        discouraged.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        lane_line, and [US-3B.06-05-06] states that crossing the lane line markings is
                        discouraged.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in the lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane, and there is no left-turn waiting area or two-way left-turn lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight, as lane changes are
                        discouraged by the solid white lines. You must stop at the visible line before
                        proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1065, 16.91 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with traffic moving away from the camera.
                        Ahead, the road continues into the distance with other traffic visible. (lanes 3, mine
                        2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): White arrows indicating straight movement in the lane.;
                        arrow:straight (full): White arrows indicating straight movement in the lane.;
                        arrow:straight (full): White arrows indicating straight movement in the lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is between two other lanes. | roles: The color (white) and pattern (solid) of
                        both boundaries fit the role of a lane_line, indicating separation between lanes
                        traveling in the same direction. | markings: The arrows in my lane all indicate
                        straight movement, which is consistent with the lane boundaries defining a through
                        lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white lane_line and [US-3B.06-05-06] states that crossing the lane line markings is
                        discouraged.
Step 6  change_right    prohibited (contested, label allowed): prohibited, because the right boundary is a
                        solid white lane_line and [US-3B.06-05-06] states that crossing the lane line markings
                        is discouraged.
Step 6  go_straight     allowed (contested, correct): allowed, because the lane marking shows a straight arrow
                        and [US-3B.23-01] indicates that lane-use arrow markings indicate permissible
                        movements.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane governing this action, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane governing this action, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane governing this action, and no left-turn waiting area or two-way
                        left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead, as lane changes are
                        discouraged by the solid white lines. No specific stopping or turning maneuvers are
                        governed by the visible markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1200, 19.21 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into the distance, possibly approaching an intersection or a change in road
                        configuration. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the adjacent lane on the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line separating my lane from the adjacent lane on the right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Two white arrows pointing straight ahead, one in the lane to
                        the left and one in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in a middle lane). | roles: The color and
                        pattern of both boundaries (solid yellow lines) fit the role of a lane line separating
                        traffic flows in the same direction (though yellow lines are typically for opposite
                        directions, here they delineate lanes in the same direction, which is unusual but
                        observed). | markings: The arrows in my lane (straight ahead) agree with the
                        boundaries (which only govern lane changes). | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: When used, lane line pavement markings delineating the separation of
                        traffic lanes that have the same direction of travel shall be white. [[US-3B.06-01]]
Step 5  Rule            right_boundary: When used, lane line pavement markings delineating the separation of
                        traffic lanes that have the same direction of travel shall be white. [[US-3B.06-01]]
Step 5  Rule            arrow:straight: Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes. [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: The left boundary is a solid yellow
                        lane line, and the rule for lane lines separating same-direction traffic suggests
                        white lines should be used, implying a restriction or prohibition based on the
                        observed yellow solid line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid yellow
                        lane line, and the rule for lane lines separating same-direction traffic suggests
                        white lines should be used, implying a restriction or prohibition based on the
                        observed yellow solid line.
Step 6  go_straight     allowed (correct): allowed: The lane marking shows an arrow pointing straight ahead,
                        and no other marking prohibits this movement.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or marking
                        in my lane indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or marking
                        in my lane indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or marking
                        in my lane indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area or a
                          two-way left-turn lane.
Step 7  Reflect         The actions are consistent with the observations, noting the conflict between the
                        observed yellow lines and the rule suggesting white lines for same-direction lane
                        lines, which is interpreted as a prohibition on lane changes.
Advice                  You should stay in your current lane to proceed straight ahead. Lane changes are
                        prohibited by the solid yellow lane lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1118, 20.7 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, there is an
                        intersection visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific lane-use arrows, words, or areas are visible
                        within my lane in the photographed section.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in a middle lane). | roles: The color and
                        pattern of both boundaries (white solid lines) fit the role of lane_line separating
                        traffic flowing in the same direction. | markings: The lack of visible markings in my
                        lane is consistent with the boundaries defining the lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is solid white, crossing the lane line markings is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            no_turn:right: No specific rule passage covers this marking as it was not clearly
                        observed. [null]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the left_boundary, as the solid white
                        line discourages crossing the lane line markings [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the right_boundary, as the
                        solid white line discourages crossing the lane line markings [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited-movement
                        markings in my lane to restrict this movement.
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane to govern this movement.
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane to govern this movement.
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited-movement markings
                        in my lane to govern this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed against a prohibition, and all decisions are based on visible features.
Advice                  You should remain in your current lane to proceed straight through the intersection.
                        Lane changes to the left or right are discouraged by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8624, out 1032, 17.24 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be a multi-lane road leading into an intersection. My car is in one of
                        the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line marking the left boundary of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the stop line.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the yellow line on the left acts as a center line separating traffic in opposite
                        directions, and the white line on the right acts as a lane line separating my lane
                        from the next lane to the right. | roles: The yellow solid line on the left fits the
                        role of a center line separating traffic in opposite directions, and the white solid
                        line on the right fits the role of a lane line separating traffic flows in the same
                        direction. | markings: The stop line is present and is located ahead of the lane,
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: Center line pavement markings, when used, shall be the pavement
                        markings used to delineate the separation of traffic lanes that have opposite
                        directions of travel on a roadway and shall be yellow. [[US-3B.01-01]]
Step 5  Rule            right_boundary: Where crossing the lane line markings is not discouraged or
                        prohibited, the lane line markings shall consist of a normal width broken white line.
                        [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines shall consist of solid white lines extending across
                        approach lanes to indicate the point at which the stop is intended or required to be
                        made. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (correct): prohibited: The solid yellow line on the left acts as a center
                        line, and while the rule for a center line is about separating traffic, the solid
                        nature implies a restriction on crossing it.
Step 6  change_right    allowed (correct): allowed: The solid white line on the right is a lane line, and
                        since no rule prohibits crossing it, it is allowed.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action, and no two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action, and no two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern this action, and no two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change right, go straight, or prepare to stop at the solid white stop line. Do
                        not change left, as the yellow line acts as a center line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1117, 22.85 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway approaching an intersection or a major junction, and my
                        car is in one of the lanes near the bottom of the photo. (lanes 4, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): A large white cross-hatching pattern is visible across the lane
                        ahead.
Step 4  Cross-check     position: The lane count (4) and my lane position (2) agree with the boundary roles
                        (white dashed lines indicate separation between lanes of the same direction). | roles:
                        The white dashed lines fit the role of lane_line, indicating separation between lanes
                        traveling in the same direction. | markings: The area:grid marking is consistent with
                        the lane markings and boundaries; it is located within my lane. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            area:grid: The grid marking indicates an area that vehicles must not block.
                        [[US-3B.26-01-02]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
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
Advice                  You may change lanes left or right, and you may proceed straight ahead. Be aware that
                        the area ahead is marked with a grid, indicating that you must not block this area.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed ['text:other']), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8624, out 1049, 20.56 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a bridge structure ahead, and the road continues
                        straight ahead into the distance. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane boundary ahead.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles
                        (white dashed lines indicate separation between lanes of the same direction). | roles:
                        The white dashed lines fit the role of lane_line, indicating separation between lanes
                        traveling in the same direction. | markings: The partial stop line marking is
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control signal. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): Allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibited-
                        movement markings in the lane, and nothing restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         All actions are decided based on the observed markings and rules, and no action is
                        allowed when prohibited.
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there is
                        a stop line visible, you must stop before it if a traffic control device requires it.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1056, 17.32 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test C | gemma4:e4b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues straight, and there is a lane guidance sign indicating straight movement in
                        all visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line marking the boundary with the left
                        lane.; line:stop_line (insufficient): A white dashed line marking the boundary with
                        the right lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (white dashed lines indicate separation between lanes of the same direction). | roles:
                        The color (white) and pattern (dashed) of both boundaries fit the role of a lane_line.
                        | markings: The lane markings listed are generic line markers and do not contradict
                        the boundaries or each other. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: Since the line is dashed, crossing the lane line markings with care is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Since the line is dashed, crossing the lane line markings with care is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: Stop lines indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign or traffic control signal. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): Allowed because the left boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a white dashed line, and
                        [US-3B.06-05-06] permits crossing the lane line markings with care.
Step 6  go_straight     allowed (correct): Allowed because there are no arrows or prohibited-movement markings
                        in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there are no arrows
                        or prohibited-movement markings in my lane, and no waiting area or two-way left-turn
                        lane is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there are no arrows
                        or prohibited-movement markings in my lane, and no waiting area or two-way left-turn
                        lane is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there are no arrows
                        or prohibited-movement markings in my lane, and no waiting area or two-way left-turn
                        lane is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no specific markings for turning, you should proceed according to standard right-
                        hand traffic rules.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8624, out 1108, 22.41 s
```
