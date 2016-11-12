#!/bin/bash

OS_NAME=$1
OS_VERSION=$2
PYTHON_VERSION=$3
LIB_TYPE=$4

if [ $# -ne 4 ]; then
    echo "$0 <OS_NAME> <OS_VERSION> <PYTHON_VERSION> <LIB_TYPE>"
    exit 1
fi

BASE_PATH="`dirname \"$0\"`"
BASE_PATH="`( cd \"$BASE_PATH\" && pwd )`"
if [ -z "$BASE_PATH" ] ; then
  exit 1
fi
echo "Base path: $BASE_PATH"

CFG_PATH="${BASE_PATH}/${OS_NAME}-${OS_VERSION}_${PYTHON_VERSION}-${LIB_TYPE}"
if [ ! -d "$CFG_PATH" ]; then
    echo "Path '$CFG_PATH' not found"
    exit 1
fi

docker build -f "${CFG_PATH}/Dockerfile" .
RET=$?
exit $RET
