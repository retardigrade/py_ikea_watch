#!/bin/bash

token=$1
date=$(date '+%Y-%m-%d--%H-%M-%S')

cd ./py_ikea_watch || exit
git pull origin main

docker stop ikea_bot
docker image rm ikea_bot:latest -f
docker build . --tag ikea_bot
docker run --name ikea_bot_"$date" -e API_TOKEN="$token" --restart unless-stopped ikea_bot:latest