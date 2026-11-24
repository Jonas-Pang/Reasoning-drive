# Reasoning of lane run 20261117_040150_laneB_UK

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
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [[UK-TSRGD-S11P4-item11]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white edge line [UK-
                        TSRGD-S11P4-item11].
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
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 787, 19.14 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
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
Step 2  Right           There is no painted line or curb on the right side of my lane; it is an open area
                        where other vehicles are positioned.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 are consistent with the left boundary being
                        an edge line and the right boundary being undefined/open. | roles: The solid yellow
                        line on the left fits the role of an edge line indicating waiting restrictions. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: I may stop to load or unload on this yellow line unless loading
                        restrictions apply. [UK-HC_MARKINGS-p2] "Waiting restrictions indicated by yellow
                        lines apply to the carriageway, pavement and verge. You may stop to load or unload
                        (unless there are also loading restr"
Step 6  change_left     prohibited (contested, label not_determined): prohibited: the left boundary is a solid
                        yellow line and a curb, and UK-Rule140/TSRGD-12(2) generally prohibit driving on
                        pavements/cycle lanes, though here it is primarily a waiting restriction edge.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: no marking governs this action.
Step 6  go_straight     allowed (contested, label not_determined): allowed: no marking restricts carrying on
                        straight along my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line to the left as it
                        borders the pavement.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 13644, out 779, 19.62 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
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
                        lane line and the right boundary being the edge of the road. | roles: The solid white
                        line on the left fits the role of a boundary for a cycle lane. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: You MUST NOT drive or park in a cycle lane marked by a solid white line
                        during its times of operation. [[UK-Rule140]]
Step 5  Rule            right_boundary: No specific rule prohibits leaving the lane to the right if it is safe
                        and the road allows it. [null]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white line boundary and [UK-
                        Rule140].
Step 6  change_right    allowed (correct): Allowed as there is no marking prohibiting it.
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right if necessary; do not enter the cycle lane on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 13644, out 770, 17.66 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
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

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, looking straight ahead towards a
                        clear stretch of road with vehicles in front. (lanes 2, mine 2, full)
Step 2  Left            A short, broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid red line marks the edge of the carriageway next to the pavement.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The broken white line fits the
                        role of a lane divider, and the red line fits the role of a carriageway edge marking.
                        | markings: There are no markings in my lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I should keep between the short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            right_boundary: Stopping to park, load/unload or to board and alight is prohibited on
                        the red line. [[UK-HC_MARKINGS-p2-8]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [UK-Rule131].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid red edge line and the
                        presence of a curb [UK-HC_MARKINGS-p2-8].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings in my lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You can proceed straight or change to the left lane. Do not cross the red line to the
                        right as it is the edge of the road and stopping is prohibited there.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13644, out 820, 57.55 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road ahead continues straight, and my car is
                        positioned in a single lane of travel. (lanes 1, mine 1, full)
Step 2  Left            I see a grey raised curb separating the road from the sidewalk.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           I see a line of parked cars along the right side of the road, but no painted line is
                        visible on the road surface.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the boundaries, as
                        both sides are edges of the carriageway. | roles: The absence of paint and the
                        presence of a curb on the left fit the role of edge boundaries. | markings: There are
                        no markings in my lane to contradict. | unseen: I have not reported any attributes I
                        did not see. | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway available for through traffic. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            right_boundary: This is the edge of the carriageway available for through traffic.
                        [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for
                        through traffic other than at a road junction, an exit from a private drive onto a
                        public road, lay-by "
Step 6  change_left     prohibited (contested, correct): Prohibited by the physical curb (left_boundary).
Step 6  change_right    allowed (correct): No marking governs this action, but it is the edge of the
                        carriageway.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the left curb into the sidewalk.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 13644, out 788, 19.92 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------
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
Step 1  Scene           This is an urban residential street with parked cars on both sides. The road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line is painted on the left side of the lane, next to the curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line on the right side, only a curb with parked cars.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The word 'BUS' is painted in yellow in the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries, as both sides are
                        edge lines. | roles: The yellow solid line on the left is a common edge marking for
                        waiting restrictions in the UK. | markings: The 'BUS' text indicates this is a
                        designated bus lane. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: You may stop to load or unload unless other restrictions apply. [UK-
                        HC_MARKINGS-p2] "Waiting restrictions indicated by yellow lines apply to the
                        carriageway, pavement and verge. You may stop to load or unload (unless there are also
                        loading restr"
Step 5  Rule            right_boundary: No specific rule for a non-painted boundary; it marks the edge of the
                        carriageway.
Step 5  Rule            text:bus: You should not drive in a bus lane during its period of operation. [UK-
                        Rule141-2] "Unless otherwise indicated, you should not drive in a bus lane during its
                        period of operation."
Step 6  change_left     prohibited (contested, correct): Prohibited by the curb and the solid yellow line
                        which marks the edge of the carriageway.
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the curb and parked cars.
Step 6  go_straight     allowed (contested, correct): Allowed, although the lane is a bus lane, there is no
                        marking prohibiting forward movement.
Step 6  turn_left       not_applicable: Not applicable; no arrow or intersection marking governs this.
Step 6  turn_right      not_applicable: Not applicable; no arrow or intersection marking governs this.
Step 6  u_turn          not_applicable: Not applicable; no arrow or intersection marking governs this.
Step 6  enter_waiting_areanot_applicable: Not applicable; no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane; you should avoid driving in it during its hours of
                        operation. Stay in the lane as there are no options to change lanes due to the curbs
                        and parked cars.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 13644, out 877, 18.17 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road ahead is clear with some parked
                        vehicles and a cyclist, and there is no immediate intersection or ramp visible. (lanes
                        1, mine 1, full)
Step 2  Left            A single solid yellow line is painted along the edge of the road next to the curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line is visible on the right side of the lane; it is bordered by the road
                        surface and parked cars.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 are consistent with the left
                        boundary being an edge line. | roles: The solid yellow line on the left is a waiting
                        restriction marking on the edge of the carriageway, fitting the edge_line role. |
                        markings: There are no markings in the lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting; however, this is a single yellow
                        line, which according to [UK-HC_MARKINGS-p2] allows stopping to load or unload unless
                        other restrictions apply. [UK-HC_MARKINGS-p2-2] "Double yellow lines mean no waiting
                        at any time, unless there are signs that specifically indicate seasonal restrictions."
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a curb and a solid
                        line, and [UK-Rule140] or general road edge definitions prohibit driving onto the
                        pavement.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: no marking governs this action on the
                        right side.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be mindful of the cyclist and parked cars on
                        your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 13644, out 798, 15.02 s
```
