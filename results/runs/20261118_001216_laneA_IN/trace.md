# Reasoning of lane run 20261118_001216_laneA_IN

```text
idd__primary_d1_leftCamImgs_0000529 | lane | Test A | meta-muse-glimmer-30b
---------------------------------------------------------------------------
Step 1  Scene           The photo shows a narrow residential street in India with buildings and parked two-
                        wheelers on both sides. The road ahead is straight and no intersection, ramp or lane
                        end is visible in the visible stretch. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line forming the left edge of the carriageway next to parked
                        scooters and a dirt verge, continuing ahead. Photo 2 shows the same solid white line
                        close up immediately to the left of my lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line forming the right edge of the carriageway next to a dirt
                        shoulder and vegetation, continuing ahead. Photo 2 shows the same solid white line
                        close up immediately to the right of my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: A lane count of 1 with ego lane index 1
                        agrees with left and right edge lines bounding the single carriageway of my direction.
                        | roles: White solid lines at the roadway edges are edge lines, consistent with their
                        position and appearance. | markings: No arrows, words, symbols, areas or lines are
                        painted in my lane in either photo. | unseen: no | result: consistent
Step 5  Rule            left_boundary: An edge line marks the boundary of the carriageway; leaving the roadway
                        across it is generally prohibited except to avoid a hazard.
Step 5  Rule            right_boundary: An edge line marks the boundary of the carriageway; leaving the
                        roadway across it is generally prohibited except to avoid a hazard.
Step 6  change_left     prohibited (correct): Left boundary is a solid white edge line; crossing the roadway
                        edge to the verge/sidewalk is prohibited.
Step 6  change_right    prohibited: Right boundary is a solid white edge line; crossing the roadway edge to
                        the shoulder is prohibited.
Step 6  go_straight     allowed (contested, correct): No lane-use arrow or prohibited-movement marking is in
                        my lane, so proceeding straight along the carriageway is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs a turn at the end of
                        the visible stretch.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs a turn at the end of
                        the visible stretch.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs a U-turn at the end of
                        the visible stretch.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or two-way left-turn lane is visible ahead
                          of or next to my lane.
Step 7  Reflect         consistent
Advice                  Stay within the carriageway between the two white edge lines. The road is narrow with
                        no lane markings ahead, so continue straight and do not cross the edge lines onto the
                        verge or shoulder.
Model's summary         This photo was taken in India, where traffic keeps to the left. Interpret my lane.
                        Photo 2 is close-up of road just ahead of my car, cut from Photo 1 and shown larger.
                        We have Photo 1 (first image) and Photo 2 (second image). Photo 1 is whole dash-camera
                        photo. Photo 2 is close-up.  We need scene: road type, what is ahead (intersection,
                        ramp, lane that ends), count lanes of my direction near bottom, ego_lane_index.  From
                        images: looks like a narrow residential street, two-way? There's a white line on left
                        and right of the road? Actually the road appears to have a central white line? Wait
                        the image shows a road with a white line on left side of the lane (from driver's
                        perspective) and a white line on right side. The motorbike is ahead in the middle of
                        the road? The road seems to be a single lane each direction? Or maybe it's a single
                        carriageway with no center line? Let's examine.  Photo 1: view forward. The road is
                        straight ahead, with buildings on both sides. There's a white line on left edge of the
                        roadway (near the parked scooters) and a white line on right edge. The road surface
                        between them is the carriageway. The motorbike is riding in the middle of that
                        carriageway. So maybe it's a single lane for each direction? Or it's a two-lane road
                        with no center marking? Wait the white lines appear to be edge lines, not center. The
                        road between them is wide enough for maybe two vehicles side by side? But the
                        motorbike is in the center.  In India, traffic keeps left. So my car is driving on the
                        left side of the road. My lane is the leftmost lane of my direction. The road appears
                        to have two directions sharing the same width, with edge lines on both sides. There is
                        no center line visible. So maybe it's a single lane road for each direction, with edge
                        lines marking the roadway boundary. The lane is the whole width between edge lines? Or
                        is there a center line? Could be a single lane road with no markings in middle.  The
                        photo shows a white line on left side of the road (my left) and a white line on right
                        side (my right). The left white line is next to parked scooters and sidewalk. The
                        right white line is next to dirt shoulder and bushes. So my lane is bounded on left by
                        a white edge line, on right by a white edge line. No lane lines between directions.
                        Lane count: near bottom of photo, how many lanes of my direction? It looks like one
                        lane. Could be one lane each direction sharing the road. So lane_count = 1? Or maybe
                        2? Let's think: the road width between the two white lines is about maybe 2 car
                        widths. But no center line. Might be considered one lane for each direction, but the
                        lane is not marked. The instruction: count the lanes of my direction near the bottom
                        of the photo. If no lane markings, maybe it's one lane.  Ego_lane_index: if
                        lane_count=1, index=1.  Scene: residential street, straight ahead, no intersection
                        visible. Maybe ahead there is oncoming traffic? There's vehicles ahead in distance. No
                        intersection visible.  Boundaries: left_boundary: observation: Photo1 shows a white
                        line on left side of road, solid? It appears solid white line along left edge. Photo2
                        shows same white line close up, solid? It looks like a solid white line, maybe with
                        some gaps? It appears continuous. Color white. Pattern solid. Curb? No raised curb,
                        just edge of pavement with dirt. Role: edge_line (edge of roadway). Evidence full?
                        Partial? Might be full.  Right_boundary: similar white line on right side. Solid
                        white. Edge line.  Markings: lane_markings: any arrows, words, symbols? None visible.
                        No stop line, no crosswalk. So empty list.  Cross-check: close_up: same in both
                        photos. Position: lane count and ego lane position agree with boundary roles? Left
                        boundary is edge line, so leftmost lane. Right boundary is edge line, so rightmost
                        lane. So consistent.  Roles: color white, pattern solid fits edge line.  Markings:
                        none.  Unseen: no.  Result consistent.  Element rules: left_boundary edge line: rule
                        allows? Edge line marks boundary of roadway; crossing is generally prohibited except
                        to avoid hazard? In India, edge line is not to be crossed? Might be allowed to cross?
                        Typically edge line is boundary, not to be crossed. But for a narrow road, maybe you
                        can use whole width. Hmm.  We need to recall traffic rule of region where photo taken.
                        India. Edge line: white solid line at edge of carriageway. Crossing is generally not
                        permitted? Actually edge line is just marking edge, you can cross to enter/exit. Might
                        be allowed.  But the instruction: for each boundary and each marking you listed,
                        recall traffic rule of region where photo was taken that applies to it, and say in one
                        sentence what it allows or prohibits for my car. If rule for this kind of marking and
                        general rule about all solid or broken lines both apply, rule for this kind of marking
                        decides.  So left_boundary edge_line solid white: rule: edge line marks edge of
                        roadway; you should stay within roadway but may cross to avoid obstruction. Might be
                        allowed to cross? Hmm.  Maybe simpler: edge line is not a lane line, so changing
                        across it is prohibited? Actually edge line is boundary of carriageway; you can cross
                        it to enter/exit property, but not to change lanes.  Given the road is narrow, my lane
                        is the whole carriageway. Changing left would be crossing edge line onto
                        sidewalk/parking area. That would be prohibited? Or not applicable? The boundary
                        governs change action. Changing left across edge line onto shoulder/sidewalk is
                        prohibited? Might be not applicable because no lane beyond.  The instruction:
                        change_left, change_right: leaving my lane across its left or right boundary in the
                        visible stretch (a lane change, overtaking, or moving onto whatever lies beyond:
                        another lane, a shoulder, a curb). So change left would be moving onto
                        sidewalk/parking area. Is that allowed? Probably prohibited.  But maybe the edge line
                        is not a prohibition, it's just edge. In many jurisdictions, you can cross edge line
                        to avoid hazard. But for lane change, maybe it's not applicable because there's no
                        lane beyond.  The schema says for each action: "not_applicable" = nothing in view
                        governs it (a side with no painted line and no curb; for turn_left...). For
                        change_left, if boundary is edge line, is that governing? The boundary governs change
                        action. So it is governed.  We need to decide allowed/prohibited.  In India, solid
                        white edge line: you should not cross it except in emergency. So change left/right is
                        prohibited.  Go straight: allowed (no arrow). Turn left/right/u_turn: not_applicable?
                        No arrow, no prohibited movement marking. So not_applicable? The instruction: for
                        turn_left, turn_right, u_turn: not_applicable = nothing in view governs it (no arrow
                        and no prohibited-movement marking in my lane; no waiting area and no two-way left-
                        turn lane). So yes not_applicable.  Enter_waiting_area: not_applicable.  But also
                        go_straight with no arrow is allowed.  So actions: change_left: prohibited (edge line)
                        change_right: prohibited (edge line) go_straight: allowed turn_left: not_applicable
                        turn_right: not_applicable u_turn: not_applicable enter_waiting_area: not_applicable
                        Advice: stay in lane, road is narrow with edge lines, no markings, proceed straight.
                        Check decision_check: consistent.  Now produce JSON.  Need fields:  scene: one or two
                        sentences lane_count: number ego_lane_index: number scene_evidence:
                        full/partial/insufficient  left_boundary: observation, color, pattern, near_line,
                        curb, role, evidence right_boundary: same  lane_markings: list (empty)  cross_check:
                        object with close_up, position, roles, markings, unseen, result  element_rules: list
                        of entries with element, rule_id null, meaning  action_reasons: object with keys
                        change_left, change_right, go_straight, turn_left, turn_right, u_turn,
                        enter_waiting_area each with reason string  decision_check: string  actions: object
                        with same keys with values allowed/prohibited/stop_first/not_applicable  advice:
                        string  Let's craft.  Scene: "The photo shows a narrow residential street in India
                        with buildings on both sides, the road ahead is straight and no intersection is
                        visible in the visible stretch." lane_count: 1? Could be 1 lane of my direction.
                        ego_lane_index: 1. scene_evidence: "full"? Might be partial because lane count
                        uncertain. Could be 1 lane. I'd say full.  Boundaries observation: Photo1 shows a
                        solid white line along the left edge of the carriageway next to parked scooters and a
                        dirt verge, continuing ahead; Photo2 shows the same solid white line close up next to
                        my lane. Similarly right.  Color white, pattern solid, near_line not_applicable, curb
                        no, role edge_line, evidence full.  Lane markings empty list.  Cross_check: close_up:
                        "the same in both photos" position: "lane count of 1 with ego lane index 1 agrees with
                        left and right edge lines" roles: "white solid lines are edge lines, consistent with
                        their position at the roadway edge" markings: "no markings are present in my lane in
                        either photo" unseen: "no" result: "consistent"  Element_rules: left_boundary: meaning
                        "An edge line marks the boundary of the carriageway; crossing it to leave the roadway
                        is generally prohibited except to avoid a hazard." right_boundary: same.
                        Action_reasons: change_left: "Left boundary is a solid white edge line; crossing the
                        roadway edge is prohibited." change_right: "Right boundary is a solid white edge line;
                        crossing the roadway edge is prohibited." go_straight: "No lane-use arrow or
                        prohibited-movement marking is in my lane, so proceeding straight is allowed."
                        turn_left: "No arrow or prohibited-movement marking governs a turn at the end of the
                        visible stretch." turn_right: same u_turn: same enter_waiting_area: "No left-turn
                        waiting area or two-way left-turn lane is visible."  Decision_check: "consistent"
                        Actions as above.  Advice: "Stay within the marked carriageway between the two white
                        edge lines; the road is narrow with no lane markings ahead, so continue straight and
                        do not cross the edge lines."  Make JSON valid.  Ensure lane_markings is empty array.
                        Element_rules entries: element: "left_boundary", rule_id: null, meaning: "..."  Ok.
                        Potential nuance: In India, traffic keeps left, so my lane is on left side of road.
                        The white line on left is edge line, right is edge line. Good.  Some might argue
                        lane_count is 2? Could be one lane each direction, but the road is not divided. The
                        lane count of my direction near bottom is 1. Good.  Evidence for boundaries: full.
                        Return JSON.  Let's output.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6824, out 3186, 18.98 s

idd__primary_d1_leftCamImgs_0000786 | lane | Test A | meta-muse-glimmer-30b
---------------------------------------------------------------------------
Step 1  Scene           Residential two-way street with no intersection visible ahead, my car is in the single
                        carriageway between edge lines with oncoming motorbikes ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line along the left edge of the asphalt, running straight ahead
                        next to the left side of the carriageway; Photo 2 shows the same white line close up
                        along the left side of the road just ahead of my car, with the line continuing ahead.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line along the right edge of the asphalt, running straight ahead
                        next to the right side of the carriageway; Photo 2 shows the same white line close up
                        along the right side of the road just ahead of my car, with the line continuing ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: lane count 1 and ego lane index 1 agree
                        with left and right edge lines | roles: white solid lines are edge lines, consistent
                        with leftmost/rightmost lane | markings: no markings in my lane, consistent | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: Edge line marks the edge of the carriageway; my car should stay within
                        the roadway and should not cross it except in an emergency.
Step 5  Rule            right_boundary: Edge line marks the edge of the carriageway; my car should stay within
                        the roadway and should not cross it except in an emergency.
Step 6  change_left     prohibited (correct): Left boundary is a white solid edge line; crossing the edge of
                        the carriageway is prohibited.
Step 6  change_right    prohibited: Right boundary is a white solid edge line; crossing the edge of the
                        carriageway is prohibited.
Step 6  go_straight     allowed (contested, correct): No lane-use arrow or prohibition in my lane; the
                        carriageway continues straight ahead.
Step 6  turn_left       not_applicable: No intersection or lane-use arrow visible ahead; no marking governs a
                        left turn.
Step 6  turn_right      not_applicable: No intersection or lane-use arrow visible ahead; no marking governs a
                        right turn.
Step 6  u_turn          not_applicable: No marking governs a U-turn and no intersection is visible.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Stay within the white edge lines and keep to the left; the road is narrow with
                        oncoming traffic ahead, so do not cross the edge lines or attempt a lane change.
Model's summary         This photo was taken in India, where traffic keeps to the left. Interpret my lane.
                        Photo 1 is whole dash-camera photo. Photo 2 is close-up of road just ahead of my car,
                        cut from Photo 1 and shown larger.  We need scene: road, what is ahead (intersection,
                        ramp, lane that ends). Count lanes of my direction near bottom of photo, and give
                        position of my lane counted from left (1 = leftmost lane of my direction).  From
                        photo: looks like a narrow residential street, two-way? There's a white line on left
                        and right of the road. The car is presumably behind camera? Wait "My car is the
                        vehicle that took the photo; its hood may be visible at the bottom of the photo." In
                        Photo 1, bottom is road ahead, no hood visible. Photo 2 is close-up. The road appears
                        to have two white lines marking the carriageway edges? Or is it a single lane each
                        direction? The road ahead shows two motorbikes coming towards camera? Wait direction:
                        traffic keeps to left in India. The camera is facing forward along road. The
                        motorbikes are ahead, coming towards camera? Actually they are in the lane ahead,
                        moving towards camera? Let's see: the motorbikes are on the road, facing the camera?
                        The motorbikes are oriented with front towards camera? The rider is facing camera? The
                        motorbike is facing the camera? The bike is coming towards the camera? Or is the
                        camera facing forward and the bikes are ahead going same direction? Wait the bikes
                        appear to be facing the camera, meaning they are coming towards the camera, i.e.,
                        opposite direction. But the road is narrow. Could be the camera is on a road and the
                        bikes are oncoming traffic. That would mean the lane of my car is the lane on the
                        right side of the image? Wait left side of image is left side of car. In India traffic
                        keeps left, so oncoming traffic would be on the right side of the road from driver's
                        perspective. Hmm.  Let's think: The photo shows a road with two white lines on both
                        sides of the asphalt. The asphalt is between the two white lines. The motorbikes are
                        on the asphalt, between the lines, and they appear to be facing the camera (i.e.,
                        coming towards). That would mean the camera is facing the oncoming direction? No, the
                        camera is mounted on a car facing forward. If the motorbikes are coming towards the
                        camera, they are oncoming traffic, so the camera is in the opposite lane. But the
                        camera's lane should be the lane straight ahead of my car, between nearest boundary on
                        its left and right. The boundaries are the white lines. So my lane is between the two
                        white lines. The motorbikes are in my lane but coming towards me? That can't be.
                        Alternative interpretation: The motorbikes are actually going away from the camera,
                        but perspective makes them look like facing camera? Let's examine: the motorbike with
                        red helmet, the bike's front is towards the camera? The bike's headlight is at front.
                        Hard to see. The bike appears to be facing away? Might be the rear of the bike is
                        visible? The red helmet rider is on a bike, the bike's rear is maybe towards camera?
                        Actually the bike's orientation: the rider is sitting, the bike's front is maybe
                        towards the camera? Usually you see the front of a bike when it's coming towards you.
                        The bike's rear would be visible if it's going away. The image is low resolution.
                        Might be the bikes are going away from camera, i.e., same direction as camera, but
                        they are in the opposite lane? Wait if traffic keeps left, and the road is two-way
                        with a central line? But there is no central line visible. The white lines are edge
                        lines.  Maybe the road is a one-way street? Or the camera is on a road and the bikes
                        are oncoming in the same physical space? Could be the road is narrow and the camera is
                        actually facing the opposite direction? No.  Alternative: The photo is taken from a
                        car that is driving, and the motorbikes are ahead of the car, going in the same
                        direction, but they appear to be facing the camera because the camera is behind them?
                        Wait if they are ahead, they'd be facing away from camera. So they'd be seen from
                        behind. The rider's back would be visible. The rider in purple is facing away? Hard to
                        tell.  Maybe the road is a two-lane road with no center marking, and the white lines
                        are edge lines. The motorbikes are in the oncoming lane, which is the same physical
                        lane as the camera's lane because it's a single lane each way sharing the same space?
                        Actually in a narrow road, the lanes are not separated. The white lines mark the edge
                        of the carriageway. So the road is one lane each direction, sharing the same width.
                        The motorbikes are oncoming, so they are in the lane that is opposite to the camera's
                        lane. But the camera's lane is also between the same two white lines? Wait the lane
                        straight ahead of my car is between the nearest boundary on its left and nearest
                        boundary on its right. The nearest boundary on left is the left white line, on right
                        is the right white line. So my lane is the whole width between the lines. The oncoming
                        traffic is also in that same space but opposite direction. So the lane is shared? Hmm.
                        Maybe the interpretation is that the road is a single carriageway with two-way
                        traffic, no lane markings in the middle, just edge lines. So my lane is the whole
                        carriageway, but the boundaries are the edge lines. The lane count of my direction
                        near the bottom of the photo: there is one lane of my direction (the whole width). The
                        ego lane index is 1 (leftmost and rightmost). The scene is a residential street with
                        no intersection ahead visible, just straight road.  The photo shows two motorbikes
                        coming towards the camera, meaning they are oncoming traffic. So the camera is driving
                        towards them. That means the camera is in the opposite direction of the bikes. So the
                        bikes are in the oncoming lane, which is the same physical space but opposite
                        direction. So the lane boundaries are the edge lines.  Thus lane_count = 1? Or maybe 2
                        lanes total (one each direction). But lane_count is lanes of my direction near the
                        bottom of the photo. So 1.  Ego_lane_index = 1 (only lane).  Scene evidence: full?
                        Might be partial because lane count uncertain? Could be 1.  Boundaries: left_boundary:
                        observation: Photo 1 shows a white solid line along left edge of road, next to my car,
                        continuing ahead. Photo 2 shows same white solid line close up. Color white, pattern
                        solid, curb? No raised curb, but there is a sidewalk/driveway. Curb maybe no. Role:
                        edge_line (edge of roadway). Evidence full.  Right_boundary: similar white solid line
                        on right edge. Color white, pattern solid, curb no, role edge_line.  Lane markings:
                        any arrows, words, symbols? None visible. No markings in my lane. So empty list.
                        Cross-check: close_up: same in both photos. Position: lane count 1, ego lane index 1
                        agrees with boundaries: left boundary is edge line meaning leftmost lane, right
                        boundary is edge line meaning rightmost lane. Roles: edge lines fit. Markings: none.
                        Unseen: none. Result consistent.  Element rules: left_boundary edge line: rule about
                        not crossing edge? In India, edge line is boundary of carriageway, crossing is allowed
                        to avoid obstacle? Might be prohibited to drive on shoulder. But rule: edge line marks
                        edge of roadway, do not cross unless necessary. So meaning: my car should stay within
                        the carriageway, crossing the edge line is prohibited except in emergency.  Similarly
                        right_boundary.  No markings.  Action reasons: change_left: boundary is left edge
                        line, solid white, edge line. Changing left would be leaving carriageway onto
                        sidewalk/driveway. Prohibited? Edge line is not a lane line, crossing edge is
                        generally prohibited. So change_left prohibited. change_right: similarly prohibited.
                        go_straight: no arrow, lane continues straight, allowed. turn_left: no arrow, not
                        applicable? Actually turn left at end of lane? No intersection visible. So not
                        applicable. turn_right: not applicable. u_turn: not applicable. enter_waiting_area:
                        not applicable.  But maybe turn left/right is not applicable because no intersection
                        ahead visible. The road goes straight ahead. So not applicable.  Decision check:
                        consistent.  Actions: change_left: prohibited change_right: prohibited go_straight:
                        allowed turn_left: not_applicable turn_right: not_applicable u_turn: not_applicable
                        enter_waiting_area: not_applicable  Advice: stay in lane, do not cross edge lines,
                        road is narrow with oncoming traffic.  Need JSON output with fields as specified.
                        Let's construct JSON.  scene: "Residential two-way street with no intersection visible
                        ahead, my car is in the single carriageway between edge lines, oncoming motorbikes
                        ahead." lane_count: 1, ego_lane_index: 1, scene_evidence: "full"  left_boundary:
                        observation: "Photo 1 shows a white line along the left edge of the asphalt, running
                        straight ahead next to the left side of the carriageway; Photo 2 shows the same white
                        line close up along the left side of the road just ahead of my car, with the line
                        continuing ahead." color: "white", pattern: "solid", curb: "no", role: "edge_line",
                        evidence: "full"  right_boundary: observation: "Photo 1 shows a white line along the
                        right edge of the asphalt, running straight ahead next to the right side of the
                        carriageway; Photo 2 shows the same white line close up along the right side of the
                        road just ahead of my car, with the line continuing ahead." color: "white", pattern:
                        "solid", curb: "no", role: "edge_line", evidence: "full"  lane_markings: [] (empty
                        list)  cross_check: close_up: "the same in both photos" position: "lane count 1 and
                        ego lane index 1 agree with left and right edge lines" roles: "white solid lines are
                        edge lines, consistent with leftmost/rightmost lane" markings: "no markings in my
                        lane, consistent" unseen: "no" result: "consistent"  element_rules: - element:
                        "left_boundary", rule_id: null, meaning: "Edge line marks the edge of the carriageway;
                        my car should stay within the roadway and should not cross it except in an emergency."
                        - element: "right_boundary", rule_id: null, meaning: "Edge line marks the edge of the
                        carriageway; my car should stay within the roadway and should not cross it except in
                        an emergency."  action_reasons: change_left: "Left boundary is a white solid edge
                        line; crossing the edge of the carriageway is prohibited." change_right: "Right
                        boundary is a white solid edge line; crossing the edge of the carriageway is
                        prohibited." go_straight: "No lane-use arrow or prohibition in my lane; the
                        carriageway continues straight ahead." turn_left: "No intersection or lane-use arrow
                        visible ahead; no marking governs a left turn." turn_right: "No intersection or lane-
                        use arrow visible ahead; no marking governs a right turn." u_turn: "No marking governs
                        a U-turn and no intersection is visible." enter_waiting_area: "No left-turn waiting
                        area or two-way left-turn lane is visible."  decision_check: "consistent"  actions:
                        change_left: "prohibited" change_right: "prohibited" go_straight: "allowed" turn_left:
                        "not_applicable" turn_right: "not_applicable" u_turn: "not_applicable"
                        enter_waiting_area: "not_applicable"  advice: "Stay within the white edge lines and
                        keep to the left; the road is narrow with oncoming traffic ahead, so do not cross the
                        edge lines or attempt a lane change."  Return JSON.  Make sure JSON keys match schema
                        exactly. The schema expects fields: scene, lane_count, ego_lane_index, scene_evidence,
                        left_boundary, right_boundary, lane_markings, cross_check, element_rules,
                        action_reasons, decision_check, actions, advice.  left_boundary and right_boundary
                        each have observation, color, pattern, near_line, curb, role, evidence. near_line is
                        required? It says near_line: only for solid_dashed... otherwise "not_applicable". So
                        include near_line: "not_applicable".  cross_check fields: close_up, position, roles,
                        markings, unseen, result.  element_rules entries: element, rule_id, meaning.
                        action_reasons entries: keys change_left etc.  actions entries: same keys.  Let's
                        output.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6824, out 3482, 19.16 s

idd__primary_d1_leftCamImgs_0002250 | lane | Test A | meta-muse-glimmer-30b
---------------------------------------------------------------------------
Step 1  Scene           A divided urban road with a raised concrete median, straight ahead with no
                        intersection visible. My car is on the left carriageway following a yellow auto
                        rickshaw. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows the left side of my lane bordered by a sidewalk with a low wall and a
                        parked white car; no painted line is visible along the edge. Photo 2 shows the same
                        road edge next to the sidewalk with no painted line visible, the auto rickshaw ahead
                        in the lane.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           Photo 1 shows the right side of my lane separated from the opposite carriageway by a
                        raised concrete block median; no painted line is visible at the edge of my lane. Photo
                        2 shows the same concrete block median immediately to the right of my lane with no
                        painted line visible.
                        none none, curb yes, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: lane count 1 and ego lane index 1 agree
                        with left edge and right median boundaries | roles: left edge with curb fits edge_line
                        role; right raised median fits center separation role | markings: no markings in my
                        lane in either photo, consistent | unseen: no attribute reported without visual
                        support | result: consistent
Step 5  Rule            left_boundary: The road edge with a curb marks the boundary of the roadway; leaving
                        the roadway onto the sidewalk is prohibited.
Step 5  Rule            right_boundary: The raised concrete median physically separates opposing traffic;
                        crossing it is prohibited.
Step 6  change_left     prohibited: left boundary is a road edge with a curb; leaving the roadway is
                        prohibited
Step 6  change_right    prohibited (contested, correct): right boundary is a raised concrete median; crossing
                        it is prohibited
Step 6  go_straight     allowed (contested, correct): no lane-use arrow or prohibition in my lane; continuing
                        straight along the lane is allowed
Step 6  turn_left       not_applicable: no arrow or prohibited-movement marking in my lane governs a turn at
                        the end; not applicable
Step 6  turn_right      not_applicable: no arrow or prohibited-movement marking in my lane governs a turn at
                        the end; not applicable
Step 6  u_turn          not_applicable: no arrow or prohibited-movement marking in my lane governs a U-turn at
                        the end; not applicable
Step 6  enter_waiting_areanot_applicable: no left-turn waiting area or two-way left-turn lane is visible; not
                          applicable
Step 7  Reflect         consistent
Advice                  Stay in the single left carriageway lane behind the auto rickshaw; the concrete median
                        prevents any right change and the curb prevents a left change, so continue straight.
Model's summary         This photo was taken in India, where traffic keeps to the left. Interpret my lane.
                        Photo 1 is whole dash-camera photo. Photo 2 is close-up of road just ahead of my car,
                        cut from Photo 1 and shown larger.  We need scene: road, what is ahead (intersection,
                        ramp, lane that ends). Count lanes of my direction near bottom of photo, and give
                        position of my lane counted from left (1 = leftmost lane of my direction).  From Photo
                        1: my car is presumably the dash cam. Hood may be visible at bottom. In photo, we see
                        a white car on left side of image (partially visible) and a yellow auto rickshaw ahead
                        in same lane? Wait the road is divided by a median with concrete blocks. My car is on
                        left side of median? The median is in center of image, separating two directions. The
                        auto rickshaw is ahead on left side of median, so that's my direction. The white/green
                        car is on the right side of median, which is opposite direction? Wait traffic keeps
                        left in India. So if median is between, the left side of image is my direction going
                        forward? The car is facing forward, hood at bottom. The road ahead is the lane with
                        auto rickshaw. The median is to the right of my lane. So my lane is on left side of
                        median. The right side of image shows oncoming traffic? Actually the white/green car
                        is on the right side of median, facing towards camera? No, the car is facing left?
                        Wait the car is on the right side of the median, its front is towards the camera? The
                        car is white with green front, facing left? The front is towards the left of image?
                        The car is on the right side of the median, its front is pointing towards the camera?
                        Let's see: the car is on the right side of the median, the front is visible,
                        headlights on left side of image? The car is facing towards the camera? Actually the
                        car is parked? Or it's on the opposite side of the road? The median is a raised curb.
                        The car is on the other side of the median, so it's either oncoming traffic or parked.
                        The car appears to be facing the camera? The front is towards the left side of the
                        image? The car's front is on the right side of the image? Hmm.  Better interpret: The
                        road is a divided road with a central median. My car is on the left carriageway, going
                        forward (away from camera). The auto rickshaw is ahead in my lane. The white/green car
                        is on the right carriageway, which is the opposite direction? Wait if traffic keeps
                        left, the carriageway on the right side of the median would be for traffic going the
                        opposite direction (towards the camera). But the white/green car appears to be facing
                        the camera? Actually the car's front is towards the left of the image, meaning it's
                        facing towards the camera? No, the car's front is on the right side of the image? The
                        car is on the right side of the median, its front is pointing to the left (towards the
                        camera's direction?). Let's see: the car's front is on the right side of the image,
                        the rear is to the left? No, the car is a front view: we see the front grille,
                        headlights. The car is on the right side of the median, and its front is facing
                        towards the left side of the image, which is towards the camera? Wait the camera is
                        looking forward along the road. The road ahead is to the top of the image. So forward
                        is up. The car is on the right side of the image, its front is pointing up? Actually
                        the car's front is pointing to the left? The car is oriented with its front towards
                        the left side of the image? No, the car is on the right side of the median, and its
                        front is facing the camera? Let's think: the median runs up the middle. The car is on
                        the right side of the median, so it's on the opposite carriageway. If traffic keeps
                        left, the opposite carriageway traffic would be coming towards the camera (i.e.,
                        moving down the image). So the car should be facing down the image (towards the
                        camera). That would mean its front is towards the bottom of the image. But the car we
                        see is facing up? Wait the car's front is visible, with headlights at the bottom of
                        the car in the image? The car is on the right side, its front is towards the bottom of
                        the image? Actually the car's front is at the bottom right of the image? The car is
                        positioned with its front towards the left? Hmm.  Maybe the white/green car is parked
                        on the side of the road on the right carriageway, facing the same direction as my car?
                        No.  Alternative interpretation: The median is a divider between two directions, but
                        the white/green car is on the same side as the camera? No, the median is between the
                        auto rickshaw and the white car. So they are on opposite sides of the median. So the
                        white car is on the opposite carriageway.  In India, traffic keeps left. So the
                        leftmost lane of my direction is the one next to the left edge of the road. The road
                        on the left side of the image has a white car parked on the left edge, and the auto
                        rickshaw is in the lane. So my lane is the lane with the auto rickshaw. How many lanes
                        of my direction near the bottom? It looks like one lane? The road appears to be a
                        single lane each direction, maybe with a shoulder. The left side has a sidewalk and
                        parked cars. The lane appears to be one lane wide. So lane_count = 1? Or maybe 2? The
                        road ahead looks wide enough for maybe one lane. The median is a concrete block
                        divider. So likely one lane per direction.  Ego lane index: counted from left (1 =
                        leftmost lane of my direction). If only one lane, index =1.  Scene: a divided urban
                        road with a central median, going straight ahead, no intersection visible. Maybe a
                        straight road.  Boundaries: left_boundary: left side of my lane. Photo 1 shows left
                        side: there is a curb? The left edge is a sidewalk with a low wall, maybe a curb. No
                        painted line visible. Photo 2 shows left side: the road edge near the sidewalk, no
                        painted line visible, maybe a curb. So left_boundary observation: Photo1 shows left
                        side is a sidewalk with a low wall and parked white car; no painted line visible.
                        Photo2 shows same, no line. Color: none. Pattern: none. Curb: yes? There is a raised
                        curb? The road edge appears to be a curb separating from sidewalk. Might be a curb.
                        Evidence partial.  Right_boundary: right side of my lane is the median with concrete
                        blocks. Photo1 shows a raised median with concrete blocks separating from opposite
                        carriageway. No painted line visible. Photo2 shows the median with concrete blocks. So
                        right_boundary is a physical barrier. Color: none. Pattern: none. Curb: yes (median).
                        Role: maybe center_line? Actually it's a median separating opposite directions, so
                        it's a center divider. But the boundary of my lane on the right is the edge of the
                        roadway adjacent to the median. Could be edge_line? Or center_line? The median is
                        between directions, so the boundary is the edge of my carriageway, which is a center
                        line? In a divided road, the boundary between directions is a median, not a painted
                        line. The role could be center_line? Or special? Might be edge_line? Hmm.  The lane is
                        bounded on the right by a physical median, not a painted line. So role maybe
                        center_line? Actually center line is between opposite directions. The median is the
                        physical separation. So role = center_line? Or other? Might be edge_line? The lane's
                        right boundary is the edge of the carriageway, which is adjacent to the median. Could
                        be considered a center_line.  Left boundary is the road edge, maybe edge_line.
                        Markings: any arrows, words, symbols in my lane? Photo2 close-up shows road surface
                        ahead, no markings visible. Photo1 shows road ahead, no arrows visible. So
                        lane_markings empty list.  Cross-check: close_up same? Photo1 and Photo2 show same.
                        Position: lane count 1, ego lane index 1 agrees with boundaries: left boundary is
                        edge, right boundary is median. Roles fit.  Markings none.  Unseen: no.  Result
                        consistent.  Element rules: left_boundary: edge_line with curb, rule allows? Edge line
                        is boundary of roadway, cannot cross? Actually edge line is not a lane line. Changing
                        across edge line onto shoulder may be prohibited? But we have curb.  Right_boundary:
                        median physical barrier, cannot cross.  No markings.  Action reasons:  change_left:
                        left boundary is road edge with curb, so prohibited? Or not applicable? Changing left
                        would be leaving roadway onto sidewalk. Prohibited.  change_right: right boundary is
                        median physical barrier, cannot cross. Prohibited.  go_straight: no arrow, lane
                        continues straight, allowed.  turn_left: no arrow, no marking, not_applicable? The
                        lane has no arrow, so turn left is not governed? Actually turn left at end of lane
                        would be possible? But no marking. The rule says when my lane has no arrow and no
                        prohibited-movement marking, turn_left is not_applicable. So not_applicable.
                        turn_right: not_applicable.  u_turn: not_applicable.  enter_waiting_area: no waiting
                        area. not_applicable.  Decision check consistent.  Advice: continue straight, cannot
                        change lanes due to median and curb.  Now produce JSON.  Need fields: scene,
                        lane_count, ego_lane_index, scene_evidence, left_boundary (observation, color,
                        pattern, near_line, curb, role, evidence), right_boundary same, lane_markings list,
                        cross_check (close_up, position, roles, markings, unseen, result), element_rules list,
                        action_reasons (change_left, change_right, go_straight, turn_left, turn_right, u_turn,
                        enter_waiting_area), decision_check, actions (same seven keys), advice.  Let's craft.
                        Scene: "A divided urban road with a raised concrete median, straight ahead with no
                        intersection visible. My car is on the left carriageway following a yellow auto
                        rickshaw." lane_count: 1, ego_lane_index:1, scene_evidence: "full"? Lane count can be
                        counted, ego lane index can be counted. Might be partial because far ahead not clear.
                        But seems full.  Left_boundary observation: "Photo 1 shows the left side of my lane
                        bordered by a sidewalk with a low wall and a parked white car; no painted line is
                        visible along the edge. Photo 2 shows the same road edge next to the sidewalk with no
                        painted line visible, the auto rickshaw ahead in the lane." color: none, pattern:
                        none, near_line: not_applicable, curb: yes, role: edge_line, evidence: partial (curb
                        visible but line not seen).  Right_boundary observation: "Photo 1 shows the right side
                        of my lane separated from the opposite carriageway by a raised concrete block median;
                        no painted line is visible at the edge of my lane. Photo 2 shows the same concrete
                        block median immediately to the right of my lane with no painted line visible." color:
                        none, pattern: none, near_line: not_applicable, curb: yes, role: center_line (or
                        other). Might be center_line. Evidence: full.  Lane_markings: empty list.
                        Cross_check: close_up: "the same in both photos". position: "lane count 1 and ego lane
                        index 1 agree with left edge and right median boundaries". roles: "left edge line with
                        curb fits edge_line role; right median fits center separation role". markings: "no
                        markings in my lane in either photo, consistent". unseen: "no attribute reported
                        without visual support". result: "consistent".  Element_rules: left_boundary: rule_id
                        null, meaning "The road edge with a curb marks the boundary of the roadway; leaving
                        the roadway onto the sidewalk is prohibited." right_boundary: "The raised concrete
                        median physically separates opposing traffic; crossing it is prohibited."
                        Action_reasons: change_left: "left boundary is a road edge with a curb; leaving the
                        roadway is prohibited". change_right: "right boundary is a raised concrete median;
                        crossing it is prohibited". go_straight: "no lane-use arrow or prohibition in my lane;
                        continuing straight along the lane is allowed". turn_left: "no arrow or prohibited-
                        movement marking in my lane governs a turn at the end; not applicable". turn_right:
                        same. u_turn: same. enter_waiting_area: "no left-turn waiting area or two-way left-
                        turn lane is visible; not applicable".  Decision_check: "consistent".  Actions:
                        change_left: "prohibited", change_right: "prohibited", go_straight: "allowed",
                        turn_left: "not_applicable", turn_right: "not_applicable", u_turn: "not_applicable",
                        enter_waiting_area: "not_applicable".  Advice: "Stay in the single left carriageway
                        lane behind the auto rickshaw; the concrete median prevents any right change and the
                        curb prevents a left change, so continue straight."  Return JSON.  Make sure JSON
                        valid.  Let's output.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6824, out 3606, 13.31 s

idd__primary_d1_leftCamImgs_0002357 | lane | Test A | meta-muse-glimmer-30b
---------------------------------------------------------------------------
Step 1  Scene           Urban divided road with a raised concrete block median, buildings and shops on both
                        sides, an auto rickshaw and a scooter ahead in the same direction, road continues
                        straight ahead with no intersection visible in the view. (lanes 1, mine 1, full)
Step 2  Left            Photo1 shows the left side of my lane is the roadway edge with parked motorcycles on
                        the sidewalk and a man standing at the edge; no painted line is visible. Photo2 shows
                        the same edge close-up with no painted line, motorcycles parked along the left and the
                        sidewalk/curb boundary at the extreme left of the frame.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo1 shows a raised concrete block median separating my direction from the opposite
                        direction on the right; no painted line is visible. Photo2 shows the same median
                        close-up with concrete blocks forming a physical barrier along the right side of my
                        lane.
                        none none, curb yes, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: lane count 1 and ego lane index 1 agree
                        with a left edge boundary and a right median/center boundary, i.e. my lane is the
                        leftmost and only lane of my direction | roles: left boundary is an edge of the
                        roadway with a curb, fitting edge_line; right boundary is a physical median separating
                        opposing traffic, fitting center_line | markings: no arrows, words, symbols or areas
                        are visible in my lane in either photo, consistent with an empty markings list |
                        unseen: no attributes were reported without being seen | result: consistent
Step 5  Rule            left_boundary: The roadway edge with a curb/sidewalk prohibits driving onto the
                        sidewalk or parking area and prohibits a lane change to the left.
Step 5  Rule            right_boundary: A raised concrete median is a physical center divider that prohibits
                        crossing to the opposite direction and prohibits a lane change to the right.
Step 6  change_left     prohibited: left boundary is a roadway edge with curb/sidewalk, crossing is prohibited
Step 6  change_right    prohibited (contested, correct): right boundary is a physical concrete median,
                        crossing is prohibited
Step 6  go_straight     allowed (contested, correct): no lane-use arrow or restriction is painted in my lane
                        and the road continues straight ahead
Step 6  turn_left       not_applicable: no arrow or prohibited-movement marking in my lane and no intersection
                        is visible to govern a turn
Step 6  turn_right      not_applicable: no arrow or prohibited-movement marking in my lane and no intersection
                        is visible to govern a turn
Step 6  u_turn          not_applicable: no arrow or prohibited-movement marking in my lane and no intersection
                        is visible to govern a U-turn
Step 6  enter_waiting_areanot_applicable: no left-turn waiting area or two-way left-turn lane is visible ahead
                          of or to the left of my lane
Step 7  Reflect         consistent
Advice                  Stay in your single lane between the sidewalk on the left and the concrete median on
                        the right; lane changes are not possible and you can proceed straight ahead.
Model's summary         This photo was taken in India, where traffic keeps to the left. Interpret my lane.
                        Photo 1 is whole dash-camera photo. Photo 2 is close-up of road just ahead of my car,
                        cut from Photo 1 and shown larger.  We need scene, lane_count, ego_lane_index,
                        scene_evidence.  From photo: road with median divider (concrete blocks). My car is on
                        left side of road? Traffic keeps left in India. So my lane is on left side of the
                        road, presumably the leftmost lane of my direction. The road appears to be a divided
                        road with a central median. On the right side of image is opposite direction? Wait
                        median is between. The road ahead: my lane is on left side of image, with parked
                        motorcycles on left edge. The median is on right side of my lane (to my right). So my
                        lane is leftmost lane of my direction, maybe only one lane? There is a scooter ahead,
                        auto rickshaw ahead. The road seems to be one lane each direction? Actually the left
                        side of image shows the road with no lane markings visible. The median is a raised
                        concrete divider. So my lane is bounded on left by edge of roadway (curb? maybe no
                        curb, just sidewalk). On right by the median (physical barrier). So lane count? Near
                        bottom of photo, my direction appears to have one lane (maybe two? but no markings).
                        Could be one lane. The opposite direction is on right side of median, with cars parked
                        on side. So lane count = 1? Or maybe 2? Let's see: the road ahead seems wide enough
                        for one lane. No lane lines visible. So lane_count = 1, ego_lane_index = 1.  Scene:
                        urban street with buildings, median divider, auto rickshaw ahead, no intersection
                        visible ahead, road continues straight.  Boundaries: left_boundary: observation:
                        Photo1 shows left side is edge of roadway with parked motorcycles on sidewalk, no
                        painted line visible, maybe a faint edge. Photo2 shows same, no line, just curb?
                        There's a small curb at edge. Might be edge_line. Color none, pattern none, curb yes?
                        There's a raised edge? The left side appears to be a sidewalk with motorcycles parked,
                        maybe a curb. Could be edge_line with curb yes. Right_boundary: median divider,
                        physical barrier. Photo1 shows concrete block median separating directions. Photo2
                        shows same. So right_boundary is median. Color none, pattern none, curb yes (physical
                        barrier). Role: left_boundary is edge_line (edge of roadway). Right_boundary is
                        center_line? Actually median separates opposing traffic, so it's a center divider.
                        Could be center_line with physical barrier. Role: center_line? Or special? Might be
                        center_line.  Markings: lane_markings: any arrows? No. No words. No stop line. So
                        empty list.  Cross-check: close_up same. Position: lane count 1, ego lane index 1
                        matches boundaries: left is edge, right is center/median, so leftmost.  Roles: left
                        edge line fits, right is center with physical barrier.  Markings none.  Unseen: none.
                        Result consistent.  Element_rules: left_boundary edge_line: rule allows? Edge line is
                        boundary of roadway, crossing is prohibited? Typically you cannot drive onto sidewalk.
                        So change_left prohibited? Actually change_left would be moving left across edge into
                        sidewalk/parking. Prohibited.  Right_boundary center_line with physical barrier:
                        cannot cross. So change_right prohibited.  No markings.  Action reasons:  change_left:
                        boundary is edge_line with curb, crossing prohibited.  change_right: boundary is
                        median physical barrier, crossing prohibited.  go_straight: no arrow, lane continues,
                        allowed.  turn_left: no arrow, not applicable? Actually turn left at end? No
                        intersection visible. So not_applicable.  turn_right: not_applicable.  u_turn:
                        not_applicable.  enter_waiting_area: not_applicable.  Decision check consistent.
                        Actions: change_left prohibited, change_right prohibited, go_straight allowed,
                        turn_left not_applicable, turn_right not_applicable, u_turn not_applicable,
                        enter_waiting_area not_applicable.  Advice: stay in lane, cannot change lanes due to
                        median and sidewalk, proceed straight.  Need JSON output with fields.  Let's craft.
                        scene: "Urban divided road with concrete median divider, buildings on both sides, auto
                        rickshaw and scooter ahead, road continues straight ahead with no intersection
                        visible."  lane_count: 1  ego_lane_index: 1  scene_evidence: "full" (?) lane count can
                        be counted? Might be partial because no markings. But we can see one lane. I'd say
                        full.  left_boundary: observation: "Photo1 shows left side of my lane is the roadway
                        edge with parked motorcycles on the sidewalk; no painted line is visible, the edge
                        appears as a curb/sidewalk boundary. Photo2 shows the same edge close-up with no
                        painted line, motorcycles parked along the left and a man standing at the edge."
                        color: none, pattern: none, curb: yes, role: edge_line, evidence: partial? maybe full?
                        color none visible, pattern none, curb yes. evidence full.  right_boundary:
                        observation: "Photo1 shows a raised concrete block median separating my direction from
                        oncoming traffic on the right; no painted line is visible. Photo2 shows the same
                        median close-up with concrete blocks forming a physical barrier." color: none,
                        pattern: none, curb: yes, role: center_line, evidence: full.  lane_markings: [] empty
                        list.  cross_check: close_up: "the same in both photos". position: "lane count 1 and
                        ego lane index 1 agree with left edge and right median boundaries". roles: "left edge
                        line fits edge role, right median fits center role with physical barrier". markings:
                        "no markings present, consistent". unseen: "no attributes reported without seeing".
                        result: "consistent".  element_rules: entries for left_boundary and right_boundary.
                        left_boundary: rule_id null, meaning "Edge of roadway with curb prohibits driving onto
                        sidewalk or parking area."  right_boundary: meaning "Physical median divider prohibits
                        crossing to opposite direction."  action_reasons: change_left: "left boundary is
                        roadway edge with curb, crossing prohibited". change_right: "right boundary is
                        physical median, crossing prohibited". go_straight: "no lane-use arrow or restriction
                        in my lane, road continues straight". turn_left: "no arrow or prohibited-movement
                        marking in my lane and no intersection visible". turn_right: same. u_turn: same.
                        enter_waiting_area: "no left-turn waiting area or two-way left-turn lane visible".
                        decision_check: "consistent"  actions: as above.  advice: "Stay in your single lane
                        between the sidewalk on the left and the concrete median on the right; lane changes
                        are not possible and you can proceed straight ahead."  Return JSON.  Make sure JSON
                        keys match schema: scene, lane_count, ego_lane_index, scene_evidence, left_boundary,
                        right_boundary, lane_markings, cross_check, element_rules, action_reasons,
                        decision_check, actions, advice.  left_boundary and right_boundary each have
                        observation, color, pattern, near_line, curb, role, evidence.  near_line:
                        "not_applicable"  cross_check fields: close_up, position, roles, markings, unseen,
                        result.  element_rules: list of objects with element, rule_id, meaning.
                        action_reasons: object with keys change_left, change_right, go_straight, turn_left,
                        turn_right, u_turn, enter_waiting_area.  actions: object with same keys values
                        allowed/prohibited/stop_first/not_applicable.  Let's produce.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6824, out 2467, 15.08 s
```
