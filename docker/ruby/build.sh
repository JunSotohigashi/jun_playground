#!/bin/bash

IMAGE_NAME='junsotohigashi/jun_playground:ruby'

docker build ./docker/ruby -t $IMAGE_NAME
docker image prune -f
