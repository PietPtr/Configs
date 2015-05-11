#!/usr/bin/python

from __future__ import division
import time
import os

print "Starting..."

dataReceivedOnBootRaw = os.popen("cat ~/.XmobarValues/EthernetDataRawDn").read()
dataTransmittedOnBoot = os.popen("cat ~/.XmobarValues/EthernetDataRawUp").read()

while True:
    #-----DATA-----
    dataReceivedThisSessionRaw = os.popen("ifconfig | grep 'RX bytes' -m 1").read().split(' ')[11].split(':')[1]
    dataTransmittedThisSession = os.popen("ifconfig | grep 'TX bytes' -m 1").read().split(' ')[16].split(':')[1]

    os.popen("echo " + str(int(dataReceivedOnBootRaw) + int(dataReceivedThisSessionRaw)) + " > /home/pieter/.XmobarValues/Eth
    os.popen("echo " + str(round(((int(dataReceivedOnBootRaw) + int(dataReceivedThisSessionRaw)) / 1024.0 / 1024.0 / 1024.0),

    os.popen("echo " + str(int(dataTransmittedOnBoot) + int(dataTransmittedThisSession)) + " > /home/pieter/.XmobarValues/Eth
    os.popen("echo " + str(round(((int(dataTransmittedOnBoot) + int(dataTransmittedThisSession)) / 1024.0 / 1024.0 / 1024.0),

    #-----STORAGE-----
    rawCommand = os.popen("df | grep '/dev/sdc1'").read().split(' ')
    totalStorage = round(int(rawCommand[6]) / 1024.0 / 1024.0, 1)
    full = round(int(rawCommand[7]) / 1024.0 / 1024.0, 1)

    os.popen("echo " + str(totalStorage) + " > /home/pieter/.XmobarValues/totalStorage") #save total storage
    os.popen("echo " + str(full) + " > /home/pieter/.XmobarValues/full") #save full storage

    #print totalStorage, int(totalStorage)

    time.sleep(7)
