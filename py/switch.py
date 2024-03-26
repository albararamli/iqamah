import os
import sys
import time
import RPi.GPIO as GPIO
from fun_sbr import *

GPIO.setwarnings(False)

# Exit the file if the device is not a mic device
if device_type != 'mic':
    sys.exit()

dir_local = path_sh
dir_local_mic = path_py

status_web = -1  # blue led status 0,1
file_web = path_data + 'mic_status_web.txt'
file_relay = path_data + 'mic_status_relay.txt'

GPIO.setmode(GPIO.BOARD)

print("Progress")

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)

GPIO.setup(SWITCH_YELLOW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)

status_web = get_it(file_web)

# Function to check switch state
def check_yellow_switch():
    if GPIO.input(SWITCH_YELLOW) == GPIO.LOW:
        return "Pressed"
    else:
        return "Not Pressed"

# Function to check switch state
def check_red_switch():
    if GPIO.input(SWITCH_RED) == GPIO.LOW:
        return "Pressed"
    else:
        return "Not Pressed"

# Main function to test the switch

start_time_yellow = None
start_time_red = None
while True:
    try:
        yellow_state = check_yellow_switch()
        red_state = check_red_switch()

        # Check if yellow button is pressed
        if yellow_state == "Pressed":
            if start_time_yellow is None:
                start_time_yellow = time.time()  # Start counting time
            elif time.time() - start_time_yellow >= 2:  # Check if 2 seconds elapsed
                print("Yellow button pressed continuously for 2 seconds.")
                #################################################
                sys.argv = ['0', 'WEB_OFF']
                runx(dir_local_mic + 'mic_control.py')
                time.sleep(0.1)
                sys.argv = ['0', 'RELAY_OFF']
                runx(dir_local_mic + 'mic_control.py')
                time.sleep(0.1)
                print("YELLOW PRESSED")
                #################################################
                start_time_yellow = None  # Reset start time
                # Do whatever you need to do when yellow button is pressed for 10 seconds

        else:
            start_time_yellow = None  # Reset start time if button is released

        # Check if red button is pressed
        if red_state == "Pressed":
            if start_time_red is None:
                start_time_red = time.time()  # Start counting time
            elif time.time() - start_time_red >= 2:  # Check if 2 seconds elapsed
                print("Red button pressed continuously for 2 seconds.")
                ##################################################
                sys.argv = ['0', 'WEB_OFF']
                runx(dir_local_mic + 'mic_control.py')
                time.sleep(0.1)
                sys.argv = ['0', 'RELAY_ON']
                runx(dir_local_mic + 'mic_control.py')
                time.sleep(0.1)
                print("RED PRESED")
                ##################################################
                start_time_red = None  # Reset start time
                # Do whatever you need to do when red button is pressed for 10 seconds

        else:
            start_time_red = None  # Reset start time if button is released

    except Exception as e:
        print("Error occurred:", e)
