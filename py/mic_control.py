import os
#   Parameter fetch by this file
#   WEB_ON
#   WEB_OFF
#   RELAY_ON
#   RELAY_OFF
from fun_sbr import *
import time
import RPi.GPIO as GPIO

#exit the file if the device is not a mic device
if(device_type=='monitor'):
    sys.exit()
    
RELAY_1=12
RELAY_2=16#Amp
RELAY_3=18#Mixer
RELAY_4=22#Wireless mic
RELAY_5=32
RELAY_6=36
RELAY_7=38
RELAY_8=40#External Speaker

LED_RED=33
LED_BLUE=29
LED_GREEN=35

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_BLUE, GPIO.OUT)#blue led

##GPIO.setup(40, GPIO.OUT)#Control the Relay
GPIO.setup(RELAY_2, GPIO.OUT)#Control the Relay
GPIO.setup(RELAY_3, GPIO.OUT)#Control the Relay
GPIO.setup(RELAY_4, GPIO.OUT)#Control the Relay

GPIO.setup(LED_RED, GPIO.OUT)#Red led
GPIO.setup(LED_GREEN, GPIO.OUT)#the Green led
#GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#the Blue switch
#GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#the Red switch

status_web=-1 #blue led status 0,1
status_local=-1 #green led status 0,1
file_relay=path_data+'mic_status_relay.txt'
file_web=path_data+'mic_status_web.txt'
############################################################################
import sys
i=0
x=0
for arg in sys.argv:
    if(i==1):
        x=arg
    i=i+1
############################################################################
# get the blue led status 0,1 from the file status_web.txt
if(x=="WEB_ON"):
    status_web=1
if(x=="WEB_OFF"):
    status_web=0
#########
if(status_web!=-1):
    GPIO.output(LED_BLUE,status_web) #blue led
    do_it(status_web,file_web) # wite the blue led status in the file status_web.txt
    print ("Web-->",status_web)
############################################################################
 # get the relay status 0,1 (as well as green led status) from the command
if(x=="RELAY_ON"):
    status_local=1
if(x=="RELAY_OFF"):
    status_local=0
#########
if(status_local!=-1):
    GPIO.output(LED_RED, swap_it(status_local)) #Red led
    GPIO.output(LED_GREEN, status_local)#the Green led
    ##GPIO.output(40, status_local)#Control the Relay
    RELAY_STATUS=swap_it(status_local)
    if(RELAY_STATUS==0):#ON
        TIME_WAIT=0.15
        GPIO.output(RELAY_4, RELAY_STATUS)#Control the Relay
        time.sleep(TIME_WAIT)
        GPIO.output(RELAY_3, RELAY_STATUS)#Control the Relay
        time.sleep(TIME_WAIT)
        GPIO.output(RELAY_2, RELAY_STATUS)#Control the Relay
    if(RELAY_STATUS==1):#OFF
        TIME_WAIT=0.35
        GPIO.output(RELAY_2, RELAY_STATUS)#Control the Relay
        time.sleep(TIME_WAIT)
        GPIO.output(RELAY_3, RELAY_STATUS)#Control the Relay
        time.sleep(TIME_WAIT)
        GPIO.output(RELAY_4,RELAY_STATUS)#Control the Relay

    do_it(status_local,file_relay) # wite the relay status in the file status_relay.txt
    print ("Status-->",status_local)
############################################################################
