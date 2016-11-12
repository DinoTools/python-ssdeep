FROM debian:8
ENV DEBIAN_FRONTEND noninteractive

# Speedup
RUN echo 'force-unsafe-io' | tee /etc/dpkg/dpkg.cfg.d/02apt-speedup && \
    echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb || true";};' | tee /etc/apt/apt.conf.d/no-cache && \
    echo 'Acquire::http {No-Cache=True;};' | tee /etc/apt/apt.conf.d/no-http-cache

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        libffi-dev \
        && \
    apt-get clean

RUN apt-get install -y \
        python3 \
        python3-dev \
        python3-pip \
        && \
    apt-get clean

RUN apt-get install -y \
        automake \
        autoconf \
        libtool \
        && \
    apt-get clean

COPY . /code
RUN cd /code && \
    BUILD_LIB=1 pip3 install . && \
    pip3 install pytest && \
    py.test
