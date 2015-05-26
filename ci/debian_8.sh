#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

PKGS="build-essential libffi-dev"
case $PYTHON in
  python2)
    PY_BIN=python
    PIP_BIN=pip
    PKGS="${PKGS} python python-dev python-pip"
    ;;
  python3)
    PY_BIN=python3
    PIP_BIN=pip3
    PKGS="${PKGS} python3 python3-dev python3-pip"
    ;;
esac

if [ "$LIB" == "system" ]; then
  export BUILD_LIB=0
  PKGS="${PKGS} libfuzzy-dev"
else
  export BUILD_LIB=1
  PKGS="${PKGS} automake autoconf libtool"
fi

echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup
apt-get update -q
apt-get install -q -y ${PKGS}

${PIP_BIN} install .
${PIP_BIN} install pytest
py.test
exit $?
