"""Prometheus metrics of the demo page, served at GET /metrics (read by Prometheus in docker compose).

Optional: without the prometheus_client package the page works as before and /metrics answers 404.
The counters start at zero when the page starts. They describe the use of the page (questions on the page and
batch runs started from it), not the experiment: the experiment's numbers are the saved runs in results/runs/.
"""
from __future__ import annotations

PATHS = {"/", "/index.html", "/api/config", "/api/items", "/api/image", "/api/prompt", "/api/progress", "/api/runs", "/api/run",
         "/api/compare", "/api/ask", "/api/saved", "/api/ask_stream", "/api/upload", "/api/passages", "/api/run_records",
         "/api/record", "/review", "/api/review/items", "/api/review/effect", "/api/review/decide", "/metrics", "/healthz",
         "/app", "/api/app/info", "/api/app/examples", "/api/app/predict", "/api/app/summary", "/api/feedback"}


class DemoMetrics:
    def __init__(self):
        from prometheus_client import CollectorRegistry, Counter, Gauge, Histogram, Info
        self.registry = r = CollectorRegistry()
        # task: lane (the whole lane) or marking (the single-marking task of Milestone 4)
        self.answers = Counter("demo_answers", "Answers, by where they were asked (page or batch run) and outcome",
                               ["task", "source", "test", "region", "outcome"], registry=r)
        self.latency = Histogram("demo_model_latency_seconds", "Time until the model answered (new API calls only)", ["task", "test"],
                                 buckets=(1, 2, 5, 10, 15, 20, 30, 45, 60, 90, 120), registry=r)
        self.tokens = Counter("demo_tokens", "Tokens of new API calls", ["task", "test", "kind"], registry=r)
        self.cost = Counter("demo_cost_usd", "Estimated cost of new API calls in US dollars", ["task", "test"], registry=r)
        self.checks = Counter("demo_label_checks", "Answers compared with the final label (output1 = the lane or the marking, output2 = the actions)",
                              ["task", "source", "test", "region", "output", "result"], registry=r)
        self.unsafe = Counter("demo_unsafe_errors", "The label prohibits an action that the answer allows", ["task", "source", "test", "region"], registry=r)
        self.issues = Counter("demo_consistency_issues", "Contradictions inside an answer, found without the label", ["task", "test"], registry=r)
        self.actions = Counter("demo_action_values", "Values of the actions in the answers", ["task", "test", "region", "action", "value"], registry=r)
        self.batches = Counter("demo_batch_runs", "Batch runs started from the page", ["task", "test", "region", "mode"], registry=r)
        self.running = Gauge("demo_batch_running", "1 while a batch run started from the page is going", registry=r)
        self.http = Counter("demo_http_requests", "Requests to the page", ["method", "path", "code"], registry=r)
        self.info = Info("demo", "Settings the page is running with", registry=r)
        # ---- lane advisor (/app), Claude 2026-11-18: monitoring without ground truth + user feedback
        self.app_predictions = Counter("app_predictions", "Answers given on /app", ["region", "test", "mode", "needs_review"], registry=r)
        self.app_latency = Histogram("app_latency_seconds", "Time to answer on /app (live mode: model call; saved mode: lookup)",
                                     ["mode"], buckets=(0.5, 1, 2, 5, 10, 20, 30, 45, 60, 90, 120), registry=r)
        self.rule_agreement = Histogram("app_rule_agreement", "Share of decided actions on which the model agrees with the rule table applied to the lines it saw",
                                        ["region"], buckets=(0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 1.0), registry=r)
        self.rule_agreement_last = Gauge("app_rule_agreement_last", "Rule agreement of the last answer", ["region"], registry=r)
        self.rule_disagreements = Counter("app_rule_disagreements", "Actions where the model and the rule table disagree",
                                          ["region", "action", "direction"], registry=r)
        self.flags = Counter("app_evidence_flags", "Partly visible lines, model errors and other flags of an answer", ["flag"], registry=r)
        self.brightness = Histogram("app_input_brightness", "Mean brightness of the photos (data drift: night, glare)",
                                    buckets=(20, 40, 60, 80, 100, 120, 140, 160, 200, 255), registry=r)
        self.fb = Counter("app_feedback", "Feedback on /app", ["region", "rating", "source"], registry=r)
        self.fb_actions = Counter("app_feedback_actions", "Feedback per action", ["region", "action", "verdict"], registry=r)
        self.fb_lines = Counter("app_feedback_lines", "Feedback per boundary line", ["region", "side", "verdict"], registry=r)
        self.fb_comment = Counter("app_feedback_comment", "Comments (first 50 characters), as in the course example",
                                  ["region", "rating", "excerpt", "themes"], registry=r)
        # ---- video input of /app (Claude 2026-11-18, web/video.py)
        self.video_jobs = Counter("app_video_jobs", "Videos analysed on /app, by outcome and model", ["state", "model", "test"], registry=r)
        self.video_frames = Counter("app_video_frames", "Frames analysed from videos", ["kind"], registry=r)
        self.video_seconds = Histogram("app_video_job_seconds", "Time to analyse one video (sampling + all frames)",
                                       buckets=(5, 10, 30, 60, 120, 180, 300, 600, 1200), registry=r)
        self.video_verdicts = Counter("app_video_verdicts", "Intended or executed manoeuvres checked against the frames",
                                      ["kind", "action", "verdict"], registry=r)
        self.video_attribution = Counter("app_video_attribution", "Executed manoeuvres with ground truth: who is at fault",
                                         ["attribution"], registry=r)

    @classmethod
    def create(cls) -> "DemoMetrics | None":
        try:
            return cls()
        except ImportError:
            return None

    def settings(self, cfg: dict) -> None:
        a = cfg["api"]
        self.info.info({"mode": "mock" if cfg.get("mock") else "real", "model": str(a.get("model", "")),
                        "reasoning_effort": str(a.get("reasoning_effort")), "prompt": str(cfg["prompt"]["dir"])})

    def request(self, method: str, path: str, code: int) -> None:
        p = "/static" if path.startswith("/static/") else path if path in PATHS else "other"
        self.http.labels(method, p, str(code)).inc()

    def answer(self, cfg: dict, rec: dict, source: str, task: str = "marking") -> None:
        from ..agent.runner import cost_of
        test, region = rec.get("test", "?"), rec.get("region", "?")
        ans, resp = rec.get("answer"), rec.get("response") or {}
        outcome = ("api_error" if rec.get("error") else "parse_error" if not ans else "cached" if rec.get("cached")
                   else "mock" if rec.get("mock") else "answered")
        self.answers.labels(task, source, test, region, outcome).inc()
        usage = resp.get("usage") or {}
        if outcome == "answered":
            self.latency.labels(task, test).observe(float(resp.get("latency_s") or 0))
            self.tokens.labels(task, test, "input").inc(usage.get("input_tokens", 0) or 0)
            self.tokens.labels(task, test, "output").inc(usage.get("output_tokens", 0) or 0)
            self.cost.labels(task, test).inc(cost_of(cfg, usage, resp.get("model")))
        if not ans:
            return
        for a, v in (ans.get("actions") or {}).items():
            self.actions.labels(task, test, region, a, str(v)).inc()
        score = rec.get("score") or {}
        self.issues.labels(task, test).inc(len(score.get("consistency") or []))
        # output1: the whole lane identified (lane task) or the marking type (single-marking task)
        for out, v in (("output1", score.get("lane") if task == "lane" else score.get("output1")), ("output2", score.get("output2"))):
            self.checks.labels(task, source, test, region, out, "not_scored" if v is None else "correct" if v else "wrong").inc()
        self.unsafe.labels(task, source, test, region).inc(len(score.get("unsafe") or []))

    # ---- lane advisor (/app)
    def app_prediction(self, rec: dict, check: dict, mode: str, seconds: float) -> None:
        region, test = rec.get("region", "?"), rec.get("test", "?")
        self.app_predictions.labels(region, test, mode, str(bool(check.get("needs_review"))).lower()).inc()
        self.app_latency.labels(mode).observe(float(((rec.get("response") or {}).get("latency_s") if mode == "live" else None) or seconds))
        rc = check.get("rule_check") or {}
        if rc.get("agreement") is not None:
            self.rule_agreement.labels(region).observe(rc["agreement"])
            self.rule_agreement_last.labels(region).set(rc["agreement"])
        for d in rc.get("disagreements") or []:
            direction = "unsafe" if d["action"] in (rc.get("unsafe_direction") or []) else "cautious" if d["model"] == "prohibited" else "other"
            self.rule_disagreements.labels(region, d["action"], direction).inc()
        for f in check.get("flags") or []:
            self.flags.labels(f).inc()
        b = (check.get("image") or {}).get("brightness")
        if b is not None:
            self.brightness.observe(b)

    def feedback(self, row: dict) -> None:
        region, rating = row.get("region") or "?", row.get("rating") or "none"
        self.fb.labels(region, rating, row.get("source") or "user").inc()
        for k, v in row.items():
            if k.startswith("act_") and v:
                self.fb_actions.labels(region, k[4:], v).inc()
        for side in ("left", "right"):
            if row.get(f"{side}_line"):
                self.fb_lines.labels(region, side, row[f"{side}_line"]).inc()
        if row.get("comment"):
            self.fb_comment.labels(region, rating, row["comment"][:50], row.get("themes") or "").inc()

    def video_job(self, job: dict) -> None:
        self.video_jobs.labels(job.get("state", "?"), job.get("model", "?"), job.get("test", "?")).inc()
        for f in job.get("frames") or []:
            self.video_frames.labels(f.get("kind", "?")).inc()
        if job.get("seconds") is not None:
            self.video_seconds.observe(float(job["seconds"]))
        ic = job.get("intent_check")
        if ic:
            self.video_verdicts.labels("intent", ic["action"], ic["verdict"]).inc()
        for e in job.get("event_checks") or []:
            self.video_verdicts.labels("event", e["action"], e["verdict"]).inc()
            if e.get("attribution"):
                self.video_attribution.labels(e["attribution"]).inc()

    def seed_predictions(self, preds: list) -> None:
        """Count the answers already in results/app/predictions.jsonl when the page starts."""
        for p in preds:
            region = p.get("region") or "?"
            self.app_predictions.labels(region, p.get("test") or "?", p.get("mode") or "?", str(bool(p.get("needs_review"))).lower()).inc()
            if p.get("rule_agreement") is not None:
                self.rule_agreement.labels(region).observe(p["rule_agreement"])
            if (p.get("image") or {}).get("brightness") is not None:
                self.brightness.observe(p["image"]["brightness"])

    def seed_feedback(self, rows: list) -> None:
        """Count the feedback already in results/app/feedback.csv when the page starts (Grafana shows all of it)."""
        for row in rows:
            self.feedback(row)

    def exposition(self) -> tuple[bytes, str]:
        from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
        return generate_latest(self.registry), CONTENT_TYPE_LATEST
