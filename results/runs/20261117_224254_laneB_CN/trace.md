# Reasoning of lane run 20261117_224254_laneB_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch leading towards a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly, with distinct dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this solid yellow line clearly next to the car. Further ahead
                        in Photo 1, the line remains solid yellow.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow in my lane pointing straight
                        ahead. Photo 1 shows another white arrow further ahead in the same lane also pointing
                        straight ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle lane) agree with the boundaries: a white dashed line on the left and a yellow
                        solid line on the right. | roles: The white dashed line correctly functions as a lane
                        line, and the yellow solid line correctly functions as a left-hand edge line (as per
                        Chinese rules). | markings: The straight arrow in my lane is consistent with the
                        lane's role and the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The yellow edge line marks the left-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       allowed: allowed by the straight or U-turn arrow [CN-5.13.1]
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          allowed: allowed by the straight or U-turn arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from this lane. You are permitted
                        to change into the left lane, but you must not move to the right beyond the yellow
                        edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['turn_left allowed although no arrow shows it']
Tokens                  in 8458, out 1007, 9.04 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. Ahead, there is a clear roadway with
                        multiple lanes and a car in the distance. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 shows a solid yellow line on
                        the right.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 shows a white left-turn arrow in my lane further ahead.
                        Photo 2 shows a white left-turn arrow in my lane just ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white lane line is on my left and a yellow edge line
                        is on my right. | roles: The white dashed line fits the role of a crossable lane line,
                        and the yellow solid line fits the role of a left-hand edge line. | markings: The
                        left-turn arrow in my lane is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The yellow edge line marks the left-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            arrow:left: The left-turn arrow indicates that the lane is for turning left.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow edge line [CN-5.4.3]
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the left-turn arrow [CN-5.13.1]
Step 6  turn_left       allowed: allowed by the left-turn arrow [CN-5.13.1]
Step 6  turn_right      prohibited: prohibited by the left-turn arrow [CN-5.13.1]
Step 6  u_turn          prohibited: prohibited by the left-turn arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to turn left at the upcoming intersection. Lane changes to the left are
                        permitted, but do not attempt to change lanes to the right or proceed straight.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8458, out 973, 9.32 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on both sides. The road ahead appears to be a
                        straight stretch with an intersection or signalized area further ahead. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow in my lane pointing straight
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's role and the dashed
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.3]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that I can go straight ahead or make a
                        U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white left boundary [CN-5.2.3]
Step 6  change_right    allowed (correct): allowed by the broken white right boundary [CN-5.2.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking [CN-5.13.1]
Step 6  turn_left       prohibited: prohibited by the arrow marking which does not show a left turn
                        [CN-5.13.2]
Step 6  turn_right      prohibited: prohibited by the arrow marking which does not show a right turn
                        [CN-5.13.2]
Step 6  u_turn          allowed: allowed by the arrow marking [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may go straight or perform a U-turn from your current lane. Lane changes to the
                        left or right are permitted as the boundaries are broken white lines. Do not attempt
                        to turn left or right as the lane markings do not permit these movements.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 971, 10.32 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure on the right. The road ahead is
                        straight with several lanes of traffic moving in the same direction. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to the car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to the car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2 shows a white curved line in the middle of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white line on the left and a white line on the right
                        indicate a lane between two others. | roles: The white solid lines correctly function
                        as lane lines separating traffic in the same direction. | markings: The curved symbol
                        is in the center of the lane and does not conflict with the boundaries. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            symbol:other: no marking governs this action
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed as no markings or boundaries prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane bounded by solid white lines on both sides, which prohibits lane
                        changes to the left or right. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 944, 9.84 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure on the right. The road ahead is
                        straight with several lanes of traffic moving in the same direction. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows the same solid white line clearly next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows this solid white line clearly next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on the left (edge line) and a white
                        line on the right (lane line). | roles: The white solid lines correctly function as an
                        edge line on the left and a lane line on the right. | markings: No markings are
                        present, which is consistent with the straight road ahead. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: No specific rule for a white edge line on the left in this context, but
                        it marks the boundary of the roadway. [null]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the lane on
                        the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 827, 8.94 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. Ahead, there is a
                        clear roadway with several lanes of traffic moving in the same direction. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): Photo 2 shows a white dashed line on the left and a white
                        dashed line on the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle lane) is consistent with having a lane line on both the left and right. |
                        roles: The white dashed lines correctly function as lane lines separating traffic in
                        the same direction. | markings: No specific arrows or words are visible in my lane to
                        contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the lane markings are broken white lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8458, out 853, 7.33 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane that appears
                        to have a turn lane or special marking ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line as a broken line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow line on the right. Photo 2 shows this yellow line as a solid
                        line near my car. Further ahead in Photo 1, the yellow line appears to be a broken-
                        solid line.
                        yellow solid_dashed (near line solid), curb no, center_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in my lane.; arrow:right
                        (full): Photo 2 shows a white right-turn arrow in my lane.; text:other (partial):
                        Photo 2 shows white characters in my lane, appearing to be '直' (straight) and '左'
                        (left) or similar, but they are partially obscured by the car ahead. Photo 1 shows a
                        white arrow pointing straight ahead in the lane to my left.
Step 4  Cross-check     close_up: The left boundary is dashed in Photo 2 and white in Photo 1. The right
                        boundary is solid in Photo 2 but becomes broken-solid further ahead in Photo 1. Photo
                        2 decides the immediate boundary (dashed left, solid-dashed right). | position: The
                        lane count (3) and my position (2) are consistent with a white lane line on the left
                        and a yellow center line on the right. | roles: The white dashed line correctly
                        identifies a lane line, and the yellow solid-dashed line correctly identifies a center
                        line. | markings: The left and right arrows in my lane are consistent with the lane's
                        function as a multi-directional turn lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid side of the broken-solid yellow line prohibits me from
                        crossing to the right. [[CN-6.2.3]]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permitted movement.
                        [[CN-5.13.1]]
Step 5  Rule            arrow:right: The arrow indicates that a right turn is a permitted movement.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid side of the broken-solid
                        yellow center line [CN-6.2.3]
Step 6  go_straight     allowed (contested, correct): allowed by the lane markings and lack of prohibiting
                        markings
Step 6  turn_left       allowed: allowed by the left-turn arrow [CN-5.13.1]
Step 6  turn_right      allowed: allowed by the right-turn arrow [CN-5.13.1]
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may turn left, turn right, or go straight from this lane. Lane changes to the left
                        are permitted, but crossing the yellow line to the right is prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'text:other'], missed []), actions True, unsafe [],
                        citation in_pack_not_accepted, contradictions ['go_straight allowed although no arrow
                        shows it']
Tokens                  in 8458, out 1191, 13.87 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an elevated structure overhead. The road ahead appears to
                        be a straight continuation of the current lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle) agree with the white lane lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines separating traffic in the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane's role and the
                        dashed boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       prohibited: prohibited by the arrow which does not show a left turn [CN-5.13.2]
Step 6  turn_right      prohibited: prohibited by the arrow which does not show a right turn [CN-5.13.2]
Step 6  u_turn          allowed: allowed by the arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn in this lane. Lane changes to the
                        left or right are permitted as the boundaries are broken white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 948, 10.34 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a bridge or overpass ahead. My car is in
                        a lane heading towards a city skyline. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is solid white near my car and becomes a broken white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is solid white near my car and remains solid white further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white left-turn arrow in the lane to my
                        left. No markings are visible in my lane.
Step 4  Cross-check     close_up: The close-up confirms the solid white line on the right and the solid-to-
                        broken transition on the left. The same in both photos. | position: The lane count (3)
                        and my position (2) are consistent with the white lane lines on both sides. | roles:
                        The white lines correctly function as lane lines separating traffic in the same
                        direction. | markings: No markings are in my lane, which is consistent with the lane
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid side may not cross; vehicles on the broken side
                        may cross. [[CN-6.2.3]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane. Lane changes to the left are prohibited where
                        the line is solid, and lane changes to the right are prohibited by the solid white
                        line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8458, out 855, 9.56 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane that appears
                        to be a dedicated bus lane or a lane with specific restrictions. (lanes 3, mine 3,
                        full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows this same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 shows this solid yellow line
                        clearly. Further ahead, the line remains solid yellow.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows large white Chinese characters '公交' (Bus) painted in my
                        lane.; no_turn:left (insufficient): Photo 1 shows a white arrow pointing straight
                        ahead in the lane to my left, but my lane has no visible arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white line on the left separates me from another lane,
                        and a yellow line on the right marks the edge of the roadway. | roles: The white lane
                        line and yellow edge line fit their respective roles. | markings: The '公交' (Bus) text
                        indicates a bus lane, which is consistent with the lane's position and the solid
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The yellow edge line marks the boundary of the roadway. [[CN-5.4.3]
                        [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            text:bus: Vehicles other than buses are prohibited from entering this lane.
                        [[CN-6.9.1] [mandatory] GB 5768.3-2025, section 6.9.1, page 54]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated bus lane (marked '公交'). You should only proceed straight in
                        this lane if you are driving a bus. Lane changes to the left or right are prohibited
                        by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left', 'text:bus'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 1033, 9.69 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a vehicle
                        directly in front of it. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        a solid white line next to my car and a broken white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow line separating my lane from the lane to the right. Photo 2
                        shows a solid yellow line next to my car and a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in my lane.; line:stop_line
                        (full): Photo 1 shows a white stop line at the end of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the boundaries: a white line on the left and a yellow line on the right. |
                        roles: The white line on the left is a lane line; the yellow line on the right is a
                        center line separating opposing traffic. | markings: The left-turn arrow in my lane is
                        consistent with the lane's purpose and the center line on the right. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid side of the broken-solid white line may not
                        cross. [[CN-6.2.3]]
Step 5  Rule            right_boundary: The single solid yellow line prohibits crossing into the opposite
                        direction. [[CN-6.1.4]]
Step 5  Rule            arrow:left: The left-turn arrow restricts the direction of travel to a left turn.
                        [[CN-5.13.2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles must stop when yielding or waiting
                        to proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     prohibited (contested, label allowed): prohibited
Step 6  turn_left       allowed: allowed
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to make a left turn at the upcoming intersection. You must stop at the
                        white stop line before turning left.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 8458, out 977, 8.61 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a physical barrier on the left and a concrete barrier on
                        the right. Ahead, there is an overpass and an intersection area. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 2 shows a solid yellow line in the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The yellow line in the center of the lane is a single solid line, not a stop-yield
                        line (which requires two parallel lines and a character). It appears to be a guide
                        line or a marking for a specific lane function. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1]]
Step 5  Rule            line:stop_yield: No specific rule for a single yellow line in the center of a lane,
                        but it generally indicates a specific lane path.
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as lane changes to the left or right are prohibited by the
                        solid white lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 8458, out 899, 30.41 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass. My car is in a lane heading
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 shows a solid yellow line next
                        to my car. Further ahead in Photo 1, the line appears to remain solid yellow.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.; text:other (full): Photo 2 shows white characters '10' and a dash in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a yellow solid line on the
                        right. | roles: The white dashed line correctly identifies a lane line, and the yellow
                        solid line correctly identifies the right edge of the roadway. | markings: The
                        straight arrow and '10' text are consistent with a through lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The yellow edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 5  Rule            text:other: The '10' marking is a specific lane instruction not covered by the
                        provided rules.
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       prohibited: prohibited by the arrow which does not show a left turn [CN-5.13.2]
Step 6  turn_right      prohibited: prohibited by the arrow which does not show a right turn [CN-5.13.2]
Step 6  u_turn          allowed: allowed by the arrow which shows a U-turn [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn in this lane. You are permitted to
                        change lanes to the left, but changing to the right is prohibited by the solid yellow
                        edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_u_turn', 'text:other'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8458, out 1074, 10.33 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane that appears
                        to be the leftmost of the main traffic flow, adjacent to a median/island on the left
                        and a sidewalk/parking area on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a median/island on the left.
                        Photo 2 shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 shows a solid yellow line next
                        to my car and a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 1 shows a white arrow pointing straight ahead in
                        my lane. Photo 2 shows the same arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree. The
                        white line on the left is an edge line (median), and the yellow line on the right is a
                        center line separating opposing traffic. | roles: The white edge line and yellow
                        center line fit their respective roles. | markings: The straight arrow in my lane is
                        consistent with the lane's role and the boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The white edge line on the left marks the boundary of the motor vehicle
                        lane. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The single solid yellow line prohibits crossing into the opposite
                        direction. [[CN-6.1.4]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane allows for straight ahead and
                        U-turn movements. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          allowed: allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from this lane. Lane changes to the
                        left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 897, 10.86 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overpass and overhead signs. My car is in a lane
                        heading straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1 shows a white arrow in my lane pointing straight
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight-ahead arrow in my lane is consistent with the lane's purpose. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight_right: The arrow indicates the permitted direction of travel is
                        straight ahead or to the right. [[CN-5.13.1] [informative] GB 5768.3-2025, section
                        5.13.1, 表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      allowed: allowed
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 939, 9.45 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        straight towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be a road edge line or
                        a separation from a sidewalk/curb area. Photo 2 shows this line is solid and white,
                        with a curb/raised area visible to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 1 shows a white arrow in my lane pointing straight
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a solid white line on the
                        right. | roles: The white dashed line correctly functions as a lane line, and the
                        solid white line correctly functions as an edge line. | markings: The straight arrow
                        in my lane is consistent with the lane's purpose and the surrounding boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       prohibited: prohibited by the arrow which does not show a left turn [CN-5.13.2]
Step 6  turn_right      prohibited: prohibited by the arrow which does not show a right turn [CN-5.13.2]
Step 6  u_turn          allowed: allowed by the arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from this lane. You are permitted
                        to change lanes to the left, but changing to the right is prohibited by the edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 988, 10.76 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection. My car is in a
                        lane that appears to be the rightmost lane of the direction of travel. (lanes 3, mine
                        3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a raised curb and a physical barrier on the right. Photo 2 shows the
                        same raised curb and a white line painted on the curb/pavement edge.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a large white arrow pointing straight
                        ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white dashed line is on my left (lane line) and a
                        curb/edge line is on my right. | roles: The white dashed line on the left fits the
                        role of a crossable lane line, and the white solid line/curb on the right fits the
                        role of an edge line. | markings: The straight arrow in my lane is consistent with the
                        lane's purpose and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line on the right marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the curb and solid edge line [CN-5.4.3]
Step 6  go_straight     allowed (correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow [CN-5.13.1]
Step 6  u_turn          allowed (WRONG, label prohibited): allowed by the straight/U-turn arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from this lane. You are permitted
                        to change lanes to the left, but changing to the right is prohibited by the curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight', 'line:stop_line']), actions
                        False, unsafe ['change_left', 'u_turn'], citation accepted, contradictions []
Tokens                  in 8458, out 994, 9.99 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is in a
                        lane moving forward towards a junction where several lanes appear to merge or turn.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows the same solid white line clearly next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows this solid white line clearly next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a large white arrow pointing straight ahead
                        in my lane.; arrow:left (full): Photo 2 shows a large white arrow pointing left in the
                        lane to my right.; arrow:right (full): Photo 2 shows a large white arrow pointing
                        right in the lane to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight-ahead arrow in my lane is consistent with the lane's role. The arrows in
                        the right lane indicate its specific turn functions. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1,
                        page 27]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      allowed: allowed
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight or turning right. You should stay in
                        your lane and avoid changing lanes or turning left at the upcoming intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight_right'], missed []), actions True,
                        unsafe [], citation unlisted, contradictions ['turn_left prohibited although an arrow
                        shows it']
Tokens                  in 8458, out 1056, 10.74 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in one of the central
                        lanes. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows the same white dashed line clearly next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white straight arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2nd
                        from left) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane lines between lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        role as a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows my car to change lanes to the right.
                        [[CN-5.2.3]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.3]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.3]
Step 6  go_straight     allowed (correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow [CN-5.13.1]
Step 6  u_turn          allowed (WRONG, label prohibited): allowed by the straight arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from this lane. Lane changes to the
                        left or right are permitted as the boundaries are broken white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight']), actions False, unsafe
                        ['u_turn'], citation accepted, contradictions []
Tokens                  in 8458, out 930, 8.83 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in one of the middle
                        lanes. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane's role and the surrounding
                        lane markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [CN-5.13.1] "Guide arrows indicate the direction of travel
                        for vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          allowed (WRONG, label prohibited): allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight or making a U-turn. Lane changes to
                        the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight', 'line:stop_line']), actions
                        False, unsafe ['u_turn'], citation accepted, contradictions []
Tokens                  in 8458, out 855, 9.57 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a white
                        arrow pointing straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [CN-5.13.1] "Guide arrows indicate the direction of travel
                        for vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          allowed (WRONG, label prohibited): allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from this lane. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight']), actions False, unsafe
                        ['u_turn'], citation accepted, contradictions []
Tokens                  in 8458, out 853, 8.59 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a white
                        arrow indicating a left turn or straight movement. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a large white arrow in my lane pointing
                        straight ahead and slightly to the left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight-left arrow is consistent with the lane's position and the surrounding
                        lane lines. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight_left: The arrow indicates that the lane allows for straight ahead or
                        left turn movements. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1,
                        page 27]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       allowed (correct): allowed
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your current lane. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8458, out 948, 11.63 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving forward
                        towards the intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left. Photo 2 shows a solid white line on the left
                        next to the car, which continues straight ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a solid white line on the right
                        next to the car, which continues straight ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white stop line across the lane at the
                        intersection.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a white line on the left (edge line) and a white line
                        on the right (lane line). | roles: The white solid line on the left acts as an edge
                        line, and the white solid line on the right acts as a lane line separating my lane
                        from the one to its right. | markings: The stop line is consistent with the lane's end
                        at an intersection. | unseen: none | result: consistent
Step 5  Rule            left_boundary: No specific rule provided for a white solid edge line, but it marks the
                        boundary of the roadway. [null]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the adjacent
                        lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            line:stop_line: The stop line marks where the vehicle must stop when yielding or
                        waiting to proceed. [CN-6.4.1]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may proceed straight through the
                        intersection after stopping at the white stop line. Lane changes to the right are
                        prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 894, 9.34 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is approaching an intersection under a bridge. There are multiple lanes of
                        traffic moving forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows this line is solid white
                        next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a yellow arrow pointing straight ahead in
                        my lane.; arrow:left (full): Photo 2 shows a yellow arrow pointing left in the lane to
                        my left.; arrow:right (full): Photo 2 shows a yellow arrow pointing right in the lane
                        to my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on the left and a white line on the
                        right. | roles: The white dashed line on the left is a lane line; the white solid line
                        on the right is an edge line. | markings: The yellow arrows in each lane correspond to
                        the lane functions. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for going straight or
                        turning right. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.3]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the lane-use arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the lane-use arrow which does not show a left turn
                        [CN-5.13.1]
Step 6  turn_right      allowed (correct): allowed by the lane-use arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the lane-use arrow which does not show a U-turn
                        [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or turn right from your current lane. Lane changes to the
                        left are permitted, but changing to the right is prohibited. Do not attempt to turn
                        left or make a U-turn from this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:straight_right'], missed []), actions False, unsafe
                        ['change_left', 'go_straight'], citation accepted, contradictions ['turn_left
                        prohibited although an arrow shows it']
Tokens                  in 8458, out 1050, 9.0 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a white fence on the left and a sidewalk on the right.
                        The road ahead appears to be a straight stretch leading toward an intersection. (lanes
                        3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a white fence on the left.
                        Photo 2 shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to my right. Photo
                        2 shows a broken white line next to my car and a broken white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (1)
                        are consistent with the left edge line and right lane line. | roles: The white solid
                        line on the left is an edge line; the white dashed line on the right is a lane line. |
                        markings: No markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white edge line on the left marks the boundary of the motor vehicle
                        lane. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white line allows for lane changes to the right.
                        [[CN-5.2.3]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane.
                        Changing to the left is prohibited by the solid edge line and the physical barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:left'], missed ['arrow:straight']), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8458, out 823, 7.73 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is in a
                        lane with a straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.; line:crosswalk (full): Photo 1 shows a white crosswalk ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane's purpose and the
                        surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 8458, out 978, 8.67 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city road approaching an intersection with a pedestrian
                        crossing. My car is in a lane that leads straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line as solid next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a large white arrow pointing straight ahead in my
                        lane.; line:crosswalk (full): Photo 1 shows a white pedestrian crossing (zebra
                        stripes) ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane's purpose and the
                        surrounding lane markings. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines, and the lane is designated for
                        straight-through traffic only.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8458, out 993, 10.2 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is
                        positioned in a lane facing forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow line on the right side of my lane. Photo 2 shows this yellow
                        line as a solid line next to my car.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows a yellow grid pattern across the intersection ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on the left and a yellow edge line on the right.
                        | roles: The white lane line on the left and yellow edge line on the right fit the
                        roles of a lane line and a right-hand edge line respectively. | markings: The yellow
                        grid marking is consistent with an intersection area where stopping is prohibited. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The yellow edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            area:grid: The grid marking shows an area where stopping for any reason is prohibited.
                        [[CN-6.8.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Do not attempt to change lanes to
                        the left or right, and do not stop within the yellow grid area at the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 737, 7.57 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. There is a grid marking in the middle
                        of the road and a car in the lane to the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows a white grid marking in the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a yellow center line on the left and a white edge line
                        on the right. | roles: The yellow solid line correctly identifies a center line, and
                        the white solid line correctly identifies an edge line. | markings: The grid marking
                        is consistent with an intersection approach. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits vehicles from crossing into the
                        opposite direction. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The solid white line normally prohibits crossing to the right.
                        [[CN-4.2.2-a]]
Step 5  Rule            area:grid: The grid marking shows an area where stopping for any reason is prohibited.
                        [[CN-6.8.1-2]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight but must not cross the solid
                        yellow line to the left or the solid white line to the right. Do not stop within the
                        grid area ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed ['symbol:other']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 859, 27.52 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city road with an intersection ahead. My car is in a lane
                        that appears to be a dedicated turn lane or a lane with specific guidance markings.
                        (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a solid white line near my car and remains solid further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a solid line. Photo 2
                        shows this line is a solid white line near my car and remains solid further ahead.
                        There is a sidewalk and a curb to the right of this line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a large white arrow in my lane pointing
                        straight ahead.; arrow:left (full): Photo 1 shows a white arrow in the lane to my left
                        pointing left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with the boundaries: a white lane line is on my left and a
                        white edge line/curb is on my right. | roles: The white solid line on the left is a
                        lane line; the white solid line on the right is an edge line. | markings: The
                        straight-right arrow in my lane is consistent with the lane's position and the solid
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway. [[CN-5.4.3]
                        [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight or
                        turning right. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (WRONG, label prohibited): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      allowed (correct): allowed
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn right from your current lane. Lane changes to the
                        left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight_right'], missed ['arrow:right']), actions False, unsafe
                        ['go_straight'], citation unlisted, contradictions ['turn_left prohibited although an
                        arrow shows it']
Tokens                  in 8458, out 1043, 29.19 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road. Ahead, there is an intersection with
                        a truck and other vehicles. The road is bounded by a concrete barrier on the left.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a concrete barrier on the left. Photo 2 shows a solid white line next to
                        the car, then a concrete barrier further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in the lane to the right of
                        my lane.; arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a concrete barrier on the left and a white line on the
                        right. | roles: The white solid line on the right acts as a lane line, and the
                        barrier/white line on the left acts as an edge line. | markings: The straight arrow in
                        my lane and the left turn arrow in the right lane are consistent with the lane layout.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: no marking governs this action [null]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            arrow:left: The arrow in the adjacent lane indicates it is for turning left.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): no marking governs this action
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line (CN-6.2.1)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow (CN-5.13.1)
Step 6  turn_left       prohibited: prohibited by the straight arrow (CN-5.13.1)
Step 6  turn_right      prohibited: prohibited by the straight arrow (CN-5.13.1)
Step 6  u_turn          prohibited: prohibited by the straight arrow (CN-5.13.1)
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the right are
                        prohibited by the solid white line, and the lane to your right is designated for left
                        turns.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions False, unsafe ['change_left'],
                        citation unlisted, contradictions ['change_left allowed across a curb', 'turn_left
                        prohibited although an arrow shows it']
Tokens                  in 8458, out 1037, 9.78 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a yellow
                        center line to its left and a white lane line to its right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to the left. Photo 2
                        shows this line is a solid yellow line near my car and becomes a broken-solid yellow
                        line further ahead.
                        yellow solid_dashed (near line solid), curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this line is a solid
                        white line near my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow in my lane pointing straight
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a white lane line is
                        on my right. | roles: The yellow center line and white lane line correctly represent
                        the center and right-side boundaries respectively. | markings: The straight-ahead
                        arrow is consistent with the lane's role. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid side of the broken-solid yellow line may not
                        cross. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from the solid-line side.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      allowed (WRONG, label prohibited): allowed
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:straight']), actions False, unsafe
                        ['turn_right'], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 871, 9.09 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city road approaching an intersection. My car is in a
                        central lane with a straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the one to the left. Photo 2 shows
                        this line is a solid white line near my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the one to the right. Photo 2 shows
                        this line is a solid white line near my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane's role and the surrounding
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 838, 8.13 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a fence on the left. The road
                        ahead appears to be a straight stretch with multiple lanes of traffic moving in the
                        same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line clearly as a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be the edge of the roadway.
                        Photo 2 shows this line as a solid white line next to my car, with a curb/barrier area
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white lane line is on my left and a white edge line
                        is on my right. | roles: The white solid line on the left is a lane line, and the
                        white solid line on the right is an edge line, which is consistent with the road
                        layout. | markings: No markings are present in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight ahead, but
                        lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8458, out 860, 8.7 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and parked cars on both sides. The road ahead
                        appears to be a straight stretch with an intersection or signalized area in the
                        distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my lane. Photo 2 shows a white
                        dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 1 shows a white dashed line further ahead in my
                        lane, possibly indicating a lane change or lane function change.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the double solid yellow line on the left (center line) and the
                        white dashed line on the right (lane line). | roles: The yellow double solid line
                        correctly identifies the center line separating opposing traffic. The white dashed
                        line correctly identifies a lane line. | markings: The white dashed line ahead is
                        consistent with a lane-change or lane-function-change indicator. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The broken white line allows vehicles to change lanes. [[CN-5.2.3]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the right lane if needed, but crossing
                        the double solid yellow line to the left is prohibited. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 8458, out 833, 8.63 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my lane. Photo 2 shows a white
                        dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The double solid yellow line on the left
                        indicates a center line separating opposing traffic, and the white dashed line on the
                        right separates lanes in the same direction. This is consistent with my lane being the
                        middle of three lanes in my direction. | roles: The yellow double solid line correctly
                        identifies a center line, and the white dashed line correctly identifies a lane line.
                        | markings: The straight-ahead arrow in my lane is consistent with the lane's purpose.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The broken white line means it may be crossed. [[CN-4.2.2-a]]
Step 5  Rule            arrow:straight_left: The guide arrow indicates the direction of travel is straight
                        ahead or left. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (WRONG, label prohibited): allowed
Step 6  turn_left       allowed (correct): allowed
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your lane. You are permitted to change into
                        the right lane but are prohibited from changing into the left lane or making a right
                        turn or U-turn.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_left'], missed ['arrow:left_u_turn', 'arrow:straight']), actions
                        False, unsafe ['go_straight'], citation accepted, contradictions []
Tokens                  in 8458, out 864, 9.64 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overpass to the left and buildings ahead. The road
                        appears to be a wide boulevard with several lanes of traffic moving in the same
                        direction. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.; arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight
                        ahead in the lane to my right.; arrow:straight_u_turn (full): Photo 2 shows a white
                        arrow pointing straight ahead in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight ahead arrows in my lane are consistent with the lane boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1,
                        表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       allowed (WRONG, label prohibited): allowed
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          allowed (WRONG, label prohibited): allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from your current lane. Lane
                        changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight']), actions False, unsafe
                        ['turn_left', 'u_turn'], citation unlisted, contradictions ['turn_left allowed
                        although no arrow shows it']
Tokens                  in 8458, out 1055, 10.08 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overpass to the left. The road ahead appears to be a
                        straight stretch leading towards an intersection or a major junction. (lanes 4, mine
                        3, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows the same solid white line clearly next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway or a separation from a sidewalk/pedestrian area. Photo 2 shows this solid
                        white line clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1 shows a white arrow pointing straight ahead in my
                        lane further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with the white lane line on my left and the white edge line
                        on my right. | roles: The white solid line on the left correctly functions as a lane
                        line, and the white solid line on the right functions as an edge line. | markings: The
                        straight-ahead arrow in my lane is consistent with the lane's purpose. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1,
                        page 27]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      allowed: allowed
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 976, 9.86 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in one of the middle
                        lanes of a multi-lane roadway. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1 shows a white arrow in my lane pointing straight
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane's role and the
                        dashed boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.3]]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white left boundary line [CN-5.2.3]
Step 6  change_right    allowed (correct): allowed by the broken white right boundary line [CN-5.2.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane [CN-5.13.1]
Step 6  turn_left       prohibited: prohibited by the arrow which does not show a left turn [CN-5.13.1]
Step 6  turn_right      allowed: allowed by the arrow in my lane [CN-5.13.1]
Step 6  u_turn          prohibited: prohibited by the arrow which does not show a U-turn [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may go straight or turn right from this lane. Lane changes to the left or right
                        are permitted as the boundaries are broken white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 936, 10.03 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a central lane of a
                        multi-lane roadway. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 1 and Photo 2 show a white arrow pointing straight
                        ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white dashed
                        lines correctly function as crossable lane lines. | markings: The straight arrow in my
                        lane is consistent with the dashed boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow [CN-5.13.1]
Step 6  u_turn          allowed (WRONG, label prohibited): allowed by the straight arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn in this lane. Lane changes to the
                        left or right are permitted as the lane boundaries are broken white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight', 'line:stop_line']), actions
                        False, unsafe ['change_left', 'change_right', 'u_turn'], citation accepted,
                        contradictions []
Tokens                  in 8458, out 938, 8.72 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city road approaching an intersection. My car is in a
                        lane that appears to be the middle lane of a three-lane direction. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line near the car and a broken line further
                        ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: The close-up (Photo 2) clarifies that the left boundary is a solid-dashed
                        line (solid near the car, broken further ahead) and the right boundary is solid. The
                        arrow is clearly visible in Photo 2. | position: The lane count of 3 and my position
                        as lane 2 are consistent with the white lane lines on both sides. | roles: The white
                        lines correctly function as lane lines separating traffic in the same direction. |
                        markings: The straight-right arrow in my lane is consistent with the lane's position
                        and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid side may not cross; vehicles on the broken side
                        may cross. [CN-6.2.3] "On a broken-solid white line, vehicles on the solid side may
                        not cross; vehicles on the broken side may cross, and a vehicle crossing the line must
                        give way to "
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            arrow:straight_right: The guide arrow indicates that the lane is for traveling
                        straight or turning right. [CN-5.13.2] "Guide arrows shall be marked on intersection
                        approaches where the direction of travel is restricted, in the lane being dropped
                        where the number of lanes is redu"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      allowed: allowed
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn right from your current lane. Lane changes to the
                        left or right are prohibited by the solid lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 906, 8.68 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane heading
                        towards the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which appears to be a lane line or an
                        edge line. Photo 2 shows a white solid line very close to the car's right side.
                        Further ahead in Photo 1, this line continues as a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white left-turn arrow in the lane to my
                        left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line is on my left and a white
                        solid line is on my right. | roles: The white dashed line on the left and white solid
                        line on the right fit the roles of lane lines. | markings: No markings are in my lane,
                        which is consistent with the lane boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from changing lanes to the right.
                        [[CN-6.2.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change to the left lane if needed, but you are prohibited from changing to the
                        right lane. You can proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 876, 7.87 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows the same white broken line clearly as a series of white dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this solid white line clearly. There is a concrete barrier
                        further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 2 shows white diagonal lines (chevrons) painted on the
                        pavement in the lane to my left, indicating a lane end or channelization.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white broken line on the left and a white solid line/curb on the
                        right. | roles: The white broken line on the left correctly identifies a lane-
                        changeable boundary, and the white solid line on the right correctly identifies the
                        edge of the roadway. | markings: The channelizing markings to the left indicate the
                        lane to my left is ending or changing, which is consistent with the lane layout. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            area:channelizing: The channelizing lines indicate that vehicles must follow the set
                        path and may not drive on or across the lines. [[CN-6.6.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and physical barrier
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the boundary is a broken white line. Do not
                        attempt to move to the right as there is a solid edge line and a physical barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 967, 7.51 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median on the left and a sidewalk/curb on the right.
                        Ahead, there is a clear roadway with multiple lanes of traffic moving in the same
                        direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1 shows a white arrow pointing straight ahead in my
                        lane. Photo 2 shows the same arrow clearly.; text:other (full): Photo 1 shows white
                        text '110M' in the lane to the right. Photo 2 shows it clearly.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between lanes of the same direction. | markings: The
                        straight-ahead arrow in my lane is consistent with the lane's purpose. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows my car to change lanes to the right.
                        [[CN-5.2.3]]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white left boundary line [CN-5.2.3]
Step 6  change_right    allowed (correct): allowed by the broken white right boundary line [CN-5.2.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight-ahead component of the lane
                        arrow [CN-5.13.1]
Step 6  turn_left       prohibited: prohibited by the lane arrow which does not show a left turn [CN-5.13.2]
Step 6  turn_right      allowed: allowed by the right-turn component of the lane arrow [CN-5.13.1]
Step 6  u_turn          prohibited: prohibited by the lane arrow which does not show a U-turn [CN-5.13.2]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are permitted as the boundaries are broken white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_right', 'text:other'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8458, out 1022, 9.15 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bus lane in the center. My car is in a lane
                        to the right of the bus lane. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the bus lane. Photo 2 shows this
                        same yellow line clearly as a broken-solid line (solid on the left, broken on the
                        right).
                        yellow solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows this same white line
                        clearly as a solid line next to a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows large white characters '公交' (bus) in the lane to my
                        left.; arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a yellow line is on my left (separating me from the bus
                        lane) and a white edge line is on my right. | roles: The yellow broken-solid line
                        correctly identifies the boundary with the bus lane, and the white solid line
                        correctly identifies the road edge. | markings: The '公交' text is in the adjacent lane,
                        and the straight arrow is in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid side of the broken-solid white/yellow line may
                        not cross; since the solid side is towards the bus lane, I may cross from my side (the
                        broken side). [[CN-6.2.3]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway. [[CN-5.4.3]]
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the lane marked with '公交'.
                        [[CN-6.9.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (contested, correct): allowed
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, label prohibited): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane for straight-ahead travel. You may change into the bus lane to your
                        left as the line is broken on your side, but you must not enter the lane if it is
                        reserved for buses. Do not move to the right as there is a curb and edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation accepted,
                        contradictions ['change_left allowed with the solid line of a solid-and-broken pair
                        nearer my lane']
Tokens                  in 8458, out 1043, 8.6 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the right and a
                        wall/barrier on the left. Ahead, there is a gantry and a merging/splitting area.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow line on the right. Photo 2 shows this line is a solid yellow
                        line near my car. Further ahead in Photo 1, it appears to remain solid yellow.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white lane line is on my left and a yellow edge line is
                        on my right. | roles: The white dashed line fits the role of a crossable lane line,
                        and the solid yellow line fits the role of a left-hand edge line. | markings: No
                        markings are present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The yellow edge line marks the left-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not attempt to move to the
                        right as it is the edge of the roadway marked with a solid yellow line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 880, 9.67 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the left and a metal
                        guardrail on the right. The road ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white dashed lines
                        correctly function as lane lines between lanes of the same direction. | markings: No
                        markings were identified in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is a crossable lane
                        line [CN-5.2.1-2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is a crossable
                        lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight in my lane.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the lane markings are broken white lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8458, out 862, 8.05 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The road is straight with
                        several lanes in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows the same white broken line clearly as a dashed line with distinct gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this white solid line clearly. There is a metal guardrail
                        further to the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on the left and a white solid
                        line on the right. | roles: The white dashed line on the left correctly functions as a
                        lane line, and the white solid line on the right correctly functions as an edge line.
                        | markings: No markings were observed in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which marks the edge of the roadway [CN-5.4.3].
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight in my lane.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may change into the left lane
                        as the boundary is a broken white line. You should not move to the right as it is the
                        edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8458, out 904, 7.61 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or elevated road with an upcoming intersection or split. My car
                        is in a lane heading forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows the same solid white line clearly next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows the same solid white line clearly next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane's forward direction. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          allowed: allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn in this lane. Lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 848, 8.47 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with trees lining both sides. The road ahead is
                        straight with several lanes of traffic moving in the same direction. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line (dashed) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line is a solid white
                        line. There is a metal guardrail further to the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white dashed line on the left and a white solid
                        line on the right. | roles: The white dashed line on the left correctly functions as a
                        crossable lane line, and the white solid line on the right functions as an edge line.
                        | markings: No markings are present to contradict the boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not attempt to move to the
                        right as the solid edge line prohibits it. Continue straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 863, 9.19 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a physical barrier on the right. The road
                        ahead is straight with several lanes of traffic moving in the same direction. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows a white broken line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a metal guardrail. Photo 2
                        shows a white solid line next to the car and a white solid line further ahead. A metal
                        guardrail is present.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white left-turn arrow in the lane to my
                        left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white broken line is on my left and a white solid
                        line/guardrail is on my right. | roles: The white broken line on the left fits the
                        role of a crossable lane line. The white solid line on the right fits the role of an
                        edge line. | markings: No markings are in my lane, which is consistent with the lane's
                        role as a through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and guardrail
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if needed, but you are
                        prohibited from moving to the right due to the solid edge line and guardrail. Proceed
                        straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 911, 10.59 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane highway or expressway with a concrete barrier on the left
                        and a raised embankment with a fence on the right. The road ahead appears to be a
                        continuous stretch of highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line and a dashed white line side by side on the left.
                        Photo 2 shows a solid white line and a dashed white line side by side on the left,
                        with the dashed line being closer to my car.
                        white solid_dashed (near line dashed), curb yes, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2 shows a red-colored rectangular area in the middle of the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a dashed line on the left indicates another lane of my
                        direction, and a solid line on the right indicates the edge of the roadway. | roles:
                        The white solid-dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: The red area is a
                        pavement marking but does not conflict with the lane boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles on the broken side may cross the line, while those on the
                        solid side may not. [[CN-6.2.3]]
Step 5  Rule            right_boundary: Crossing the solid edge line is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            symbol:other: No specific rule governs the red area, but it is a pavement marking.
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the lane to your left as it is marked with a broken line. Do not
                        attempt to move to the right as it is bounded by a solid edge line. Proceed straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:other'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['change_left allowed across a curb']
Tokens                  in 8458, out 917, 9.11 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway or expressway. Ahead, there is a wide area with white
                        markings, possibly an intersection or a merging/diverging zone with multiple lanes.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows this same white broken line clearly as a series of white dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway or a separation from a shoulder/barrier. Photo 2 shows this solid white line
                        clearly. Further right, there is a metal guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 and Photo 2 show large white diagonal lines
                        (chevrons) across the road ahead, indicating a channelized area or a lane termination.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle lane) agree with the boundaries: a white broken line on the left and a white
                        solid line on the right. | roles: The white broken line on the left fits the role of a
                        crossable lane line. The white solid line on the right fits the role of an edge line.
                        | markings: The channelizing markings ahead indicate a change in road geometry or a
                        lane termination, consistent with the wide markings seen in both photos. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line on the right marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            area:channelizing: The channelizing lines indicate that vehicles must follow the set
                        path and may not drive on or across the lines. [[CN-6.6.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not move to the right as it
                        is bounded by a solid edge line. Follow the channelizing markings ahead to navigate
                        the road geometry change.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 989, 8.91 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view of the road ahead. There is a
                        green overhead sign and a white car in the lane to the left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right. Photo 2 shows a white solid line on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white broken line on the left and a white solid line
                        on the right. | roles: The white broken line on the left correctly functions as a lane
                        line, and the white solid line on the right functions as an edge line. | markings: No
                        markings are present in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows for lane changes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not attempt to move to the
                        right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 844, 8.17 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a sound barrier on both sides. The road ahead
                        appears to be a straight stretch of highway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line clearly near the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows the same white broken line clearly near the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white broken lines on both sides, which indicate lanes of the same
                        direction. | roles: The white broken lines correctly function as lane lines between
                        lanes of the same direction. | markings: No markings are present in my lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows my car to change lanes to the right.
                        [[CN-5.2.3]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.3].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes [CN-5.2.3].
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight.
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may change lanes to the left
                        or right as needed, and you may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 851, 10.95 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a sound barrier on the right. The road ahead
                        is straight with mountains visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows a white broken line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a physical barrier/curb.
                        Photo 2 shows a solid white line next to the car and a solid white line further ahead.
                        A metal guardrail and sound barrier are on the far right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white dashed line in the center of my
                        lane, but it appears to be a lane divider for the lane to my left, not a marking
                        inside my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white broken line on the left and a white solid line/curb
                        on the right. | roles: The white broken line on the left fits the role of a crossable
                        lane line. The white solid line on the right fits the role of an edge line. |
                        markings: No markings are clearly inside my lane; the dashed line seen is a boundary
                        for the left lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The white edge line on the right marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.3]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and physical barrier
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane as the line is broken, but
                        you are prohibited from moving to the right due to the solid edge line and physical
                        barrier. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 922, 8.16 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a curve ahead. My car is in a lane bounded by a physical
                        barrier on the left and a curb/barrier on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a physical barrier (metal railing and concrete wall) on the left. Photo
                        2 shows the same physical barrier.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line on
                        the right.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows a white grid/box marking in the middle of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a physical barrier on the left and a dashed
                        line/curb on the right define the lane. | roles: The left edge line (barrier) and
                        right edge line (dashed white line) are consistent with the road layout. | markings:
                        The grid marking is centered in the lane and does not conflict with the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: no marking governs this action [null]
Step 5  Rule            right_boundary: no marking governs this action [null]
Step 5  Rule            area:grid: no marking governs this action [null]
Step 6  change_left     prohibited (WRONG, label allowed): no marking governs this action
Step 6  change_right    allowed (WRONG, label prohibited): no marking governs this action
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane bounded by a barrier on the left and a dashed line on the right. You
                        may move to the right if needed, but you should avoid stopping in the grid area ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe ['change_right'], citation unlisted,
                        contradictions ['change_right allowed across a curb']
Tokens                  in 8458, out 851, 8.58 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane bridge or elevated roadway with a bus directly
                        ahead. The road is bounded by metal guardrails on both sides. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line to the left of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        No markings are present, which is consistent with the lane boundaries. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from the left side into the
                        adjacent lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from the right side into the
                        adjacent lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8458, out 846, 8.9 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or elevated road with overhead lane signs. The road ahead is
                        straight with several lanes of traffic moving in the same direction. (lanes 4, mine 3,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the one to its left. Photo 2 shows
                        this line as a broken white line (dashed) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the one to its right. Photo 2 shows
                        this line as a broken white line (dashed) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with the white lane lines on both sides. | roles: The white
                        dashed lines correctly function as crossable lane lines between lanes of the same
                        direction. | markings: No markings are present, which is consistent with a standard
                        through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows my car to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line on the left [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line on the right [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may change lanes to the left or right as needed, and
                        you may continue straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 849, 9.57 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median on the left and a sidewalk/parking area on the
                        right. Ahead, there is a slight curve and an overpass. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a median strip on the left. Photo 2 shows a raised
                        curb and a median strip on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a curb on the left and a white dashed line on the
                        right. | roles: The curb acts as a left edge line and the white dashed line acts as a
                        right lane line. | markings: No markings are present in the lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: no marking governs this action [null]
Step 5  Rule            right_boundary: The broken white line allows for lane changes to the right.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     prohibited (correct): no marking governs this action
Step 6  change_right    allowed (WRONG, label prohibited): The white dashed line on the right allows for lane
                        changes to the right per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane.
                        Changing to the left is prohibited by the curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_right'], citation
                        unlisted, contradictions []
Tokens                  in 8458, out 821, 7.87 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a central median and a sidewalk on the right. Ahead,
                        there is a clear roadway with a car in the adjacent lane and a motorcycle on the
                        right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a concrete median/barrier on the left. Photo 2 shows the concrete
                        median/barrier clearly on the left.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a median on the left and a white line on the right. |
                        roles: The concrete median acts as a left edge line, and the white line acts as a
                        right lane line. | markings: No markings are present in the lane. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: no marking governs this action [null]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     allowed (WRONG, label prohibited): no marking governs this action
Step 6  change_right    prohibited (correct): prohibited by the solid white line on the right (CN-6.2.1)
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the left lane of a two-lane roadway. You may proceed straight or change to
                        the left if necessary, but you are prohibited from changing into the right lane due to
                        the solid white line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        unlisted, contradictions ['change_left allowed across a curb']
Tokens                  in 8458, out 826, 7.98 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass on the right. My car is in a lane
                        heading straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line on the left. Photo 2 shows a solid yellow line next to the
                        car and a solid yellow line further ahead.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a solid white line next to the
                        car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The yellow line on the left and white
                        line on the right correctly identify my lane as the leftmost lane of the direction of
                        travel (lane 1). | roles: The yellow edge line on the left and white lane line on the
                        right are consistent with the direction of travel. | markings: The straight arrow is
                        consistent with the lane's role and boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the adjacent lane.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          allowed: allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn in this lane. Lane changes to the
                        left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 857, 7.36 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. The road is straight, and there are
                        buildings and trees on both sides. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows a solid white line on the
                        left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        no_turn:left (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a white edge line on the left and a white lane line on
                        the right. | roles: The white solid lines correctly serve as an edge line (left) and a
                        lane line (right). | markings: No markings are present, which is consistent with the
                        straight road ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: no marking governs this action [null]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 774, 13.18 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian overpass on the right. The car is traveling
                        straight ahead in a lane bounded by a median and a sidewalk. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left. Photo
                        2 shows a solid yellow line next to the car and a raised concrete median further
                        ahead.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the sidewalk. Photo 2 shows a white
                        line next to the car and a raised curb further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white lane-use arrow pointing straight
                        ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a white edge line is
                        on my right. | roles: The yellow solid line correctly identifies a center line, and
                        the white solid line correctly identifies an edge line. | markings: The straight arrow
                        in my lane is consistent with the lane's role and the boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits crossing into the lane to the
                        left. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          allowed: allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn in this lane. Lane changes to the
                        left or right are prohibited by the solid boundary lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 885, 9.46 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees and buildings on both sides. The road ahead appears
                        to be a straight stretch with a median separating opposing traffic. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        the middle of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a white line on the left separates me from another
                        lane, and a white line/curb on the right marks the edge. | roles: The white solid line
                        on the left is a lane line, and the white solid line on the right is an edge line. |
                        markings: The straight arrow in my lane is consistent with the lane's purpose. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          allowed: allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn in your current lane. Lane changes
                        to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 892, 8.54 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide sidewalk and a median on the left. Ahead, there is
                        a clear roadway with a car and a cyclist in the distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a median/sidewalk area. Photo
                        2 shows a solid white line next to the car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to the car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the boundaries: a white edge line on the left and a white lane line on the
                        right. | roles: The white solid lines correctly function as an edge line (left) and a
                        lane line (right). | markings: No markings are present to contradict the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: no marking governs this action [null]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane on the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     allowed (WRONG, label prohibited): no marking governs this action
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line (CN-6.2.1)
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may proceed straight ahead. Lane
                        changes to the right are prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        unlisted, contradictions ['change_left allowed across a curb']
Tokens                  in 8458, out 839, 9.05 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an overpass to the left and a tree-lined sidewalk to the
                        right. The road ahead appears to be a straight stretch with multiple lanes of traffic.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows this line is a solid
                        white line near my car. Further ahead in Photo 1, it remains solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white dashed line on the left and a solid white line on the
                        right. | roles: The white dashed line on the left correctly functions as a lane line,
                        and the solid white line on the right functions as an edge line. | markings: The
                        straight arrow in my lane is consistent with the lane's role and the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       prohibited: prohibited by the arrow which does not show a left turn [CN-5.13.1]
Step 6  turn_right      prohibited: prohibited by the arrow which does not show a right turn [CN-5.13.1]
Step 6  u_turn          allowed: allowed by the arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn in this lane. You are permitted to
                        change lanes to the left, but changing to the right is prohibited by the solid edge
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 994, 8.4 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a dedicated bicycle and scooter lane on a city street. My car is
                        positioned at the start of this lane, which is separated from the main roadway by a
                        curb and a fence. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line on the left. Photo 2 shows a white solid line on the
                        left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a raised curb and a metal fence on the right. Photo 2 shows a raised
                        curb and a metal fence on the right.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 1 shows a large white arrow pointing straight
                        ahead in the center of the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries (left lane line, right curb). | roles: The white solid
                        line on the left and the curb on the right correctly define the lane. | markings: The
                        straight arrow is consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The curb/edge defines the right limit of the lane. [CN-5.4.3] "An edge
                        line on the right side of the direction of travel shall be white, and an edge line on
                        the left side of the direction of travel shall be yellow; a motor/"
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [CN-5.13.1] "Guide arrows indicate the direction of travel
                        for vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          allowed (WRONG, label prohibited): allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane to go straight ahead or perform a U-turn. Lane changes to the left or
                        right are prohibited by the solid line and the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight']), actions False, unsafe
                        ['u_turn'], citation accepted, contradictions ['leftmost lane, but a lane line on the
                        left']
Tokens                  in 8458, out 850, 6.62 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a median on the left and a sidewalk on
                        the right. My car is in a lane heading straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the median. Photo 2 shows a
                        solid yellow line next to my car.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the boundaries: a yellow center line is on my left and a white lane line is
                        on my right. | roles: The yellow solid line correctly identifies a center line
                        (separating opposing traffic), and the white solid line correctly identifies a lane
                        line. | markings: No markings were observed. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane and proceed straight ahead. Lane changes to the
                        left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 8458, out 809, 7.82 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a sidewalk and trees on the left. Ahead, there is a clear
                        roadway with several lanes of traffic moving in the same direction. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line on the left, which appears to be a lane line or edge
                        line. Photo 2 shows a solid white line very close to the car, and further ahead, it
                        remains a solid white line.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line
                        immediately to the right of the car's lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a solid white line on the left (edge line) and a solid
                        white line on the right (lane line). | roles: The white solid lines correctly
                        represent an edge line on the left and a lane line on the right. | markings: No
                        markings are present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white edge line on the left marks the boundary of the motor vehicle
                        lane. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing from the side of the
                        solid line. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may proceed straight ahead, but
                        you are prohibited from changing lanes to the left or right due to the solid white
                        lines.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 845, 8.83 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a median and a sidewalk on the right. Ahead, there is a
                        clear road section with a blue overhead sign indicating lane directions. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        a single yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a yellow line and a raised curb on the right. Photo 2 shows a yellow
                        line and a raised curb next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): Photo 2 shows a white dashed line between my lane and
                        the lane to my left.; line:crosswalk (insufficient): Photo 2 shows a white dashed line
                        between my lane and the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left and a yellow edge
                        line is on my right. | roles: The yellow solid center line and yellow solid edge line
                        fit the roles of center line and edge line respectively. | markings: The white dashed
                        line is a lane line, not a crosswalk line. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid yellow center line prohibits crossing into the left lane.
                        [[CN-6.1.1]]
Step 5  Rule            right_boundary: The yellow edge line marks the left-hand edge of the direction of
                        travel (in this context, the right side of the roadway). [[CN-5.4.3]]
Step 5  Rule            line:crosswalk: no marking governs this action [null]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line and curb
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the direction of travel. You may proceed straight
                        ahead, but lane changes to the left or right are prohibited by the solid yellow lines
                        and the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 782, 9.05 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a white fence on the left and a sidewalk/curb on the
                        right. Ahead, there is an intersection with traffic lights and a pedestrian crossing.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car and a sidewalk/curb further ahead. There is a physical curb/barrier on the
                        far right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (partial): Photo 2 shows a white dashed line in the middle of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white dashed line on the left and a solid white line/curb
                        on the right. | roles: The white dashed line on the left is a lane line; the solid
                        white line/curb on the right is an edge line. | markings: The dashed line in the
                        middle of the lane appears to be a lane-change or guide line, but no specific arrows
                        or words are visible. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the boundary is a broken white line. Do not
                        attempt to move to the right as it is bounded by a solid white line and a curb.
                        Proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 904, 8.2 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. Ahead, there is a car
                        in the lane directly in front of my car. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        a single solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a single solid white line next
                        to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1 shows a white arrow in my lane pointing straight
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left and a white edge
                        line is on my right. | roles: The yellow solid line correctly identifies a center
                        line, and the white solid line correctly identifies an edge line. | markings: The
                        straight arrow in my lane is consistent with the lane's role and boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            arrow:straight_right: The guide arrow indicates the direction of travel for vehicles
                        is straight ahead or to the right. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      allowed: allowed
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 860, 9.12 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bicycle lane on the right. The car is in a
                        lane next to a bus lane, heading towards a distant intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left
                        (occupied by a bus). Photo 2 shows this same solid yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a bicycle lane on the right.
                        Photo 2 shows this solid white line clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white arrow in the lane to my left
                        indicating a straight-ahead movement. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a yellow center line on the left and a white edge
                        line on the right. | roles: The yellow solid line correctly identifies a center line
                        separating opposing flows (or a bus lane), and the white solid line correctly
                        identifies the edge of the motor vehicle lane. | markings: No markings are in my lane,
                        which is consistent with the lane's role. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits crossing into the lane to the
                        left. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The single solid white line prohibits crossing into the bicycle lane
                        on the right. [[CN-6.2.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left (into the bus lane)
                        or to the right (into the bicycle lane) are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8458, out 852, 8.33 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees and buildings on both sides. Ahead, there is a wide
                        intersection or open area with a vehicle in the lane directly ahead. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this same yellow line clearly as a solid line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a raised curb and a sidewalk on the right. Photo 2 shows a solid white
                        line painted on the curb/pavement edge.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        no_turn:left (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left, and a white edge
                        line is on my right. | roles: The yellow solid line correctly identifies a center line
                        separating opposing traffic, and the white line/curb correctly identifies the right
                        edge. | markings: No markings were observed in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may proceed straight ahead, but
                        you are prohibited from changing lanes to the left due to the solid yellow center
                        line. No turn markings are present, so stay in your lane for straight travel.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 845, 9.39 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a wide intersection or junction ahead. My car is in one
                        of the middle lanes. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the one to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the one to my right. Photo 2 shows
                        this white line as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (full): Photo 1 shows a white left-turn arrow in the lane to my left. No
                        markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        No markings are in my lane, and the left-turn arrow is in the adjacent lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8458, out 804, 7.52 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street with an intersection ahead. My car is in a
                        lane that appears to be a dedicated turn lane or a lane with specific guidance
                        markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the sidewalk/pedestrian area on the
                        right. Photo 2 shows this line as a solid white line next to my car, and a raised curb
                        is visible further ahead on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a large white arrow in my lane pointing
                        straight and to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane line on my left and the white edge line/curb on my
                        right. | roles: The white solid line on the left correctly acts as a lane line, and
                        the white solid line on the right acts as an edge line. | markings: The straight-right
                        arrow in my lane is consistent with the lane's position and the surrounding
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the roadway. [[CN-5.4.3]
                        [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight_right: The arrow indicates that the allowed movements in this lane are
                        straight ahead or turning right. [[CN-5.13.2] [mandatory] GB 5768.3-2025, section
                        5.13.2, page 27]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      allowed (correct): allowed
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn right. Do not attempt to
                        change lanes or turn left from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 8458, out 992, 10.62 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a tunnel or underpass ahead. My car is in a lane moving
                        forward towards the underpass. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which appears to be the edge of the
                        roadway or a separation from a sidewalk/curb area. Photo 2 shows this white solid line
                        clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): Photo 1 shows white dashed lane lines separating the
                        three lanes of my direction.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed line on the left and the white solid line on the
                        right. | roles: The white dashed line correctly functions as a lane line, and the
                        white solid line correctly functions as an edge line. | markings: No specific arrows
                        or words are visible in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change to the left lane if needed, but you should not move to the right as it
                        is the edge of the roadway. Proceed straight ahead toward the underpass.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 855, 8.55 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway under an overpass. The road ahead appears to be a
                        continuous stretch of lanes with no immediate intersection or ramp visible in the
                        immediate foreground. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right. Photo 2 shows a white solid line next
                        to my car and a white solid line further ahead. There is a raised concrete
                        curb/barrier to the right of that line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:left_turn_waiting (insufficient): Photo 1 shows a white dashed line in the lane
                        to my left, but no markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with a white dashed line on my left and a white solid
                        line/curb on my right. | roles: The white dashed line on the left correctly identifies
                        a lane-line, and the white solid line with a curb on the right correctly identifies an
                        edge-line. | markings: No markings were found in my lane; the left-turn waiting area
                        is in the adjacent lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line on the right marks the boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and curb
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the lane to your left. Do not attempt to move
                        to the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:left_turn_waiting'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 903, 8.29 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows the same white broken line clearly next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be a road edge line.
                        Photo 2 shows this solid white line clearly next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): Photo 1 shows a white dashed line in the middle of my
                        lane, but it is a lane-change line (1-1 line) as it is further ahead.;
                        area:left_turn_waiting (insufficient): No other markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white broken line on the left and a white solid line on the
                        right. | roles: The white broken line on the left is a lane line; the white solid line
                        on the right is an edge line. | markings: No specific arrows or words are visible in
                        my lane to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.3]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change to the left lane if needed, but you are prohibited from moving to the
                        right beyond the edge line. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'line:crosswalk'], missed []), actions True, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 8458, out 904, 7.44 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a narrow paved road or access path passing under a bridge. Ahead, there
                        is a white van parked or stopped in the lane. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a low hedge and a curb-like edge on the left. Photo 2 shows a distinct
                        curb and a dense hedge/shrubbery on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a red wall and a sidewalk on the right. Photo 2 shows a sidewalk and a
                        red wall on the right.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the physical boundaries (curbs/walls) on both sides. | roles: The
                        physical boundaries correctly serve as edge lines. | markings: No markings are present
                        in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: no marking governs this action [null]
Step 5  Rule            right_boundary: no marking governs this action [null]
Step 6  change_left     not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  change_right    not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  The lane is bounded by a hedge on the left and a wall on the right. Proceed straight
                        with caution as there is a vehicle ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8458, out 724, 8.86 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching a large intersection. My car is in
                        a lane that appears to be a dedicated turn lane or a lane with specific guidance
                        markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this same white line clearly as a solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a metal fence/barrier on the right. Photo 2 shows a metal fence/barrier
                        immediately to the right of my lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a large white left-turn arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on the left and a fence on the right. | roles:
                        The white solid line correctly identifies a lane-line, and the fence correctly
                        identifies an edge-line. | markings: The left-turn arrow in my lane is consistent with
                        the lane's position and the surrounding context. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: no marking governs this action [no marking governs this action]
Step 5  Rule            arrow:left: The arrow indicates that the lane is for turning left. [[CN-5.13.1]
                        [informative] GB 5768.3-2025, section 5.13.1, 表1, page 27]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the physical barrier/curb
Step 6  go_straight     prohibited (correct): prohibited by the left-turn arrow [CN-5.13.1]
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the left-turn arrow [CN-5.13.1]
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the left-turn arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the left-turn arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Use this lane specifically to turn left at the upcoming intersection. Do not attempt
                        to change lanes or go straight, as the markings and boundaries prohibit these actions.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed ['arrow:right', 'line:stop_line']), actions False, unsafe
                        ['turn_left'], citation unlisted, contradictions []
Tokens                  in 8458, out 1002, 9.52 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway under an overpass. The road ahead is straight with
                        several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 1 shows a white arrow in my lane pointing straight
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries (white lines on both sides). | roles: The white solid
                        lines correctly function as lane lines separating traffic in the same direction. |
                        markings: The straight arrow in my lane is consistent with the lane's role and the
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1,
                        表1, page 27]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          allowed: allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight travel or U-turns. Lane changes to the left
                        or right are prohibited by the solid white lines. Proceed straight or perform a U-turn
                        as indicated by the lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 961, 6.01 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear view ahead. The road appears to be a
                        straight stretch with several lanes in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this line is solid white and there is a guardrail and a curb-
                        like structure further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a large white circle with '60' inside it in my
                        lane.; text:speed_limit (full): Photo 1 shows a large white circle with '80' in the
                        lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white lane line is on my left and a white edge
                        line is on my right. | roles: The white dashed line on the left fits the role of a
                        crossable lane line, and the solid white line on the right fits the role of an edge
                        line. | markings: The speed limit markings are consistent with the lane layout. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            text:speed_limit: The '60' marking indicates a maximum speed limit of 60 km/h for this
                        lane. [[CN-5.14.2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane with a speed limit of 60 km/h. You may change lanes to the
                        left, but you are prohibited from moving to the right onto the shoulder or beyond the
                        edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 1010, 9.81 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus and a van in adjacent lanes. The road ahead appears
                        to be a straight stretch with an intersection or signalized area in the distance.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane's role and the surrounding
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [CN-5.13.1] "Guide arrows indicate the direction of travel
                        for vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          allowed: allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from your current lane. Lane
                        changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 864, 9.56 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear sky. Ahead, there are other vehicles
                        and a motorcycle. My car is in one of the middle lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line to the left of my lane. Photo 2 shows a white dashed
                        line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right of my lane. Photo 2 shows a white
                        dashed line clearly visible next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the white dashed lines on both sides, which indicate a lane between two
                        other lanes. | roles: The white dashed lines correctly function as lane lines
                        separating traffic in the same direction. | markings: No markings were observed, which
                        is consistent with the clear road surface. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows my car to change lanes to the right.
                        [[CN-5.2.3]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.3].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes [CN-5.2.3].
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a middle lane with broken white lines on both sides, allowing you to change
                        lanes to the left or right if necessary. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 861, 8.55 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane divided highway with a clear view of the road ahead. The car is traveling
                        in a lane with white markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line clearly as a broken white line near the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line clearly as a broken white line near the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane in
                        Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: No markings were observed in the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows my car to change lanes to the right.
                        [[CN-5.2.3]]
Step 6  change_left     allowed (correct): allowed by the broken white left boundary line [CN-5.2.3]
Step 6  change_right    allowed (correct): allowed by the broken white right boundary line [CN-5.2.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may change lanes to the left
                        or right as the lane markings are broken. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8458, out 833, 9.38 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a clear road ahead. The car is traveling in a
                        lane that appears to be one of the rightmost lanes. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be an edge line. Photo
                        2 shows this solid white line clearly next to a raised curb/barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3)
                        are consistent with the boundaries: a white dashed line on the left and a white solid
                        line/curb on the right. | roles: The white dashed line on the left correctly functions
                        as a lane line, and the white solid line on the right correctly functions as an edge
                        line. | markings: No markings were observed, which is consistent with the clear road
                        ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left as the line is broken. Do not attempt to move to the
                        right as it is bounded by a solid edge line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 872, 9.0 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or expressway under an overpass. Ahead,
                        there is a merging or lane-reduction area with multiple lanes of traffic. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this same yellow line clearly as a solid line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this white line as a solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white line further ahead that appears
                        to be a lane-change line or a guide line, but no specific arrows or words are visible
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow center line is on my left and a white lane line is
                        on my right. | roles: The yellow center line correctly identifies the left boundary
                        (separating opposing traffic) and the white line identifies the right boundary
                        (separating same-direction traffic). | markings: No specific arrows or words are
                        visible in my lane to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 849, 8.05 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a physical barrier on the left and a wide shoulder or
                        adjacent lanes on the right. The sun is low in the sky, creating a hazy atmosphere.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a physical barrier (guardrail and concrete posts) on the left. Photo 2
                        shows a solid white line next to the car, and further ahead, the line appears to be a
                        solid white line bordering the barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line on the right. Photo 2 shows a white dashed line with
                        clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): Photo 2 shows a white dashed line separating my lane
                        from the lane to the right.; area:left_turn_waiting (insufficient): No other markings
                        are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the left edge line and right lane line. | roles: The white solid
                        line on the left acts as an edge line, and the white dashed line on the right acts as
                        a lane line. | markings: No specific arrows or words are present to contradict the
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The white edge line on the left marks the boundary of the motor vehicle
                        lanes. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white line allows for lane changes to the right.
                        [[CN-5.2.3]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change into the right lane.
                        Changing into the left lane is prohibited by the physical barrier and edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'line:crosswalk'], missed []), actions True, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 8458, out 883, 9.52 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with a clear view of the road ahead. There are no immediate
                        intersections or ramps visible in the immediate foreground. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows the same white broken line clearly as a dashed line with distinct gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to my right. Photo
                        2 shows this white broken line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle lane, index 2) agree with the white broken lines on both sides. | roles: The
                        white broken lines correctly function as lane lines between lanes of the same
                        direction. | markings: No markings were observed in the lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows my car to change lanes to the right.
                        [[CN-5.2.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line on the left [CN-5.2.3]
Step 6  change_right    allowed (correct): allowed by the broken white lane line on the right [CN-5.2.3]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may change lanes to the left
                        or right as the lane markings are broken white lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8458, out 834, 10.66 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a physical barrier on the left and a paved
                        shoulder/curb area on the right. The road ahead is straight. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line and a metal guardrail on the left. Photo 2 shows a
                        solid white line next to the car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): None visible in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego lane index
                        (1) are consistent with a left edge line (guardrail/solid white) and a right lane line
                        (solid white). | roles: The white solid lines correctly represent a left edge line and
                        a right lane line. | markings: No markings are present, which is consistent with the
                        straight road ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The left edge line is white, marking the boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing from the side of the
                        solid line. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8458, out 807, 6.77 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a gantry overhead. The road ahead is straight
                        with several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a broken white line (dashed) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line is a broken white line (dashed) with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white dashed
                        lines correctly function as crossable lane lines. | markings: The straight arrow in my
                        lane is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is intended for straight
                        ahead or U-turn movements. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       prohibited: prohibited by the arrow which does not show a left turn [CN-5.13.2]
Step 6  turn_right      prohibited: prohibited by the arrow which does not show a right turn [CN-5.13.2]
Step 6  u_turn          allowed: allowed by the arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left or right as needed. You are permitted to go straight
                        or perform a U-turn, but left and right turns are prohibited in this lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions False, unsafe ['change_left'], citation
                        accepted, contradictions []
Tokens                  in 8458, out 953, 9.32 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overpass to the right. The road ahead is
                        straight with several lanes of traffic moving in the same direction. (lanes 4, mine 3,
                        full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows a white broken line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway or a barrier. Photo 2 shows a solid white line next to a metal guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (3rd
                        from left) are consistent with a white broken line on the left and a solid white
                        line/guardrail on the right. | roles: The white broken line on the left correctly
                        identifies a lane-changeable lane line, and the solid white line on the right
                        correctly identifies the edge of the roadway. | markings: No markings were observed in
                        the lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and guardrail
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the third lane from the left. You may change into the lane to your left as
                        it is separated by a broken white line. Do not attempt to move to the right as there
                        is a solid white line and a guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 892, 8.5 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees and buildings on both sides. The road ahead appears
                        to be a straight stretch with multiple lanes of traffic moving in the same direction.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows a white broken line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to my right. Photo
                        2 shows a white broken line with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white broken lines on both sides. | roles: The
                        white broken lines correctly function as lane lines separating traffic in the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane lines
                        and the straight road ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white line allows me to change lanes to the right.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows lane changes
                        [CN-5.2.1-2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows lane
                        changes [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): The arrow in my lane indicates that going straight is an
                        allowed movement [CN-5.13.1].
Step 6  turn_left       prohibited: The arrow in my lane does not show a left turn, and the lane is for
                        straight or U-turn [CN-5.13.1].
Step 6  turn_right      prohibited: The arrow in my lane does not show a right turn, and the lane is for
                        straight or U-turn [CN-5.13.1].
Step 6  u_turn          allowed: The arrow in my lane indicates that a U-turn is an allowed movement
                        [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may go straight or perform a U-turn. Lane changes to
                        the left or right are permitted. Do not attempt to turn left or right from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_u_turn'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 853, 8.53 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test B | gemma4:12b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an upcoming intersection or exit area. My car
                        is in a lane with large white markings on the pavement. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line and a metal guardrail on the right. Photo 2 shows the white
                        line and the guardrail clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows large white characters '直' (straight) in my lane.;
                        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane
                        further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on the left and a white edge line/guardrail on
                        the right. | roles: The white solid line on the left is a lane line; the white solid
                        line on the right is an edge line. | markings: The '直' (straight) text and the
                        straight arrow are consistent with each other and the lane's role. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            text:other: The '直' character indicates the lane is for straight movement.
Step 5  Rule            arrow:straight: The arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel, as indicated by the '直'
                        character and the straight arrow. Do not attempt to change lanes or turn, as the solid
                        white lines on both sides prohibit crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'text:other'], missed ['text:speed_limit']), actions False, unsafe
                        [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 777, 8.22 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane approaching a
                        set of traffic lights and overhead signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows the same solid
                        white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the double solid yellow line on the left (center line) and the
                        solid white line on the right (lane line). | roles: The double solid yellow line
                        correctly identifies the center line, and the solid white line correctly identifies
                        the lane line. | markings: No markings were observed, which is consistent with the
                        lack of specific lane-use indicators. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right due to the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 660, 7.3 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a clear view ahead. The car is in a lane with a white
                        line on its right and a yellow line on its left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line on the left. Photo 2 shows a solid yellow line next to the
                        car and a broken-solid yellow line further ahead.
                        yellow solid_dashed (near line solid), curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a solid white line next to the
                        car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow in the lane ahead pointing
                        straight.
Step 4  Cross-check     close_up: The close-up shows the left boundary is a broken-solid yellow line further
                        ahead, while the right boundary is a solid white line. These match the general layout
                        in Photo 1. | position: The lane count (3) and my position (2) are consistent with a
                        yellow center line on the left and a white lane line on the right. | roles: The yellow
                        line on the left correctly identifies a center line separating opposing traffic, and
                        the white line on the right separates lanes in the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid side of the broken-solid yellow line may not
                        cross. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from the solid-line side.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Do not attempt to change lanes
                        or turn left/right, as the solid lines and lane markings prohibit these actions.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 904, 9.83 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a tram/bus lane on the right. The road ahead appears to
                        be a straight stretch leading towards a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows the same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line separating my lane from the tram/bus lane on the
                        right. Photo 2 shows this solid yellow line clearly.
                        yellow solid, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1 shows a white arrow in my lane pointing straight
                        ahead. Photo 2 shows the arrow clearly.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on the left and a yellow line on the
                        right. | roles: The white line on the left is a lane line; the yellow line on the
                        right is a special lane line (bus/tram lane). | markings: The straight-right arrow is
                        consistent with the lane's role and boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid yellow line prohibits vehicles other than buses from
                        entering the lane to the right. [[CN-6.9.1] [mandatory] GB 5768.3-2025, section 6.9.1,
                        page 54]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane allows for straight ahead or
                        right turn movements. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1, 表1,
                        page 27]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      allowed: allowed
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn right from your current lane. Lane changes to the
                        left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': None}, markings False (added
                        ['arrow:straight_right'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 969, 9.44 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with several vehicles moving in the same direction. There is a
                        clear road ahead with a blue overhead sign and a sidewalk on the right. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this line is a solid yellow line next to my car and remains solid further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a solid white line next to my car and remains solid further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): No markings are visible in my lane in
                        Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a yellow center line is on my left and a white
                        lane line is on my right. | roles: The yellow center line correctly identifies the
                        boundary with opposing traffic, and the white line correctly identifies the boundary
                        with the adjacent lane. | markings: No markings were observed in my lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right due to the solid lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 843, 7.2 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a subway station on the right. Ahead, there is an
                        intersection with traffic signals and a subway entrance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which appears to be the edge of the
                        roadway or a separation from a transit area. Photo 2 shows a solid yellow line next to
                        my car.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 1 shows a large white arrow in my lane pointing
                        straight ahead.; symbol:other (full): Photo 2 shows a white triangle marking on the
                        ground in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on the left and a yellow edge line on the right.
                        | roles: The white lane line on the left and yellow edge line on the right fit the
                        roles of a lane line and an edge line respectively. | markings: The straight-ahead
                        arrow and the triangle marking are consistent with the lane's purpose. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The yellow edge line marks the right-hand edge of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.2] [mandatory] GB 5768.3-2025, section 5.13.2, page
                        27]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      allowed (WRONG, label prohibited): allowed
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or turn right from your current lane. Lane changes to
                        the left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right', 'symbol:other'], missed ['arrow:straight']), actions False,
                        unsafe ['turn_right'], citation unlisted, contradictions []
Tokens                  in 8458, out 1008, 10.35 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus lane or special lane on the right. There is a bus
                        stop on the left and a white van ahead in the center lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken-solid line separating my lane from the lane to the left.
                        Photo 2 shows a yellow broken-solid line with the dashed part closer to my lane.
                        yellow solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line and a solid white line further right. Photo 2 shows
                        a solid yellow line immediately to the right of my lane, and a solid white line
                        further right.
                        yellow solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 1 shows a white arrow pointing straight ahead in
                        my lane. Photo 2 shows a white arrow pointing straight ahead.; text:bus (full): Photo
                        1 shows a yellow '公交' (BUS) marking and a yellow arrow in the lane to my right. Photo
                        2 shows the yellow '公交' text and a yellow arrow clearly in the rightmost lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a yellow line on the left and a yellow line on the right
                        indicate I am in a middle lane. | roles: The yellow broken-solid line on the left and
                        solid yellow line on the right correctly identify the lane boundaries. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. The '公交' marking is
                        clearly in the right lane, not my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Vehicles on the broken side (my side) may cross the line, but must give
                        way to vehicles travelling normally. [[CN-6.2.3]]
Step 5  Rule            right_boundary: The solid white/yellow line prohibits crossing from the solid side.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (contested, correct): allowed by the broken-solid line (broken side)
                        [CN-6.2.3]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       allowed: allowed by the U-turn component of the arrow [CN-5.13.1]
Step 6  turn_right      prohibited: prohibited by the arrow which does not show a right turn [CN-5.13.2]
Step 6  u_turn          allowed: allowed by the U-turn component of the arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight, make a U-turn, or change into the left lane if safe. Do not
                        attempt to change into the right lane, which is a reserved bus lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn', 'text:bus'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['turn_left allowed although no arrow shows it']
Tokens                  in 8458, out 1108, 9.63 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with traffic moving in the same direction. An intersection or
                        large crossing is visible ahead under bright sunlight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows two
                        solid yellow lines side by side.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a single solid white line to the right of my lane. Photo 2 shows a
                        single solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (insufficient): No markings are visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The double yellow line on the left
                        indicates a center line separating opposing traffic, and the white line on the right
                        separates my lane from the adjacent lane. This is consistent with being in the middle
                        lane of three. | roles: The yellow double solid line correctly identifies a no-
                        crossing center line. The white solid line correctly identifies a no-crossing lane
                        line. | markings: No markings were observed in my lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right due to the solid lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8458, out 816, 8.98 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus in the center lane. The road ahead appears to be a
                        straight stretch or an approach to an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a solid white line near my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.
Step 4  Cross-check     close_up: The same in both photos. | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white lines
                        correctly identify lane boundaries between lanes of the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane's role and the white
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change into the left lane.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The solid white line prohibits my car from changing into the right
                        lane. [[CN-6.2.1]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white left boundary [CN-5.2.3]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary
                        [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed by the straight arrow in my lane [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the arrow which does not show a left turn
Step 6  turn_right      prohibited (correct): prohibited by the arrow which does not show a right turn
Step 6  u_turn          allowed (WRONG, label prohibited): allowed by the arrow which shows a U-turn
                        [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from your current lane. You are
                        permitted to change into the left lane but are prohibited from changing into the right
                        lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight']), actions False, unsafe
                        ['u_turn'], citation accepted, contradictions []
Tokens                  in 8458, out 944, 14.46 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken-solid yellow line (solid on the left, broken on the right) near
                        my car, but it appears to be a single solid yellow line further ahead.
                        yellow solid_dashed (near line dashed), curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a broken white line near my car and remains broken further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 2 shows a white left-turn arrow in the lane to my
                        left. No markings are visible in my lane.
Step 4  Cross-check     close_up: The left boundary is a broken-solid yellow line near the car (Photo 2) and a
                        solid yellow line further ahead (Photo 1). Photo 2 decides the near-line (dashed). |
                        position: The lane count (3) and my position (2) are consistent with a yellow center
                        line on the left and a white lane line on the right. | roles: The yellow center line
                        and white lane line fit their respective roles. | markings: No markings are in my
                        lane; the left-turn arrow is in the adjacent lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Vehicles on the broken side of the broken-solid yellow line may cross,
                        while the solid side is normally prohibited. [[CN-6.1.3]]
Step 5  Rule            right_boundary: The broken white line allows for lane changes. [[CN-5.2.3]]
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the markings
                        allow. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 872, 8.11 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching a large intersection with a
                        crosswalk. My car is positioned in a lane heading towards the intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line (dashed) near the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line as a solid white line
                        near the car. Further ahead in Photo 1, the line appears to remain solid.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white crosswalk across the lanes ahead.
Step 4  Cross-check     close_up: The close-up (Photo 2) confirms the left boundary is a broken white line and
                        the right boundary is a solid white line. The crosswalk is visible in both. |
                        position: The lane count of 3 and my position as lane 2 (middle) are consistent with a
                        white line on my left and a white line on my right. | roles: The white lines correctly
                        function as lane lines separating traffic in the same direction. | markings: The
                        crosswalk is consistent with an intersection approach. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change into the lane on the
                        left. [[CN-5.2.3]]
Step 5  Rule            right_boundary: The solid white line prohibits my car from crossing into the lane on
                        the right. [[CN-6.2.1]]
Step 5  Rule            line:crosswalk: No specific rule provided for crosswalks in the list, but they
                        generally indicate a pedestrian crossing area.
Step 6  change_left     allowed: allowed by the broken white line [CN-5.2.3]
Step 6  change_right    prohibited: prohibited by the solid white line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from changing into
                        the right lane. Proceed straight through the intersection, being mindful of the
                        crosswalk.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 934, 14.48 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a taxi to the left and a bus lane to the
                        right. Ahead, there is a large overhead gantry with signs and a clear intersection
                        area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the lane to the left.
                        Photo 2 shows the same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a red-paved bus lane on the
                        right. Photo 2 shows this solid white line clearly.
                        white solid, curb no, special_lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 1 shows a white lane line further ahead in my
                        lane, but no arrows or text are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the double yellow center line on the left and the white special
                        lane line on the right. | roles: The yellow double solid line correctly identifies a
                        center line, and the white solid line correctly identifies a special lane boundary. |
                        markings: No markings are visible in my lane to contradict the boundaries. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The bus lane line indicates that vehicles other than buses shall not
                        enter the lane. [[CN-6.9.1]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane. Changing lanes to the left is prohibited by the
                        double solid yellow line, and changing to the right is prohibited as it leads into a
                        bus lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 847, 8.81 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bus lane or special lane on the right. The
                        road continues straight ahead into a city area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to the left. Photo 2
                        shows this same yellow line clearly as a broken line near the car.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line and a thick yellow-painted area with symbols on the
                        right. Photo 2 shows a solid yellow line and a large yellow-painted area with a bus
                        symbol and '公交' text.
                        yellow solid, curb no, special_lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows a large yellow bus symbol and '公交' text in the lane to
                        the right.; arrow:straight (full): Photo 1 shows a yellow arrow pointing straight
                        ahead in the lane to the left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a yellow center line is on my left, and a yellow
                        special lane line is on my right. | roles: The yellow center line and yellow special
                        lane line fit their roles. | markings: The bus marking is in the lane to the right,
                        and the straight arrow is in the lane to the left, which is consistent with the lane
                        layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: Vehicles on the broken side (my side) may cross the yellow line.
                        [[CN-6.1.3]]
Step 5  Rule            right_boundary: Vehicles other than buses are prohibited from entering the bus lane.
                        [[CN-6.9.1]]
Step 5  Rule            text:bus: The lane is reserved for buses only. [[CN-6.9.1]]
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the left lane. Do not move into the lane on
                        your right as it is a reserved bus lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'text:bus'], missed []), actions None, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8458, out 938, 9.96 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road or elevated highway with a green-
                        painted surface. Ahead, there are other vehicles and a clear path forward. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a double solid yellow line to the right of my lane. Photo 2 shows the
                        same double solid yellow line clearly.
                        yellow double_solid, curb no, center_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the double solid yellow lines on both sides, which
                        indicate a center line separating opposing traffic or a restricted area. | roles: The
                        double solid yellow lines correctly function as no-crossing center lines. | markings:
                        No markings are present to contradict the boundaries. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The double solid yellow line prohibits vehicles in both directions
                        from crossing. [[CN-6.1.2]]
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as lane changes to the left or right are prohibited by the
                        double solid yellow lines. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 805, 7.84 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line to the left. Photo 2 shows a yellow broken line
                        next to my car.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right. Photo 2 shows a white solid line next
                        to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the boundaries: a yellow center line on the left and a white lane
                        line on the right. | roles: The yellow broken line correctly identifies a crossable
                        center line, and the white solid line correctly identifies a no-crossing lane line. |
                        markings: The straight arrow is consistent with the lane's purpose. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The crossable center line allows vehicles to cross the line to
                        overtake, turn or make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The no-crossing lane line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change lanes to the
                        left across the yellow broken line, but you are prohibited from changing lanes to the
                        right or making turns, as indicated by the straight arrow and the solid white line on
                        your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 875, 9.13 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road approaching an intersection with an overpass.
                        My car is in a lane that leads toward the center of the intersection. (lanes 4, mine
                        2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is solid white near the car and becomes a broken white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is solid white near the car and becomes a broken white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 2 shows a white arrow pointing left in the lane to my
                        right.; arrow:left (full): Photo 1 shows a white arrow pointing left in the lane to my
                        left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white lane lines
                        correctly identify the boundaries between lanes of the same direction. | markings: The
                        straight arrow in my lane is consistent with the lane's role as a through lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: Vehicles on the solid side may not cross; vehicles on the broken side
                        may cross. [CN-6.2.3] "On a broken-solid white line, vehicles on the solid side may
                        not cross; vehicles on the broken side may cross, and a vehicle crossing the line must
                        give way to "
Step 5  Rule            right_boundary: Vehicles on the solid side may not cross; vehicles on the broken side
                        may cross. [CN-6.2.3] "On a broken-solid white line, vehicles on the solid side may
                        not cross; vehicles on the broken side may cross, and a vehicle crossing the line must
                        give way to "
Step 5  Rule            arrow:straight_right: The arrow indicates the direction of travel is straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You should proceed straight ahead. Lane changes to the left
                        or right are prohibited as the lines are solid near your car.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight_right'], missed ['arrow:straight']), actions False,
                        unsafe [], citation accepted, contradictions ['turn_left prohibited although an arrow
                        shows it', 'turn_right prohibited although an arrow shows it']
Tokens                  in 8458, out 963, 9.45 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a central lane
                        approaching a set of traffic lights and turn lanes. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this white line as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        my lane.; area:left_turn_waiting (full): Photo 1 shows a white left-turn waiting area
                        with two parallel broken lines and a left-turn arrow to the left of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The straight arrow in my lane is consistent with the lane's role. The left-turn
                        waiting area is correctly identified to the left. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The solid white line prohibits crossing into the lane to the right.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1]]
Step 5  Rule            area:left_turn_waiting: The area allows left-turning vehicles to wait in advance.
                        [[CN-5.5.1-3]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       allowed: allowed
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          allowed: allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from your current lane. Lane
                        changes to the left or right are prohibited by the solid white lines. A left-turn
                        waiting area is available in the lane to your left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:left_turn_waiting', 'arrow:straight_u_turn'], missed ['line:stop_line']),
                        actions True, unsafe [], citation in_pack_not_accepted, contradictions ['turn_left
                        allowed although no arrow shows it']
Tokens                  in 8458, out 1000, 8.65 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a bus and other vehicles. There is a
                        fence on the left and a bus lane or sidewalk area on the right. The road ahead appears
                        to be a straight stretch with multiple lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow line on the right. Photo 2 shows this yellow line as a solid
                        line next to my car. Further ahead in Photo 1, the yellow line remains solid.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): Photo 2 shows a white lane line to my left and a white
                        lane line to my right, but no arrows or words are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane line on my left and the yellow edge line on my
                        right. | roles: The white lane line on the left and yellow edge line on the right fit
                        the roles of lane_line and edge_line respectively. | markings: No markings are present
                        in my lane to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane on the left.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The yellow edge line marks the left-hand edge of the direction of
                        travel (in this context, the right side of the roadway) and prohibits crossing.
                        [[CN-5.4.3]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane and proceed straight. Lane changes to the left or
                        right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 872, 9.09 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city road approaching an intersection with a crosswalk.
                        My car is in a lane heading straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this white line as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white stop line across my lane at the
                        intersection.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white solid lines
                        correctly function as lane lines separating traffic in the same direction. | markings:
                        The stop line is consistent with the approach to an intersection. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing from my side into the left
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The solid white line prohibits crossing from my side into the right
                        lane. [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            line:stop_line: The stop line marks where vehicles must stop when yielding or waiting
                        to proceed. [[CN-6.4.1-2] [informative] GB 5768.3-2025, section 6.4.1, 6.4.2, page 48]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     stop_first (contested, label allowed): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You must come to a complete stop at the white stop line
                        before proceeding straight through the intersection. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 8458, out 967, 8.71 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with an intersection ahead. My car is in a
                        lane moving forward towards the intersection. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows this same white dashed line clearly in the foreground.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows this same white dashed line clearly in the foreground.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (insufficient): Photo 1 shows a white left-turn arrow in the lane to my
                        left. No markings are visible in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: No markings are in my lane; the left-turn arrow is in the adjacent lane. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken line means it may be crossed. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: The broken line means it may be crossed. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-4.2.2-a]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that allows for lane changes to the left or right as the boundaries
                        are broken white lines. You may proceed straight ahead into the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['no_turn:left'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 839, 9.24 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in one of the lanes
                        approaching the intersection. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows the same white broken line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb on the right. Photo 2 shows the
                        solid white line and the curb clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; text:other (full): Photo 2 shows the Chinese character '直' (straight) in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        are consistent with the boundaries: a white broken line on the left and a white solid
                        line/curb on the right. | roles: The white broken line on the left is a lane line, and
                        the white solid line on the right is an edge line. | markings: The straight arrow and
                        '直' character are consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight_right: The arrow indicates that the lane is for traveling straight
                        ahead or turning right. [[CN-5.13.1]]
Step 5  Rule            text:other: The character '直' confirms the lane is for straight movement.
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [CN-5.13.1] and '直' text
Step 6  turn_left       prohibited: prohibited by the straight arrow [CN-5.13.1]
Step 6  turn_right      allowed: allowed by the straight arrow [CN-5.13.1]
Step 6  u_turn          prohibited: prohibited by the straight arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead or turn right from this lane. Lane changes to the left
                        are permitted, but moving to the right is prohibited by the curb and edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 1043, 10.17 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test B | gemma4:12b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city road approaching an intersection. My car is in a
                        lane with a straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a broken white line (dashed) near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white lane lines on both sides. | roles: The white dashed
                        lines correctly function as lane lines between lanes of the same direction. |
                        markings: The straight arrow is consistent with the lane's role and the dashed
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows my car to change lanes to the left.
                        [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white line allows my car to change lanes to the right.
                        [[CN-5.2.3]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.3]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.3]
Step 6  go_straight     allowed (correct): allowed by the straight arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are permitted as the boundaries are broken white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 8458, out 922, 8.34 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane urban road with a dedicated lane for straight-ahead
                        traffic. There is a vehicle directly ahead in my lane and a bicycle lane to the right.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the left. Photo 2 shows a
                        solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a bicycle lane. Photo 2 shows
                        a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a large white arrow pointing straight
                        ahead in the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries (left edge line and right lane line). | roles: The
                        white solid lines correctly serve as the left edge and right lane line. | markings:
                        The straight arrow is consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The white edge line on the left marks the boundary of the motor vehicle
                        lane. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing from the side of the
                        solid line. [[CN-6.2.1]]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for straight ahead or
                        U-turn movements. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          allowed (WRONG, label prohibited): allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel or U-turns. You should stay in
                        your lane and are prohibited from changing lanes to the left or right. You may proceed
                        straight or perform a U-turn at the end of the lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight']), actions False, unsafe
                        ['u_turn'], citation accepted, contradictions []
Tokens                  in 8458, out 872, 8.02 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings and trees on both sides. The road ahead is a two-way
                        street with a central divider and lanes for motor vehicles and potentially non-
                        motorized vehicles. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to the left. Photo
                        2 shows the same solid yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a lane line or edge line.
                        Photo 2 shows a white dashed line (broken line) on the right, and further right, a
                        solid white line or curb area.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (insufficient): Photo 2 shows a white dashed line on the right side of
                        my lane.
Step 4  Cross-check     close_up: The close-up (Photo 2) clarifies that the right boundary is a dashed white
                        line, while the left boundary is a solid yellow line. These are consistent with the
                        overall view in Photo 1. | position: The lane count (2) and my position (2, the right
                        lane) agree with the boundaries: a yellow center line is on my left, and a white lane
                        line is on my right. | roles: The solid yellow line correctly identifies as a center
                        line (separating opposing traffic), and the white dashed line correctly identifies as
                        a lane line. | markings: No specific arrows or words are visible in my lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The broken white line means it may be crossed. [[CN-4.2.2-a]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-way street. You may proceed straight or change
                        to the right if needed, but you are prohibited from crossing the solid yellow line to
                        the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 8458, out 890, 7.4 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane moving forward
                        towards a set of traffic lights. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the lane to my left. Photo 2
                        shows the same solid yellow line clearly.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a sidewalk/curb on the right. Photo 2 shows a
                        solid white line next to the lane and a raised curb/sidewalk beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a white arrow pointing straight ahead in
                        the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a yellow center line on the left and a white edge
                        line on the right. | roles: The yellow solid line correctly identifies a center line
                        separating opposing traffic (or a restricted lane), and the white solid line correctly
                        identifies the right edge. | markings: The straight arrow is consistent with the
                        lane's role and the surrounding boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            arrow:straight_u_turn: The guide arrow indicates that the lane is for traveling
                        straight ahead or making a U-turn. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          allowed: allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from this lane. Lane changes to the
                        left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed ['line:stop_line']), actions True, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 8458, out 884, 7.05 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching an intersection with a pedestrian crossing and a
                        large open area to the right. My car is in a lane heading straight toward the
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a solid line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow line on the right, which appears to be a solid line. Photo 2
                        shows a solid yellow line next to my car, and a raised curb/sidewalk further to the
                        right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_u_turn (full): Photo 2 shows a large white arrow pointing straight
                        ahead in the center of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with a white lane line on the left and a yellow edge line on the right.
                        | roles: The white lane line on the left and yellow edge line on the right correctly
                        identify the boundaries of my lane. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose and the surrounding boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line prohibits crossing into the lane to the left.
                        [[CN-6.2.1] [mandatory] GB 5768.3-2025, section 6.2.1, page 44]
Step 5  Rule            right_boundary: The yellow edge line marks the right-hand boundary of the roadway.
                        [[CN-5.4.3] [mandatory] GB 5768.3-2025, section 5.4.3, page 5]
Step 5  Rule            arrow:straight_u_turn: The arrow indicates that the lane is for traveling straight
                        ahead or making a U-turn. [[CN-5.13.1] [informative] GB 5768.3-2025, section 5.13.1,
                        表1, page 27]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          allowed (WRONG, label prohibited): allowed
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or perform a U-turn from this lane. Lane changes to the
                        left or right are prohibited by the solid markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight_u_turn'], missed ['arrow:straight', 'line:stop_line']), actions
                        False, unsafe ['u_turn'], citation unlisted, contradictions []
Tokens                  in 8458, out 986, 9.12 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bus in the center lane. The road is lined with
                        buildings and trees, and there are parked cars on both sides. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the center lane. Photo 2
                        shows a solid yellow line clearly visible next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (3) agree with the boundaries: a yellow center line on the left and a white edge line
                        on the right. | roles: The yellow solid line correctly identifies as a center line
                        (separating opposing traffic or a center lane), and the white solid line correctly
                        identifies as an edge line. | markings: No markings are present in the lane. | unseen:
                        none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits vehicles in both directions from
                        crossing. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 759, 6.46 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane elevated roadway or bridge. Ahead, the road
                        continues straight toward a distant area with buildings. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line on
                        the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal railing. Photo 2
                        shows a solid white line on the right, followed by a concrete base and a metal
                        railing.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane in Photo 1 or Photo
                        2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a yellow center line is on my left, and a white edge
                        line is on my right. | roles: The yellow center line and white edge line fit their
                        respective roles. | markings: No markings are present to contradict the boundaries. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: The single solid yellow line prohibits crossing into the opposite
                        direction. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The solid white line normally prohibits crossing onto the right side.
                        [[CN-4.2.2-a]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 793, 6.35 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a bicycle lane on the right. The road ahead appears to be
                        a straight stretch with an intersection or signalized area further ahead. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a red-painted bicycle lane on
                        the right. Photo 2 shows this solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white bicycle symbol on a red-painted area to the
                        right of my lane. This is not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white dashed line on the left and a solid white line on
                        the right. | roles: The white dashed line on the left is a crossable lane line; the
                        solid white line on the right is a no-crossing lane line. | markings: The bicycle
                        symbol is in the adjacent lane, not my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to change lanes to the left.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line prohibits me from crossing into the bicycle lane
                        on the right. [[CN-6.2.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change lanes to the left if necessary, but you are prohibited from moving into
                        the bicycle lane on your right. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 868, 7.87 s
```
