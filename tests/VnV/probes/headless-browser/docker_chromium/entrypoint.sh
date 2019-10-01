#!/bin/bash

source /config.cfg


mkdir -m 777 -p /output/${PROBE}/${HOSTNAME}

#docker run -e WEB="https://rooms.quobis.com" -e CALLER="quobisqa3@quobis" -e PASSWORD="oWc0n2M84xt2" -e CALLED="quobisqa1" -e DURATION=10000 --user apps --privileged docker-chromium

echo "CALL CONFIGURATION"
echo "Docker User: "$USER
echo "Web: "$WEB
echo "User Caller: "$CALLER
echo "User Called: "$CALLED
echo "Duration: "$DURATION
echo "Result file: /output/${PROBE}/$HOSTNAME/results.log"

echo "$RP_IP  comm-pilot.5gtango.eu" >> "/etc/hosts"
#echo "10.10.10.134  comm-pilot.5gtango.eu" >> "/etc/hosts"
echo "$(</etc/hosts)"
dur=$DURATION
ringingTime=40000

capturingTime=$((dur+ringingTime))
capturingTime=$((capturingTime/1000))
sleep 60
sudo iftop -i any -t -o s2 -L 2 -s $capturingTime -P >> "/res1.log" &
#tcpdump -i eth0 udp -vv >> "/output/${PROBE}/$HOSTNAME/aux.log" &
sudo tshark -i any -q -f 'udp portrange 1-65000' -o rtp.heuristic_rtp:TRUE -q -z rtp,streams,stat -a duration:$capturingTime >> "/res.log" &


su -c "echo 'PUPPETEER LOGS'  >> '/output/${PROBE}/$HOSTNAME/results.log'" apps
node /app.js  >> "/output/${PROBE}/$HOSTNAME/results.log"
echo -e " \n"  >> "/output/${PROBE}/$HOSTNAME/results.log"

echo -e "CALL CONFIGURATION"  >> "/output/${PROBE}/$HOSTNAME/results.log"
echo "Docker User: "$USER  >> "/output/${PROBE}/$HOSTNAME/results.log"
echo "Web: "$WEB  >> "/output/${PROBE}/$HOSTNAME/results.log"
echo "Caller user: "$CALLER  >> "/output/${PROBE}/$HOSTNAME/results.log"
echo "Called user: "$CALLED  >> "/output/${PROBE}/$HOSTNAME/results.log"
echo "Duration: "$DURATION  >> "/output/${PROBE}/$HOSTNAME/results.log"
echo "Result file: /output/${PROBE}/$HOSTNAME/results.log"  >> "/output/${PROBE}/$HOSTNAME/results.log"
echo -e " \n"  >> "/output/${PROBE}/$HOSTNAME/results.log"
echo -e "TSHARK RTP STATS"  >> "/output/${PROBE}/$HOSTNAME/results.log"
cat "/res.log" >> "/output/${PROBE}/$HOSTNAME/results.log"
echo -e " \n"  >> "/output/${PROBE}/$HOSTNAME/results.log"
cat "/res1.log" >> "/output/${PROBE}/$HOSTNAME/results.log"
