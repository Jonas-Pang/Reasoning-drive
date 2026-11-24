# Reasoning of lane run 20261118_003346_laneC_IN

```text
idd__primary_d0_leftCamImgs_0000778 | lane | Test C | gemma4:e4b
----------------------------------------------------------------
Step 1  Scene           This is a narrow, paved residential street. Ahead, the street continues into the
                        distance, with buildings lining both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1: No painted line immediately to the left of the car. Photo 2: No painted line
                        immediately to the left of the car.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           Photo 1: A white line is visible immediately to the right of the car. Photo 2: A white
                        line is visible immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (1) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is an edge line, right boundary is a
                        lane line defining the single lane). | roles: the right boundary is a dashed white
                        lane line, which fits the role of a lane_line. | markings: no markings were reported
                        in the lane, which is consistent with the observation. | unseen: no attributes were
                        reported that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: The edge of the carriageway is indicated by this marking, which is
                        informative. [UK-TSRGD-S11P4-item13]
Step 5  Rule            right_boundary: You should keep between lane dividers, which are short, broken white
                        lines used to divide wide carriageways into lanes. [UK-Rule131]
Step 5  Rule            line:stop_line: This marking indicates a stop line at signals or police control,
                        although no such control is visible. [UK-HC_MARKINGS-p1]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is an edge line, and no markings
                        govern a lane change in this direction.
Step 6  change_right    allowed: allowed: The right boundary is a dashed white lane line, and no markings
                        prohibit a lane change in this direction.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along
                        this lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane to govern this action.
Step 6  turn_right      not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane to govern this action.
Step 6  u_turn          not_applicable: not_applicable: There is no arrow or prohibited-movement marking in
                        the lane to govern this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of the
                          lane or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You are in a single lane, and while you can change right if safe, you should proceed
                        straight ahead as no specific movements are restricted by markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 14737, out 858, 12.97 s

idd__primary_d0_leftCamImgs_0001907 | lane | Test C | gemma4:e4b
----------------------------------------------------------------
Step 1  Scene           This is a paved, two-way road with trees lining both sides. Ahead, the road continues
                        into a built-up area, but no specific intersection or end of lane is visible in the
                        immediate view. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line near the car, and Photo 2 shows a solid white line
                        near the car. Further ahead, Photo 1 shows the solid white line continuing, and Photo
                        2 shows the solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line near the car, and Photo 2 shows a solid white line
                        near the car. Further ahead, Photo 1 shows the solid white line continuing, and Photo
                        2 shows the solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (solid lines on both sides indicate two lanes of
                        travel in the same direction, and my lane is the left one as traffic keeps to the
                        left) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check against the boundaries | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 6  change_left     prohibited (correct): prohibited: The solid white line on the left boundary prohibits
                        lane changes into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The solid white line on the right
                        boundary prohibits lane changes into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed: Nothing restricts carrying on straight along my
                        lane, and the boundaries do not govern it.
Step 6  turn_left       not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  turn_right      not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  u_turn          not_applicable: not_applicable: No arrow or prohibited-movement marking in my lane
                        governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: There is no marked area for waiting ahead of my lane
                          or a two-way left-turn lane directly to its left.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as both boundaries are solid white lines. You are
                        permitted to proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 14737, out 803, 12.37 s

idd__primary_d0_leftCamImgs_0002074 | lane | Test C | gemma4:e4b
----------------------------------------------------------------
Step 1  Scene           This is a paved, two-way road with trees lining both sides. Ahead, the road continues
                        into a built-up area, but no specific intersection or end of lane is immediately
                        visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line near the car, and Photo 2 shows a solid white line
                        near the car. Further ahead, Photo 1 shows the solid white line continuing, and Photo
                        2 shows the solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line near the car, and Photo 2 shows a solid white line
                        near the car. Further ahead, Photo 1 shows the solid white line continuing, and Photo
                        2 shows the solid white line continuing.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2 shows a dashed white line in the center of the
                        road, separating the two lanes.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (solid white lines on both sides indicate lane
                        division). | roles: the solid white lines on both sides fit the role of lane_line. |
                        markings: the dashed white line in the center is interpreted as a yield line based on
                        the provided rule set, although its appearance is more like a lane divider in this
                        context, the interpretation is consistent with the visual evidence. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used on wide
                        carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            line:stop_yield: Vehicular traffic must give way in accordance with the requirements
                        in paragraph 7 of Part 7. [[UK-TSRGD-Part6,item3]]
Step 6  change_left     prohibited (correct): prohibited: The left boundary is a solid white line, and there
                        are no markings allowing a lane change.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: The right boundary is a solid white
                        line, and there are no markings allowing a lane change.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in the lane prohibiting
                        straight movement.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted left turn.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted right turn.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in the lane indicating a
                        permitted U-turn or prohibiting it.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings indicating a waiting area for
                          a left turn.
Step 7  Reflect         consistent
Advice                  You must stay in your current lane as lane changes are prohibited by the solid white
                        lines. You may proceed straight ahead, but be aware that the central dashed line
                        requires you to give way to traffic on the major road.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['leftmost lane, but a lane line on the left',
                        'go_straight allowed without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 14737, out 911, 8.64 s

idd__primary_d0_leftCamImgs_0002563 | lane | Test C | gemma4:e4b
----------------------------------------------------------------
Step 1  Scene           This is a two-way road in an urban area, and the road continues ahead into the
                        distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line immediately next to the car, and further ahead, it
                        appears to be a solid white line. Photo 2 shows a solid white line immediately next to
                        the car, and further ahead, it appears to be a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line immediately next to the car, and further ahead, it
                        appears to be a solid white line. Photo 2 shows a solid white line immediately next to
                        the car, and further ahead, it appears to be a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundary roles (solid lines on both sides indicate lane division).
                        | roles: the color and pattern of each boundary fit the role of a lane_line. |
                        markings: there are no markings in my lane to check against the boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 6  change_left     prohibited: prohibited, the left boundary is a solid white line, and there is no
                        specific rule prohibiting a lane change from a solid line in this context, but the
                        solid line generally restricts lane changes.
Step 6  change_right    prohibited (contested, correct): prohibited, the right boundary is a solid white line,
                        and there is no specific rule prohibiting a lane change from a solid line in this
                        context, but the solid line generally restricts lane changes.
Step 6  go_straight     allowed (contested, correct): allowed, there are no markings in my lane to prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable, there are no markings in my lane to allow or prohibit
                        turning left.
Step 6  turn_right      not_applicable: not_applicable, there are no markings in my lane to allow or prohibit
                        turning right.
Step 6  u_turn          not_applicable: not_applicable, there are no markings in my lane to allow or prohibit
                        a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable, there are no markings in my lane to indicate a
                          waiting area.
Step 7  Reflect         consistent
Advice                  You should remain in your current lane to proceed straight ahead, as lane changes are
                        prohibited by the solid white lines on both sides. No specific markings govern turning
                        movements, so proceed with caution.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 14737, out 956, 7.9 s

idd__primary_d0_leftCamImgs_0004255 | lane | Test C | gemma4:e4b
----------------------------------------------------------------
Step 1  Scene           This is a multi-lane road under an overpass. Ahead, the road continues straight under
                        the overpass structure. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows no painted line immediately next to the car. Photo 2 shows no painted
                        line immediately next to the car. Further ahead in Photo 1, there is a solid white
                        line separating the lane from the adjacent lane. Photo 2 shows this solid white line
                        further ahead.
                        white solid, curb no, lane_line, evidence partial
Step 2  Right           Photo 1 shows a solid white line immediately next to the car. Photo 2 shows a solid
                        white line immediately next to the car. Further ahead in Photo 1, there is a solid
                        white line continuing to define the edge of the road. Photo 2 shows this solid white
                        line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is a lane_line, right boundary is an
                        edge_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check against boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: The boundary of the carriageway at a road junction or a lay-by, or at
                        an exit from a private drive onto a public road, or the start of a traffic lane, is
                        indicated by this marking. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            left_boundary: This marking indicates the appropriate traffic lanes for different
                        manoeuvres. [[UK-TSRGD-S11P4-item20]]
Step 5  Rule            right_boundary: This marking indicates the edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by or emergency refuge area. [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            left_boundary: This marking indicates the edge of carriageway of a road that is not a
                        motorway and which has hard strips or hard shoulders, other than at a junction with a
                        slip road, and incorporating an audible and tactile warning. [[UK-TSRGD-S11P4-item13]]
Step 6  change_left     prohibited (correct): prohibited because the left boundary is a solid white lane_line,
                        and there is no rule allowing crossing a solid lane_line for a lane change.
Step 6  change_right    allowed: allowed because the right boundary is a solid white edge_line, and there is
                        no rule prohibiting crossing an edge_line for a lane change.
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in my lane to
                        prohibit going straight.
Step 6  turn_left       not_applicable: not_applicable because there are no markings in my lane to allow or
                        prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable because there are no markings in my lane to allow or
                        prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable because there are no markings in my lane to allow or
                        prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable because there are no markings in my lane indicating a
                          waiting area or two-way left-turn lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane, and you may change right if safe, but changing left is
                        prohibited by the solid lane line. You may proceed straight ahead.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14737, out 1042, 13.52 s

idd__primary_d0_leftCamImgs_0004361 | lane | Test C | gemma4:e4b
----------------------------------------------------------------
Step 1  Scene           This is a multi-lane road under an overpass, and the road continues ahead without an
                        immediate intersection visible in the close-up. There are multiple lanes of traffic in
                        my direction near the bottom of the photo. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a metal guardrail on the far left, followed by a painted line further
                        ahead. Photo 2 shows a painted line next to the car and a painted line further ahead.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a concrete barrier/retaining wall on the right. Photo 2 shows a painted
                        line next to the car and a painted line further ahead.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:right (full): No lane markings (arrows, text, symbols, areas, or lines) are
                        visible across my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (2) agree with the boundary roles (left boundary is an edge line, right boundary is an
                        edge line, indicating my lane is between two lanes/edges, and the presence of a dashed
                        line on the left suggests it is not the absolute leftmost lane if the guardrail is not
                        considered a lane boundary, but given the context of the right boundary being a
                        physical barrier, the lane count and index are consistent with my lane being one of
                        the middle lanes between two edges/lanes) | roles: the color and pattern of both
                        boundaries (white, dashed) fit the role of an edge line, although the left boundary is
                        adjacent to a guardrail which is not a painted line, the painted line is present and
                        matches the description | markings: there are no markings in my lane to check for
                        agreement | unseen: no | result: consistent
Step 5  Rule            left_boundary: The boundary indicates the division between the main carriageway and a
                        diverging or merging traffic lane at a road junction, or the boundary between the main
                        carriageway and a cycle lane through a junction, depending on the specific context not
                        fully visible. [[UK-TSRGD-S11P4-item10]]
Step 5  Rule            right_boundary: The boundary indicates the edge of the carriageway available for
                        through traffic other than at a road junction, lay-by or emergency refuge area. [[UK-
                        TSRGD-S11P4-item11]]
Step 5  Rule            no_turn:right: No specific rule passage covers this general marking type in the
                        provided list, so no specific allowance or prohibition can be stated. [null]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a dashed white line,
                        and no rule prohibits changing left.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and no rule
                        prohibits changing right.
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
Advice                  You are in the middle lane of a multi-lane road, and lane changes are permitted as the
                        boundaries are dashed. You may proceed straight ahead in this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:right'], missed []), actions False, unsafe ['change_left'], citation
                        unlisted, contradictions ['change_right allowed across a curb']
Tokens                  in 14737, out 1004, 8.43 s

idd__primary_d2_leftCamImgs_0001842 | lane | Test C | gemma4:e4b
----------------------------------------------------------------
Step 1  Scene           This is a two-way road with trees lining both sides. Ahead, the road continues into
                        the distance with traffic moving in both directions. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line near the car, and Photo 2 shows a solid white line
                        near the car. Further ahead, Photo 1 shows a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line near the car, and Photo 2 shows a broken white line
                        near the car. Further ahead, Photo 1 shows a broken white line.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is a lane line, right boundary is a
                        center line) | roles: the color and pattern of each boundary fit the role given to it
                        | markings: there are no markings in my lane to check against boundaries | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines which are used on
                        wide carriageways to divide them into lanes. [[UK-Rule131]]
Step 5  Rule            right_boundary: A broken white line marks the centre of the road, and you should not
                        cross it unless you can see the road is clear and wish to overtake or turn off. [[UK-
                        Rule127]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: The left boundary is a solid white line,
                        and there is no rule prohibiting a lane change into the adjacent lane.
Step 6  change_right    allowed (correct): allowed: The right boundary is a dashed white line, and there is no
                        rule prohibiting a lane change into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed: There are no markings in my lane that prohibit
                        going straight.
Step 6  turn_left       not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit turning left.
Step 6  turn_right      not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit turning right.
Step 6  u_turn          not_applicable: not_applicable: There are no markings in my lane that permit or
                        prohibit a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no markings in my lane indicating a
                          waiting area.
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane road. You may change left or right, and you may
                        proceed straight ahead. No specific turning or waiting areas are marked in your lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 14737, out 769, 5.85 s

idd__primary_d2_leftCamImgs_0002423 | lane | Test C | gemma4:e4b
----------------------------------------------------------------
Step 1  Scene           This is a two-way road in a built-up area, and the road continues ahead into the
                        distance with buildings on both sides. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows no painted line immediately next to the car. Photo 2 shows no painted
                        line immediately next to the car.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           Photo 1 shows no painted line immediately next to the car. Photo 2 shows no painted
                        line immediately next to the car.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (both sides are edge lines, indicating the lane is
                        one of two in the direction of travel). | roles: the role of both boundaries as
                        edge_line is consistent with the lack of internal lane markings. | markings: there are
                        no markings in the lane to check for agreement. | unseen: no attributes were reported
                        that were not actually seen. | result: consistent
Step 5  Rule            left_boundary: This boundary indicates the edge of the carriageway of a road that is
                        not a motorway and which has hard strips or hard shoulders, other than at a junction
                        with a slip road, and incorporating an audible and tactile warning. [[UK-
                        TSRGD-S11P4-item13]]
Step 5  Rule            right_boundary: This boundary indicates the edge of the carriageway of a road that is
                        not a motorway and which has hard strips or hard shoulders, other than at a junction
                        with a slip road, and incorporating an audible and tactile warning. [[UK-
                        TSRGD-S11P4-item13]]
Step 6  change_left     allowed: allowed: The left boundary is an edge_line, and no rule prohibits changing
                        into the adjacent lane.
Step 6  change_right    allowed (contested, label prohibited): allowed: The right boundary is an edge_line,
                        and no rule prohibits changing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): allowed: No markings in the lane restrict proceeding
                        straight ahead.
Step 6  turn_left       not_applicable: not_applicable: No markings in the lane govern turning left.
Step 6  turn_right      not_applicable: not_applicable: No markings in the lane govern turning right.
Step 6  u_turn          not_applicable: not_applicable: No markings in the lane govern U-turning or turning in
                        reverse.
Step 6  enter_waiting_areanot_applicable: not_applicable: There are no marked waiting areas or two-way left-
                          turn lanes visible ahead.
Step 7  Reflect         The boundaries and markings decided are consistent with the close-up view, and no
                        action is allowed against a prohibition.
Advice                  You are in the left lane of a two-way road, and you may change left or right if safe.
                        You may proceed straight ahead in your current lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_left allowed across a curb', 'change_right allowed across a curb']
Tokens                  in 14737, out 814, 6.08 s

idd__primary_d2_leftCamImgs_0003438 | lane | Test C | gemma4:e4b
----------------------------------------------------------------
Step 1  Scene           This is a multi-lane road with an elevated structure overhead. Ahead, the road
                        continues, and there is a barrier separating the road from the right side. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1: No painted line immediately next to the car. The line further ahead is not
                        clearly visible due to distance and context. Photo 2: No painted line immediately next
                        to the car. The line further ahead is not visible in the close-up.
                        none none, curb no, edge_line, evidence partial
Step 2  Right           Photo 1: A continuous white line is visible next to the car. Further ahead, this line
                        continues. Photo 2: A continuous white line is visible next to the car. Further ahead,
                        this line continues.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (1) agree with the boundary roles (left boundary is edge_line, right boundary is
                        lane_line) | roles: the color and pattern of each boundary fit the role given to it |
                        markings: there are no markings in my lane to check against boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: No specific rule applies to the absence of a painted line on the left
                        side of the lane. [null]
Step 5  Rule            right_boundary: The division of traffic lanes indicates the requirements for vehicular
                        traffic in this direction. [[UK-TSRGD-S11P4-item4]]
Step 5  Rule            left_boundary: No specific rule applies to the absence of a painted line on the left
                        side of the lane. [null]
Step 5  Rule            right_boundary: The division of traffic lanes indicates the requirements for vehicular
                        traffic in this direction. [[UK-TSRGD-S11P4-item4]]
Step 6  change_left     not_applicable: not_applicable
Step 6  change_right    allowed (contested, label prohibited): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left lane of two lanes. You may change right into the right lane, and
                        you may proceed straight ahead. Turning left, turning right, or performing a U-turn is
                        not governed by markings in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 14737, out 760, 6.96 s
```
