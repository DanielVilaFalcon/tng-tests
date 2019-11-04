#!/bin/bash

mkdir -p /output/${PROBE}/${HOSTNAME}

echo "RTT and BW: "
echo " - Result file: /output/${PROBE}/$HOSTNAME/results.log"

python3 /parser.py $MS_IP >> /output/${PROBE}/$HOSTNAME/results.log
