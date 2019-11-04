#!/bin/bash

source /config.cfg

mkdir -m 777 -p /output/${PROBE}/${HOSTNAME}

#docker run -e WEB="https://rooms.quobis.com" -e CALLER="quobisqa3@quobis" -e PASSWORD="oWc0n2M84xt2" -e CALLED="quobisqa1" -e DURATION=10000 --user apps --privileged docker-chromium

echo "Result file: /output/${PROBE}/$HOSTNAME/results.log"

echo "$RP_IP  comm-pilot.5gtango.eu" >> "/etc/hosts"
#echo "10.10.10.141  comm-pilot.5gtango.eu" >> "/etc/hosts"
echo "$(</etc/hosts)"
date
sleep 30
python3 -u  /test.py
echo "TEST PASSED"
