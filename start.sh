#!/bin/sh

DATA_DIR="${1:-$PWD/data}"
MC_VERSION=1.20.2
CON_NAME=spigot

if which podman &> /dev/null; then
    CON_CMD=podman
elif which docker &> /dev/null; then
    CON_CMD=docker
else
    echo "docker or podman not found"
    exit 1
fi

PLUGIN_DIR=${DATA_DIR}/plugins
PYTHON_DIR=${PWD}/python

mkdir -p $PLUGIN_DIR
cp python.jar $PLUGIN_DIR
mkdir -p $PYTHON_DIR

$CON_CMD run \
    -i -t --rm \
    --name $CON_NAME \
    -e MEMORYSIZE='2G' \
    -p 25565:25565 \
    --mount type=bind,src=$DATA_DIR,dst=/data,relabel=shared \
    --mount type=bind,src=$PYTHON_DIR,dst=/py,relabel=shared \
    -i docker.io/buddyspencer/spigot:$MC_VERSION
