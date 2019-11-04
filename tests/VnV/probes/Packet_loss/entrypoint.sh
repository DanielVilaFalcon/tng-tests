#!/bin/bash

mkdir -p /output/${PROBE}/${HOSTNAME}

echo "Packet loss: "
echo " - Result file: /output/${PROBE}/$HOSTNAME/results.log"

python3 /parser.py $MS_IP >> /output/${PROBE}/$HOSTNAME/results.log
