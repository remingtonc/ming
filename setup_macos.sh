#!/usr/bin/env bash
brew install podman
brew install libpq
brew link --force libpq
podman create --name quick-postgres -p 5432:5432 -e POSTGRES_PASSWORD=quick postgres:alpine