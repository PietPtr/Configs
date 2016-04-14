#!/usr/bin/python

from __future__ import division
import time
import os

print "Starting memory script"

while True:
    rawoutput = os.popen("cat /proc/meminfo | grep MemTotal").read()
    splitoutput = filter(None, rawoutput.split(' '))
    
    totalMemory = (int(splitoutput[1]) / 1024)

    rawoutput = os.popen("cat /proc/meminfo | grep Active:").read()
    usedMemory = int((filter(None, rawoutput.split(' ')))[1]) / 1024


    os.popen("echo " + str(int(totalMemory)) + " > /home/pieter/.XmobarValues/totalMemory")
    os.popen("echo " + str(int(usedMemory )) + " > /home/pieter/.XmobarValues/usedMemory ")

    time.sleep(7)
