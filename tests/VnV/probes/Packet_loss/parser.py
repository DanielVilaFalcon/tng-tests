#!/usr/bin/env python
import sys
import os, subprocess

if __name__ == '__main__':

    command_success="ping "+sys.argv[1]+" -c1500 -q -i 0.2"
    result_success = str(subprocess.check_output([command_success], shell=True)).split("\\n")
    aux = result_success[3].split(",")
    for i, value in enumerate(aux):
        if(i!=3):
            print(value.strip())
        if i==2:
            pl=float(value.replace("% packet loss","").replace(" ",""))

    if (pl<2):
        print("Packet loss lower than 2%")
        print("TEST PASSED")
    else:
        print("Packer loss higher than 2%")
        print("TEST FAILED")
