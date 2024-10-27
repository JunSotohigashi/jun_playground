#!/bin/bash

IMAGE_NAME='junsotohigashi/jun_playground:gcc'

docker build ./docker/gcc -t $IMAGE_NAME
docker image prune -f
