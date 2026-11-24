#!/bin/bash
# Build the Docker image from a clean copy on the Mac's own disk.
# Why: the project is on the T9 drive (exFAT). macOS keeps extended attributes there in hidden "._name" files, and
# Docker's builder fails on them ("failed to xattr ._…: operation not permitted"), even for files it would ignore.
# The copy holds only what the image needs (the same list as .dockerignore), without "._" files.
# usage:  bash scripts/docker_build.sh        then  docker compose up -d --no-build
# Added by Claude, 2026-11-18.
set -e
cd "$(dirname "$0")/.."
SRC="$(pwd)"
BUILD="$HOME/.cache/reasoning_drive_build"
mkdir -p "$BUILD/deploy"
echo "== copying the build context to $BUILD (without ._ files)"
for d in reasoning_drive configs prompts regulations; do
  rsync -a --delete --exclude '._*' --exclude '.DS_Store' --exclude '__pycache__' --exclude '*.pyc' \
        --exclude 'inbox/' "$SRC/$d/" "$BUILD/$d/"
done
cp "$SRC/main.py" "$SRC/Dockerfile" "$BUILD/"
cp "$SRC/deploy/requirements-docker.lock" "$BUILD/deploy/"
printf '**/._*\n**/.DS_Store\n**/__pycache__\n' > "$BUILD/.dockerignore"
echo "== docker build -t reasoning-driving:latest"
docker build -t reasoning-driving:latest "$BUILD"
