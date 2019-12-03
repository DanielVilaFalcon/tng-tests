#!/usr/bin/env python
import sys
import os, subprocess

if __name__ == '__main__':

    command_success="tng-cli -u http://pre-int-vnv-bcn.5gtango.eu result -g "+str(sys.argv[1])
    result_success = str(subprocess.check_output([command_success], shell=True))
    res = result_success.find("service_instantiation_time")
    timeInstanNs = float(result_success[res+30:res+30+6])
    if (timeInstanNs < 900) and (timeInstanNs> 300):
        print("Service instantiation time: "+str(timeInstanNs/60)+" min ("+str(timeInstanNs) +"s)")
        print("Time between 5 min (300s) and 15 min (900s)")
        print("TEST PASSED")
    else:
        print("TEST FAILED")
