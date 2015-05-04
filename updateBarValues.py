from __future__ import division
import time
import os

dataReceivedOnBootRaw = os.popen("cat ~/.XmobarValues/EthernetDataRawDn").read()
dataTransmittedOnBoot = os.popen("cat ~/.XmobarValues/EthernetDataRawUp").read()

while True:
    hours = os.popen("sudo smartctl /dev/sdc -a | grep 'Power_On_Hours'").read()
    SMART5 = os.popen("sudo smartctl /dev/sdc -a | grep 'Reallocated_Sector_Ct'").read()
    SMART197 = os.popen("sudo smartctl /dev/sdc -a | grep 'Current_Pending_Sector'").read()
    SMART198 = os.popen("sudo smartctl /dev/sdc -a | grep 'Offline_Uncorrectable'").read()
    hours = hours[len(hours)-8:len(hours)-1].strip()
    SMART5 = SMART5[len(SMART5)-8:len(SMART5)-1].strip()
    SMART197 = SMART197[len(SMART197)-8:len(SMART197)-1].strip()
    SMART198 = SMART198[len(SMART198)-8:len(SMART198)-1].strip()

    dataReceivedThisSessionRaw = os.popen("ifconfig | grep 'RX bytes' -m 1").read().split(' ')[11].split(':')[1]
    dataTransmittedThisSession = os.popen("ifconfig | grep 'TX bytes' -m 1").read().split(' ')[16].split(':')[1]

    warning = int(SMART5) + int(SMART197) + int(SMART198)

    os.popen("echo " + str(int(dataReceivedOnBootRaw) + int(dataReceivedThisSessionRaw)) + " > /home/pieter/.XmobarValues/EthernetDataRawDn") #save the new total
    os.popen("echo " + str(round(((int(dataReceivedOnBootRaw) + int(dataReceivedThisSessionRaw)) / 1024.0 / 1024.0 / 1024.0), 2)) + " > /home/pieter/.XmobarValues/EthernetDataDn")

    os.popen("echo " + str(int(dataTransmittedOnBoot) + int(dataTransmittedThisSession)) + " > /home/pieter/.XmobarValues/EthernetDataRawUp") #save the new total
    os.popen("echo " + str(round(((int(dataTransmittedOnBoot) + int(dataTransmittedThisSession)) / 1024.0 / 1024.0 / 1024.0), 2)) + " > /home/pieter/.XmobarValues/EthernetDataUp")

    os.popen("echo " + hours + " > //home//pieter//.XmobarValues//HDDPowerOnHours")
    os.popen("echo " + str(warning) + " > //home//pieter//.XmobarValues//WarningValue")
    #print (os.popen("date").read())

    time.sleep(30)
