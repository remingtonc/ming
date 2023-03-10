#!/usr/bin/env bash
brew install podman
brew install libpq
brew link --force libpq
brew tap sqitchers/sqitch
brew install sqitch --with-postgres-support
# Share /Users/user to podman machine for bind mounts
podman machine init --now --cpus=1 --memory=2048 -v $HOME:$HOME