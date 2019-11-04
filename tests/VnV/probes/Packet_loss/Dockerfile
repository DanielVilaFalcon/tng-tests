FROM ubuntu:14.04
FROM debian

RUN apt-get update; apt-get clean

#Install python3
RUN apt-get install -y python3


#Set working directory
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-setuptools
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -U setuptools

ENV PROBE "packetLoss"
ENV MS_IP ""
WORKDIR /output/${PROBE}/$HOSTNAME

COPY entrypoint.sh /
COPY config.cfg /
COPY parser.py /
RUN ["chmod", "777", "/parser.py"]
RUN ["chmod", "777", "/entrypoint.sh"]
RUN ["chmod", "777", "/config.cfg"]
ENTRYPOINT [ "/entrypoint.sh" ]
