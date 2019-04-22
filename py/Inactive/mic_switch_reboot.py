from fun_sbr import *
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

SWITCH_REBOOT=7
GPIO.setup(SWITCH_REBOOT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#the Reboot switch

while True:
############################################################################
    SWITCH_REBOOT_INPUT=GPIO.input(SWITCH_REBOOT)#read the Red switch
    if (SWITCH_REBOOT_INPUT==1):#read the Reboot switch
        #########
        message="reboot"
        print ("Status-->",message)
        GPIO.cleanup()
        os.system('reboot')
        time.sleep(1.50)
        #########
############################################################################

        
