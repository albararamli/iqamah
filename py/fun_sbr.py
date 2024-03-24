import os
import sys

def runx(filex):
    if sys.version_info.major==2:
        execfile(filex)
    else:
        exec(open(filex).read())
        
def os_system(command):
    try:
        #os.system("set +e")
        os.system(""+command)
        #os.system("set -e")
        print ("Done: "+command)
    except:
        print ("Error: "+command)
        pass
#------------------------------------------------------------------
def swap_it(status): #swap the status from 0 to 1 or opposite
    if(status==0):
        status=1
    else:
        status=0
    return status
#------------------------------------------------------------------
def get_it(file): #get the status from the file status.txt
    status=0
    # read the file status.txt to get the status of the mic
    i=0
    if os.path.exists(file):
        with open(file) as fp:
            for line in fp:
                if(i==0): status=int(line.rstrip('\n'))
                i+=1
    return status
#------------------------------------------------------------------
def do_it(status,file): #wtite the status to the file status.txt
    f = open(file,'w')
    f.write(str(status))
    f.close()
    return status
#------------------------------------------------------------------
#get the config form config.txt, 
# orx=0 city name  
# orx=1 device_id
# orx=2 device_type
# orx=3 url
def get_line_form_file(file,orx): 
    status=''
    # read the file status.txt to get the status of the mic
    i=0
    if os.path.exists(file):
        with open(file) as fp:
            for line in fp:
                if(i==orx): status=line.rstrip('\n')
                i+=1
    return status
#------------------------------------------------------------------
#def do_config(file): #wtite the status to the file cinfig.txt
#    f = open(file,'w')
#    f.write(str(city+'\n'))
#    f.write(str(device_id+'\n'))
#    f.write(str(device_type+'\n'))
#    f.write(str(app_url+'\n'))
#    f.close()
#------------------------------------------------------------------

#do_config('../config.txt') # to save the configuration in the file

# cd to Script Directory
scriptDirectory = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(scriptDirectory)
path_config=scriptDirectory+'/../'
path_sh=path_config+'sh/'
path_py=path_config+'py/'
path_data=path_config+'data/'

config_file=path_config+'config.txt'

city       =get_line_form_file(config_file,0) # davis vs sac vs brentwood
device_id  =get_line_form_file(config_file,1) # 1 vs 2 vs 3
device_type=get_line_form_file(config_file,2) # monitor vs mic vs ''
app_url    =get_line_form_file(config_file,3) # http://albara.ramli.net/iqamah/
screen_size    =get_line_form_file(config_file,4) # 27 vs 7

RELAY_1=12
RELAY_2=16#Amp
RELAY_3=18#Mixer
RELAY_4=22#Wireless mic
RELAY_5=32
RELAY_6=36
RELAY_7=38
RELAY_8=40#External Speaker

'''
LED_RED=15
LED_BLUE=33
LED_GREEN=31
LED_WHITE=37
LED_YELLOW=29

HCSR04_1_TRIG=13
HCSR04_1_ECHO=35
'''


LED_RED=11#15
LED_BLUE=15#33
LED_GREEN=24#31
LED_YELLOW=26#29

LED_WHITE=33#37

HCSR04_1_TRIG=13
HCSR04_1_ECHO=35
