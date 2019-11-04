#!/usr/bin/env python

import random
import time
import requests
import json
import urllib3
from datetime import datetime
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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
    print(response)
    parsedResponse = json.loads(response.content.decode('utf-8'))
    return parsedResponse["access_token"]

def get_num_active_sessions(sapi_url,token):
    url = sapi_url + "/sessions?to=-1"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    response = requests.get(url, headers=headers, verify=False)
    parsedResponse = json.loads(response.content.decode('utf-8'))
    return len(parsedResponse)

def post_num_active_sessions(sapi_url, token):
    url = sapi_url + "/sessions?to=-1"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    postData = {
           "context": {
                "src": "test@example.com",
                "language": "es"
            }
    }
    response = requests.post(url, data=json.dumps(postData), headers=headers, verify=False)


if __name__ == '__main__':

    SAPI_URL = "https://comm-pilot.5gtango.eu/sapi"
    ADMIN_USERNAME = "admin@quobis"
    ADMIN_PASSWORD = "admin"
    # GET bearer token for the admin user
    adminAccessToken = get_oauth_token(SAPI_URL, ADMIN_USERNAME, ADMIN_PASSWORD)

    for i in range (int(sys.argv[1])):
        post_num_active_sessions(SAPI_URL,adminAccessToken)

    active_sessions = get_num_active_sessions(SAPI_URL,adminAccessToken)
    print (active_sessions)
