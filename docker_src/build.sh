#!/usr/bin/env bash

echo "Start Build"

export GIT_CLONE=https://github.com/artemzdor/authorization_interface.git
export DOCKER_URL=asfree/authorization_interface:latest

echo "Git Clone: book_crud_api"

git clone $GIT_CLONE

echo "Docker Build"

docker build -t $DOCKER_URL .

echo "Delete $GIT_CLONE"

rm -rf ./authorization_interface

echo "End"

