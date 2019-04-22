#!/usr/bin/python
from fun_sbr import *
from datetime import date, datetime, time, timedelta
import time as timeSleep
import os
import sys
import subprocess

#exit the file if the device is not a monitor device
if(device_type=='mic'):
    sys.exit() 

csv_file=path_data+'parsedIqamah.csv' # we assume that the csv file already exisis, in future we have to deal with the appcenece of this file

if os.path.exists(csv_file):
    # Praery Time Import from csv
    data_of_csv=get_line_form_file(csv_file,1)
    fajrAthan = datetime.combine(date.today(), time(int(data_of_csv[0:2]),int(data_of_csv[2:4])))

    data_of_csv=get_line_form_file(csv_file,5) 
    Duha = datetime.combine(date.today(), time(int(data_of_csv[0:2]),int(data_of_csv[2:4])))

    data_of_csv=get_line_form_file(csv_file,7) 
    DhuhrAthan = datetime.combine(date.today(), time(int(data_of_csv[0:2]),int(data_of_csv[2:4])))

    data_of_csv=get_line_form_file(csv_file,17) 
    IshaIqamah = datetime.combine(date.today(), time(int(data_of_csv[0:2]),int(data_of_csv[2:4])))
else:
    sys.exit() 

# Set Delay on Screen On and Off Times
screenOnBeforeFajr = fajrAthan - timedelta(hours=1)
screenOnBeforeFajr = screenOnBeforeFajr.time()
screenOffAfterDuha = Duha + timedelta(minutes=30)
screenOffAfterDuha = screenOffAfterDuha.time()
screenOnBeforeDhuhr = DhuhrAthan - timedelta(hours=1)
screenOnBeforeDhuhr = screenOnBeforeDhuhr.time()
screenOffAfterIsha = IshaIqamah + timedelta(hours=2)
screenOffAfterIsha = screenOffAfterIsha.time()

# Define Midnight Time
Midnight = datetime.combine(date.today(), time(00, 00))
Midnight = Midnight.time()

# Simulate Current Time
# currentTime = datetime.combine(date.today(), time(12, 50))
# currentTime = currentTime.time()

'''
# Print Prayer Times for Verifiation
print("screenOnBeforeFajr: " + str(screenOnBeforeFajr))
print("screenOffAfterDuha: " + str(screenOffAfterDuha))
print("screenOnBeforeDhuhr: " + str(screenOnBeforeDhuhr))
print("screenOffAfterIsha: " + str(screenOffAfterIsha))
'''
#while True:
# Check Server Screen Status
autoscreen_file=path_data+"autoscreen_status.txt"
if os.path.exists(autoscreen_file):
    autoScreenStatusFile = open(autoscreen_file, "r")
    autoScreenStatus = autoScreenStatusFile.readline(1)
    print "auto file exsist="+autoScreenStatus
else:
    autoScreenStatus = "1"
    print "auto file Not exsist="+autoScreenStatus
'''
screen_file=path_data+"screen_status.txt"
if os.path.exists(screen_file):
    screenStatusFile = open(screen_file, "r")
    screenStatus = screenStatusFile.readline(1)
    print "screen file exsist="+screenStatus
else:
    screenStatus = "0"
    print "screen file Not exsist="+screenStatus
'''
comm=""
ran=""
used="no"
# If There is No Override, Run Screen Check Schedule
if autoScreenStatus == "1":
    # Check Current Time
    currentTime = datetime.now().time()
    if screen_size=="27":
        # Check real time screenStatus from shell
        output = subprocess.check_output("vcgencmd display_power", shell=True)
        screenStatus = output[14]
    if screen_size=="7":
        output2 = subprocess.check_output("cat /sys/class/backlight/rpi_backlight/bl_power", shell=True)
        screenStatus = output2[0]
        if output2[0]=="0":
            screenStatus="1"
        else:
            screenStatus="0"
    if screen_size!="27" and screen_size!="7":
        print "screenStatus="+"Not here"
    else:
        print "screenStatus="+screenStatus

    
    # Turn Screen On for Fajr
    print str(currentTime )+">="+str( screenOnBeforeFajr)+" and " +str(currentTime )+"<"+str(  screenOffAfterDuha)
    if currentTime >= screenOnBeforeFajr and currentTime < screenOffAfterDuha:
        print "Turn Screen On for Fajr"
        used="yes"
        if screenStatus == "0":
            comm="on"
            ran="1"
            
    # Turn Screen On for day
    print str(currentTime )+"<"+str( screenOffAfterIsha)
    if currentTime < screenOffAfterIsha:
        print str(IshaIqamah.time() )+">"+str( screenOffAfterIsha)
        if IshaIqamah.time() > screenOffAfterIsha:
            print "Turn Screen On for ishaa after 12"
            used="yes"
            if screenStatus == "0":
                comm="on"
                ran="2"
    else:
        print str(currentTime)+">="+str( screenOnBeforeDhuhr)
        if currentTime >= screenOnBeforeDhuhr:
            print "Turn Screen On for the day"
            used="yes"
            if screenStatus == "0":
                comm="on"
                ran="3"
            
    if used!="yes":
        print "Turn Screen On other wise"
        used="yes"
        if screenStatus == "1":
            comm="off"
            ran="4"
    '''
    # Turn Screen On for Fajr
    if currentTime >= screenOnBeforeFajr and currentTime < screenOffAfterDuha:
        print "Turn Screen On for Fajr"
        if screenStatus == "0":
            comm="on"
            ran="1"

    # Turn Screen Off After Fajr
    if currentTime >= screenOffAfterDuha and currentTime < screenOnBeforeDhuhr:
        print "Turn Screen Off After Fajr"
        if screenStatus == "1":
            comm="off"
            ran="2"
            
    # Turn Screen On Before Dhuhr
    if currentTime >= screenOnBeforeDhuhr and currentTime < screenOffAfterIsha and IshaIqamah.time() < screenOffAfterIsha:
        print "Turn Screen On Before Dhuhr"
        if screenStatus == "0":
            comm="on"
            ran="3"
            
    # Turn Screen On Before Dhuhr
    if currentTime >= screenOnBeforeDhuhr and currentTime > screenOffAfterIsha  and IshaIqamah.time() > screenOffAfterIsha:
        print "Turn Screen On Before Dhuhr"
        if screenStatus == "0":
            comm="on"
            ran="3"
            
    # Turn Screen Off After Isha
    if currentTime >= screenOffAfterIsha and IshaIqamah.time() < screenOffAfterIsha:
        # if the screenOffAfterIsha >=00:00 I have to deal with it becouase it should be for next day not the same day. Now I just let the time less than 12
        print "Turn Screen Off After Isha"
        if screenStatus == "1":
            comm="off"
            ran="4"
            
     # Turn Screen Off for the Night
    if currentTime < screenOnBeforeFajr:
        # if the screenOffAfterIsha >=00:00 I have to deal with it becouase it should be for next day not the same day. Now I just let the time less than 12
        print "Turn Screen Off for the Night"
        if screenStatus == "1":
            comm="off"
            ran="4"
    '''
    if comm=="on":
        print "Turn ON"
        '''
        os_system('sh '+dir_local+'Chromium_Open.sh &')
        time.sleep(1.0)
        '''
        os_system('sh '+path_sh+'screen_on.sh')
        
    if comm=="off":     
        print "Turn OFF"
        '''
        os_system('sh '+dir_local+'Chromium_Close.sh &')
        time.sleep(1.0)
        '''
        os_system('sh '+path_sh+'screen_off.sh')

print "comm="+ran+"   "+"comm="+comm
'''
print "comm="+ran+"   "+"comm="+comm+"   "+str(currentTime )+">="+str( screenOnBeforeFajr)+" and " +str(currentTime )+"<"+str(  screenOffAfterDuha)
print "comm="+ran+"   "+"comm="+comm+"   "+str(currentTime )+">="+str( screenOffAfterDuha)+" and " +str(currentTime )+"<"+str(  screenOnBeforeDhuhr)
print "comm="+ran+"   "+"comm="+comm+"   "+str(currentTime )+">="+str( screenOnBeforeDhuhr)+" and "+str(currentTime )+"<"+str(  screenOffAfterIsha)
print "comm="+ran+"   "+"comm="+comm+"   "+str(currentTime )+">="+str( screenOffAfterIsha)+" or "  +str(currentTime )+"<"+str(  screenOnBeforeFajr)
'''
# Sleep for a second before rerunning the loop
#timeSleep.sleep(1)
