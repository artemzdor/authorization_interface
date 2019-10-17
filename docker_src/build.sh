#!/usr/bin/env bash

echo "Start Build"

cp -r ../authorization_interface ./authorization_interface

echo "Docker Build authorization_interface"

docker build -t asfree/authorization_interface:latest -f Dockerfile_Flask .

echo "End Build authorization_interface"

echo "Docker Build JS"

docker build -t asfree/authorization_interface_js:latest -f Dockerfile_JS .

echo "End Build JS"

echo "Delete authorization_interface"

rm -rf ./authorization_interface

echo "End"

