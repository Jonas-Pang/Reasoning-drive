# Feedback report (232 feedback rows, source: all)

## Ratings by region

| region | good | bad | bad rate |
|---|---|---|---|
| CN | 62 | 62 | 50 % |
| US | 68 | 40 | 37 % |

## Wrong rate per action (right + wrong verdicts)

| action | wrong | judged | wrong rate |
|---|---|---|---|
| change_left | 50 | 232 | 22 % |
| change_right | 69 | 232 | 30 % |
| go_straight | 8 | 232 | 3 % |
| turn_left | 12 | 232 | 5 % |
| turn_right | 13 | 232 | 6 % |
| u_turn | 17 | 232 | 7 % |
| enter_waiting_area | 3 | 232 | 1 % |

| line | wrong | judged | wrong rate |
|---|---|---|---|
| left | 88 | 232 | 38 % |
| right | 72 | 232 | 31 % |

## Verification layer vs feedback

The 'needs review' flag is set without a label (rule check, visibility). Treated as a detector of answers users rate bad:

- flagged and bad (caught): 4 · flagged but good: 1 · not flagged but bad (missed): 98 · not flagged, good: 129
- recall (bad answers caught) = 4 %, precision (flagged answers that were bad) = 80 %
- bad rate among flagged = 80 % vs not flagged = 43 %

## Comment themes (keyword coding)

| theme | comments | example |
|---|---|---|
| solid_vs_dashed | 113 | the left line is dashed, not solid; the right line is yellow, not white (line colour); the |
| too_cautious | 42 | the left line is dashed, not solid; change left should be allowed (too cautious) |
| unsafe | 42 | the left side is a bus / special lane; change left should be prohibited (unsafe); u turn:  |
| bus_or_special_lane | 24 | the left line is dashed, not solid; the right line is yellow, not white (line colour); the |
| line_color | 14 | the left line is dashed, not solid; the right line is yellow, not white (line colour); the |
| arrow_or_turn | 13 | the left side is a bus / special lane; change left should be prohibited (unsafe); u turn:  |

| theme | CN | US |
|---|---|---|
| solid_vs_dashed | 71 | 42 |
| too_cautious | 18 | 24 |
| unsafe | 29 | 13 |
| bus_or_special_lane | 22 | 2 |
| line_color | 14 | 0 |
| arrow_or_turn | 8 | 5 |

(scikit-learn not installed: clustering skipped)
