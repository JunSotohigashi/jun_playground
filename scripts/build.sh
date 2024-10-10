#!/bin/bash

IMAGE_NAME='junsotohigashi/jun_playground:latest'

docker build ./docker -t $IMAGE_NAME
docker image prune -f
