# CARLA closed-loop run

Map Town10HD_Opt, weather ClearNoon, region US, prompt prompts/v3, model gpt-6.1-sol, seed 6216, started 20261113_020404.

## Per test (one request = one boundary line in one frame)

| Test | Requests | Answered | Marking type correct | Cross line correct | Unsafe | Over-cautious | Mean latency (s) | Cost (USD) |
|---|---|---|---|---|---|---|---|---|
| A | 6 | 6 | 6/6 | 6/6 | 0 | 0 | 5.69 | 0.048 |
| B | 6 | 6 | 6/6 | 6/6 | 0 | 0 | 4.5 | 0.0678 |

By marking type, Test A:

| Marking (truth) | n | Type correct | Cross line correct |
|---|---|---|---|
| white_dashed | 3 | 3 | 3 |
| white_solid | 1 | 1 | 1 |
| yellow_double_solid | 2 | 2 | 2 |

By marking type, Test B:

| Marking (truth) | n | Type correct | Cross line correct |
|---|---|---|---|
| white_dashed | 3 | 3 | 3 |
| white_solid | 1 | 1 | 1 |
| yellow_double_solid | 2 | 2 | 2 |

## Test A vs Test B on the same lines (cross line)

6 pairs: both right 6, only A right 0, only B right 0, both wrong 0.

## Closed loop (lane changes decided by Test B)

- Decision points: 3
- Lane change wanted and a lane available: 2
- Allowed by the system: 2; lane change started: 2, completed: 1
- Blocked although the rules allow it: 0
- Wanted to cross a prohibited line: 1; blocked by the system: 1
- Allowed although the rules prohibit it: 0
- Lines crossed (lane invasion sensor): {'white_dashed': 4}
- Prohibited lines crossed: 0
