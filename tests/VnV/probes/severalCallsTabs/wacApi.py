#!/usr/bin/env python

import random
import time
import requests
import json
import urllib3
from datetime import datetime
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_num_active_sessions(sapi_url,token):
    url = sapi_url + "/sessions?to=-1"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    response = requests.get(url, headers=headers, verify=False)
    parsedResponse = json.loads(response.content.decode('utf-8'))
    return len(parsedResponse)

def get_user(sapi_url,token, username):
    url = sapi_url + "/users"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    response = requests.get(url, headers=headers, verify=False)
    parsedResponse = json.loads(response.content.decode('utf-8'))
    user = [i for i, value in enumerate(parsedResponse) if username==value.get("username")]
    return parsedResponse[user[0]].get("id")

def get_credentials(sapi_url,token):
    url = sapi_url + "/credentials?state=active"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    response = requests.get(url, headers=headers, verify=False)
    parsedResponse = json.loads(response.content.decode('utf-8'))
    return len(parsedResponse)

def get_conferences(sapi_url,token):
    url = sapi_url + "/conferences?state=active"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    response = requests.get(url, headers=headers, verify=False)
    parsedResponse = json.loads(response.content.decode('utf-8'))
    return len(parsedResponse)

def get_contacts(sapi_url,token,username):
    url = sapi_url + "/contacts"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    response = requests.get(url, headers=headers, verify=False)
    parsedResponse = json.loads(response.content.decode('utf-8'))
    user = [i for i, value in enumerate(parsedResponse) if username==value.get("name")]
    return parsedResponse[user[0]].get("user")

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

def post_user(sapi_url, token, username):
    url = sapi_url + "/users"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    postData = {
            "domain": "quobis",
  	    "username": username,
            "email": username+"@quobis.com",
            "role": "user",
            "capabilities": [],
            "mobilePhone": []
    }
    response = requests.post(url, data=json.dumps(postData), headers=headers, verify=False)

def post_credential(sapi_url, token, username):
    url = sapi_url + "/credentials"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    postData = {
          "source": "wac",
          "type": "basic",
          "context": {},
          "domain": "quobis",
          "user": user,
          "data": {
             "password": username
          },
          "lease": 0
    }
    response = requests.post(url, data=json.dumps(postData), headers=headers, verify=False)

if __name__ == '__main__':

    username=sys.argv[1]
    adminAccessToken=sys.argv[2]
    SAPI_URL = "https://comm-pilot.5gtango.eu/sapi"
    if username=="stats":
        print("Number of active conferences: "+str(get_conferences(SAPI_URL,adminAccessToken)))
        print("Number of active sesions: "+str(get_num_active_sessions(SAPI_URL,adminAccessToken)))
    else:
        post_user(SAPI_URL,adminAccessToken, username)			#Get the ID of the use to search by field user in get_contacts
        user = get_contacts(SAPI_URL,adminAccessToken,username)	#Search by ID and get the "User" field
        post_credential(SAPI_URL,adminAccessToken,username)			#Post the credentials os user identified by "User" field
