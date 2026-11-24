# Reasoning of lane run 20261117_123051_laneB_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. Ahead is a junction with a red bus and other
                        vehicles. My car is in the leftmost lane of its direction. (lanes 2, mine 1, full)
Step 2  Left            A solid red line is painted along the edge of the road next to the pavement.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line divides my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The red solid
                        line fits the role of an edge line (Red Route), and the broken white line fits the
                        role of a lane divider. | markings: There are no markings in my lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Stopping to park, load/unload or to board and alight is prohibited on
                        the red line. [[UK-HC_MARKINGS-p2-8]]
Step 5  Rule            right_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a red edge line and a curb;
                        crossing it would mean leaving the carriageway, which is prohibited.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white lane line,
                        which allows lane changes if safe [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): No marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may proceed straight or change to the right lane if
                        safe. Do not stop or park on the red line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe ['change_right'],
                        citation accepted, contradictions []
Tokens                  in 13891, out 814, 9.25 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road in the UK. The road ahead continues straight with
                        some roadworks indicated by cones and signs in the distance. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a cycle lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway next to a pavement.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a special lane
                        line on the left and an edge line on the right. | roles: The solid white lines fit the
                        roles of a cycle lane boundary and a carriageway edge line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles must not be driven in the cycle lane during its hours of
                        operation. [[UK-TSRGD-12(2)]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white line boundary of the
                        cycle lane [UK-TSRGD-12(2)].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line and the
                        presence of a curb [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings in the lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the cycle lane on the left or
                        cross the edge line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 13891, out 820, 11.1 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. Ahead is a junction with traffic signals and
                        pedestrians. My car is in the middle lane of a three-lane road. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position at index 2 agree with having lane lines
                        on both my left and right. | roles: The white dashed pattern for both boundaries is
                        consistent with the role of lane dividers. | markings: The straight-ahead arrow is
                        consistent with a through-lane bounded by lane lines. | unseen: No attributes were
                        reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: I should keep between these short, broken white lines. [[UK-Rule131]]
Step 5  Rule            right_boundary: I should keep between these short, broken white lines. [[UK-Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [UK-Rule131].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [UK-Rule131].
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, you must change
                        lanes as the current lane is for straight-ahead traffic only.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line', 'symbol:bike']), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 904, 12.81 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a single-carriageway urban road with shops and houses. The road continues
                        straight ahead with no immediate intersection or ramp visible. (lanes 1, mine 1, full)
Step 2  Left            I see a double yellow line on the left edge of the road, separating the carriageway
                        from the pavement.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           I see a broken white line on the right, separating my lane from the opposing traffic
                        lane.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the boundaries: a
                        center line on the right and an edge line on the left. | roles: The double yellow edge
                        line and broken white center line fit their respective roles for a single-carriageway
                        road. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [[UK-
                        HC_MARKINGS-p2-2]]
Step 5  Rule            right_boundary: A broken white center line may be crossed to overtake if the road is
                        clear. [[UK-Rule127]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the left boundary (edge line/curb) and
                        the double yellow lines which restrict waiting/stopping on the verge.
Step 6  change_right    allowed (correct): Allowed by the broken white center line and [UK-Rule127], provided
                        it is safe to overtake.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings in my lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: Not applicable as there is no intersection or turn marking in view.
Step 6  turn_right      not_applicable: Not applicable as there is no intersection or turn marking in view.
Step 6  u_turn          not_applicable: Not applicable as there is no intersection or turn marking in view.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to overtake if
                        it is safe to do so, but do not stop or park on the left due to the double yellow
                        lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 830, 12.27 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead leads to a T-junction or intersection
                        where the road ends. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from the pavement on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from the pavement on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): White zig-zag lines are painted on both sides of the lane
                        approaching the intersection.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the edge lines on both sides. |
                        roles: The solid white lines on both sides correctly serve as edge lines for a single-
                        lane road. | markings: The zig-zag lines are consistent with an approach to a
                        pedestrian crossing or junction. | unseen: No attributes were reported without visual
                        evidence. | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            symbol:other: You must not park or overtake within the zig-zag area before the
                        crossing. [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to ensure that
                        drivers and pedestrians can see each other clearly. As a driver, you must not park
                        your vehicle anywh"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white edge
                        line and there is a curb.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and there is a curb.
Step 6  go_straight     not_applicable (contested, label allowed): not_applicable: the road ends at the
                        intersection ahead.
Step 6  turn_left       allowed: allowed: no marking in my lane prohibits turning left at the end of the road.
Step 6  turn_right      allowed: allowed: no marking in my lane prohibits turning right at the end of the
                        road.
Step 6  u_turn          allowed: allowed: no marking in my lane prohibits a U-turn, provided it is safe.
Step 6  enter_waiting_areanot_applicable: not_applicable: there is no marked waiting area.
Step 7  Reflect         consistent
Advice                  Stay in your lane and do not cross the solid white edge lines. Do not park or overtake
                        in the zig-zag area. Prepare to turn left or right at the end of the road.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        accepted, contradictions ['turn_left, turn_right, u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 13891, out 913, 14.49 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road in the UK. The road continues straight ahead with
                        other vehicles in front. (lanes 1, mine 1, full)
Step 2  Left            Two solid red lines are painted along the left edge of the road, separating the
                        carriageway from the pavement.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from a parking area or side lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the left boundary being an
                        edge line and the right boundary being a lane line (though the right side appears to
                        be a parking/service area). | roles: The double red lines on the left are edge lines
                        indicating restrictions; the broken white line on the right is a lane divider. |
                        markings: There are no markings in my lane. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: Double red lines mean no stopping at any time. [[UK-HC_MARKINGS-p2-9]]
Step 5  Rule            right_boundary: Broken white lane dividers are used to divide lanes and you should
                        keep between them. [[UK-Rule131]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a double red line; [UK-
                        HC_MARKINGS-p2-9] prohibits stopping, and as an edge line with a curb, changing left
                        is prohibited.
Step 6  change_right    allowed (correct): The right boundary is a broken white line; [UK-Rule131] allows
                        keeping between them, and broken lines generally permit crossing if safe.
Step 6  go_straight     allowed (contested, correct): No marking governs this action; it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action; not applicable at this stretch of
                        road.
Step 6  turn_right      not_applicable: No marking governs this action; not applicable at this stretch of
                        road.
Step 6  u_turn          not_applicable: No marking governs this action; not applicable at this stretch of
                        road.
Step 6  enter_waiting_areanot_applicable: No waiting area is present; not applicable.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop or pull over to the left due to
                        the double red lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 13891, out 695, 13.15 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, proceeding straight ahead on a clear
                        stretch of road. (lanes 3, mine 1, full)
Step 2  Left            A solid white line separates the lane from a blue-painted cycle lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A short, broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 agree with the left boundary being
                        a special lane line (cycle lane) and the right boundary being a lane line. | roles:
                        The solid white line for a cycle lane and dashed white line for lane division fit
                        their roles. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles must not be driven in the cycle lane during its hours of
                        operation. [[UK-TSRGD-12(2)]]
Step 5  Rule            right_boundary: Drivers should keep between these short, broken white lane dividers.
                        [[UK-Rule131]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white line boundary of the
                        cycle lane [UK-TSRGD-12(2)].
Step 6  change_right    allowed (correct): Allowed by the broken white lane divider [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right if needed. Do not enter the cycle lane on the
                        left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 13891, out 789, 11.75 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with shops on the right and a sidewalk on the left. The road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            I see a solid white line separating the lane from a cycle lane and sidewalk.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           I see a white dashed line separating my lane from a parking area where cars are
                        stopped.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries, as both sides are
                        edge lines. | roles: The white solid line on the left and white dashed line on the
                        right are consistent with edge lines in an urban setting. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: I must not drive in the cycle lane during its hours of operation. [[UK-
                        TSRGD-12(2)]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the solid white line and [UK-
                        TSRGD-12(2)] as it is a cycle lane.
Step 6  change_right    allowed (correct): Allowed by the dashed white line and [UK-TSRGD-S11P4-item11] as it
                        is an edge line to a parking area.
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane to proceed straight. Do not enter the cycle lane on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 13891, out 804, 13.93 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, approaching a pedestrian crossing.
                        (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a paved area/cycle lane on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from the opposite direction of traffic.
                        white solid, curb no, center_line, evidence full
Step 3  Markings        symbol:other (full): White zig-zag lines are painted along the sides of the lane
                        approaching the crossing.; line:crosswalk (full): A zebra crossing with wide white
                        stripes is across the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the presence of an edge line on
                        the left and a center line on the right. | roles: The solid white lines fit the roles
                        of edge and center lines in this urban context. | markings: The zig-zag lines and
                        zebra crossing are consistent with a pedestrian crossing area. | unseen: No attributes
                        were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            right_boundary: This is the division between opposing flows of traffic. [UK-
                        TSRGD-S11P4-item6] "Diagram 1008 Division between opposing flows of traffic on a
                        carriageway other than at places where the marking at item 2 is used (Longitudinal
                        marking)"
Step 5  Rule            symbol:other: You must not park or overtake within the zig-zag area before the
                        crossing. [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to ensure that
                        drivers and pedestrians can see each other clearly. As a driver, you must not park
                        your vehicle anywh"
Step 5  Rule            line:crosswalk: This is a pedestrian crossing where drivers must yield to pedestrians.
                        [UK-HC_MARKINGS-p1] "Stop line at signals or police control"
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white edge line (UK-
                        TSRGD-S11P4-item11).
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white center line (UK-
                        Rule129).
Step 6  go_straight     allowed (contested, correct): Allowed as no marking prohibits continuing straight
                        through the crossing after yielding.
Step 6  turn_left       not_applicable: Not applicable as there is no intersection or turn arrow.
Step 6  turn_right      not_applicable: Not applicable as there is no intersection or turn arrow.
Step 6  u_turn          not_applicable: Not applicable as there is no intersection or turn arrow.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and do not overtake or park in the zig-zag area. Be prepared to stop
                        for pedestrians at the zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 987, 16.28 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead is clear with no immediate
                        intersection or ramp visible. (lanes 1, mine 1, full)
Step 2  Left            A broken white line separates my lane from a cycle lane on the left.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway next to a row of buildings.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A white circle with the number 20 inside it is painted on the
                        road.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a special lane
                        line on the left and an edge line on the right. | roles: The white dashed line on the
                        left fits the role of a cycle lane boundary, and the solid white line on the right
                        fits the role of a carriageway edge. | markings: The speed limit marking is consistent
                        with an urban road environment. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: I should not drive or park in the cycle lane unless it is unavoidable.
                        [UK-Rule140-2] "Do not drive or park in a cycle lane marked by a broken white line
                        unless it is unavoidable."
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            text:speed_limit: I should follow the road markings, which indicate a speed limit of
                        20 mph. [UK-Rule134] "You should follow the signs and road markings and get into the
                        lane as directed."
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line for a
                        cycle lane; UK-Rule140-2 allows crossing it if unavoidable, but generally discourages
                        it.
Step 6  change_right    allowed (correct): The right boundary is a solid white edge line; no specific rule
                        prohibits crossing it to leave the road, but it marks the end of the carriageway.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight; it is allowed by
                        default.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and observe the 20 mph speed limit. Avoid entering the cycle lane on
                        the left unless necessary.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 13891, out 940, 16.29 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road continues straight ahead, and my car is in a
                        single lane. (lanes 1, mine 1, full)
Step 2  Left            A solid red line is painted along the left edge of the road next to the pavement.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the opposing traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and right
                        center line. | roles: The red solid line fits an edge line (Red Route), and the broken
                        white line fits a center line. | markings: The straight arrow is consistent with a
                        single lane proceeding forward. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: Stopping to park, load/unload or to board and alight is prohibited on
                        red lines. [[UK-HC_MARKINGS-p2-8]]
Step 5  Rule            right_boundary: I may cross this broken white center line to overtake or turn off if
                        the road is clear. [[UK-Rule127]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     prohibited (contested, label allowed): Prohibited by the solid red edge line and curb
                        [UK-HC_MARKINGS-p2-8].
Step 6  change_right    allowed (correct): Allowed by the broken white center line [UK-Rule127].
Step 6  go_straight     allowed (correct): Allowed by the straight arrow [UK-TSRGD-Part6,item20].
Step 6  turn_left       prohibited (WRONG, label allowed): Prohibited by the straight arrow [UK-TSRGD-
                        Part6,item20].
Step 6  turn_right      prohibited (correct): Prohibited by the straight arrow [UK-TSRGD-Part6,item20].
Step 6  u_turn          prohibited (correct): Prohibited by the straight arrow [UK-TSRGD-Part6,item20].
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight ahead as indicated by the arrow. Do not stop or
                        park on the left due to the red route markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 13891, out 911, 31.02 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a two-way urban road with shops on the left and residential buildings on the
                        right. The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a parking area and the curb.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the opposing traffic lane.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a center line on
                        the right and an edge line on the left. | roles: The white dashed line fits the role
                        of a center line, and the white solid line fits the role of an edge line. | markings:
                        There are no markings in the lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            right_boundary: This marks the centre of the road; I may cross it to overtake or turn
                        off if the road is clear. [UK-Rule127] "A broken white line. This marks the centre of
                        the road. When this line lengthens and the gaps shorten, it means that there is a
                        hazard ahead. Do not cross it un"
Step 6  change_left     allowed (correct): The left boundary is a solid white edge line; no rule prohibits
                        crossing it to enter the parking area if safe, but it is not a lane change.
Step 6  change_right    allowed (correct): The right boundary is a broken white center line, which allows
                        crossing to overtake or turn if the road is clear per UK-Rule127.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action, so it is not_applicable.
Step 6  turn_right      not_applicable: No marking governs this action, so it is not_applicable.
Step 6  u_turn          not_applicable: No marking governs this action, so it is not_applicable.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You can proceed straight in your lane. You may cross the center line to the right to
                        overtake if it is safe to do so.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 13891, out 816, 12.13 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with traffic signals
                        ahead. (lanes 2, mine 1, full)
Step 2  Left            A double red line is painted along the left edge of the road, separating the
                        carriageway from the pavement.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           A short, broken white line divides my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The double red
                        line on the left is an edge line for the carriageway; the broken white line on the
                        right is a lane divider. | markings: The straight-ahead arrow is consistent with a
                        through-lane. | unseen: No attributes were reported without being visible. | result:
                        consistent
Step 5  Rule            left_boundary: Double red lines mean no stopping at any time. [[UK-HC_MARKINGS-p2-9]]
Step 5  Rule            right_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the double red edge line and curb [UK-
                        HC_MARKINGS-p2-9].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [UK-Rule131].
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  turn_left       prohibited (WRONG, label allowed): Prohibited by the straight-ahead arrow [UK-TSRGD-
                        Part6,item20].
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. Do not stop or park on the left due to the double
                        red lines. If you need to turn, you must change to the right lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 13891, out 936, 13.28 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead is a single carriageway with a slight
                        bend, and my car is positioned in the only lane for its direction. (lanes 1, mine 1,
                        full)
Step 2  Left            A solid white line separates the lane from a paved area/sidewalk on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the opposing traffic lane.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left boundary being an edge
                        line and the right boundary being a center line. | roles: The solid white edge line
                        and dashed white center line are consistent with their roles in a single-lane-per-
                        direction urban road. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            right_boundary: This marks the centre of the road; I may cross it to overtake or turn
                        off if the road is clear. [UK-Rule127] "A broken white line. This marks the centre of
                        the road. When this line lengthens and the gaps shorten, it means that there is a
                        hazard ahead. Do not cross it un"
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white edge line and a
                        curb; crossing it is prohibited as it leads off the carriageway.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken white center
                        line, which allows crossing if safe [UK-Rule127].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to proceeding straight.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to the right if
                        it is safe to overtake or turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 13891, out 825, 14.26 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead towards
                        a distant intersection, with buildings on both sides. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates the lane from a cycle lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the boundaries: a
                        special lane line on the left (cycle lane) and a lane line on the right. | roles: The
                        solid white line on the left fits the role of a cycle lane boundary, and the dashed
                        white line on the right fits the role of a lane divider. | markings: The straight-
                        ahead arrow is consistent with the lane's direction and boundaries. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles must not be driven in the cycle lane during its hours of
                        operation. [[UK-TSRGD-12(2)]]
Step 5  Rule            right_boundary: You should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white line boundary and [UK-
                        TSRGD-12(2)] as it is a cycle lane.
Step 6  change_right    allowed (correct): Allowed by the dashed white line boundary and [UK-Rule131].
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead arrow and [UK-TSRGD-Part6,item20].
Step 6  turn_left       prohibited (WRONG, label allowed): Prohibited by the straight-ahead arrow and [UK-
                        TSRGD-Part6,item20].
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead arrow and [UK-TSRGD-
                        Part6,item20].
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead arrow and [UK-TSRGD-
                        Part6,item20].
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right lane if needed. You must proceed straight ahead
                        as indicated by the lane arrow; do not enter the cycle lane on your left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions []
Tokens                  in 13891, out 956, 14.16 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead continues straight, passing a
                        pedestrian crossing. (lanes 1, mine 1, full)
Step 2  Left            I see a solid white line on the left, bordering a sidewalk and buildings.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           I see a solid white line on the right, bordering a sidewalk and buildings.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): I see a zebra crossing with white stripes across the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the edge lines on both sides. |
                        roles: The solid white lines on both sides fit the role of edge lines for a single-
                        lane urban road. | markings: The crosswalk is a standard marking across the lane. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            line:crosswalk: Drivers must not park within zig-zag markings or overtake vehicles
                        stopped at the crossing. [UK-KYTS-zigzag] "The zig-zag markings at crossings are there
                        to ensure that drivers and pedestrians can see each other clearly. As a driver, you
                        must not park your vehicle anywh"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white edge
                        line and there is a curb.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and there is a curb.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs turning left at the end of
                        the lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs turning right at the end
                        of the lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: there is no waiting area in view.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be cautious of pedestrians at the zebra
                        crossing and do not overtake any vehicles stopped there.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 894, 12.51 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead is clear, and my car is in a lane next
                        to a bus lane. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A solid red line marks the edge of the carriageway on the right.
                        other solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        special lane line on the left and an edge line on the right. | roles: The solid white
                        line fits the role of a special lane boundary, and the red line fits the role of a red
                        route edge line. | markings: There are no markings in my lane to contradict. | unseen:
                        No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a designated lane (bus lane). [[UK-TSRGD-
                        Part6,item11]]
Step 5  Rule            right_boundary: The red line indicates that stopping to park, load/unload or to board
                        and alight is prohibited. [[UK-HC_MARKINGS-p2-8]]
Step 6  change_left     prohibited (contested, correct): The solid white line boundary of a bus lane prohibits
                        entering it unless permitted by signs or for specific purposes like loading, but
                        generally, it is a reserved lane.
Step 6  change_right    prohibited (WRONG, label allowed): The red line is an edge line; crossing it would
                        mean leaving the carriageway, which is prohibited.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Do not enter the bus lane to your left
                        or cross the red line to your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 823, 12.44 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road continues straight ahead with a bus stopped
                        in a designated lane to the left. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A grey metal railing and a curb form the right edge of the road.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a special lane
                        line on the left and a curb on the right. | roles: The solid white line fits the role
                        of a special lane boundary, and the curb fits the role of the road edge. | markings:
                        There are no markings in my lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a bus lane or other designated lane. [[UK-
                        TSRGD-Part6,item11]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line marking a bus
                        lane; [UK-Rule141-2] recommends not driving in a bus lane during operation, and [UK-
                        Rule140] prohibits driving in a cycle lane marked by a solid line, but for bus lanes,
                        it is generally restricted.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb and railing, which
                        physically prohibits leaving the lane to the right.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the bus lane to the left or cross
                        the curb to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 818, 11.99 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road continues straight ahead with other vehicles
                        present. (lanes 2, mine 1, full)
Step 2  Left            I see double red lines on the far left edge of the roadway.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           I see a broken white line dividing my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The double red
                        lines on the left fit the role of an edge line (Red Route), and the broken white line
                        on the right fits the role of a lane divider. | markings: The straight-ahead arrow is
                        consistent with the lane's boundaries and the general flow of traffic. | unseen: No
                        attributes were reported without being visible. | result: consistent
Step 5  Rule            left_boundary: Double red lines mean no stopping at any time. [[UK-HC_MARKINGS-p2-9]]
Step 5  Rule            right_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the double red edge lines [UK-
                        HC_MARKINGS-p2-9] and the physical curb.
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [UK-Rule131].
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right lane if needed. You must proceed straight ahead
                        as indicated by the lane arrow; do not stop or park on the left due to the double red
                        lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 944, 13.52 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road continues straight ahead, and my car is in
                        the middle lane of a three-lane road. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position at index 2 agree with having lane lines
                        on both my left and right. | roles: The white dashed patterns are consistent with the
                        role of lane dividers. | markings: The straight-ahead arrow is consistent with a
                        through-lane bounded by lane lines. | unseen: No attributes were reported without
                        being visible. | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: I should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     allowed (correct): Allowed by the broken white line [UK-Rule131], provided it is safe.
Step 6  change_right    allowed (correct): Allowed by the broken white line [UK-Rule131], provided it is safe.
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20],
                        which mandates proceeding ahead.
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20],
                        which mandates proceeding ahead.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20],
                        which mandates proceeding ahead.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right at the next
                        intersection, you must change lanes as the current lane is for straight-through
                        traffic only.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 914, 15.31 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead with no
                        immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            A short, broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway, with a sidewalk and trees beyond
                        it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        lane line on the left and an edge line on the right. | roles: The white dashed line
                        fits the role of a lane divider, and the white solid line fits the role of an edge
                        line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line [UK-
                        Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line [UK-
                        TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may proceed straight or change to
                        the left lane, but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 807, 14.01 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road continues straight ahead, and my car is in a
                        lane that is adjacent to a bus lane on the left. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        special lane line on the left and a center line on the right. | roles: The solid white
                        line for a bus lane boundary and the broken white line for a center line are
                        consistent with UK road markings. | markings: There are no markings in my lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: This is the boundary of a bus lane. [[UK-TSRGD-Part6,item11]]
Step 5  Rule            left_boundary: I should not drive in the bus lane during its period of operation.
                        [[UK-Rule141-2]]
Step 5  Rule            right_boundary: I may cross this broken white center line to overtake if the road is
                        clear. [[UK-Rule127]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white line boundary of the
                        bus lane [UK-Rule141-2].
Step 6  change_right    allowed (correct): Allowed by the broken white center line [UK-Rule127].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight
                        along my lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area in view.
Step 7  Reflect         consistent
Advice                  Stay in your current lane to go straight. Do not enter the bus lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 845, 13.78 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. Ahead is a junction with a traffic signal and a
                        pedestrian crossing. My car is in the leftmost lane of its direction. (lanes 1, mine
                        1, full)
Step 2  Left            I see a solid white line separating the road from a cycle lane and pavement.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           I see a broken white line separating my lane from the opposing traffic flow.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        line:crosswalk (full): I see white zig-zag lines painted across the lane before the
                        crossing.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left boundary being an edge
                        line and the right boundary being a center line. | roles: The solid white left
                        boundary fits the role of an edge line for a cycle lane, and the dashed white right
                        boundary fits the role of a center line. | markings: The zig-zag lines are consistent
                        with the approach to a pedestrian crossing. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: I must not drive in the cycle lane during its hours of operation. [[UK-
                        TSRGD-12(2)]]
Step 5  Rule            right_boundary: I may cross this center line to overtake or turn off if the road is
                        clear. [[UK-Rule127]]
Step 5  Rule            line:crosswalk: I must not park in the zig-zag area and must not overtake vehicles
                        nearest the crossing. [[UK-Rule191]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white line and [UK-
                        TSRGD-12(2)] as it is a cycle lane.
Step 6  change_right    allowed (contested, label prohibited): Allowed by the dashed white line and [UK-
                        Rule127] if safe.
Step 6  go_straight     allowed (contested, correct): Allowed as no marking prohibits it and it is the natural
                        path of the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the cycle lane to the left, and
                        do not overtake any vehicles within the zig-zag markings before the crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 13891, out 932, 15.34 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with shops on the left. The road continues straight ahead
                        towards a junction. (lanes 2, mine 1, full)
Step 2  Left            I see a raised curb and double yellow lines on the left edge of the road.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           I see a broken white line dividing my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The double
                        yellow lines on the edge and the broken white line as a lane divider fit their roles.
                        | markings: The straight-ahead arrow is consistent with the lane's position and
                        boundaries. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [UK-HC_MARKINGS-p2-2]
                        "Double yellow lines mean no waiting at any time, unless there are signs that
                        specifically indicate seasonal restrictions."
Step 5  Rule            right_boundary: I should keep between the short, broken white lane dividers. [UK-
                        Rule131] "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): Prohibited by the left boundary (curb and double
                        yellow lines) as it is the edge of the carriageway.
Step 6  change_right    allowed (contested, correct): Allowed by the right boundary (broken white line)
                        provided it is safe to do so.
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead arrow in my lane.
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead arrow which mandates proceeding
                        ahead only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead arrow which mandates proceeding
                        ahead only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead arrow which mandates proceeding
                        ahead only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight ahead. Do not stop or park on the left due to
                        the double yellow lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 877, 14.78 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway, with a sidewalk and buildings
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the presence of a
                        lane line on the left and an edge line on the right. | roles: The white dashed line
                        fits the role of a lane divider, and the white solid line fits the role of an edge
                        line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [UK-Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and the
                        presence of a curb [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may proceed straight or change to
                        the left lane, but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 807, 14.21 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, proceeding straight ahead towards a
                        distant intersection. (lanes 2, mine 2, full)
Step 2  Left            A short, broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway, with a sidewalk and metal
                        railing beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The broken white line fits the
                        role of a lane divider, and the solid white line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [UK-Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and the
                        presence of a curb/railing [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane if
                        needed; do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 811, 12.89 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway, with a red line and a sidewalk
                        beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The broken white line fits the
                        role of a lane divider, and the solid white line fits the role of a carriageway edge.
                        | markings: There are no markings in my lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line [UK-
                        Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line [UK-
                        TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may proceed straight or change to
                        the left lane, but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 803, 29.27 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead is straight with no immediate
                        intersection or ramp visible. My car is in a single lane of traffic. (lanes 1, mine 1,
                        full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the opposing traffic lane.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a special lane
                        line on the left and a center line on the right. | roles: The solid white line on the
                        left fits the role of a bus lane boundary, and the broken white line on the right fits
                        the role of a center line. | markings: There are no markings in my lane to contradict.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a bus lane. [[UK-TSRGD-Part6,item11]]
Step 5  Rule            left_boundary: I should not drive in the bus lane during its period of operation.
                        [[UK-Rule141-2]]
Step 5  Rule            right_boundary: I may cross this broken white center line to overtake if the road is
                        clear. [[UK-Rule127]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white line boundary of the
                        bus lane [UK-Rule141-2].
Step 6  change_right    allowed (correct): Allowed by the broken white center line [UK-Rule127].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight
                        along my lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or intersection in view.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or intersection in view.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow or intersection in view.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the bus lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 842, 12.54 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road with shops on the right. The road continues straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line marks the edge of the carriageway, with a sidewalk and trees beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway, with a sidewalk and shops beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): White zig-zag lines are painted along the sides of the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the presence of edge lines on
                        both sides. | roles: The solid white lines on both sides correctly serve as edge lines
                        for a single-lane road. | markings: The zig-zag lines are consistent with a pedestrian
                        crossing area, though the crossing itself is further ahead. | unseen: No attributes
                        were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            symbol:other: You must not park or overtake within the zig-zag area. [[UK-KYTS-
                        zigzag]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid edge line
                        and there is a curb.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid edge line
                        and there is a curb.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits continuing straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not park or overtake other vehicles within
                        the zig-zag markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 13891, out 887, 34.82 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead continues straight through a junction
                        with traffic signals. (lanes 2, mine 2, full)
Step 2  Left            A short, broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway, next to a sidewalk with a metal
                        railing.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead.
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the lane line on
                        the left and the edge line on the right. | roles: The white dashed line fits the role
                        of a lane divider, and the white solid line fits the role of an edge line. | markings:
                        The straight-ahead arrow is consistent with the lane's position and boundaries. |
                        unseen: No attributes were reported without being visible. | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [UK-Rule131].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line and the
                        presence of a curb/railing [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed by the straight-ahead arrow [UK-TSRGD-
                        Part6,item20].
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  turn_right      prohibited (WRONG, label allowed): Prohibited by the straight-ahead arrow [UK-TSRGD-
                        Part6,item20].
Step 6  u_turn          prohibited: Prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn, you must change to the left
                        lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation accepted, contradictions []
Tokens                  in 13891, out 929, 14.39 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead is straight with parked cars on the
                        right and a bus lane on the left. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A broken white line separates my lane from a parking area or shoulder on the right.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        special lane line on the left and an edge line on the right. | roles: The solid white
                        line for a bus lane and dashed white line for the edge of the carriageway fit their
                        roles. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a bus lane. [[UK-TSRGD-Part6,item11]]
Step 5  Rule            left_boundary: I should not drive in the bus lane during its period of operation.
                        [[UK-Rule141-2]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white line boundary of the
                        bus lane [UK-Rule141-2].
Step 6  change_right    allowed (correct): Allowed by the broken white edge line [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along my lane.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane to go straight. Do not enter the bus lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 859, 13.75 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with shops on both sides; the road continues straight ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway, with a sidewalk and shops beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane divider, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line [UK-
                        Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and the
                        presence of a curb [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of a two-lane road. You may proceed straight or change
                        to the left lane, but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 802, 13.54 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings and shops on the left. The road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from a bus lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the opposing traffic flow.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        lane line on the left and a center line on the right. | roles: The white dashed
                        patterns fit the roles of lane divider and center line. | markings: There are no
                        markings in my lane to contradict. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: I may cross this center line to overtake or turn off if the road is
                        clear. [[UK-Rule127]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white line [UK-Rule131],
                        though the lane to the left is a bus lane and subject to [UK-Rule141-2].
Step 6  change_right    allowed (correct): Allowed by the broken white line [UK-Rule127] if the road is clear.
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can proceed straight or change lanes if safe. Note that the lane to your left is a
                        bus lane; avoid driving in it during its hours of operation.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 786, 13.99 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings and shops on both sides. The road ahead
                        continues straight, and there is a parking area or side road to the right. (lanes 1,
                        mine 1, full)
Step 2  Left            A solid white line separates my lane from a red-painted lane to the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area and a concrete island to the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a special lane
                        line on the left and an edge line on the right. | roles: The solid white lines fit the
                        roles of a special lane boundary and a roadway edge. | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: This is the boundary of a designated lane (bus or other), and crossing
                        it is governed by the rules of that lane. [[UK-TSRGD-Part6,item11]]
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line marking a
                        special lane; crossing it is prohibited unless permitted by specific rules for that
                        lane (e.g., to load/unload).
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line and a
                        curb, which prohibits leaving the carriageway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the red-painted lane to the left
                        or cross the edge line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13891, out 840, 12.54 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides. The road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A short, broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway, with a sidewalk beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A white circle containing the number 20 is painted in the
                        lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The broken white line fits the
                        role of a lane divider, and the solid white line fits the role of an edge line. |
                        markings: The speed limit marking is a standard informative marking and does not
                        contradict the boundaries. | unseen: No attributes were reported without being
                        visible. | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            text:speed_limit: This indicates a speed limit of 20 mph. [null]
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken white line [UK-
                        Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move left if needed. Observe the 20 mph speed limit indicated on
                        the road.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 13891, out 909, 12.86 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides; the road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a parking area and sidewalk on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from the opposing traffic flow.
                        white solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries being an edge line
                        on the left and a center line on the right. | roles: The white solid lines fit the
                        roles of edge and center lines in this urban context. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: You MUST NOT cross or straddle the solid white line unless it is safe
                        and you need to enter adjoining premises or a side road, or to pass a stationary
                        vehicle/slow cycle/horse. [[UK-Rule129]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid edge line; while not
                        explicitly prohibiting crossing in all cases, it marks the edge of the carriageway
                        [UK-TSRGD-S11P4-item11].
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid center line which
                        prohibits crossing or straddling [UK-Rule129].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 13891, out 803, 14.02 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead is a straight stretch with parked
                        vehicles on the right side. (lanes 1, mine 1, full)
Step 2  Left            I see a broken white line on the left, separating my lane from the opposite direction
                        of traffic.
                        white dashed, curb no, center_line, evidence full
Step 2  Right           I see a single yellow line on the right, next to the curb and parked cars.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the center line on
                        the left and the edge line on the right. | roles: The broken white center line and
                        solid yellow edge line fit their respective roles. | markings: There are no markings
                        in my lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: I may cross this broken white center line to overtake or turn off if
                        the road is clear. [[UK-Rule127]]
Step 5  Rule            right_boundary: The single yellow line indicates that I may stop to load or unload
                        unless other restrictions apply. [[UK-HC_MARKINGS-p2]]
Step 6  change_left     allowed (correct): Allowed by the broken white center line [UK-Rule127].
Step 6  change_right    prohibited (contested, correct): Prohibited by the physical curb and the edge line
                        role.
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or intersection in view.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or intersection in view.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow or intersection in view.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may change left to overtake if it is safe
                        to do so.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 13891, out 769, 12.71 s
```
