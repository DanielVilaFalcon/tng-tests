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


if __name__ == '__main__':

    os.system("node /appCalled.js 5gtango1 5gtango1 &")
    os.system("node /appCaller.js 5gtango2 5gtango2 5gtango1 80000 &")
    time.sleep(120)
