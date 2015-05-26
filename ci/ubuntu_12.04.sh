#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

PKGS="build-essential libffi-dev"
EASYINSTALL_BIN=
case $PYTHON in
  python2)
    PY_BIN=python
    PIP_BIN=pip
    PKGS="${PKGS} python python-dev python-pip"
    ;;
  python3)
    PY_BIN=python3
    EASYINSTALL_BIN=easy_install3
    PIP_BIN=pip
    PKGS="${PKGS} python3 python3-dev python3-setuptools"
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

if [ "${EASYINSTALL_BIN}" != "" ]; then
  ${EASYINSTALL_BIN} pip
fi

${PIP_BIN} install .
${PIP_BIN} install pytest
py.test
exit $?
