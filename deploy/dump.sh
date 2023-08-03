#!/bin/bash

source ./config/.env

docker compose exec -it mysql mysqldump --user=root --password=$MYSQL_ROOT_PASSWORD \
  --databases Aiogram \
  --routines > data/dump.sql
