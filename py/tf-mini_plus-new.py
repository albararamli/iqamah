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


# -*- coding: utf-8 -*
import time
import serial
# written by Ibrahim for Public use

# Checked with TFmini plus

# ser = serial.Serial("/dev/ttyUSB1", 115200)
T_NEW=-1
distance = -1
ser = serial.Serial("/dev/ttyS0", 115200)
# ser = serial.Serial("COM12", 115200)


# we define a new function that will get the data from LiDAR and publish it
def read_data():
    global T_NEW, distance, ser
    while True:
        try:
            #print("===>",get_it(file_web))
            #################
            while get_it(file_web)==0:
                GPIO.output(LED_YELLOW,True)
                time.sleep(0.15)
                GPIO.output(LED_YELLOW,False)
                time.sleep(0.15)
            status_web= get_it(file_web)
            #print("WEB==> ",status_web)
            #################
            #time.sleep(0.25)#waitl 0.25sec
            counter = ser.in_waiting # count the number of bytes of the serial port
            if counter > 8:
                bytes_serial = ser.read(9)
                ser.reset_input_buffer()

                if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # this portion is for python3
                    print("Printing python3 portion")            
                    distance = bytes_serial[2] + bytes_serial[3]*256 # multiplied by 256, because the binary data is shifted by 8 to the left (equivalent to "<< 8").                                              # Dist_L, could simply be added resulting in 16-bit data of Dist_Total.
                    strength = bytes_serial[4] + bytes_serial[5]*256
                    temperature = bytes_serial[6] + bytes_serial[7]*256
                    temperature = (temperature/8) - 256
                    print("Distance:"+ str(distance))
                    print("Strength:" + str(strength))
                    if temperature != 0:
                        print("Temperature:" + str(temperature))
                    ser.reset_input_buffer()

                if bytes_serial[0] == "Y" and bytes_serial[1] == "Y":
                    distL = int(bytes_serial[2].encode("hex"), 16)
                    distH = int(bytes_serial[3].encode("hex"), 16)
                    stL = int(bytes_serial[4].encode("hex"), 16)
                    stH = int(bytes_serial[5].encode("hex"), 16)
                    distance = distL + distH*256
                    strength = stL + stH*256
                    tempL = int(bytes_serial[6].encode("hex"), 16)
                    tempH = int(bytes_serial[7].encode("hex"), 16)
                    temperature = tempL + tempH*256
                    temperature = (temperature/8) - 256
                    print("Printing python2 portion")
                    print("Distance:"+ str(distance) + "\n")
                    print("Strength:" + str(strength) + "\n")
                    print("Temperature:" + str(temperature) + "\n")
                    ser.reset_input_buffer()
                ###################
                if distance>=10 and distance<=180:
                    print("ON")
                    T_NEW=time.time()
                    ########################
                    #status_web=get_it(file_web) # get the blue led status 0,1 from the file status_web.txt
                    if(status_web==1):
                        sys.argv = ['0','RELAY_ON']
                        runx(dir_local_mic+'mic_control.py')
                        #####time.sleep(1800)#Here is was 600=10min
                        #GPIO.output(LED_GREEN,False)
                        '''if(GPIO.input(LED_GREEN)==0):
                            for i in range(0,0):
                                GPIO.output(LED_GREEN,True)
                                time.sleep(0.15)
                                GPIO.output(LED_GREEN,False)
                                time.sleep(0.15)'''
                            #GPIO.output(LED_GREEN,True)
                    ########################
                elif float(time.time()-T_NEW)>=1200.0:#20min
                    print("OFF",distance,time.time(),T_NEW,time.time()-T_NEW)
                    ########################
                    #status_web=get_it(file_web) # get the blue led status 0,1 from the file status_web.txt
                    if(status_web==1):
                        sys.argv = ['0','RELAY_OFF']
                        runx(dir_local_mic+'mic_control.py')
                        #GPIO.output(LED_RED,False)
                        '''if(GPIO.input(LED_RED)==0):
                            for i in range(0,0):
                                GPIO.output(LED_RED,True)
                                time.sleep(0.15)
                                GPIO.output(LED_RED,False)
                                time.sleep(0.15)'''
                            #GPIO.output(LED_RED,True)
                    ########################
                ###################
        except Exception as e:
            print("================= EXCEPT ================",e)
            #if ser != None:
            #    ser.close()
            ser = serial.Serial("/dev/ttyS0", 115200)
            if ser.isOpen() == False:
                ser.open()
                
if __name__ == "__main__":
    while True:
        try:
            if ser.isOpen() == False:
                ser.open()
            read_data()
        except:
            if ser != None:
                ser.close()
                print("program interrupted by the user")
