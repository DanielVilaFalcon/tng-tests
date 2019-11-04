#!/usr/bin/env python
import sys
import os, subprocess
import time
from xml.dom import minidom
import requests
import json
import urllib3
from datetime import datetime
import os, subprocess
from wacApi import get_num_active_sessions

def create_users (numNeededUsers, indexUser, availableUsers, adminAccessToken):
    for i in range (numNeededUsers):
        os.system("python3 ./wacApi.py 5gtango"+str(indexUser)+" "+adminAccessToken)
        availableUsers.append("5gtango"+str(indexUser))
        indexUser=indexUser+1;
    return availableUsers

def get_oauth_token(sapi_url,username, password):
    url = sapi_url + "/o/token"
    postData = {
        "grant_type": "password",
        "username": username,
        "password": password
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json.dumps(postData), headers=headers, verify=False)
    parsedResponse = json.loads(response.content.decode('utf-8'))
    return parsedResponse["access_token"]

if __name__ == '__main__':

    indexUser=6
    SAPI_URL = "https://comm-pilot.5gtango.eu/sapi"
    ADMIN_USERNAME = "admin@quobis"
    ADMIN_PASSWORD = "admin"
    adminAccessToken = get_oauth_token(SAPI_URL, ADMIN_USERNAME, ADMIN_PASSWORD)
    now = datetime.now()
    timesToStart=[]
    durations=[]
    numCalls=[]
    availableUsers=[]
    for u in range(1,6):
        availableUsers.append("5gtango"+str(u))
    xmldoc = minidom.parse('/tasks.xml')
    author = xmldoc.getElementsByTagName('author')[0]
    name = xmldoc.getElementsByTagName('name')[0]
    description = xmldoc.getElementsByTagName('description')[0]
    vendor = xmldoc.getElementsByTagName('vendor')[0]
    version = xmldoc.getElementsByTagName('version')[0]
    #Print the test information
    print("Test name: "+name.firstChild.data)
    print("Test description: "+description.firstChild.data)
    print("Vendor: "+vendor.firstChild.data)
    print("Version: "+version.firstChild.data)

    tasks = xmldoc.getElementsByTagName('task')

    for task in tasks:
        start = task.getElementsByTagName("from")[0].firstChild.data
        aux = start.split(":")
        timesToStart.append(now.replace(hour=int(aux[0]), minute=int(aux[1]), second=0, microsecond=0))
        durations.append(task.getElementsByTagName("duration")[0].firstChild.data)
        numCalls.append(task.getElementsByTagName("numCalls")[0].firstChild.data)

    while True:
        now = datetime.now()
        for index,timeToStart in enumerate(timesToStart):
            if (timeToStart<now):
                if (len(availableUsers)/2<int(numCalls[index])):
                    #Create the number of USER needed
                    numNeededUsers = (int(numCalls[index])*2) - len(availableUsers)
                    availableUsers = create_users (numNeededUsers, indexUser, availableUsers, adminAccessToken)
                    indexUser=indexUser+int(numNeededUsers)-1
                    auxIndex= indexUser
                for n in range(int(numCalls[index]),0,-8):
                    if (n>8):
                        os.system("node /app.js "+str(8)+" "+str(auxIndex)+" &")
                        auxIndex = auxIndex - 16
                    else:
                        os.system("node /app.js "+str(n)+" "+str(auxIndex)+" &")
                        auxIndex = auxIndex - (int(n)*2) 
                    time.sleep(5)
                for i in range(int(numCalls[index])):
                    del availableUsers[0:2]
                    time.sleep(2)
                del timesToStart[index]
                del durations[index]
                del numCalls[index]
            else:
                print("Waiting...")
        time.sleep(10)
        numSessions=get_num_active_sessions(SAPI_URL,adminAccessToken)
        print(numSessions)
        if (not timesToStart and int(numSessions)==0):
            sys.exit()
