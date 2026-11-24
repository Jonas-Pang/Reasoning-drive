# Deployment with Docker

The project runs in a container built from the `Dockerfile`: Python 3.11, the pinned packages, `main.py` and the package `reasoning_drive/`, the settings (`configs/`), the prompts and the countries' rules (`regulations/`). Anyone with Docker gets the same environment with one command, on macOS, Windows or Linux, without installing Python or the packages. Docker Compose starts three containers together:

```
browser ──8770──> demo      the web page (python main.py web) ──HTTPS──> OpenAI API (real mode only)
                   │ /metrics
                   v
                prometheus  reads the metrics every 15 s ──9090──> browser
                   │
                   v
                grafana     dashboard "Reasoning Driving · demo page" ──3000──> browser
```

| File | Purpose |
|---|---|
| `Dockerfile` | how the image is built |
| `.dockerignore` | the build sees only `main.py`, the package, the settings, the prompts, the rules and the lock file; `.env`, images, datasets, results and PDFs in `regulations/inbox/` stay out |
| `docker-compose.yml` | the three services, the folders they see, their ports and limits |
| `deploy/requirements-docker.txt`, `deploy/requirements-docker.lock` | packages of the image; the lock pins every version and file hash |
| `deploy/prometheus.yml` | what Prometheus reads |
| `deploy/grafana/` | data source and dashboard, loaded when Grafana starts |
| `reasoning_drive/web/metrics.py` | the metrics of the web page (GET `/metrics`) |

## Start

Requires Docker Desktop (or Docker Engine with the Compose plugin). In `.env` (copy of `.env.example`):

* `GRAFANA_ADMIN_PASSWORD`: a password of your choice (required);
* `OPENAI_API_KEY`: for real answers;
* `DATASETS_ROOT`: the folder with the UF, bdd100k and culane workspaces, so the labeled images can be shown.

```bash
docker compose up --build        # first time: builds the image (a few minutes), then starts the three containers
```

| Address | What |
|---|---|
| http://localhost:8770 | demo page |
| http://localhost:8770/project | project page: results, evaluation, regulations (upload, extraction, accept), CARLA runs |
| http://localhost:8770/review | blind review of the lane answers that disagree with the labels; decisions are written to `results/runs/review/` |
| http://localhost:3000 | Grafana (user `admin`, the password from `.env`); the dashboard opens as the home page |
| http://localhost:9090 | Prometheus (Status > Targets shows whether the demo page is read) |

The demo page starts in the mode of `configs/experiment.yaml` (`experiment.mock`); switch to real answers in the page's settings.

| Command | What it does |
|---|---|
| `docker compose up --build` | build (only the layers that changed) and start |
| `docker compose up -d` | start in the background |
| `docker compose ps` | which containers run, and their health |
| `docker compose logs -f demo` | messages of the demo page |
| `docker compose down` | stop and remove the containers (the image and the data volumes stay) |
| `docker compose down -v` | the same, and delete the Prometheus and Grafana data |
| `docker compose run --rm demo python main.py selftest` | the self-test inside the image |
| `docker compose run --rm demo python main.py lane run --test AB --split dev --real` | a batch run inside the image; results in `results/runs/` as usual |

## What the containers can see

| Inside the container | On the computer | Access |
|---|---|---|
| `/data` | `DATASETS_ROOT` from `.env` | read-only |
| `/app/datasets` | `datasets/` | read-only |
| `/app/configs` | `configs/` | read and write ("Save" on the page writes `configs/api.yaml` or `configs/experiment.yaml`) |
| `/app/results` | `results/` | read and write (saved runs, the answer cache, the blind review decisions, evaluation reports, the results index; the same as without Docker) |
| `/app/regulations` | `regulations/` | read and write (the extractor writes drafts and accepted passages of new countries) |

Everything else in the container comes from the image and is reset when the container is recreated. On a Mac the datasets folder must be under a path Docker Desktop shares (`/Users` and `/Volumes` are shared by default).

CARLA is not in the image: it needs a GPU and runs as its own server on the computer (*Simulation in CARLA* in the README). The project page in the container can show the saved CARLA runs in `results/carla/`; starting CARLA and driving a route work when the page runs on the computer with CARLA (`python main.py web`).

## Metrics

| Metric | Labels | Meaning |
|---|---|---|
| `demo_answers_total` | task (lane, marking), source (page, batch), test, region, outcome | answers; outcome is answered (new API call), cached, mock, api_error or parse_error |
| `demo_model_latency_seconds` | test | histogram of the time until the model answered (new calls) |
| `demo_tokens_total` | test, kind (input, output) | tokens of new calls |
| `demo_cost_usd_total` | test | estimated cost of new calls (prices in `configs/api.yaml`) |
| `demo_label_checks_total` | task, source, test, region, output (output1, output2), result | answer against the final label; output1 is the whole lane (lane task) or the marking (single-marking task), output2 the actions |
| `demo_unsafe_errors_total` | source, test, region | the label prohibits an action that the answer allows |
| `demo_consistency_issues_total` | test | contradictions inside answers, found without the label |
| `demo_action_values_total` | test, region, action, value | the values of the actions in the answers |
| `demo_batch_runs_total`, `demo_batch_running` | test, region, mode | batch runs started from the page; 1 while one is going |
| `demo_http_requests_total` | method, path, code | requests to the page |
| `demo_info` | mode, model, prompt, reasoning_effort | settings of the page, updated when they are changed |

Every metric of an answer also carries the task; the dashboard has a Task selector at the top (lane or marking). The dashboard shows the running settings and whether the page is up; answers, new API calls, cost, errors and batch runs; answers per minute by outcome; median and 95th percentile latency; Output 1 and Output 2 correct and unsafe errors per test; the share of each action value and of not_determined per action; contradictions per answer; tokens per minute, cost per hour and page requests.

The counters start at zero when the page starts and describe its use. The experiment's numbers are the saved runs in `results/runs/`, which do not depend on Docker.

## Security and privacy settings

| Setting | Where |
|---|---|
| Small base image (`python:3.11-slim`); packages installed with `--no-cache-dir` and checked against the hashes in the lock file | `Dockerfile` |
| The page runs as the user `appuser`, not root | `Dockerfile` |
| Only the needed folders are copied into the image; `.env`, images, datasets and results never are | `Dockerfile`, `.dockerignore` |
| The API key is an environment variable given to the demo container at start, read from `.env`; it is not in the image, the repository or the metrics | `docker-compose.yml` |
| Ports are bound to 127.0.0.1, so other computers on the network cannot open them | `docker-compose.yml` |
| Images and datasets are mounted read-only | `docker-compose.yml` |
| Grafana needs the password from `.env`; anonymous access, sign-up, usage reporting and update checks are off | `docker-compose.yml` |
| CPU and memory limits for the demo container; restart after a crash | `docker-compose.yml` |
| Health check: Docker asks `/healthz` every 30 s and marks the container unhealthy when it does not answer | `Dockerfile` |

`python main.py selftest` checks that the Docker files keep these settings, that the image packages have the same versions as `requirements.txt`, and that `/metrics` and `/healthz` work without showing the key.

To scan the image for known vulnerabilities (Docker Desktop includes Docker Scout):

```bash
docker scout cves reasoning-driving:latest
```

## Changing packages

Change the version in `requirements.txt` and `deploy/requirements-docker.txt`, then make the lock file again and rebuild:

```bash
uv pip compile deploy/requirements-docker.txt --universal --python-version 3.11 --exclude-newer <date> --generate-hashes -o deploy/requirements-docker.lock
docker compose up --build
```

`--universal` writes one lock for every platform (the image is built for arm64 on Apple silicon and amd64 elsewhere).

## Problems

| Message or symptom | Fix |
|---|---|
| `failed to xattr .../._.dockerignore: operation not permitted` | the repository is on a drive formatted exFAT, where macOS keeps extended attributes in hidden `._` files that Docker cannot read; delete them with `dot_clean -m .` in the repository folder and build again (they come back when macOS writes files there) |
| `required variable GRAFANA_ADMIN_PASSWORD is missing a value` | set it in `.env` |
| `port is already allocated` | another program uses 8770, 3000 or 9090 (for example the demo page started without Docker); stop it, or change the left number of the port in `docker-compose.yml` |
| the page lists no images | set `DATASETS_ROOT` in `.env`, check that Docker Desktop shares that folder, run `docker compose up` again |
| "No API key" in real mode | set `OPENAI_API_KEY` in `.env`, run `docker compose up` again |
| Prometheus target `demo` is down | `docker compose logs demo` shows why the page did not start |
