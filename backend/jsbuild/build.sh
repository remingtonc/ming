#!/usr/bin/env bash
npx rollup -c
npx tailwindcss -i ./tailwind_src/input.css -o ../ming/routes/static/css/tailwind.css