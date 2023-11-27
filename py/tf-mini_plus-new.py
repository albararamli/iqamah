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
import serial
import time

ser = serial.Serial("/dev/ttyAMA0", 115200)
#ser = serial.Serial(port='/dev/ttyAMA0',baudrate = 115200)

def getTFminiData():
    global ser
    n=0
    k=0
    while True:
        #################
        while get_it(file_web)==0:
            GPIO.output(LED_YELLOW,True)
            time.sleep(0.15)
            GPIO.output(LED_YELLOW,False)
            time.sleep(0.15)
        status_web= get_it(file_web)
        #print("WEB==> ",status_web)
        #################
        try:
            ser = serial.Serial("/dev/ttyAMA0", 115200)
            #ser.open()
            #print(ser)
            #time.sleep(0.25)
            count = ser.in_waiting
            #print(count)
            if count > 8:
                recv = ser.read(9)   
                #print(recv)
                ser.reset_input_buffer() 
                # type(recv), 'str' in python2(recv[0] = 'Y'), 'bytes' in python3(recv[0] = 89)
                # type(recv[0]), 'str' in python2, 'int' in python3 
                
                if recv[0] == 0x59 and recv[1] == 0x59:     #python3
                    print("###")
                    distance = recv[2] + recv[3] * 256
                    strength = recv[4] + recv[5] * 256
                    print(distance, strength)
                    ser.reset_input_buffer()
                    
                if recv[0] == 'Y' and recv[1] == 'Y':     #python2
                    print("@@@@")
                    lowD = int(recv[2].encode('hex'), 16)      
                    highD = int(recv[3].encode('hex'), 16)
                    lowS = int(recv[4].encode('hex'), 16)      
                    highS = int(recv[5].encode('hex'), 16)
                    distance = lowD + highD * 256
                    strength = lowS + highS * 256
                    print(distance, strength)
                
                ###################
                if strength>=1000:
                    ########################
                    #status_web=get_it(file_web) # get the blue led status 0,1 from the file status_web.txt
                    if(status_web==1):
                        sys.argv = ['0','RELAY_ON']
                        runx(dir_local_mic+'mic_control.py')
                        time.sleep(1800)#Here is was 600=10min
                        #GPIO.output(LED_GREEN,False)
                        '''if(GPIO.input(LED_GREEN)==0):
                            for i in range(0,0):
                                GPIO.output(LED_GREEN,True)
                                time.sleep(0.15)
                                GPIO.output(LED_GREEN,False)
                                time.sleep(0.15)'''
                            #GPIO.output(LED_GREEN,True)
                    ########################
                else:
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
                # you can also distinguish python2 and python3: 
                #import sys
                #sys.version[0] == '2'    #True, python2
                #sys.version[0] == '3'    #True, python3
            ser.close()
        except Exception as e:
            ser.close()
            #time.sleep(0.25)
            print(e)

if __name__ == '__main__':
    try:
        if ser.is_open == False:
            ser.open()
        getTFminiData()
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()
