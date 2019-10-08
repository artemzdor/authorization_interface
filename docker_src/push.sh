#!/usr/bin/env bash

echo "Start Push"

docker push asfree/authorization_interface:latest
docker push asfree/authorization_interface_js:latest

echo "End"

