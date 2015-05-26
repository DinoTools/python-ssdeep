#!/bin/bash

PKGS="libffi-devel"
case $PYTHON in
  python2)
    PY_BIN=python
    PIP_BIN=pip
    PYTEST_BIN=py.test
    PKGS="${PKGS} python-devel python-pip pytest"
    ;;
  *)
    echo "Python version not supported"
    exit 1
    ;;
esac

if [ "$LIB" == "system" ]; then
  export BUILD_LIB=0
  PKGS="${PKGS} ssdeep-devel ssdeep-lib"
else
  export BUILD_LIB=1
  PKGS="${PKGS} automake autoconf libtool"
fi

yum -q -y groupinstall "Development Tools"
yum -q -y install epel-release
yum -q -y install ${PKGS}

${PIP_BIN} install .

if [ "${PYTEST_BIN}" == "" ]; then
  ${PIP_BIN} install pytest
fi

py.test
exit $?
