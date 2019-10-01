#!/bin/bash

echo "$RP_IP  comm-pilot.5gtango.eu" >> "/etc/hosts"
#echo "10.10.10.134  comm-pilot.5gtango.eu" >> "/etc/hosts"

echo "$(</etc/hosts)"
sleep 60

su -c "node /app.js" apps
