from fun_sbr import *
import os
import sys

#exit the file if the device is not a monitor device
if(device_type=='mic'):
    sys.exit() 
    
    
import time
import socket
REMOTE_SERVER = "www.google.com"
def is_connected():
  try:
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
    pass
    return False
time.sleep(15)
tx = time.asctime( time.localtime(time.time()) )
print "Starting ",tx
ppx="Starting "+tx
os_system("echo \""+ppx+"\" >> "+path_data+"internet_status.txt")
inix0=is_connected()
time.sleep(2)
inix1=is_connected()
if inix0!=inix1:
  inix=True #is_connected()
else:
  inix=inix0

nextx=inix


dir_local=path_sh
file_chrome=path_data+'chrome_status.txt'
pass_ini=1
while 1:
  ##print "Loop"
  #ppx="loop"
  #os.system("echo \""+ppx+"\" >> /home/pi/rpiMasjidDisplay/sh/internet_status.txt")
  time.sleep(2)
  nextx0=is_connected()
  time.sleep(2)
  nextx1=is_connected()
  if nextx0!=nextx1:
    #time.sleep(2)
    nextx=True #is_connected()
  else:
    nextx=nextx0

  #ppx="S(0)="+ str(nextx0)+ " S(1)=" + str(nextx1)+ " S(Final)=" + str(nextx)+ " "+tx
  #os.system("echo \""+ppx+"\" >> /home/pi/rpiMasjidDisplay/sh/internet_status.txt")
  #print ppx
  if nextx!=inix:
    tx = time.asctime( time.localtime(time.time()) )

    print "From=", inix, " To=" , nextx, " ", tx
    ppx="From="+ str(inix)+ " To=" + str(nextx)+ " "+tx
    os_system("echo \""+ppx+"\" >> "+path_data+"internet_status.txt")
    if nextx == True:
      pass_ini=1
      tx = time.asctime( time.localtime(time.time()) )
      print "Wake", tx
      ppx="Wake "+tx
      os_system("echo \""+ppx+"\" >> "+path_data+"internet_status.txt")
      os_system("sh "+dir_local+'Chromium_Close.sh &')
      time.sleep(1.0)
      ##do_it(1,file_chrome)
      os_system("sh "+dir_local+'Chromium_Open.sh &')
      time.sleep(1)
    else:
      pass_ini=0
      tx = time.asctime( time.localtime(time.time()) )
      print "Sleep", tx
      ppx="Sleep "+tx
      os_system("echo \""+ppx+"\" >> "+path_data+"internet_status.txt")
      os_system("sh "+dir_local+'Chromium_Close.sh &')
      time.sleep(1.0)
      ##do_it(1,file_chrome)
      os_system("sh "+dir_local+'Chromium_Open_Local.sh &')
      time.sleep(1)
  else:
    if nextx==inix:
      if nextx==False:
        if pass_ini==1:
          tx = time.asctime( time.localtime(time.time()) )
          print "Down=[", pass_ini, "] ", tx
          ppx="Down=["+str(pass_ini)+"] "+tx
          os_system("echo \""+ppx+"\" >> "+path_data+"internet_status.txt")
          os_system("sh "+dir_local+'Chromium_Close.sh &')
          time.sleep(1.0)
          ##do_it(1,file_chrome)
          os_system("sh "+dir_local+'Chromium_Open_Local.sh &')
          time.sleep(1)
        pass_ini=0
      else:
        pass_ini=1
  inix=nextx
