# Reasoning of lane run 20261117_145105_laneC_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, there appears
                        to be an intersection or a point where traffic flow changes, indicated by the road
                        markings. (lanes 2, mine 1, full)
Step 2  Left            The left boundary is marked by a white dashed line, and beyond it, there is a curb.
                        white dashed, curb yes, lane_line, evidence full
Step 2  Right           The right boundary is marked by a white dashed line, and beyond it, there is no
                        visible curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): White dashed lines marking the lane boundaries.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is one of two lanes in my direction. | roles: The white dashed lines fit the role
                        of lane_line, as they separate my lane from adjacent lanes in the same direction of
                        travel. | markings: The stop line marking is consistent with the lane boundaries, as
                        it is located within the lane. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a white dashed line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  change_right    allowed (WRONG, label prohibited): Allowed, as the right boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in my
                        lane, and boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You may change lanes after signaling, and
                        you may proceed straight ahead. You should be aware of the stop line ahead, which
                        suggests you may need to stop for traffic control.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['symbol:bike']), actions False, unsafe ['change_right'], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_left allowed
                        across a curb']
Tokens                  in 5799, out 1087, 6.28 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road leading towards an intersection ahead. My car is in the lane
                        closest to the center of the visible lanes. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane boundary ahead.
Step 4  Cross-check     position: The lane count (3) and ego_lane_index (2) agree with the boundary roles
                        (both are lane_lines). | roles: The color (white) and pattern (dashed) of both
                        boundaries fit the role of a lane_line. | markings: The stop line marking is
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a dashed
                        lane_line and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (contested, label prohibited): Allowed, as the right boundary is a dashed
                        lane_line and [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and lane changes are permitted after signaling. You may
                        proceed straight ahead, but you must stop before the visible stop line if a traffic
                        signal is red or amber.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 5799, out 1025, 6.46 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into a built-up area, and there is no immediate intersection or ramp
                        visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead.; arrow:straight (full):
                        A white arrow pointing straight ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The color (white) and pattern
                        (solid) of both boundaries fit the role of a lane_line. | markings: The arrows in my
                        lane (both pointing straight) agree with the boundaries (solid lines restrict lane
                        changes, but the arrows dictate movement). | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: While driving on a multi-lane road, where direction arrows pointing to
                        the left are marked on the road, the driver shall use that lane while taking a left
                        turn. [[IN-8(1)(c)]]
Step 5  Rule            arrow:straight: While driving on a multi-lane road, where direction arrows pointing to
                        the right are marked on the road, the driver shall remain in that lane while taking
                        right turn. [[IN-8(2)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited, because the left boundary is a solid
                        white lane_line and [IN-6(1)] requires driving within the lane and changing lanes only
                        after signaling/marking.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white lane_line and [IN-6(1)] requires driving within the lane and changing lanes only
                        after signaling/marking.
Step 6  go_straight     allowed (correct): allowed, because the lane marking shows an arrow pointing straight
                        ahead, and no rule prohibits going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable, because there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines. No specific stopping or turning maneuvers are
                        indicated by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 1163, 7.26 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road with buildings on the left and houses on the right, and it appears to
                        be leading towards a junction or a stretch where traffic flow might change. There are
                        two lanes visible in my direction near the bottom of the photo. (lanes 2, mine 1,
                        full)
Step 2  Left            There is no painted line visible on the left boundary; the lane abuts a
                        sidewalk/building area.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           The right boundary is marked by a broken yellow line.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (full): A single solid yellow line runs down the center of the road,
                        separating the two lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two. | roles: The right boundary is yellow and dashed,
                        which fits the role of a lane line separating traffic in the same direction. |
                        markings: The central solid yellow line acts as a center line, which is consistent
                        with the lane configuration. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: No specific rule passage governs the edge of the roadway abutting the
                        sidewalk. [null]
Step 5  Rule            right_boundary: When a road is divided by a longitudinal yellow or white solid line,
                        the driver, proceeding in the same direction and trying to overtake another vehicle
                        ahead, shall not cross the said yellow or white solid line. [[IN-6(4)]]
Step 5  Rule            line:stop_yield: Where a “Give Way” sign is displayed on the road, supplemented by a
                        single or double broken transverse “Give Way” road marking, the driver shall slowdown,
                        give way to traffic on the road he is approaching, and proceed cautiously. [[IN-7(3)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is an edge line, and
                        no marking prohibits a lane change.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a yellow dashed
                        lane line, and while the rule [IN-6(7)] permits crossing a broken line to overtake,
                        the general rule [IN-6(1)] requires changing lanes only after signaling or road
                        marking, and the presence of the central solid line suggests caution.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable: There are no arrows or prohibited-movement markings in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which is the edge lane. You may proceed straight or
                        change left, but changing right is prohibited by the lane marking. Be aware that the
                        central line suggests you must yield to traffic approaching from the opposite
                        direction.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb', 'change_right prohibited across a
                        broken lane line', 'go_straight allowed without the stop that the STOP or 停 marking in
                        my lane requires']
Tokens                  in 5799, out 1091, 6.99 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road, and ahead there is a junction/intersection where the
                        road continues and other traffic is present. (lanes 2, mine 1, full)
Step 2  Left            The left boundary is defined by a curb and the edge of the sidewalk/building.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           The right boundary is marked by a white dashed line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the separation between lanes.;
                        line:stop_line (partial): A white dashed line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line (curb), and the right boundary is a lane_line (dashed
                        line separating it from another lane). | roles: The right boundary's white dashed line
                        fits the role of a lane_line separating my lane from another lane of my direction. |
                        markings: The stop lines are consistent with the boundaries; they are transverse lines
                        across the lane. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The edge of the roadway defined by the curb does not impose specific
                        driving restrictions based on the provided rules. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: When a traffic control signal shows a red light, the driver shall stop
                        before crossing the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 5  Rule            line:stop_line: If the stop line is not marked or not visible, the vehicle shall stop
                        before the pedestrian crossing. [[IN-12(1)(b)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is an edge_line
                        and no solid line prohibits a lane change, and the rule [IN-6(1)] requires signaling
                        for lane changes.
Step 6  change_right    allowed (contested, label prohibited): Allowed, as the right boundary is a dashed
                        lane_line, and the rule [IN-6(1)] requires signaling for lane changes.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited markings
                        in the lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; no action is allowed
                        against a prohibition, and all decisions are based on visible features.
Advice                  You are in the left lane, which is the edge lane. You may change lanes left or right,
                        but you must signal before doing so. You may proceed straight ahead, but you must stop
                        before the visible stop line if a traffic signal is red or if you are approaching a
                        pedestrian crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        unlisted, contradictions ['change_left allowed across a curb']
Tokens                  in 5799, out 1208, 8.03 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is an intersection where the road
                        appears to widen or change direction slightly. (lanes 2, mine 1, full)
Step 2  Left            There is a curb and a painted white line separating my lane from the adjacent lane on
                        the left.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           There is a painted white line separating my lane from the adjacent lane on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A single solid white line runs down the center of my lane,
                        separating it from the lane to the right.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line (implying a lane to the left, which is not visible but
                        consistent with the count), and the right boundary is a lane line (implying another
                        lane to the right). | roles: The white solid line on the left is consistent with a
                        lane_line, and the white solid line on the right is consistent with a lane_line. |
                        markings: The single solid white line observed is interpreted as a stop line, which is
                        consistent with the lane markings. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a lane_line
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a lane_line and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane of two lanes; you may change lanes after signaling. You may
                        proceed straight ahead, but be aware of the stop line ahead, which suggests you may
                        need to stop for traffic or pedestrians.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_left allowed
                        across a curb']
Tokens                  in 5799, out 1103, 7.3 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a continuation
                        of the road, not an intersection or a ramp. (lanes 2, mine 1, full)
Step 2  Left            The left boundary is marked by a solid white line, and beyond it there is a verge with
                        trees and a fence.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           The right boundary is marked by a broken white line, and beyond it there is a sidewalk
                        and buildings.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the left edge of the lane.;
                        line:stop_line (partial): A dashed white line separating my lane from the adjacent
                        lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes. | roles: The white solid line on the left fits
                        the role of an edge_line, and the white dashed line on the right fits the role of a
                        lane_line. | markings: The markings observed are lines, and they are consistent with
                        the boundaries, although the specific interpretation of 'stop_line' here is based on
                        the visual appearance of a line near the foreground, not a clear stop line ahead. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is an edge_line
                        and [IN-6(1)] permits driving within the lane, and no marking prohibits it.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a lane_line and [IN-6(1)] permits
                        driving within the lane, provided a signal is given.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited markings
                        in the lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         Consistent, as all actions are decided based on the absence of restrictive markings or
                        boundaries, or are correctly marked as not applicable.
Advice                  You are in the leftmost lane of two. You may change left or right, and you may proceed
                        straight. Since there are no specific turn arrows or waiting areas visible, you should
                        proceed cautiously.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5799, out 1198, 7.58 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban area, and ahead there is a
                        junction/intersection. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits the roles of lane_line. | markings: The visible marking is a dashed
                        line near the end of the lane, which is consistent with the lane boundaries. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: When a red light is displayed, the driver shall stop the vehicle
                        before the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a lane_line and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a lane_line and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in the
                        lane, and boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is suitable for going straight. Lane changes are
                        permitted provided you signal correctly. Be prepared to stop at the visible stop line
                        ahead of the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 1025, 6.24 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with a pedestrian crossing ahead, and the road continues
                        forward. My car is in the lane closest to the left boundary. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the roadway, followed by a curb and a
                        grassy area.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the separation between lanes.;
                        line:stop_line (partial): A white dashed line marking the separation between lanes.;
                        line:stop_line (partial): A white dashed line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost. | roles: The left boundary is solid white and has a curb,
                        fitting the role of an edge_line. The right boundary is dashed white, fitting the role
                        of a lane_line. | markings: The lane markings (dashed lines) are consistent with the
                        right boundary role (lane_line). The stop lines are visible ahead. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The right boundary is a dashed
                        lane_line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is a dashed
                        lane_line, and [IN-6(1)] permits lane changes after signaling.
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
Advice                  You are in the leftmost lane, which is permitted to change lanes after signaling. You
                        may proceed straight, but be aware of the pedestrian crossing ahead where you must
                        stop if required by traffic signals or pedestrians.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        unlisted, contradictions ['change_left allowed across a curb']
Tokens                  in 5799, out 1139, 6.47 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there is an intersection where
                        traffic appears to be moving through or approaching a crossing area. (lanes 2, mine 1,
                        full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white dashed line marking the lane boundary ahead.;
                        line:stop_line (full): A white dashed line marking the lane boundary ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        both boundaries are lane lines. | roles: The color (white) and pattern (dashed) of
                        both boundaries fit the role of a lane_line. | markings: The stop lines are consistent
                        with the lane boundaries and do not contradict any other markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 5  Rule            line:stop_line: When, at an intersection or at a place other than an intersection,
                        rapid intermittent flashes of red light are displayed by a traffic control signal, the
                        vehicle facing the signal shall stop before the stop line preceding the pedestrian
                        crossing. [[IN-12(1)(e)(i)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the left_boundary because the rule
                        [IN-6(1)] permits lane changes after signaling/marking.
Step 6  change_right    allowed (correct): Allowed by the right_boundary because the rule [IN-6(1)] permits
                        lane changes after signaling/marking.
Step 6  go_straight     allowed (contested, correct): Allowed because there are no markings in the lane
                        prohibiting straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: Not_applicable because there are no arrows or waiting areas governing
                        this action.
Step 6  turn_right      not_applicable: Not_applicable because there are no arrows or waiting areas governing
                        this action.
Step 6  u_turn          not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings governing this action.
Step 6  enter_waiting_areanot_applicable: Not_applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane and can proceed straight or change lanes left or right,
                        provided you signal appropriately. You must stop before the visible stop line if a red
                        or flashing red light is displayed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 1118, 7.97 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining the left side and trees lining
                        the right side. Ahead, the road continues into a built-up area, and there is an arrow
                        indicating straight movement. (lanes 2, mine 1, full)
Step 2  Left            The left boundary is marked by a solid white line.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           The right boundary is marked by a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.;
                        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is solid white,
                        fitting the role of an edge_line. The right boundary is dashed white, fitting the role
                        of a lane_line. | markings: The two straight arrows in my lane agree with the
                        boundaries and each other. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: No specific rule passage governs the straight arrow in this context,
                        but it indicates the permitted movement.
Step 5  Rule            arrow:straight: No specific rule passage governs the straight arrow in this context,
                        but it indicates the permitted movement.
Step 6  change_left     prohibited (contested, label allowed): prohibited: The left boundary is an edge_line,
                        and [IN-6(1)] mandates driving within the lane and changing lanes only after
                        signaling/marking.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed lane_line, and [IN-6(1)]
                        allows lane changes after signaling/marking, and [IN-6(7)] permits overtaking across a
                        broken line.
Step 6  go_straight     allowed (correct): allowed: The lane marking shows a straight arrow, and no rule
                        prohibits going straight.
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable: There are no markings
                        indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There are no markings
                        indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings for a waiting area or two-way
                          left-turn lane.
Step 7  Reflect         consistent
Advice                  You should stay in your lane to go straight, but you are permitted to change right
                        after signaling. No specific markings govern turning left or right, and there is no
                        designated waiting area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions []
Tokens                  in 5799, out 907, 8.79 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in a built-up area, and ahead there is a junction/intersection where
                        the road continues straight and curves to the right. My car is in the lane closest to
                        the left side of the road. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the lane.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the edge of the lane ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost. | roles: The left boundary is a solid white edge_line, and the
                        right boundary is a dashed white lane_line, which fits the roles. | markings: The stop
                        line is visible ahead, which is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (correct): The right boundary is a dashed white lane_line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  change_right    allowed (correct): The right boundary is a dashed white lane_line, and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Nothing restricts carrying on straight along my lane,
                        and the boundaries do not govern it.
Step 6  turn_left       not_applicable: No marking governs this action, and the boundaries do not govern it.
Step 6  turn_right      not_applicable: No marking governs this action, and the boundaries do not govern it.
Step 6  u_turn          not_applicable: No marking governs this action, and the boundaries do not govern it.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which is the edge of the road. You may change lanes left
                        or right after signaling. You may proceed straight ahead, but you must stop before the
                        visible stop line if a traffic signal requires it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['change_left allowed across a curb']
Tokens                  in 5799, out 1006, 6.33 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban or suburban setting, and ahead there is a
                        junction or intersection where the road continues. (lanes 2, mine 1, full)
Step 2  Left            There is a curb and a painted white line separating my lane from the area to the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a painted white line separating my lane from the adjacent lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead in the left lane.;
                        arrow:straight (full): A white arrow pointing straight ahead in the right lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line (suggesting it's the leftmost lane or adjacent to the
                        edge), and the right boundary is a lane_line (suggesting another lane to the right). |
                        roles: The white solid line on the left fits the role of an edge_line, and the white
                        dashed line on the right fits the role of a lane_line. | markings: The arrows in the
                        lane show straight movement, which is consistent with the lane markings. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: While driving on a multi-lane road, where direction arrows pointing to
                        the left are marked on the road, the driver shall use that lane while taking a left
                        turn. [[IN-8(1)(c)]]
Step 5  Rule            arrow:straight: While driving on a multi-lane road, where direction arrows pointing to
                        the right are marked on the road, the driver shall remain in that lane while taking
                        right turn. [[IN-8(2)(c)]]
Step 6  change_left     allowed (contested, label prohibited): The right boundary is a dashed lane_line, and
                        [IN-6(1)] requires changing lanes only after giving a proper signal or road marking or
                        signage.
Step 6  change_right    allowed (correct): The right boundary is a dashed lane_line, and [IN-6(1)] requires
                        changing lanes only after giving a proper signal or road marking or signage.
Step 6  go_straight     allowed (correct): The arrow in my lane shows straight ahead, and nothing restricts
                        carrying on straight along my lane.
Step 6  turn_left       not_applicable (WRONG, label allowed): There is no arrow or prohibited-movement
                        marking in my lane governing this action, and no waiting area or two-way left-turn
                        lane is visible.
Step 6  turn_right      not_applicable (WRONG, label prohibited): There is no arrow or prohibited-movement
                        marking in my lane governing this action, and no waiting area or two-way left-turn
                        lane is visible.
Step 6  u_turn          not_applicable (WRONG, label prohibited): There is no arrow or prohibited-movement
                        marking in my lane governing this action, and no waiting area or two-way left-turn
                        lane is visible.
Step 6  enter_waiting_areanot_applicable: There is no left-turn waiting area or two-way left-turn lane visible
                          ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is marked for going straight. You may change lanes
                        after signaling, but be aware that the right lane is also marked for going straight.
                        Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions ['change_left allowed across a curb']
Tokens                  in 5799, out 1202, 7.23 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a paved urban road with buildings lining both sides. Ahead, the road continues
                        into a built-up area, and there is a pedestrian crossing visible further down. (lanes
                        2, mine 1, full)
Step 2  Left            There is a curb and a solid white line marking the edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the separation between lanes.;
                        line:stop_line (partial): A white dashed line marking the separation between lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two. | roles: The left boundary is a solid white
                        edge_line, and the right boundary is a dashed white lane_line, which fits the roles
                        assigned. | markings: The lane markings (stop lines) are consistent with the
                        boundaries and do not contradict the lane structure. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 5  Rule            line:stop_line: If the stop line is not marked or, if marked is not visible, the
                        vehicle shall stop before the pedestrian crossing. [[IN-12(1)(b)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the right boundary is a dashed
                        lane_line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    prohibited (contested, correct): Prohibited, as the left boundary is a solid
                        edge_line, and [IN-6(1)] requires driving within the lane.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibited markings
                        in the lane, and nothing restricts carrying on straight along the lane.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited markings in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited markings in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited markings in the
                        lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane and can proceed straight or change left after signaling.
                        You must stop before the visible stop lines if approaching an intersection or
                        pedestrian crossing where traffic signals or signs require it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        unlisted, contradictions ['change_left allowed across a curb', 'change_right
                        prohibited across a broken lane line']
Tokens                  in 5799, out 1186, 6.94 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane city street with buildings lining both sides. Ahead, the road
                        continues into the distance, suggesting a continuation of the current road segment
                        rather than an immediate intersection or ramp. (lanes 2, mine 1, full)
Step 2  Left            There is a metal railing separating the roadway from the sidewalk/building area.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is a white dashed line marking the boundary of the lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is a physical edge
                        (railing/curb) and has no painted line, fitting the edge_line role. The right boundary
                        is a white dashed line, fitting the lane_line role. | markings: The white arrow
                        pointing straight ahead is located within the lane and is consistent with the lane
                        boundaries. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The physical edge does not have a specific traffic rule governing it
                        based on the provided passages. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The provided rules do not specify a mandatory action for a straight-
                        ahead arrow in this context. [null]
Step 6  change_left     prohibited (contested, correct): prohibited: The right boundary is a white dashed
                        line, and [IN-6(1)] mandates driving within the lane and changing lanes only after
                        signaling/marking, which implies the dashed line allows it, but the general rule is
                        restrictive without further context.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [IN-6(1)]
                        allows lane changes after signaling/marking, and the dashed line permits crossing.
Step 6  go_straight     allowed (correct): allowed: The lane marking shows a white arrow pointing straight
                        ahead, and no rule prohibits going straight.
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable: There is no arrow or waiting
                        area indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: There is no arrow or
                        prohibited-movement marking indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; the right boundary's
                        dashed line permits lane changes, and the straight arrow permits going straight.
Advice                  You are in the leftmost lane, which is marked for straight travel. You may change
                        right after signaling, and you are permitted to go straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions []
Tokens                  in 5799, out 1055, 7.71 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a city street with buildings lining both sides. Ahead, there is a pedestrian
                        crossing and what appears to be an intersection or junction. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the edge of the lane.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): A white dashed line marking the pedestrian crossing area.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is a solid white
                        edge_line, and the right boundary is a dashed white lane_line, which fits the roles
                        assigned. | markings: The crosswalk marking is consistent with the lane boundaries and
                        does not contradict any other observed markings. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:crosswalk: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the right boundary is a dashed
                        lane_line and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    prohibited (contested, correct): Prohibited, as the left boundary is a solid edge_line
                        and [IN-6(1)] requires lane changes to be signaled.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in my
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane, which is permitted to change right after signaling, but
                        changing left is allowed as the line is broken. You may proceed straight, but be
                        prepared to stop for pedestrians at the marked crossing ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['change_left
                        allowed across a curb', 'change_right prohibited across a broken lane line']
Tokens                  in 5799, out 1067, 6.79 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there is an intersection where
                        the road continues. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the right boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): The text 'BUS LANE' is painted on the left side of my lane.;
                        line:stop_line (partial): A white dashed line is painted across the lane ahead,
                        indicating a lane division or merge point.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes in my direction. | roles: The color (white) and pattern (solid) of both
                        boundaries fit the role of a lane_line. | markings: The text 'BUS LANE' is in my lane,
                        and the dashed line ahead is interpreted as a stop line, which is consistent with the
                        lane markings. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:bus: A vehicle of that class (bus) shall drive in that lane only. [[IN-6(2)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white lane_line and [IN-6(1)] requires driving within the lane and changing lanes only
                        after signaling/marking.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a solid white lane_line, but
                        [IN-6(1)] requires changing lanes only after signaling/marking.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows in my lane and
                        nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable, because there is no arrow or waiting area marking in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane.
Step 6  u_turn          not_applicable: not_applicable, because there is no arrow or prohibited-movement
                        marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane marking in my lane.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you must adhere to the rules for this special lane. You may
                        proceed straight or change right, but any lane change must be signaled. You must stop
                        before the marked line ahead if traffic signals require it.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line', 'text:bus'], missed []), actions True, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 1156, 7.19 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a
                        junction/intersection. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A solid white line marking the lane boundary is visible
                        ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The left boundary is solid
                        white, and the right boundary is dashed white, which fits the roles of lane_line. |
                        markings: The stop line is visible ahead, which is consistent with the lane markings.
                        | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the right boundary's role as a
                        lane_line, as no rule prohibits changing left.
Step 6  change_right    allowed (correct): Allowed by the left boundary's role as a lane_line, as no rule
                        prohibits changing right.
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
Advice                  You are in the leftmost lane of two. You may change lanes left or right, and you may
                        proceed straight ahead. You must stop before the visible stop line if a red light is
                        displayed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['text:speed_limit']), actions True, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 1039, 7.0 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where traffic flow is visible. (lanes 3, mine 2, full)
Step 2  Left            There is a white dashed line separating my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles
                        (left boundary is a lane line, right boundary is a lane line). | roles: The white
                        dashed lines fit the role of lane_line. | markings: The arrow pointing straight ahead
                        is consistent with the lane markings. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: No specific rule passage was found that governs an arrow pointing
                        straight ahead in this context.
Step 6  change_left     allowed (correct): The left boundary is a white dashed line, and [IN-6(1)] requires
                        changing lanes only after signaling or road marking, which is not explicitly shown to
                        prohibit it.
Step 6  change_right    allowed (correct): The right boundary is a white dashed line, and [IN-6(1)] requires
                        changing lanes only after signaling or road marking, which is not explicitly shown to
                        prohibit it.
Step 6  go_straight     allowed (correct): The lane marking shows an arrow pointing straight ahead, and no
                        rule prohibits going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No arrow or marking in the lane permits or
                        prohibits turning left.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No arrow or marking in the lane permits or
                        prohibits turning right.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No arrow or marking in the lane permits or
                        prohibits a U-turn.
Step 6  enter_waiting_areanot_applicable: No marking for a waiting area was observed in my lane.
Step 7  Reflect         The decisions are consistent with the observations and the cited rules.
Advice                  You are in the middle lane, which is marked for going straight ahead. Lane changes are
                        permitted as the boundaries are broken, but you must signal before changing lanes. You
                        should proceed straight ahead through the intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5799, out 787, 5.56 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test C | gemma4:e4b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a road in an urban area, and ahead there is an intersection. My car is in the
                        lane closest to the center of the road. (lanes 2, mine 1, full)
Step 2  Left            The left boundary is marked by a white dashed line, and beyond it is a curb.
                        white dashed, curb yes, lane_line, evidence full
Step 2  Right           The right boundary is marked by a white dashed line, and beyond it is the edge of the
                        road.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): White arrow pointing straight ahead; arrow:straight (full):
                        White arrow pointing straight ahead; arrow:straight (full): White arrow pointing
                        straight ahead
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is a lane_line, and the right boundary is a lane_line. | roles: The
                        white dashed lines fit the role of lane_line. | markings: The straight arrows in my
                        lane agree with the boundaries, as they indicate movement within the lane structure. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: While driving on a multi-lane road, where direction arrows pointing to
                        the left are marked on the road, the driver shall use that lane while taking a left
                        turn. [[IN-8(1)(c)]]
Step 5  Rule            arrow:straight: While driving on a multi-lane road, where direction arrows pointing to
                        the right are marked on the road, the driver shall remain in that lane while taking
                        right turn. [[IN-8(2)(c)]]
Step 5  Rule            arrow:straight: No specific rule passage was found that governs the action of
                        proceeding straight based on a straight arrow.
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the left_boundary, as per [IN-6(1)],
                        which requires changing lanes only after giving a proper signal or road marking or
                        signage.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the right_boundary, as per [IN-6(1)],
                        which requires changing lanes only after giving a proper signal or road marking or
                        signage.
Step 6  go_straight     allowed (correct): Allowed because the lane markings include an arrow pointing
                        straight ahead, and no rule prohibits going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        marking indicating a permitted left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        marking indicating a permitted right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        marking indicating a permitted U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You should stay in your current lane to proceed straight through the intersection.
                        Lane changes are prohibited by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_right prohibited
                        across a broken lane line']
Tokens                  in 5799, out 1177, 7.05 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings on both sides, and it appears to
                        continue straight ahead into the distance. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, words, symbols, areas, or lines are visible
                        across my lane from the bottom to the end.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating two
                        lanes in my direction. | roles: The left boundary is a solid white lane line, and the
                        right boundary is a dashed white lane line, which fits the roles of lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, but the general rules for
                        lane boundaries apply. [null]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a lane line
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a lane line and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in my lane prohibiting
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
Advice                  You are in the left lane of a two-lane road; you may change lanes after signaling. You
                        may proceed straight ahead, but turning movements are not explicitly permitted by
                        markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 990, 6.36 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there is an intersection where
                        traffic appears to be moving through or approaching it. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No specific lane markings like arrows, text, or areas are
                        visible within my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two lanes visible. | roles: The left boundary is a solid
                        white lane line, and the right boundary is a dashed white lane line, which fits the
                        roles of lane_line. | markings: The absence of specific markings in my lane is
                        consistent with the boundaries defining the lane. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so the default permissive
                        rule applies.
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a lane_line
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a lane_line and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in my
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       allowed: Allowed, as there are no arrows or prohibitions in my lane, and no waiting
                        area or two-way left-turn lane is present.
Step 6  turn_right      allowed: Allowed, as there are no arrows or prohibitions in my lane, and no waiting
                        area or two-way left-turn lane is present.
Step 6  u_turn          allowed: Allowed, as there are no arrows or prohibitions in my lane, and no solid line
                        prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You may change lanes after signaling, and all movements (straight, left, right,
                        U-turn) appear permitted based on the lane markings. Since there are no specific
                        markings governing turns, you should proceed cautiously towards the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'turn_right allowed
                        although a prohibited-movement marking forbids it']
Tokens                  in 5799, out 1030, 6.98 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with traffic moving away from the camera. Ahead, there
                        is an intersection marked with pedestrian crossings and road markings. (lanes 2, mine
                        1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): White dashed lines forming a crosshatch pattern ahead of the
                        intersection.; area:grid (full): White dashed lines forming a crosshatch pattern ahead
                        of the intersection.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating two
                        lanes in my direction. | roles: The left boundary is solid white, and the right
                        boundary is dashed white, which fits the roles of lane_line. | markings: The area:grid
                        markings are consistent with the lane boundaries and do not contradict the lane
                        structure. | unseen: No attributes were reported that were not actually seen. |
                        result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            area:grid: A vehicle shall not be stopped- on a yellow box marked on road.
                        [[IN-22.(1)viii]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a lane_line
                        and [IN-6(1)] permits lane changes after signaling/marking.
Step 6  change_right    allowed (contested, label prohibited): Allowed, as the right boundary is a lane_line
                        and [IN-6(1)] permits lane changes after signaling/marking.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in my
                        lane, and boundaries do not restrict going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane, and
                        no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         Consistent, as all actions are decided based on the observed markings and rules, and
                        no prohibited action is allowed.
Advice                  You are in the left lane of a two-lane road. You may change lanes after signaling, and
                        you are permitted to go straight ahead. Be aware that you must not stop within the
                        marked grid area ahead of the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 1101, 7.07 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there is an intersection where
                        the road continues. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead.; arrow:straight (full):
                        A white arrow pointing straight ahead, located in the adjacent lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits the roles of lane_line. | markings: The arrow in my lane shows
                        straight ahead, which is consistent with the lane markings and boundaries. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: On a road having a single broken line along with a solid line, the
                        driver of the vehicle driving on the left of broken line may cross the broken line in
                        order to o vertake, but shall return to his lane after completing the manoeuvre,
                        observing the safety precautions specified in regulation 12. [[IN-6(7)]]
Step 5  Rule            arrow:straight: While driving on a multi-lane road, where direction arrows pointing to
                        the left are marked on the road, the driver shall use that lane while taking a left
                        turn. [[IN-8(1)(c)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the right boundary's role as a
                        lane_line, as the rule [IN-6(7)] permits crossing a broken line for overtaking, and
                        the left boundary is a solid line which does not prohibit lane change.
Step 6  change_right    allowed (contested, correct): Allowed by the right boundary's role as a lane_line, as
                        the rule [IN-6(7)] permits crossing a broken line for overtaking, and the left
                        boundary is a solid line which does not prohibit lane change.
Step 6  go_straight     allowed (correct): Allowed because the arrow in my lane shows straight ahead, and no
                        rule prohibits going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a left turn.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a right turn.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable because there is no arrow or
                        prohibited-movement marking in my lane indicating a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable because there is no marked waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane, which is marked for straight travel. You may change lanes
                        left or right to overtake, but you must signal and return to your lane after
                        overtaking. You may proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left', 'change_left
                        allowed across a curb']
Tokens                  in 5799, out 1125, 5.96 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is an intersection
                        where the road continues and other lanes are visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, words, symbols, areas, or lines are visible
                        across my lane in the visible stretch.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is not the leftmost or rightmost in a way that contradicts the count. | roles:
                        The left boundary is a solid white lane line, and the right boundary is a dashed white
                        lane line, which fits the roles of lane_line. | markings: The absence of markings in
                        my lane is consistent with the boundaries. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so the default permissive
                        rule applies. [null]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a lane_line and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a lane_line and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in my
                        lane, and boundaries do not prohibit going straight.
Step 6  turn_left       allowed: Allowed, as there are no arrows or prohibitions in my lane, and no waiting
                        area or two-way left-turn lane is present.
Step 6  turn_right      allowed: Allowed, as there are no arrows or prohibitions in my lane, and no waiting
                        area or two-way left-turn lane is present.
Step 6  u_turn          allowed: Allowed, as there are no arrows or prohibitions in my lane, and no solid line
                        prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: Not applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may change lanes after signaling, and all movements (straight, left, right,
                        U-turn) appear permitted by the lane markings. Use the lane appropriate for your
                        intended turn or travel direction at the intersection ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'turn_right allowed
                        although a prohibited-movement marking forbids it']
Tokens                  in 5799, out 1026, 7.2 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and the road continues ahead into
                        the distance with buildings on both sides. (lanes 2, mine 1, full)
Step 2  Left            There is a white dashed line separating my lane from the adjacent lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           There is a white dashed line separating my lane from the adjacent lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the lane boundary ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles, as
                        both boundaries are lane lines. | roles: The color (white) and pattern (dashed) of
                        both boundaries fit the role of a lane_line. | markings: The stop line marking is
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (correct): Allowed, as the left boundary is a dashed lane_line and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a dashed lane_line and [IN-6(1)]
                        permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in the
                        lane, and the boundaries do not prohibit going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in the lane,
                        and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane and can change lanes after signaling. You may proceed
                        straight, but be aware of the stop line ahead, which suggests an intersection or
                        crossing is approaching.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 1022, 6.96 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and it continues ahead into the
                        distance without an immediate intersection visible. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left edge of the lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           There is a broken white line separating my lane from the adjacent lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No specific arrows, words, symbols, areas, or lines are visible
                        within my lane.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is an edge line, and the right boundary is a lane line, indicating my
                        lane is the leftmost of the two lanes. | roles: The left boundary is a solid white
                        edge line, and the right boundary is a dashed white lane line, which fits their roles.
                        | markings: There are no markings in my lane to contradict the boundaries. | unseen:
                        No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so the default rules
                        apply. [null]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is an edge line, and
                        [IN-6(1)] permits driving within the lane, which allows for a lane change if signaled.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed lane line, and [IN-6(7)]
                        permits crossing a broken line to overtake, which allows for a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       allowed: allowed: No arrow or prohibited-movement marking in my lane restricts turning
                        left.
Step 6  turn_right      allowed: allowed: No arrow or prohibited-movement marking in my lane restricts turning
                        right.
Step 6  u_turn          allowed: allowed: No arrow or prohibited-movement marking in my lane restricts
                        U-turning.
Step 6  enter_waiting_areanot_applicable: not_applicable: No left-turn waiting area or two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may change left or right, and all movements
                        (straight, left, right, U-turn) are permitted as no lane-use markings restrict you.
                        Use your signal when changing lanes.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['turn_right allowed although a prohibited-movement marking forbids
                        it']
Tokens                  in 5799, out 826, 7.91 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in a built-up area, and ahead there is a continuation of the
                        road with traffic moving in both directions. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a solid white line marking the boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Text 'BUS LANE' painted on the road surface.; area:channelizing
                        (full): A painted area indicating a bus lane.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating my
                        lane is not the leftmost or rightmost in a way that contradicts the count. | roles:
                        The color and pattern of both boundaries (white solid lines) fit the role of a
                        lane_line. | markings: The text 'BUS LANE' and the associated area marking are
                        consistent with the lane boundaries and do not contradict the lane structure. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:bus: Where any lane is marked specially for a class of vehicles, a vehicle of
                        that class shall drive in that lane only. [[IN-6(2)]]
Step 5  Rule            area:channelizing: Where a lane has been marked for a specified class of vehicles or
                        for a special purpose, no other vehicle of any other class shall be driven in that
                        lane. [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white lane line and [IN-6(1)] requires driving within the lane and changing lanes only
                        after signaling/marking.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited, because the right boundary is a solid
                        white lane line and [IN-6(1)] requires driving within the lane and changing lanes only
                        after signaling/marking.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no markings in my lane
                        prohibiting straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no marked waiting area or two-way
                          left-turn lane visible ahead of my lane.
Step 7  Reflect         consistent
Advice                  You must remain in this lane as it is designated as a bus lane, and lane changes are
                        prohibited by the solid white lines. You are permitted to proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing', 'text:bus'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 1142, 7.13 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way road with buildings lining both sides. Ahead, the road continues
                        into a built-up area, and there is no immediate intersection visible. (lanes 2, mine
                        1, full)
Step 2  Left            The left boundary is marked by a white dashed line, and beyond it is a sidewalk/curb
                        area.
                        white dashed, curb yes, lane_line, evidence full
Step 2  Right           The right boundary is marked by a white dashed line, and beyond it is the edge of the
                        road/sidewalk.
                        white dashed, curb yes, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the separation between the two
                        lanes.; line:stop_line (partial): A white dashed line marking the separation between
                        the two lanes.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes of travel in this direction. | roles: The white dashed lines fit the role of
                        lane_line, as they separate lanes of traffic moving in the same direction. | markings:
                        The markings observed are dashed lines, which are consistent with the boundaries being
                        dashed lines. The markings are not contradictory with the boundaries. | unseen: No
                        attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 5  Rule            line:stop_line: If the stop line is not marked or, if marked is not visible, the
                        vehicle shall stop before the pedestrian crossing. [[IN-12(1)(b)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (contested, label prohibited): Allowed, as the right boundary is a white
                        dashed line, and [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings in the lane
                        prohibiting straight movement, and the boundaries do not prohibit it.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane governing this action.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane governing this action.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibited-movement markings
                        in the lane governing this action.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and rules; no action is allowed
                        against a prohibition, and all decisions are based on visible features.
Advice                  You are in the left lane, which is permitted to change lanes after signaling. You may
                        proceed straight ahead, but be aware of the stop lines ahead, which suggest caution or
                        potential stopping points.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_left allowed
                        across a curb', 'change_right allowed across a curb']
Tokens                  in 5799, out 1190, 9.8 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane city street with traffic moving in both directions. Ahead, there
                        is a junction or intersection where the road continues. (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:right (full): A white arrow pointing right is painted in the adjacent lane to my
                        right.
Step 4  Cross-check     position: The lane count (2) and my lane position (1) agree with the boundary roles:
                        the left boundary is a lane line, and the right boundary is a lane line. | roles: The
                        left boundary is a solid white lane line, and the right boundary is a dashed white
                        lane line, which fits the roles of lane_line. | markings: The arrow in my lane points
                        straight ahead, which is consistent with the lane markings. The arrow in the adjacent
                        lane points right, which is also consistent. | unseen: No attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: On a road having a single broken line along with a solid line, the
                        driver of the vehicle driving on the left of broken line may cross the broken line in
                        order to o vertake, but shall return to his lane after completing the manoeuvre,
                        observing the safety precautions specified in regulation 12. [[IN-6(7)]]
Step 5  Rule            arrow:straight: While driving on a multi-lane road, where direction arrows pointing to
                        the left are marked on the road, the driver shall use that lane while taking a left
                        turn. [[IN-8(1)(c)]]
Step 5  Rule            arrow:right: While driving on a multi-lane road, where direction arrows pointing to
                        the right are marked on the road, the driver shall remain in that lane while taking
                        right turn. [[IN-8(2)(c)]]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the left_boundary, as it is a solid
                        lane line, and [IN-6(1)] requires driving within the lane and changing lanes only
                        after signaling or marking.
Step 6  change_right    allowed (contested, label prohibited): Allowed by the right_boundary, as it is a
                        dashed lane line, and [IN-6(7)] permits crossing the broken line to overtake.
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed by the arrow:straight, as the arrow permits
                        going straight ahead.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not_applicable, as there is no arrow or
                        marking in my lane permitting a left turn.
Step 6  turn_right      not_applicable (WRONG, label allowed): Not_applicable, as there is no arrow or marking
                        in my lane permitting a right turn.
Step 6  u_turn          not_applicable: Not_applicable, as there is no arrow or marking in my lane permitting
                        a U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change right into the adjacent lane. Changing left is
                        prohibited by the solid white line. No specific stopping or waiting areas are marked
                        in your lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['go_straight'], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left', 'turn_right
                        not_applicable although an arrow shows it']
Tokens                  in 5799, out 1180, 7.66 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance with traffic moving in both directions. (lanes 2, mine 1,
                        full)
Step 2  Left            The left boundary is marked by a solid white line, and beyond it there is a curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           The right boundary is marked by a broken white line, and beyond it there is no visible
                        curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): The text 'BUS LANE' is painted on the road surface near the bottom of
                        the photo.; line:stop_line (partial): A white dashed line extends across the lane
                        ahead.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is an edge_line, and the right boundary is a lane_line, indicating my
                        lane is the leftmost of the two lanes in my direction. | roles: The solid white line
                        on the left fits the role of an edge_line, and the dashed white line on the right fits
                        the role of a lane_line. | markings: The text 'BUS LANE' is present in my lane, and
                        the dashed line ahead is interpreted as a stop line, which is consistent with the lane
                        markings. | unseen: No attributes were reported that were not actually seen. | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:bus: A vehicle of that class shall drive in that lane only. [[IN-6(2)]]
Step 5  Rule            line:stop_line: A motor vehicle facing the red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the right boundary's role as a
                        lane_line, as no rule prohibits changing left, and the left boundary allows driving
                        within the lane [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the right boundary's role as a
                        lane_line, as the driver must drive within the lane and change lanes only after giving
                        a proper signal or road marking or signage [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): Allowed because there are no arrows or prohibited-
                        movement markings in my lane, and the boundaries do not prohibit going straight
                        [IN-6(1)].
Step 6  turn_left       not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: Not_applicable because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: Not_applicable because there is no left-turn waiting area or two-way
                          left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you must only drive in this lane. You may change left after
                        signaling, but changing right is restricted. You may proceed straight ahead, but you
                        must stop before the marked line ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line', 'text:bus'], missed []), actions False, unsafe [], citation
                        unlisted, contradictions ['change_left allowed across a curb', 'change_right
                        prohibited across a broken lane line']
Tokens                  in 5799, out 1243, 7.77 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 2, mine 1, full)
Step 2  Left            The left boundary is marked by a white dashed line, and beyond it, there is a curb.
                        white dashed, curb yes, lane_line, evidence full
Step 2  Right           The right boundary is marked by a white dashed line, and beyond it, the road
                        continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A white dashed line marking the right edge of the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes in the direction of travel. | roles: The white dashed lines fit the role of
                        lane_line, as they separate lanes of traffic moving in the same direction. | markings:
                        The line:stop_line is visible near the end of the visible lane stretch, which is
                        consistent with the lane boundaries. | unseen: No attributes were reported that were
                        not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            line:stop_line: A motor vehicle facing a red light of a traffic control signal at an
                        intersection or at a place other than an intersection, shall stop the vehicle before
                        the stop line preceding the pedestrian crossing. [[IN-12(1)(a)]]
Step 6  change_left     allowed (contested, label prohibited): allowed: The left boundary is a white dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): allowed: The right boundary is a white dashed line, and [IN-6(1)]
                        permits lane changes after signaling.
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
Advice                  You are in the left lane, and lane changes are permitted after signaling. You may
                        proceed straight, but be aware of the stop line ahead, which suggests an upcoming
                        intersection or crossing where stopping may be required by traffic signals or
                        pedestrian crossings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_left allowed
                        across a curb']
Tokens                  in 5799, out 1050, 7.39 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): The text 'BUS LANE' is painted on the road in my lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line. | roles: The left
                        boundary is a solid white lane line, and the right boundary is a dashed white lane
                        line, which fits the roles of lane_line. | markings: The 'BUS LANE' text is in my lane
                        and does not contradict the boundaries or other markings. | unseen: No attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:bus: Where any lane is marked specially for a class of vehicles, a vehicle of
                        that class shall drive in that lane only. [[IN-6(2)]]
Step 6  change_left     prohibited (contested, correct): prohibited, because the left boundary is a solid
                        white lane line and [IN-6(1)] mandates driving within the lane and changing lanes only
                        after signaling/marking.
Step 6  change_right    allowed (correct): allowed, because the right boundary is a dashed white lane line and
                        [IN-6(1)] allows lane changes after signaling/marking.
Step 6  go_straight     allowed (contested, correct): allowed, because there are no arrows or prohibited
                        markings in my lane, and nothing restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  turn_right      not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  u_turn          not_applicable: not_applicable, because there are no arrows or prohibited-movement
                        markings in my lane, and no waiting area or two-way left-turn lane is visible.
Step 6  enter_waiting_areanot_applicable: not_applicable, because there is no left-turn waiting area or two-
                          way left-turn lane visible.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, so you must adhere to the rules for this special lane. You may
                        change right after signaling, but changing left is prohibited by the solid line. You
                        may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 1066, 6.6 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 2, mine 1, full)
Step 2  Left            There is a solid white line marking the left boundary of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           There is a broken white line marking the right boundary of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (full): No lane-use arrows, words, symbols, areas, or lines are visible
                        across my lane from the bottom to the end.
Step 4  Cross-check     position: The lane count (2) and ego lane index (1) agree with the boundary roles: the
                        left boundary is a lane line, and the right boundary is a lane line, indicating two
                        lanes in my direction. | roles: The left boundary is a solid white lane line, and the
                        right boundary is a dashed white lane line, which fits the roles of lane_line. |
                        markings: The absence of markings in my lane is consistent with the boundaries. |
                        unseen: No attributes were reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            no_turn:right: No specific rule passage covers this element, so the default permissive
                        rule applies. [null]
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a lane_line
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a lane_line and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no arrows or prohibitions in my
                        lane, and boundaries do not restrict going straight.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or waiting areas governing this
                        action.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane
                        governing this action.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or prohibitions in my lane
                        governing this action.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         All actions are decided based on the observed features and the applicable rules, and
                        no prohibited action is allowed.
Advice                  You are in the left lane of a two-lane road; you may change lanes after signaling. You
                        may proceed straight ahead, but turning left, right, or making a U-turn is not
                        governed by any markings in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 5799, out 1024, 7.7 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road in an urban environment, and ahead there is a
                        junction/intersection where traffic flow is visible. (lanes 3, mine 2, full)
Step 2  Left            The left boundary is marked by a solid white line, and beyond it is a curb.
                        white solid, curb yes, lane_line, evidence full
Step 2  Right           The right boundary is marked by a solid white line, and beyond it is the edge of the
                        road/sidewalk.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): A circular speed limit sign showing '20' is painted on the
                        road.; text:speed_limit (full): A circular speed limit sign showing '20' is painted on
                        the road.; text:speed_limit (full): A circular speed limit sign showing '30' is
                        painted on the road.
Step 4  Cross-check     position: The lane count (3) and ego lane index (2) agree with the boundary roles: the
                        left boundary is a lane line (indicating a lane to the left), and the right boundary
                        is a lane line (indicating a lane to the right). | roles: The solid white lines on
                        both sides fit the role of lane_line, as they separate my lane from adjacent lanes. |
                        markings: The speed limit markings are consistent with the boundaries and do not
                        contradict any lane use rules. | unseen: No attributes were reported that were not
                        actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            text:speed_limit: No specific rule passage dictates the action based on the presence
                        of a speed limit marking. [null]
Step 6  change_left     allowed (contested, correct): Allowed, as the left boundary is a lane_line and
                        [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (correct): Allowed, as the right boundary is a lane_line and [IN-6(1)] permits
                        lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as there are no markings prohibiting straight
                        movement in my lane, and boundaries do not govern this action.
Step 6  turn_left       not_applicable: Not_applicable, as there are no arrows or markings indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: Not_applicable, as there are no arrows or markings indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: Not_applicable, as there are no arrows or markings indicating a
                        permitted U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed against a prohibition, and all decisions are based on visible features.
Advice                  You are in the middle lane, and you may change left or right after signaling. You may
                        proceed straight, but be mindful of the posted speed limits of 20 and 30.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions ['change_left
                        allowed across a curb']
Tokens                  in 5799, out 1126, 8.81 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road with buildings lining both sides. Ahead, the road
                        continues into the distance, and there is no immediate intersection or ramp visible.
                        (lanes 2, mine 1, full)
Step 2  Left            The left boundary is marked by a white dashed line, and beyond it, there is a curb.
                        white dashed, curb yes, lane_line, evidence full
Step 2  Right           The right boundary is marked by a white dashed line, and beyond it, the road
                        continues.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Two white dashed arrows pointing straight ahead are visible in
                        the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        left boundary is a lane_line, and the right boundary is a lane_line, indicating two
                        lanes in the direction of travel. | roles: The white dashed lines fit the role of
                        lane_line, as they separate lanes of traffic moving in the same direction. | markings:
                        The arrow showing straight ahead is consistent with the lane markings and boundaries;
                        it does not conflict with the lane lines. | unseen: No attributes were reported that
                        were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            arrow:straight: No specific rule passage was found that dictates the action based on a
                        straight-ahead arrow in this context.
Step 6  change_left     allowed (contested, label prohibited): Allowed, as the left boundary is a dashed line,
                        and [IN-6(1)] permits lane changes after signaling.
Step 6  change_right    allowed (contested, label prohibited): Allowed, as the right boundary is a dashed
                        line, and [IN-6(1)] permits lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): Allowed, as the lane marking shows an arrow pointing
                        straight ahead, and no rule prohibits this movement.
Step 6  turn_left       not_applicable: Not_applicable, as there is no arrow or marking indicating a permitted
                        left turn.
Step 6  turn_right      not_applicable: Not_applicable, as there is no arrow or marking indicating a permitted
                        right turn.
Step 6  u_turn          not_applicable: Not_applicable, as there is no arrow or marking indicating a permitted
                        U-turn.
Step 6  enter_waiting_areanot_applicable: Not_applicable, as there is no marked waiting area or two-way left-
                          turn lane visible.
Step 7  Reflect         The actions are consistent with the observations and the cited rules; no action is
                        allowed against a prohibition, and all decisions are based on visible features.
Advice                  You are in the left lane, which is permitted to change lanes after signaling. You may
                        proceed straight ahead, but turning left, right, or performing a U-turn is not
                        indicated as permitted by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['leftmost lane, but a lane line on the left', 'change_left allowed
                        across a curb']
Tokens                  in 5799, out 1036, 9.7 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test C | gemma4:e4b
------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with trees lining the sides, and the road continues ahead
                        into the distance without an immediate intersection visible. (lanes 2, mine 1, full)
Step 2  Left            There is no visible painted line or curb on the left side of my lane in the visible
                        stretch.
                        none none, curb no, edge_line, evidence insufficient
Step 2  Right           The right boundary is marked by a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:right (insufficient): No lane markings are visible across my lane from the
                        bottom to the end of the lane.
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (1) agree with the boundary roles: the
                        right boundary is a lane_line, indicating my lane is not the rightmost lane, and the
                        left boundary has no line, suggesting it is the leftmost lane or the edge. | roles:
                        The right boundary is white and solid, fitting the role of a lane_line separating my
                        lane from another lane. | markings: There are no markings in my lane to contradict the
                        boundaries. | unseen: The lack of a clear left boundary line makes the role of the
                        left boundary uncertain. | result: consistent
Step 5  Rule            left_boundary: No specific rule passage covers the lack of a painted line or curb on
                        the left side of my lane. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane, and change lanes only after
                        giving a proper signal or road marking or signage. [[IN-6(1)]]
Step 5  Rule            no_turn:right: No specific rule passage covers a general 'no turn right' marking in
                        this context. [null]
Step 6  change_left     allowed (correct): allowed: The left boundary has no governing marking, and there is
                        no rule prohibiting a lane change into the adjacent lane.
Step 6  change_right    prohibited (contested, correct): prohibited: The right boundary is a solid white
                        lane_line, and [IN-6(1)] mandates driving within the lane and changing lanes only
                        after signaling/marking.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or waiting area in my lane to govern
                        a left turn.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or waiting area in my lane to govern
                        a right turn.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in my
                        lane to govern a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked waiting area or two-way left-turn
                          lane visible.
Step 7  Reflect         consistent
Advice                  You are in the left lane and can proceed straight or change left, but changing right
                        is prohibited by the solid white line. Since there are no specific turn arrows, you
                        must follow general road rules for turning.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['change_left decided although that side cannot be seen']
Tokens                  in 5799, out 1018, 7.39 s
```
