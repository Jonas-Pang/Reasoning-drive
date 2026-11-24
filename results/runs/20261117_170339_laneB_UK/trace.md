# Reasoning of lane run 20261117_170339_laneB_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test B | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction where a red double-decker
                        bus is stopped ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line dividing my lane from another lane to the left.
                        Photo 2 confirms this is a series of short white dashes with gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the road from the pavement. Photo 2 shows
                        this solid white line next to the car, and further ahead it remains solid.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 2 shows a white bicycle symbol painted in the lane
                        to the left of my lane, but not in my lane. No markings are seen within my lane in
                        Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a lane divider, and the white solid line
                        fits the role of an edge line. | markings: No markings were found in my lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [UK-Rule131].
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and the presence of a
                        curb [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane restricting
                        it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left'], missed ['line:stop_line', 'symbol:bike']), actions True, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 14577, out 927, 64.7 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single carriageway urban road, approaching a junction or crossing area
                        where the road layout changes. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line next to the car that becomes a series of short dashes, then
                        further ahead it forms a boundary for a cycle lane. Photo 2 shows a white dashed line
                        next to the car.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car, which further ahead becomes a solid
                        white line near the curb. Photo 2 shows a white dashed line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should not drive or park in a cycle lane marked by a broken white
                        line unless it is unavoidable. [[UK-Rule140-2]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 6  change_left     prohibited (contested, correct): prohibited by the cycle lane boundary and [UK-
                        Rule140-2]
Step 6  change_right    allowed (contested, label prohibited): allowed by the dashed lane line and [UK-
                        Rule131]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right if necessary; do not enter the cycle lane on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 14577, out 768, 13.84 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on an urban road in the UK, approaching a junction with traffic signals and
                        a pedestrian crossing ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car, which continues ahead. Photo 2
                        confirms a white solid line and a raised curb/barrier on the far right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.;
                        symbol:bike (full): Photo 2 shows a white bicycle symbol in a designated area ahead of
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being a lane_line and the right boundary being an
                        edge_line. | roles: The white dashed line fits the role of a lane divider, and the
                        white solid line fits the role of a road edge. | markings: The straight arrow is
                        consistent with the lane's position and the bike symbol indicates an advanced stop
                        line for cyclists. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 5  Rule            symbol:bike: This area is a cycle lane or route for pedal cycles and electric
                        scooters. [[UK-TSRGD-S11P4-item28]]
Step 6  change_left     allowed (correct): allowed by the broken white line [UK-Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        physical curb [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  enter_waiting_areanot_applicable: not_applicable; the bike symbol area is for cyclists, not a
                          vehicular waiting area.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the cycle area ahead of you at
                        the stop line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14577, out 1103, 17.97 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-carriageway urban road with buildings on the left and right.
                        The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid yellow lines running along the left edge of the road. Photo 2
                        confirms two solid yellow lines next to the car and continuing ahead.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the opposite direction of
                        traffic. Photo 2 shows a broken white line next to the car, consisting of several long
                        dashes and gaps.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [[UK-
                        HC_MARKINGS-p2-2]]
Step 5  Rule            right_boundary: A broken white line marks the centre of the road; do not cross it
                        unless you can see the road is clear and wish to overtake or turn off. [[UK-Rule127]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double yellow edge line and the
                        physical curb.
Step 6  change_right    allowed (correct): allowed by the broken white center line, provided the road is
                        clear.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to overtake if
                        it is safe to do so, but do not stop or park on the left due to the double yellow
                        lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 795, 14.24 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test B | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a pedestrian crossing (zebra
                        crossing) and a junction. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, which becomes zig-zagged
                        as it approaches the crossing. Photo 2 shows the white line next to the car is a solid
                        line that then transitions into a zig-zag pattern.
                        white zigzag, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line along the right edge of the road, which also becomes zig-
                        zagged as it approaches the crossing. Photo 2 shows the white line next to the car is
                        a solid line that then transitions into a zig-zag pattern.
                        white zigzag, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show white transverse stripes across the
                        lane, indicating a zebra crossing.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: You must not park in the zig-zag area or overtake moving or stationary
                        vehicles within it. [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to
                        ensure that drivers and pedestrians can see each other clearly. As a driver, you must
                        not park your vehicle anywh"
Step 5  Rule            right_boundary: You must not park in the zig-zag area or overtake moving or stationary
                        vehicles within it. [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to
                        ensure that drivers and pedestrians can see each other clearly. As a driver, you must
                        not park your vehicle anywh"
Step 5  Rule            line:crosswalk: This is a pedestrian crossing where pedestrians have priority. [UK-
                        HC_MARKINGS-p1] "Stop line at signals or police control"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is an edge line with a
                        curb, and the zig-zag markings prohibit overtaking/crossing in this area.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is an edge line with a
                        curb, and the zig-zag markings prohibit overtaking/crossing in this area.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits proceeding straight
                        through the crossing, provided pedestrians are yielded to.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking in my lane governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking in my lane governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not overtake or park within the zig-zag
                        lines, and be prepared to stop for pedestrians at the zebra crossing.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 955, 67.03 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test B | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, traveling straight ahead. There are
                        no intersections or ramps immediately visible. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid red lines running along the left edge of the road next to a
                        curb. Photo 2 confirms two solid red lines next to the curb.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my car, separating my lane from a
                        parked car and a cycle lane. Photo 2 shows a series of short white dashes and gaps.
                        white dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double red lines mean no stopping at any time. [[UK-HC_MARKINGS-p2-9]]
Step 5  Rule            right_boundary: Do not drive or park in a cycle lane marked by a broken white line
                        unless it is unavoidable. [[UK-Rule140-2]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double red lines and curb [UK-
                        HC_MARKINGS-p2-9]
Step 6  change_right    allowed (correct): allowed but discouraged unless unavoidable as it is a cycle lane
                        [UK-Rule140-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop or park on the left due to the
                        double red lines, and avoid entering the cycle lane on the right unless necessary.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14577, out 793, 14.15 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead. There are
                        no immediate intersections or ramps visible in the foreground. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the road from a blue-painted cycle lane.
                        Photo 2 confirms this solid white line next to the car and continuing ahead.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of short white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 1 shows white text 'A22' and 'A3' painted in the lane further
                        ahead. Photo 2 also shows these route numbers.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 1
                        agree with the left boundary being a special lane line (cycle lane) and the right
                        boundary being a lane line. | roles: The solid white line on the left fits the role of
                        a cycle lane boundary; the broken white line on the right fits the role of a lane
                        divider. | markings: The route numbers (A22, A3) are informative and do not contradict
                        the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You MUST NOT drive or park in a cycle lane marked by a solid white line
                        during its times of operation. [[UK-Rule140]]
Step 5  Rule            right_boundary: You should keep between these short, broken white lines. [[UK-
                        Rule131]]
Step 5  Rule            text:other: Route numbers are informative and do not restrict movement.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line boundary of the
                        cycle lane [UK-Rule140].
Step 6  change_right    allowed (correct): allowed by the broken white lane divider [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict going straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or intersection governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right if needed. Do not enter the cycle lane to the
                        left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 14577, out 962, 47.52 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, heading towards a straight stretch
                        with parked cars and shops on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from a cycle lane on the left.
                        Photo 2 shows the same white broken line next to my car, consisting of short dashes
                        and gaps.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from another traffic lane. Photo
                        2 shows the same white broken line next to my car, consisting of short dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 1 agree with the boundaries: a special lane line on the left (cycle lane) and a
                        lane line on the right. | roles: The white dashed patterns fit the roles of a cycle
                        lane boundary and a lane divider. | markings: No markings are present in my lane,
                        which is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: I should not drive or park in the cycle lane unless it is unavoidable.
                        [[UK-Rule140-2]]
Step 5  Rule            right_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line marking a cycle lane; [UK-
                        Rule140-2] allows crossing it if unavoidable, and [UK-TSRGD-S11P4-item2] recommends
                        not crossing unless safe and clear of cyclists.
Step 6  change_right    allowed (correct): The right boundary is a broken white lane divider; [UK-Rule131]
                        allows changing lanes provided it is safe.
Step 6  go_straight     allowed (contested, correct): No marking governs this action; it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may proceed straight or change lanes if safe. Be
                        cautious of the cyclist in the cycle lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 866, 48.56 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, approaching a zebra crossing. The
                        road is a single carriageway with one lane in each direction. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line that is solid near the car and then becomes zig-zagged as
                        it approaches the crossing. Photo 2 confirms the line next to the car is a solid white
                        line.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line that is solid near the car and then becomes zig-zagged as
                        it approaches the crossing. Photo 2 confirms the line next to the car is a solid white
                        line.
                        white solid, curb no, center_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show white zig-zag lines on both sides of
                        the lane approaching the crossing.; line:crosswalk (full): Photo 1 and Photo 2 show a
                        zebra crossing (broad white stripes) across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is the division between opposing flows of traffic. [UK-
                        TSRGD-S11P4-item7] "Diagram 1008.1 Division between opposing flows of traffic on a
                        carriageway other than at places where the marking at item 3 is used (Longitudinal
                        marking)"
Step 5  Rule            line:crosswalk: You must not park or overtake within the zig-zag area before the
                        crossing. [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to ensure that
                        drivers and pedestrians can see each other clearly. As a driver, you must not park
                        your vehicle anywh"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white edge
                        line and the area is a zig-zag crossing zone where overtaking/crossing is restricted.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white
                        center line and the area is a zig-zag crossing zone.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits proceeding straight
                        through the crossing after yielding to pedestrians.
Step 6  turn_left       not_applicable: not_applicable: no intersection or turn arrow is present.
Step 6  turn_right      not_applicable: not_applicable: no intersection or turn arrow is present.
Step 6  u_turn          not_applicable: not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not overtake or change lanes within the
                        zig-zag markings; stop and give way to any pedestrians using the zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 983, 49.13 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test B | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, traveling straight ahead. There are
                        no immediate intersections or ramps visible in the foreground. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms this is a broken white line with short dashes and short gaps.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms this is a broken white line with short dashes and short gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle with the number '20'
                        painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries; the left boundary separates the lane from a cycle lane, and the
                        right boundary marks the edge of the carriageway. | roles: The white dashed lines fit
                        the roles of a cycle lane boundary and a carriageway edge line in an urban setting. |
                        markings: The speed limit marking is consistent with the residential nature of the
                        road. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should not drive or park in a cycle lane marked by a broken white
                        line unless it is unavoidable. [UK-Rule140-2] "Do not drive or park in a cycle lane
                        marked by a broken white line unless it is unavoidable."
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            text:speed_limit: This is an informative marking indicating the speed limit of 20 mph.
                        [null]
Step 6  change_left     allowed (contested, label prohibited): allowed, but discouraged by UK-Rule140-2 as it
                        is a cycle lane.
Step 6  change_right    allowed (correct): allowed, as the right boundary is a dashed edge line (UK-
                        TSRGD-S11P4-item11).
Step 6  go_straight     allowed (contested, correct): allowed, as no marking prohibits it.
Step 6  turn_left       not_applicable: not_applicable, no arrow or intersection governs this.
Step 6  turn_right      not_applicable: not_applicable, no arrow or intersection governs this.
Step 6  u_turn          not_applicable: not_applicable, no arrow or intersection governs this.
Step 6  enter_waiting_areanot_applicable: not_applicable, no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and observe the 20 mph speed limit. Avoid entering the cycle lane to
                        the left unless unavoidable.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 14577, out 969, 15.37 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test B | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a junction with traffic signals ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which then becomes a broken white
                        line further ahead. Photo 2 confirms the solid white line next to the car and the
                        start of the broken line further ahead.
                        white solid_dashed (near line solid), curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car and continuing ahead. Photo 2 shows
                        a broken white line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 and Photo 2 show a white arrow in the lane pointing
                        straight and then turning left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the right boundary is a lane line, suggesting another lane of the same
                        direction to the right. | roles: the white color and dashed/solid patterns fit the
                        roles of lane and edge lines. | markings: the left-turn arrow is consistent with the
                        lane's position. | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is an edge line at a road junction. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            right_boundary: This is a lane divider; I should keep between the lane lines. [[UK-
                        Rule131]]
Step 5  Rule            arrow:left: Vehicular traffic must turn left. [[UK-TSRGD-Part6,item19]]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white line of the left
                        boundary [UK-Rule129]
Step 6  change_right    allowed (correct): allowed by the broken white line of the right boundary [UK-Rule131]
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited by the left-turn arrow [UK-TSRGD-
                        Part6,item19]
Step 6  turn_left       allowed (correct): allowed by the left-turn arrow [UK-TSRGD-Part6,item19]
Step 6  turn_right      prohibited (correct): prohibited by the left-turn arrow [UK-TSRGD-Part6,item19]
Step 6  u_turn          prohibited (correct): prohibited by the left-turn arrow [UK-TSRGD-Part6,item19]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane that must turn left at the junction. If you wish to go straight or
                        turn right, you must change to the lane on your right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:straight_left']), actions False, unsafe [], citation
                        accepted, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 14577, out 972, 36.32 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road in the UK, traveling straight ahead. There are no
                        intersections or ramps immediately in view. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 shows a
                        series of short white dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 are
                        consistent with a solid edge line on the left and a dashed lane line on the right,
                        indicating another lane of the same direction exists to the right. | roles: The solid
                        white line on the left acts as an edge line (separating the carriageway from the
                        parking/curb area), and the dashed white line on the right acts as a lane divider. |
                        markings: No markings are present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            right_boundary: These are lane dividers; the driver should keep between them. [UK-
                        Rule131] "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid white edge
                        line, and crossing it would move the car off the carriageway onto the curb/parking
                        area.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line, which
                        allows lane changes when safe.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if necessary. Do not cross the solid
                        white line on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 14577, out 859, 48.86 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with a pedestrian crossing
                        and a traffic island ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows two solid red lines along the left edge of the road. Photo 2 confirms
                        two solid red lines next to the car and continuing ahead.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line dividing the lanes. Photo 2 shows a broken white
                        line next to the car with several short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left_right (full): Photo 2 shows a white arrow in my lane pointing both straight
                        and left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 1 agree with having an edge line on the left and a lane line on the right |
                        roles: the double red edge line and broken white lane line fit their roles | markings:
                        the straight-and-left arrow is consistent with the lane's position | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Double red lines mean no stopping at any time. [[UK-HC_MARKINGS-p2-9]]
Step 5  Rule            right_boundary: Broken white lane dividers are used to divide lanes; I should keep
                        between them. [[UK-Rule131]]
Step 5  Rule            arrow:left_right: The arrow indicates that both going straight and turning left are
                        possible movements. [[UK-HC_MARKINGS-p3-6]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double red edge line and curb [UK-
                        HC_MARKINGS-p2-9]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [UK-Rule131]
Step 6  go_straight     allowed (correct): allowed by the arrow in my lane [UK-HC_MARKINGS-p3-6]
Step 6  turn_left       allowed (correct): allowed by the arrow in my lane [UK-HC_MARKINGS-p3-6]
Step 6  turn_right      prohibited (correct): prohibited by the arrow in my lane which only shows straight and
                        left [UK-HC_MARKINGS-p3-6]
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may proceed straight or turn left. Do not stop or park
                        on the left due to the double red lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left_right'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions ['go_straight allowed although no arrow shows it',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 14577, out 948, 49.85 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-carriageway urban road in the UK, facing forward. There are no
                        intersections immediately ahead, but the road continues straight. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road, which becomes a zig-
                        zag pattern further ahead. Photo 2 shows the line next to the car is a solid white
                        line bordering a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line along the right edge of the road, which also becomes
                        a zig-zag pattern further ahead. Photo 2 shows the line next to the car is a solid
                        white line bordering a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): Photo 1 and Photo 2 show white zig-zag lines on both sides of the
                        lane further ahead, indicating a pedestrian crossing area.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            symbol:other: You must not park or overtake other vehicles within the zig-zag area
                        before the crossing. [[UK-KYTS-zigzag]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid edge line
                        with a raised curb, and there is no lane to the left.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid edge line
                        with a raised curb, and there is no lane to the right.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits continuing straight in the
                        only available lane.
Step 6  turn_left       not_applicable: not_applicable: no intersection or turn-off is present in the visible
                        stretch.
Step 6  turn_right      not_applicable: not_applicable: no intersection or turn-off is present in the visible
                        stretch.
Step 6  u_turn          not_applicable: not_applicable: no intersection or sufficient space is present for a
                        U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not park or overtake other vehicles when
                        you reach the zig-zag markings ahead of the crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 14577, out 964, 15.41 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction with traffic
                        signals. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a curb and double red lines along the left edge of the road. Photo 2
                        confirms the presence of a raised curb and two solid red lines running parallel to the
                        lane.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of short white dashes and gaps immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double red lines mean no stopping at any time. [[UK-HC_MARKINGS-p2-9]]
Step 5  Rule            right_boundary: Broken white lane dividers are used to divide lanes; the driver should
                        keep between them. [[UK-Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double red lines and curb [UK-
                        HC_MARKINGS-p2-9]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [UK-Rule131]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [UK-TSRGD-Part6,item20]
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited by the straight-ahead arrow [UK-TSRGD-
                        Part6,item20]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. Do not stop or park on the left due to the double
                        red lines. If you need to turn, change to the right lanes.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 14577, out 916, 15.53 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test B | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a pedestrian crossing and a
                        junction ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, which becomes a zig-zag
                        pattern as it approaches the crossing. Photo 2 shows the line next to the car is a
                        solid white line.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line along the right edge of the road, which also becomes a zig-
                        zag pattern as it approaches the crossing. Photo 2 shows the line next to the car is a
                        solid white line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show white zebra stripes across the lane.;
                        symbol:other (full): Photo 1 shows zig-zag white lines on both sides of the lane
                        approaching the crossing.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            line:crosswalk: This is a pedestrian crossing. [UK-HC_MARKINGS-p1] "Stop line at
                        signals or police control"
Step 5  Rule            symbol:other: You must not park or overtake within the zig-zag area before the
                        crossing. [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to ensure that
                        drivers and pedestrians can see each other clearly. As a driver, you must not park
                        your vehicle anywh"
Step 6  change_left     prohibited (contested, correct): prohibited: the boundary is an edge line with a
                        raised curb, and the zig-zag markings prohibit overtaking/crossing in this area.
Step 6  change_right    prohibited (contested, correct): prohibited: the boundary is an edge line with a
                        raised curb, and the zig-zag markings prohibit overtaking/crossing in this area.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits proceeding straight
                        through the crossing.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this movement in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this movement in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not overtake or park within the zig-zag
                        lines approaching the zebra crossing; yield to pedestrians.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14577, out 1013, 65.5 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, traveling straight ahead. There is a bus lane to
                        the left and a sidewalk to the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        this solid white line next to the car.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a red line along the edge of the road next to the curb. Photo 2 shows a
                        double red line next to the car, and a curb.
                        other double_solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: Photo 2 reveals the right boundary is a double red line, whereas Photo 1
                        only shows a red line; Photo 2 decides. | position: The lane count of 1 and index 1
                        agree with the boundaries: a special lane line on the left and an edge line on the
                        right. | roles: The solid white line on the left fits the role of a bus lane boundary;
                        the double red line on the right fits the role of a road edge with waiting
                        restrictions. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a bus lane. [[UK-TSRGD-Part6,item11]]
Step 5  Rule            right_boundary: Double red lines mean no stopping at any time. [[UK-HC_MARKINGS-p2-9]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line marking a bus
                        lane; [UK-Rule141-2] recommends not driving in a bus lane, and [UK-TSRGD-Part6,item11]
                        defines it as a reserved lane.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb and double red lines;
                        [UK-HC_MARKINGS-p2-9] prohibits stopping, and the curb physically prevents leaving the
                        roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action; it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Do not enter the bus lane to the left
                        or stop along the red lines to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 901, 49.0 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test B | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on an urban road in the UK, traveling straight ahead. There are no
                        immediate intersections or ramps visible. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line separating my lane from a bus lane. Photo 2 confirms
                        a white solid line next to my car and continuing ahead.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a grey curb and a metal railing on the right. Photo 2 shows the grey
                        curb immediately to the right of my lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a designated lane (bus lane). [[UK-TSRGD-
                        Part6,item11]]
Step 5  Rule            right_boundary: This is the edge of the carriageway. [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white line
                        separating my lane from a bus lane, and [UK-Rule140] prohibits driving in a
                        cycle/special lane marked by a solid white line during operation; however, more
                        specifically, a solid line generally prohibits crossing unless permitted by other
                        rules.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a raised curb and
                        railing.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the bus lane to the left or cross
                        the curb to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14577, out 803, 14.62 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test B | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction or
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        shows a series of short white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows the head of a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a solid white edge line on the left and a dashed lane line
                        on the right. | roles: The solid white line on the left fits the role of an edge line;
                        the dashed white line on the right fits the role of a lane divider. | markings: The
                        straight arrow in the lane is consistent with the boundaries and the road layout. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This is a lane divider; I should keep between the lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line [UK-
                        TSRGD-S11P4-item11] and the fact that it is the edge of the road.
Step 6  change_right    allowed (correct): allowed by the dashed lane line [UK-Rule131].
Step 6  go_straight     allowed (correct): allowed by the straight arrow [UK-TSRGD-Part6,item20].
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow [UK-TSRGD-Part6,item20] which
                        mandates proceeding ahead.
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow [UK-TSRGD-Part6,item20] which
                        mandates proceeding ahead.
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow [UK-TSRGD-Part6,item20] which
                        mandates proceeding ahead.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight ahead as indicated by the arrow. You may change
                        to the right lane if necessary, but do not cross the solid line on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 1007, 15.17 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, facing a junction with traffic lights
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the left lane. Photo 2
                        confirms a broken white line next to my car with several short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right lane. Photo 2
                        confirms a broken white line next to my car with several short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right. |
                        roles: The white dashed lines are consistent with the role of lane dividers. |
                        markings: The straight-ahead arrow is consistent with a middle lane intended for
                        through traffic. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            right_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            arrow:straight: This indicates the lane is for proceeding straight ahead. [[UK-
                        HC_MARKINGS-p3-6]]
Step 6  change_left     allowed (correct): allowed by the broken white line [UK-Rule131].
Step 6  change_right    allowed (correct): allowed by the broken white line [UK-Rule131].
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [UK-HC_MARKINGS-p3-6].
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [UK-HC_MARKINGS-p3-6]
                        which restricts the lane to straight movement.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [UK-HC_MARKINGS-p3-6]
                        which restricts the lane to straight movement.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [UK-HC_MARKINGS-p3-6]
                        which restricts the lane to straight movement.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, change to the
                        corresponding outer lane before the junction.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 952, 47.53 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead. The road
                        continues forward with no immediate intersection or ramp visible. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        confirms this is a single solid white line next to the car, extending further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right. Photo 2 shows a series of short white
                        dashes with gaps next to the car, continuing as a broken line further ahead.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white solid line on the left acts as a lane divider, and the white dashed
                        line on the right acts as the edge of the carriageway. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: This is a division of traffic lanes; while not explicitly prohibiting
                        crossing in this specific informative rule, general UK rules for solid white lane
                        lines typically restrict crossing. [UK-TSRGD-S11P4-item4] "Diagram 1005 Division of
                        carriageway into traffic lanes on part of the carriageway where vehicles normally
                        proceed in the same direction other than at places wh"
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     prohibited (contested, correct): prohibited; the left boundary is a solid white line,
                        which generally prohibits crossing between lanes.
Step 6  change_right    allowed (correct): allowed; the right boundary is a dashed line, which allows crossing
                        if safe, though it is an edge line.
Step 6  go_straight     allowed (contested, correct): allowed; no markings restrict going straight.
Step 6  turn_left       not_applicable: not_applicable; no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable; no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable; no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Do not cross the solid white line to
                        the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 879, 49.91 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with shops on both sides. The road ahead is clear,
                        with a few vehicles in the opposite direction. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road. Photo 2 confirms a
                        double solid yellow line next to the car, continuing as a solid line further ahead.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line dividing the road. Photo 2 shows a series of short
                        white dashes with gaps next to the car, continuing ahead.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [UK-HC_MARKINGS-p2-2]
                        "Double yellow lines mean no waiting at any time, unless there are signs that
                        specifically indicate seasonal restrictions."
Step 5  Rule            right_boundary: A broken white line marks the centre of the road; do not cross it
                        unless you can see the road is clear and wish to overtake or turn off. [UK-Rule127] "A
                        broken white line. This marks the centre of the road. When this line lengthens and the
                        gaps shorten, it means that there is a hazard ahead. Do not cross it un"
Step 6  change_left     prohibited (contested, correct): prohibited by the left edge boundary and the curb.
Step 6  change_right    allowed (correct): allowed by the broken white center line, provided the road is
                        clear.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection immediately ahead.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection immediately ahead.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop or park on the left due to the
                        double yellow lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 776, 12.39 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead. The road
                        continues forward with no immediate intersection or ramp visible. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line dividing the road. Photo 2 shows a series of short
                        white dashes with gaps of similar length next to the car, continuing further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line at the edge of the road. Photo 2 shows a solid white
                        line next to the car, which continues as a continuous line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a lane divider, and the white solid line
                        fits the role of a carriageway edge line. | markings: No markings were observed in the
                        lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line [UK-
                        Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited as it would cross the solid white edge
                        line [UK-TSRGD-S11P4-item11] into a non-carriageway area.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no intersection or arrow governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no intersection or arrow governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no intersection or arrow governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the left lane if needed. Do not cross the solid white
                        line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14577, out 860, 15.48 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward. The road is wet, and there are
                        buildings and a bus stop on the left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road, next to the
                        pavement. Photo 2 confirms a solid yellow line immediately to the left of my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line to the right of my lane; it is an open area where other
                        cars are parked or moving. Photo 2 also shows no painted line to the right of my car.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 are
                        consistent with the left boundary being an edge line and the right boundary being
                        absent/unknown. | roles: The solid yellow line on the left fits the role of an edge
                        line indicating waiting restrictions. | markings: No markings were observed in the
                        lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A single yellow line indicates that waiting is restricted, but stopping
                        to load or unload may be permitted. [UK-HC_MARKINGS-p2] "Waiting restrictions
                        indicated by yellow lines apply to the carriageway, pavement and verge. You may stop
                        to load or unload (unless there are also loading restr"
Step 6  change_left     prohibited (contested, label not_determined): prohibited: the left boundary is a solid
                        yellow line and a curb, and UK-Rule140/TSRGD-12(2) generally prohibit driving on
                        pavements/cycle lanes, though here it is primarily a physical curb and waiting
                        restriction line.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: there is no marking or curb governing
                        the right side.
Step 6  go_straight     allowed (contested, label not_determined): allowed: no marking restricts going
                        straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line to the left as it
                        borders the pavement.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 14577, out 804, 13.75 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction where a bus lane is
                        present on the left. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from a bus lane. Photo 2 shows
                        the same white broken line next to my car, consisting of short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the right edge of the road.
                        Photo 2 shows the same white broken line next to my car, consisting of short dashes
                        and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show the words 'BUS LANE' painted in the lane to
                        the left of my lane, not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with the boundaries: a lane line on the left and an edge line on the
                        right. | roles: The white dashed pattern fits both the lane divider and the edge of
                        the carriageway in an urban setting. | markings: The 'BUS LANE' text is in the
                        adjacent lane, which is consistent with the left boundary being a lane line. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (contested, label prohibited): allowed; the left boundary is a broken white
                        line [UK-Rule131].
Step 6  change_right    allowed (correct): allowed; the right boundary is a broken white line [UK-
                        TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): allowed; no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable; no arrow governs this action.
Step 6  turn_right      not_applicable: not_applicable; no arrow governs this action.
Step 6  u_turn          not_applicable: not_applicable; no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area is present in my lane.
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane. You may proceed straight or change lanes, but be aware
                        that the lane to your left is a designated bus lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 14577, out 920, 16.19 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, facing a road that appears to be a single lane
                        in the current direction, with a yellow box junction ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to the car, which then becomes a white solid
                        line further ahead near the junction. Photo 2 confirms the white dashed line
                        immediately next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows the edge of the road with a curb and some white markings on the asphalt.
                        Photo 2 shows the curb and a white line marking the edge of the carriageway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show a yellow criss-cross box junction ahead of
                        the car.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            area:grid: I must not enter the box junction if I will have to stop within it due to
                        stationary vehicles. [[UK-TSRGD-11(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed; the left boundary is a broken white
                        line [UK-Rule131].
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited; the right boundary is a solid
                        line and a curb [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): allowed; no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable; no arrow governs this action.
Step 6  turn_right      not_applicable: not_applicable; no arrow governs this action.
Step 6  u_turn          not_applicable: not_applicable; no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change to the left lane. Do not enter the yellow box
                        junction ahead unless your exit is clear.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 14577, out 905, 35.56 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides. A red bus is ahead in the same
                        direction. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with long dashes and gaps.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, only the edge of the road and parked cars.
                        Photo 2 shows no painted line next to the car.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white bicycle symbol to the left of the lane, but
                        it is not in my lane; it is in the cycle lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a special lane line on the left and an edge on the right. |
                        roles: The white dashed line on the left fits the role of a boundary for a cycle lane.
                        | markings: The bicycle symbol is in the cycle lane, not in my lane, which is
                        consistent with the boundary roles. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should not drive in a cycle lane marked by a broken white line
                        unless it is unavoidable. [[UK-Rule140-2]]
Step 5  Rule            right_boundary: No specific rule prohibits movements across a non-painted edge line
                        unless other rules apply. [null]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line
                        marking a cycle lane; [UK-Rule140-2] discourages entering it unless unavoidable, but
                        it is not strictly prohibited.
Step 6  change_right    allowed (correct): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking governs this action; it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Avoid entering the cycle lane on your left
                        unless necessary.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions ['change_right decided with nothing marked on that side']
Tokens                  in 14577, out 868, 14.43 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with a pedestrian crossing
                        and traffic signals ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road, which becomes zig-
                        zag lines further ahead. Photo 2 shows the solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a central island/refuge.
                        Photo 2 shows this solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show white zig-zag lines on both sides of
                        the lane approaching the crossing.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is the division between the main carriageway and a traffic lane
                        or island. [UK-TSRGD-S11P4-item10] "Diagram 1010 (a) edge of the carriageway at a road
                        junction or a lay-by, or at an exit from a private drive onto a public road; (b) the
                        start of a traffic lane,"
Step 5  Rule            line:crosswalk: You must not park or overtake within the zig-zag area before the
                        crossing. [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to ensure that
                        drivers and pedestrians can see each other clearly. As a driver, you must not park
                        your vehicle anywh"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white line
                        and a curb [UK-Rule140]
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white line
                        and a curb [UK-Rule140]
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not overtake or park within the zig-zag
                        markings ahead of the crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14577, out 889, 46.41 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with shops on both sides, proceeding straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a parking area with cars.
                        Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line in the center of the road. Photo 2 shows a series of
                        short white dashes with gaps next to the car.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a center line on the right and an edge line on the left. | roles:
                        The white solid line on the left fits the role of an edge line for a parking area; the
                        white dashed line on the right fits the role of a center line. | markings: No markings
                        are present in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This marks the centre of the road; I may cross it to overtake if the
                        road is clear. [[UK-Rule127]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white edge line; while
                        not explicitly prohibited by a 'must not' rule for this specific edge line, it marks
                        the boundary of the carriageway/parking area.
Step 6  change_right    allowed (correct): The right boundary is a broken white center line, which allows
                        crossing if the road is clear according to [UK-Rule127].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to overtake if
                        it is safe to do so, but do not enter the parking area on the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14577, out 856, 67.56 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with shops on the left, approaching a junction with a
                        traffic signal. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and double yellow lines along the left edge of the road.
                        Photo 2 confirms the raised curb and the double yellow lines next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a stretch of this broken white line with several short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane.;
                        symbol:bike (full): Photo 2 shows a white bicycle symbol painted in my lane, further
                        ahead of the arrow.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a curb/edge line on the left and a lane line on the
                        right indicate I am in the leftmost lane of a two-lane road. | roles: the yellow edge
                        line and white dashed lane line fit their respective roles. | markings: the straight
                        arrow and bike symbol are consistent with a lane that allows through traffic and
                        shares space with cyclists. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [UK-HC_MARKINGS-p2-2]
                        "Double yellow lines mean no waiting at any time, unless there are signs that
                        specifically indicate seasonal restrictions."
Step 5  Rule            right_boundary: I should keep between the short, broken white lane dividers. [UK-
                        Rule131] "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 5  Rule            symbol:bike: This indicates a cycle lane or route, and I should be cautious of
                        cyclists. [UK-TSRGD-S11P4-item28] "Diagram 1057 Cycle lane, track , route, or a way
                        that would be a cycle track but for it being accessible, under a temporary statutory
                        provision, by electric sco"
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb and double yellow lines
                        (UK-HC_MARKINGS-p2-2).
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line (UK-Rule131).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (UK-TSRGD-Part6,item20).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (UK-TSRGD-Part6,item20)
                        and the curb.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (UK-TSRGD-Part6,item20).
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (UK-TSRGD-Part6,item20).
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. Be mindful of cyclists as indicated by the bike
                        symbol. Do not stop or park on the left due to the double yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 14577, out 1095, 17.04 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction where a bus is
                        stopped ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line dividing my lane from the lane to the left. Photo 2
                        confirms this is a short, broken white line next to the car, continuing as a dashed
                        line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line at the edge of the road, which becomes a broken line
                        further ahead near the junction. Photo 2 shows a solid white line immediately to the
                        right of the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right | roles: the
                        white dashed line fits the role of a lane divider, and the white solid line fits the
                        role of an edge line | markings: no markings were found in the lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [UK-Rule131]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [UK-
                        TSRGD-S11P4-item11]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 853, 67.81 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides, proceeding straight ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line dividing the road into two lanes. Photo 2 shows the
                        same broken white line next to the car, consisting of several short white dashes and
                        gaps of similar length.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line at the edge of the road, which becomes a broken line
                        further ahead near a junction. Photo 2 shows a solid white line next to the car,
                        separating the lane from the pavement/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right | roles: the
                        white dashed line fits the role of a lane_line and the white solid line fits the role
                        of an edge_line | markings: no markings present in the lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which allows
                        lane changes provided it is safe.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line and there is a curb, which prohibits leaving the carriageway.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane if
                        safe to do so; do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 881, 67.21 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, proceeding straight ahead. There are
                        no immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms this is a short, broken white line next to my car, continuing as a dashed
                        line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, bordering a sidewalk with a metal
                        railing. Photo 2 shows the solid white line next to my car and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle with the number '20'
                        painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 (rightmost) agree with having a lane line on the left and an edge line on the
                        right. | roles: The broken white line fits the role of a lane divider, and the solid
                        white line with a curb fits the role of an edge line. | markings: The speed limit
                        marking is consistent with an urban road environment. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            text:speed_limit: This is an informative marking indicating a speed limit of 20 mph.
                        [null]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [UK-Rule131],
                        which permits lane changes when safe.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line [UK-TSRGD-S11P4-item11] and a raised curb, which prohibits leaving the
                        carriageway.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight, and the
                        boundaries do not restrict this movement.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: there is no waiting area or two-way left-turn lane
                          in view.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the left lane if needed. Observe the 20 mph speed limit
                        indicated on the road.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:speed_limit'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 14577, out 1027, 67.72 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing a T-junction or intersection ahead. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a grey raised curb separating the road from the sidewalk. Photo 2
                        confirms the presence of a raised curb and a white line painted along the edge of the
                        road next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from a parking area or another
                        lane. Photo 2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This is a lane divider; I should keep between the lane dividers. [[UK-
                        Rule131]]
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb and solid edge line.
Step 6  change_right    allowed (correct): allowed by the dashed lane line [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right if necessary. Be aware of the parked cars on the
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 14577, out 757, 48.0 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-carriageway urban road with shops on both sides, proceeding
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a line of white paint along the left edge of the road.
                        Photo 2 shows the raised curb and a broken white line next to the car, consisting of
                        short dashes and gaps.
                        white dashed, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a wide area of asphalt to the right with parked cars and no painted
                        lines. Photo 2 shows no painted lines to the right of the car.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the word 'BUS' painted in white on the road surface in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the boundaries being edge lines on both sides | roles: the white dashed line on
                        the left is consistent with an edge line for a cycle lane or shoulder | markings: the
                        'BUS' text indicates the lane is a bus lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: No painted line exists; the edge of the road is defined by the
                        physical space. [null]
Step 5  Rule            text:bus: You should not drive in a bus lane during its period of operation. [UK-
                        Rule141-2] "Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation."
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb and edge line [UK-
                        Rule140-2]
Step 6  change_right    allowed (correct): allowed as there is no marking prohibiting it
Step 6  go_straight     allowed (contested, correct): allowed, although the lane is a bus lane, there is no
                        mandatory prohibition against proceeding straight if the car is already in it, but it
                        is discouraged [UK-Rule141-2]
Step 6  turn_left       not_applicable: not_applicable as there is no arrow and the boundary is a curb
Step 6  turn_right      not_applicable: not_applicable as there is no arrow
Step 6  u_turn          not_applicable: not_applicable as there is no arrow
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane. You should move to the right if possible to avoid
                        driving in a reserved lane during its operation.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation unlisted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 14577, out 948, 23.09 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides, proceeding straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a parking/loading area where
                        cars are stopped. Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a cycle lane. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is an edge line at a road junction or boundary of a lane; it does
                        not explicitly prohibit crossing unless other rules apply. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            right_boundary: You MUST NOT drive or park in a cycle lane marked by a solid white
                        line during its times of operation. [[UK-Rule140]]
Step 6  change_left     allowed (contested, label prohibited): allowed; the solid white line on the left is an
                        edge line for a parking/loading area, and no rule prohibits crossing it if safe.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited; the right boundary is a solid white
                        line marking a cycle lane, which is prohibited by [UK-Rule140].
Step 6  go_straight     allowed (contested, correct): allowed; no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable; no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable; no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable; no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the cycle lane to your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14577, out 811, 13.41 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on the left and trees on the right. Ahead is
                        a clear stretch of road with no immediate intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a single solid white line next to my car and continuing ahead.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line on the right. Photo 2 shows a series of short white
                        dashes and gaps next to my car and continuing ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a special lane line on the left and a lane line on the right.
                        | roles: The solid white line on the left fits the role of a bus lane boundary, and
                        the dashed white line on the right fits the role of a lane divider. | markings: No
                        markings were found in my lane, which is consistent with the boundaries. | unseen: No
                        | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a bus lane. [[UK-TSRGD-Part6,item11]]
Step 5  Rule            left_boundary: I should not drive in the bus lane during its period of operation.
                        [[UK-Rule141-2]]
Step 5  Rule            right_boundary: This is a lane divider; I should keep between the lane dividers. [[UK-
                        Rule131]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line boundary of the
                        bus lane [UK-Rule141-2].
Step 6  change_right    allowed (correct): allowed by the dashed white lane line [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along my lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Do not enter the bus lane to
                        your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 14577, out 897, 50.14 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road in the UK. The road ahead is straight with no
                        immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a grey stone curb and a sidewalk to the left. Photo 2 confirms the
                        presence of a raised stone curb immediately next to the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white zigzag line along the right side of the road. Photo 2 shows the
                        same white zigzag line next to the car, consisting of several diagonal segments.
                        white zigzag, curb no, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 and Photo 2 show white zigzag lines painted on the
                        road surface, extending from the right boundary into the lane area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a curb on the left and a zigzag edge line on the right. | roles:
                        The curb on the left and zigzag line on the right both fit the role of edge boundaries
                        for a single-lane road. | markings: The zigzag lines are typical for pedestrian
                        crossing approach areas in the UK, which is consistent with the urban residential
                        setting. | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: You must not park or overtake within the zig-zag area. [UK-KYTS-
                        zigzag] "The zig-zag markings at crossings are there to ensure that drivers and
                        pedestrians can see each other clearly. As a driver, you must not park your vehicle
                        anywh"
Step 5  Rule            area:channelizing: You MUST NOT park in the area covered by the zig-zag lines and MUST
                        NOT overtake moving or stopped vehicles here. [UK-Rule191] "You MUST NOT park on a
                        crossing or in the area covered by the zig-zag lines. You MUST NOT overtake the moving
                        vehicle nearest the crossing or the vehicle neares"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a raised curb [UK-
                        TSRGD-S11P4-item11].
Step 6  change_right    allowed (contested, label prohibited): allowed: the right boundary is a zigzag line
                        which prohibits parking/overtaking but not moving into the space if safe, though it is
                        an edge line.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no intersection or arrow governs this action.
Step 6  turn_right      not_applicable: not_applicable: no intersection or arrow governs this action.
Step 6  u_turn          not_applicable: not_applicable: no intersection or arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not park or overtake other vehicles within
                        the zigzag marked area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14577, out 973, 37.35 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction with a traffic
                        signal ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms this is a short, broken white line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line at the edge of the road, which then becomes a broken
                        line further ahead near the junction. Photo 2 shows a solid white line next to my car
                        and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 2 shows a white arrow pointing right in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane divider, and the white solid line
                        with a curb fits the role of an edge line | markings: the right-turn arrow is
                        consistent with being in the rightmost lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            arrow:right: Vehicular traffic must turn right. [[UK-TSRGD-Part6,item21]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [UK-Rule131]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and raised
                        curb [UK-TSRGD-S11P4-item11]
Step 6  go_straight     prohibited (correct): prohibited by the mandatory right-turn arrow [UK-TSRGD-
                        Part6,item21]
Step 6  turn_left       prohibited (correct): prohibited by the mandatory right-turn arrow [UK-TSRGD-
                        Part6,item21]
Step 6  turn_right      allowed (correct): allowed by the mandatory right-turn arrow [UK-TSRGD-Part6,item21]
Step 6  u_turn          prohibited: prohibited by the mandatory right-turn arrow [UK-TSRGD-Part6,item21]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a mandatory right-turn lane. If you intend to go straight or turn left, you
                        must change to the left lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 988, 17.82 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead. There are
                        no immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane on the left. Photo
                        2 confirms this solid white line immediately next to the car and extending forward.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right, separating my lane from another lane
                        of the same direction. Photo 2 shows a short white dash and a gap immediately to the
                        right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a bus lane. [[UK-TSRGD-Part6,item11]]
Step 5  Rule            left_boundary: Driving in a lane marked by a solid white line (as a cycle or special
                        lane) is prohibited during its times of operation. [[UK-Rule140]]
Step 5  Rule            right_boundary: Short, broken white lines divide lanes; you should keep between them
                        but may cross them if safe. [[UK-Rule131]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line boundary of the
                        bus lane [UK-Rule140].
Step 6  change_right    allowed (correct): allowed by the broken white lane divider [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict continuing straight in
                        the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane or move to the right if necessary. Do not enter the bus lane
                        to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 14577, out 852, 16.63 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road in the UK. The road ahead is straight with parked
                        cars on the right and a designated bus lane on the left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from a bus lane. Photo 2 confirms
                        a single solid yellow line next to my car and continuing ahead.
                        yellow solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows the edge of the road with parked cars and a curb. Photo 2 shows a solid
                        white line next to the parked cars and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows the word 'BUS' painted in yellow in the lane to the
                        left of my lane, but not in my lane. There are no markings within my own lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line separating a general traffic lane from a bus lane
                        prohibits crossing into the bus lane unless permitted. [null]
Step 5  Rule            right_boundary: This is the edge of the carriageway; crossing it is generally
                        prohibited as it leads to a curb/parking area. [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow boundary line
                        separating my lane from the bus lane.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and the
                        presence of a raised curb.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or turn arrow in the
                        visible stretch.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or turn arrow in the
                        visible stretch.
Step 6  u_turn          not_applicable: not_applicable as there are no markings governing a U-turn in this
                        stretch.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the bus lane to your left or
                        cross the edge line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 14577, out 874, 14.32 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with shops on both sides, proceeding straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a parking area with cars.
                        Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line in the center of the road. Photo 2 shows a series of
                        short white dashes with gaps next to the car.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a center line on the right and an edge line on the left. | roles:
                        The white solid line on the left fits the role of an edge line for a parking area; the
                        white dashed line on the right fits the role of a center line. | markings: No markings
                        are present in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This marks the centre of the road; I may cross it to overtake if the
                        road is clear. [[UK-Rule127]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white edge line; while
                        not explicitly prohibited by a 'must not' rule for this specific edge line, it marks
                        the boundary of the carriageway/parking area.
Step 6  change_right    allowed (correct): The right boundary is a broken white center line, which allows
                        crossing if the road is clear according to [UK-Rule127].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to overtake if
                        it is safe to do so, but do not enter the parking area on the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 856, 67.56 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead. There are
                        no immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane on the left. Photo
                        2 confirms a solid white line immediately to the left of the car, extending forward.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane of the same
                        direction. Photo 2 shows a series of short white dashes and gaps immediately to the
                        right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show the words 'BUS LANE' painted in the lane to
                        the left of my lane, not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a special lane line on the left (bus lane) and a lane line
                        on the right. | roles: The solid white line on the left fits the role of a bus lane
                        boundary; the broken white line on the right fits the role of a lane divider. |
                        markings: The 'BUS LANE' text is in the adjacent lane, which is consistent with the
                        solid white boundary separating it from my lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I MUST NOT drive in a cycle or designated lane marked by a solid white
                        line during its times of operation. [[UK-Rule140]]
Step 5  Rule            right_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white boundary of the bus
                        lane [UK-Rule140].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane or move to the right lane if needed. Do not enter the bus
                        lane to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation accepted, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 14577, out 942, 67.67 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-carriageway urban road in the UK, proceeding straight ahead.
                        There are no intersections or ramps immediately visible in the foreground. (lanes 1,
                        mine 1, full)
Step 2  Left            Photo 1 shows a continuous yellow line along the left edge of the road, next to a
                        sidewalk. Photo 2 confirms a single solid yellow line immediately to the left of the
                        car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line to the right of the car; the road surface is open until
                        it meets parked cars and buildings. Photo 2 also shows no painted line on the right
                        side of the lane.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 are
                        consistent with a yellow edge line on the left and no boundary on the right,
                        indicating a narrow single-lane road. | roles: The yellow solid line on the left fits
                        the role of an edge line indicating waiting restrictions. | markings: There are no
                        markings in the lane to contradict the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A single yellow line indicates that waiting is restricted, but loading
                        or unloading may be permitted. [[UK-HC_MARKINGS-p2]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a curb and a solid
                        yellow line; crossing it would mean leaving the carriageway.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: there is no painted line or curb
                        governing the right side of the lane.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict proceeding straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the left boundary into the
                        sidewalk/curb area; be mindful of the yellow line indicating waiting restrictions.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 14577, out 807, 48.7 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving straight ahead. There is a traffic island
                        to the right and parked cars on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from a parking/loading area on
                        the left. Photo 2 shows the same white broken line next to my car, consisting of long
                        dashes and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to a raised concrete traffic island. Photo 2
                        shows the white solid line and the raised curb of the island immediately to the right
                        of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is an edge line marking the boundary of the carriageway available
                        for through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the
                        carriageway available for through traffic other than at a road junction, an exit from
                        a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is an edge line marking the division between the main carriageway
                        and a traffic island. [UK-TSRGD-S11P4-item10] "Diagram 1010 (a) edge of the
                        carriageway at a road junction or a lay-by, or at an exit from a private drive onto a
                        public road; (b) the start of a traffic lane,"
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white line to the right
                        as it is a physical boundary (traffic island).
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14577, out 740, 14.2 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward on a road with multiple lanes
                        of the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line to the left of my car. Photo 2 confirms a broken
                        white line next to my car, consisting of short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my car. Photo 2 confirms a broken
                        white line next to my car, consisting of short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a white circle containing the number '20'
                        painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        lane 2 agree with having lane lines on both the left and right. | roles: The white
                        dashed lines are consistent with the role of lane dividers. | markings: The speed
                        limit marking is a standard informative marking and does not conflict with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            right_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            text:speed_limit: This is an informative marking indicating a speed limit of 20 mph.
                        [null]
Step 6  change_left     allowed (contested, correct): allowed; the left boundary is a broken white lane line
                        [UK-Rule131].
Step 6  change_right    allowed (correct): allowed; the right boundary is a broken white lane line [UK-
                        Rule131].
Step 6  go_straight     allowed (contested, correct): allowed; no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable; there is no waiting area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  Stay in your lane and observe the 20 mph speed limit. You may change lanes if it is
                        safe to do so.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 14577, out 923, 14.85 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street with shops on both sides, proceeding towards a junction.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, which becomes a zig-zag
                        pattern further ahead. Photo 2 shows a white line next to the car that is solid, then
                        transitions into a zig-zag pattern.
                        white zigzag, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the oncoming traffic lane. Photo 2
                        shows this line next to the car as a broken white line with long dashes and gaps.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: I must not park or overtake other vehicles within the zig-zag area.
                        [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to ensure that drivers
                        and pedestrians can see each other clearly. As a driver, you must not park your
                        vehicle anywh"
Step 5  Rule            right_boundary: I may cross this broken white center line to overtake if the road is
                        clear. [UK-Rule127] "A broken white line. This marks the centre of the road. When this
                        line lengthens and the gaps shorten, it means that there is a hazard ahead. Do not
                        cross it un"
Step 6  change_left     prohibited (contested, correct): prohibited by the left edge line and curb
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken white center line [UK-
                        Rule127]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your lane or overtake to the right if safe. Do not stop or park in the zig-zag
                        area on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 14577, out 733, 60.07 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, driving behind a red double-decker bus. The road
                        continues straight ahead with parked vehicles on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows no painted line on the left, only the road surface and the side of the
                        bus. Photo 2 also shows no painted line next to the car.
                        none none, curb no, unknown, evidence full
Step 2  Right           Photo 1 shows a solid yellow line along the right edge of the road, next to the curb.
                        Photo 2 confirms a solid yellow line next to the car, and further ahead it remains a
                        solid yellow line.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 are
                        consistent with the right boundary being an edge line and no left boundary being
                        present. | roles: The solid yellow line on the right fits the role of an edge line
                        indicating waiting restrictions. | markings: There are no markings in the lane to
                        contradict. | unseen: No | result: consistent
Step 5  Rule            right_boundary: A single yellow line indicates that waiting is restricted, but
                        stopping to load or unload may be permitted. [[UK-HC_MARKINGS-p2]]
Step 6  change_left     allowed (correct): no marking governs this action
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid yellow line and a curb;
                        crossing it would mean leaving the carriageway, which is prohibited by the curb.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not drive or park on the right side of the
                        road where the yellow line and curb are located.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_left decided with nothing marked on that side']
Tokens                  in 14577, out 762, 12.5 s
```
