#!/bin/bash
echo "export DISPLAY=:0.0" >> /etc/environment
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/
DISPLAY=:1.0
export DISPLAY
echo $DISPLAY
Xvfb :1 -screen 0 1024x768x24 -extension RANDR &> xvfb.log &

source /config.cfg

mkdir -m 777 -p /output/${PROBE}/${HOSTNAME}

echo "Result file: /output/${PROBE}/$HOSTNAME/results.log"

echo "$RP_IP  comm-pilot.5gtango.eu" >> "/etc/hosts"
#echo "10.10.10.141  comm-pilot.5gtango.eu" >> "/etc/hosts"
echo "$(</etc/hosts)"
sleep 90
python3 -u  /test.py
python3 -u  /parser.py >> "/output/${PROBE}/$HOSTNAME/results.log"
echo "$(</output/${PROBE}/$HOSTNAME/results.log)"
