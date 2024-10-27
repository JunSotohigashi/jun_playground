#!/bin/bash

IMAGE_NAME='junsotohigashi/jun_playground:python_cuda'

docker build ./docker/python_cuda -t $IMAGE_NAME
docker image prune -f
