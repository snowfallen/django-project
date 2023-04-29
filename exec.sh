#!/bin/bash

case "$1" in
  "build") scripts/build.sh ;;
  "runserver") scripts/runserver.sh ;;
  "bash") docker-compose exec django -it bash ;;
  *) docker-compose "$1"
esac