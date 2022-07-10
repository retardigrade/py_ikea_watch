#!/bin/bash

token=$1
cd ./py_ikea_watch || exit
git pull origin main

docker stop ikea_bot
docker image rm ikea_bot:latest -f
docker build . --tag ikea_bot
docker run --name ikea_bot -e="$token" --restart unless-stopped ikea_bot:latest