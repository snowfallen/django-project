#!/bin/bash

case "$1" in
  "build") scripts/build.sh ;;
  "runserver") scripts/runserver.sh ;;
  "bash") docker-compose exec django -it bash ;;
  "shell") scripts/shell.sh ;;
  "createSuperUser") scripts/createSuperUser.sh ;;
  "stop") scripts/stop.sh ;;
  *) docker-compose "$1"
esac