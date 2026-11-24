# Image of the project: the web page (python main.py web) and the command line (runs, lane runs, evaluation,
# regulation extraction, selftest). CARLA is not in the image: it needs a GPU and runs as its own server.
# Normally started with Prometheus and Grafana:  docker compose up --build   (docs/deployment.md)
# Alone:  docker build -t reasoning-driving .
#         docker run --rm -p 127.0.0.1:8770:8770 reasoning-driving
#
# The image holds the code, the settings, the prompts and the countries' rules. Images, labels, results and the .env
# file stay outside it (.dockerignore); docker compose mounts them, and passes the API key as an environment variable.

# Small Debian image with the Python version of requirements.txt
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    MPLBACKEND=Agg

WORKDIR /app
# ffmpeg: H.264 encoding of the annotated videos of the Video tab (OpenCV alone writes mp4v, which browsers do not play).
# Added by Claude, 2026-11-18.
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && rm -rf /var/lib/apt/lists/*

# Packages first, so a code change does not reinstall them. Every version and file hash is pinned in the lock file.
COPY deploy/requirements-docker.lock deploy/requirements-docker.lock
RUN pip install --no-cache-dir --require-hashes -r deploy/requirements-docker.lock

# Only what the project needs to run. --chmod=755 makes the files readable for the normal user below whatever
# permissions they have on the computer (a drive formatted exFAT gives them to the owner only).
COPY --chmod=755 main.py main.py
COPY --chmod=755 reasoning_drive reasoning_drive
COPY --chmod=755 configs configs
COPY --chmod=755 prompts prompts
COPY --chmod=755 regulations regulations

# Run as a normal user, not root
RUN useradd --create-home --uid 1000 appuser \
    && mkdir -p /app/results /app/datasets /app/regulations/inbox \
    && chown -R appuser:appuser /app/results /app/configs /app/regulations
USER appuser

# The web page; /metrics on the same port is read by Prometheus
EXPOSE 8770

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8770/healthz', timeout=4)" || exit 1

CMD ["python", "main.py", "web", "--host", "0.0.0.0", "--port", "8770", "--no-browser"]
