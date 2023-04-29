#!/usr/bin/env bash

# Create env if doesn't exist.
echo "Copy .env example to .env"
FILE=.env
if [ -f "$FILE" ]; then
    echo ".env already exists, skipping"
else
    cp .env.example .env
fi

docker-compose up -d --build --force-recreate
