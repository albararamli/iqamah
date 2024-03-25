import os
from fun_sbr import *
import RPi.GPIO as GPIO
GPIO.setwarnings(False) 

import time
import sys

#exit the file if the device is not a mic device
if(device_type!='mic'):
    sys.exit() 
        
dir_local=path_sh
dir_local_mic=path_py

status_web=-1 #blue led status 0,1
file_web=path_data+'mic_status_web.txt'
#status_local=0 #green led status 0,1
file_relay=path_data+'mic_status_relay.txt'

GPIO.setmode(GPIO.BOARD)

print("Progress")

GPIO.setup(LED_RED,GPIO.OUT)
GPIO.setup(LED_GREEN,GPIO.OUT)
GPIO.setup(LED_YELLOW,GPIO.OUT)

GPIO.setup(SWITCH_YELLOW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)

status_web= get_it(file_web)


# Function to check switch state
def check_yellow_switch():
    if GPIO.input(SWITCH_YELLOW) == GPIO.LOW:
        #if(status_web==1):
        sys.argv = ['0','WEB_OFF']
        runx(dir_local_mic+'mic_control.py')
        time.sleep(0.1)
        ###
        sys.argv = ['0','RELAY_OFF']
        runx(dir_local_mic+'mic_control.py')
        time.sleep(0.1)
        return "Pressed"
    else:
        return "Not Pressed"

# Function to check switch state
def check_red_switch():
    if GPIO.input(SWITCH_RED) == GPIO.LOW:
        #if(status_web==1):
        sys.argv = ['0','WEB_OFF']
        runx(dir_local_mic+'mic_control.py')
        time.sleep(0.1)
        ###
        sys.argv = ['0','RELAY_ON']
        runx(dir_local_mic+'mic_control.py')
        time.sleep(0.1)
        return "Pressed"
    else:
        return "Not Pressed"


# Main function to test the switch

while True:
    try:
        yellow_state = check_yellow_switch()
        red_state = check_red_switch()
    except:
        pass
