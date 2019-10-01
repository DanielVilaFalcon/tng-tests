FROM ubuntu:14.04
FROM debian

RUN apt-get update; apt-get clean

#Install python3
RUN apt-get install -y python3


#Install git
RUN apt-get update \
    && apt-get install -y git
RUN mkdir /home/sampleTest \
   && cd /home/sampleTest \
   && git clone https://github.com/sonata-nfv/tng-cli.git

#Set working directory
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-setuptools
WORKDIR /home/sampleTest
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -U setuptools

#Install python3
RUN apt-get update \
    && apt-get install -y python3

RUN cd /home/sampleTest/tng-cli \
    && python3 setup.py install
RUN cd /home/sampleTest/tng-cli \
    && pip3 install tngcli

ENV PROBE "timeNS"
ENV RESULT_UUID ""
WORKDIR /output/${PROBE}/$HOSTNAME

COPY entrypoint.sh /
COPY config.cfg /
RUN ["chmod", "777", "/entrypoint.sh"]
RUN ["chmod", "777", "/config.cfg"]
ENTRYPOINT [ "/entrypoint.sh" ]
