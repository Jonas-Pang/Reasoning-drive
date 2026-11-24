# Reasoning of lane run 20261118_001517_laneA_US

```text
bdd100k_val__b2afce7f-0cb9967a | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane highway with traffic moving in the same direction, bordered by a concrete
                        barrier on the left and a guardrail on the right. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white dash and gap immediately in front of the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right edge of the roadway, with a metal
                        guardrail running parallel to it. Photo 2 shows the white solid line and the guardrail
                        next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line and guardrail prohibit leaving the roadway to
                        the right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the white solid edge line and guardrail
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts continuing straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but you cannot exit the road to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 742, 20.99 s

bdd100k_val__b459e707-2d208c56 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane road in the United States with traffic keeping right; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with clear dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right edge of the roadway. Photo 2 shows a
                        solid yellow line next to my car.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows crossing for lane changes.
Step 5  Rule            right_boundary: A solid yellow edge line prohibits crossing into the shoulder or off-
                        road area.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (correct): prohibited by the solid yellow edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts continuing straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the yellow line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 718, 3.2 s

bdd100k_val__b5046f1e-b1ef44b9 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           Urban road in the United States with buildings on both sides; my car is in a single
                        lane heading towards an intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a shoulder or bike lane.
                        Photo 2 shows the same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane to the right.
                        Photo 2 shows a series of short white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows the letters 'N L' (part of 'ONLY') painted in the
                        lane, and Photo 1 shows the full word 'ONLY' further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits leaving the roadway to the left.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 5  Rule            text:only: The word ONLY indicates that the lane is restricted to a specific movement,
                        but the accompanying arrow is needed to determine which one.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid edge line, which
                        prohibits leaving the roadway.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a broken lane line, which
                        allows lane changes.
Step 6  go_straight     allowed (contested, correct): No arrow governs this action, and the lane does not end,
                        so it is allowed.
Step 6  turn_left       not_applicable: No arrow governs this action, so it is not applicable.
Step 6  turn_right      not_applicable: No arrow governs this action, so it is not applicable.
Step 6  u_turn          not_applicable: No arrow governs this action, so it is not applicable.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a lane that allows going straight or changing to the right. The 'ONLY'
                        marking is present, but without a visible arrow, proceed with caution and follow the
                        traffic flow.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 3812, out 878, 31.01 s

bdd100k_val__b6decb24-82234e11 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           Urban road in the United States with multiple lanes of traffic heading straight toward
                        an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car and continuing ahead. Photo 2 shows a
                        series of white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car and continuing ahead. Photo 2 shows a
                        series of white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white arrow pointing straight ahead
                        with the word 'ONLY' below it in my lane.; text:only (full): Photo 1 and Photo 2 show
                        the word 'ONLY' below the straight arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: the white
                        dashed patterns on both sides are consistent with lane lines separating traffic in the
                        same direction. | markings: the straight arrow and 'ONLY' text are consistent with a
                        lane dedicated to going straight. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows crossing to change lanes.
Step 5  Rule            right_boundary: A broken white lane line allows crossing to change lanes.
Step 5  Rule            arrow:straight: A straight arrow allows going straight and prohibits turns.
Step 5  Rule            text:only: The 'ONLY' text reinforces that only the movement indicated by the arrow is
                        permitted.
Step 6  change_left     allowed (correct): allowed by the broken white lane line on the left.
Step 6  change_right    allowed (correct): allowed by the broken white lane line on the right.
Step 6  go_straight     allowed (correct): allowed by the straight arrow in the lane.
Step 6  turn_left       prohibited (correct): prohibited by the straight arrow and 'ONLY' text.
Step 6  turn_right      prohibited (correct): prohibited by the straight arrow and 'ONLY' text.
Step 6  u_turn          prohibited (correct): prohibited by the straight arrow and 'ONLY' text.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  My lane is a straight-only lane. I can go straight or change lanes, but I cannot turn
                        left or right from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:only'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 968, 3.23 s

bdd100k_val__b7719f1d-e6e580dd | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane highway in the United States with traffic moving forward; no intersection
                        or ramp is immediately ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white dash and gap immediately to the left of my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, with a concrete barrier further right.
                        Photo 2 shows a white solid line next to my car and a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane position
                        agree with the boundaries; a lane line on the left and an edge line on the right
                        indicate the rightmost lane. | roles: the white dashed line is a standard lane line
                        and the white solid line is a standard edge line. | markings: no markings in my lane,
                        which is consistent with a highway lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows lane changes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the shoulder or
                        barrier area.
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed lane line.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid edge line
                        and there is a concrete barrier.
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
Advice                  You are in the rightmost lane of the highway. You may continue straight or change
                        lanes to the left, but do not cross the solid line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 825, 5.37 s

bdd100k_val__b775af1c-bb5afbe3 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection. There is a vehicle ahead in the
                        same lane. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which becomes a curb at the
                        intersection. Photo 2 shows a white solid line next to my car and a raised curb
                        further ahead on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2 shows a white right-turn arrow painted in my lane.;
                        line:stop_line (full): Photo 1 shows a white stop line across the lane at the
                        intersection.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a lane line on the left and an edge line/curb on the right
                        indicate the rightmost lane. | roles: the white dashed line is a standard lane line
                        and the white solid line/curb is a standard edge boundary. | markings: the right-turn
                        arrow is consistent with the rightmost lane position. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A white dashed line allows lane changes to the left.
Step 5  Rule            right_boundary: A white solid line and curb prohibit leaving the roadway to the right.
Step 5  Rule            arrow:merge_right: A right-turn arrow requires the vehicle to turn right and prohibits
                        going straight or turning left.
Step 5  Rule            line:stop_line: A stop line indicates where the vehicle must stop when required by a
                        signal or sign.
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a dashed white line.
Step 6  change_right    prohibited (contested, label allowed): prohibited: the right boundary is a solid white
                        line and a curb.
Step 6  go_straight     prohibited (correct): prohibited: the lane arrow only allows a right turn.
Step 6  turn_left       prohibited (correct): prohibited: the lane arrow only allows a right turn.
Step 6  turn_right      allowed (correct): allowed: the lane arrow shows a right turn.
Step 6  u_turn          prohibited (correct): prohibited: the lane arrow only allows a right turn.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a right-turn-only lane. You must turn right at the intersection; if you
                        need to go straight or turn left, you must change to the left lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:merge_right'], missed ['arrow:right']), actions True, unsafe [], citation
                        None, contradictions ['go_straight, turn_left, turn_right, u_turn decided without an
                        arrow or prohibited-movement marking']
Tokens                  in 3812, out 1015, 36.14 s

bdd100k_val__b9db357e-cd30a8ae | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road in the United States, approaching an intersection
                        with traffic signals. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left edge of the road. Photo 2 shows the same
                        solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        white edge line on the left indicates the leftmost lane of the roadway | roles: the
                        white solid edge line and white dashed lane line fit their roles | markings: no
                        markings in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area beyond the
                        roadway edge.
Step 5  Rule            right_boundary: A broken white lane line allows lane changes into the adjacent lane.
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white edge line
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but you cannot cross the left edge line.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 754, 2.98 s

bdd100k_val__bc05c126-d00aeb9c | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A two-way urban road with my car in the rightmost lane of its direction, heading
                        straight. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction.
                        Photo 2 shows two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a reddish-brown shoulder or
                        bike lane. Photo 2 shows a solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow center line prohibits crossing into the opposite
                        lane of traffic.
Step 5  Rule            right_boundary: A solid white edge line prohibits leaving the roadway or entering the
                        shoulder/bike lane.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 715, 19.17 s

bdd100k_val__bca36352-5de70a3f | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road in the US, approaching a section where the
                        rightmost lane ends or transitions into a restricted area marked by cones and
                        channelizing lines. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line that becomes a white solid line with a yellow solid
                        line inside it, then a white solid line again. Photo 2 shows a white solid line next
                        to my car, and further ahead, a yellow solid line appears inside the white boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 and Photo 2 show diagonal white lines (chevrons)
                        forming a buffer area to the right of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing to the right.
Step 5  Rule            area:channelizing: Channelizing lines indicate an area where vehicles should not
                        drive.
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed white lane line.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits continuing straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present in my lane.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left. Do not cross the solid white
                        line to the right into the channelized area.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['area:channelizing'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 3812, out 872, 33.35 s

bdd100k_val__bcbbfd82-add80c05 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road at night, heading towards a distant intersection
                        with traffic lights. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from another lane to the left.
                        Photo 2 shows the same white dashed line next to the car, with visible gaps between
                        dashes.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the roadway. Photo 2 shows the
                        same solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        lane line on the left and an edge line on the right indicate the rightmost lane of a
                        two-lane road. | roles: the white dashed line is a standard lane line and the white
                        solid line is a standard edge line. | markings: no markings in my lane, consistent
                        with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits leaving the roadway to the right.
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the white dashed lane line
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the white solid edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but do
                        not cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 3812, out 780, 26.96 s

bdd100k_val__bd026bc5-9418706c | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           Urban city street in the United States with multiple lanes of traffic heading straight
                        toward an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        a solid white line immediately next to my car, continuing forward.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line immediately next to my car, continuing forward.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white straight-ahead arrow painted
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right sides. | roles: the white
                        solid lines correctly serve as lane lines in an urban environment. | markings: the
                        straight-ahead arrow is consistent with the lane's position and boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits changing lanes.
Step 5  Rule            right_boundary: A solid white lane line prohibits changing lanes.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left, turning right, or making a U-turn.
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white left_boundary
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white right_boundary
Step 6  go_straight     allowed (correct): allowed by the arrow:straight marking
Step 6  turn_left       prohibited (correct): prohibited by the arrow:straight marking
Step 6  turn_right      prohibited (correct): prohibited by the arrow:straight marking
Step 6  u_turn          prohibited (correct): prohibited by the arrow:straight marking
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight through the intersection; lane changes
                        are prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 850, 27.88 s

bdd100k_val__be278041-2173a980 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road, likely a ramp or highway approach, with a concrete
                        barrier on the left and a lane splitting or ending ahead due to a gore area with a
                        chevron marker. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 confirms a solid
                        yellow line and a raised concrete barrier.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line that is initially broken and then becomes a double solid
                        white line further ahead. Photo 2 shows a white broken line (long dashes and gaps)
                        next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow edge line and concrete barrier prohibit leaving the
                        roadway to the left.
Step 5  Rule            right_boundary: The broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line and concrete barrier
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing in the lane
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the left boundary
                        due to the concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 738, 17.67 s

bdd100k_val__be4cbd00-97fec78b | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road at night, heading towards an intersection with
                        traffic lights ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car and continuing ahead. Photo 2 shows
                        a single white dash of a broken line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car and continuing ahead. Photo 2 shows
                        a single white dash of a broken line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundary roles as there are lane lines on both sides | roles: the white
                        dashed pattern fits the role of a lane line | markings: no markings in lane,
                        consistent with boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed left boundary
Step 6  change_right    allowed (correct): allowed by the white dashed right boundary
Step 6  go_straight     allowed (correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this
                        action
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this
                        action
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right. Be mindful of the traffic lights at the intersection ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 754, 25.63 s

bdd100k_val__beccfad4-d24a29c5 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading towards an intersection or ramp area. There is
                        a concrete barrier on the right and a curb on the left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car and a curb. Photo 2 shows a solid
                        white line and a raised concrete curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and a concrete barrier. Photo 2 shows
                        a solid white line and a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing the boundary to leave the
                        roadway.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing the boundary to leave the
                        roadway.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and curb
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and concrete barrier
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes are prohibited by the edge lines
                        and barriers.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 723, 24.07 s

bdd100k_val__bf6315ee-a77e1bb2 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           Urban road at night with traffic ahead, approaching a signalized intersection. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left separating my lane from a line of parked
                        cars. Photo 2 shows the same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right separating my lane from parked cars.
                        Photo 2 shows the same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area beyond it.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the area beyond it.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line on the
                        left.
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line on the
                        right.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight toward the intersection. Lane changes to the
                        left or right are prohibited by the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 744, 24.47 s

bdd100k_val__bf6711ef-76e408aa | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, traveling straight ahead toward an
                        intersection or a controlled area. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the road. Photo 2 confirms a
                        solid yellow line next to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to the car with a long dash and a gap.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows the word 'ONLY' painted in the lane. Photo 1 shows the
                        word 'ONLY' and a straight-ahead arrow further ahead.; arrow:straight (full): Photo 1
                        shows a straight-ahead arrow in the lane. Photo 2 shows the head of the straight-ahead
                        arrow.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        yellow edge line on the left indicates the leftmost lane of the direction. | roles:
                        the yellow solid edge line and white dashed lane line fit their roles. | markings: the
                        'ONLY' text and straight arrow are consistent with a lane dedicated to going straight.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits leaving the roadway to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            text:only: The 'ONLY' marking indicates that only the movement shown by the
                        accompanying arrow is permitted.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turning
                        left or right.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line.
Step 6  change_right    allowed (contested, correct): allowed by the white dashed lane line.
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow.
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow and 'ONLY' marking.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow and 'ONLY' marking.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow and 'ONLY' marking.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Your lane is a straight-only lane. You may continue straight or change lanes to the
                        right, but you cannot turn left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 992, 36.93 s

bdd100k_val__bfd64d5f-ec05de8b | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway approaching an exit ramp on the right. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line that curves to the right, marking the edge of the
                        main roadway. Photo 2 shows a white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        lane line on the left and an edge line on the right indicate my lane is the rightmost
                        of two lanes. | roles: the white dashed line is a standard lane line and the white
                        solid line is a standard edge line. | markings: no markings in my lane; consistent
                        with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes.
Step 5  Rule            right_boundary: A white solid edge line prohibits leaving the roadway to the right.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the white solid edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane.
                        Do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 773, 2.76 s

bdd100k_val__c01c4d85-36b417ee | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road at night, traveling straight ahead. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a single white dash and gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 shows a solid
                        white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line allows changing lanes.
Step 5  Rule            right_boundary: A solid white edge line prohibits leaving the roadway to the right.
Step 6  change_left     allowed (correct): allowed by the broken white lane line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 706, 23.9 s

bdd100k_val__c0a71f47-14439a44 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane road at night in the United States. My car is in the rightmost lane of
                        its direction, heading towards a distant intersection with traffic lights. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to the left. Photo 2
                        shows two yellow lines side by side, both solid, next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows the right edge of the road, which appears dark and lacks a painted line.
                        Photo 2 shows no painted line or curb next to my car.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a double yellow line on the left indicates the center
                        of a two-way road, making my lane the rightmost of my direction. | roles: the double
                        yellow solid lines correctly identify the center line for a two-way road. | markings:
                        no markings in my lane, consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: The edge of the roadway allows moving onto the shoulder if safe and
                        permitted.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line.
Step 6  change_right    allowed (WRONG, label prohibited): allowed as there is no painted line or curb
                        prohibiting it.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement.
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines to the
                        left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions
                        ['change_right decided with nothing marked on that side', 'u_turn decided without an
                        arrow or prohibited-movement marking']
Tokens                  in 3812, out 792, 28.53 s

bdd100k_val__c0f5b0d0-17e0110c | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane road at night, with traffic ahead and a wall on the right. (lanes 1, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the opposite direction of
                        traffic. Photo 2 shows the same solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the shoulder/wall. Photo 2
                        shows the same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing into the opposite traffic
                        lane.
Step 5  Rule            right_boundary: A solid white edge line prohibits leaving the roadway to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 704, 3.55 s

bdd100k_val__c16d3fdb-a3a8c912 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or freeway, traveling straight ahead on a clear
                        road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating the road from a shoulder and a concrete
                        barrier. Photo 2 shows the same solid yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits crossing into the shoulder or
                        opposite direction.
Step 5  Rule            right_boundary: A broken white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow edge line, which prohibits
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is the default
                        movement for a highway lane.
Step 6  turn_left       not_applicable: No marking governs this action; it is not applicable on a highway.
Step 6  turn_right      not_applicable: No marking governs this action; it is not applicable on a highway.
Step 6  u_turn          not_applicable: No marking governs this action; it is not applicable on a highway.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane as needed. Do not cross the solid yellow
                        line on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 744, 23.27 s

bdd100k_val__c1e6340e-084ce27d | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road at night, traveling straight ahead. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from the opposite direction of
                        traffic. Photo 2 shows the same solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to my car with a visible gap.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left indicates my lane is the
                        leftmost of my direction | roles: the yellow solid line fits the role of a center
                        line, and the white dashed line fits the role of a lane line | markings: no markings
                        in my lane to conflict with boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    allowed (correct): allowed by the white dashed lane line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may continue straight or change
                        lanes to the right, but you must not cross the yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 773, 3.48 s

bdd100k_val__c39dc2ff-6976d19d | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           Urban street at night with multiple lanes of traffic. My car is in a lane that appears
                        to be a dedicated turn lane approaching an intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left edge of the road. Photo 2 shows the same
                        solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to my car with visible gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow and the word 'ONLY' painted
                        in my lane.; text:only (full): Photo 2 shows the word 'ONLY' painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing to the left of the roadway.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 5  Rule            arrow:left: A left-turn arrow requires the vehicle to turn left and prohibits going
                        straight or turning right.
Step 5  Rule            text:only: The word 'ONLY' reinforces that only the movement indicated by the arrow is
                        permitted.
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line
Step 6  change_right    allowed (contested, correct): allowed by the dashed white lane line
Step 6  go_straight     prohibited (correct): prohibited by the left-turn arrow and 'ONLY' text
Step 6  turn_left       allowed (correct): allowed by the left-turn arrow
Step 6  turn_right      prohibited (correct): prohibited by the left-turn arrow and 'ONLY' text
Step 6  u_turn          allowed (correct): allowed as a left-turn arrow typically permits U-turns unless
                        prohibited
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a left-turn-only lane. You must turn left or perform a U-turn; you cannot
                        go straight. You may change lanes to the right if needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 932, 31.28 s

bdd100k_val__c3ecb3cb-5fb43d29 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane city road with a construction zone on the left; my car is in a lane that
                        appears to be a dedicated turn lane. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line next to the car, with a row of orange and white traffic
                        cones/bollards on the left. Photo 2 shows a solid yellow line immediately to the left
                        of the lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows a solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows the word 'ONLY' painted in white in my lane.;
                        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing into the opposite traffic
                        lane.
Step 5  Rule            right_boundary: A solid white lane line prohibits changing lanes to the right.
Step 5  Rule            text:only: The word ONLY indicates that only the movement shown by the accompanying
                        arrow is permitted.
Step 5  Rule            arrow:straight: A straight-ahead arrow permits going straight and prohibits turns.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white lane line
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow and the ONLY marking
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow and the ONLY marking
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow and the ONLY marking
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes and turns are prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 907, 27.24 s

bdd100k_val__c400a0e1-c137168b | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban highway or expressway with an exit ramp ahead to the
                        right. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 shows the same
                        solid yellow line and the concrete barrier.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows the word 'ONLY' painted in the lane to the right, not
                        in my lane. Photo 1 shows no markings within my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line and barrier prohibit leaving the roadway to
                        the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line and concrete barrier
Step 6  change_right    allowed (contested, correct): allowed by the white dashed lane line
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing straight
Step 6  turn_left       prohibited: prohibited by the left boundary and lack of a left-turn arrow
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement in my lane
Step 6  u_turn          prohibited: prohibited by the left boundary and lack of a u-turn arrow
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the right. To exit, move into the
                        rightmost lane which is marked 'ONLY' for the exit.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation None, contradictions
                        ['turn_left, u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 3812, out 792, 26.34 s

bdd100k_val__c464c963-0279dcc0 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A two-way residential street with parked cars on both sides; the road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two solid yellow lines separating the directions of traffic. Photo 2
                        shows two solid yellow lines next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, but a curb with parked cars. Photo 2 shows
                        no painted line next to my car, only the edge of the roadway and a curb.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the center line on the left and the curb on the right | roles: the double solid yellow
                        lines correctly identify a center line for a two-way road | markings: no markings in
                        lane, consistent with boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double solid yellow lines prohibit crossing into the opposite lane of
                        traffic.
Step 5  Rule            right_boundary: The curb marks the edge of the roadway and prohibits leaving the road.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line
Step 6  change_right    prohibited (correct): prohibited by the curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines or drive
                        onto the curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['u_turn decided without
                        an arrow or prohibited-movement marking']
Tokens                  in 3812, out 748, 21.93 s

bdd100k_val__c4b77809-63fd577c | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a city street in the United States, approaching an intersection. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line. Photo 2 shows two solid yellow lines side by
                        side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows the edge of the road with a parked white truck. Photo 2 shows no painted
                        line, just the asphalt meeting the curb/parking area.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        text:stop (full): Photo 1 and Photo 2 both show the word 'STOP' painted in white
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits crossing into the opposite traffic
                        lane.
Step 5  Rule            right_boundary: The edge of the roadway/curb prohibits leaving the road to the right.
Step 5  Rule            text:stop: The STOP marking requires the vehicle to come to a complete stop before
                        proceeding.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line
Step 6  change_right    prohibited (correct): prohibited by the curb/edge of the road
Step 6  go_straight     stop_first (contested, correct): stop_first due to the STOP marking in the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and come to a complete stop at the STOP line before proceeding
                        straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 816, 28.35 s

bdd100k_val__c4d25f00-3b1d8669 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road at night, approaching a crosswalk and an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white dashed line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to the car with a long dash and a gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to the car with a long dash and a gap.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white crosswalk line across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right sides. | roles: the white
                        dashed patterns are consistent with lane lines in the US. | markings: the crosswalk is
                        consistent with an approaching intersection. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 5  Rule            line:crosswalk: A crosswalk indicates a pedestrian crossing area and does not restrict
                        vehicle movement except for yielding to pedestrians.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight, and the boundaries
                        do not restrict it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane and can proceed straight or change lanes to the left or
                        right. Be prepared to stop for pedestrians at the crosswalk.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 891, 27.81 s

bdd100k_val__c4e92086-e1b8324f | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, traveling straight ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from a parking or shoulder area on
                        the right. Photo 2 shows a white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries: a lane line on the left and an edge line on the right place my
                        lane as the second of three lanes (or the rightmost travel lane). | roles: the white
                        dashed line is a standard lane line and the white solid line is a standard edge line.
                        | markings: no markings are present in my lane, which is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes.
Step 5  Rule            right_boundary: A white solid edge line prohibits crossing into the shoulder or
                        parking area.
Step 6  change_left     allowed (correct): allowed by the white dashed lane line
Step 6  change_right    prohibited (correct): prohibited by the white solid edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the left. Do not cross the solid white
                        line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 776, 3.7 s

bdd100k_val__c55da7df-facccafc | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the US with traffic keeping right, approaching an
                        intersection or ramp area. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to my car, which continues as a white broken
                        line further ahead. Photo 2 shows a white broken line with clear dashes and gaps next
                        to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to my car and continuing as a white solid line
                        further ahead. Photo 2 shows a white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows the word 'ONLY' and a right-turn arrow painted in my
                        lane.; arrow:merge_right (full): Photo 2 shows a right-turn arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white solid edge line prohibits leaving the roadway to the right.
Step 5  Rule            text:only: The word ONLY indicates that only the movement shown by the accompanying
                        arrow is permitted.
Step 5  Rule            arrow:merge_right: A right-turn arrow allows turning right and prohibits going
                        straight or turning left.
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed lane line.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid edge line.
Step 6  go_straight     prohibited (contested, label allowed): prohibited: the right-turn arrow in my lane
                        prohibits going straight.
Step 6  turn_left       prohibited: prohibited: the right-turn arrow in my lane prohibits turning left.
Step 6  turn_right      allowed: allowed: the right-turn arrow in my lane allows turning right.
Step 6  u_turn          prohibited: prohibited: the right-turn arrow in my lane prohibits U-turns.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  My lane is a right-turn-only lane. To go straight or turn left, I must change to the
                        lane on the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:merge_right'], missed []), actions True, unsafe [], citation None,
                        contradictions ['go_straight, turn_left, turn_right, u_turn decided without an arrow
                        or prohibited-movement marking']
Tokens                  in 3812, out 946, 29.16 s

bdd100k_val__c588eb5e-dfd59d8e | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a city street with multiple lanes of traffic. The road continues
                        straight ahead into the distance. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction of
                        traffic. Photo 2 shows the same double yellow lines immediately to the left of my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to my car, with a gap and a dash visible.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left indicates my lane is the
                        leftmost of my direction | roles: the yellow double-solid line fits the role of a
                        center line, and the white dashed line fits the role of a lane line | markings: no
                        markings in my lane to conflict with boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow center line prohibits crossing into the opposite
                        lane of traffic.
Step 5  Rule            right_boundary: A white dashed lane line allows changing into the adjacent lane.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line
Step 6  change_right    allowed (correct): allowed by the white dashed lane line
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may continue straight or change
                        lanes to the right, but you cannot cross the double yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 815, 27.63 s

bdd100k_val__c59500f0-130d7415 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in the US with traffic keeping right; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 shows the same double solid yellow lines next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the rightmost lane, and
                        further ahead, a white solid line at the edge of the road. Photo 2 shows a white
                        dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left and a lane line on the right
                        indicate I am in the second lane from the left of my direction, but the leftmost of
                        the travel lanes in this specific section if the rightmost is a parking/slow lane,
                        however, based on the car to the right, it is a standard multi-lane road. | roles: the
                        double solid yellow line fits the role of a center line; the white dashed line fits
                        the role of a lane line. | markings: no markings in my lane, consistent with
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow center line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line.
Step 6  change_right    allowed (correct): allowed by the white dashed lane line.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement.
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the double yellow
                        lines to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right', 'u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 3812, out 835, 2.97 s

bdd100k_val__c5b2506d-07e406a6 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           Urban road in a city with multiple lanes of traffic moving in the same direction.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating the roadway from a median/curb area.
                        Photo 2 shows the same solid yellow line next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dash and gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits crossing into the median or
                        shoulder.
Step 5  Rule            right_boundary: A broken white lane line allows changing into the adjacent lane.
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow line and a
                        curb, which prohibits leaving the lane to the left.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows changing to
                        the right lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict forward movement.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you cannot cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 746, 26.25 s

bdd100k_val__c74ee988-8f4b380d | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on both sides. The road ahead is straight
                        with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating the ego lane from the opposite direction
                        of traffic. Photo 2 confirms two solid yellow lines next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating the ego lane from a parking area. Photo 2 shows
                        a white dashed line next to the car.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits crossing into the opposite
                        direction of traffic.
Step 5  Rule            right_boundary: A dashed white edge line allows crossing into the parking area if
                        safe.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line
Step 6  change_right    allowed (contested, label prohibited): allowed by the dashed white edge line
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may move to the right to park, but do not
                        cross the double yellow lines to the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 718, 2.66 s

bdd100k_val__c7c042ec-4986a853 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane city road at night, with an intersection ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the left lane. Photo 2 shows
                        a white broken line with clear dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the right lane. Photo 2
                        shows a white broken line with clear dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a straight-ahead arrow in my lane. Photo 2 shows
                        the arrow head pointing forward.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; white broken lines on both sides indicate I am in the
                        middle of at least three lanes. | roles: the white dashed pattern fits the role of a
                        lane line. | markings: the straight arrow is consistent with a through lane. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A white broken lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white broken lane line allows changing lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead arrow allows going straight and prohibits turns.
Step 6  change_left     allowed (correct): allowed by the white broken left boundary
Step 6  change_right    allowed (correct): allowed by the white broken right boundary
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the straight-ahead arrow
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn, change to the appropriate lane
                        using the broken white lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_right']), actions False, unsafe [],
                        citation None, contradictions []
Tokens                  in 3812, out 841, 3.06 s

bdd100k_val__c96ffe59-1cf2df11 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings and trees on both sides. The road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating the ego lane from the opposite direction
                        of traffic. Photo 2 shows the same double yellow line next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating the ego lane from a parking or shoulder area.
                        Photo 2 shows a white dashed line next to the car.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow center line prohibits crossing into the opposite
                        lane of traffic.
Step 5  Rule            right_boundary: A dashed white edge line allows crossing into the area to the right,
                        such as for parking or pulling over.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the double solid yellow center line
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the dashed white edge line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow line to the
                        left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation None, contradictions
                        ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 3812, out 705, 4.03 s

bdd100k_val__ca15f699-e51c14c0 | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane road at night, heading towards a distant
                        intersection or urban area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to my car with clear gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the presence of lane lines on both the left and right sides. | roles: the white
                        dashed patterns are consistent with lane lines separating traffic in the same
                        direction. | markings: no markings were observed in the lane, which is consistent with
                        the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A white dashed lane line allows changing lanes to the right.
Step 6  change_left     allowed (correct): The left boundary is a dashed white line, which allows lane
                        changes.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not prohibit it.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 3812, out 786, 29.34 s

bdd100k_val__fe194677-e2d2ac8c | lane | Test A | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road, likely near a terminal or transit hub, with
                        traffic moving forward. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white line separating my lane from a shoulder or curb area covered in
                        snow. Photo 2 shows the same white line next to the car, partially obscured by snow.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with visible gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or non-
                        roadway area.
Step 5  Rule            right_boundary: A dashed white lane line allows changing lanes to the right.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid edge line with a curb,
                        which prohibits leaving the lane to the left.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a dashed lane line, which
                        allows changing to the right lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict forward movement.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left edge line into the snow-covered area.
Score                   lane False, boundaries {'left': None, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 3812, out 754, 2.98 s
```
