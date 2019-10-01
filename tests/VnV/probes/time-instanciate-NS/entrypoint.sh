#!/bin/bash

mkdir -p /output/${PROBE}/${HOSTNAME}

echo "Time to instancate the Network Service: "
echo " - Result file: /output/${PROBE}/$HOSTNAME/results.log"

su -c "tng-cli -e http://pre-int-vnv-bcn.5gtango.eu result -g $RESULT_UUID >> /output/${PROBE}/$HOSTNAME/results.log"
