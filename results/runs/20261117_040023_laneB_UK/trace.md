# Reasoning of lane run 20261117_040023_laneB_UK

```text
lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with shops on both sides; the road continues straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a paved area with shops.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a parking area where a car is stopped.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries being edge lines
                        on both sides. | roles: The solid white lines on both sides are consistent with edge
                        lines in an urban setting. | markings: There are no markings in the lane to contradict
                        the boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white edge line (UK-
                        TSRGD-S11P4-item11).
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line (UK-
                        TSRGD-S11P4-item11).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 787, 18.11 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road ahead is straight with no
                        immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            A short, broken white line divides my lane from another lane of the same direction.
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
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the right-hand lane of a two-lane road. You may proceed straight or change
                        to the left lane, but do not cross the solid white line on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 811, 45.59 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides. The road ahead appears
                        to be a straight stretch with no immediate intersection or ramp visible. (lanes 1,
                        mine 1, full)
Step 2  Left            I see a solid yellow line along the left edge of the road next to the pavement.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line or curb on the right side, only the asphalt of the road where
                        other vehicles are positioned.
                        none none, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 are consistent with a yellow edge line on
                        the left and no boundary on the right (indicating a shared or unmarked space). |
                        roles: The solid yellow line on the left fits the role of an edge line indicating
                        waiting restrictions. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting; however, this is a single yellow
                        line, which according to [UK-HC_MARKINGS-p2], allows stopping to load or unload unless
                        other restrictions apply. [UK-HC_MARKINGS-p2-2] "Double yellow lines mean no waiting
                        at any time, unless there are signs that specifically indicate seasonal restrictions."
Step 5  Rule            right_boundary: No specific rule governs a boundary that consists of no painted line
                        and no curb.
Step 6  change_left     prohibited (contested, label not_determined): prohibited by the solid yellow edge line
                        and the presence of the pavement/curb.
Step 6  change_right    allowed (WRONG, label not_determined): allowed as there is no marking or physical
                        barrier governing this action.
Step 6  go_straight     allowed (contested, label not_determined): allowed as there are no markings in the
                        lane restricting forward movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line to the left as it
                        marks the edge of the carriageway.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['rightmost lane, but a lane line on the right', 'change_right decided with nothing
                        marked on that side']
Tokens                  in 13644, out 826, 21.3 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street in the UK. The road ahead is clear with a red bus in the
                        distance; there is no immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            I see a white dashed line separating the road from a parking area or side street on
                        the left.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           I see a white dashed line separating my lane from a row of parked cars on the right.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        area:grid (full): A yellow criss-cross box junction is painted across the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries, as both are edge
                        lines. | roles: The white dashed patterns fit the role of edge lines in an urban
                        setting. | markings: The yellow box junction is a standard feature at junctions or
                        narrow points in the UK. | unseen: No attributes were reported without visual
                        evidence. | result: consistent
Step 5  Rule            left_boundary: This is an informative marking indicating the edge of the carriageway
                        available for through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the
                        carriageway available for through traffic other than at a road junction, an exit from
                        a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is an informative marking indicating the edge of the carriageway
                        available for through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the
                        carriageway available for through traffic other than at a road junction, an exit from
                        a private drive onto a public road, lay-by "
Step 5  Rule            area:grid: The driver must not enter the box junction if they will have to stop within
                        it due to stationary vehicles. [UK-TSRGD-11(1)] "Subject to sub-paragraphs (2), (3)
                        and (4), the yellow criss-cross marking conveys the prohibition that a person must not
                        cause a vehicle to enter the box junct"
Step 6  change_left     allowed (contested, label prohibited): allowed; the left boundary is a dashed white
                        line, and no rule prohibits crossing it if safe.
Step 6  change_right    allowed (WRONG, label not_determined): allowed; the right boundary is a dashed white
                        line, and no rule prohibits crossing it if safe.
Step 6  go_straight     allowed (contested, correct): allowed; no marking prohibits going straight, and it is
                        the natural path of the lane.
Step 6  turn_left       not_applicable: not_applicable; no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable; no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable; no arrow or prohibited-movement marking governs this.
Step 6  enter_waiting_areanot_applicable: not_applicable; there is no left-turn waiting area or two-way left-
                          turn lane.
Step 7  Reflect         consistent
Advice                  You may proceed straight. Do not enter the yellow box junction unless your exit is
                        clear, to avoid blocking the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 13644, out 935, 49.17 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings on both sides. A red bus is ahead in the same
                        direction, and the road continues straight. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a cycle lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           There is no painted line on the right, only the edge of the road where cars are
                        parked.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left boundary being a special
                        lane line and the right boundary being the edge of the carriageway. | roles: The solid
                        white line on the left fits the role of a boundary for a cycle lane. | markings: There
                        are no markings in the lane to contradict. | unseen: No attributes were reported that
                        were not visible. | result: consistent
Step 5  Rule            left_boundary: Vehicles must not be driven in the cycle lane during its hours of
                        operation. [[UK-TSRGD-12(2)]]
Step 5  Rule            right_boundary: No specific rule prohibits moving right if the road is clear, but it
                        is the edge of the carriageway. [null]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line marking a
                        cycle lane, which prohibits driving in it per [UK-TSRGD-12(2)].
Step 6  change_right    allowed (correct): No marking governs this action, but it is the edge of the road.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the cycle lane on your left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 13644, out 796, 17.18 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with shops on both sides; the road continues straight ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            A short, broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the carriageway, with a sidewalk and shops beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the presence of a
                        lane line on the left and an edge line on the right. | roles: The broken white line
                        fits the role of a lane divider, and the solid white line fits the role of an edge
                        line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line [UK-
                        Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and the
                        presence of a curb [UK-TSRGD-S11P4-item11].
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
Tokens                  in 13644, out 807, 13.25 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, looking straight ahead towards a
                        clear stretch of road with vehicles in front. (lanes 2, mine 1, full)
Step 2  Left            A solid red line is painted along the left edge of the road, next to the pavement.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line divides my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The solid red
                        line on the left fits the role of an edge line (Red Route), and the broken white line
                        on the right fits the role of a lane divider. | markings: There are no markings in my
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: Stopping to park, load/unload or to board and alight is prohibited on
                        the red line. [[UK-HC_MARKINGS-p2-8]]
Step 5  Rule            right_boundary: I should keep between the lane divider lines. [[UK-Rule131]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid red edge line; while
                        it prohibits stopping, it does not explicitly prohibit a lane change if safe, but it
                        is the edge of the carriageway.
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, which allows
                        changing lanes if safe according to [UK-Rule131].
Step 6  go_straight     allowed (contested, correct): No marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right lane if needed. Do not stop or park on the left
                        side due to the red route restrictions.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13644, out 804, 18.07 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead continues straight, and my car is
                        positioned in a single lane of traffic. (lanes 1, mine 1, full)
Step 2  Left            I see a grey raised curb separating the road from the sidewalk.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           I see a white dashed line separating my lane from a parking area where cars are
                        stopped.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the boundaries; I
                        have an edge boundary on both the left (curb) and right (dashed line). | roles: The
                        curb on the left and the dashed white line on the right both fit the role of edge
                        boundaries for a single-lane road. | markings: There are no markings in my lane to
                        contradict. | unseen: I have not reported any attributes I did not see. | result:
                        consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is the boundary between the main carriageway and a parking area
                        or side road. [UK-TSRGD-S11P4-item10] "Diagram 1010 (a) edge of the carriageway at a
                        road junction or a lay-by, or at an exit from a private drive onto a public road; (b)
                        the start of a traffic lane,"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a physical curb.
Step 6  change_right    allowed (correct): allowed: the right boundary is a dashed white line, which does not
                        prohibit crossing if safe.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You can proceed straight in your lane. You may move to the right to access the parking
                        area if it is safe to do so, but do not cross the curb on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 833, 20.41 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with shops on both sides; the road continues straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a parking area and sidewalk.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           There is no painted line on the right, only the edge of the asphalt meeting a parking
                        area with cars.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries, as both sides are
                        edge lines. | roles: The solid white line on the left fits the role of an edge line
                        for a parking/sidewalk area. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: This is an informative marking indicating the edge of the carriageway
                        available for through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the
                        carriageway available for through traffic other than at a road junction, an exit from
                        a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: No specific rule for a non-painted boundary; it defines the physical
                        limit of the lane.
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a solid white edge line;
                        while not explicitly prohibiting crossing in all cases, it marks the edge of the
                        carriageway, and crossing into the parking/sidewalk area is generally not a standard
                        lane change.
Step 6  change_right    allowed (correct): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may proceed straight or move to the sides if safe to do
                        so for parking or exiting the road.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 13644, out 793, 57.12 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban residential road with buildings on both sides. The road continues
                        straight ahead with parked cars along the right side. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line is painted on the left side of the lane.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           There is no painted line on the right side, but parked cars and a curb define the
                        edge.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The word 'BUS' is painted in yellow in the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries, as both sides are
                        edge lines. | roles: The yellow solid line on the left is a common marking for waiting
                        restrictions at the edge of the carriageway. | markings: The 'BUS' text indicates this
                        is a designated bus lane. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: You may stop to load or unload unless other restrictions apply. [UK-
                        HC_MARKINGS-p2] "Waiting restrictions indicated by yellow lines apply to the
                        carriageway, pavement and verge. You may stop to load or unload (unless there are also
                        loading restr"
Step 5  Rule            right_boundary: No specific rule for a non-painted boundary with a curb, but it marks
                        the edge of the roadway. [null]
Step 5  Rule            text:bus: You should not drive in a bus lane during its period of operation. [UK-
                        Rule141-2] "Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation."
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a solid yellow line; no
                        rule prohibits crossing it for a lane change, but it is an edge line.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb, which physically
                        prohibits leaving the lane to the right.
Step 6  go_straight     allowed (contested, correct): The lane is a bus lane; while no arrow prohibits going
                        straight, driving in it is discouraged by UK-Rule141-2.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane; you should avoid driving in it during its hours of
                        operation. Be mindful of the parked cars on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 13644, out 884, 13.79 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead is clear with some parked vehicles on
                        the right; my car is driving forward in a single lane. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line is painted along the edge of the road next to the curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line is visible on the right side, but there is a curb and parked cars.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries, as both sides are
                        edge lines. | roles: The yellow solid line on the left is a waiting restriction
                        marking at the edge of the carriageway. | markings: There are no markings in the lane
                        to contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: I may stop to load or unload unless other restrictions apply. [UK-
                        HC_MARKINGS-p2] "Waiting restrictions indicated by yellow lines apply to the
                        carriageway, pavement and verge. You may stop to load or unload (unless there are also
                        loading restr"
Step 5  Rule            right_boundary: No specific rule for a non-painted boundary; it marks the edge of the
                        road. [null]
Step 6  change_left     prohibited (contested, correct): Prohibited by the curb and the solid yellow line
                        which marks the edge of the carriageway.
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the curb and the presence of
                        parked vehicles.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no intersection or arrow governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no intersection or arrow governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line on the left or
                        enter the area with parked cars on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 13644, out 776, 10.65 s
```
