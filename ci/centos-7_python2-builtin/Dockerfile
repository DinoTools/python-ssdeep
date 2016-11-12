FROM centos:7

RUN yum -q -y groupinstall "Development Tools" && \
    yum -q -y install epel-release

RUN yum -q -y install \
        libffi-devel \
        python-devel \
        python-pip \
        pytest

RUN yum -q -y install \
        automake \
        autoconf \
        libtool

COPY . /code
RUN cd /code && \
    BUILD_LIB=1 pip install . && \
    pip install pytest && \
    py.test
