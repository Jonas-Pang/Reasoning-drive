# Reasoning of lane run 20261117_043107_laneB_US

```text
bdd100k_val__b1c66a42-6f7d68ca | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from a median/curb area on the left.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): The word 'SCHOOL' is painted in white in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. A yellow
                        line on the left indicates a center line/median, and a white line on the right
                        indicates a lane line. | roles: The yellow solid line fits the center line role, and
                        the white solid line fits the lane line role. | markings: The 'SCHOOL' text is
                        centered in the lane and does not contradict the boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line on a two-way
                        roadway, but here it delineates the separation of opposite traffic flows or a median.
                        [[US-3B.01-05]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [[US-3B.06-05-06]]
Step 5  Rule            text:other: The 'SCHOOL' marking is used for guidance or warning and does not restrict
                        specific movements. [[US-3B.20-01]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited: prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your lane. Lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8634, out 851, 6.73 s

bdd100k_val__b1f0efd9-e900c6e5 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           An urban street with an intersection ahead. My car is in a lane approaching a
                        crosswalk and a pedestrian crossing signal. (lanes 2, mine 1, full)
Step 2  Left            A raised concrete curb and a small median island are on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to the
                        right, but my lane has no arrows or words.
Step 4  Cross-check     position: The lane count (2) and my position (1) are consistent with the left curb and
                        right dashed line. | roles: The left curb acts as an edge line and the right dashed
                        line acts as a lane line. | markings: No markings are visible in my lane to contradict
                        the boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: No specific rule for a curb is provided, but it serves as a physical
                        boundary. [null]
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the right lane is
                        permitted. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  change_right    allowed (correct): right_boundary is a broken white line, which is permissive
                        [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may proceed straight or change into the right lane. Be mindful of the pedestrian
                        crossing and the upcoming intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8634, out 794, 7.75 s

bdd100k_val__b1f4491b-dd8dfed5 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the right. The road
                        ahead appears to be a straight stretch of highway. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white dashed
                        line on my left and the white solid line/barrier on my right. | roles: The white
                        dashed line correctly identifies a lane-line (same direction), and the white solid
                        line correctly identifies an edge-line. | markings: No markings were observed, which
                        is consistent with a standard through-lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02] and the presence of a concrete barrier.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn markings or arrows are present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn markings or arrows are present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn markings or arrows are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the left lane. Changing into the right lane
                        is prohibited by the edge line and the concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 858, 8.42 s

bdd100k_val__b20b69d2-e31380a7 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane roadway approaching a fork or a split in the road. A large
                        sign for 'West View City' is visible ahead. (lanes 2, mine 2, full)
Step 2  Left            A yellow curb and a painted yellow line separate my lane from a median/island on the
                        left.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A white line separates my lane from a guardrail and a shoulder on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): none
Step 4  Cross-check     position: The lane count (2) and my lane position (2) agree with the boundaries: a
                        yellow center line is on my left and a white edge line is on my right. | roles: The
                        yellow solid line correctly identifies a center line/median boundary, and the white
                        solid line correctly identifies the right edge. | markings: No markings are present in
                        the lane, which is consistent with the clear roadway ahead. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The yellow line delineates the separation of traffic traveling in
                        opposite directions or a median. [[US-3A.03-03-04]]
Step 5  Rule            right_boundary: The white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 777, 7.41 s

bdd100k_val__b263f57d-1ccf6e51 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street in wet conditions, approaching an intersection with traffic
                        signals. My car is in one of the right-hand lanes. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a concrete curb/sidewalk to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A white stop line is visible ahead of my lane at the
                        intersection.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on my left and a white solid line/curb on my right. | roles: The white dashed
                        line correctly identifies a lane-to-lane separation, and the white solid line/curb
                        correctly identifies the right edge of the roadway. | markings: The stop line is
                        consistent with an approaching intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            line:stop_line: Vehicles are required to stop behind the white line. [US-3B.19-01-02]
                        "Stop lines may be used to indicate the point behind which vehicles are required to
                        stop in compliance with a STOP sign ... or some other traffic control device "
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited: Prohibited by the solid white edge line and curb [US-3B.09-01-02].
Step 6  go_straight     stop_first (contested, label allowed): Allowed as no markings prohibit it, but must
                        stop first due to the stop line.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow or area is present.
Step 6  turn_right      not_applicable (WRONG, label allowed): Not applicable as no right-turn arrow or area
                        is present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn arrow or area is present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if desired. You must come to a complete stop at the
                        white line before proceeding through the intersection.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 922, 8.12 s

bdd100k_val__b2fbf86d-d5de82a4 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with tall buildings on both sides. The road ahead is
                        straight, and there are several vehicles in the surrounding lanes. (lanes 4, mine 2,
                        full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible in the middle of my
                        lane, but it appears to be a lane divider for the adjacent lane, not a marking within
                        my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as lane 2 are consistent with the white
                        dashed lines on both sides. | roles: The white dashed lines correctly indicate lane
                        separation for traffic moving in the same direction. | markings: No markings are
                        clearly inside my lane; the dashed lines are boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 6  change_left     allowed (correct): Allowed by the white dashed left boundary line [US-3B.06-05-06].
Step 6  change_right    allowed (correct): Allowed by the white dashed right boundary line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn markings are present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn markings are present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn markings are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a standard through lane. You may change lanes to the left or right as the
                        dashed lines permit. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 8634, out 836, 9.13 s

bdd100k_val__b3060c96-d2391b61 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road lined with trees. The road ahead appears to be a straight
                        stretch with an intersection or signalized area in the distance. (lanes 3, mine 1,
                        full)
Step 2  Left            A solid yellow line separates my lane from a grassy area with trees on the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (insufficient): none
Step 4  Cross-check     position: The lane count (3) and my position (1) are consistent with a yellow edge
                        line on the left and a white lane line on the right. | roles: The yellow solid line
                        correctly identifies the left edge of the roadway, and the white dashed line correctly
                        identifies a lane divider. | markings: No markings are visible in my lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: The solid white line (or yellow in this context) delineates the left-
                        hand edge of the roadway. [US-3B.09-01-02] "If used, edge line pavement markings shall
                        delineate the right or left edges of a roadway. ... Right edge line pavement markings,
                        if used, shall consist of a no"
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        is permitted. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (WRONG, label not_determined): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change into the lane to your
                        right. Changing to the left is prohibited by the solid yellow edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8634, out 788, 6.18 s

bdd100k_val__b306fb3f-f02e46cc | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a grassy embankment on the left. The road continues straight
                        ahead. (lanes 3, mine 1, full)
Step 2  Left            A solid yellow line separates my lane from the grassy area on the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (1) are consistent with the left edge
                        line and right lane line. | roles: The yellow solid line correctly identifies the left
                        edge of the roadway, and the white dashed line correctly identifies a lane divider. |
                        markings: No markings are present to contradict the boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line (or yellow in this context) delineates the left-
                        hand edge of the roadway. [US-3B.09-01-02] "If used, edge line pavement markings shall
                        delineate the right or left edges of a roadway. ... Right edge line pavement markings,
                        if used, shall consist of a no"
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        is permitted. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (WRONG, label not_determined): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change into the lane to your
                        right. Changing to the left is prohibited by the solid yellow edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 757, 7.63 s

bdd100k_val__b321c6b6-ab603d42 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A city street with multiple lanes of traffic moving forward. There is a construction
                        zone or barrier on the left side of the road. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from a lane to the left, which is bordered by a
                        construction barrier.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane to the right where cars are parked or
                        stopped.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the center
                        of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 are consistent with the white
                        lane lines on both sides. | roles: The white solid lines correctly delineate lanes of
                        the same direction. | markings: The straight arrow is consistent with the lane's role
                        as a through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 818, 7.09 s

bdd100k_val__b4542860-0b880bb4 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. The road is wide with several
                        lanes of traffic moving in the same direction. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane or a lane ending.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3rd from left) are consistent with the
                        white lane lines on both sides. | roles: The white dashed line on the left and solid
                        white line on the right are consistent with lane-to-lane separation. | markings: The
                        left-turn arrow in my lane is consistent with the lane's function as a turn lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement from this
                        lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     allowed (correct): allowed by the dashed white line on the left (US-3B.06-05-06).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        (US-3B.06-05-06).
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the left-turn arrow in my lane
                        (US-3B.23-01).
Step 6  turn_left       allowed: allowed by the left-turn arrow in my lane (US-3B.23-01).
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated left-turn lane. You are permitted to turn left or change into
                        the lane to your left, but you should not attempt to go straight or change into the
                        lane to your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 934, 8.87 s

bdd100k_val__b48c7b5f-800d31b4 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with a taxi directly ahead. The road appears to be a one-way
                        street or a multi-lane roadway with a curb on the right. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line and a raised curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in the lane
                        ahead of the taxi.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        yellow center line on the left and a white edge line/curb on the right. | roles: The
                        yellow line on the left correctly identifies a center line (separation of opposite
                        traffic or a special lane), and the white line on the right correctly identifies an
                        edge line. | markings: The straight arrow in the lane ahead is consistent with the
                        lane's purpose. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The yellow line delineates the separation of traffic traveling in
                        opposite directions. [US-3A.03-03-04] "When used, yellow markings for longitudinal
                        lines shall delineate: A. The separation of traffic traveling in opposite directions,
                        B. The left-hand edge of the r"
Step 5  Rule            right_boundary: The white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory
                        or permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid yellow center line
                        [US-3A.04-01]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line and
                        curb [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking [US-3B.23-01]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are prohibited by the solid markings and the curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8634, out 741, 7.32 s

bdd100k_val__b49d6c0d-457e13b3 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings and storefronts on both sides. The road ahead
                        appears to be a straight continuation of the current street. (lanes 2, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking area or curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol is painted in the center of my lane.
Step 4  Cross-check     position: The lane count (2) and my position (2) are consistent with the boundaries: a
                        double yellow center line is on my left, and a white edge line is on my right. |
                        roles: The yellow double solid line correctly identifies a center line, and the white
                        solid line correctly identifies an edge line. | markings: The bicycle symbol is
                        centered in the lane, consistent with its role as a designated lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            symbol:bike: The bicycle symbol indicates a preferential lane for bicycles.
                        [[US-3E.01-01]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for bicycles, as indicated by the pavement symbol. You
                        may proceed straight, but you are prohibited from changing lanes to the left due to
                        the double solid yellow line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 845, 7.33 s

bdd100k_val__b4d18d1a-193e24a1 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane that appears
                        to be a turn lane or a lane approaching an intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        parking or curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in my lane.;
                        area:left_turn_waiting (full): A white left-turn waiting area is visible ahead of my
                        lane.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries
                        (white line on left, white line/curb on right). | roles: The white lines and curb
                        roles are consistent with standard US markings. | markings: The left-turn arrow and
                        waiting area are consistent with the lane's role as a turn lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible or mandatory
                        movement. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 5  Rule            area:left_turn_waiting: The area provides a space to wait for a left turn. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left
                        (US-3B.06-05-06).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line and curb on the
                        right (US-3B.09-01-02).
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the left-turn arrow
                        (US-3B.23-01).
Step 6  turn_left       allowed: allowed by the left-turn arrow (US-3B.23-01).
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areaallowed: allowed by the left-turn waiting area marking.
Step 7  Reflect         consistent
Advice                  Use this lane to turn left. You may enter the left-turn waiting area ahead. Lane
                        changes to the left or right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:left_turn_waiting', 'arrow:left'], missed []), actions False, unsafe [],
                        citation unlisted, contradictions []
Tokens                  in 8634, out 1015, 8.96 s

bdd100k_val__b5042634-1034573c | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway under an overpass structure. Ahead, there is a
                        signalized intersection or a point where lanes may merge or change. (lanes 3, mine 2,
                        full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is occupied by a
                        taxi.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white color and dashed/solid patterns are consistent
                        with lane-to-lane separation. | markings: The straight arrow is consistent with the
                        lane's forward path. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement for
                        this lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory
                        or permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     allowed (correct): allowed by the dashed white line on the left (US-3B.06-05-06).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        (US-3B.06-05-06).
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking (US-3B.23-01).
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change into the left lane.
                        Changing into the right lane is prohibited by the solid white line.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 883, 7.73 s

bdd100k_val__b54c065e-8b13cfe7 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban street with a vehicle ahead. The road appears to be a one-way
                        street or a multi-lane roadway with a clear right-hand edge. (lanes 3, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane or area to my right, with a curb
                        visible further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        double yellow line on the left indicates a center line, and a white line on the right
                        indicates an edge line. | roles: The yellow double solid line correctly identifies a
                        center line for opposite traffic, and the white solid line correctly identifies the
                        right edge. | markings: No markings are present in my lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the left lane for
                        passing. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight ahead. Lane changes to the left
                        or right are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 789, 6.89 s

bdd100k_val__b5661732-3684230b | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on both sides. The road ahead is straight with
                        several lanes of traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both the left and right. | roles: The white dashed lines correctly
                        identify as lane lines between same-direction traffic. | markings: No markings are
                        present, which is consistent with the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): Allowed by the white dashed left boundary [US-3B.06-05-06].
Step 6  change_right    allowed (correct): Allowed by the white dashed right boundary [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no turn markings or areas are present.
Step 6  turn_right      not_applicable: Not applicable as no turn markings or areas are present.
Step 6  u_turn          not_applicable: Not applicable as no turn markings or areas are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane roadway. You may change lanes to the left
                        or right as the lane markings are dashed. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 815, 7.53 s

bdd100k_val__b577827c-28fc9b0d | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway approaching an intersection with a subway station on the right.
                        My car is in one of the center lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.;
                        arrow:left (full): A white arrow pointing left is in the lane to my left.; arrow:right
                        (full): A white arrow pointing right is in the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes of the
                        same direction. | markings: The straight arrow in my lane is consistent with the solid
                        white boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement for
                        this lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory
                        or permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (correct): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (contested, correct): allowed by the arrow:straight marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight'], missed []), actions False, unsafe [],
                        citation accepted, contradictions ['turn_left not_applicable although an arrow shows
                        it', 'turn_right not_applicable although an arrow shows it']
Tokens                  in 8634, out 907, 6.9 s

bdd100k_val__b59e50fa-ca034dd0 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on both sides and a clear view ahead. The road
                        appears to be a one-way street or a multi-lane roadway with traffic moving in the same
                        direction. (lanes 4, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible in the middle of my
                        lane, but no arrows or words are present.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white dashed lines on both sides. | roles: White dashed lines correctly indicate
                        lane separation for traffic moving in the same direction. | markings: No specific
                        arrows or words are visible in my lane to contradict the boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 6  change_left     allowed (correct): Allowed by the white dashed left boundary [US-3B.06-05-06].
Step 6  change_right    allowed (correct): Allowed by the white dashed right boundary [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn markings are present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn markings are present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn markings are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You are in a standard through lane. You may change lanes to the left or right as the
                        dashed white lines permit it. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 8634, out 839, 7.74 s

bdd100k_val__b5cd5f72-32232751 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway approaching an intersection with a turn lane. My car is in a lane
                        that appears to be a dedicated turn lane or a lane with a specific turn marking.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right edge of the roadway/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white arrow pointing to the right is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the edge line on my right. | roles: The white solid lines
                        correctly delineate same-direction traffic and the right edge of the roadway. |
                        markings: The right-turn arrow in my lane is consistent with the lane's function as a
                        turn lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        my left. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:right: The arrow indicates that a right turn is a permissible movement from this
                        lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     prohibited (correct): prohibited
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      allowed (correct): allowed
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated right-turn lane. You should only perform a right turn at the
                        upcoming intersection. Lane changes to the left or right are prohibited by the solid
                        lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 846, 6.79 s

bdd100k_val__b5f84825-c97df380 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a city street approaching an intersection. My car is in a lane that
                        appears to be a turn lane or a lane leading into an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is a right-turn
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight ahead with a turn to the
                        left.; arrow:right (full): A white arrow pointing to the right.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight-left arrow in my lane is
                        consistent with the lane's position between a left-turn lane and a right-turn lane. |
                        unseen: None | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right-
                        turn lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:straight_left: The arrow indicates that straight ahead and left turns are the
                        permitted movements for this lane. [US-3B.23-01] "Lane-use arrow markings are used to
                        indicate the mandatory or permissible movements in certain lanes and in two-way left-
                        turn lanes."
Step 5  Rule            arrow:right: The arrow in the adjacent lane indicates a right turn is the permitted
                        movement for that lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate
                        the mandatory or permissible movements in certain lanes and in two-way left-turn
                        lanes."
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight_left marking
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the arrow:straight_left marking
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight or turn left from your current lane. Lane changes to the left
                        or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right', 'arrow:straight_left'], missed ['arrow:straight_right',
                        'line:stop_line']), actions False, unsafe ['turn_left'], citation accepted,
                        contradictions ['turn_right not_applicable although an arrow shows it']
Tokens                  in 8634, out 964, 8.61 s

bdd100k_val__b65fd3df-87ed965a | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a city street with parked cars on the right and a multi-lane roadway
                        ahead. The car is positioned in a lane that appears to be part of a multi-lane flow.
                        (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a row of parked cars on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as lane 2 (rightmost) are consistent
                        with a white lane line on my left and a white edge line on my right. | roles: The
                        white solid lines correctly identify a lane-to-lane separation on the left and a
                        roadway edge on the right. | markings: No markings were observed in the lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line on the
                        left
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line on the
                        right
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the roadway. You may proceed straight ahead, but lane
                        changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 652, 6.72 s

bdd100k_val__b7041acc-6de39959 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway approaching an overpass and an intersection. There are several
                        lanes of traffic moving in the same direction. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white dashed
                        line on my left and the white solid line on my right. | roles: The white dashed line
                        correctly identifies a lane-line (same direction), and the white solid line correctly
                        identifies an edge-line. | markings: The left-turn arrow is consistent with the lane's
                        function as it approaches the intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed lane line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement from this
                        lane. [[US-3B.23-01]]
Step 6  change_left     allowed (correct): Allowed by the dashed white lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking prohibits it and the arrow
                        indicates a turn is possible.
Step 6  turn_left       allowed: Allowed by the left-turn arrow [US-3B.23-01].
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or marking.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow or marking.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  You may turn left or continue straight from your current lane. You are permitted to
                        change into the lane to your left, but you should not move to the right as it is the
                        edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation accepted, contradictions
                        ['go_straight allowed although no arrow shows it']
Tokens                  in 8634, out 930, 7.69 s

bdd100k_val__b7935597-13c4b9dd | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with parked cars on both sides. An intersection is visible
                        ahead with a traffic light. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings are visible in my lane.; line:yield_line
                        (insufficient): No markings are visible in my lane.; line:stop_yield (insufficient):
                        No markings are visible in my lane.; arrow:merge_left (insufficient): No markings are
                        visible in my lane.; arrow:merge_right (insufficient): No markings are visible in my
                        lane.; arrow:two_way_left (insufficient): No markings are visible in my lane.;
                        text:only (insufficient): No markings are visible in my lane.; text:bus
                        (insufficient): No markings are visible in my lane.; text:hov (insufficient): No
                        markings are visible in my lane.; text:stop (insufficient): No markings are visible in
                        my lane.; text:keep_clear (insufficient): No markings are visible in my lane.;
                        text:speed_limit (insufficient): No markings are visible in my lane.;
                        symbol:hov_diamond (insufficient): No markings are visible in my lane.; symbol:bike
                        (insufficient): No markings are visible in my lane.; symbol:other (insufficient): No
                        markings are visible in my lane.; area:left_turn_waiting (insufficient): No markings
                        are visible in my lane.; area:two_way_left_turn_lane (insufficient): No markings are
                        visible in my lane.; area:grid (insufficient): No markings are visible in my lane.;
                        area:channelizing (insufficient): No markings are visible in my lane.; line:crosswalk
                        (insufficient): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. I am in
                        the left lane of two lanes moving in the same direction. | roles: The white solid
                        lines correctly identify as lane lines between same-direction traffic. | markings: No
                        markings were observed, which is consistent with the lack of specific movement
                        instructions. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white right boundary
                        line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but lane changes to the
                        left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'symbol:bike', 'symbol:hov_diamond', 'symbol:other', 'text:bus',
                        'text:hov', 'text:keep_clear', 'text:only', 'text:speed_limit', 'text:stop'], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['leftmost lane, but a
                        lane line on the left', 'go_straight allowed without the stop that the STOP or 停
                        marking in my lane requires']
Tokens                  in 8634, out 1167, 10.99 s

bdd100k_val__b7aa329e-25d68dec | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A two-way residential street with trees and houses on both sides. The road ahead
                        appears to be a continuous two-way street. (lanes 2, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and grass beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my lane position (2) agree with the boundaries: a
                        double yellow center line is on my left, and a white edge line is on my right. |
                        roles: The yellow double solid line correctly identifies a center line for opposite
                        traffic, and the white solid line correctly identifies the right edge. | markings: No
                        markings are present, which is consistent with a standard through lane. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite lane
                        for passing. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-way street. You may proceed straight ahead,
                        but you are prohibited from crossing the double yellow line to the left or moving onto
                        the shoulder/curb to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 798, 7.17 s

bdd100k_val__b80018ef-3a620af0 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban street at night. The road ahead appears to be a straight stretch
                        with parked cars on both sides. (lanes 2, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as lane 2 (rightmost) are consistent
                        with a center line on my left and an edge line on my right. | roles: The yellow double
                        solid line correctly identifies a center line, and the white solid line correctly
                        identifies a right edge line. | markings: No markings were reported in my lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the adjacent lane
                        for traffic in the opposite direction. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-06]
Step 6  change_right    not_applicable (contested, label prohibited): no marking governs this action
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead. Changing lanes to the
                        left is prohibited by the double solid yellow line.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 610, 6.41 s

bdd100k_val__b84146a1-a5f588ef | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane with other
                        vehicles moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No arrows, words, or symbols are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: White lines are correct for same-direction traffic
                        separation. | markings: No markings were observed in the lane. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white line on the left [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if necessary, but you should not change into the
                        right lane. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8634, out 802, 8.01 s

bdd100k_val__b8fe9f2b-d63131a3 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white line is painted across the lane ahead, appearing to be
                        a stop line.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both my left and right. | roles: The white solid lines correctly
                        function as lane lines between same-direction traffic. | markings: The stop line is
                        consistent with an approaching intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: The stop line indicates the point behind which vehicles are required
                        to stop. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left_boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right_boundary line
Step 6  go_straight     stop_first (contested, label allowed): allowed as no markings prohibit it, but must
                        stop first
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You must come to a complete stop at the white stop line
                        before proceeding straight through the intersection. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 853, 7.99 s

bdd100k_val__b91cdc5d-bce994ce | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with parked cars on the right and a row of residential
                        buildings. The road ahead appears to be a standard urban street with multiple lanes of
                        traffic. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        curb and parked cars.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white dashed line on the left and solid white line
                        on the right correctly identify lane-to-lane boundaries. | markings: The left-turn
                        arrow in my lane is consistent with the urban street context. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement from this
                        lane. [[US-3B.23-01]]
Step 6  change_left     allowed (correct): allowed by the dashed white line on the left [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it
Step 6  turn_left       allowed: allowed by the left-turn arrow [US-3B.23-01]
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may turn left or continue straight from your current lane. You are permitted to
                        change into the left lane, but changing into the right lane is prohibited by the solid
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight allowed although no arrow shows it']
Tokens                  in 8634, out 901, 7.52 s

bdd100k_val__b928271b-fe5cc5d1 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban street with an intersection ahead. My car is in one of the
                        rightmost lanes. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with a white dashed
                        line on my left and a solid white line/curb on my right. | roles: The white dashed
                        line correctly identifies a lane-line, and the white solid line correctly identifies
                        an edge-line. | markings: No markings were observed in my lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn markings are present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn markings are present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn markings are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may move into the lane to your left. You are prohibited from moving to the right
                        onto the curb. You may proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 824, 8.33 s

bdd100k_val__b9429f07-33ae3ff1 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road approaching an intersection. The car is in a lane heading
                        straight toward the intersection. (lanes 3, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which ends at a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a center line on
                        the left and an edge line on the right. | roles: The yellow double solid line
                        correctly identifies a center line, and the white solid line correctly identifies an
                        edge line. | markings: No markings are present in the lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the left lane for
                        passing. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-06]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 797, 7.51 s

bdd100k_val__ba2db972-f29458c8 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a commercial area on the right. The road ahead appears to
                        continue straight. (lanes 3, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, adjacent to a curb and a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my left,
                        but no markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the boundaries: a
                        white dashed line is on my left (lane line) and a white solid line is on my right
                        (edge line). | roles: The white dashed line correctly identifies a lane to the left,
                        and the white solid line correctly identifies the right edge. | markings: No markings
                        are present in my lane to contradict the boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the left lane. Do not attempt to move to the
                        right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 837, 5.79 s

bdd100k_val__ba9f6c98-2a75a096 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A two-lane rural roadway with a clear view ahead. The road appears to be a two-way
                        street with a grassy area and some buildings on the left and right. (lanes 2, mine 2,
                        full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): A small, faint, dark marking or crack is visible in the center of
                        the lane, but it is not a standard pavement marking.
Step 4  Cross-check     position: The lane count (2) and my lane position (2) agree with the boundaries: a
                        double yellow center line is on my left and a white edge line is on my right. | roles:
                        The double yellow center line and white edge line fit their respective roles
                        correctly. | markings: The faint marking does not correspond to any standard lane-use
                        markings or arrows. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the opposite lane
                        for passing. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-06]
Step 6  change_right    allowed (contested, label prohibited): no marking governs this action
Step 6  go_straight     allowed (contested, correct): allowed as there is no arrow prohibiting it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-way road. You may proceed straight or move
                        slightly to the right if needed, but you are prohibited from crossing the double
                        yellow line to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:other'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 829, 7.87 s

bdd100k_val__bab692c9-4d1f2bdd | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with a light rail track in the center. The road ahead is
                        straight, flanked by buildings and trees. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the light rail tracks.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is to my left and a white lane line is to my right. | roles: The
                        yellow solid line correctly identifies a center line (separation from opposite/special
                        traffic), and the white solid line correctly identifies a same-direction lane line. |
                        markings: No markings are present to contradict the boundaries. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The yellow line delineates the separation of traffic flows in opposite
                        directions or special lanes. [US-3A.03-03-04] "When used, yellow markings for
                        longitudinal lines shall delineate: A. The separation of traffic traveling in opposite
                        directions, B. The left-hand edge of the r"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is
                        not discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 771, 6.75 s

bdd100k_val__bb289fdb-4bc01501 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway at night. The road continues straight ahead toward a city
                        skyline with visible buildings and streetlights. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be an
                        edge lane or a lane ending.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my left.;
                        area:two_way_left_turn_lane (insufficient): No markings are visible within my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white lines correctly delineate lanes of
                        traffic moving in the same direction. | markings: No markings are present in my lane
                        to contradict the boundaries. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the dashed white line on the left [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line on the right
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the left lane. Changing into the right lane
                        is prohibited by the solid white line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane', 'line:stop_line'], missed []), actions False, unsafe
                        [], citation accepted, contradictions []
Tokens                  in 8634, out 861, 6.24 s

bdd100k_val__bb8dba97-3537805c | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane divided highway or expressway. The road ahead is straight with several
                        lanes of traffic moving in the same direction. (lanes 3, mine 1, full)
Step 2  Left            A solid yellow line separates my lane from a median or barrier on the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none; line:yield_line (insufficient): none;
                        line:stop_yield (insufficient): none; arrow:merge_left (insufficient): none;
                        arrow:merge_right (insufficient): none; arrow:two_way_left (insufficient): none;
                        no_turn:left (insufficient): none; no_turn:right (insufficient): none; text:only
                        (insufficient): none; text:bus (insufficient): none; text:hov (insufficient): none;
                        text:stop (insufficient): none; text:keep_clear (insufficient): none; text:speed_limit
                        (insufficient): none; text:other (insufficient): none; symbol:hov_diamond
                        (insufficient): none; symbol:bike (insufficient): none; symbol:other (insufficient):
                        none; area:left_turn_waiting (insufficient): none; area:two_way_left_turn_lane
                        (insufficient): none; area:grid (insufficient): none; area:channelizing
                        (insufficient): none; line:stop_line (insufficient): none
Step 4  Cross-check     position: The lane count of 3 and my position as 1 (leftmost) is consistent with a
                        solid yellow edge line on the left and a white dashed lane line on the right. | roles:
                        The yellow solid line correctly identifies the left edge of the roadway, and the white
                        dashed line correctly identifies the lane separation to the right. | markings: No
                        markings were observed in the lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the right-hand edge of the roadway, but
                        here a yellow line is used for the left-hand edge of the roadway. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        is permitted. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line
Step 6  change_right    allowed (correct): allowed by the broken white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may move into the lane to your right as the white
                        line is broken. You are prohibited from moving further left as there is a solid yellow
                        edge line and a physical barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:stop_line', 'line:stop_yield', 'line:yield_line',
                        'no_turn:left', 'no_turn:right', 'symbol:bike', 'symbol:hov_diamond', 'symbol:other',
                        'text:bus', 'text:hov', 'text:keep_clear', 'text:only', 'text:other',
                        'text:speed_limit', 'text:stop'], missed []), actions True, unsafe [], citation
                        accepted, contradictions ['go_straight allowed without the stop that the STOP or 停
                        marking in my lane requires']
Tokens                  in 8634, out 1156, 10.07 s

bdd100k_val__bbf0f5d7-ea2f1cc3 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway on an elevated structure or bridge, with
                        buildings and a 'Discount Builders Supply' sign visible on the right. Ahead, there is
                        a white vehicle in the lane to the left. (lanes 2, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a concrete
                        barrier/railing beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my lane position (2) are consistent with the
                        boundaries: a yellow center line is on my left and a white edge line is on my right. |
                        roles: The yellow solid line correctly identifies a center line (separation of
                        opposite directions or special lanes), and the white solid line correctly identifies
                        the right edge. | markings: No markings were observed in my lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line on a two-way
                        roadway, but here it likely delineates a two-way left-turn lane or a divided flow.
                        [US-3B.01-05] "A single solid yellow line shall not be used as a center line marking
                        on a two-way roadway."
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        physical barrier
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the roadway. You may proceed straight ahead, but lane
                        changes to the left are prohibited by the solid yellow line, and a change to the right
                        is blocked by the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 699, 5.6 s

bdd100k_val__bbf48d08-b6a11dd8 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban or suburban road with an intersection ahead. My car is in a lane
                        moving forward. (lanes 2, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the right edge of the roadway, which is
                        adjacent to a curb and grass.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my position (2) are consistent with the boundaries: a
                        double yellow center line is on my left and a white edge line is on my right. | roles:
                        The double yellow line correctly identifies a center line (opposite traffic), and the
                        white line correctly identifies an edge line. | markings: No markings are present in
                        my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the left lane for
                        passing. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead. Lane changes to the
                        left are prohibited by the double solid yellow line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 770, 7.51 s

bdd100k_val__bbfe3b4f-5137ff9f | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane city street approaching a large intersection with a
                        subway entrance on the left. My car is positioned in a lane that leads directly into
                        the intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        turn lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the center
                        of my lane.; line:crosswalk (full): A white crosswalk is visible ahead of my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as lane 2 (middle) are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of the same direction. | markings: The straight arrow is consistent with a
                        through lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement for
                        this lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory
                        or permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (contested, label not_determined): prohibited by the solid white lane line
                        on the left.
Step 6  change_right    prohibited (contested, label not_determined): prohibited by the solid white lane line
                        on the right.
Step 6  go_straight     allowed (correct): allowed by the straight arrow marking.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight through the intersection. Lane
                        changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 708, 5.5 s

bdd100k_val__bc19c993-c0a0f85f | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane with a 'ONLY'
                        marking. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is next to a
                        curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:only (full): The word 'ONLY' is painted in white in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow line on the left and a white line on the right. | roles: The yellow line on the
                        left correctly indicates a lane of the same direction, and the white line on the right
                        correctly indicates the edge of the roadway. | markings: The 'ONLY' marking is
                        consistent with a dedicated lane, though the specific movement is not explicitly shown
                        by an arrow in the immediate foreground. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is
                        not discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            text:only: The 'ONLY' marking indicates the lane is designated for a single movement.
                        [US-3B.21-04] "Where through lanes approaching an intersection become mandatory turn
                        lanes, ONLY word pavement markings should be used in addition to signs and the
                        required la"
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid yellow line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for a specific movement (indicated by 'ONLY'). You may
                        proceed straight, but you are prohibited from changing lanes to the left or right due
                        to the solid boundary lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:only'], missed ['text:other']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 880, 7.98 s

bdd100k_val__bc9b5bfb-51ebcf39 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street at night with an intersection ahead. My car is in a lane that
                        appears to be part of a multi-lane roadway. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white stop line is visible across the lane ahead.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes of the
                        same direction. | markings: The stop line is consistent with an approaching
                        intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            line:stop_line: The stop line indicates the point behind which vehicles must stop.
                        [US-3B.19-01-02] "Stop lines may be used to indicate the point behind which vehicles
                        are required to stop in compliance with a STOP sign ... or some other traffic control
                        device "
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight but must come to a full stop at
                        the white stop line before entering the intersection. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 841, 6.84 s

bdd100k_val__bcbf328d-953430de | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with an intersection ahead. My car is in a lane that appears to
                        be a dedicated turn lane or a lane with specific turn restrictions. (lanes 3, mine 2,
                        full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from a sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in the lane.; text:only (full):
                        The word 'ONLY' is painted in white in the lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the double yellow
                        center line on my left and the white edge line on my right. | roles: The double yellow
                        line correctly identifies a center line for opposite traffic, and the white line/curb
                        correctly identifies the right edge. | markings: The left-turn arrow and 'ONLY' text
                        are consistent with a dedicated turn lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:left: The arrow indicates that the mandatory or permissible movement in this
                        lane is a left turn. [[US-3B.23-01]]
Step 5  Rule            text:only: The 'ONLY' marking indicates the lane is designated for the exclusive use
                        of the movement shown by the arrow. [[US-3B.21-04]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     prohibited (contested, label allowed): prohibited
Step 6  turn_left       allowed: allowed
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated left-turn-only lane. You must turn left at the upcoming
                        intersection and are prohibited from going straight or changing lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'text:only'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8634, out 948, 9.01 s

bdd100k_val__bd338426-4b27de63 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a McDonald's on the right. The road appears to be a divided
                        highway or a large multi-lane street with a median on the left. (lanes 4, mine 3,
                        full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway, which is
                        adjacent to a curb and a parking/driveway area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        a white dashed line on my left and a white solid line on my right. | roles: The white
                        dashed line correctly identifies a lane-to-lane separation, and the white solid line
                        correctly identifies the right edge of the roadway. | markings: No markings are
                        present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings govern this.
Step 6  turn_right      not_applicable: Not applicable as no markings govern this.
Step 6  u_turn          not_applicable: Not applicable as no markings govern this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the lane to your left. Do not attempt to move to the right as it
                        is the edge of the roadway. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['area:grid'], missed []), actions False, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8634, out 851, 7.98 s

bdd100k_val__bd354e59-e5a9e8c6 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban street with parked cars on the right and a sidewalk/curb on the
                        left. The road continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line separates my lane from a sidewalk and a curb on the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking lane with parked cars on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line separates my lane from the lane to
                        my right.; line:stop_yield (insufficient): There are no arrows, words, or symbols in
                        my lane.
Step 4  Cross-check     position: The lane count (2) and my position (1) are consistent with the left edge
                        line (yellow) and right edge line (white). | roles: The yellow line on the left and
                        white line on the right correctly identify the boundaries of the travel lane. |
                        markings: No markings were observed in the lane; the dashed line to the right is a
                        lane line, not a marking within my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost travel lane. You may proceed straight ahead. Lane changes to
                        the left or right are prohibited by the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight allowed without the stop that the
                        STOP or 停 marking in my lane requires']
Tokens                  in 8634, out 837, 7.85 s

bdd100k_val__bd3bd3ab-8e38f822 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway approaching an area with structures overhead,
                        possibly a transit station or a complex intersection. The road appears to be a one-way
                        street or a multi-lane roadway with a clear lane for my car. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which appears to be a
                        parking or loading area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane line on my left and the white edge line on my right. | roles: The white
                        solid line on the left correctly identifies a lane-to-lane separation, and the white
                        solid line on the right correctly identifies the roadway edge. | markings: No markings
                        are present, which is consistent with the lack of specific movement instructions. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead, but you are prohibited from
                        changing lanes to the left or right due to the solid white lines.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 839, 6.59 s

bdd100k_val__bd656105-ed6f8161 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           An urban intersection at sunset. My car is positioned at a stop line, facing a
                        crosswalk and an intersection with a green light. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line across the lane at the bottom of the photo.;
                        line:crosswalk (full): A white crosswalk is ahead of my lane.
Step 4  Cross-check     position: The lane count (2) and my position (2) are consistent with a white lane line
                        on my left and a white edge line/curb on my right. | roles: The white solid line on
                        the left correctly identifies a lane-line, and the white solid line/curb on the right
                        correctly identifies an edge-line. | markings: The stop line and crosswalk are
                        consistent with an intersection approach. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            line:stop_line: The stop line indicates the point behind which vehicles are required
                        to stop. [US-3B.19-01-02] "Stop lines may be used to indicate the point behind which
                        vehicles are required to stop in compliance with a STOP sign ... or some other traffic
                        control device "
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white lane line on the left.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb on
                        the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it and the light is
                        green.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight through the intersection. Lane changes to the left or right
                        are prohibited by the solid lines and the curb.
Score                   lane False, boundaries {'left': None, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 910, 9.88 s

bdd100k_val__bd65dd37-4c3cdf2d | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with an intersection or junction ahead. The road appears to be a
                        divided highway or a large urban thoroughfare with a concrete barrier on the right.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a concrete barrier on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on the left and a white line/curb on the right. | roles: The white solid
                        lines correctly delineate same-direction traffic and the right edge of the roadway. |
                        markings: No markings are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and the
                        concrete barrier on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid line markings and the physical barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 794, 7.29 s

bdd100k_val__bd8d420d-ec34c634 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with a bus stop and a white delivery truck ahead. The road
                        continues straight forward. (lanes 3, mine 3, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the boundaries: a
                        white line on the left indicates another lane of my direction, and a white line on the
                        right indicates the edge of the roadway. | roles: The white solid lines correctly
                        represent a lane line and an edge line for a right-hand traffic system. | markings:
                        The straight arrow is consistent with the lane's role as a through lane. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_right']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 8634, out 830, 8.33 s

bdd100k_val__bdc0dc52-b4d05890 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. The car is approaching a wide
                        intersection with multiple lanes of traffic. (lanes 4, mine 3, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the lane to my right, which is adjacent to a
                        curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.;
                        arrow:left (full): A white arrow pointing left is in the lane to my left.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        the white lane line on my left and the edge line on my right. | roles: The white solid
                        line on the left is a lane line, and the white solid line on the right is an edge
                        line, which is consistent with the roadway layout. | markings: The straight arrow in
                        my lane is consistent with the lane's role as a through lane. | unseen: none | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory
                        or permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line on
                        the left
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line on
                        the right
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow in my lane
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed ['line:stop_line']), actions False, unsafe
                        [], citation accepted, contradictions ['turn_left not_applicable although an arrow
                        shows it']
Tokens                  in 8634, out 730, 6.77 s

bdd100k_val__bdf6ab8b-3ebe8356 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway on a bridge or overpass. Ahead, there is a green overhead sign
                        and a slight curve or incline. (lanes 2, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a concrete barrier and
                        guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my position (2) are consistent with the boundaries: a
                        yellow line on my left indicates a lane to my left, and a white line on my right
                        indicates the edge of the roadway. | roles: The yellow line on the left and white line
                        on the right correctly fit the roles of a lane line and an edge line respectively. |
                        markings: No markings are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight, but lane changes to the left
                        are discouraged or prohibited by the solid yellow line. Stay within the lane marked by
                        the white edge line on your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 797, 12.46 s

bdd100k_val__be0a188d-c47bac51 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a bridge with a steel truss structure overhead. Ahead, the
                        road continues straight across the bridge. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a concrete barrier/curb delineate the right edge of the
                        roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        arrow:left (full): A white arrow pointing left is visible in the lane to my left.;
                        arrow:right (full): A white arrow pointing right is visible in the lane to my right.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white line on my left separates me from another lane, and a white line/curb on my
                        right marks the edge. | roles: The white solid lines correctly represent lane
                        separation and the right edge in a same-direction flow. | markings: The straight arrow
                        in my lane is consistent with the lane's role as a through lane. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory
                        or permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation accepted, contradictions ['turn_left
                        not_applicable although an arrow shows it', 'turn_right not_applicable although an
                        arrow shows it']
Tokens                  in 8634, out 926, 8.44 s

bdd100k_val__be22a1e1-cbcd82a6 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street at night, approaching an intersection with visible traffic
                        lights. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No markings visible in my lane.; line:yield_line
                        (insufficient): No markings visible in my lane.; arrow:straight (insufficient): No
                        markings visible in my lane.; arrow:left (insufficient): No markings visible in my
                        lane.; arrow:right (insufficient): No markings visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        a white dashed line on my left and a white solid line/curb on my right. | roles: The
                        white dashed line on the left correctly identifies a same-direction lane line, and the
                        white solid line on the right correctly identifies an edge line. | markings: No
                        markings were observed in my lane. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is discouraged but not prohibited.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:straight: no marking governs this action [null]
Step 6  change_left     allowed (correct): The white dashed line on the left discourages but does not prohibit
                        crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white line and curb on the right prohibit
                        moving onto the sidewalk.
Step 6  go_straight     allowed (contested, correct): No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change to the left lane if necessary. Do not move to the
                        right as it is bounded by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:right', 'arrow:straight', 'line:stop_line', 'line:yield_line'],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['go_straight
                        decided from an arrow that cannot be read']
Tokens                  in 8634, out 784, 7.56 s

bdd100k_val__be60191c-2dea5114 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban or suburban road with an intersection ahead. The traffic lights are
                        visible. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is the rightmost
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my left,
                        but my lane itself has no arrows or words.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white dashed line on the left and solid
                        white line on the right are consistent with lane-to-lane separation. | markings: No
                        markings were observed in my lane, which is consistent with a standard through lane. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The dashed white line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which is permissive
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white line, which
                        prohibits crossing [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in my lane govern this action.
Step 6  turn_right      not_applicable: No markings in my lane govern this action.
Step 6  u_turn          not_applicable: No markings in my lane govern this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is visible to the left.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you should not change into the right
                        lane. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 711, 7.63 s

bdd100k_val__be839b4c-fba3ea45 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. The traffic light is green.
                        (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is a turn lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        text:only (full): A white word 'ONLY' is visible in the lane to my right.;
                        line:crosswalk (full): A white crosswalk is ahead of my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white lane
                        lines on both sides. | roles: The white lines correctly delineate lanes of the same
                        direction. | markings: The straight arrow in my lane is consistent with the lane's
                        function. The 'ONLY' text in the adjacent lane correctly identifies it as a turn-only
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the dashed white line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: Crossing the solid white line is discouraged or prohibited.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     allowed (correct): Allowed by the dashed white line (US-3B.06-05-06).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white line
                        (US-3B.06-05-06).
Step 6  go_straight     allowed (contested, correct): Allowed by the straight arrow (US-3B.23-01).
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow or marking in my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or marking in my lane.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow or marking in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or change into the lane to your left. Do not attempt to
                        change into the lane to your right as it is a turn-only lane separated by a solid
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight', 'text:only'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8634, out 1004, 8.37 s

bdd100k_val__be926190-5293afb9 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban street with traffic moving forward. There is an intersection ahead
                        with traffic signals visible. (lanes 2, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, adjacent to a sidewalk and
                        parked cars.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my position (2) are consistent with the boundaries: a
                        center line is on my left and an edge line is on my right. | roles: The yellow double
                        solid line correctly identifies a center line, and the white solid line correctly
                        identifies a right edge line. | markings: No markings are present to contradict the
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the left lane for
                        passing. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-06]
Step 6  change_right    prohibited: prohibited by the solid white edge line [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-way street. You may proceed straight ahead,
                        but you are prohibited from changing lanes to the left or right due to the solid line
                        markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 818, 6.39 s

bdd100k_val__bfa92b30-f12f3535 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a slight uphill incline. There is an intersection or a
                        continuation of the road ahead. (lanes 2, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none; line:yield_line (insufficient): none;
                        line:stop_yield (insufficient): none; arrow:merge_left (insufficient): none;
                        arrow:merge_right (insufficient): none; arrow:two_way_left (insufficient): none;
                        text:only (insufficient): none; text:bus (insufficient): none; text:hov
                        (insufficient): none; text:stop (insufficient): none; text:keep_clear (insufficient):
                        none; text:speed_limit (insufficient): none; symbol:hov_diamond (insufficient): none;
                        symbol:bike (insufficient): none; symbol:other (insufficient): none;
                        area:left_turn_waiting (insufficient): none; area:two_way_left_turn_lane
                        (insufficient): none; area:grid (insufficient): none; area:channelizing
                        (insufficient): none; line:crosswalk (insufficient): none
Step 4  Cross-check     position: The lane count (2) and my lane position (2) agree with the boundaries: a
                        double yellow center line is on my left and a white edge line is on my right. | roles:
                        The double yellow center line and white edge line fit their respective roles. |
                        markings: No markings were observed in my lane. | unseen: No attributes were reported
                        that were not visible. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to my
                        left. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-06]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight ahead, but you are prohibited
                        from changing lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing', 'area:grid', 'area:left_turn_waiting',
                        'area:two_way_left_turn_lane', 'arrow:merge_left', 'arrow:merge_right',
                        'arrow:two_way_left', 'line:crosswalk', 'line:stop_line', 'line:stop_yield',
                        'line:yield_line', 'symbol:bike', 'symbol:hov_diamond', 'symbol:other', 'text:bus',
                        'text:hov', 'text:keep_clear', 'text:only', 'text:speed_limit', 'text:stop'], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['go_straight allowed
                        without the stop that the STOP or 停 marking in my lane requires']
Tokens                  in 8634, out 1074, 11.36 s

bdd100k_val__bfe2b817-505676ef | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban or suburban road with a center median area. The road ahead appears
                        to be a straight stretch with a potential intersection or turn-off further ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        center line on the left and an edge line on the right. | roles: The yellow double
                        solid line correctly identifies a center line, and the white solid line correctly
                        identifies an edge line. | markings: No markings are present in my lane. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the left lane for
                        passing. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left are prohibited by the double solid yellow line. The right
                        boundary is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 789, 7.93 s

bdd100k_val__bff4bb8b-152c6105 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway with an upcoming interchange or exit. My car is in a lane heading
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line is visible to the left, separated from my lane by a concrete
                        barrier and a metal guardrail.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A white dashed line is visible to the right, separating my lane from the lane to its
                        right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line on the left and a white lane line on the right. | roles: The yellow
                        solid line correctly identifies a center line (separation of opposite traffic), and
                        the white dashed line correctly identifies a lane line (same direction). | markings:
                        No markings are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line marking on a
                        two-way roadway, but here it serves as a center line separating opposite flows.
                        [US-3B.01-05] "A single solid yellow line shall not be used as a center line marking
                        on a two-way roadway."
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the right lane is
                        permitted. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    allowed (correct): allowed by the broken white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or move into the right lane. Changing to the left is
                        prohibited by the solid yellow center line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 804, 7.37 s

bdd100k_val__c02d18db-f5278de0 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an elevated structure (viaduct) on the left. The road
                        ahead appears to be a straight continuation with multiple lanes of traffic. (lanes 4,
                        mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        lane-to-lane separation for same-direction traffic. | markings: The straight arrow is
                        consistent with the lane's role as a through lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement in
                        this lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory
                        or permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 820, 7.43 s

bdd100k_val__c068a67b-03b6e200 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with parked cars on both sides. The road continues straight
                        ahead into a residential/commercial area. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A yellow line is visible on the left, but no arrows or
                        words are in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a center line on
                        the left and a lane line on the right. | roles: The yellow center line and white lane
                        line match the expected colors for opposite-direction and same-direction separation. |
                        markings: No markings are present in my lane to contradict the boundaries. | unseen:
                        No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is prohibited as a center line on a two-way
                        roadway, but here it likely delineates the separation of traffic flows. [US-3B.01-05]
                        "A single solid yellow line shall not be used as a center line marking on a two-way
                        roadway."
Step 5  Rule            right_boundary: A solid white line discourages or prohibits crossing into the adjacent
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight ahead. Lane changes to the left
                        or right are discouraged/prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8634, out 791, 6.39 s

bdd100k_val__c07733d0-7525eae7 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the left and a
                        shoulder/barrier on the right. An exit or interchange is visible ahead. (lanes 3, mine
                        2, full)
Step 2  Left            A solid yellow line separates my lane from a concrete barrier on the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible in the middle of my
                        lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow edge line on the left and a white lane line on the right. | roles: The yellow
                        solid line correctly identifies the left edge of the roadway, and the white dashed
                        line correctly identifies a lane divider. | markings: The dashed line in the lane is
                        not clearly a stop/yield line but appears to be a lane-related marking or just a gap
                        in the pavement; it does not contradict the boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the right lane is
                        permitted. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line
Step 6  change_right    allowed (correct): allowed by the broken white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may move into the right lane if needed, but you are
                        prohibited from moving left across the solid yellow line. You may proceed straight
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 8634, out 827, 6.8 s

bdd100k_val__c07733d0-aebb8786 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a grassy area and trees on the left and a fenced area on the
                        right. The road ahead appears to be a straight stretch with multiple lanes of traffic.
                        (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which ends in a white
                        solid line and a curb/barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 3rd from the left are consistent with
                        a white dashed line on my left and a white solid line on my right. | roles: The white
                        dashed line correctly identifies a lane-to-lane separation, and the white solid line
                        correctly identifies the right edge of the roadway. | markings: No markings are
                        present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings or arrows govern this.
Step 6  turn_right      not_applicable: Not applicable as no markings or arrows govern this.
Step 6  u_turn          not_applicable: Not applicable as no markings or arrows govern this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the lane to your left. Do not attempt to move
                        to the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 855, 7.93 s

bdd100k_val__c0e7271a-a3c8d55f | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with an intersection ahead. My car is in a lane moving forward.
                        (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a concrete curb separate my lane from the right edge of the
                        roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a white solid line/curb on the right. | roles: The white dashed
                        line correctly identifies a lane-to-lane separation, and the white solid line/curb
                        correctly identifies the right edge. | markings: No markings are present, which is
                        consistent with the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and curb
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings or arrows govern this movement.
Step 6  turn_right      not_applicable: Not applicable as no markings or arrows govern this movement.
Step 6  u_turn          not_applicable: Not applicable as no markings or arrows govern this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if necessary, but you are prohibited from moving to
                        the right of your current lane. You may proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 837, 6.97 s

bdd100k_val__c0efbe92-2ee3e529 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A city street with buildings on both sides. The road ahead is a multi-lane urban
                        street with a white car in the distance. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the curb/parking area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible in the middle of my
                        lane, possibly indicating a lane division or a specific area.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a solid white line on the right. | roles: The white dashed line
                        on the left correctly identifies a lane to the left, and the solid white line on the
                        right correctly identifies the edge of the roadway. | markings: The dashed line in the
                        middle of the lane is unclear and does not clearly define a movement. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed by the white dashed line on the left [US-3B.06-05-06]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white line and curb on
                        the right [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving to the
                        right. You are clear to proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions True, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 8634, out 840, 6.99 s

bdd100k_val__c100db13-71b423e5 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the right. There is an
                        overhead sign and a clear view of the road ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a concrete barrier on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a white solid line/barrier on the right. | roles: The white
                        dashed line correctly identifies a lane-to-lane separation, and the white solid line
                        correctly identifies the right edge of the roadway. | markings: No markings are
                        present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line and concrete
                        barrier [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings or geometry indicate a turn.
Step 6  turn_right      not_applicable: Not applicable as no markings or geometry indicate a turn.
Step 6  u_turn          not_applicable: Not applicable as no markings or geometry indicate a U-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the left lane. Do not attempt to move to the
                        right as it is bounded by a concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 839, 7.41 s

bdd100k_val__c107c2f1-b2b8fff0 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane divided highway with an overpass ahead. My car is traveling in one of the
                        lanes of the right-hand roadway. (lanes 3, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        concrete barrier.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        center line is on my left and a lane line is on my right. | roles: The double solid
                        yellow line correctly identifies a center line, and the solid white line correctly
                        identifies a lane line. | markings: No markings are present, which is consistent with
                        the absence of specific lane-use instructions. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the left lane for
                        passing. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left or right are
                        prohibited by the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 773, 7.15 s

bdd100k_val__c121b93f-b2ee73d4 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban road with an intersection ahead. My car is in a lane that appears
                        to be a right-turn lane or a lane ending at an intersection. (lanes 3, mine 3, full)
Step 2  Left            A white solid line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:merge_right (full): A white arrow pointing right is visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 3 (rightmost) are consistent with a
                        lane line on my left and an edge line on my right. | roles: The white solid line on
                        the left is a standard lane line, and the white solid line on the right is a standard
                        edge line. | markings: The right-turn arrow in my lane is consistent with the lane's
                        position as a right-turn lane. | unseen: none | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        my left. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:merge_right: The arrow indicates the mandatory or permissible movement for this
                        lane, which is a right turn. [US-3B.23-01] "Lane-use arrow markings are used to
                        indicate the mandatory or permissible movements in certain lanes and in two-way left-
                        turn lanes."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on my left
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb on
                        my right
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the right-turn arrow in my lane
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      allowed: allowed by the right-turn arrow in my lane
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated right-turn lane. You must turn right at the upcoming
                        intersection and are prohibited from changing lanes or proceeding straight.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight, turn_right decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 8634, out 722, 6.75 s

bdd100k_val__c1589305-200e315b | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is positioned in a lane
                        approaching a crosswalk and a stop line. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is occupied by a
                        taxi.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line across the lane at the intersection.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of traffic moving in the same direction. | markings: The stop line is consistent
                        with the intersection and crosswalk ahead. | unseen: None | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            line:stop_line: The stop line indicates the point behind which vehicles are required
                        to stop. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (contested, label not_determined): prohibited by the solid white
                        left_boundary line.
Step 6  change_right    prohibited (contested, label not_determined): prohibited by the solid white
                        right_boundary line.
Step 6  go_straight     stop_first (contested, label allowed): stop_first due to the stop_line marking.
Step 6  turn_left       stop_first: stop_first due to the stop_line marking.
Step 6  turn_right      stop_first: stop_first due to the stop_line marking.
Step 6  u_turn          stop_first: stop_first due to the stop_line marking.
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You must come to a complete stop at the white stop line before proceeding. Lane
                        changes to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk']), actions None, unsafe [], citation accepted, contradictions
                        ['turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 8634, out 870, 8.08 s

bdd100k_val__c15c29a5-74788f46 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings on the right and trees on the left. The road
                        ahead is straight. (lanes 3, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        double yellow line on the left indicates a center line (separating opposite traffic or
                        a special lane), and a white line on the right indicates an edge line. | roles: The
                        double yellow line on the left and white line on the right fit the roles of center
                        line and edge line respectively. | markings: No markings are present in my lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the lane to the
                        left. [[US-3B.01-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight in your current lane. Lane changes to the left and right are
                        prohibited by the solid line markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 779, 7.47 s

bdd100k_val__c1627cd8-d8c10968 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street at night with an intersection ahead. Traffic lights are
                        visible. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow and the word 'ONLY' are painted in my
                        lane.; text:only (full): The word 'ONLY' is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries
                        (yellow line on left, white line on right). | roles: The yellow line on the left and
                        white line on the right are consistent with standard lane delineations. | markings:
                        The left-turn arrow and 'ONLY' text are consistent with a mandatory turn lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line (or yellow in this context) discourages or
                        prohibits crossing. [US-3B.06-05-06] "Where crossing the lane line markings with care
                        is not discouraged or prohibited, the lane line markings shall consist of a normal
                        width broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing.
                        [US-3B.06-05-06] "Where crossing the lane line markings with care is not discouraged
                        or prohibited, the lane line markings shall consist of a normal width broken white
                        line. Wher"
Step 5  Rule            arrow:left: The arrow indicates that this is a mandatory turn lane. [US-3B.23-08]
                        "Where through lanes approaching an intersection become mandatory turn lanes, turn
                        lane-use arrow markings shall be used and shall be accompanied by standard sig"
Step 5  Rule            text:only: The 'ONLY' text reinforces that the lane is for the exclusive use of a
                        single movement (left turn). [US-3B.21-04] "Where through lanes approaching an
                        intersection become mandatory turn lanes, ONLY word pavement markings should be used
                        in addition to signs and the required la"
Step 6  change_left     prohibited (correct): prohibited by the solid yellow left boundary line.
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white right boundary
                        line.
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited by the left-turn arrow and 'ONLY'
                        marking.
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the left-turn arrow and 'ONLY' marking.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a mandatory left-turn lane. You must turn left at the upcoming intersection
                        and are prohibited from changing lanes or going straight.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:straight']), actions False, unsafe ['turn_left'],
                        citation accepted, contradictions []
Tokens                  in 8634, out 951, 8.93 s

bdd100k_val__c173438f-01b0b013 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway at night, approaching an intersection or a point where lanes may
                        merge or change. My car is in one of the rightmost lanes. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a shoulder or curb beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): No arrows, words, or symbols are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on my left and a solid white line on my right. | roles: The white dashed line
                        correctly identifies a lane-line, and the solid white line correctly identifies an
                        edge-line. | markings: No markings were observed in the lane. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn markings are present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn markings are present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn markings are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if necessary. Do not move to the right beyond the
                        solid white line. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings None (added None,
                        missed None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 846, 8.22 s

bdd100k_val__c1b3582d-b9c87c82 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane moving
                        forward. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a bicycle lane or sidewalk area on the
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol is painted on the pavement to the right of
                        my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a solid white line on the right. | roles: The white dashed line
                        correctly identifies a lane-line, and the solid white line correctly identifies an
                        edge-line. | markings: The bicycle symbol is outside my lane, which is consistent with
                        the right boundary. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the edge of the roadway, and crossing
                        it is prohibited. [US-3B.09-01-02] "If used, edge line pavement markings shall
                        delineate the right or left edges of a roadway. ... Right edge line pavement markings,
                        if used, shall consist of a no"
Step 5  Rule            symbol:bike: No specific rule provided for the bike symbol, but it indicates a bicycle
                        lane. [null]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn markings are present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn markings are present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn markings are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving into
                        the bicycle lane on your right. Proceed straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:bike'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8634, out 888, 7.55 s

bdd100k_val__c1b5a91c-9e402e78 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with an overpass ahead. The car is traveling in a lane that
                        appears to be part of a divided highway or a large multi-lane thoroughfare. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left, which is adjacent to a
                        concrete barrier.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): none
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. A yellow
                        line on my left indicates a center line separating opposite traffic or a left-hand
                        edge, and a white line on my right indicates a lane line. | roles: The yellow solid
                        line fits the role of a center line (separating opposite directions or a left-turn
                        lane), and the white dashed line fits the role of a lane line. | markings: No markings
                        are present in my lane to contradict the boundaries. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line is prohibited as a center line on a two-way
                        roadway, but [US-3A.03-03-04] allows it to separate traffic in opposite directions.
                        [[US-3B.01-05]]
Step 5  Rule            right_boundary: A broken white line indicates that crossing the lane line is
                        permitted. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the lane to your right as it is marked with a broken white line.
                        You are prohibited from changing into the lane to your left due to the solid yellow
                        center line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 834, 7.56 s

bdd100k_val__c2021c8c-474a8eda | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with vehicles in both directions and parked cars on the
                        right. The road ahead appears to be a straight continuation of the current street.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which has parked
                        vehicles.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly delineate
                        lanes of traffic moving in the same direction. | markings: No markings are present,
                        which is consistent with a standard through-lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it and it is a through
                        lane.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane roadway. You may proceed straight ahead,
                        but lane changes to the left or right are discouraged/prohibited by the solid white
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 797, 8.38 s

bdd100k_val__c264943c-5e493c9f | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane that appears
                        to be part of a turn bay or a specific lane configuration near a crosswalk. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): The word 'SCHOOL' is painted in large white letters across my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a yellow center
                        line on the left and a white lane line on the right. | roles: The yellow solid line
                        correctly identifies a center line (separation of opposite traffic or special lane),
                        and the white solid line correctly identifies a same-direction lane separation. |
                        markings: The 'SCHOOL' text is a general warning and does not contradict the
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is prohibited as a center line on a two-way
                        roadway, but it is used here to delineate the separation of traffic flows.
                        [US-3B.01-05] "A single solid yellow line shall not be used as a center line marking
                        on a two-way roadway."
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the lane
                        to the right. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            text:other: The 'SCHOOL' marking is used for warning or guidance. [US-3B.20-01] "Word,
                        symbol, and arrow markings on the pavement are used for the purpose of regulating,
                        warning, or guiding traffic. These pavement markings can be helpful to "
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your lane. Do not attempt to change lanes to the
                        left or right as the solid lines prohibit such maneuvers.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8634, out 858, 8.96 s

bdd100k_val__c28b60fb-a5e9b955 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a concrete barrier on the left and a hillside on the right.
                        Ahead, there is a commercial area with several buildings and a gas station. (lanes 3,
                        mine 2, full)
Step 2  Left            A solid yellow line separates my lane from a concrete barrier on the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my right,
                        but my lane itself has no markings.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with a
                        yellow edge line on the left and a white lane line on the right. | roles: The yellow
                        solid line correctly identifies the left edge of the roadway, and the white dashed
                        line correctly identifies a lane divider. | markings: No markings were found in my
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line (or yellow in this context) delineates the left-
                        hand edge of the roadway. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        is permitted. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may move into the right lane if needed, but you are
                        prohibited from moving left across the solid yellow edge line. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 799, 7.38 s

bdd100k_val__c2fb790e-4cd5a630 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A city street with multiple lanes of traffic moving forward. An intersection is
                        visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in my lane.;
                        text:other (full): The word 'ONLY' is painted in the lane to my left.
Step 4  Cross-check     position: The lane count of 3 and my position as 2nd from the left are consistent with
                        the white lane line on my left and the edge line on my right. | roles: The white solid
                        line on the left correctly identifies a lane-line, and the white solid line on the
                        right correctly identifies an edge-line. | markings: The straight arrow in my lane is
                        consistent with the lane's function. The 'ONLY' text is in the adjacent lane, not
                        mine. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory
                        or permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (contested, label allowed): prohibited
Step 6  go_straight     allowed (WRONG, label prohibited): allowed
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (contested, label allowed): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead. Lane changes to the left or
                        right are discouraged/prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'text:other'], missed ['arrow:left', 'text:only']), actions False,
                        unsafe ['go_straight'], citation accepted, contradictions []
Tokens                  in 8634, out 885, 7.36 s

bdd100k_val__c300fd4b-8ff92c2d | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban roadway under an elevated structure. Ahead,
                        there is a continuation of the roadway with several lanes of traffic. (lanes 2, mine
                        1, full)
Step 2  Left            A solid yellow line separates my lane from a sidewalk/curb area on the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A concrete barrier separates my lane from a lane of traffic moving in the same
                        direction.
                        none none, curb yes, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count and my lane position agree. The yellow line on the left is an
                        edge line, and the barrier on the right separates me from another lane. | roles: The
                        yellow solid line correctly identifies the left edge of the roadway, and the barrier
                        acts as a lane divider. | markings: No markings were observed in the lane. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line delineates the edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The barrier acts as a solid line that prohibits crossing into the
                        adjacent lane. [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Continue straight in your current lane. Lane changes to the left are prohibited by the
                        solid yellow edge line, and the concrete barrier to your right prevents a lane change
                        to the right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 777, 12.47 s

bdd100k_val__c3026ac7-8105e9a9 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with an overpass and an intersection ahead. My car is in a
                        lane with other vehicles moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right, which is bounded by a
                        concrete barrier.
                        white dashed, curb yes, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in my lane.; arrow:left (full):
                        A white left-turn arrow is painted in the lane to my right.; arrow:left (full): A
                        white left-turn arrow is painted in the lane to my left.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white dashed
                        lines on both sides. | roles: The white dashed lines correctly indicate lane
                        separation for traffic moving in the same direction. | markings: The left-turn arrows
                        in all three lanes are consistent with the lane boundaries and the upcoming
                        intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement from this
                        lane. [[US-3B.23-01]]
Step 6  change_left     allowed (correct): Allowed by the white dashed left boundary line [US-3B.06-05-06].
Step 6  change_right    allowed (correct): Allowed by the white dashed right boundary line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking prohibits it and the arrow
                        indicates a turn is possible, but straight is generally permitted unless an arrow
                        specifically excludes it.
Step 6  turn_left       allowed: Allowed by the left-turn arrow marking [US-3B.23-01].
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or marking.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow or marking.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You may turn left from your current lane as indicated by the pavement arrow. Lane
                        changes to the left or right are permitted as the lane markings are dashed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation accepted, contradictions
                        ['change_right allowed across a curb', 'go_straight allowed although no arrow shows
                        it']
Tokens                  in 8634, out 1008, 7.45 s

bdd100k_val__c308561a-1b698bb4 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a concrete barrier and sound wall on the right. There is a
                        vehicle directly ahead in my lane and others in adjacent lanes. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a shoulder or edge area, with a concrete
                        barrier and sound wall beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white lane line
                        on my left and a white edge line on my right. | roles: The white solid line on the
                        left correctly identifies a same-direction lane separation, and the white solid line
                        on the right correctly identifies the roadway edge. | markings: The straight arrow is
                        consistent with the lane's forward path. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line
                        [US-3B.06-05-06]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow [US-3B.23-01]
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane designated for straight-ahead travel. Lane changes to the left or
                        right are prohibited by the solid markings. Continue straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 899, 8.21 s

bdd100k_val__c31d9531-694298f0 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with a concrete barrier on the right. The road
                        continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane to the right, which is bounded by a
                        concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A white dashed line is visible in the lane to my
                        right.; line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on my left and a white solid line/barrier on my right. | roles: The white dashed
                        line on the left correctly identifies a lane-line, and the white solid line on the
                        right correctly identifies an edge-line. | markings: No markings were identified in my
                        lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     allowed (correct): The white dashed line on the left allows for a lane change.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white line and concrete barrier on the
                        right prohibit moving to the right.
Step 6  go_straight     allowed (contested, correct): No markings in my lane prohibit going straight.
Step 6  turn_left       not_applicable: No markings in my lane govern this action.
Step 6  turn_right      not_applicable: No markings in my lane govern this action.
Step 6  u_turn          not_applicable: No markings in my lane govern this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is visible.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving to the
                        right. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 683, 6.49 s

bdd100k_val__c3321660-e6b60390 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A city street at night with an intersection ahead. My car is in a lane approaching a
                        crosswalk and intersection. (lanes 2, mine 1, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a large vehicle (truck) on the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow pointing straight ahead is painted in the
                        center of my lane.; line:stop_line (full): A solid white line across the lane
                        indicates a stop line.
Step 4  Cross-check     position: The lane count and my position as the left lane are consistent with the
                        white lane lines on both sides. | roles: The white solid lines correctly delineate the
                        boundaries of my lane. | markings: The straight arrow and stop line are consistent
                        with a through lane approaching an intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 5  Rule            line:stop_line: The stop line indicates the point where the vehicle is required to
                        stop. [US-3B.19-01-02] "Stop lines may be used to indicate the point behind which
                        vehicles are required to stop in compliance with a STOP sign ... or some other traffic
                        control device "
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white left boundary
                        line
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white right boundary
                        line
Step 6  go_straight     stop_first (WRONG, label allowed): allowed by the straight arrow marking
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You must come to a full stop at the white stop line before
                        proceeding straight ahead. Lane changes to the left or right are prohibited by the
                        solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions ['leftmost lane, but
                        a lane line on the left']
Tokens                  in 8634, out 939, 8.06 s

bdd100k_val__c3bb4925-f78e285a | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with several vehicles ahead. The road appears to be a
                        divided highway or a large boulevard with a concrete barrier on the left. (lanes 3,
                        mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        white dashed line on the left and a white solid line/barrier on the right. | roles:
                        The white dashed line on the left correctly identifies a lane to the left, and the
                        white solid line/barrier on the right correctly identifies the edge of the roadway. |
                        markings: No markings were observed, which is consistent with the lack of specific
                        lane-use instructions. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the dashed white line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the dashed white lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02] and the physical barrier.
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn markings or arrows are present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn markings or arrows are present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn markings or arrows are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving to the
                        right due to the edge line and barrier. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 874, 8.64 s

bdd100k_val__c4057c0c-000a6aaf | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with an intersection ahead. My car is in a lane approaching a
                        stop line. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in my lane.; line:stop_line
                        (full): A white stop line is visible across the lane.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with the
                        white lane lines on both sides. | roles: White solid lines correctly delineate lanes
                        of the same direction. | markings: The left-turn arrow and stop line are consistent
                        with an approach to an intersection. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:left: The arrow indicates that a left turn is a permissible movement from this
                        lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 5  Rule            line:stop_line: The stop line indicates the point where the vehicle must stop.
                        [US-3B.19-01-02] "Stop lines may be used to indicate the point behind which vehicles
                        are required to stop in compliance with a STOP sign ... or some other traffic control
                        device "
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line
Step 6  go_straight     not_applicable (contested, label stop_first): not_applicable
Step 6  turn_left       allowed: allowed by the left-turn arrow marking
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated left-turn lane. You must come to a complete stop at the white
                        stop line before making your left turn. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'line:stop_line'], missed ['text:stop']), actions True, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 8634, out 939, 7.83 s

bdd100k_val__c47fb4ff-92db68d6 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway passing under a bridge. The road appears to be a divided highway
                        or a large multi-lane thoroughfare with a concrete wall on the right. (lanes 3, mine
                        3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a paved shoulder area, which is bounded by a
                        concrete wall and a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A white line perpendicular to the lane direction marks the end
                        of the travel lane and the start of the shoulder area.
Step 4  Cross-check     position: The lane count of 3 and my position as the rightmost lane (3) are consistent
                        with a white dashed line on the left and a white solid line/curb on the right. |
                        roles: The white dashed line correctly identifies a lane-to-lane separation, and the
                        white solid line correctly identifies the right edge of the roadway. | markings: The
                        perpendicular line marks the transition to the shoulder, which is consistent with the
                        right edge line. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            line:stop_line: The line indicates the point behind which vehicles are required to
                        stop (in this context, it marks the end of the travel lane). [US-3B.19-01-02] "Stop
                        lines may be used to indicate the point behind which vehicles are required to stop in
                        compliance with a STOP sign ... or some other traffic control device "
Step 6  change_left     allowed (correct): allowed by the white dashed line (US-3B.06-05-06)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb
                        (US-3B.09-01-02)
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may change into the lane to your left. Do not move onto the shoulder to your
                        right, as it is bounded by a solid line and a curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 929, 7.1 s

bdd100k_val__c4b3ab99-a4a09eeb | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway under an overpass, approaching an intersection or a point of lane
                        convergence. My car is in a lane on the right side of the road. (lanes 3, mine 3,
                        full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right-hand edge of the roadway, which is
                        adjacent to a wall and a shoulder.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:channelizing (full): White diagonal lines (cross-hatching) are visible to the
                        left of my lane, indicating a neutral area or buffer.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white color and
                        solid pattern are consistent with lane lines and edge lines in a same-direction flow.
                        | markings: The channelizing area to the left is consistent with the lane
                        configuration. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the lane to
                        the left. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            area:channelizing: The channelizing lines form a neutral area where traffic is not
                        permitted to enter. [[US-3B.08-01-03]]
Step 6  change_left     prohibited (contested, label allowed): prohibited
Step 6  change_right    not_applicable (contested, label prohibited): not_applicable
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight in your current lane. Lane changes to the left are prohibited
                        by the solid white line.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 858, 8.11 s

bdd100k_val__c4b3ce3d-cdc056ce | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway with an overhead gantry and green directional signs. The road
                        continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a shoulder or barrier area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on the left and a solid white line on the right. | roles: The white dashed line
                        correctly identifies a lane-to-lane separation, and the solid white line correctly
                        identifies the right edge. | markings: No markings are present, which is consistent
                        with the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings govern this.
Step 6  turn_right      not_applicable: Not applicable as no markings govern this.
Step 6  u_turn          not_applicable: Not applicable as no markings govern this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change to the left lane if needed, but you are prohibited from moving to the
                        right beyond the solid white line. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 819, 7.47 s

bdd100k_val__c4e97226-7be7eef5 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a high brick wall on the right and a concrete barrier
                        on the left. An overpass is visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A dashed white line separates my lane from the lane to my right, which is adjacent to
                        a curb and a brick wall.
                        white dashed, curb yes, lane_line, evidence full
Step 3  Markings        line:stop_line (insufficient): A dashed white line is visible to the right of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white lines correctly delineate lanes of the same
                        direction. | markings: No specific arrows or words are in my lane; the dashed line to
                        the right is a lane line, not a marking in my lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The dashed white line indicates a permissive condition for crossing
                        into the right lane. [US-3B.06-05-06] "Where crossing the lane line markings with care
                        is not discouraged or prohibited, the lane line markings shall consist of a normal
                        width broken white line. Wher"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white line on the left.
Step 6  change_right    allowed (correct): allowed by the dashed white line on the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or move into the right lane. Changing into the left lane is
                        prohibited by the solid white line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['change_right allowed across a curb']
Tokens                  in 8634, out 793, 7.5 s

bdd100k_val__c4ee0cc4-b7af9602 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway at night with an intersection or junction ahead. My car is in a
                        lane moving forward. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible on the right side of my
                        lane, possibly indicating a lane drop or a transition.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) are consistent with having
                        a lane line on both the left and right. | roles: The white solid lines correctly
                        identify lane-to-lane separation in the same direction of travel. | markings: The
                        dashed line on the right is unclear and does not contradict the primary solid
                        boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line
                        [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You should continue straight in your current lane. Lane changes to the left or right
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions False, unsafe [], citation accepted, contradictions
                        ['go_straight allowed without the stop that the STOP or 停 marking in my lane
                        requires']
Tokens                  in 8634, out 816, 7.51 s

bdd100k_val__c5588233-b03622f3 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with a concrete barrier on the left and a wooded area on the
                        right. Ahead, there is a slight curve or merge area with several vehicles in the
                        distance. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from a concrete barrier on the left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to my right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow edge line on the left and a white lane line on the right. | roles: The yellow
                        solid line correctly identifies the left edge of the roadway, and the white dashed
                        line correctly identifies a lane divider. | markings: No markings are present to
                        contradict the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line (or yellow in this context) delineates the left-
                        hand edge of the roadway. [US-3B.09-01-02] "If used, edge line pavement markings shall
                        delineate the right or left edges of a roadway. ... Right edge line pavement markings,
                        if used, shall consist of a no"
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        is permitted. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    allowed (correct): allowed
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the lane to your right. Changing into the
                        lane to your left is prohibited by the solid yellow edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 781, 7.59 s

bdd100k_val__c561cb9a-aafc0bad | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway approaching an intersection. My car is in a lane
                        with a straight-ahead arrow and a right-hand edge line. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        line on my left and the white edge line on my right. | roles: The white solid line on
                        the left correctly identifies a same-direction lane separation, and the white solid
                        line on the right correctly identifies the edge of the roadway. | markings: The
                        straight arrow in my lane is consistent with the lane's role as a through lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-ahead movement.
                        [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (contested, correct): prohibited
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead but are prohibited from
                        changing lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:only']), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 845, 7.53 s

bdd100k_val__c65c2462-96e8ae92 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane roadway under an overpass. Ahead, there is a
                        clear path forward with other vehicles in adjacent lanes. (lanes 3, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a concrete barrier/wall form the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the boundaries: a
                        white dashed line is on my left and a white solid line/curb is on my right. | roles:
                        The white dashed line correctly identifies a same-direction lane line, and the white
                        solid line/curb correctly identifies the right edge. | markings: No markings are
                        present, which is consistent with the clear path ahead. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line and concrete
                        barrier [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow or area.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or area.
Step 6  u_turn          not_applicable: Not applicable as there is no u-turn arrow or area.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the left lane. Do not attempt to move to the
                        right as it is the edge of the roadway bounded by a barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 872, 8.43 s

bdd100k_val__c66d2237-f9c0a1ef | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with parked cars on both sides. An intersection or signalized
                        area is ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from a two-way left-turn lane to my left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from a parking lane on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.;
                        area:two_way_left_turn_lane (full): A two-way left-turn lane is visible to the left of
                        my lane, marked with yellow lines.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is to my left and a white edge line is to my right. | roles: The
                        yellow solid line correctly identifies a center line (separation from a two-way left-
                        turn lane), and the white solid line correctly identifies an edge line. | markings:
                        The straight arrow in my lane is consistent with the lane's role as a through lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is prohibited as a center line on a two-way
                        roadway, but [US-3A.03-03-04] allows it to separate a two-way left-turn lane from
                        other lanes. [[US-3B.01-05]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement in
                        this lane. [[US-3B.23-01]]
Step 5  Rule            area:two_way_left_turn_lane: The area to the left is a two-way left-turn lane, which
                        can be entered from my lane for a left turn. [[US-3B.05-01]]
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       allowed: allowed
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areaallowed: allowed
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead or enter the two-way left-turn lane to your left to
                        prepare for a left turn. Lane changes to the left or right are prohibited by the solid
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane', 'arrow:straight'], missed []), actions False, unsafe
                        [], citation in_pack_not_accepted, contradictions ['turn_left allowed although no
                        arrow shows it']
Tokens                  in 8634, out 1015, 9.6 s

bdd100k_val__c68f8fd2-61681484 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an overhead sign indicating exits. The road
                        ahead appears to be a continuation of the current roadway with multiple lanes. (lanes
                        4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is bounded by a
                        concrete barrier/curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the boundaries: a
                        white dashed line is on my left and a white solid line/curb is on my right. | roles:
                        The white dashed line correctly identifies a lane to the left, and the white solid
                        line/curb correctly identifies the right edge of the roadway. | markings: No markings
                        are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02] and the presence of a curb.
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings or boundaries indicate a turn.
Step 6  turn_right      not_applicable: Not applicable as no markings or boundaries indicate a turn.
Step 6  u_turn          not_applicable: Not applicable as no markings or boundaries indicate a u-turn.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  You may continue straight or change into the lane to your left. Do not attempt to move
                        to the right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 861, 7.35 s

bdd100k_val__c6d77a40-03423c96 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings and trees on both sides. An intersection is
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            A white broken line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a curb separate my lane from the sidewalk and a parked van.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white line across the lane ahead of the van.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a lane line on my
                        left and an edge line/curb on my right. | roles: The white dashed line on the left and
                        white solid line/curb on the right fit the roles of a lane line and edge line
                        respectively. | markings: The stop line is positioned at the intersection ahead,
                        consistent with the boundaries. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The broken white line indicates that crossing into the left lane is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            line:stop_line: The stop line indicates the point behind which vehicles are required
                        to stop. [[US-3B.19-01-02]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line and curb
                        [US-3B.09-01-02].
Step 6  go_straight     stop_first (contested, label allowed): Allowed as there is no arrow prohibiting it,
                        but must stop first due to the stop line.
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow or marking.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or marking.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow or marking.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is marked.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed. You must come to a complete stop at the
                        white stop line before proceeding straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 927, 7.73 s

bdd100k_val__c6dca574-6e641016 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban street with trees lining both sides. The road ahead appears to be a
                        continuous street with parked cars on the left and a sidewalk on the right. (lanes 2,
                        mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the sidewalk/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my position (2) are consistent with a center line on
                        the left and an edge line on the right. | roles: The yellow double solid line
                        correctly identifies a center line, and the white solid line correctly identifies an
                        edge line. | markings: No markings were observed, which is consistent with the lack of
                        specific lane-use instructions. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the adjacent lane
                        for traffic in the opposite direction. [US-3B.01-06] "Except where a reversible lane
                        or a two-way left-turn lane is present, the center line markings on undivided two-way
                        roadways with four or more lanes for moving"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        curb
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-way street. You may proceed straight ahead,
                        but you are prohibited from changing lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 806, 7.41 s

bdd100k_val__c6dcc1a9-0fa80e62 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane bridge or elevated roadway with an overhead sign. The
                        road ahead is a multi-lane highway with several lanes of traffic moving in the same
                        direction. (lanes 4, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a concrete barrier/curb
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (4) and my position (3) are consistent with the white dashed
                        line on my left and the white solid line on my right. | roles: The white dashed line
                        correctly identifies a lane-line (same direction), and the white solid line correctly
                        identifies an edge-line. | markings: No markings are present in my lane. | unseen:
                        None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the white dashed lane line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings govern this.
Step 6  turn_right      not_applicable: Not applicable as no markings govern this.
Step 6  u_turn          not_applicable: Not applicable as no markings govern this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the lane to your left. You are prohibited from moving to the right
                        as it is the edge of the roadway. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe ['change_left'], citation
                        accepted, contradictions []
Tokens                  in 8634, out 838, 12.64 s

bdd100k_val__c6e1c974-906461f4 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with buildings and trees on both sides. An intersection is
                        visible in the distance. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is in the center of my
                        lane.; text:only (full): The word 'ONLY' is painted in white in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the white lane
                        lines on both sides. | roles: The white solid lines correctly delineate lanes of the
                        same direction. | markings: The straight arrow and 'ONLY' text are consistent with a
                        dedicated through lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for straight-through movement.
                        [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 5  Rule            text:only: The 'ONLY' marking indicates the lane is for the exclusive use of the
                        movement shown by the arrow. [US-3B.21-04] "Where through lanes approaching an
                        intersection become mandatory turn lanes, ONLY word pavement markings should be used
                        in addition to signs and the required la"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       prohibited (correct): prohibited
Step 6  turn_right      prohibited (correct): prohibited
Step 6  u_turn          prohibited (correct): prohibited
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a dedicated through lane. You should proceed straight ahead and are
                        prohibited from changing lanes or making turns from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 897, 7.39 s

bdd100k_val__c6ed8102-2bbcbcc2 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway under an overpass. The road continues straight
                        ahead. (lanes 3, mine 3, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a metal guardrail form the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:hov_diamond (full): A small white diamond-shaped symbol is visible in the
                        middle of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with a white dashed
                        line on my left and a white solid line/guardrail on my right. | roles: The white
                        dashed line correctly identifies a lane-line, and the white solid line/guardrail
                        correctly identifies an edge-line. | markings: The HOV diamond is centered in the
                        lane, consistent with its role as a preferential lane marking. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            symbol:hov_diamond: This indicates a preferential lane for high-occupancy vehicles.
                        [[US-3E.03-02]]
Step 6  change_left     allowed (correct): allowed
Step 6  change_right    prohibited (contested, correct): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a preferential HOV lane. You may move to the left into the adjacent lane,
                        but you are prohibited from moving to the right as it is the edge of the roadway.
                        Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:hov_diamond'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 840, 7.61 s

bdd100k_val__c85416bd-db975d94 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with an intersection or junction ahead. The car is in a lane on
                        the right side of the road. (lanes 3, mine 3, full)
Step 2  Left            A white solid line separates my lane from the lane to its left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb and grass beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the boundaries: a
                        white line on my left and a white edge line on my right. | roles: The white solid line
                        on the left is a lane line, and the white solid line on the right is an edge line,
                        which is consistent with US rules. | markings: No markings are present in my lane. |
                        unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line on the
                        left.
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and curb on
                        the right.
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You may proceed straight ahead in your current lane. Lane changes to the left or right
                        are prohibited by the solid line markings.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 797, 6.17 s

bdd100k_val__c8a7a62d-e58e7297 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A city street with multiple lanes of traffic moving forward. There is a crosswalk and
                        an intersection ahead. (lanes 3, mine 3, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left.
                        yellow solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a sidewalk/curb form the right edge of the roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:left (full): A white left-turn arrow is painted in my lane.; text:only (full):
                        The word 'ONLY' is painted in my lane next to the arrow.; line:stop_line (full): A
                        white stop line is visible ahead of my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the boundaries: a
                        yellow line on my left and a white line/curb on my right. | roles: The yellow line on
                        the left correctly identifies a lane separation, and the white line/curb on the right
                        correctly identifies the edge. | markings: The left-turn arrow and 'ONLY' text are
                        consistent with a mandatory turn lane, and the stop line is consistent with an
                        intersection approach. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The solid white/yellow line discourages or prohibits crossing into the
                        adjacent lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is
                        not discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:left: The arrow indicates that this is a mandatory turn lane. [US-3B.23-08]
                        "Where through lanes approaching an intersection become mandatory turn lanes, turn
                        lane-use arrow markings shall be used and shall be accompanied by standard sig"
Step 5  Rule            text:only: The 'ONLY' marking reinforces that the lane is for the exclusive use of a
                        single movement (left turn). [US-3B.21-04] "Where through lanes approaching an
                        intersection become mandatory turn lanes, ONLY word pavement markings should be used
                        in addition to signs and the required la"
Step 5  Rule            line:stop_line: The stop line indicates the point behind which vehicles must stop.
                        [US-3B.19-01-02] "Stop lines may be used to indicate the point behind which vehicles
                        are required to stop in compliance with a STOP sign ... or some other traffic control
                        device "
Step 6  change_left     prohibited (correct): prohibited by the solid yellow line (US-3B.06-05-06)
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        curb (US-3B.09-01-02)
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the mandatory left-turn arrow and
                        'ONLY' marking (US-3B.23-08, US-3B.21-04)
Step 6  turn_left       allowed: allowed by the left-turn arrow (US-3B.23-08)
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a mandatory left-turn lane. You must turn left at the upcoming intersection
                        and are prohibited from going straight or changing lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:left', 'line:stop_line', 'text:only'], missed ['text:other']), actions False,
                        unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 1141, 8.43 s

bdd100k_val__c8e01103-9ff8595d | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A city street with an intersection ahead. The road is wet, and there is a crosswalk
                        visible. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        line:crosswalk (full): A white crosswalk is ahead of my lane.
Step 4  Cross-check     position: The lane count (2) and my position (2) are consistent with the boundaries
                        (lane line on left, edge line on right). | roles: The white solid lines correctly
                        represent a lane line and a right edge line. | markings: The straight arrow is
                        consistent with the lane's role as a through lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement.
                        [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (contested, label not_determined): prohibited
Step 6  change_right    prohibited (contested, label not_determined): prohibited
Step 6  go_straight     allowed (correct): allowed
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead but are prohibited from
                        changing lanes to the left or right due to the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8634, out 851, 7.36 s

bdd100k_val__c909551e-fb24caeb | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane city street with tall buildings and trees on both sides. An intersection
                        is visible ahead. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count of 4 and my position as 2nd from the left are consistent with
                        the white lane lines on both sides. | roles: The white solid lines correctly identify
                        the boundaries between lanes of the same direction. | markings: The straight arrow is
                        consistent with the lane's role as a through lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permissible movement for
                        this lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory
                        or permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white left boundary line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white right boundary line
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead. Lane changes
                        to the left or right are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 826, 7.07 s

bdd100k_val__c90b5398-8d49f2f2 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban roadway with a large building and a truck ahead. The road appears
                        to be a one-way street or a multi-lane roadway with a turn lane or bike lane on the
                        left. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a lane or area to the right, with a curb and
                        a sidewalk beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_yield (insufficient): A white dashed line is visible in the middle of my
                        lane, possibly indicating a lane drop or a transition.
Step 4  Cross-check     position: The lane count of 3 and my position as 2 (middle) is consistent with a white
                        dashed line on the left and a solid white line on the right. | roles: The white dashed
                        line on the left correctly identifies a same-direction lane line, and the solid white
                        line on the right correctly identifies an edge line. | markings: The dashed line in
                        the lane is not clearly a stop/yield line but rather a lane-use indicator or
                        transition; however, no specific arrow or word is visible. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [US-3B.06-05-06] "Where
                        crossing the lane line markings with care is not discouraged or prohibited, the lane
                        line markings shall consist of a normal width broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     allowed (contested, label prohibited): Allowed by the white dashed lane line on the
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and the
                        presence of a curb.
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn arrow or area is visible.
Step 6  turn_right      not_applicable: Not applicable as no right-turn arrow or area is visible.
Step 6  u_turn          not_applicable: Not applicable as no U-turn arrow or area is visible.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is visible.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed. Do not attempt to move to the right as it
                        is the edge of the roadway. Proceed straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_yield'], missed []), actions False, unsafe [], citation accepted,
                        contradictions ['go_straight allowed without the stop that the STOP or 停 marking in my
                        lane requires']
Tokens                  in 8634, out 888, 5.96 s

bdd100k_val__c90c8198-f73aed79 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings on both sides. The road ahead appears to be a
                        straight continuation of the current street. (lanes 2, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the lane to my left.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (2) and my lane position (2) agree with the boundaries: a
                        double yellow center line is on my left, and a white edge line is on my right. |
                        roles: The yellow double solid line correctly identifies a center line, and the white
                        solid line correctly identifies a right edge line. | markings: No markings are present
                        in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: The double solid yellow line prohibits crossing into the left lane for
                        passing. [US-3B.01-06] "Except where a reversible lane or a two-way left-turn lane is
                        present, the center line markings on undivided two-way roadways with four or more
                        lanes for moving"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line
Step 6  change_right    not_applicable: not_applicable
Step 6  go_straight     allowed (contested, correct): allowed as no markings prohibit it
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-way street. You may proceed straight ahead,
                        but you are prohibited from changing into the left lane due to the double solid yellow
                        center line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 789, 7.79 s

bdd100k_val__c9283177-4ac407c3 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane urban street with buildings on the right and a barrier/trees on the left.
                        The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to my left, which is bounded by a
                        curb/barrier.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to my right, which is adjacent to a
                        sidewalk.
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with the boundaries: a
                        yellow center line is to my left and a white lane line is to my right. | roles: The
                        yellow solid line correctly identifies a center line (separation of opposite flows or
                        special lanes), and the white solid line correctly identifies a lane line. | markings:
                        The straight arrow is consistent with the lane's forward path. | unseen: None. |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line is not used as a center line marking on a
                        two-way roadway, but here it delineates the separation of traffic flows. [US-3B.01-05]
                        "A single solid yellow line shall not be used as a center line marking on a two-way
                        roadway."
Step 5  Rule            right_boundary: The solid white line discourages or prohibits crossing into the right
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement.
                        [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory or
                        permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (correct): prohibited
Step 6  change_right    prohibited (WRONG, label allowed): prohibited
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may proceed straight ahead as indicated by the pavement
                        arrow. Lane changes to the left or right are discouraged/prohibited by the solid
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 865, 7.14 s

bdd100k_val__c94d8213-1f593522 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           The photo shows a multi-lane roadway approaching an intersection or a point of lane
                        configuration change. There are several lanes of traffic moving in the same direction.
                        (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the lane to my left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line and a concrete barrier form the right edge of my lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.;
                        arrow:left (full): A white arrow pointing left is painted in the lane to my left.
Step 4  Cross-check     position: The lane count and my lane position are consistent with the boundaries (lane
                        line on left, edge line on right). | roles: The white solid lines correctly represent
                        a lane line and an edge line for same-direction traffic. | markings: The straight
                        arrow in my lane is consistent with the lane's role as a through lane. | unseen: None.
                        | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages or prohibits crossing into the left
                        lane. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            arrow:straight: The arrow indicates that going straight is a permitted movement for
                        this lane. [US-3B.23-01] "Lane-use arrow markings are used to indicate the mandatory
                        or permissible movements in certain lanes and in two-way left-turn lanes."
Step 6  change_left     prohibited (contested, label not_determined): prohibited by the solid white lane line
                        (US-3B.06-05-06)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and concrete
                        barrier
Step 6  go_straight     allowed (contested, correct): allowed by the straight arrow marking (US-3B.23-01)
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a through lane. You are permitted to proceed straight ahead. Lane changes
                        to the left are prohibited by the solid white line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:left', 'arrow:straight'], missed []), actions None, unsafe [], citation
                        accepted, contradictions ['turn_left not_applicable although an arrow shows it']
Tokens                  in 8634, out 911, 7.68 s

bdd100k_val__c9b099e4-6ab2e4f4 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane highway or expressway with an exit or interchange ahead. The road is wet,
                        and there are overhead signs and a concrete barrier on the right. (lanes 3, mine 3,
                        full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a concrete barrier/curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (3) are consistent with the boundaries: a
                        white dashed line is on my left and a white solid line/curb is on my right. | roles:
                        The white dashed line on the left correctly identifies a lane to the left, and the
                        white solid line on the right correctly identifies the edge of the roadway. |
                        markings: No markings are present in my lane. | unseen: None. | result: consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line and the
                        presence of a curb [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no left-turn markings or arrows are present.
Step 6  turn_right      not_applicable: Not applicable as no right-turn markings or arrows are present.
Step 6  u_turn          not_applicable: Not applicable as no U-turn markings or arrows are present.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving to the
                        right due to the edge line and barrier. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 864, 7.79 s

bdd100k_val__ca146661-7f70d0c4 | lane | Test B | gemma4:12b
-----------------------------------------------------------
Step 1  Scene           A multi-lane roadway with an intersection or merge point ahead. My car is in a lane
                        moving forward. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to my left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a dirt/grass shoulder
                        beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): No markings are visible in my lane.
Step 4  Cross-check     position: The lane count (3) and my position (2) are consistent with a white dashed
                        line on my left and a white solid line on my right. | roles: The white dashed line
                        correctly identifies a lane-line, and the white solid line correctly identifies an
                        edge-line. | markings: No markings are present in my lane. | unseen: None. | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the white dashed line is permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings prohibit it.
Step 6  turn_left       not_applicable: Not applicable as no markings govern this movement.
Step 6  turn_right      not_applicable: Not applicable as no markings govern this movement.
Step 6  u_turn          not_applicable: Not applicable as no markings govern this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change into the left lane if needed, but you are prohibited from moving onto
                        the shoulder to the right. Proceed straight ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8634, out 819, 7.18 s
```
