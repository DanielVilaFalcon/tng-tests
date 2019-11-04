#!/bin/bash

mkdir -p /output/${PROBE}/${HOSTNAME}

echo "Time to instancate the Network Service: "
echo " - Result file: /output/${PROBE}/$HOSTNAME/results.log"

python3 /parser.py $RESULT_UUID >> /output/${PROBE}/$HOSTNAME/results.log
