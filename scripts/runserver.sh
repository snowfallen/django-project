#!/usr/bin/env bash

docker-compose stop
docker-compose up -d
docker-compose run --rm django python manage.py makemigrations
docker-compose run --rm django python manage.py migrate
echo "website is running on 127.0.0.1:8000"

