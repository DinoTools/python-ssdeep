#!/bin/bash

unknown_os ()
{
  echo "Unknown OS"
  exit 1
}

BASE_PATH="`dirname \"$0\"`"
BASE_PATH="`( cd \"$BASE_PATH\" && pwd )`"
if [ -z "$BASE_PATH" ] ; then
  exit 1
fi
echo "$BASE_PATH"

os=
version=
version_major=
dist=

if [ -e /etc/lsb-release ]; then
  . /etc/lsb-release
  dist=${DISTRIB_CODENAME}
  os=`echo ${DISTRIB_ID} | awk '{ print tolower($1) }'`
  version=${DISTRIB_RELEASE}
elif [ `which lsb_release 2>/dev/null` ]; then
  dist=`lsb_release -c | cut -f2`
  os=`lsb_release -i | cut -f2 | awk '{ print tolower($1) }'`
  version=`lsb_release -r | cut -f2`
elif [ -e /etc/debian_version ]; then
  os=`cat /etc/issue | head -1 | awk '{ print tolower($1) }'`
  if grep -q '/' /etc/debian_version; then
    dist=`cut --delimiter='/' -f1 /etc/debian_version`
  else
    dist=`egrep '^deb' /etc/apt/sources.list | awk '{ print tolower($3) }' | head -n 1 | grep -v '-' | cut --delimiter='/' -f1`
    version=`cat /etc/debian_version`
  fi
elif [ -e /etc/fedora-release ]; then
  major_version=`cut -f3 --delimiter=' ' /etc/fedora-release`
  os='fedora'
elif [ -e /etc/oracle-release ]; then
  os='ol'
  version=`cut -f5 --delimiter=' ' /etc/oracle-release`
elif [ -e /etc/redhat-release ]; then
  os=`cat /etc/redhat-release  | awk '{ print tolower($1) }'`
  if [ "${os}" = "centos" ]; then
    version=`cat /etc/redhat-release | awk '{ print $4 }'`
  elif [ "${os}" = "scientific" ]; then
    version=`cat /etc/redhat-release | awk '{ print $4 }'`
  else
    version=`cat /etc/redhat-release  | awk '{ print tolower($7) }'`
    os='redhatenterpriseserver'
  fi
else
  unknown_os
fi

if [[ -z "$os" ]]; then
  unknown_os
fi

version_major=`echo ${version} | awk -F '.' '{ print $1 }'`

echo "OS:   ${os}"
echo "DIST: ${dist}"
echo "VER:  ${version}"

SCRIPT_FILE=

case ${os} in
  ubuntu)
    SCRIPT_FILE="${os}_${version}.sh"
    ;;
  centos|debian|fedora)
    SCRIPT_FILE="${os}_${version_major}.sh"
    ;;
  *)
    echo "OS not supported"
    exit 1
esac

/bin/bash ${BASE_PATH}/${SCRIPT_FILE}
exit $?
