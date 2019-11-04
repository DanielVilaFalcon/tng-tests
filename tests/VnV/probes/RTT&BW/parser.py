#!/usr/bin/env python
import sys
import os, subprocess

if __name__ == '__main__':

    command_success="qperf -v "+sys.argv[1]+" udp_bw udp_lat -to 20"
    result_success = str(subprocess.check_output([command_success], shell=True)).replace(" ","").split("\\n")
    for i, value in enumerate(result_success):
        if "latency" in value:
            aux = value.split("=")
            if "ms" in aux[1]:
                latency = aux[1].replace("ms","")
                latency = float(latency)
            elif "us" in aux[1]:
                latency = aux[1].replace("us","")
                latency = float(latency)/1000
        if "send_bw" in value:
            aux = value.split("=")
            if "GB/sec" in aux[1]:
                BW = aux[1].replace("GB/sec","")
                BW = float(BW)*1000000
            elif "MB/sec" in aux[1]:
                BW = aux[1].replace("MB/sec","")
                BW = float(BW)*1000
            elif "KB/sec" in aux[1]:
                BW = aux[1].replace("KB/sec","")
                BW = float(BW)

    if (latency < 20) and (BW > 100):
        print("Latency: "+str(latency)+" ms")
        print("Latency lower than 20ms")
        print("BW: "+str(BW)+" KB/sec")
        print("BW greater than 100 KB/sec")
        print("TEST PASSED")
    elif (latency > 20) and (BW > 100):
        print("Latency: "+str(latency)+" ms")
        print("Latency greater than 20ms")
        print("BW: "+str(BW)+" KB/sec")
        print("BW greater than 100 KB/sec")
        print("TEST FAILED -> Latency")
    elif (latency < 20) and (BW < 100):
        print("Latency: "+str(latency)+" ms")
        print("Latency lower than 20ms")
        print("BW: "+str(BW)+" KB/sec")
        print("BW lower than 100 KB/sec")
        print("TEST FAILED -> BW")
    else:
        print("Latency: "+str(latency)+" ms")
        print("Latency greater than 20ms")
        print("BW: "+str(BW)+" KB/sec")
        print("BW lower than 100 KB/sec")
        print("TEST FAILED -> Latency and BW")
