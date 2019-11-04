#!/bin/bash

mkdir -p /output/${PROBE}/${HOSTNAME}

echo "Increasing the number of sessions: "
echo " - Result file: /output/${PROBE}/$HOSTNAME/results.log"
echo "$RP_IP  comm-pilot.5gtango.eu" >> "/etc/hosts"
#echo "10.120.0.208  comm-pilot.5gtango.eu" >> "/etc/hosts"

#echo "$(</etc/hosts)"

python3 parser.py $SESSIONS >> "/output/${PROBE}/$HOSTNAME/results.log"
