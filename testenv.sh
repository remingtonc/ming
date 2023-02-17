#!/usr/bin/env bash
podman start quick-postgres
podman exec quick-postgres psql -U postgres -c 'CREATE DATABASE ming;'