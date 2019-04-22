import os
from fun_sbr import *
import RPi.GPIO as GPIO
import time
import sys

#exit the file if the device is not a mic device
if(device_type=='monitor'):
    sys.exit() 
        
dir_local=path_sh
dir_local_mic=path_py

status_web=-1 #blue led status 0,1
file_web=path_data+'mic_status_web.txt'
#status_local=0 #green led status 0,1
file_relay=path_data+'mic_status_relay.txt'

GPIO.setmode(GPIO.BOARD)

TRIG=15
ECHO=13
LED=11

print "Progress"

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(TRIG,False)

print "Wait for settle"

time.sleep(2)
k=0
pulse_start=time.time()
pulse_end=time.time()
n=0
while 1:

    #status_web= # get the blue led status 0,1 from the file status_web.txt
    while get_it(file_web)==0:
        GPIO.output(LED,0)
        #time.sleep(0.5)

    status_web= get_it(file_web)
    print "WEB==> ",status_web
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    # print "======================="
    i=0
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
        #print "ECHO Sender",i
        i=i+1
        if(i>3000):
            break
    j=0
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
        #print "ECHO Receiver",j
        j=j+1
        if(j>3000):
            break


    pulse_d=pulse_end-pulse_start

    if(i<=3000 and j<=3000):
        d=round(pulse_d*17150,2)
        k=k+1
        #print k,"] Distense=",d

        print k,"]  D=",d,"cm"
        if(d<=180):
            print "See"
            if(n<0):
                n=0
            else:
                n=n+1

            if(n>=4):
                #status_web=get_it(file_web) # get the blue led status 0,1 from the file status_web.txt
                if(status_web==1):
                    sys.argv = ['0','RELAY_ON']
                    execfile(dir_local_mic+'mic_control.py')
                    if(GPIO.input(LED)==0):
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                        time.sleep(0.15)
                        GPIO.output(LED,False)
                        time.sleep(0.15)
                        GPIO.output(LED,True)
                    #time.sleep(1)

        else:
            print "Empty=",n
            if(n>0):
                n=-1
            else:
                n=n-1
            if(n<=-1):
                if(n<=-150):
                    #status_web=get_it(file_web) # get the blue led status 0,1 from the file status_web.txt
                    if(status_web==1):
                        GPIO.output(LED,False)
                        #time.sleep(0.25)
                        sys.argv = ['0','RELAY_OFF']
                        execfile(dir_local_mic+'mic_control.py')
                    n=-1 
#GPIO.cleanup()
