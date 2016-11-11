FROM centos:7

RUN yum -q -y groupinstall "Development Tools" && \
    yum -q -y install epel-release && \
    yum -q -y install \
        libffi-devel \
        python-devel \
        python-pip \
        pytest \
        automake \
        autoconf \
        ssdeep-devel \
        ssdeep-lib

COPY . /code
RUN cd /code && \
    BUILD_LIB=1 pip install . && \
    pip install pytest && \
    py.test