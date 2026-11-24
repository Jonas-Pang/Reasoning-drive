# Reasoning of lane run 20261117_211411_laneB_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction where a red bus is stopped
                        ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the edge of the road next to the pavement. Photo 2
                        confirms a double red line next to the car, extending further ahead.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line dividing the road. Photo 2 shows a series of short
                        white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white bicycle symbol painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a double red edge line on the left and a dashed lane line on the
                        right. | roles: the double red line fits the role of an edge line (Red Route), and the
                        dashed white line fits the role of a lane divider. | markings: the bicycle symbol
                        indicates a cycle lane, which is consistent with the boundary types. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The double red line means no stopping at any time. [[UK-
                        HC_MARKINGS-p2-9]]
Step 5  Rule            right_boundary: The broken white line is a lane divider; I should keep between it and
                        the left boundary. [[UK-Rule131]]
Step 5  Rule            symbol:bike: I should not drive in a cycle lane marked by a broken white line unless
                        it is unavoidable. [[UK-Rule140-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a curb and a
                        double red line [UK-HC_MARKINGS-p2-9].
Step 6  change_right    allowed (WRONG, label prohibited): allowed: the right boundary is a broken white line
                        [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight, although
                        the lane is a cycle lane [UK-Rule140-2].
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently driving in a cycle lane; you should move into the adjacent lane to
                        the right if it is safe to do so. Do not stop or park on the left due to the double
                        red lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation accepted,
                        contradictions []
Tokens                  in 14754, out 972, 16.09 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single carriageway urban road, approaching a junction or a narrowing
                        of the road where traffic is channeled. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line next to the car that becomes a series of short dashes, then
                        further ahead it forms a boundary for a channelized area. Photo 2 shows a white dashed
                        line next to the car.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car, which further ahead curves to the
                        right to form a channelized area. Photo 2 shows a white dashed line next to the car.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 and Photo 2 show a white area with diagonal stripes
                        (chevrons) ahead of the car, creating a channel.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries, as both sides are edge lines (separating the lane from a cycle
                        lane on the left and a shoulder/curb area on the right). | roles: The white dashed
                        pattern fits the role of advisory edge lines in this urban context. | markings: The
                        channelizing area ahead is consistent with the boundaries curving to guide traffic. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: This is an advisory edge line; crossing it is generally discouraged
                        unless safe. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is an advisory edge line; crossing it is generally discouraged
                        unless safe. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 5  Rule            area:channelizing: Since the area is bordered by broken white lines, I should not
                        enter it unless necessary and safe. [UK-Rule130-2] "If the area is bordered by a
                        broken white line, you should not enter the area unless it is necessary and you can
                        see that it is safe to do so."
Step 6  change_left     allowed (contested, label prohibited): allowed; governed by a dashed white edge line
                        [UK-TSRGD-S11P4-item11].
Step 6  change_right    allowed (contested, label prohibited): allowed; governed by a dashed white edge line
                        [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): allowed; no marking prohibits continuing straight
                        through the channel.
Step 6  turn_left       not_applicable: not_applicable; no arrow in my lane governs this movement.
Step 6  turn_right      not_applicable: not_applicable; no arrow in my lane governs this movement.
Step 6  u_turn          not_applicable: not_applicable; no arrow in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and follow the channel created by the chevron markings. Avoid
                        entering the chevron area unless necessary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 1009, 51.65 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on an urban road in the UK, approaching a junction with a pedestrian
                        crossing and a cycle lane ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a solid white line and a raised curb/barrier on the far right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.;
                        symbol:bike (full): Photo 2 shows a white bicycle symbol in a designated area ahead of
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being a lane_line and the right boundary being an
                        edge_line. | roles: The white dashed line fits the role of a lane divider, and the
                        white solid line fits the role of an edge line. | markings: The straight arrow is
                        consistent with the lane's position and the bike symbol indicates a cycle lane ahead.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 5  Rule            symbol:bike: This indicates a cycle lane or route. [[UK-TSRGD-S11P4-item28]]
Step 6  change_left     allowed (correct): allowed: governed by a broken white lane line [UK-Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: governed by a solid white edge line and
                        a physical curb [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (correct): allowed: governed by the straight-ahead arrow [UK-TSRGD-
                        Part6,item20].
Step 6  turn_left       prohibited (correct): prohibited: the straight-ahead arrow prohibits other movements
                        [UK-TSRGD-Part6,item20].
Step 6  turn_right      prohibited (correct): prohibited: the straight-ahead arrow prohibits other movements
                        [UK-TSRGD-Part6,item20].
Step 6  u_turn          prohibited (correct): prohibited: the straight-ahead arrow prohibits other movements
                        [UK-TSRGD-Part6,item20].
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight ahead. Do not enter the cycle lane marked with
                        the bicycle symbol ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14754, out 1112, 54.75 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-carriageway urban road with shops and houses on the sides. The
                        road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid yellow lines running along the left edge of the road. Photo 2
                        confirms two solid yellow lines next to the car and continuing ahead.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the opposing traffic. Photo
                        2 shows a series of short white dashes and gaps next to the car.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [[UK-
                        HC_MARKINGS-p2-2]]
Step 5  Rule            right_boundary: A broken white line marks the centre of the road; it may be crossed to
                        overtake if the road is clear. [[UK-Rule127]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a curb and double
                        yellow lines which mark the edge of the carriageway.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white center line which
                        allows crossing for overtaking if safe.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to overtake if
                        it is safe to do so, but do not stop or park on the left due to the double yellow
                        lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 809, 49.02 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a junction with a pedestrian
                        crossing ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, which becomes a zig-zag
                        pattern as it approaches the crossing. Photo 2 shows the white line next to the car is
                        a solid line, and further ahead it transitions into a zig-zag pattern.
                        white zigzag, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line along the right edge of the road, which also becomes a zig-
                        zag pattern as it approaches the crossing. Photo 2 shows the white line next to the
                        car is a solid line, and further ahead it transitions into a zig-zag pattern.
                        white zigzag, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a zebra crossing (white stripes)
                        across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: I must not park or overtake other vehicles within the zig-zag area.
                        [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to ensure that drivers
                        and pedestrians can see each other clearly. As a driver, you must not park your
                        vehicle anywh"
Step 5  Rule            right_boundary: I must not park or overtake other vehicles within the zig-zag area.
                        [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to ensure that drivers
                        and pedestrians can see each other clearly. As a driver, you must not park your
                        vehicle anywh"
Step 5  Rule            line:crosswalk: I must not park on the crossing and must not overtake vehicles stopped
                        for pedestrians. [UK-Rule191] "You MUST NOT park on a crossing or in the area covered
                        by the zig-zag lines. You MUST NOT overtake the moving vehicle nearest the crossing or
                        the vehicle neares"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is an edge line with a
                        raised curb, and the zig-zag markings prohibit overtaking/crossing into the pedestrian
                        area.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is an edge line with a
                        raised curb, and the zig-zag markings prohibit overtaking/crossing into the pedestrian
                        area.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits continuing straight
                        through the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be prepared to stop for pedestrians at the
                        zebra crossing; do not overtake any vehicles stopped at the crossing.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 941, 14.59 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, traveling straight ahead. There are
                        no intersections or ramps immediately visible. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid red lines running along the left edge of the road next to the
                        curb. Photo 2 confirms two solid red lines immediately next to the car and continuing
                        ahead.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from a parking/stopping area on
                        the right. Photo 2 shows a series of short white dashes and gaps immediately to the
                        right of the car.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double red lines mean no stopping at any time. [[UK-HC_MARKINGS-p2-9]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a double red line
                        and a curb, and [UK-HC_MARKINGS-p2-9] prohibits stopping/parking there; crossing a
                        curb is generally prohibited.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which is an
                        advisory edge line [UK-TSRGD-S11P4-item11] and does not prohibit crossing if safe.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop or park on the left due to the
                        double red lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 845, 13.94 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead. There are
                        no immediate intersections or ramps visible in the foreground. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the road from a blue-painted cycle lane.
                        Photo 2 confirms a single solid white line next to the car, continuing straight ahead.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of short white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 1 shows white text 'A22' and 'A3' painted in the lane further
                        ahead. Photo 2 also shows these route numbers.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 1
                        are consistent with having a special lane line on the left and a lane line on the
                        right. | roles: The solid white line on the left correctly identifies the boundary of
                        a cycle lane, and the dashed white line on the right correctly identifies a lane
                        divider. | markings: The route numbers (A22, A3) are informative and do not contradict
                        the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles must not be driven in the cycle lane during its hours of
                        operation. [[UK-TSRGD-12(2)]]
Step 5  Rule            right_boundary: Lane dividers are used to divide wide carriageways into lanes; you
                        should keep between them. [[UK-Rule131]]
Step 5  Rule            text:other: Route numbers are informative and do not restrict movement.
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line boundary of the
                        cycle lane [UK-TSRGD-12(2)].
Step 6  change_right    allowed (correct): allowed by the dashed white lane divider [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting in area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking
                        governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right if needed. Do not enter the blue cycle lane to
                        your left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 14754, out 981, 51.75 s

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
                        lane 1 are consistent with having a special lane (cycle lane) on the left and another
                        traffic lane on the right. | roles: The white dashed lines fit the roles of a cycle
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
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the left-most traffic lane. You may proceed straight or change lanes to the
                        right. Be cautious of cyclists in the cycle lane to your left before crossing into it.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 870, 11.4 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, approaching a zebra crossing with a
                        pedestrian currently crossing. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, which becomes zig-zagged
                        as it approaches the crossing. Photo 2 shows the line next to the car is a solid white
                        line, and further ahead it transitions into zig-zag markings.
                        white zigzag, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the opposite direction of traffic.
                        Photo 2 shows this line next to the car is a broken white line.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a zebra crossing (broad white stripes)
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: You must not park or overtake within the zig-zag area before the
                        crossing. [[UK-KYTS-zigzag]]
Step 5  Rule            right_boundary: This marks the centre of the road; do not cross it unless the road is
                        clear and you wish to overtake or turn off. [[UK-Rule127]]
Step 5  Rule            line:crosswalk: This is a pedestrian crossing where pedestrians have priority. [[UK-
                        HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is an edge line with a
                        raised curb.
Step 6  change_right    allowed (contested, label prohibited): allowed: the right boundary is a broken white
                        center line, which allows crossing if safe [UK-Rule127].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Proceed straight with caution and stop for the pedestrian crossing the road. Do not
                        overtake any vehicles within the zig-zag markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 899, 50.88 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, traveling straight ahead. There are
                        no immediate intersections or ramps visible in the foreground. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with short dashes and short gaps.
                        white dotted, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with short dashes and short gaps.
                        white dotted, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle with the number '20'
                        painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and index 1 are
                        consistent with the boundaries; the left boundary is a special lane line (cycle lane)
                        and the right is a lane line dividing from another lane of the same direction. |
                        roles: The white dotted patterns are consistent with lane dividers and cycle lane
                        boundaries in the UK. | markings: The speed limit marking is a standard informative
                        marking and does not contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: You should not drive or park in a cycle lane marked by a broken white
                        line unless it is unavoidable. [[UK-Rule140-2]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            text:speed_limit: This is an informative marking indicating the speed limit. [null]
Step 6  change_left     prohibited (contested, correct): prohibited; the left boundary is a cycle lane and
                        [UK-Rule140-2] restricts entry unless unavoidable.
Step 6  change_right    allowed (correct): allowed; the right boundary is a broken lane line and [UK-Rule131]
                        allows keeping between them but does not prohibit changing lanes if safe.
Step 6  go_straight     allowed (contested, correct): allowed; no marking prohibits continuing straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable; no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable; no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and observe the 20 mph speed limit. Do not enter the cycle lane to
                        your left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions ['rightmost
                        lane, but a lane line on the right']
Tokens                  in 14754, out 977, 51.96 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test B | gemma4:31b | from cache
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, facing straight ahead. There is a junction or
                        intersection further ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which then becomes a broken white
                        line further ahead. Photo 2 confirms the solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line. Photo 2 shows a broken white line with several
                        dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 and Photo 2 show a white arrow in the lane that points
                        straight and then turns left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 are
                        consistent with a left edge line and a right lane line, as there is another lane to
                        the right. | roles: The white solid line on the left acts as an edge line, and the
                        white dashed line on the right acts as a lane divider. | markings: The left-turn arrow
                        is consistent with the lane's position. | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is a lane divider; I should keep between the lane dividers. [UK-
                        Rule131] "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:left: Vehicular traffic must turn left. [UK-TSRGD-Part6,item19] "Vehicular
                        traffic must turn left"
Step 6  change_left     prohibited (contested, label allowed): prohibited: the left boundary is a solid white
                        edge line, and crossing it would leave the carriageway.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line, which
                        allows lane changes if safe.
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited: the arrow in the lane only allows a
                        left turn.
Step 6  turn_left       allowed (correct): allowed: the arrow in the lane indicates a left turn.
Step 6  turn_right      prohibited (correct): prohibited: the arrow in the lane only allows a left turn.
Step 6  u_turn          allowed (WRONG, label prohibited): allowed: a left-turn arrow in a left-keep system
                        allows a U-turn unless prohibited by other markings.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a left-turn lane. You must turn left at the end of the lane; if you wish to
                        go straight or turn right, you must change to the lane on your right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:straight_left']), actions False, unsafe ['u_turn'],
                        citation accepted, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 14754, out 967, 45.16 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road in the UK, traveling straight ahead. There are no
                        intersections or ramps immediately in view. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with long dashes and gaps.
                        white dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, and further ahead it remains a
                        white broken line. Photo 2 shows a white broken line with short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 are
                        consistent with the left boundary being a center line and the right boundary being a
                        lane line (indicating another lane of the same direction to the right). | roles: The
                        white dashed pattern fits both the center line and lane line roles in this context. |
                        markings: No markings were found in the lane, which is consistent with the boundaries.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: I may cross this broken white center line to overtake or turn off if
                        the road is clear. [[UK-Rule127]]
Step 5  Rule            right_boundary: I should keep between these lane divider lines. [[UK-Rule131]]
Step 6  change_left     allowed (correct): allowed by the broken white center line [UK-Rule127].
Step 6  change_right    allowed (correct): allowed by the broken white lane divider [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking
                        governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to proceed straight or change lanes to the left or
                        right. Be mindful of the cyclist ahead in your lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 14754, out 849, 15.39 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with a pedestrian crossing
                        and a small traffic island ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows two solid red lines along the left edge of the road. Photo 2 confirms
                        two solid red lines next to the car, continuing further ahead.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line dividing the two lanes. Photo 2 shows a short broken
                        white line (one dash and one gap) next to the car, continuing as a dashed line further
                        ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left_right (full): Photo 2 shows a white arrow pointing both straight and left
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the left boundary being an edge line and the right boundary being a
                        lane line. | roles: the double red edge line and broken white lane line fit their
                        roles. | markings: the straight-and-left arrow is consistent with the lane's position.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double red lines mean no stopping at any time. [[UK-HC_MARKINGS-p2-9]]
Step 5  Rule            right_boundary: Short broken white lines divide lanes; I should keep between them.
                        [[UK-Rule131]]
Step 5  Rule            arrow:left_right: The arrow indicates that both going straight and turning left are
                        possible movements. [[UK-HC_MARKINGS-p3-6]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double red edge line and curb [UK-
                        HC_MARKINGS-p2-9].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [UK-Rule131].
Step 6  go_straight     allowed (correct): allowed by the arrow in my lane [UK-HC_MARKINGS-p3-6].
Step 6  turn_left       allowed (correct): allowed by the arrow in my lane [UK-HC_MARKINGS-p3-6].
Step 6  turn_right      prohibited (correct): prohibited by the arrow in my lane which only shows straight and
                        left [UK-HC_MARKINGS-p3-6].
Step 6  u_turn          allowed (WRONG, label prohibited): allowed as the arrow allows a turn toward opposite
                        traffic (left turn) [UK-HC_MARKINGS-p3-6].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may proceed straight or turn left. Do not stop or park
                        on the left due to the double red lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left_right'], missed ['arrow:straight_left']), actions False, unsafe
                        ['u_turn'], citation accepted, contradictions ['go_straight allowed although no arrow
                        shows it', 'turn_right prohibited although an arrow shows it']
Tokens                  in 14754, out 986, 15.28 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-carriageway urban road in the UK, facing forward. The road
                        ahead is a straight stretch with buildings on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, which is solid next to the
                        car and becomes a zigzag pattern further ahead. Photo 2 confirms the line next to the
                        car is a solid white line.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line along the right edge of the road, which is solid next to
                        the car and becomes a zigzag pattern further ahead. Photo 2 confirms the line next to
                        the car is a solid white line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show white zigzag lines across the lane
                        further ahead, indicating a pedestrian crossing area.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and ego_lane_index 1
                        agree with the presence of edge lines on both sides | roles: the white solid lines on
                        both sides fit the role of edge lines for a single-lane road | markings: the zigzag
                        lines are consistent with a pedestrian crossing area in the UK | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            line:crosswalk: You must not park or overtake within the zig-zag area before the
                        crossing. [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to ensure that
                        drivers and pedestrians can see each other clearly. As a driver, you must not park
                        your vehicle anywh"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid edge line
                        with a raised curb, and there is no lane to change into.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid edge line
                        with a raised curb, and there is no lane to change into.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs a left turn at the end of
                        the visible stretch.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs a right turn at the end of
                        the visible stretch.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not overtake or park within the zig-zag
                        markings ahead of the pedestrian crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 1001, 52.51 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction with traffic
                        signals. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a curb and double red lines along the left edge of the road. Photo 2
                        confirms the presence of a raised curb and two solid red lines running parallel to the
                        lane.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the next lane. Photo 2 shows
                        a series of short white dashes and gaps immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 both show a white arrow pointing straight
                        ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double red lines mean no stopping at any time. [[UK-HC_MARKINGS-p2-9]]
Step 5  Rule            right_boundary: Broken white lane dividers are used to divide lanes; you should keep
                        between them. [[UK-Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double red edge line and curb [UK-
                        HC_MARKINGS-p2-9].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [UK-Rule131].
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited by the straight-ahead arrow [UK-TSRGD-
                        Part6,item20].
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. Do not stop or park on the left due to the double
                        red lines. If you need to turn, change to the right lanes.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 14754, out 924, 50.56 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching a pedestrian crossing and a
                        junction ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road. Photo 2 confirms a
                        single solid white line next to the car, continuing ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line along the right edge of the road. Photo 2 confirms a
                        single solid white line next to the car, continuing ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show white zebra stripes across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            line:crosswalk: Drivers must not park in the zig-zag area or overtake vehicles stopped
                        for pedestrians at the crossing. [UK-KYTS-zigzag] "The zig-zag markings at crossings
                        are there to ensure that drivers and pedestrians can see each other clearly. As a
                        driver, you must not park your vehicle anywh"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white edge
                        line with a curb, and no rule permits crossing it.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line with a curb, and no rule permits crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits continuing straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be prepared to stop for pedestrians at the
                        zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 894, 15.72 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with multiple lanes. Ahead is a straight stretch of road
                        with buses in the adjacent lane. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a single solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a red line along the edge of the road next to the sidewalk. Photo 2
                        shows a single solid red line next to my car.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is a lane divider; I should keep between the lane markings. [UK-
                        TSRGD-S11P4-item4] "Diagram 1005 Division of carriageway into traffic lanes on part of
                        the carriageway where vehicles normally proceed in the same direction other than at
                        places wh"
Step 5  Rule            right_boundary: The red line indicates that stopping to park, load/unload or to board
                        and alight is prohibited. [UK-HC_MARKINGS-p2-8] "The double and single red lines used
                        on Red Routes indicate that stopping to park, load/unload or to board and alight from
                        a vehicle (except for a licensed taxi"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white line,
                        and the adjacent lane is a bus lane (indicated by 'BUS LANE' text in that lane), which
                        is restricted under UK-Rule141-2.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid red line
                        and a curb, and the area beyond is a sidewalk.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight in my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Do not enter the bus lane to your left
                        or stop along the red line on your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 811, 12.66 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on an urban road in the UK, traveling straight ahead. There is a bus
                        stopped in a lane to the left and other vehicles ahead in the same direction. (lanes
                        2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        confirms this is a single solid white line next to my car and continues as a solid
                        white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a grey curb and a metal railing on the right side of the road. Photo 2
                        shows the raised grey curb immediately to the right of my lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and a curb on the right. | roles:
                        The solid white line on the left fits the role of a lane divider, and the curb on the
                        right fits the role of the roadway edge. | markings: No markings were observed in my
                        lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid white lane line generally prohibits crossing unless permitted
                        by other rules; however, no specific mandatory prohibition for this exact line type is
                        provided in the snippets other than general lane keeping. [null]
Step 5  Rule            right_boundary: The curb marks the edge of the carriageway and prohibits leaving the
                        road. [null]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white line,
                        and without a permissive rule, crossing a solid line is prohibited.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a raised curb.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action, and it is the
                        default movement of the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Do not cross the solid white line to
                        the left or drive onto the curb to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 14754, out 884, 51.0 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with a
                        traffic signal ahead. (lanes 2, mine 1, full)
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
                        straight-ahead arrow is consistent with the lane's position and boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This is a lane divider; I should keep between the lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid white edge
                        line, and crossing it would leave the carriageway.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line, which
                        allows lane changes when safe.
Step 6  go_straight     allowed (correct): allowed: the arrow in my lane indicates that I must proceed ahead.
Step 6  turn_left       prohibited (correct): prohibited: the arrow in my lane only allows proceeding straight
                        ahead.
Step 6  turn_right      prohibited (correct): prohibited: the arrow in my lane only allows proceeding straight
                        ahead.
Step 6  u_turn          prohibited (correct): prohibited: the arrow in my lane only allows proceeding straight
                        ahead.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed, but do
                        not cross the solid line on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 959, 51.24 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction with traffic
                        lights ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the left lane. Photo 2
                        confirms a broken white line with short dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right lane. Photo 2
                        confirms a broken white line with short dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right. |
                        roles: The white dashed lines are consistent with the role of lane dividers. |
                        markings: The straight-ahead arrow is consistent with being in the middle lane of a
                        three-lane road. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            right_boundary: I should keep between the lane dividers. [[UK-Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 6  change_left     allowed (correct): allowed by the broken white line [UK-Rule131]
Step 6  change_right    allowed (correct): allowed by the broken white line [UK-Rule131]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [UK-TSRGD-Part6,item20]
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [UK-TSRGD-Part6,item20]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, you must change
                        lanes first, as this lane is for straight-ahead traffic only.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 935, 16.4 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, proceeding straight ahead. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        confirms a solid white line immediately to the left of the car, continuing straight
                        ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right, separating my lane from a cycle lane
                        or shoulder. Photo 2 shows a series of short white dashes and gaps immediately to the
                        right of the car.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white solid line as a lane divider and white dashed line as an edge/cycle
                        lane boundary are consistent with UK road markings. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: This is a lane divider; I should keep between the lane markings. [UK-
                        TSRGD-S11P4-item4] "Diagram 1005 Division of carriageway into traffic lanes on part of
                        the carriageway where vehicles normally proceed in the same direction other than at
                        places wh"
Step 5  Rule            right_boundary: This indicates a cycle lane; I should not cross or straddle the line
                        unless it is safe to do so and the lane is clear of cyclists. [UK-TSRGD-S11P4-item2]
                        "Diagram 1004 Vehicular traffic should not cross or straddle the line unless it is
                        safe to do so and when the line is used to indicate a cycle lane, motor vehicl"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white line,
                        and while UK-TSRGD-S11P4-item4 is informative, a solid lane line generally prohibits
                        crossing unless specifically permitted; however, based on the provided rules, there is
                        no permissive rule for crossing a solid lane line here.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which according
                        to UK-TSRGD-S11P4-item2 allows crossing if safe and clear of cyclists.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action, and there is no
                        restriction to proceeding straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may move right into the cycle lane only if
                        it is safe and clear of cyclists.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 955, 15.39 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street with shops on both sides. The road ahead is a straight
                        stretch with no immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road. Photo 2 confirms a
                        double solid yellow line next to the car, continuing as a solid line further ahead.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, only the edge of the road. Photo 2 shows
                        no painted line next to the car, just the asphalt meeting the curb area.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [[UK-
                        HC_MARKINGS-p2-2]]
Step 5  Rule            right_boundary: No specific rule for a boundary with no paint and a curb; it marks the
                        edge of the roadway. [null]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a curb and a double
                        yellow line, and there is no lane to change into.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a curb, and there
                        is no lane to change into.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop or park on the left side due to
                        the double yellow lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 14754, out 784, 49.65 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead. The road is
                        lined with buildings on the left and trees on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line dividing my lane from the lane to the left. Photo 2
                        shows the same broken white line next to my car, consisting of short white dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, separating the road from a
                        parking/shoulder area. Photo 2 shows this solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right. | roles: The
                        broken white line fits the role of a lane divider, and the solid white line fits the
                        role of an edge line. | markings: No markings are present in the lane, which is
                        consistent with the boundaries. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a broken white
                        line [UK-Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line [UK-TSRGD-S11P4-item11].
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
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the solid white line on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 894, 46.74 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on both sides. The road ahead appears to be
                        a single carriageway with parked cars and oncoming traffic. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line along the left edge of the road next to the pavement.
                        Photo 2 confirms a single yellow line next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line between my lane and the oncoming traffic; the road
                        surface is wet and reflective. Photo 2 also shows no painted line to the right of my
                        car.
                        none none, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the left edge line and the right center line role. | roles: The yellow edge line
                        on the left fits the role of a boundary between the carriageway and the
                        pavement/parking area. The absence of a line on the right is consistent with a simple
                        city street center. | markings: No markings were observed in the lane. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: A single yellow line indicates that waiting is restricted, but stopping
                        to load or unload may be permitted. [[UK-HC_MARKINGS-p2]]
Step 5  Rule            right_boundary: No specific rule for a non-existent line; the driver must simply keep
                        to the left of the road. [null]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a curb/edge line,
                        and crossing it would mean leaving the carriageway.
Step 6  change_right    prohibited: prohibited: changing right would move the car into the path of oncoming
                        traffic on a single carriageway.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits continuing straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be mindful of the oncoming traffic and the
                        parked cars on the left.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 14754, out 857, 50.9 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction where a bus lane is
                        located to the left. (lanes 2, mine 2, full)
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
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a broken white
                        line [UK-Rule131].
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line [UK-
                        TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane. You may proceed straight or change lanes if safe; be
                        aware that the lane to your left is a designated bus lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 14754, out 941, 50.64 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, facing a red bus ahead. The road is a single
                        carriageway with parking on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line next to the car, which becomes a solid white line
                        further ahead near the intersection. Photo 2 shows the white dashed line next to the
                        car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line next to the car, which becomes a solid white line
                        further ahead. Photo 2 shows the white dashed line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show a yellow criss-cross box area across the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and index 1 agree
                        with the boundaries, as the dashed lines separate the driving lane from
                        parking/service areas. | roles: The white dashed lines fit the role of lane
                        dividers/dividing the carriageway. | markings: The yellow box junction is a standard
                        marking for this type of urban road. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            right_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            area:grid: I must not enter the box junction if I will have to stop within it due to
                        stationary vehicles. [[UK-TSRGD-11(1)]]
Step 6  change_left     allowed (contested, label prohibited): allowed; governed by a broken white line [UK-
                        Rule131].
Step 6  change_right    allowed (correct): allowed; governed by a broken white line [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed; no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable; no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable; no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable; no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change lanes if safe. Do not enter the yellow box junction
                        unless your exit is clear.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['leftmost lane, but a
                        lane line on the left', 'rightmost lane, but a lane line on the right']
Tokens                  in 14754, out 941, 38.64 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with buildings on both sides. A red bus is ahead in
                        the opposite direction, and several cars are parked on the right side of the road.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from a cycle lane. Photo 2 shows
                        the same white broken line next to my car, with a bicycle symbol painted to its left.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows the edge of the road on the right, where cars are parked. Photo 2 shows
                        a solid white line further ahead, but next to the car, there is no painted line, only
                        the edge of the carriageway near the parked cars.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should not drive in the cycle lane marked by a broken white line
                        unless it is unavoidable. [[UK-Rule140-2]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken white line [UK-
                        Rule140-2], provided it is unavoidable or safe to do so to avoid an accident or enter
                        premises.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited as there is no lane to the right, only
                        the edge of the carriageway and parked cars.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along my lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Avoid entering the cycle lane to your left
                        unless necessary.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 840, 49.64 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with a pedestrian crossing
                        and traffic signals ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line along the left edge of the road. Photo 2 confirms a
                        single solid white line next to the car, continuing ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a central island/refuge.
                        Photo 2 shows a single solid white line next to the car, which then forms a triangle-
                        shaped area further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): Photo 1 and Photo 2 show white zig-zag lines on both sides of the
                        lane approaching the junction.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is the boundary between the main carriageway and a traffic lane
                        or island. [UK-TSRGD-S11P4-item10] "Diagram 1010 (a) edge of the carriageway at a road
                        junction or a lay-by, or at an exit from a private drive onto a public road; (b) the
                        start of a traffic lane,"
Step 5  Rule            symbol:other: You must not park or overtake within the zig-zag area before the
                        crossing. [UK-KYTS-zigzag] "The zig-zag markings at crossings are there to ensure that
                        drivers and pedestrians can see each other clearly. As a driver, you must not park
                        your vehicle anywh"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white edge
                        line with a curb, and there is no rule allowing crossing it.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white line
                        with a curb/island, and there is no rule allowing crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not park or overtake other vehicles within
                        the zig-zag markings ahead of the crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 909, 16.73 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with shops on both sides, proceeding straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a parking area with cars.
                        Photo 2 confirms a single solid white line next to the car, extending forward.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating the lane from the opposite direction of
                        traffic. Photo 2 shows a series of short white dashes and gaps next to the car.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This marks the centre of the road; I should not cross it unless the
                        road is clear and I wish to overtake or turn off. [[UK-Rule127]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white edge
                        line, and there is no rule permitting crossing it into the parking area here.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white center line, which
                        allows crossing if the road is clear [UK-Rule127].
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to overtake if
                        it is safe to do so, but do not cross the solid white line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 826, 14.83 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with shops on the left. Ahead is a straight stretch of road
                        with a vehicle in front. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and double yellow lines along the left edge of the road.
                        Photo 2 confirms the raised curb and the double yellow lines next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a short broken white line next to the car, with a gap and a dash visible.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane.;
                        symbol:bike (full): Photo 2 shows a white bicycle symbol painted in my lane, ahead of
                        the arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 1 agree with having an edge line on the left and a lane line on the right. |
                        roles: The yellow edge line and white dashed lane line fit their respective roles. |
                        markings: The straight arrow and bike symbol are consistent with a through-lane that
                        may be shared with cyclists. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [[UK-
                        HC_MARKINGS-p2-2]]
Step 5  Rule            right_boundary: Short, broken white lines divide lanes; I should keep between them.
                        [[UK-Rule131]]
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [[UK-TSRGD-Part6,item20]]
Step 5  Rule            symbol:bike: This indicates a cycle lane or route. [[UK-TSRGD-S11P4-item28]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a raised curb and
                        double yellow lines, and the curb physically prevents leaving the roadway.
Step 6  change_right    allowed (contested, correct): allowed: the right boundary is a broken white line,
                        which allows lane changes if safe.
Step 6  go_straight     allowed (correct): allowed: the arrow in my lane indicates proceeding ahead.
Step 6  turn_left       prohibited (correct): prohibited: the arrow in my lane only allows proceeding
                        straight.
Step 6  turn_right      prohibited (correct): prohibited: the arrow in my lane only allows proceeding
                        straight.
Step 6  u_turn          prohibited (correct): prohibited: the arrow in my lane only allows proceeding
                        straight.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may change to the right lane if necessary,
                        but do not stop or park on the left due to the double yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 14754, out 1054, 54.36 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction where a bus is
                        stopped ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line dividing my lane from the lane to the left. Photo 2
                        shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which separates the road from the
                        pavement. Photo 2 shows this solid white line next to my car, and further ahead it
                        remains solid.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position in
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a lane divider, and the white solid line
                        fits the role of an edge line. | markings: There are no markings in my lane to
                        contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [UK-Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line and there is a curb.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 858, 49.8 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides, proceeding straight ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line dividing the road into two lanes. Photo 2 shows the
                        same broken white line next to the car, consisting of several short white dashes and
                        gaps of similar length.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line at the edge of the road, which becomes a red line
                        closer to the curb. Photo 2 shows a solid white line next to the car, and further
                        right, a red line along the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right | roles: the
                        white dashed line fits the role of a lane_line and the white solid line fits the role
                        of an edge_line | markings: no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [UK-Rule131]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line and there is a curb [UK-TSRGD-S11P4-item11]
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane if
                        safe to do so; do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 884, 15.53 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, proceeding straight ahead toward a
                        distant intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line dividing my lane from the lane to the left. Photo 2
                        shows the same broken white line next to my car, consisting of long white dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a raised curb and a metal
                        railing. Photo 2 shows the solid white line next to my car and the raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 1 and Photo 2 show a white circle with the number '20'
                        painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The broken white line fits the role of a lane divider, and the solid white line
                        next to a curb fits the role of an edge line. | markings: The speed limit marking is
                        consistent with a standard urban lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            text:speed_limit: This indicates a speed limit of 20 mph. [null]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [UK-Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        line and a raised curb [UK-TSRGD-S11P4-item11].
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
Advice                  Stay in your lane or change to the left lane if needed. Observe the 20 mph speed limit
                        indicated on the road.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:speed_limit'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 14754, out 976, 17.2 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, facing straight ahead. The road
                        continues forward with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a grey curb separating the road from the sidewalk. Photo 2 confirms a
                        raised grey curb and a thin white line painted along the edge of the curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from a parking area/shoulder.
                        Photo 2 shows a series of short white dashes with gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This is the boundary between the main carriageway and a parking area
                        or shoulder. [[UK-TSRGD-S11P4-item10]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a raised curb and
                        solid edge line.
Step 6  change_right    allowed (correct): allowed: the right boundary is a dashed white line, which is
                        permissive for entering the shoulder/parking area if safe.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits continuing straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection marking governs this
                        movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection marking governs this
                        movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may move to the right to park or pull over
                        if safe to do so.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 791, 12.83 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-carriageway urban road with shops on both sides, proceeding
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a line of white paint along the left edge of the road.
                        Photo 2 shows the raised curb and a broken white line next to the car, consisting of
                        short dashes and gaps.
                        white dashed, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a wide area of asphalt to the right with parked cars and no painted
                        lines. Photo 2 shows no painted lines to the right of the car.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left edge line and the absence of a right lane line | roles: the white dashed
                        line on the left fits the role of an edge line for a cycle lane or roadway edge |
                        markings: no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: Do not drive or park in a cycle lane marked by a broken white line
                        unless it is unavoidable. [[UK-Rule140-2]]
Step 5  Rule            right_boundary: No marking governs this boundary. [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the left boundary (broken white line
                        indicating a cycle lane) per [UK-Rule140-2]
Step 6  change_right    allowed (correct): allowed as there is no marking or curb governing this action
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane restricting
                        it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking
                        governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the cycle lane on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 14754, out 827, 50.04 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides. The road ahead is straight
                        with no immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a parking/loading area where
                        cars are stopped. Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a cycle lane. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This is the boundary of a cycle lane. [[UK-TSRGD-S11P4-item28]]
Step 5  Rule            right_boundary: You MUST NOT drive or park in a cycle lane marked by a solid white
                        line during its times of operation. [[UK-Rule140]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white edge
                        line and there is no permissive rule to cross it into the parking area here.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        line marking a cycle lane, and [UK-Rule140] prohibits driving in it.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the cycle lane to your right or
                        the parking area to your left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 870, 47.05 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on the left and trees on the right. Ahead is
                        a straight stretch of road with a bus lane to the left. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane. Photo 2 confirms
                        a single solid white line next to my car and continuing ahead.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line on the right. Photo 2 shows a series of short white
                        dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a lane line on the right indicates another lane of my
                        direction to the right, and a special lane line on the left indicates a bus lane. |
                        roles: the white solid line on the left fits the role of a bus lane boundary, and the
                        white dashed line on the right fits the role of a lane divider. | markings: no
                        markings are present in my lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a bus lane. [[UK-TSRGD-Part6,item11]]
Step 5  Rule            left_boundary: Driving in a cycle or special lane marked by a solid white line is
                        prohibited during its times of operation. [[UK-Rule140]]
Step 5  Rule            right_boundary: Lane dividers are short, broken white lines; you should keep between
                        them. [[UK-Rule131]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white line boundary of the
                        bus lane [UK-Rule140].
Step 6  change_right    allowed (correct): allowed by the broken white lane divider [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Do not enter the bus lane to
                        the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 14754, out 925, 15.37 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road in the UK. The road ahead is straight with no
                        immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a grey raised curb and a white line running along the edge of the road.
                        Photo 2 confirms the white line is a solid line next to the curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white zig-zag line on the right side of the lane. Photo 2 shows the
                        zig-zag pattern clearly, consisting of diagonal segments.
                        white zigzag, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: You must not park or overtake within the zig-zag area before a
                        crossing. [[UK-KYTS-zigzag]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid edge line
                        with a curb, and there is no lane to the left.
Step 6  change_right    allowed (contested, label prohibited): allowed: the right boundary is a zig-zag line
                        which is an advisory edge marking, but overtaking is prohibited by [UK-KYTS-zigzag].
                        However, as a boundary for lane change, it is not a solid mandatory line.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not park or overtake other vehicles in the
                        zig-zag area on the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 803, 36.83 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a junction with a traffic
                        signal ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of short dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a raised curb and metal railing. Photo 2
                        confirms a solid white line and a raised curb immediately to the right of my lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2 shows a white arrow pointing right in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            arrow:merge_right: The arrow indicates the possible traffic movement at the end of the
                        lane. [[UK-TSRGD-Part6,item12]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [UK-Rule131].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white line
                        and a raised curb [UK-TSRGD-S11P4-item11].
Step 6  go_straight     prohibited (correct): prohibited: the lane arrow only shows a right turn [UK-TSRGD-
                        Part6,item12].
Step 6  turn_left       prohibited (correct): prohibited: the lane arrow only shows a right turn [UK-TSRGD-
                        Part6,item12].
Step 6  turn_right      allowed (correct): allowed: the lane arrow shows a right turn [UK-TSRGD-Part6,item12].
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited: the lane arrow only shows a right turn
                        [UK-TSRGD-Part6,item12].
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a right-turn only lane. If you wish to go straight or turn left, you must
                        change to the left lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:right']), actions False, unsafe [], citation
                        accepted, contradictions ['go_straight, turn_left, turn_right, u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 14754, out 950, 50.06 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead. There are
                        no immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane on the left. Photo
                        2 confirms a single solid white line immediately to the left of the car, extending
                        forward.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane of the same
                        direction. Photo 2 shows a single white dash and gap immediately to the right of the
                        car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show the words 'BUS LANE' painted in the lane to
                        the left of my lane, not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a special lane line on the left (bus lane) and a lane line
                        on the right. | roles: The solid white line on the left fits the role of a bus lane
                        boundary; the broken white line on the right fits the role of a lane divider. |
                        markings: The 'BUS LANE' text is in the adjacent lane, which is consistent with the
                        solid white boundary of my lane. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a bus lane. [[UK-TSRGD-Part6,item11]]
Step 5  Rule            right_boundary: Lane dividers are short, broken white lines; you should keep between
                        them. [[UK-Rule131]]
Step 5  Rule            text:bus: The marking indicates a bus lane in the adjacent lane. [[UK-Rule141]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white line
                        marking a bus lane, and [UK-Rule141-2] states you should not drive in a bus lane
                        during its period of operation.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which [UK-
                        Rule131] allows as a lane divider.
Step 6  go_straight     allowed (contested, correct): allowed: no marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane or change to the right. Do not enter the bus lane to your
                        left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation accepted, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 14754, out 1029, 54.14 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, looking straight ahead. The road is
                        a single carriageway with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road. Photo 2 confirms a
                        single solid yellow line next to the car and continuing ahead.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, only parked cars and a curb. Photo 2
                        confirms there is no painted line next to the car on the right.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the word 'BUS' painted in yellow in the lane. Photo 1
                        shows this is part of a bus lane marking.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single yellow line indicates that waiting is restricted, but
                        loading/unloading may be allowed. [UK-HC_MARKINGS-p2] "Waiting restrictions indicated
                        by yellow lines apply to the carriageway, pavement and verge. You may stop to load or
                        unload (unless there are also loading restr"
Step 5  Rule            right_boundary: No painted line is present; the curb defines the edge of the roadway.
Step 5  Rule            text:bus: You should not drive in a bus lane during its period of operation. [UK-
                        Rule141-2] "Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation."
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid yellow line
                        and a curb, and it is a bus lane boundary.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a curb.
Step 6  go_straight     allowed (contested, correct): allowed: nothing restricts carrying on straight along
                        the lane, although it is a bus lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently driving in a bus lane; check signs for its hours of operation. Do
                        not park or stop on the left where the yellow line is present.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 898, 16.4 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with shops on both sides, proceeding straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a parking area with cars.
                        Photo 2 confirms a single solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line in the center of the road. Photo 2 shows a series of
                        white dashes and gaps next to my car.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This marks the centre of the road; I should not cross it unless I can
                        see the road is clear and wish to overtake or turn off. [[UK-Rule127]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white edge
                        line, and there is no rule permitting crossing it into the parking area here.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white center line, which
                        allows crossing if the road is clear [UK-Rule127].
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the center line to overtake if
                        it is safe to do so, but do not cross the solid white line on the left into the
                        parking area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 825, 14.26 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, traveling straight ahead. There are
                        no immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane on the left. Photo
                        2 confirms this solid white line next to the car and extending forward.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right. Photo 2 shows a series of short white
                        dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show the words 'BUS LANE' painted in the lane to
                        the left of my lane, not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the right and a special lane line on the
                        left. | roles: The solid white line on the left fits the role of a bus lane boundary;
                        the broken white line on the right fits the role of a lane divider. | markings: The
                        'BUS LANE' text is in the adjacent lane, which is consistent with the solid white
                        boundary of that special lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is the boundary of a bus lane. [[UK-TSRGD-Part6,item11]]
Step 5  Rule            left_boundary: Driving in a cycle or designated lane marked by a solid white line is
                        prohibited during its times of operation. [[UK-Rule140]]
Step 5  Rule            right_boundary: Lane dividers are short, broken white lines; you should keep between
                        them. [[UK-Rule131]]
Step 5  Rule            right_boundary: This is a division of carriageway into traffic lanes. [[UK-
                        TSRGD-S11P4-item4]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid white line
                        marking a bus lane [UK-Rule140].
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight in this
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
Advice                  Stay in your lane or move to the right if needed. Do not enter the bus lane to your
                        left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation accepted, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 14754, out 1050, 15.98 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-carriageway urban road, proceeding straight ahead. There are no
                        intersections or ramps immediately in view. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road, next to a sidewalk.
                        Photo 2 confirms a single solid yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line to the right of the car; the road surface continues
                        until it meets parked cars and buildings. Photo 2 also shows no painted line on the
                        right side.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 are
                        consistent with a left edge line and no right boundary line, indicating a narrow
                        single-lane road. | roles: The solid yellow line on the left is a standard edge
                        marking for waiting restrictions in the UK. | markings: No markings are present in the
                        lane, which is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A single yellow line (as seen here) generally indicates waiting
                        restrictions, but the boundary itself does not prohibit driving within the lane. [UK-
                        HC_MARKINGS-p2-2] "Double yellow lines mean no waiting at any time, unless there are
                        signs that specifically indicate seasonal restrictions."
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid line and
                        there is a raised curb/sidewalk.
Step 6  change_right    allowed (correct): allowed: there is no painted line or curb governing the right side.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts proceeding straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be mindful of the cyclist and parked vehicles
                        on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 14754, out 793, 13.94 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-carriageway urban road with shops on the left and a parking
                        area on the right. Ahead is a clear stretch of road. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the left edge of the road. Photo 2 shows a single solid
                        red line next to the car.
                        other solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating the lane from a parking area, which then leads
                        to a concrete island. Photo 2 shows a single solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The red line indicates that stopping to park, load/unload or to board
                        and alight is prohibited. [[UK-HC_MARKINGS-p2-8]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid red line,
                        and there is no rule permitting crossing it to change lanes as it is an edge line
                        bordering a restricted area.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        line and a curb, which prohibits leaving the carriageway.
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop or park on the left due to the red
                        line restrictions.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 823, 49.32 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, driving forward. The road ahead is straight
                        with no immediate intersection or ramp. (lanes 3, mine 2, full)
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
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken white line, which
                        allows lane changes according to [UK-Rule131].
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which allows
                        lane changes according to [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: there is no waiting area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  Stay in your lane and observe the 20 mph speed limit. You may change lanes if it is
                        safe to do so.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 14754, out 937, 50.69 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street with shops on both sides. The road ahead is a single
                        carriageway with a white zig-zag marking across the lane. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the road, which becomes a zig-zag
                        pattern further ahead. Photo 2 shows the white zig-zag line next to my car.
                        white zigzag, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which is a zig-zag pattern. Photo 2 shows the
                        white zig-zag line next to my car.
                        white zigzag, curb no, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 and Photo 2 show white zig-zag lines forming a
                        pattern across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: I must not park or overtake within the zig-zag area. [UK-KYTS-zigzag]
                        "The zig-zag markings at crossings are there to ensure that drivers and pedestrians
                        can see each other clearly. As a driver, you must not park your vehicle anywh"
Step 5  Rule            right_boundary: I must not park or overtake within the zig-zag area. [UK-KYTS-zigzag]
                        "The zig-zag markings at crossings are there to ensure that drivers and pedestrians
                        can see each other clearly. As a driver, you must not park your vehicle anywh"
Step 5  Rule            area:channelizing: I should not enter the area unless it is necessary and safe. [UK-
                        Rule130-2] "If the area is bordered by a broken white line, you should not enter the
                        area unless it is necessary and you can see that it is safe to do so."
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a zig-zag line at a
                        crossing, and UK-KYTS-zigzag prohibits overtaking in this area.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a zig-zag line at a
                        crossing, and UK-KYTS-zigzag prohibits overtaking in this area.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not overtake or park within the zig-zag
                        markings as this is a pedestrian crossing area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 897, 14.9 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-carriageway urban road with buildings and trees on the right.
                        The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the opposite direction of
                        traffic. Photo 2 shows the same broken white line next to my car, consisting of one
                        visible dash and one gap.
                        white dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line along the edge of the road. Photo 2 shows a double
                        solid yellow line next to my car, and a raised curb.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: Photo 2 reveals the right boundary is a double yellow line rather than a
                        single one; Photo 2 decides for the area next to the car. | position: The center line
                        on the left and edge line on the right agree that my lane is the only lane of my
                        direction. | roles: The white dashed center line and yellow double solid edge line fit
                        their respective roles. | markings: No markings are present in the lane. | unseen: No
                        | result: consistent
Step 5  Rule            left_boundary: I may cross the broken white center line to overtake or turn off if the
                        road is clear. [[UK-Rule127]]
Step 5  Rule            right_boundary: Double yellow lines mean no waiting at any time. [[UK-
                        HC_MARKINGS-p2-2]]
Step 6  change_left     allowed (correct): allowed: governed by the broken white center line [UK-Rule127].
Step 6  change_right    prohibited (contested, correct): prohibited: governed by the raised curb and double
                        yellow edge line; crossing into the curb/pavement is prohibited.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You can proceed straight or change left to overtake if safe. Do not stop or park on
                        the right side due to the double yellow lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 865, 47.23 s
```
