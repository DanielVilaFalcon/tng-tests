#!/usr/bin/env python
import sys
import os, subprocess

if __name__ == '__main__':

    command_success="python3 snmpWacAPI.py "+sys.argv[1]
    result_success = str(subprocess.check_output([command_success], shell=True)).replace(" ","").split("\\n")
    numSession = float(result_success[1])
    if (numSession>=10):
        print("The registration per second is "+str(numSession)+"sessions/sec, greater than 10 sessions/sec")
        print("TEST PASSED")
    else:
        print("The registration per second is "+str(numSession)+"sessions/sec, lower than 10 sessions/sec")
        print("TEST FAILED")
