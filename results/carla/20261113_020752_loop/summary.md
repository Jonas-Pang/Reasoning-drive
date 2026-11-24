# CARLA closed-loop run

Map Town10HD_Opt, weather ClearNoon, region US, prompt prompts/v3, model gpt-6.1-sol, seed 6216, started 20261113_020752.

## Per test (one request = one boundary line in one frame)

| Test | Requests | Answered | Marking type correct | Cross line correct | Unsafe | Over-cautious | Mean latency (s) | Cost (USD) |
|---|---|---|---|---|---|---|---|---|
| A | 40 | 40 | 40/40 | 37/40 | 2 | 1 | 4.77 | 0.322 |
| B | 40 | 40 | 40/40 | 40/40 | 0 | 0 | 4.45 | 0.4543 |

By marking type, Test A:

| Marking (truth) | n | Type correct | Cross line correct |
|---|---|---|---|
| white_dashed | 20 | 20 | 19 |
| white_solid | 8 | 8 | 8 |
| yellow_double_solid | 10 | 10 | 10 |
| yellow_solid | 2 | 2 | 0 |

By marking type, Test B:

| Marking (truth) | n | Type correct | Cross line correct |
|---|---|---|---|
| white_dashed | 20 | 20 | 20 |
| white_solid | 8 | 8 | 8 |
| yellow_double_solid | 10 | 10 | 10 |
| yellow_solid | 2 | 2 | 2 |

## Test A vs Test B on the same lines (cross line)

40 pairs: both right 37, only A right 0, only B right 3, both wrong 0.

## Closed loop (lane changes decided by Test B)

- Decision points: 20
- Lane change wanted and a lane available: 13
- Allowed by the system: 13; lane change started: 13, completed: 6
- Blocked although the rules allow it: 0
- Wanted to cross a prohibited line: 5; blocked by the system: 5
- Allowed although the rules prohibit it: 0
- Lines crossed (lane invasion sensor): {'white_dashed': 32}
- Prohibited lines crossed: 0
