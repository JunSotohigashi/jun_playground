#!/bin/bash

IMAGE_NAME='junsotohigashi/jun_playground:latest'

docker run --rm -it \
    --gpus all \
    -v .:/workspace \
    -e HOST_UID=$(id -u) \
    -e HOST_GID=$(id -g) \
    -e HOST_UNAME=$(id -un) \
    -e HOST_GNAME=$(id -gn) \
    $IMAGE_NAME \
    bash
