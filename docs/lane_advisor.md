# Lane advisor: the deployed system (Module 8 deployment, Module 9 monitoring and feedback)

Added 2026-11-18. The research console (`/`, `/project`, `/review`) stays as it was; `/app` is the page for users.

## What it does

A driver (or a planner module) gives one dash-camera photo and the region. The service answers, in a fixed format,
what the two lines of the ego lane are and which of 7 actions are allowed, prohibited or not applicable, with the rule
passages it used. Before the answer is shown, a verification layer checks it; anything suspicious is marked
**Needs human review**. Users can rate every answer; the ratings feed the monitoring and the improvement loop.

```
photo + region ──► input checks ──► prompt builder ──► vision-language model ──► schema-constrained JSON
 (upload)           type, size,      rules of the        Gemma 4 31B             (7 actions, 2 lines,
                    re-encode,       region (Test B),     (NaviGator or           markings, cited rules)
                    no metadata      lane_v4c procedure    Ollama) or GPT              │
                                                                                       ▼
 feedback ◄── page /app ◄── audit log ◄── verification layer (guard.py): rule table on the model's own
 (feedback.csv)   (analyze /     (predictions.jsonl)   lines → agreement, unsafe direction, visibility,
      │           feedback /                            image brightness → needs_review
      ▼           monitor)                 │
 Prometheus /metrics ──► Grafana dashboard "Lane advisor – monitoring" + 4 alert rules
      │
      ▼
 scripts/feedback_report.py ──► review queue / label fixes / prompt changes ──► re-run frozen test set ──► release
```

## Components

| Part | File | Role |
|---|---|---|
| Page | `reasoning_drive/web/static/app.{html,js,css}` | Analyze · Feedback · Monitor tabs |
| API | `reasoning_drive/web/server.py` | `GET /app`, `/api/app/info`, `/api/app/examples`, `/api/app/summary`; `POST /api/upload`, `/api/app/predict`, `/api/feedback` |
| Model call | `reasoning_drive/agent/lane.py`, `client.py` | prompt `lane_v4c`, JSON schema `configs/schemas/lane_schema.json` (answers can only be the labelling options) |
| Verification | `reasoning_drive/web/guard.py` | rule check without a label, unsafe-direction check, visibility flags, brightness |
| Logs | `reasoning_drive/web/feedback.py` | `results/app/predictions.jsonl` (audit), `results/app/feedback.csv` |
| Metrics | `reasoning_drive/web/metrics.py` | `app_*` metrics at `/metrics` |
| Dashboard, alerts | `deploy/grafana/dashboards/app.json`, `deploy/grafana/provisioning/alerting/rules.yml` | made by `claude_analysis/deploy_src/make_grafana.py` |
| Analysis | `scripts/feedback_report.py`, `scripts/replay_feedback.py` | feedback report; test-set replay as simulated reviewer feedback |

## Run it

```
cp .env.example .env            # set GRAFANA_ADMIN_PASSWORD, NAVIGATOR_API_KEY (or OPENAI_API_KEY + LANE_API_PROFILE)
docker compose up --build
```
Lane advisor http://localhost:8770/app · Grafana http://localhost:3000 · Prometheus http://localhost:9090.
Without Docker: `python main.py web --api nav_gemma4_31b_bf16 --lane-prompt lane_v4c` (add `--mock` for made-up answers).
Without any key, choose **Saved answer (offline)**: the page shows the answer the main configuration gave in the frozen
test run, and the verification, logging, feedback and metrics work the same way.

## Metrics (Prometheus) and alerts (Grafana)

| Metric | Type | Meaning |
|---|---|---|
| `app_predictions_total{region,test,mode,needs_review}` | counter | answers given |
| `app_latency_seconds{mode}` | histogram | time to answer |
| `app_rule_agreement{region}` | histogram | proxy accuracy without ground truth (see below) |
| `app_rule_disagreements_total{region,action,direction}` | counter | unsafe / cautious disagreements with the rule table |
| `app_evidence_flags_total{flag}` | counter | partly visible lines, model errors |
| `app_input_brightness` | histogram | data drift (night, glare) |
| `app_feedback_total{region,rating,source}` | counter | feedback (as `gradio_feedback_total` in the course example) |
| `app_feedback_actions_total{region,action,verdict}`, `app_feedback_lines_total{region,side,verdict}` | counter | right / wrong per action and line |
| `app_feedback_comment_total{region,rating,excerpt,themes}` | counter | comment table in Grafana |

Alert rules: rule agreement < 0.85 (15 min), more than 30 % of feedback bad (1 h), latency p90 > 60 s, any model error.

**Training/evaluation metrics vs monitoring metrics.** With labels (the frozen test set): action accuracy, line
accuracy, unsafe errors (label prohibits, answer allows), McNemar tests between configurations. In production there is
no label, so the service watches proxies: rule agreement, needs-review rate, user feedback, latency, input drift.

## What the replay showed (test set, gemma4:31b + lane_v4c, Test B, China + United States, 232 photos)

`python scripts/replay_feedback.py --test B` then `python scripts/feedback_report.py` (results/app/feedback_report.md):
102 of 232 answers would be rated bad (not all 7 actions right); wrong-rate per action: change right 30 %,
change left 22 %, U-turn 7 %, turns 5–6 %, straight 3 %. The verification layer flagged 5 answers; 4 of them were bad
(precision 80 %), but it caught only 4 % of the bad answers. Reason: the model's reasoning is self-consistent, its
errors are perception errors (solid read as dashed, the most frequent comment theme), and a rule check on its own
perception cannot see them. This matches the experiments and points to the next guard: a second look at the
near-field crop or several video frames, or a lane-line detector, to check the lines themselves.

## Compliance and security

- Data licences: images are sent to a model only for collections listed in `configs/experiment.yaml` `send_to_api`
  (UK LingoQA and India IDD stay off until the owner accepts their terms, so the page has no UK/IN examples).
- UF policy: on UF resources only models from allowed countries (Gemma 4 on HiPerGator or NaviGator; no Qwen/GLM/Kimi).
- Uploads: type and size checked, decoded and written again without metadata (no GPS), deleted when the service stops;
  the audit log keeps the answer, not the photo.
- Keys only in `.env`, passed to the container as environment variables; image runs as a non-root user; ports bound to
  127.0.0.1; Grafana password required, sign-up and anonymous access off.
- Reproducibility: every live answer records model, prompt folder and, for batch runs, the frozen protocol
  (`configs/lane_protocol__*.json`: model digest, prompt hashes, seed 6216, temperature 0).

## CI/CD (proposed)

On every push: `python main.py selftest` (mock mode, no API), schema and rule-table checks, `docker build`, image scan
(e.g. `docker scout` / Trivy); on a tag: re-run the frozen dev set with the release candidate and block the release if
action accuracy or unsafe errors are worse than the last release (McNemar), then push the image.
