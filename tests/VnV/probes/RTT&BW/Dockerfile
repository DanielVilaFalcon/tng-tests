FROM ubuntu:14.04
FROM debian

RUN apt-get update; apt-get clean

#Install python3
RUN apt-get install -y python3


#Set working directory
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-setuptools
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -U setuptools

#Install iperf command_success
RUN apt-get install -y iperf


ENV QPERF_DOWNLOAD_LINK https://www.openfabrics.org/downloads/qperf/qperf-0.4.9.tar.gz
ENV QPERF_TAR qperf-0.4.9.tar.gz

# Install wget
RUN ["/bin/bash", "-c", "apt-get update && apt-get install wget build-essential -y"]

# Download and extract qperf
RUN ["/bin/bash", "-c", "wget $QPERF_DOWNLOAD_LINK && tar -xvf $QPERF_TAR && rm $QPERF_TAR"]

# Build qperf
WORKDIR qperf-0.4.9
RUN ["/bin/bash", "-c", "./configure && make"]

# Copy qperf
RUN ["/bin/bash", "-c", "cp src/qperf /usr/local/bin"]

ENV PROBE "RTTandBW"
ENV MS_IP ""
WORKDIR /output/${PROBE}/$HOSTNAME

COPY entrypoint.sh /
COPY config.cfg /
COPY parser.py /
RUN ["chmod", "777", "/parser.py"]
RUN ["chmod", "777", "/entrypoint.sh"]
RUN ["chmod", "777", "/config.cfg"]
ENTRYPOINT [ "/entrypoint.sh" ]
