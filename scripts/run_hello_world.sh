#!/bin/bash

IMAGE_NAME='junsotohigashi/jun_playground:latest'

docker run --rm -it \
    -u $(id -u):$(id -g) \
    $IMAGE_NAME \
    echo 'Hello world!'
