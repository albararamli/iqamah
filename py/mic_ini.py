#   initial status that in the files already or off if there is nothing
from fun_sbr import *
import RPi.GPIO as GPIO
import sys
import time
dir_local=path_sh
dir_local_mic=path_py

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

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)#blue led

##GPIO.setup(40, GPIO.OUT)#Control the Relay
GPIO.setup(RELAY_2, GPIO.OUT)#Control the Relay
GPIO.setup(RELAY_3, GPIO.OUT)#Control the Relay
GPIO.setup(RELAY_4, GPIO.OUT)#Control the Relay

GPIO.setup(33, GPIO.OUT)#Red led
GPIO.setup(35, GPIO.OUT)#the Green led
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#the Blue switch
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#the Red switch

status_web=-1 #blue led status 0,1
status_local=-1 #green led status 0,1
file_relay=path_data+'mic_status_relay.txt'
file_web=path_data+'mic_status_web.txt'
############################################################################
i=0
x=0
for arg in sys.argv:
    if(i==1):
        x=arg
    i=i+1
############################################################################
# get the blue led status 0,1 from the file status_web.txt
status_web=get_it(file_web) # get the blue led status 0,1 from the file status_web.txt
#########
GPIO.output(29,status_web) #blue led
do_it(status_web,file_web) # wite the blue led status in the file status_web.txt
print ("Web-->",status_web)
############################################################################
# get the relay status 0,1 (as well as green led status) from the command
status_local=get_it(file_relay) # get the relay status 0,1 (as well as green led status) from the file status_relay.txt
#########
GPIO.output(33, swap_it(status_local)) #Red led
GPIO.output(35, status_local)#the Green led
##GPIO.output(40, status_local)#Control the Relay
if(status_local==0):
    ###GPIO.output(RELAY_4, swap_it(status_local))#Control the Relay
    ###time.sleep(0.15)
    ###GPIO.output(RELAY_3, swap_it(status_local))#Control the Relay
    ###time.sleep(0.15)
    ###GPIO.output(RELAY_2, swap_it(status_local))#Control the Relay
    sys.argv = ['0','RELAY_OFF']
else:
    ###GPIO.output(RELAY_2, swap_it(status_local))#Control the Relay
    ###time.sleep(0.15)
    ###GPIO.output(RELAY_3, swap_it(status_local))#Control the Relay
    ###time.sleep(0.15)
    ###GPIO.output(RELAY_4, swap_it(status_local))#Control the Relay
    sys.argv = ['0','RELAY_ON']
execfile(dir_local_mic+'mic_control.py')

do_it(status_local,file_relay) # wite the relay status in the file status_relay.txt
print ("Status-->",status_local)
############################################################################
