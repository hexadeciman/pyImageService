#!/bin/bash

docker kill $(docker ps -q)
docker rm $(docker ps --filter status=exited -q)
docker rm $(docker ps --filter status=created -q)
docker rmi -f $(docker images -aq)
# docker build --tag c2 .
# docker run --name c2 -d -p 8080:8080 c2 
docker-compose up -d