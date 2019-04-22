import RPi.GPIO as GPIO
from fun_sbr import *
import os
import json
import requests
import sys
import time

# cd to Script Directory
##scriptDirectory = os.path.dirname(os.path.realpath(sys.argv[0]))
##os.chdir(scriptDirectory)
dir_local=path_sh ##scriptDirectory+'/../sh/'
dir_local_mic=path_py #scriptDirectory

### Load server link
##dir_online_file = open("../../credentials/serverPath.txt", "r")
dir_online = app_url +'pi/'# the server path already a global variable #dir_online_file.read()

###### To send the current status in RP
status_web=-1 #blue led status 0,1
status_local=-1 #green led status 0,1
status_screen=0 #screen status 0,1
status_autoscreen=0 #screen status 0,1
status_chrome=0 #chrome status 0,1
file_relay=path_data+'mic_status_relay.txt'
file_web=path_data+'mic_status_web.txt'
file_screen=path_data+'screen_status.txt'
file_autoscreen=path_data+'autoscreen_status.txt'
file_chrome=path_data+'chrome_status.txt'
####
while True:
    try:
    ######
        title= ""
        status= ""
        status_web=str(get_it(file_web)) # get the blue led status 0,1 from the file status_web.txt
        status_local=str(get_it(file_relay)) # get the relay status 0,1 (as well as green led status) from the file status_relay.txt
        status_screen=str(get_it(file_screen))
        status_autoscreen=str(get_it(file_autoscreen))
        status_chrome=str(get_it(file_chrome))
        h=requests.get(dir_online+'make.php?city='+city+'&device_id='+device_id+'&device_type='+device_type+'&'+'action=update&status_chrome='+status_chrome+'&status_autoscreen='+status_autoscreen+'&status_screen='+status_screen+'&status_web='+status_web+'&status_local='+status_local)
      ######
        r = requests.get(dir_online+ city+'/'+device_id+'/internet.json')

        if r.status_code != 404:
            x=r.json()
            # print x
            title= x['posts'][0]['title']
            status= x['posts'][0]['status']
            r = requests.get(dir_online+'make.php?city='+city+'&device_id='+device_id+'&device_type='+device_type+'&'+'action=rm')
    ####################
        if(title=="RELAY" and device_type!='monitor'):
            if(status=="ON"):
                    sys.argv = ['0','RELAY_ON']
            else:
                sys.argv = ['0','RELAY_OFF']
            execfile(dir_local_mic+'mic_control.py')
    ####################
        if(title=="WEB" and device_type!='monitor'  ):
            if(status=="ON"):
                sys.argv = ['0','WEB_ON']
            else:
                sys.argv = ['0','WEB_OFF']
            execfile(dir_local_mic+'mic_control.py')
    ####################
        if(title=="PI"):
            if(status=="REBOOT"):
                GPIO.cleanup()
                os_system('reboot')
    ####################
        if(title=="CHROME" and device_type!='mic'):
            if(status=="ON"):
                do_it(1,file_chrome)
                try:
                    time.sleep(1.0)
                    os_system('sh '+dir_local+'Chromium_Open.sh &')
                except:
                    pass

                
            if(status=="OFF"):
                do_it(0,file_chrome)
                try:
                    os_system('pkill chromium')
                    time.sleep(1.0)
                    os_system('sh '+dir_local+'Chromium_Close.sh &')
                except:
                    pass
                
                
    ####################
        if(title=="SCREEN" and device_type!='mic'):
            if(status=="ON"):
                #dummyVariable=1
                #vcgencmd display_power 1
                '''
                os_system('sh '+dir_local+'Chromium_Open.sh &')
                time.sleep(1.0)
                '''
                os_system('sh '+dir_local+'screen_on.sh')
            if(status=="OFF"):
                #dummyVariable=0
                #vcgencmd display_power 0
                '''
                os_system('sh '+dir_local+'Chromium_Close.sh &')
                time.sleep(1.0)
                '''
                os_system('sh '+dir_local+'screen_off.sh')
    ####################
        if(title=="AUTOSCREEN" and device_type!='mic'):
            if(status=="ON"):
                do_it(1,file_autoscreen)
            if(status=="OFF"):
                do_it(0,file_autoscreen)
        else:
            #print ("There is no acion online")
            time.sleep(1.0)
    ####################
    except:
        pass
