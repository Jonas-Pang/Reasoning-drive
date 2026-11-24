# Reasoning of lane run 20261117_044748_laneC_US

```text
bdd100k_val__b2afce7f-0cb9967a | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with trees lining the right side, and it appears to be
                        leading towards an intersection or a section where lane configuration might change
                        ahead. There are multiple lanes visible in my direction near the bottom of the photo.
                        (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A broken white line is visible in the lane, indicating lane
                        division.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The visible marking (partial stop_line)
                        is consistent with the lane markings. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white lane_line, and
                        [CN-5.2.1-2] permits the crossing of a broken white lane line.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a solid white
                        edge_line, and [CN-5.4.2] permits the use of a solid edge line in this context (though
                        the rule is general, the solid line itself does not prohibit changing right).
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
Advice                  You are in the middle lane, and lane changes to the left or right are permitted as the
                        lane lines allow. You may proceed straight ahead, but be aware of the stop line ahead,
                        which indicates where you should stop if required to yield or wait.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 971, 16.58 s

bdd100k_val__b459e707-2d208c56 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road stretching ahead, leading towards what appears to be a
                        junction or area with buildings on the right. My car is in the lane closest to the
                        center of the visible traffic flow. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid yellow line marking the edge of the travel lane on the right.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A broken white line marking the lane division ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a white dashed lane_line, and the right boundary is a solid yellow
                        edge_line, which fits the roles. | markings: The stop line is visible ahead, and it is
                        consistent with the lane markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white lane_line, and
                        [CN-5.2.1-2] permits the crossable lane line to be crossed.
Step 6  change_right    prohibited (correct): prohibited: The right boundary is a solid yellow edge_line, and
                        [CN-6.1.1] implies that solid lines prohibit crossing, although this is an edge line,
                        the solid nature restricts movement.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but changing right is prohibited by the solid yellow
                        edge line. You may proceed straight, but you must stop before the visible stop line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 1104, 16.07 s

bdd100k_val__b5046f1e-b1ef44b9 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings on both sides, and there is a road ahead leading
                        towards what appears to be an intersection or a continuation of the road. (lanes 2,
                        mine 1, full)
Step 2  Left            There is a solid white line marking the left edge of the travel lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the travel lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (partial): A white arrow pointing straight ahead is visible in
                        the lane.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a solid white lane line, and the right boundary is a solid white edge
                        line, which fits their roles. | markings: The white arrow pointing straight ahead is
                        visible in the lane and is consistent with the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line on the right side of the direction of travel marks
                        the edge of the roadway. [[CN-5.4.3]]
Step 5  Rule            arrow:straight_right: The guide arrow indicates the direction of travel for vehicles,
                        in this case, straight ahead or to the right. [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a solid white lane
                        line, and [CN-6.2.1] prohibits vehicles on the solid-line side from crossing.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid white edge
                        line, and there is no rule prohibiting a lane change onto the shoulder/next lane.
Step 6  go_straight     allowed (contested, correct): allowed: The white arrow indicates straight ahead or to
                        the right, and there is no restriction prohibiting going straight.
Step 6  turn_left       prohibited: prohibited: The white arrow indicates straight ahead or to the right, and
                        does not show a left turn.
Step 6  turn_right      allowed: allowed: The white arrow indicates straight ahead or to the right, and
                        permits turning right.
Step 6  u_turn          prohibited: prohibited: The white arrow indicates straight ahead or to the right, and
                        does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of the lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane of two lanes. You may change right, go straight, or turn
                        right. You are prohibited from changing left, turning left, or making a U-turn.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['text:only']), actions False, unsafe
                        ['change_right'], citation in_pack_not_accepted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 7597, out 832, 13.5 s

bdd100k_val__b6decb24-82234e11 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes heading forward, and there is a multi-lane
                        intersection ahead. (lanes 3, mine 2, full)
Step 2  Left            The left boundary is marked by a solid white line, and beyond it, there is a curb.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           The right boundary is marked by a broken white line, and beyond it, the road
                        continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits the roles of lane_line. | markings: The stop line is visible, and it
                        is consistent with the lane markings. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): Allowed because the left boundary is a solid white
                        lane line, and [CN-6.2.1] prohibits crossing from the solid side, but since I am on
                        the solid side, I cannot cross left.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a broken white lane line, and
                        [CN-5.2.1-2] permits crossing.
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
Advice                  You may change right into the adjacent lane, or proceed straight ahead. You must stop
                        before the visible stop line if you intend to stop for any reason.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 1024, 17.31 s

bdd100k_val__b7719f1d-e6e580dd | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or major road with traffic moving away from the camera.
                        Ahead, the road continues, and there is a barrier on the right side. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right, which is
                        adjacent to a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:right (insufficient): There are no arrows, words, symbols, areas, or lines
                        painted within my lane visible from the bottom to the end of the lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is a dashed white lane_line, and the right boundary is a solid white
                        edge_line, which fits their roles. | markings: The lack of markings in the lane is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane_line, and
                        [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        edge_line, and [CN-4.2.2-a] implies that a solid line prohibits crossing, although
                        this is an edge line.
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
Advice                  You may change lanes to the left, but changing right is prohibited by the solid white
                        edge line. You may proceed straight, but turning left, right, or making a U-turn is
                        not governed by any markings in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7597, out 1102, 16.14 s

bdd100k_val__b775af1c-bb5afbe3 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the lane closest
                        to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a crossable
                        lane line separating lanes of the same direction. | markings: The arrow pointing
                        straight ahead is consistent with the lane markings and boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, correct): prohibited: The left boundary is a white dashed lane
                        line, and while this line is crossable, the arrow in my lane only permits straight or
                        right movement.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a white dashed
                        lane line, and the arrow in my lane permits straight or right movement.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: The arrow in my lane permits straight
                        ahead movement.
Step 6  turn_left       prohibited (correct): prohibited: The arrow in my lane does not show a left turn
                        movement.
Step 6  turn_right      allowed (correct): allowed: The arrow in my lane permits a right turn movement.
Step 6  u_turn          prohibited (correct): prohibited: The arrow in my lane does not show a U-turn
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a left-turn waiting
                          area or a two-way left-turn lane directly to the left.
Step 7  Reflect         consistent
Advice                  You are in a lane that permits going straight or turning right. You may change right
                        if necessary, but you cannot turn left or make a U-turn from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:right', 'line:stop_line']), actions False,
                        unsafe ['go_straight'], citation in_pack_not_accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 7597, out 796, 15.46 s

bdd100k_val__b9db357e-cd30a8ae | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the lane closest
                        to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the stop line.
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
Step 6  change_left     allowed (contested, correct): allowed: The left boundary is a dashed lane_line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    prohibited (contested, label not_determined): prohibited: The right boundary is a
                        solid edge_line, and [CN-4.2.2-a] prohibits crossing a solid line (unless in
                        emergency).
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change left into the adjacent lane, but changing right is prohibited by the
                        solid white edge line. You may proceed straight through the intersection, but you must
                        stop before the solid white stop line.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 1049, 13.89 s

bdd100k_val__bc05c126-d00aeb9c | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards a distant intersection. My car is in the
                        rightmost lane visible in the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            There is a double solid yellow line separating my lane from the adjacent lane to the
                        left.
                        yellow double_solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): Two parallel solid yellow lines marking the center of the
                        road ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the double solid yellow line on the left indicates another lane to the left, and the
                        solid white line on the right indicates the edge of the roadway. | roles: The double
                        solid yellow line on the left fits the role of a lane_line separating traffic in the
                        same direction (though yellow lines usually separate opposing traffic, here it
                        functions as a lane divider between lanes going the same way, which is unusual but
                        observed), and the solid white line on the right fits the role of an edge_line. |
                        markings: The line:stop_yield marking is present in my lane and is consistent with the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a double solid yellow
                        line, and [CN-6.1.2] prohibits crossing.
Step 6  change_right    allowed (contested, label prohibited): allowed, because the right boundary is a solid
                        white edge line, and no rule prohibits crossing it.
Step 6  go_straight     stop_first (contested, label allowed): stop_first, because the marking line:stop_yield
                        is present in my lane, and [CN-6.5.1.1-2] turns allowed movements into stop_first.
Step 6  turn_left       stop_first: stop_first, because the marking line:stop_yield is present in my lane, and
                        [CN-6.5.1.1-2] turns allowed movements into stop_first.
Step 6  turn_right      stop_first: stop_first, because the marking line:stop_yield is present in my lane, and
                        [CN-6.5.1.1-2] turns allowed movements into stop_first.
Step 6  u_turn          stop_first: stop_first, because the marking line:stop_yield is present in my lane, and
                        [CN-6.5.1.1-2] turns allowed movements into stop_first.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before the stop-and-yield line to proceed straight,
                        turn left, turn right, or make a U-turn. You may change lanes to the right, but
                        changing left is prohibited by the double solid yellow line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 7597, out 1147, 23.68 s

bdd100k_val__bca36352-5de70a3f | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the
                        rightmost lane visible in the immediate foreground. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the stop line for the intersection
                        ahead.; line:stop_line (full): A solid white line segment indicating the boundary of
                        the lane ahead of the stop line.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a dashed white lane line, which fits the role of separating lanes in
                        the same direction. The right boundary is a solid white edge line, which fits the role
                        of marking the edge of the roadway. | markings: The stop lines are consistent with the
                        boundaries and do not contradict any other markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed white lane line, and
                        [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a solid white
                        edge line, and [CN-5.4.3] indicates this is the edge line on the right side of the
                        direction of travel.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which allows you to go straight or change left or
                        right. You must stop at the solid white stop line before entering the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 1105, 16.17 s

bdd100k_val__bcbbfd82-add80c05 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road at night, and there is a commercial area ahead, suggesting
                        an intersection or a stretch of city road. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the travel lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No markings are visible within my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is a solid white
                        edge line, and the right boundary is a dashed white lane line, which fits their roles.
                        | markings: There are no arrows, words, or areas in my lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/non-motor separation line between traffic in the same direction shall be white.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element as it was not observed.
                        [null]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The right boundary is a broken white lane
                        line, and [CN-5.2.1-2] permits crossing the lane line.
Step 6  change_right    allowed (correct): allowed: The left boundary is a solid white edge line, and
                        [CN-4.2.2-a] implies that a solid line prohibits crossing, but since the right
                        boundary is a lane line, the left boundary's role as an edge line does not prohibit a
                        lane change to the left.
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
Advice                  You are in the leftmost lane of two. You may change left or right, and you may proceed
                        straight. Since there are no specific markings for turns, you may proceed straight or
                        turn if the intersection allows it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation
                        unlisted, contradictions []
Tokens                  in 7597, out 1062, 17.29 s

bdd100k_val__bd026bc5-9418706c | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is an urban road with multiple lanes ahead, leading towards an intersection. My
                        car is in one of the lanes near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a broken white line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow pointing straight ahead is visible in my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles: a
                        lane line on the left means another lane to the left, and a lane line on the right
                        means another lane to the right. | roles: The white dashed line on the left fits the
                        role of a crossable lane line, and the white solid line on the right fits the role of
                        a no-crossing lane line. | markings: The white arrow showing straight ahead is
                        consistent with the lane markings and boundaries. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     allowed (contested, correct): Prohibited by the right boundary's role as a lane line,
                        but the left boundary is a crossable lane line, and the arrow does not prohibit a lane
                        change.
Step 6  change_right    prohibited (contested, label allowed): Prohibited by the right boundary, which is a
                        no-crossing lane line ([CN-6.2.1]).
Step 6  go_straight     allowed (correct): Allowed because the arrow shows straight ahead ([CN-5.13.1]) and
                        nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane that allows or prohibits a left turn.
Step 6  turn_right      allowed (WRONG, label prohibited): Allowed because the arrow shows straight or right
                        ([CN-5.13.1]) and nothing restricts turning right.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane that allows or prohibits a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         Consistent, as the right boundary prohibits changing right, the arrow permits going
                        straight and turning right, and the left boundary permits changing left.
Advice                  You may proceed straight or turn right from your lane. Lane changes to the left are
                        permitted, but changing right is prohibited by the solid white line. Use this lane for
                        straight or right turns.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight', 'line:stop_line']), actions False,
                        unsafe ['turn_right'], citation in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 1069, 22.09 s

bdd100k_val__be278041-2173a980 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or approach road at night, and there is an elevated
                        structure or overpass ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line on the left side of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           There is a solid white line on the right side of my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): A yellow diamond-shaped warning sign is visible on the left side of
                        the road.; line:stop_line (full): A solid white line is painted across the lane ahead,
                        likely a stop line or guide line.; area:channelizing (full): A chevron marking is
                        visible on the right side of the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        yellow center line on the left indicates traffic in the opposite direction, and the
                        white edge line on the right indicates the edge of the roadway. | roles: The yellow
                        solid line on the left fits the role of a center_line separating opposing traffic, and
                        the white solid line on the right fits the role of an edge_line. | markings: The
                        warning sign is context, the stop line is visible ahead, and the channelizing marking
                        is visible ahead. They are consistent with the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            text:other: The warning sign is informative and does not restrict movement based on
                        the provided rules. [null]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 5  Rule            area:channelizing: Channelizing lines show that vehicles must follow the set path and
                        may not drive on or across the lines. [[CN-6.6.1-3]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid yellow center_line, and
                        [CN-6.1.1] prohibits crossing.
Step 6  change_right    allowed (contested, correct): allowed: The right boundary is a solid white edge_line,
                        and no rule prohibits crossing it in the visible stretch.
Step 6  go_straight     allowed (contested, correct): allowed: No arrow in my lane restricts carrying on
                        straight along my lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may change right if necessary. You may proceed
                        straight ahead, but you must stop before the solid white line ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing', 'line:stop_line', 'text:other'], missed []), actions True,
                        unsafe [], citation unlisted, contradictions []
Tokens                  in 7597, out 975, 16.67 s

bdd100k_val__be4cbd00-97fec78b | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road at night, and there is an intersection ahead. (lanes 2, mine
                        1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles
                        (both are lane_lines separating lanes in the same direction). | roles: The color and
                        pattern of both boundaries (solid white lines) fit the role of a lane_line. |
                        markings: The stop line agrees with the boundaries as it marks the end of the lane. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
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
Step 6  go_straight     allowed (correct): allowed, because there are no arrows or prohibited-movement
                        markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable (WRONG, label not_determined): not_applicable, because there is no
                        arrow or prohibited-movement marking in my lane, and no waiting area or two-way left-
                        turn lane is visible.
Step 6  turn_right      not_applicable (WRONG, label not_determined): not_applicable, because there is no
                        arrow or prohibited-movement marking in my lane, and no waiting area or two-way left-
                        turn lane is visible.
Step 6  u_turn          not_applicable (WRONG, label not_determined): not_applicable, because there is no
                        arrow or prohibited-movement marking in my lane, and no waiting area or two-way left-
                        turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You may proceed straight through the intersection, but you must stop at the
                        solid white stop line before entering the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 7597, out 1021, 13.84 s

bdd100k_val__beccfad4-d24a29c5 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This appears to be a multi-lane road leading towards an overpass or intersection in
                        the distance. My car is in one of the lanes near the bottom of the photo. (lanes 2,
                        mine 1, full)
Step 2  Left            There is a concrete barrier/curb on the left side of my lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is a concrete
                        barrier/curb (edge_line), and the right boundary is a solid white line (lane_line),
                        which fits the roles. | markings: There are no arrows, words, or areas painted in my
                        lane, so there are no internal contradictions. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Where a non-motorized lane is needed and there is no separating
                        facility between it and the motor vehicle lanes, a motor/non-motor separation line
                        shall be provided, but here a physical barrier exists. [[CN-5.4.5]]
Step 5  Rule            right_boundary: The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. [[CN-6.2.1]]
Step 5  Rule            left_boundary: No specific rule passage covers the concrete barrier/curb as an edge
                        line in this context. [null]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited, and may be crossed
                        in an emergency when it is safe. [[CN-4.2.2-a]]
Step 6  change_left     not_applicable (WRONG, label prohibited): not_applicable
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of two. You may proceed straight, but changing right into
                        the adjacent lane is prohibited by the solid white line. No specific turning movements
                        are governed by markings in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 7597, out 767, 10.65 s

bdd100k_val__bf6315ee-a77e1bb2 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road at night, and there is an intersection ahead. (lanes
                        2, mine 1, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the boundary between my lane and
                        the lane to my left.; line:stop_line (partial): A white dashed line marking the
                        boundary between my lane and the lane to my right.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line.
                        | markings: The stop lines are located at the end of the visible lane area, consistent
                        with the boundaries. | unseen: No attributes were reported that were not actually
                        seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white line, and [CN-5.2.1-2]
                        permits crossing the lane line.
Step 6  change_right    allowed (contested, correct): allowed: The right boundary is a broken white line, and
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
                          turn lane directly to the left of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right as the lane lines are broken. You may proceed
                        straight through the intersection, but you must stop before the stop line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7597, out 889, 22.88 s

bdd100k_val__bf6711ef-76e408aa | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, likely an elevated or underpass section, leading towards an
                        intersection ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a yellow solid line on the left side of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           There is a white broken line on the right side of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane to
                        my right.; arrow:straight (full): A white arrow pointing straight ahead is visible in
                        the lane to my left.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the yellow solid line on the left acts as a center_line separating opposing traffic,
                        and the white broken line on the right acts as a lane_line separating my lane from the
                        lane to the right. | roles: The yellow solid line on the left fits the role of a
                        center_line separating opposing traffic, and the white dashed line on the right fits
                        the role of a lane_line separating traffic in the same direction. | markings: The
                        arrows in my lane show straight ahead, which is consistent with the lane markings and
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and an
                        arrow pointing straight ahead indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a solid yellow
                        center_line, and [CN-6.1.1] prohibits crossing.
Step 6  change_right    allowed (contested, correct): allowed, because the right boundary is a broken white
                        lane_line, and [CN-5.2.1-2] permits crossing.
Step 6  go_straight     allowed (correct): allowed, because the arrow in my lane shows straight ahead, and
                        [CN-5.13.1] indicates this direction of travel.
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
Advice                  You may change right into the adjacent lane, and you are permitted to go straight
                        ahead. Do not attempt to change left, as it is prohibited by the solid yellow center
                        line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['text:only']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7597, out 1185, 18.68 s

bdd100k_val__bfd64d5f-ec05de8b | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway approaching an exit ramp. My car is in the rightmost lane
                        of the visible lanes in my direction. (lanes 3, mine 3, full)
Step 2  Left            There is a broken white line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A white solid line marking the end of the current lane,
                        indicating the exit ramp.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a broken white lane line, which fits the role of separating lanes in
                        the same direction. The right boundary is a solid white edge line, which fits the role
                        of marking the edge of the roadway. | markings: The stop line is located at the end of
                        the lane, consistent with the lane structure. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized vehicle lanes. [[CN-5.4.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken white lane line, and
                        [CN-5.2.1-2] permits the crossable lane line to separate traffic flows in the same
                        direction.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid white edge
                        line, and while no specific rule prohibits changing onto the exit ramp, the solid line
                        suggests a defined edge.
Step 6  go_straight     prohibited (contested, label allowed): prohibited: The lane ends at a stop line, and
                        [CN-6.4.1-2] indicates this line marks where vehicles stop when waiting to proceed.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a left-turn waiting
                          area or a two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You should prepare to exit the highway as the lane ends at a stop line. A lane change
                        to the left is permitted, but changing right is restricted by the edge line. Use the
                        exit ramp indicated by the signs.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 7597, out 1065, 16.16 s

bdd100k_val__c01c4d85-36b417ee | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road at night, and there is a marked area ahead suggesting an
                        intersection or lane change zone. (lanes 3, mine 2, full)
Step 2  Left            There is a white broken line on the left side of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line on the right side of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): A series of dashed white lines forming a pattern ahead of the car.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) are consistent with the
                        boundaries, as both sides have lane lines, indicating multiple lanes in the same
                        direction. | roles: The white dashed lines on both sides fit the role of a lane_line
                        separating traffic flows in the same direction. | markings: The area:grid marking is
                        ahead of the lane and is consistent with the lane markings. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            area:grid: The grid marking shows an area where stopping for any reason is prohibited.
                        [[CN-6.8.1-2]]
Step 6  change_left     allowed (correct): allowed: The left_boundary is a crossable lane line, and
                        [CN-5.2.1-2] permits the separation of traffic flows in the same direction.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right_boundary is a crossable lane
                        line, and [CN-5.2.1-2] permits the separation of traffic flows in the same direction.
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
Advice                  You may change lanes left or right, and you may proceed straight ahead. Be aware that
                        the grid marking ahead prohibits stopping for any reason in that area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7597, out 1034, 20.16 s

bdd100k_val__c0a71f47-14439a44 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road at night, and there is a street ahead with traffic
                        continuing in both directions. (lanes 2, mine 1, full)
Step 2  Left            There is a yellow dashed line separating my lane from the adjacent lane to the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        yellow dashed line on the left indicates another lane to the left, and the solid white
                        line on the right indicates the edge of the roadway. | roles: The yellow dashed line
                        on the left fits the role of a lane_line separating traffic in the same direction, and
                        the solid white line on the right fits the role of an edge_line. | markings: There are
                        no arrows, words, or areas in my lane, so this check is consistent. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: No rule passage specifically governs this element as it was not
                        observed. [null]
Step 5  Rule            line:yield_line: No rule passage specifically governs this element as it was not
                        observed. [null]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed line, and
                        [CN-4.2.2-a] states a broken line means it may be crossed.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid line, but no
                        rule passage explicitly prohibits changing right when the line is solid, and
                        [CN-4.2.2-a] only prohibits crossing on a solid line.
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
Advice                  You are in the left lane of a two-lane road. You may change left because the line is
                        dashed, and you may change right because the line is solid. You may proceed straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7597, out 920, 18.05 s

bdd100k_val__c0f5b0d0-17e0110c | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road at night, and there is an intersection ahead. (lanes 2, mine
                        1, full)
Step 2  Left            There is a solid yellow line on the left side of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           There is a broken white line on the right side of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the right edge of my lane.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        yellow solid line on the left acts as a center line separating opposing traffic, and
                        the white dashed line on the right acts as a lane line separating my lane from another
                        lane in the same direction. | roles: The yellow solid line on the left is consistent
                        with a center line separating opposing traffic, and the white dashed line on the right
                        is consistent with a lane line separating traffic in the same direction. | markings:
                        The stop line is located at the end of the lane, which is consistent with the lane
                        structure. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction, and it is a broken white line.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited: The solid yellow line on the left prohibits crossing
                        into the opposing traffic flow, as per [CN-6.1.1].
Step 6  change_right    allowed (contested, label prohibited): allowed: The broken white line on the right
                        permits crossing into the adjacent lane, as per [CN-5.2.1-2].
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
Step 7  Reflect         consistent
Advice                  You may change right into the adjacent lane, or proceed straight ahead. You must stop
                        at the solid white line before entering the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 1012, 18.38 s

bdd100k_val__c16d3fdb-a3a8c912 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway with a barrier on the left and a guardrail on the right,
                        leading towards a distant area where the road appears to continue straight. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a concrete barrier separating the road from the left side.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is a metal guardrail separating the road from the right side.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles, as
                        the left boundary is an edge line and the right boundary is an edge line, suggesting
                        the lane is between two edges or lanes. | roles: The left boundary is a concrete
                        barrier (edge_line) and the right boundary is a guardrail (edge_line). | markings:
                        There are no markings in the lane to check against boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: Where a non-motorized lane is needed and there is no separating
                        facility between it and the motor vehicle lanes, a motor/non-motor separation line
                        shall be provided. [[CN-5.4.5]]
Step 5  Rule            right_boundary: Where a non-motorized lane is needed and there is no separating
                        facility between it and the motor vehicle lanes, a motor/non-motor separation line
                        shall be provided. [[CN-5.4.5]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: no marking governs this action
Step 6  change_right    allowed (correct): allowed: no marking governs this action
Step 6  go_straight     allowed (contested, correct): allowed: nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it
Step 6  turn_left       not_applicable: not_applicable: for turn_left, turn_right and u_turn: no arrow and no
                        prohibited-movement marking in my lane; no waiting area and no two-way left-turn lane
Step 6  turn_right      not_applicable: not_applicable: for turn_left, turn_right and u_turn: no arrow and no
                        prohibited-movement marking in my lane; no waiting area and no two-way left-turn lane
Step 6  u_turn          not_applicable: not_applicable: for turn_left, turn_right and u_turn: no arrow and no
                        prohibited-movement marking in my lane; no waiting area and no two-way left-turn lane
Step 6  enter_waiting_areanot_applicable: not_applicable: nothing in view governs it
Step 7  Reflect         consistent
Advice                  You may change lanes left or right, and you may proceed straight ahead. Since there
                        are no markings indicating turns, you should proceed straight unless you intend to
                        change lanes to exit or turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions ['change_left allowed across a curb', 'change_right decided with
                        nothing marked on that side']
Tokens                  in 7597, out 936, 14.93 s

bdd100k_val__c1e6340e-084ce27d | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway at night, and there is no immediate intersection or ramp
                        visible ahead, just the continuation of the road. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the adjacent lane on the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): A solid yellow line runs down the center of the visible
                        road, separating opposing traffic.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        left boundary is a yellow solid lane line, and the right boundary is a white solid
                        edge line, which fits their roles. | markings: The solid yellow line observed is a
                        center line, which is consistent with the boundaries and general road markings. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (correct): Prohibited by the left_boundary because it is a solid yellow
                        lane line, and [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (correct): Allowed because the right_boundary is a solid white edge line, and
                        there is no rule prohibiting a lane change onto the shoulder/beyond.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not govern going straight.
Step 6  turn_left       not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You may change right, go straight, or proceed as is, but changing left is prohibited
                        by the solid yellow line. Since there are no specific markings for turns, you should
                        proceed cautiously.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 7597, out 1069, 16.18 s

bdd100k_val__c39dc2ff-6976d19d | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a city street at night, and there is traffic ahead, including vehicles and
                        pedestrian activity. My car is in one of the lanes moving forward. (lanes 2, mine 1,
                        full)
Step 2  Left            There is a solid white line marking the left edge of the travel lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right edge of the travel lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): The word 'ONLY' is painted on the lane.; arrow:left (full): A left-
                        pointing arrow is painted on the lane.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles, as
                        the left boundary is a lane line and the right boundary is a lane line, indicating two
                        lanes in the direction of travel. | roles: The color and pattern of both boundaries
                        (solid white lines) fit the role of a lane line separating traffic flows in the same
                        direction. | markings: The text 'ONLY' and the left-pointing arrow are present in the
                        lane and do not contradict the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            text:only: No specific rule passage was found that dictates the action based on the
                        'ONLY' text marking. [null]
Step 5  Rule            arrow:left: Guide arrows indicate the direction of travel for vehicles, and this arrow
                        indicates a left turn. [[CN-5.13.1]]
Step 5  Rule            line:stop_line: No stop line was observed in the lane. [null]
Step 5  Rule            line:yield_line: No yield line was observed in the lane. [null]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white lane line, and
                        [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    prohibited (contested, label allowed): prohibited: The right boundary is a solid white
                        lane line, and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  go_straight     prohibited (correct): prohibited: The lane marking includes a left-pointing arrow, and
                        [CN-5.13.1] indicates the direction of travel is restricted to the arrow's direction.
Step 6  turn_left       allowed (correct): allowed: The lane marking includes a left-pointing arrow, and
                        [CN-5.13.1] indicates this movement is permitted.
Step 6  turn_right      prohibited (correct): prohibited: The lane marking includes a left-pointing arrow, and
                        [CN-5.13.1] indicates the direction of travel is restricted to the arrow's direction.
Step 6  u_turn          prohibited (contested, label allowed): prohibited: The lane marking includes a left-
                        pointing arrow, and [CN-5.13.1] indicates the direction of travel is restricted to the
                        arrow's direction.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          was observed.
Step 7  Reflect         consistent
Advice                  You must stay in this lane, as it is marked 'ONLY' for left turns. You are only
                        permitted to turn left at the next intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 7597, out 1022, 15.18 s

bdd100k_val__c3ecb3cb-5fb43d29 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the rightmost lane
                        visible in the direction of travel. (lanes 3, mine 3, full)
Step 2  Left            There is a solid white line separating my lane from the adjacent lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): The word 'ONLY' painted in large white letters.;
                        arrow:straight_right (full): A white arrow pointing straight ahead.
Step 4  Cross-check     position: The lane count (3) and my lane position (3) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        color and pattern of the boundaries fit their roles: the left boundary is a solid
                        white lane line, and the right boundary is a solid white edge line. | markings: The
                        markings agree: the 'ONLY' text and the straight-ahead arrow are within the lane and
                        do not contradict the boundaries. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            text:other: No specific rule passage covers the meaning of the 'ONLY' text marking.
                        [null]
Step 5  Rule            arrow:straight_right: Guide arrows indicate the direction of travel for vehicles, and
                        this arrow indicates straight ahead or right. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a solid white lane line
                        and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    allowed (contested, correct): allowed, because the right boundary is a solid white
                        edge line, and no rule prohibits changing right onto the edge.
Step 6  go_straight     allowed (correct): allowed, because the arrow shows straight ahead, and no other
                        marking prohibits it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in the lane governing this action.
Step 6  turn_right      allowed (WRONG, label prohibited): allowed, because the arrow shows straight or right,
                        and no other marking prohibits it.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in the lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane, which is designated for straight or right turns, as
                        indicated by the arrow. You may change right if necessary, but changing left is
                        prohibited by the solid white line. You should proceed straight or turn right at the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_right', 'text:other'], missed ['arrow:straight', 'text:only']),
                        actions False, unsafe ['turn_right'], citation unlisted, contradictions []
Tokens                  in 7597, out 1093, 18.32 s

bdd100k_val__c400a0e1-c137168b | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an elevated structure overhead, and the road continues
                        ahead towards what appears to be an intersection or another section of the roadway.
                        (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the adjacent lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the adjacent lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line (separating from lane 1), and the right boundary is a
                        lane_line (separating from lane 3). | roles: The left boundary is yellow solid, which
                        is consistent with a lane_line separating traffic flows in opposite directions if it
                        were a center line, but since it's a lane_line, the color is noted. The right boundary
                        is white solid, consistent with a lane_line separating traffic flows in the same
                        direction. | markings: The stop line is present at the end of the lane, which is
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited, because the left boundary is a solid yellow
                        lane_line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    prohibited (contested, label allowed): prohibited, because the right boundary is a
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
Advice                  You must remain in your current lane as lane changes are prohibited by the solid lane
                        lines. You may proceed straight ahead until you reach the stop line, where you must
                        stop.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 1104, 24.06 s

bdd100k_val__c464c963-0279dcc0 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving away from the camera. Ahead, the road
                        continues into a more built-up area, but no specific intersection or end of lane is
                        visible in the immediate foreground. (lanes 2, mine 1, full)
Step 2  Left            There is a yellow solid line marking the left edge of the travel lane.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           There is a broken yellow line marking the right edge of the travel lane.
                        yellow dashed, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (full): A solid yellow line runs down the center of the road,
                        separating opposing traffic.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge line (yellow, indicating the left side of travel), and the
                        right boundary is an edge line (yellow, indicating the right side of travel). | roles:
                        The left boundary is yellow solid, fitting the role of an edge line on the left side
                        of travel (CN-5.4.3). The right boundary is yellow dashed, fitting the role of an edge
                        line on the right side of travel (CN-5.4.3). | markings: The central marking is a
                        solid yellow line, which functions as a no-crossing centre line (CN-6.1.1). This is
                        consistent with the boundaries defining the travel lanes. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow. [[CN-5.4.3]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a yellow solid edge line, and
                        while the rule for edge lines is informative, the solid nature suggests restriction,
                        and the general rule for solid lines prohibits crossing (CN-4.2.2-a).
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a yellow dashed edge
                        line, and a broken line means it may be crossed (CN-4.2.2-a).
Step 6  go_straight     stop_first (contested, label allowed): stop_first: The lane contains a stop-and-yield
                        line (line:stop_yield), which turns all allowed movements into stop_first
                        (CN-6.5.1.1-2).
Step 6  turn_left       stop_first: stop_first: The lane contains a stop-and-yield line (line:stop_yield),
                        which turns all allowed movements into stop_first (CN-6.5.1.1-2).
Step 6  turn_right      stop_first: stop_first: The lane contains a stop-and-yield line (line:stop_yield),
                        which turns all allowed movements into stop_first (CN-6.5.1.1-2).
Step 6  u_turn          stop_first: stop_first: The lane contains a stop-and-yield line (line:stop_yield),
                        which turns all allowed movements into stop_first (CN-6.5.1.1-2).
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area
                          ahead of the lane.
Step 7  Reflect         All actions are decided based on the observed markings and rules, and no action is
                        allowed when prohibited.
Advice                  You must come to a complete stop before proceeding into the intersection. You may
                        change right, but you must stop first before attempting any movement, including going
                        straight, turning left, turning right, or U-turning.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 7597, out 1234, 20.71 s

bdd100k_val__c4b77809-63fd577c | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is an urban street scene with buildings on both sides, and ahead there is an
                        intersection where traffic flow is regulated by markings. (lanes 2, mine 1, full)
Step 2  Left            The left boundary is marked by a yellow solid line near the bottom, transitioning to a
                        yellow dashed line further ahead.
                        yellow solid_dashed (near line solid), curb no, center_line, evidence full
Step 2  Right           The right boundary is marked by a white dashed line.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (full): A double yellow line is visible near the bottom, which appears
                        to be the center line separating traffic flows.; line:stop_yield (partial): A yellow
                        dashed line is visible further ahead, indicating a lane boundary.; line:stop_yield
                        (partial): A white dashed line is visible on the right side of the lane.;
                        line:stop_yield (partial): A white dashed line is visible on the left side of the
                        lane, near the intersection.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a center_line, and the right boundary is an edge_line. | roles: The
                        left boundary is yellow and solid_dashed, fitting the role of a center_line separating
                        opposing traffic. The right boundary is white and dashed, fitting the role of an
                        edge_line. | markings: The markings observed (stop_yield lines) are consistent with
                        the boundaries, although the specific markings are not fully detailed in the provided
                        list for the observed lines. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: The edge line at an emergency stopping lane shall be solid.
                        [[CN-5.4.7]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (correct): prohibited due to the left boundary being a center_line with a
                        solid component, which prohibits crossing.
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a dashed
                        edge_line, which permits crossing.
Step 6  go_straight     stop_first (contested, correct): stop_first because the lane contains a
                        line:stop_yield marking, which turns all allowed movements into stop_first.
Step 6  turn_left       stop_first: stop_first because the lane contains a line:stop_yield marking, which
                        turns all allowed movements into stop_first.
Step 6  turn_right      stop_first: stop_first because the lane contains a line:stop_yield marking, which
                        turns all allowed movements into stop_first.
Step 6  u_turn          stop_first: stop_first because the lane contains a line:stop_yield marking, which
                        turns all allowed movements into stop_first.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must come to a complete stop before proceeding through the intersection. You may
                        change lanes to the right, but you must stop first before making any movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed ['line:stop_line', 'text:stop']), actions False, unsafe
                        ['change_right'], citation in_pack_not_accepted, contradictions ['turn_left,
                        turn_right, u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 7597, out 1169, 20.32 s

bdd100k_val__c4d25f00-3b1d8669 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road at night, and there is an intersection ahead. (lanes
                        3, mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white broken line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane boundary to the left.;
                        line:stop_line (partial): A white dashed line marking the lane boundary to the right.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of a lane_line
                        separating traffic in the same direction. | markings: The stop lines are located at
                        the end of the visible lane area, consistent with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): Allowed because the left boundary is a dashed line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  change_right    allowed (correct): Allowed because the right boundary is a dashed line, and
                        [CN-4.2.2-a] permits crossing a broken line.
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
Step 7  Reflect         The actions are consistent with the observations and the cited rules.
Advice                  You may change lanes left or right as the lane lines are broken, and you may proceed
                        straight through the intersection. Since there are no specific turn arrows, you can
                        proceed straight, but be mindful of the intersection ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7597, out 1032, 16.0 s

bdd100k_val__c4e92086-e1b8324f | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road, and ahead there appears to be an intersection or a section
                        where lane configuration changes. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No specific markings like arrows, text, or areas are visible
                        within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        color (white) and pattern (dashed) of both boundaries fit the role of a lane_line. |
                        markings: The lack of specific markings in the lane is consistent with the boundaries
                        defining the lane. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            no_turn:right: No specific rule passage covers this general absence of a prohibited
                        movement marking. [null]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed lane_line, and [CN-4.2.2-a]
                        permits crossing a broken line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a dashed lane_line,
                        and [CN-4.2.2-a] permits crossing a broken line.
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
                        are no specific markings for turns, you may proceed with caution for turning
                        movements.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_right'], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7597, out 1036, 25.83 s

bdd100k_val__c55da7df-facccafc | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection or a point where the road
                        configuration changes, and my car is in one of the lanes ahead. (lanes 3, mine 2,
                        full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right, and beyond
                        that, there is a curb/shoulder area.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        text:only (full): The word 'ONLY' is painted on the pavement in the center of my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        white dashed line on the left fits the role of a crossable lane line (CN-5.2.1-2) and
                        the white dashed line on the right fits the role of a broken edge line (CN-5.4.2). |
                        markings: The text 'ONLY' is present in my lane and does not contradict the boundaries
                        or other markings. | unseen: No attributes were reported that were not actually seen.
                        | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken edge line has 60 cm segments and 30 cm gaps (also called a
                        "dense broken line"). [[CN-5.4.2]]
Step 5  Rule            text:only: No specific rule passage covers the meaning of the 'ONLY' text marking.
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a broken line, which means it may
                        be crossed (CN-4.2.2-a).
Step 6  change_right    allowed (contested, label prohibited): Allowed, as the right boundary is a broken edge
                        line, which implies it can be crossed (CN-5.4.2).
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited markings
                        in my lane that restrict going straight.
Step 6  turn_left       not_applicable: Not applicable, as there are no arrows or prohibited markings in my
                        lane that govern turning movements.
Step 6  turn_right      not_applicable: Not applicable, as there are no arrows or prohibited markings in my
                        lane that govern turning movements.
Step 6  u_turn          not_applicable: Not applicable, as there are no arrows or prohibited markings in my
                        lane that govern U-turn movements.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed while prohibited, or decided without governing features.
Advice                  You may change lanes left or right, and you may proceed straight ahead. The 'ONLY'
                        marking indicates a restriction that should be noted in your driving.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right allowed across a curb']
Tokens                  in 7597, out 1050, 17.19 s

bdd100k_val__c588eb5e-dfd59d8e | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road at dusk, and there is traffic ahead, suggesting a
                        continuation of the road rather than an immediate intersection or ramp. (lanes 3, mine
                        2, full)
Step 2  Left            There is a yellow solid line on the left side of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           There is a yellow solid line on the right side of my lane.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_yield (partial): A double solid yellow line is visible ahead.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) are consistent with the
                        boundaries, as the left and right boundaries are center lines separating traffic
                        flows. | roles: The yellow solid lines fit the role of a center_line separating
                        opposing traffic flows. | markings: The double solid yellow line ahead is consistent
                        with the boundaries, as it reinforces the prohibition on crossing. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.1]]
Step 5  Rule            line:stop_yield: The stop-and-yield line means that vehicles shall stop completely
                        before entering the intersection and may proceed only after making sure it is safe.
                        [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (correct): prohibited due to the left_boundary being a solid yellow
                        center_line, which prohibits crossing.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited due to the right_boundary being a solid
                        yellow center_line, which prohibits crossing.
Step 6  go_straight     stop_first (contested, label allowed): stop_first because the line:stop_yield marking
                        requires vehicles to stop completely before entering the intersection.
Step 6  turn_left       stop_first: stop_first because the line:stop_yield marking requires vehicles to stop
                        completely before entering the intersection.
Step 6  turn_right      stop_first: stop_first because the line:stop_yield marking requires vehicles to stop
                        completely before entering the intersection.
Step 6  u_turn          stop_first: stop_first because the line:stop_yield marking requires vehicles to stop
                        completely before entering the intersection.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings indicating a waiting
                          area or two-way left-turn lane.
Step 7  Reflect         The actions are consistent, as the stop-and-yield line governs all movements, and the
                        solid center lines prohibit lane changes.
Advice                  You must come to a complete stop before the double solid yellow line to ensure safety
                        before proceeding straight, turning left, turning right, or making a U-turn. Lane
                        changes are prohibited by the solid yellow lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 7597, out 1001, 20.36 s

bdd100k_val__c59500f0-130d7415 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with traffic moving in the same direction. Ahead, there is a
                        continuation of the road, not an intersection or ramp end visible in the immediate
                        view. (lanes 3, mine 2, full)
Step 2  Left            There is a solid yellow line separating my lane from the adjacent lane to the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway to my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): Double solid yellow lines are visible in the distance,
                        separating opposing traffic flows.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        left boundary is solid yellow, which fits the role of a lane_line separating traffic
                        in the same direction if it were a center line, but since it's a lane_line, the color
                        suggests a separation between opposing flows if it were a center line, which
                        contradicts the lane_line role for same-direction traffic. The right boundary is solid
                        white, fitting the edge_line role. | markings: The double solid yellow lines observed
                        in the distance are interpreted as a line:stop_yield, which is a marking across the
                        lane, but the description of the line itself (double solid yellow) matches CN-6.12.1-2
                        for entrance/exit lines, not the stop-and-yield line (CN-6.5.1.1-2) which is white.
                        The observed double solid yellow lines are likely a center line marking, not a marking
                        within my lane. | unseen: No attributes were reported that were not actually seen. |
                        result: corrected
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_yield: Vehicles shall stop completely before entering the intersection and
                        may proceed only after making sure it is safe. [[CN-6.5.1.1-2]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid yellow lane_line, and
                        CN-6.2.1 mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (correct): allowed: The right boundary is a solid white edge_line, and no rule
                        prohibits changing right across this line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in my lane that restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no right-turn arrow is visible.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane, and no U-turn arrow is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules, noting that the
                        interpretation of the distant double solid yellow lines as a stop-and-yield line is
                        based on a partial observation and is not governing the immediate actions.
Advice                  You may change right, go straight, or proceed, but changing left is prohibited by the
                        solid yellow lane line. Since there are no specific markings for turning, you should
                        proceed with caution.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 7597, out 1217, 20.54 s

bdd100k_val__c5b2506d-07e406a6 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides, and there appears to
                        be an intersection ahead. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles
                        (lane lines on both sides). | roles: The color and pattern of both boundaries (solid
                        white lines) fit the role of a lane_line. | markings: The white arrow pointing
                        straight ahead in my lane is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            arrow:straight: Guide arrows indicate the direction of travel for vehicles, and this
                        arrow indicates straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white lane_line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white lane_line and [CN-6.2.1] prohibits crossing on the solid-line side.
Step 6  go_straight     allowed (contested, correct): allowed, because the lane marking shows a white arrow
                        pointing straight ahead, and [CN-5.13.1] indicates this direction of travel.
Step 6  turn_left       prohibited: prohibited, because there is no marking allowing a left turn and the lane
                        is not designated for it.
Step 6  turn_right      prohibited: prohibited, because there is no marking allowing a right turn and the lane
                        is not designated for it.
Step 6  u_turn          prohibited: prohibited, because there is no marking allowing a U-turn and the lane is
                        not designated for it.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You must remain in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines. No specific stopping or waiting area is marked
                        for your intended movements.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 984, 23.83 s

bdd100k_val__c74ee988-8f4b380d | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road approaching an intersection. My car is in the rightmost lane
                        visible near the bottom of the photo. (lanes 3, mine 3, full)
Step 2  Left            There is a yellow solid line separating my lane from the adjacent lane on the left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on the right side.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line marking the end of the lane.
Step 4  Cross-check     position: The lane count (3) and ego lane index (3) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is an edge line. | roles: The
                        yellow solid line on the left fits the role of a lane_line separating traffic in the
                        same direction, and the white solid line on the right fits the role of an edge_line. |
                        markings: The stop line is consistent with the lane boundaries and the general road
                        layout. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a yellow solid line, and
                        [CN-6.2.1] mandates that vehicles on the solid-line side may not cross.
Step 6  change_right    allowed (contested, label prohibited): allowed: There is no marking governing this
                        action, and the right boundary is an edge line.
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
Advice                  You may proceed straight or turn right from your lane. If you intend to turn left, you
                        must change lanes to the left, but be aware that the lane line on your left is solid,
                        prohibiting crossing. You must stop before the solid white line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 882, 22.38 s

bdd100k_val__c7c042ec-4986a853 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road at night, and there is an intersection ahead. (lanes 3, mine
                        2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the lane division ahead.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles
                        (both are lane_lines). | roles: The color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: The stop line marking is
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a dashed line, and [CN-4.2.2-a]
                        permits crossing when it is safe.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed line, and [CN-4.2.2-a]
                        permits crossing when it is safe.
Step 6  go_straight     allowed (correct): allowed: Nothing restricts carrying on straight along my lane, and
                        the boundaries do not govern it.
Step 6  turn_left       not_applicable (WRONG, label not_determined): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable (WRONG, label not_determined): not_applicable: There is no arrow or
                        prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes left or right as long as it is safe, and you may proceed straight
                        through the intersection. You must stop before the white line at the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['arrow:straight_right']), actions False, unsafe [],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 951, 16.59 s

bdd100k_val__c96ffe59-1cf2df11 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and there is a road ahead leading
                        into what appears to be an intersection or a continuation of the road. (lanes 2, mine
                        1, full)
Step 2  Left            There is a white broken line separating my lane from the adjacent lane to the left.
                        white dashed, curb yes, lane_line, evidence full
Step 2  Right           There is a solid white line marking the edge of the roadway on my right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line segment is visible in the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is an edge_line. | roles: The
                        white dashed line on the left fits the role of a crossable lane_line, and the solid
                        white line on the right fits the role of an edge_line. | markings: The stop line is
                        visible in the lane and is consistent with the lane markings. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a broken line, and [CN-5.2.1-2]
                        permits the crossable lane line to be crossed.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: The right boundary is a solid line, but no
                        rule prohibits crossing it, and [CN-4.2.2-a] implies that a solid line prohibits
                        crossing unless in an emergency.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited-movement
                        markings in the lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane of two lanes. You may change left or right, and you may
                        proceed straight. You must stop before the visible stop line if you intend to stop for
                        any reason.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'change_left allowed across a curb']
Tokens                  in 7597, out 1067, 17.43 s

bdd100k_val__ca15f699-e51c14c0 | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road at night, and there is a stretch of road ahead leading
                        towards what appears to be an intersection or a continuation of the road. (lanes 3,
                        mine 2, full)
Step 2  Left            There is a white broken line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the right edge of my lane.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (lane_line on both sides). | roles: The white dashed lines fit the role of lane_line
                        separating traffic in the same direction. | markings: The partial observation of a
                        line marking the right edge is consistent with the boundaries. | unseen: No attributes
                        were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     allowed (correct): allowed: The left boundary is a white dashed line, and [CN-4.2.2-a]
                        permits crossing a broken line.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and
                        [CN-4.2.2-a] permits crossing a broken line.
Step 6  go_straight     allowed (contested, correct): allowed: There are no arrows or prohibited markings in
                        my lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane, and no left-turn waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no left-turn waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted as the lane lines are
                        broken. You may proceed straight, but you should be aware of the stop line ahead,
                        which indicates where you should stop if required to yield or wait.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7597, out 1046, 14.12 s

bdd100k_val__fe194677-e2d2ac8c | lane | Test C | gemma4:e4b | from cache
------------------------------------------------------------------------
Step 1  Scene           This appears to be a multi-lane road leading towards a large building complex, likely
                        an intersection or a major roadway area. My car is in one of the lanes near the bottom
                        of the photo. (lanes 3, mine 2, full)
Step 2  Left            There is a solid white line separating my lane from the lane to the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line separating my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No specific lane markings (arrows, text, areas) are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (3) and my lane position (2) agree with the boundary roles (a
                        lane line on both sides indicates I am in a lane between others). | roles: The solid
                        white lines fit the role of a lane_line separating traffic in the same direction. |
                        markings: The lack of visible markings is consistent with the boundaries defining the
                        lane. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so its allowance or
                        prohibition cannot be determined based on the provided rules. [null]
Step 6  change_left     prohibited (contested, label not_determined): Prohibited by the left_boundary because
                        the solid white lane line prohibits crossing onto the adjacent lane [CN-6.2.1].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the right_boundary because the
                        solid white lane line prohibits crossing onto the adjacent lane [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings restricting
                        movement straight ahead in my lane, and the boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no left-turn waiting area is visible.
Step 6  turn_right      not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no right-turn guidance is present.
Step 6  u_turn          not_applicable: Not applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no U-turn guidance is present.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed while a rule prohibits it, and all decisions are based on visible features.
Advice                  You should remain in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines on both sides. No specific stopping or turning
                        guidance is visible in your lane.
Score                   lane False, boundaries {'left': None, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 7597, out 1044, 22.62 s
```
