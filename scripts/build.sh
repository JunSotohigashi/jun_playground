#!/bin/bash

IMAGE_NAME='junsotohigashi/jun_playground:latest'

docker build . -t $IMAGE_NAME
docker image prune -f
