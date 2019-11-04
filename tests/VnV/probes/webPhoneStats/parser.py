#!/usr/bin/python
import sys
import os, subprocess
import time

def parser():

    indexes=[];
    bytesReceivedValues=[]
    bitsReceivedPerSecondValues=[]
    recvpacketsLostValues=[]
    packetsReceivedValues=[]
    packetsReceivedPerSecondValues=[]
    googJitterBufferMsValues=[]
    googPreferredJitterBufferMsValues=[]
    bytesSentValues=[]
    bitsSentPerSecondValues=[]
    packetsSentValues=[]
    packetsSentPerSecondValues=[]
    sendpacketsLostValues=[]
    googRttValues=[]
    #------------- Video Information -------------#
    googAvailableReceiveBandwidthValues=[]
    googAvailableSendBandwidthValues=[]
    googTransmitBitrateValues=[]
    googFirsSentValue=0
    googPlisSentValue=0
    googNacksSentValue=0
    googNacksReceivedValue=0
    googFirsReceivedValue=0
    googPlisReceivedValue=0

    f=open("/webrtc_internals_dump.txt")
    lines=f.readlines();
    for r, line in enumerate(lines):
        if "ssrc" in line:
            if "recv-bytesReceived" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                bytesReceivedValues.append(float(values[len(values) -1])); #ADD
            elif "recv-bitsReceivedPerSecond" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    bitsReceivedPerSecondValues.append(float(value)) #Average
            elif "recv-packetsLost" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    recvpacketsLostValues.append(float(value)) #Average
            elif 'recv-packetsReceived"' in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                packetsReceivedValues.append(float(values[len(values) -1])) #Add
            elif "recv-packetsReceivedPerSecond" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    packetsReceivedPerSecondValues.append(float(value)) #Average
            elif "recv-googJitterBufferMs" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    googJitterBufferMsValues.append(float(value)) #Average
            elif "recv-googNacksSent" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                googNacksSentValue = float(values[len(values) -1]) #Average
            elif "recv-googFirsSent" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                googFirsSentValue = float(values[len(values) -1]) #Average
            elif "recv-googPlisSent" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                googPlisSentValue = float(values[len(values) -1]) #Average
            elif "recv-googPreferredJitterBufferMs" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    googPreferredJitterBufferMsValues.append(float(value)) #Average
            elif "send-googNacksReceived" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                googNacksReceivedValue = float(values[len(values) -1]) #Average
            elif "send-googFirsReceived" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                googFirsReceivedValue = float(values[len(values) -1]) #Average
            elif "send-googPlisReceived" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                googPlisReceivedValue = float(values[len(values) -1]) #Average
            elif "send-bytesSent" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                bytesSentValues.append(float(values[len(values) -1])) #ADD
            elif "send-bitsSentPerSecond" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    bitsSentPerSecondValues.append(float(value)) #Average
            elif 'send-packetsSent"' in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                packetsSentValues.append(float(values[len(values) -1])) #ADD
            elif "send-packetsSentPerSecond" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    packetsSentPerSecondValues.append(float(value)) #Average
            elif "send-packetsLost" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    sendpacketsLostValues.append(float(value)) #
            elif "send-googRtt" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    googRttValues.append(float(value)) #Average
            elif "send-googRtt" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    googRttValues.append(float(value)) #Average
        if "bweforvideo" in line: #Optional but not displayed
            if "googAvailableReceiveBandwidth" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    googAvailableReceiveBandwidthValues.append(float(value)) #Average
            elif "googAvailableSendBandwidth" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    googAvailableSendBandwidthValues.append(float(value)) #Average
            elif "googTransmitBitrate" in line:
                aux = lines[r+3].split(":")[1]
                values = str(aux).replace("[","").replace("]","").replace(" ","").replace('"',"")
                values = values.split(",")
                for i,value in enumerate(values):
                    googTransmitBitrateValues.append(float(value)) #Average

    #print ("# --------------------- Generic information -------------------- #")
    #print ("Total bytes received [KB]: "+str(int(sum(bytesReceivedValues)/1000)))
    print ("Average bits received per second [Kb/s]: "+str(int(Average(bitsReceivedPerSecondValues)/1000)))
    print ("Average received packet loss: "+str(int(sum(recvpacketsLostValues))))
    #print ("Total received packet: "+str(int(sum(packetsReceivedValues))))
    #print ("Average packets received per second [packets/s]: "+str(int(Average(packetsReceivedPerSecondValues))))
    #print ("Average of jitter buffer [ms]: "+str(int(Average(googJitterBufferMsValues))))
    #print ("Average of preferred jitter buffer [ms]: "+str(int(Average(googPreferredJitterBufferMsValues))))
    #print ("Total bytes sent [KB]: "+str(int(sum(bytesSentValues)/1000)))
    print ("Average bits sent per second [Kb/s]: "+str(int(Average(bitsSentPerSecondValues)/1000)))
    #print ("Average packets sent per second [packets/s]: "+str(int(Average(packetsReceivedPerSecondValues))))
    print ("Average sent packet loss: "+str(int(sum(sendpacketsLostValues))))
    print ("NACK messages received: "+str(int(googNacksReceivedValue)))
    print ("Total sent packet: "+str(int(sum(packetsSentValues))))
    print ("Average sent round trip time, RTT [ms]: "+str(int(Average(googRttValues))))
    #print ("# ----------------- Specific video information ----------------- #")
    #print ("PLI messages received: "+str(int(googPlisReceivedValue)))
    #print ("FIR messages received: "+str(int(googFirsReceivedValue)))
    #print ("NACK messages sent: "+str(int(googNacksSentValue)))
    #print ("PLI messages sent: "+str(int(googPlisSentValue)))
    #print ("FIR messages sent: "+str(int(googFirsSentValue)))

    #if (int(Average(googRttValues))>80):
        #print("Round Trip Time (RTT) value: "+str(int(Average(googRttValues))))
        #print("The Round Trip Time (RTT) value is greater than 80 ms")
        #print("TEST FAILED")
    #else:
        #print("Round Trip Time (RTT) value: "+str(int(Average(googRttValues))))
        #print("The Round Trip Time (RTT) value is lower than 80 ms")
        #print("TEST PASSED")
# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)

def main():
    parser()

if __name__ == '__main__':
    main()
