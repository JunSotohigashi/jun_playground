#!/bin/bash

IMAGE_NAME='junsotohigashi/jun_playground:java'

docker build ./docker/java -t $IMAGE_NAME
docker image prune -f
