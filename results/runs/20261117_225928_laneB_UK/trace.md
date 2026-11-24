# Reasoning of lane run 20261117_225928_laneB_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane and a cycle lane. The road ahead leads to a
                        junction or a continuation of the main road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line very close to the car, which appears to be a lane divider.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line very close to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white bicycle symbol in the lane to the left.;
                        area:grid (full): Photo 1 and Photo 2 show a white rectangular box with a diagonal
                        line through it in the lane to the right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a dashed line on the left and a solid line on the right. |
                        roles: The white dashed line on the left and solid line on the right fit the roles of
                        lane dividers. | markings: The bike symbol is in the leftmost lane, and the grid area
                        is in the rightmost lane, consistent with the lane layout. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used to divide
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used to divide
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            symbol:bike: The lane to the left is a mandatory cycle lane. [UK-TSRGD-Part6,item7]
                        "Boundary of a mandatory cycle lane or division of a route into that part reserved for
                        pedal cycles [ F3 and electric scooters being used in a trial ] and that p"
Step 5  Rule            area:grid: You must not enter the grid area marked with chevrons/lines except in an
                        emergency. [UK-Rule130-3] "If the area is marked with chevrons and bordered by solid
                        white lines you MUST NOT enter it except in an emergency."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Do not attempt to change lanes to
                        the left into the cycle lane or to the right into the restricted grid area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:stop_line']), actions False, unsafe [], citation
                        accepted, contradictions ['change_left prohibited across a broken lane line']
Tokens                  in 14754, out 998, 10.08 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction or pedestrian crossing ahead. My car is in a
                        lane that appears to be part of a main carriageway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line as a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line as a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 2 shows a white triangle pointing forward in the center of
                        my lane.; area:grid (full): Photo 1 shows white lines forming a box-like shape or
                        hatching ahead of my lane, indicating a junction or crossing area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane dividers. | markings: The triangle and grid markings
                        are consistent with a junction/crossing area. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used to divide
                        the carriageway into lanes. [UK-Rule131] "Lane dividers. These are short, broken white
                        lines which are used on wide carriageways to divide them into lanes. You should keep
                        between them."
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used to divide
                        the carriageway into lanes. [UK-Rule131] "Lane dividers. These are short, broken white
                        lines which are used on wide carriageways to divide them into lanes. You should keep
                        between them."
Step 5  Rule            symbol:other: No specific rule for this triangle marking, but it typically indicates a
                        hazard or junction.
Step 5  Rule            area:grid: Keep the area clear of stationary vehicles. [UK-HC_MARKINGS-p3-2] "Keep
                        entrance clear of stationary vehicles, even if picking up or setting down children"
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    allowed (contested, label prohibited): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the
                        boundaries are broken white lines. Proceed straight through the junction, ensuring you
                        do not block the grid area ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid', 'symbol:other'], missed ['line:crosswalk']), actions None, unsafe [],
                        citation in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 964, 8.88 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane with a
                        straight-ahead arrow. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a solid white line next to my car, which then becomes a broken white line
                        further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from a cycle lane on the right. Photo 2
                        shows this line is a solid white line next to my car. Further ahead in Photo 1, the
                        line remains solid.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; symbol:bike (full): Photo 1 shows a bicycle symbol in the lane to my right.
Step 4  Cross-check     close_up: The same in both photos. | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white line on my left separates me from the left lane,
                        and a white line on my right separates me from the cycle lane. | roles: The white
                        lines correctly function as lane dividers. | markings: The straight arrow in my lane
                        is consistent with the lane's purpose. The bike symbol correctly identifies the
                        adjacent lane as a cycle lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the short, broken white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Proceed straight ahead in your current lane. Do not attempt to change lanes or turn,
                        as the markings indicate a straight-ahead-only path and the lane boundaries are solid.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 937, 10.49 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a cycle lane on the left and a car in the adjacent lane
                        to the right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from a cycle lane. Photo 2 shows
                        two parallel yellow lines, one solid and one broken, very close together.
                        yellow solid_dashed (near line solid), curb yes, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white line that is solid near the car and appears to be a standard lane
                        divider.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): Photo 1 shows a white line on the right
                        and a double yellow line on the left.
Step 4  Cross-check     close_up: The close-up confirms the double yellow lines on the left are a solid and a
                        dashed line side by side. The white line on the right is solid. | position: The lane
                        count of 3 is consistent with the boundaries: a special lane line on the left (cycle
                        lane) and a lane line on the right. | roles: The yellow lines correctly identify a
                        special lane boundary (cycle lane), and the white line identifies a standard lane
                        divider. | markings: No specific arrows or words are visible in my lane; the area to
                        the left is a cycle lane, not a two-way left-turn lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: You MUST NOT drive in a cycle lane marked by a solid white line during
                        its times of operation. [UK-Rule140] "You MUST NOT drive or park in a cycle lane
                        marked by a solid white line during its times of operation."
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        on wide carriageways to divide them into lanes. [UK-Rule131] "Lane dividers. These are
                        short, broken white lines which are used on wide carriageways to divide them into
                        lanes. You should keep between them."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Do not attempt to change lanes to
                        the left into the cycle lane or to the right across the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 897, 9.62 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street approaching a junction with a pedestrian crossing. My car is in a lane
                        that leads towards the intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line near my car and becomes a solid white line further
                        ahead as it approaches the junction.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on my right. Photo 2 shows this line is a solid white line
                        near my car and remains solid as it approaches the junction.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white pedestrian crossing (zebra crossing)
                        ahead of my lane.; area:grid (full): Photo 1 shows white lines forming a box-like
                        shape or diagonal markings ahead of my lane, indicating a junction area.
Step 4  Cross-check     close_up: The close-up (Photo 2) clearly shows the left boundary is a dashed line near
                        the car and a solid line further ahead, which matches the interpretation. | position:
                        The lane count of 2 and my position as lane 2 (rightmost) is consistent with a lane
                        line on my left and an edge line/curb on my right. | roles: The white lines and curb
                        correctly define the lane boundaries. | markings: The crosswalk and grid markings are
                        consistent with a junction ahead. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The broken white line marks the centre of the road and may be crossed
                        to overtake or turn off if safe. [UK-Rule127] "A broken white line. This marks the
                        centre of the road. When this line lengthens and the gaps shorten, it means that there
                        is a hazard ahead. Do not cross it un"
Step 5  Rule            right_boundary: The edge of the carriageway is the boundary of the road. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            line:crosswalk: You must not park on a crossing or in the area covered by the zig-zag
                        lines. [UK-Rule191] "You MUST NOT park on a crossing or in the area covered by the
                        zig-zag lines. You MUST NOT overtake the moving vehicle nearest the crossing or the
                        vehicle neares"
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if it is safe to do so, as the boundary is a broken
                        white line. You should proceed straight through the junction, being mindful of the
                        pedestrian crossing ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 14754, out 978, 10.03 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with houses on the left and a sidewalk on the right. The road
                        ahead appears to be a straight continuation of the current street. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a double red line on the left. Photo 2 shows two parallel solid red
                        lines very close to the curb.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right. Photo 2 shows a white dashed line
                        clearly separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 shows yellow markings on the road surface to the right of my
                        lane, but they are in the adjacent lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the left edge line (red lines) and the right lane line (white
                        dashed). | roles: The red lines correctly function as an edge line, and the white
                        dashed line functions as a lane divider. | markings: The grid markings are in the
                        adjacent lane and do not affect my lane's movements. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The red lines indicate a prohibition on stopping or parking. [UK-
                        Rule127] "A broken white line. This marks the centre of the road. When this line
                        lengthens and the gaps shorten, it means that there is a hazard ahead. Do not cross it
                        un"
Step 5  Rule            right_boundary: The broken white line indicates a lane divider where you should keep
                        between the lines. [UK-Rule131] "Lane dividers. These are short, broken white lines
                        which are used on wide carriageways to divide them into lanes. You should keep between
                        them."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead or change into the right
                        lane. Changing into the left lane is prohibited by the red lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:grid'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 14754, out 818, 9.62 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings on the right and a park-like area with trees on
                        the left. The road ahead appears to be a straight stretch with multiple lanes of
                        traffic. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows a solid white line very close to the car, which then becomes a dashed white line
                        further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows a solid white line next to the car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; text:bus (full): Photo 2 shows white text 'BUS' in the lane to my left.
Step 4  Cross-check     close_up: Photo 2 shows the left boundary is solid near the car and dashed further
                        ahead, while Photo 1 shows the overall lane structure. The markings are consistent. |
                        position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white lines correctly function as
                        lane dividers. | markings: The straight arrow in my lane is consistent with the lane's
                        purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You may cross the lines to overtake if it is safe, provided you can
                        complete the manoeuvre before reaching a solid white line on your side. [UK-Rule128]
                        "Double white lines where the line nearer to you is broken. This means you may cross
                        the lines to overtake if it is safe, provided you can complete the manoeuvre"
Step 5  Rule            right_boundary: You should keep between the short, broken white lines. [UK-Rule131]
                        "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change to the left if
                        safe, but you should not change to the right or attempt any turns at the end of this
                        lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'text:bus'], missed []), actions False, unsafe [], citation
                        accepted, contradictions ['change_left allowed with the solid line of a solid-and-
                        broken pair nearer my lane']
Tokens                  in 14754, out 952, 10.27 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a cycle lane on the left and parked cars on the right.
                        The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the cycle lane. Photo 2
                        shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane with parked cars.
                        Photo 2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a white bicycle symbol in the lane to my left. Photo
                        2 shows a white bicycle symbol in the lane to my left.; symbol:bike (full): Photo 1
                        shows a white bicycle symbol in the lane to my left. Photo 2 shows a white bicycle
                        symbol in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane dividers. | markings: The bicycle symbols are in the
                        lane to the left, consistent with the cycle lane boundary. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines that divide the lanes.
                        [UK-Rule131] "Lane dividers. These are short, broken white lines which are used on
                        wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the broken white lines that divide the lanes.
                        [UK-Rule131] "Lane dividers. These are short, broken white lines which are used on
                        wide carriageways to divide them into lanes. You should keep between them."
Step 6  change_left     allowed (correct): allowed by the broken white line on the left (UK-Rule131)
Step 6  change_right    allowed (correct): allowed by the broken white line on the right (UK-Rule131)
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as it is safe to do so, as the boundaries are broken white lines. Proceed
                        straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 738, 6.14 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian crossing and a small traffic island ahead.
                        My car is in a lane approaching a junction or crossing. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows white lines forming a box-like shape or area around
                        the pedestrian crossing.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as 2
                        (middle lane) is consistent with the white lane lines on both sides. | roles: The
                        white solid lines correctly function as lane dividers. | markings: The grid-like
                        markings around the crossing are consistent with the road layout. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but since this is
                        solid, it indicates a firmer division. [UK-Rule131] "Lane dividers. These are short,
                        broken white lines which are used on wide carriageways to divide them into lanes. You
                        should keep between them."
Step 5  Rule            right_boundary: You should keep between the white lines. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            area:grid: Keep the area clear of stationary vehicles. [UK-HC_MARKINGS-p3-2] "Keep
                        entrance clear of stationary vehicles, even if picking up or setting down children"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Do not attempt to change lanes as the
                        solid white lines prohibit it. Ensure you do not stop within the marked grid area
                        around the pedestrian crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 696, 7.29 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction or pedestrian crossing ahead. My car is in a
                        lane with a white van directly ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows the same white dashed line clearly.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows this solid white line
                        clearly.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white circular marking with a bicycle symbol
                        inside it in the lane to my right.; area:two_way_left_turn_lane (full): Photo 1 and
                        Photo 2 show a white dashed line and a bicycle symbol on the far left, indicating a
                        cycle lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the left dashed line and right solid line. | roles: The white
                        dashed line on the left is a lane divider, and the solid white line on the right is an
                        edge line. | markings: The bike symbol is in the adjacent lane, not my lane. The cycle
                        lane is to the left. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You may cross the broken white line to overtake or turn off if it is
                        safe. [UK-Rule127] "A broken white line. This marks the centre of the road. When this
                        line lengthens and the gaps shorten, it means that there is a hazard ahead. Do not
                        cross it un"
Step 5  Rule            right_boundary: The solid white line marks the edge of the carriageway available for
                        through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white line [UK-Rule127].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited as it would involve crossing the edge
                        line [UK-TSRGD-S11P4-item11].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow is present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow is present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn arrow is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked in my lane.
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the left lane if safe. Do not move to the right
                        as it is the edge of the carriageway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane', 'symbol:bike'], missed ['text:speed_limit']), actions
                        False, unsafe [], citation accepted, contradictions []
Tokens                  in 14754, out 951, 8.27 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops and pedestrians on the left. Ahead, there is a
                        junction with clear lane markings and a white van in the distance. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line as a solid white line near the car, which then becomes a dashed white line
                        further ahead before the junction.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line as a dashed white line near the car and continuing as a dashed white
                        line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 2 shows a white arrow pointing left in the lane to my
                        left.
Step 4  Cross-check     close_up: The close-up (Photo 2) clarifies that the left boundary is a solid white
                        line near the car and a dashed white line further ahead. The right boundary is
                        consistently dashed in both photos. | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on the left and a white line on the
                        right. | roles: The white lines correctly function as lane dividers. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose. The left arrow in the
                        adjacent lane is consistent with its purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You may cross the lines to overtake if it is safe, provided you can
                        complete the manoeuvre before reaching a solid white line on your side. [UK-Rule128]
                        "Double white lines where the line nearer to you is broken. This means you may cross
                        the lines to overtake if it is safe, provided you can complete the manoeuvre"
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        to divide lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines
                        which are used on wide carriageways to divide them into lanes. You should keep between
                        them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     allowed (contested, correct): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change lanes to the
                        left or right if safe, but you must not turn left from this lane as indicated by the
                        road markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['arrow:straight_left']), actions False,
                        unsafe [], citation accepted, contradictions ['change_left allowed with the solid line
                        of a solid-and-broken pair nearer my lane', 'turn_left prohibited although an arrow
                        shows it']
Tokens                  in 14754, out 985, 17.86 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a cycle lane on the left and a bus lane or similar
                        designated lane on the right. There is a junction or continuation of the road ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 shows a white circular marking with a bicycle symbol on
                        the right side of the road, ahead of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) agree with the white dashed lines on both sides. | roles: The white
                        dashed lines correctly function as lane dividers. | markings: The bike symbol on the
                        right indicates a cycle lane, which is consistent with the lane layout. | unseen: none
                        | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used to divide
                        the wide carriageway into lanes. [UK-Rule131] "Lane dividers. These are short, broken
                        white lines which are used on wide carriageways to divide them into lanes. You should
                        keep between them."
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used to divide
                        the wide carriageway into lanes. [UK-Rule131] "Lane dividers. These are short, broken
                        white lines which are used on wide carriageways to divide them into lanes. You should
                        keep between them."
Step 5  Rule            symbol:bike: You must not drive or park in a cycle lane marked by a solid white line,
                        but the dashed line here suggests a different status or a transition. [UK-Rule140]
                        "You MUST NOT drive or park in a cycle lane marked by a solid white line during its
                        times of operation."
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the boundaries are dashed white lines. The lane to your right is a cycle
                        lane, indicated by the bicycle symbol.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 904, 9.77 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian area to the left and a sidewalk to the
                        right. Ahead, there is a junction with multiple lanes and turn arrows. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a double red line on the left. Photo 2 shows two solid red lines side by
                        side.
                        other solid_dashed (near line solid), curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to the right. Photo 2 shows a white dashed line to
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a white arrow pointing straight ahead with a
                        small left-turn branch in my lane.; arrow:left (full): Photo 1 shows a white arrow
                        pointing left in the lane to my right.; arrow:straight (full): Photo 1 shows a white
                        arrow pointing straight ahead in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position
                        (middle, index 2) agree with the boundaries: a red edge line on the left and a white
                        lane line on the right. | roles: The red lines correctly indicate the edge of the
                        carriageway, and the white dashed line correctly divides my lane from the right lane.
                        | markings: The straight-left arrow in my lane is consistent with the lane's position
                        and the surrounding arrows. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The red lines indicate that stopping to park, load/unload or to
                        board/alight is prohibited. [UK-TSRGD-P2-8]
Step 5  Rule            right_boundary: The broken white line indicates a lane divider; you should keep
                        between them. [UK-Rule131] "Lane dividers. These are short, broken white lines which
                        are used on wide carriageways to divide them into lanes. You should keep between
                        them."
Step 5  Rule            arrow:straight_left: The arrow indicates the possible traffic movements at the end of
                        the lane. [UK-TSRGD-Part6,item12] "Direction of possible traffic movements at the end
                        of a nearside with-flow bus lane or other designated lane, or where there is an
                        intermediate discontinuation "
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       allowed (correct): allowed
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight ahead or turn left from your current lane. You may change
                        into the right lane if safe, but you must not change into the left lane or turn right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions True, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 14754, out 982, 11.49 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a junction or a point where the road layout
                        changes. My car is in a lane that appears to be part of a multi-lane system. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line as a broken white line (dashed) next to my car, which then becomes a solid
                        white line further ahead as it approaches the junction area.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on my right. Photo 2 shows this line as a broken white line
                        (dashed) next to my car, which also appears to become solid further ahead near the
                        junction.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (full): Photo 1 shows white zigzag lines across the road ahead of my
                        lane, indicating a pedestrian crossing area.; symbol:other (full): Photo 1 shows white
                        zigzag lines on the road surface ahead.
Step 4  Cross-check     close_up: The close-up (Photo 2) confirms the dashed nature of the lines immediately
                        adjacent to the car, while Photo 1 shows the transition to solid lines further ahead.
                        Both photos agree on the white color. | position: The lane count of 3 and my position
                        as lane 2 (middle) are consistent with the white lane lines on both sides. | roles:
                        The white dashed/solid lines correctly function as lane dividers. | markings: The
                        zigzag lines are consistent with a pedestrian crossing area ahead. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The broken white line allows me to cross it to overtake or turn if it
                        is safe. [UK-Rule127] "A broken white line. This marks the centre of the road. When
                        this line lengthens and the gaps shorten, it means that there is a hazard ahead. Do
                        not cross it un"
Step 5  Rule            right_boundary: The broken white line allows me to cross it to overtake or turn if it
                        is safe. [UK-Rule127] "A broken white line. This marks the centre of the road. When
                        this line lengthens and the gaps shorten, it means that there is a hazard ahead. Do
                        not cross it un"
Step 5  Rule            line:stop_yield: The zigzag markings prohibit parking or overtaking near the crossing.
                        [UK-Rule191] "You MUST NOT park on a crossing or in the area covered by the zig-zag
                        lines. You MUST NOT overtake the moving vehicle nearest the crossing or the vehicle
                        neares"
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white line (UK-Rule127)
Step 6  change_right    allowed (contested, label prohibited): allowed by the dashed white line (UK-Rule127)
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the immediate
                        markings are dashed, but be cautious as the lines become solid ahead. Do not stop or
                        overtake in the zigzag area ahead of the pedestrian crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield', 'symbol:other'], missed ['line:crosswalk']), actions None, unsafe
                        [], citation accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 14754, out 1025, 10.01 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a red line on the left. Photo 2 shows a raised curb
                        with a red line painted on the edge of the pavement next to the curb.
                        other none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white line next to my car and a white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow in my lane pointing straight ahead
                        and slightly to the left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (1)
                        agree with the left edge line and right lane line. | roles: The red line/curb on the
                        left correctly identifies an edge line; the white line on the right correctly
                        identifies a lane divider. | markings: The straight arrow in my lane is consistent
                        with the lane's role and boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The red line indicates that stopping to park, load/unload or to
                        board/alight is prohibited. [UK-HC_MARKINGS-p2-8] "The double and single red lines
                        used on Red Routes indicate that stopping to park, load/unload or to board and alight
                        from a vehicle (except for a licensed taxi"
Step 5  Rule            right_boundary: The white line is a lane divider, and you should keep between them.
                        [UK-Rule131] "Lane dividers. These are short, broken white lines which are used on
                        wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane. Lane changes and turns are
                        prohibited by the road markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 14754, out 867, 9.0 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A city street approaching a pedestrian crossing and a junction. My car is in a lane
                        that leads directly toward a crosswalk. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows a solid white line on the
                        left that turns into a zigzag pattern near the crossing.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line on the
                        right that turns into a zigzag pattern near the crossing.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a pedestrian crossing (zebra stripes) ahead.
                        Photo 2 shows the zebra stripes clearly.; symbol:other (full): Photo 1 shows zigzag
                        lines on both sides of the crossing. Photo 2 shows these clearly.
Step 4  Cross-check     close_up: The close-up (Photo 2) clarifies that the solid white lines on both sides
                        become zigzag markings as they approach the pedestrian crossing. Photo 2 decides the
                        pattern near the car; Photo 1 shows the overall context. | position: The lane count
                        and position are consistent with the edge lines on both sides. | roles: The white
                        lines correctly function as edge lines for the lane. | markings: The crosswalk and
                        zigzag markings are consistent with a pedestrian crossing area. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The white line marks the edge of the carriageway available for through
                        traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available
                        for through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            right_boundary: The white line marks the edge of the carriageway available for through
                        traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available
                        for through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            line:crosswalk: You must not park on a crossing or in the area covered by the zig-zag
                        lines. [UK-Rule191] "You MUST NOT park on a crossing or in the area covered by the
                        zig-zag lines. You MUST NOT overtake the moving vehicle nearest the crossing or the
                        vehicle neares"
Step 5  Rule            symbol:other: You must not park your vehicle anywhere within these markings. [UK-KYTS-
                        zigzag] "The zig-zag markings at crossings are there to ensure that drivers and
                        pedestrians can see each other clearly. As a driver, you must not park your vehicle
                        anywh"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Proceed straight through the crossing. Do not change lanes or park within the zigzag
                        markings or on the pedestrian crossing.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 997, 11.28 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with several buses. My car is in a lane next to a bus lane.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from a bus lane on the left. Photo
                        2 shows this same solid white line clearly.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line on the right. Photo 2 shows this dashed white line
                        clearly.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows 'BUS LANE' text and a bus symbol in the lane to the
                        left of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a solid white line on the left separates me from the bus
                        lane, and a dashed line on the right separates me from the rightmost lane. | roles:
                        The solid white line on the left correctly acts as a lane divider, and the dashed line
                        on the right acts as a lane divider. | markings: The 'BUS LANE' marking is in the lane
                        to the left, which is consistent with the solid white line boundary. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: You may cross the broken white line to overtake if it is safe. [UK-
                        Rule127] "A broken white line. This marks the centre of the road. When this line
                        lengthens and the gaps shorten, it means that there is a hazard ahead. Do not cross it
                        un"
Step 5  Rule            text:bus: Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation. [UK-Rule141] "Bus lanes. These are shown by road markings and
                        signs that indicate which (if any) other vehicles are permitted to use the bus lane."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane and do not move into the bus lane on your left. You may
                        change into the right lane if it is safe to do so.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:bus'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 14754, out 876, 8.77 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street in the UK. Ahead, there is a junction or a change in road
                        layout with a cyclist and a car in the adjacent lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left (where
                        the bus is). Photo 2 shows this same solid white line clearly. Further ahead, the line
                        remains solid white.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right, which appears to be a lane divider or edge
                        line. Photo 2 shows a white line that is dashed/broken. Further ahead in Photo 1, this
                        line appears to be a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): Photo 2 shows a white circular arrow
                        marking in the lane to the right, but my lane has no specific arrows or words.
Step 4  Cross-check     close_up: The close-up confirms the solid white line on the left and the dashed white
                        line on the right. The circular arrows are in the lane to the right, not my lane. |
                        position: The lane count of 3 and my position as 2 (middle) is consistent with a solid
                        line on the left and a dashed line on the right. | roles: The solid white line on the
                        left acts as a lane divider, and the dashed line on the right acts as a lane divider.
                        | markings: No markings are directly in my lane. The circular arrows are in the right-
                        hand lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: You may cross the broken white line to overtake if it is safe. [UK-
                        Rule127] "A broken white line. This marks the centre of the road. When this line
                        lengthens and the gaps shorten, it means that there is a hazard ahead. Do not cross it
                        un"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane and avoid moving to the left due to the solid
                        white line. You may move to the right if it is safe to do so, as the boundary is a
                        broken white line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane'], missed ['text:speed_limit']), actions True, unsafe
                        [], citation accepted, contradictions []
Tokens                  in 14754, out 908, 9.44 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road with an intersection ahead. My car is in a lane that appears to
                        be a dedicated turn lane or a lane leading to a junction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows this line is solid and white near the car, and it remains solid as it curves
                        slightly to the left ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right. Photo 2 shows this line is solid and
                        white near the car, and it remains solid as it continues ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 2 shows a white arrow pointing left in the lane to my
                        left.; arrow:right (full): Photo 2 shows a white arrow pointing right in the lane to
                        my right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the boundaries: a white line on the left and a white line on the right
                        define my lane. | roles: The white solid lines correctly function as lane dividers. |
                        markings: The straight arrow in my lane is consistent with the solid white boundaries
                        defining a dedicated straight-ahead lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines and the straight-ahead arrow.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right'], missed []), actions False, unsafe [], citation
                        accepted, contradictions ['turn_left prohibited although an arrow shows it',
                        'turn_right prohibited although an arrow shows it']
Tokens                  in 14754, out 951, 10.62 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test B | gemma4:12b
----------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching a junction or a point where lanes are organized.
                        My car is in a central lane. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to my left. Photo 2
                        shows the same white broken line clearly next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to my right. Photo
                        2 shows the same white broken line clearly next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; arrow:left (full): Photo 2 shows a white arrow pointing left in the lane to my
                        left.; arrow:right (full): Photo 2 shows a white arrow pointing right in the lane to
                        my right.; line:stop_line (full): Photo 2 shows a white stop line across the lanes
                        ahead.; text:other (full): Photo 2 shows the word 'ONLY' painted in the lane to the
                        left of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (4) and my position (2)
                        are consistent with the white dashed lines on both sides. | roles: The white dashed
                        lines correctly function as lane dividers. | markings: The straight arrow in my lane
                        is consistent with the lane's purpose, and the surrounding arrows/text define the
                        adjacent lanes. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the short, broken white lines that divide the
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 5  Rule            line:stop_line: This is a stop line at a signal or police control. [UK-HC_MARKINGS-p1]
                        "Stop line at signals or police control"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     stop_first (WRONG, label allowed): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You must come to a full stop at
                        the white stop line before proceeding. Do not change lanes or turn left/right from
                        this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'arrow:right', 'text:other'], missed []), actions False, unsafe [],
                        citation accepted, contradictions ['change_left prohibited across a broken lane line',
                        'change_right prohibited across a broken lane line', 'turn_left prohibited although an
                        arrow shows it', 'turn_right prohibited although an arrow shows it']
Tokens                  in 14754, out 1096, 9.92 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white line on my left and a white line on my right. |
                        roles: The white solid lines correctly function as lane dividers. | markings: The
                        straight arrow in my lane is consistent with the lane's purpose and the solid
                        boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines, but since these are
                        solid, they indicate a firmer division. [UK-Rule131] "Lane dividers. These are short,
                        broken white lines which are used on wide carriageways to divide them into lanes. You
                        should keep between them."
Step 5  Rule            right_boundary: You should keep between the broken white lines, but since these are
                        solid, they indicate a firmer division. [UK-Rule131] "Lane dividers. These are short,
                        broken white lines which are used on wide carriageways to divide them into lanes. You
                        should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight ahead as indicated by the road
                        markings. Lane changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 702, 6.87 s

lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops and trees on both sides. A bus and a van are
                        visible ahead in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        a white line with short dashes and gaps next to my car, and a solid white line further
                        ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white line with short dashes and gaps next to my car, and a solid white line
                        further ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 2 shows a white dashed line in the center of my
                        lane.
Step 4  Cross-check     close_up: The same in both photos. | position: The lane count and my lane position
                        agree with the boundary roles. I am in the middle lane of three. | roles: The white
                        solid_dashed lines correctly identify the boundaries of my lane. | markings: The
                        dashed line in the center of my lane is not a stop_yield line but a lane divider or
                        similar marking; however, no specific arrow or word governs the movement. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines. [UK-Rule131]
                        "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the short, broken white lines. [UK-Rule131]
                        "Lane dividers. These are short, broken white lines which are used on wide
                        carriageways to divide them into lanes. You should keep between them."
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as the dashed
                        lines permit. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 14754, out 661, 7.4 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and trees on both sides. The road ahead appears
                        to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        a white dashed line next to my car and a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        a white dashed line next to my car and a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 2 (middle) are consistent with the white dashed lines on both sides. | roles: The
                        white dashed lines correctly function as lane dividers. | markings: No markings are
                        present to contradict the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used to divide
                        the wide carriageway into lanes. [UK-Rule131] "Lane dividers. These are short, broken
                        white lines which are used on wide carriageways to divide them into lanes. You should
                        keep between them."
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used to divide
                        the wide carriageway into lanes. [UK-Rule131] "Lane dividers. These are short, broken
                        white lines which are used on wide carriageways to divide them into lanes. You should
                        keep between them."
Step 6  change_left     allowed (contested, label prohibited): allowed by the dashed white lane line on the
                        left (UK-Rule131)
Step 6  change_right    allowed (correct): allowed by the dashed white lane line on the right (UK-Rule131)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as the lane markings are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 848, 8.64 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings on both sides. There is a car directly ahead
                        in my lane and a parked car to the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line on the far left. Photo 2 shows a solid yellow line next to
                        the car ahead, which appears to be a double yellow line on the edge of the road.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white line with a dashed pattern next to the car ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: The left boundary is a double yellow line (edge of road) and the right
                        boundary is a white dashed line. Photo 2 confirms the dashed nature of the right line.
                        | position: The lane count is 2. My lane is the left one (index 1), bounded by a
                        yellow edge line on the left and a white dashed line on the right. | roles: The yellow
                        line correctly identifies the edge of the carriageway, and the white dashed line
                        correctly identifies a lane divider. | markings: No markings are present in the lane.
                        | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The yellow line indicates waiting restrictions apply to the
                        carriageway. [UK-HC_MARKINGS-p2] "Waiting restrictions indicated by yellow lines apply
                        to the carriageway, pavement and verge. You may stop to load or unload (unless there
                        are also loading restr"
Step 5  Rule            right_boundary: The broken white line marks the centre of the road or a lane divider;
                        it may be crossed to overtake or change lanes if safe. [UK-Rule127] "A broken white
                        line. This marks the centre of the road. When this line lengthens and the gaps
                        shorten, it means that there is a hazard ahead. Do not cross it un"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed: allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the left-hand lane. You may proceed straight ahead or change into the right
                        lane if safe. Changing to the left is prohibited by the edge of the road.
Score                   lane False, boundaries {'left': True, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 871, 8.77 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus lane on the left and a dedicated lane for a
                        vehicle on the right. The car is in a central lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the bus lane. Photo 2 shows a solid
                        white line next to the car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line next to the car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows 'BUS' and 'LANE' painted in the lane to the left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the white lines on both sides. | roles: The white lines correctly
                        function as lane dividers. | markings: The 'BUS LANE' text is in the lane to the left,
                        consistent with the left boundary. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the white lane dividers. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the white lane dividers. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            text:bus: Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation. [UK-Rule141] "Bus lanes. These are shown by road markings and
                        signs that indicate which (if any) other vehicles are permitted to use the bus lane."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Do not attempt to change lanes to
                        the left into the bus lane or to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 14754, out 844, 7.98 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings on both sides. A bus is approaching in the opposite
                        direction. There is a box junction ahead of my car. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows a solid white line on the
                        left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows a yellow criss-cross box junction marking ahead of my
                        car.; text:other (partial): Photo 1 shows white text on the right side of the lane
                        further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my lane position
                        (1) agree with the boundaries: a solid white line on the left indicates an edge line,
                        and a solid white line on the right indicates a lane divider. | roles: The white solid
                        lines correctly serve as an edge line on the left and a lane divider on the right. |
                        markings: The grid marking is a box junction, and the text on the right is consistent
                        with a designated lane (likely a bus lane). | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line marks the edge of the carriageway. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            right_boundary: The solid white line divides the carriageway into traffic lanes. [UK-
                        TSRGD-S11P4-item4] "Diagram 1005 Division of carriageway into traffic lanes on part of
                        the carriageway where vehicles normally proceed in the same direction other than at
                        places wh"
Step 5  Rule            area:grid: A vehicle must not enter the box junction so that the vehicle has to stop
                        within the box junction due to the presence of stationary vehicles. [UK-TSRGD-11(1)]
                        "Subject to sub-paragraphs (2), (3) and (4), the yellow criss-cross marking conveys
                        the prohibition that a person must not cause a vehicle to enter the box junct"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Do not enter the box junction unless
                        your exit is clear of stationary vehicles.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 14754, out 938, 16.92 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated cycle lane on the left and parked cars on the
                        right. A red bus is visible ahead in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the cycle lane. Photo 2 shows
                        a solid white line next to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a white line next to my car and a white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a bicycle symbol and a white line in the lane to the
                        left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a solid white line on the left separates me from
                        the cycle lane (edge_line), and a solid white line on the right separates me from the
                        rightmost lane. | roles: The white solid lines correctly function as an edge line for
                        the cycle lane and a lane divider for the right side. | markings: The bike symbol is
                        in the lane to the left, consistent with the cycle lane boundary. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line marks the edge of the carriageway available for
                        through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 5  Rule            right_boundary: The white line divides the road into lanes and you should keep between
                        them. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            symbol:bike: The bike symbol and lane indicate a cycle lane where motor vehicles are
                        generally prohibited. [UK-Rule140] "You MUST NOT drive or park in a cycle lane marked
                        by a solid white line during its times of operation."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Do not attempt to change lanes to
                        the left into the cycle lane or to the right across the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 14754, out 915, 10.23 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction or pedestrian crossing ahead. My car is in a
                        central lane approaching a set of markings that indicate a junction or a change in
                        road layout. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the one to the left. Photo 2 shows
                        this line as a solid white line near the car, which then becomes a broken white line
                        further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the one to the right. Photo 2 shows
                        this line as a solid white line near the car, which then becomes a broken white line
                        further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 2 shows white diagonal lines forming a box-like area ahead of
                        my lane.
Step 4  Cross-check     close_up: The same in both photos. | position: The lane count and my lane position
                        agree with the boundary roles. I am in the middle lane of three. | roles: The white
                        lines correctly function as lane dividers. | markings: The grid markings indicate a
                        restricted area ahead, consistent with a junction or crossing. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the broken white lines. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            area:grid: Keep the entrance clear of stationary vehicles. [UK-HC_MARKINGS-p3-2] "Keep
                        entrance clear of stationary vehicles, even if picking up or setting down children"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane as the solid lines near the car prohibit lane changes.
                        Proceed straight ahead, ensuring you do not block the grid area marked on the road.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 14754, out 862, 8.38 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops and pedestrians on both sides. The road ahead
                        appears to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is a broken white line near the car and remains broken further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows this line is solid and
                        continuous near the car and further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): Photo 1 shows a white dashed line separating the
                        middle lane from the right lane. Photo 2 shows this line clearly.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my lane position
                        (2) agree with the boundaries: a white dashed line is on my left (lane line) and a
                        solid white line with a curb is on my right (edge line). | roles: The white dashed
                        line on the left fits the role of a lane divider, and the solid white line on the
                        right fits the role of an edge line. | markings: The dashed line to the right of my
                        lane is a standard lane divider. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You may cross the broken white line to overtake if it is safe. [UK-
                        Rule127] "A broken white line. This marks the centre of the road. When this line
                        lengthens and the gaps shorten, it means that there is a hazard ahead. Do not cross it
                        un"
Step 5  Rule            right_boundary: The solid white line marks the edge of the carriageway available for
                        through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 6  change_left     allowed (contested, label prohibited): allowed by UK-Rule127
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid edge line and curb
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change into the left lane if it is safe to do so.
                        Do not move into the area to the right of the solid white line as it is the edge of
                        the carriageway.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 14754, out 893, 9.9 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a sidewalk on the left and a cycle lane on the right.
                        Ahead, there is a junction or a point where the road layout changes. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line next to my car and a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my
                        lane.; symbol:bike (full): Photo 2 shows a white bicycle symbol in the lane to the
                        right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a solid white line on the left (edge line) and a
                        solid white line on the right (lane line). | roles: The white solid lines correctly
                        define the boundaries of the lane. | markings: The straight arrow in my lane is
                        consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line marks the edge of the carriageway available for
                        through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 5  Rule            right_boundary: The white line divides the road into lanes and I should keep between
                        them. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should stay in your current lane and proceed straight ahead as indicated by the
                        road marking. Lane changes to the left or right are prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 14754, out 750, 7.77 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrian crossing and a junction ahead. My car is in
                        the middle lane of a three-lane roadway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to my left. Photo 2
                        shows a white dashed line very close to the car, which remains dashed further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to my right. Photo
                        2 shows this line is also white and dashed.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white pedestrian crossing (zebra) ahead of my
                        lane. Photo 2 shows the crossing clearly.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane dividers. | markings: The crosswalk is consistent with the
                        urban road setting. | unseen: none | result: consistent
Step 5  Rule            left_boundary: A broken white line marks the centre of the road or a lane divider; it
                        may be crossed if it is safe to do so. [[UK-Rule127]]
Step 5  Rule            right_boundary: A broken white line marks the centre of the road or a lane divider; it
                        may be crossed if it is safe to do so. [[UK-Rule127]]
Step 5  Rule            line:crosswalk: no marking governs this action [no marking governs this action]
Step 6  change_left     allowed (correct): allowed by the white dashed left_boundary [UK-Rule127]
Step 6  change_right    allowed (correct): allowed by the white dashed right_boundary [UK-Rule127]
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right if it is safe to
                        do so. Proceed with caution as there is a pedestrian crossing ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 14754, out 908, 10.47 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a junction or pedestrian crossing ahead. My car is in a
                        lane heading straight forward. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line as a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line as a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 shows a white stop line across my lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        agree with the white dashed lines on both sides. | roles: The white dashed lines
                        correctly function as lane dividers. | markings: The stop line is consistent with the
                        lane's end at a junction. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used to divide
                        the wide carriageway into lanes. [UK-Rule131] "Lane dividers. These are short, broken
                        white lines which are used on wide carriageways to divide them into lanes. You should
                        keep between them."
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used to divide
                        the wide carriageway into lanes. [UK-Rule131] "Lane dividers. These are short, broken
                        white lines which are used on wide carriageways to divide them into lanes. You should
                        keep between them."
Step 5  Rule            line:stop_line: Vehicular traffic must not proceed beyond the line when required to
                        stop. [UK-TSRGD-Part6,item1] "Vehicular traffic must not proceed beyond the line when
                        required to stop by the stop sign"
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     stop_first (contested, label allowed): stop_first
Step 6  turn_left       stop_first: stop_first
Step 6  turn_right      stop_first: stop_first
Step 6  u_turn          stop_first: stop_first
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change lanes to the left or
                        right as it is safe to do so. You must come to a complete stop at the white line
                        before proceeding through the junction.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 14754, out 872, 9.25 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a pedestrianized area or sidewalk to the right. There is
                        a junction or area of interest ahead with various lane markings. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a solid white line near my car. Further ahead in Photo 1, the line
                        appears to remain solid.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white circle with a bicycle symbol inside it in
                        the lane to my right. Photo 2 also shows a white circle with a bicycle symbol inside
                        it in my lane.; line:stop_line (full): Photo 1 shows a white line across the lane
                        ahead of my car, appearing to be a stop line or a line indicating a change in lane
                        configuration.
Step 4  Cross-check     close_up: The close-up confirms the left boundary is dashed and the right boundary is
                        solid. The bicycle symbols are clearly visible in both lanes. | position: The lane
                        count of 3 and my position as 2 (middle) is consistent with a dashed line on the left
                        and a solid line/curb on the right. | roles: The white dashed line on the left
                        correctly functions as a lane divider, and the solid white line/curb on the right
                        functions as an edge line. | markings: The bicycle symbols indicate a cycle lane to
                        the right, which is consistent with the solid edge line/boundary. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: You may cross the broken white line to overtake or turn off if it is
                        safe. [[UK-Rule127]]
Step 5  Rule            right_boundary: You must not drive in a cycle lane marked by a solid white line. [[UK-
                        Rule140]]
Step 5  Rule            symbol:bike: The bicycle symbol indicates a cycle lane where motor vehicles are
                        prohibited. [[UK-Rule140]]
Step 5  Rule            line:stop_line: You must not proceed beyond the line when required to stop. [[UK-
                        TSRGD-Part6,item1]]
Step 6  change_left     allowed (correct): allowed by the broken white line [UK-Rule127]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line and cycle lane
                        marking [UK-Rule140]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if it is safe to do so. Do not move into the lane to
                        your right as it is a designated cycle lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line', 'symbol:bike'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 1095, 12.59 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A residential street with a wide carriageway and a pedestrian area to the left. Ahead,
                        there is a junction or a wide open area with multiple lanes and parked cars. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from a pedestrian area/sidewalk. Photo 2
                        shows a solid white line next to the car and a dashed white line further ahead.
                        white solid_dashed (near line solid), curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line next to the car and a dashed white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: The same in both photos. | position: The lane count and position are
                        consistent. The left boundary is an edge line (curb/pedestrian area), and the right
                        boundary is a lane line. | roles: The white lines correctly define the boundaries of
                        the lane. | markings: The straight arrow is consistent with the lane's purpose. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            right_boundary: The broken white line indicates a lane divider, and you should keep
                        between them. [UK-Rule131] "Lane dividers. These are short, broken white lines which
                        are used on wide carriageways to divide them into lanes. You should keep between
                        them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane. Lane changes to the left or
                        right are prohibited by the solid lines near your car.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 865, 8.22 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the sidewalk/pedestrian area
                        on the left. Photo 2 shows a solid white line next to the car and a solid white line
                        further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a dashed white line separating my lane from the lane to the right. Photo
                        2 shows a dashed white line next to the car and a dashed white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:keep_clear (full): Photo 2 shows a white rectangle with the words 'KEEP CLEAR'
                        inside it in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries: a solid white line on the left indicates an edge line,
                        and a dashed white line on the right indicates a lane divider. | roles: The white
                        solid line on the left correctly acts as an edge line, and the dashed white line on
                        the right correctly acts as a lane divider. | markings: The 'KEEP CLEAR' marking is
                        centered in the lane and is consistent with the lane boundaries. | unseen: none |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line marks the edge of the carriageway available for
                        through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 5  Rule            right_boundary: The broken white line marks the centre of the road or a lane divider,
                        allowing for overtaking or lane changes when safe. [UK-Rule127] "A broken white line.
                        This marks the centre of the road. When this line lengthens and the gaps shorten, it
                        means that there is a hazard ahead. Do not cross it un"
Step 5  Rule            text:keep_clear: The 'KEEP CLEAR' marking indicates that the area should be kept free
                        of stationary vehicles. [UK-HC_MARKINGS-p3-2] "Keep entrance clear of stationary
                        vehicles, even if picking up or setting down children"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or change into the right lane if safe. Do not block the
                        'KEEP CLEAR' area with your vehicle.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:keep_clear'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 754, 7.71 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with buildings and shops on both sides. The road ahead appears
                        to be a straight stretch with multiple lanes for traffic moving in the same direction.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line near the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        carriageway. Photo 2 shows this solid white line clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (partial): Photo 1 shows a white dashed line in the middle of my lane
                        further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a dashed white line on the left indicates another
                        lane of my direction, and a solid white line on the right indicates the edge of the
                        carriageway. | roles: The dashed white line on the left fits the role of a lane
                        divider, and the solid white line on the right fits the role of an edge line. |
                        markings: The dashed line in the middle of the lane is consistent with a lane divider
                        for a multi-lane road. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used to divide
                        the carriageway into lanes. [UK-Rule131] "Lane dividers. These are short, broken white
                        lines which are used on wide carriageways to divide them into lanes. You should keep
                        between them."
Step 5  Rule            right_boundary: The solid white line marks the edge of the carriageway available for
                        through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 5  Rule            line:stop_yield: The dashed line in the center of the lane indicates a division of the
                        road into lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines
                        which are used on wide carriageways to divide them into lanes. You should keep between
                        them."
Step 6  change_left     allowed (contested, label prohibited): allowed
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may change into the left lane as
                        it is separated by a broken white line, but you must not move into the area to the
                        right of the solid white edge line. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 14754, out 951, 8.8 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a dedicated bus lane on the left. My car is in the lane
                        to the right of the bus lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the bus lane. Photo 2 shows this
                        line clearly as a solid white line next to my car, which then becomes a dashed white
                        line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line to my right. Photo 2 shows this as a dashed white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows 'BUS LANE' text and a bus symbol in the lane to my
                        left.; symbol:other (full): Photo 2 shows a yellow line marking the edge of the bus
                        lane area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on my left separates me from the bus
                        lane, and a white line on my right separates me from the next lane. | roles: The white
                        lines correctly function as lane dividers. | markings: The 'BUS LANE' marking is in
                        the lane to my left, which is consistent with the boundary separating my lane from it.
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the short, broken white lines used to divide
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the short, broken white lines used to divide
                        lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines which are used
                        on wide carriageways to divide them into lanes. You should keep between them."
Step 5  Rule            text:bus: Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation. [UK-Rule141] "Bus lanes. These are shown by road markings and
                        signs that indicate which (if any) other vehicles are permitted to use the bus lane."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight. Do not move into the bus lane on your
                        left, as it is reserved for buses. You may change into the lane on your right if it is
                        safe to do so.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:other', 'text:bus'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 941, 10.35 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a central area and side lanes. Ahead, the road appears to
                        have a central divider or markings separating opposing flows of traffic. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from a central area. Photo 2 shows this
                        line is a broken white line with a zigzag pattern.
                        white zigzag, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line is a broken white
                        line with a zigzag pattern.
                        white zigzag, curb yes, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 2 shows a white zigzag line in the center of the road.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the boundaries; the left boundary is a center line and the right is an
                        edge line. | roles: The white zigzag lines correctly identify the center and edge
                        boundaries. | markings: The channelizing markings (zigzag lines) are consistent with
                        the lane layout. | unseen: none | result: consistent
Step 5  Rule            left_boundary: A broken white line marks the center of the road; it may be crossed to
                        overtake or turn if safe. [UK-Rule127] "A broken white line. This marks the centre of
                        the road. When this line lengthens and the gaps shorten, it means that there is a
                        hazard ahead. Do not cross it un"
Step 5  Rule            right_boundary: The marking indicates the boundary between the main carriageway and a
                        diverging or merging traffic lane or the edge of the carriageway. [UK-
                        TSRGD-S11P4-item10] "Diagram 1010 (a) edge of the carriageway at a road junction or a
                        lay-by, or at an exit from a private drive onto a public road; (b) the start of a
                        traffic lane,"
Step 5  Rule            area:channelizing: The zigzag lines separate traffic lanes or protect traffic turning
                        right. [UK-Rule130] "Areas of white diagonal stripes or chevrons painted on the road.
                        These are to separate traffic lanes or to protect traffic turning right."
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken white center line (UK-
                        Rule127)
Step 6  change_right    prohibited (contested, correct): prohibited by the curb and edge line (UK-
                        TSRGD-S11P4-item10)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the left if safe. Do not attempt to move to the
                        right as it is bounded by a curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 14754, out 738, 16.21 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road approaching a junction. My car is in a lane that appears to be
                        a dedicated turn lane or a lane leading to a specific movement at the intersection.
                        (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this same white line clearly as a broken line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a raised curb and a metal fence on the right. Photo 2 shows a solid
                        white line painted next to the curb, which then meets the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow in my lane pointing straight ahead
                        and slightly to the left.; arrow:straight (full): Photo 2 shows a white arrow in the
                        lane to my left pointing straight ahead.; arrow:left (full): Photo 2 shows a white
                        arrow in the lane to the left of that (the leftmost lane) pointing left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (3)
                        agree with the boundaries: a white dashed line is on my left (lane_line) and a white
                        solid line/curb is on my right (edge_line). | roles: The white dashed line on the left
                        correctly identifies a lane divider, and the solid line/curb on the right correctly
                        identifies the edge of the carriageway. | markings: The arrows in the lanes correspond
                        to the lane layout and the boundaries. | unseen: none | result: consistent
Step 5  Rule            left_boundary: A broken white line marks the centre of the road or a lane divider; you
                        may cross it if it is safe to do so. [UK-Rule127] "A broken white line. This marks the
                        centre of the road. When this line lengthens and the gaps shorten, it means that there
                        is a hazard ahead. Do not cross it un"
Step 5  Rule            right_boundary: The solid white line and curb mark the edge of the carriageway
                        available for through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the
                        carriageway available for through traffic other than at a road junction, an exit from
                        a private drive onto a public road, lay-by "
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     allowed (correct): allowed by the broken white line (UK-Rule127)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line and curb (UK-
                        TSRGD-S11P4-item11)
Step 6  go_straight     allowed (WRONG, label prohibited): allowed by the straight arrow (UK-TSRGD-
                        Part6,item20)
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the straight arrow (UK-TSRGD-
                        Part6,item20)
Step 6  u_turn          prohibited (WRONG, label allowed): prohibited by the straight arrow (UK-TSRGD-
                        Part6,item20)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for going straight ahead. You may change into the lane to
                        your left if it is safe to do so, but you must not move to the right onto the
                        pavement. Do not attempt to turn left or right from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['arrow:right']), actions False, unsafe
                        ['go_straight'], citation in_pack_not_accepted, contradictions ['turn_left prohibited
                        although an arrow shows it']
Tokens                  in 14754, out 1148, 11.77 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a bus lane on the left and a central median. My car is
                        positioned in the lane to the right of the bus lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the bus lane. Photo 2 shows a
                        solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to my right. Photo 2
                        shows a solid white line next to my car. Further ahead, there is a physical
                        median/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows 'BUS LANE' text in the lane to my left.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on my left separates me from the bus
                        lane, and a white line/curb on my right defines the edge of my lane. | roles: The
                        white solid lines correctly function as lane dividers and edge lines. | markings: The
                        'BUS LANE' text is in the lane to the left, which is consistent with the solid white
                        line separating it from my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 5  Rule            text:bus: This indicates a bus lane, which is restricted for other vehicles. [UK-
                        Rule141] "Bus lanes. These are shown by road markings and signs that indicate which
                        (if any) other vehicles are permitted to use the bus lane."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight. Do not move into the bus lane on your
                        left or towards the curb on your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 14754, out 893, 8.91 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings and trees on both sides. The road ahead appears to be a
                        multi-lane street with parked cars on the right and a designated area on the left.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line and a curb on the left. Photo 2 shows a solid white
                        line and a curb on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line on the right. Photo 2 shows a broken white line on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows 'BUS' in yellow letters on the road surface in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree; the
                        left boundary is an edge line and the right is a lane divider. | roles: The white
                        solid line on the left acts as an edge line, and the broken white line on the right
                        acts as a lane divider. | markings: The 'BUS' text indicates a bus lane, which is
                        consistent with the lane's position and the markings. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line marks the edge of the carriageway available for
                        through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway
                        available for through traffic other than at a road junction, an exit from a private
                        drive onto a public road, lay-by "
Step 5  Rule            right_boundary: The broken white line marks the centre of the road or a lane divider,
                        allowing for crossing if safe. [UK-Rule127] "A broken white line. This marks the
                        centre of the road. When this line lengthens and the gaps shorten, it means that there
                        is a hazard ahead. Do not cross it un"
Step 5  Rule            text:bus: The 'BUS' marking indicates a lane reserved for buses. [UK-Rule141] "Bus
                        lanes. These are shown by road markings and signs that indicate which (if any) other
                        vehicles are permitted to use the bus lane."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     prohibited (contested, label allowed): prohibited
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  My lane is a designated bus lane, as indicated by the 'BUS' markings. You should not
                        drive in this lane unless you are a bus or an authorized vehicle; use the lane to the
                        right for general traffic.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed ['text:other']), actions True, unsafe [], citation accepted,
                        contradictions ['go_straight, turn_left, turn_right, u_turn decided without an arrow
                        or prohibited-movement marking']
Tokens                  in 14754, out 889, 10.4 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with shops and pedestrians on both sides. The road ahead
                        appears to be a straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line as a broken white line near the car and a solid white line further ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows this line as a solid
                        white line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (partial): Photo 1 shows red markings on the road surface
                        to the left of my lane, but none are inside my lane.
Step 4  Cross-check     close_up: Photo 2 shows the left boundary is a dashed line near the car and a solid
                        line further ahead, which is consistent with Photo 1. The right boundary is solid in
                        both. | position: The lane count of 3 and my position as lane 2 (middle) are
                        consistent with a lane line on the left and an edge line on the right. | roles: The
                        white dashed/solid line on the left acts as a lane divider, and the solid white line
                        on the right acts as an edge line. | markings: No markings are inside my lane. The red
                        markings to the left are outside my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You may cross the lines to overtake if it is safe, provided you can
                        complete the manoeuvre before reaching a solid white line on your side. [UK-Rule128]
                        "Double white lines where the line nearer to you is broken. This means you may cross
                        the lines to overtake if it is safe, provided you can complete the manoeuvre"
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     allowed (contested, label prohibited): Allowed by the dashed part of the left boundary
                        (UK-Rule128).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line (UK-
                        TSRGD-S11P4-item11).
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane if it is safe to do so,
                        but you must not move to the right as it is the edge of the carriageway. Proceed
                        straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 14754, out 954, 9.26 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a bus lane on the left and a parking area on the right.
                        The car is positioned in a central lane heading straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the bus lane. Photo 2 shows this
                        line is a solid white line near the car and becomes a broken white line further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from a parking lane. Photo 2 shows this
                        line is a broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show 'BUS LANE' text and a bus symbol in the lane
                        to the left.; line:stop_line (insufficient): Photo 1 and Photo 2 show a white line
                        separating the bus lane from my lane.
Step 4  Cross-check     close_up: The left boundary is solid near the car and broken further ahead in both
                        photos. The right boundary is dashed in both. | position: The lane count (3) and my
                        position (2) are consistent with the boundaries (lane line on left, lane line on
                        right). | roles: The white lines correctly function as lane dividers. | markings: The
                        'BUS LANE' marking is in the lane to the left, consistent with the left boundary. |
                        unseen: none | result: consistent
Step 5  Rule            left_boundary: You must not cross the solid white line unless it is safe and necessary
                        to enter adjoining premises or a side road. [UK-Rule129] "Double white lines where the
                        line nearer to you is solid. This means you MUST NOT cross or straddle it unless it is
                        safe and you need to enter adjoining premise"
Step 5  Rule            right_boundary: You should keep between the broken white lines. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            text:bus: Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation. [UK-Rule141] "Bus lanes. These are shown by road markings and
                        signs that indicate which (if any) other vehicles are permitted to use the bus lane."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight. Do not move into the bus lane on your
                        left as it is marked for buses only. You may move to the right if necessary.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line', 'text:bus'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 14754, out 945, 9.41 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a cycle lane on the left. My car is in a lane heading
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from a cycle lane. Photo 2 shows
                        a solid yellow line next to my car and a solid yellow line further ahead.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line to my right. Photo 2 shows a white dashed line next
                        to my car and a white dashed line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a yellow edge line on the left and a white dashed
                        lane line on the right. | roles: The yellow solid line correctly acts as an edge line
                        for the cycle lane, and the white dashed line acts as a lane divider. | markings: The
                        straight arrow is consistent with the lane's purpose. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The yellow line indicates a waiting restriction, but as an edge line,
                        it defines the boundary of the carriageway. [UK-HC_MARKINGS-p2] "Waiting restrictions
                        indicated by yellow lines apply to the carriageway, pavement and verge. You may stop
                        to load or unload (unless there are also loading restr"
Step 5  Rule            right_boundary: The broken white line marks the centre of the road or a lane divider,
                        allowing for overtaking or lane changes if safe. [UK-Rule127] "A broken white line.
                        This marks the centre of the road. When this line lengthens and the gaps shorten, it
                        means that there is a hazard ahead. Do not cross it un"
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       prohibited: prohibited
Step 6  turn_right      prohibited: prohibited
Step 6  u_turn          prohibited: prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should proceed straight ahead in your current lane. A lane change to the right is
                        permitted if safe, but changing to the left into the cycle lane is prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 881, 8.66 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a central divider and parking areas on both sides. My
                        car is in a lane heading straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to my left. Photo 2
                        shows a solid white line very close to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb/island to the right. Photo 2 shows
                        a solid white line and a raised curb/island immediately to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings visible in my lane in Photo 1 or Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a white line on the left separates me from another lane,
                        and a white line/curb on the right marks the edge. | roles: The white solid line on
                        the left is a lane divider, and the white solid line with a curb on the right is an
                        edge line. | markings: No markings are present in the lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: You should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: This marks the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in your current lane to proceed straight ahead. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 823, 8.95 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban street with shops on both sides. The road ahead has several lanes
                        and a clear junction area with speed limit markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line as a solid white line near the car, which then becomes a dashed white line
                        further ahead.
                        white solid_dashed (near line solid), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line as a dashed white line near the car and continuing as a dashed white
                        line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a '20' speed limit circle in the center of my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        the middle lane (2) are consistent with the white lines on both sides. | roles: The
                        white lines correctly function as lane dividers. | markings: The '20' speed limit
                        marking is centered in my lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You may cross the lines to overtake if it is safe, provided you can
                        complete the manoeuvre before reaching a solid white line on your side. [UK-Rule128]
                        "Double white lines where the line nearer to you is broken. This means you may cross
                        the lines to overtake if it is safe, provided you can complete the manoeuvre"
Step 5  Rule            right_boundary: You should keep between the short, broken white lines which are used
                        to divide lanes. [UK-Rule131] "Lane dividers. These are short, broken white lines
                        which are used on wide carriageways to divide them into lanes. You should keep between
                        them."
Step 5  Rule            text:speed_limit: No specific rule passage provided for the '20' marking, but it
                        indicates a speed limit.
Step 6  change_left     allowed (contested, correct): allowed
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right as long as it is
                        safe to do so. Observe the 20 mph speed limit indicated in your lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['change_left allowed
                        with the solid line of a solid-and-broken pair nearer my lane']
Tokens                  in 14754, out 889, 7.69 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a central area marked with zig-zag lines. Ahead, there is
                        a junction or a wide area where lanes appear to converge or diverge. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to my left. Photo 2 shows
                        this line is a broken white line near my car and becomes a solid white line further
                        ahead as it forms part of a zig-zag pattern.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to my right. Photo 2 shows
                        this line is a broken white line near my car and also becomes part of a zig-zag
                        pattern further ahead.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show white zig-zag lines across the center of
                        the road.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position are
                        consistent with the white lines on both sides. | roles: The white lines correctly
                        function as lane dividers. | markings: The zig-zag lines are consistent with a central
                        area or pedestrian crossing zone. | unseen: none | result: consistent
Step 5  Rule            left_boundary: You should keep between the broken white lines. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            right_boundary: You should keep between the broken white lines. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            area:grid: The zig-zag lines separate traffic lanes or protect turning traffic. [UK-
                        Rule130] "Areas of white diagonal stripes or chevrons painted on the road. These are
                        to separate traffic lanes or to protect traffic turning right."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay within your lane and proceed straight. Lane changes to the left or right are
                        prohibited due to the lane markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions ['change_left prohibited with the broken line of a solid-and-broken
                        pair nearer my lane', 'change_right prohibited with the broken line of a solid-and-
                        broken pair nearer my lane']
Tokens                  in 14754, out 685, 8.09 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test B | gemma4:12b
------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with trees on both sides. A red double-decker bus is in the
                        lane to the left, and a silver van is in the lane to the right. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the bus lane. Photo 2 shows this
                        line is a broken white line near my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane with the van. Photo 2
                        shows this line is a solid white line near my car. Further ahead in Photo 1, the line
                        appears to remain solid.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and my position (2)
                        are consistent with the boundaries: a white line on my left (lane 1) and a white line
                        on my right (lane 3). | roles: The white dashed line on the left and solid line on the
                        right correctly define the lane boundaries. | markings: The straight arrow in my lane
                        is consistent with the lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: A broken white line marks the centre of the road or a lane divider; you
                        may cross it if it is safe to do so. [UK-Rule127] "A broken white line. This marks the
                        centre of the road. When this line lengthens and the gaps shorten, it means that there
                        is a hazard ahead. Do not cross it un"
Step 5  Rule            right_boundary: Lane dividers are short, broken white lines; however, since this is
                        solid, it indicates a prohibition on crossing unless necessary for safety or entering
                        a side road. [UK-Rule131] "Lane dividers. These are short, broken white lines which
                        are used on wide carriageways to divide them into lanes. You should keep between
                        them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     allowed (correct): allowed by the broken white line (UK-Rule127)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white line (UK-Rule131)
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  turn_left       prohibited: prohibited by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  turn_right      prohibited: prohibited by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  u_turn          prohibited: prohibited by the straight arrow (UK-TSRGD-Part6,item20)
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. You may change into the left
                        lane if safe, but you must not change into the right lane. Do not turn left or right
                        from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 14754, out 846, 7.43 s
```
