#!/bin/bash

IMAGE_NAME='junsotohigashi/jun_playground:golang'

docker build ./docker/golang -t $IMAGE_NAME
docker image prune -f
