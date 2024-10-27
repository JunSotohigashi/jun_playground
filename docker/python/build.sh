#!/bin/bash

IMAGE_NAME='junsotohigashi/jun_playground:python'

docker build ./docker/python -t $IMAGE_NAME
docker image prune -f
