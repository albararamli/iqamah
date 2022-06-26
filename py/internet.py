from fun_sbr import *
import os
import sys
##############################
import json
import datetime
import re
##################
def update_local_change(x,letter='A',num='0',put=':)'):
  y=re.findall('<span id="'+letter+num+'">.*</span>', x)
  #print(y)
  w = re.sub(">.*<", ">"+put+"<", y[0])
  #print(w)
  x=re.sub(y[0],w,x)
  return x
##################
def update_local():
  f1 = open(path_data+"local.html")
  x=f1.read()
  the_time_now = datetime.datetime.now()
  f2 = open(path_data+str(the_time_now.year)+'.json')
  data = json.load(f2)
  n=0
  for row in data:
    if n!=0:
      y=int(str(row[0]).strip())
      m=int(str(row[1]).strip())
      d_name=str(row[2]).strip() 
      d=int(str(row[3]).strip())
      if the_time_now.year==y and the_time_now.month==m and the_time_now.day==d:
      #if 2022==y and 1==m and 7==d:
        ######
        prayer_id=4
        for i in range(0,6):
          x=update_local_change(x,letter='A',num=str(i),put=str(row[prayer_id]).strip())
          prayer_id=prayer_id+1
          x=update_local_change(x,letter='I',num=str(i),put=str(row[prayer_id]).strip())
          prayer_id=prayer_id+1
          if d_name == "Friday" and i==2 and prayer_id==10:
            #print(d_name,i,prayer_id)
            x=update_local_change(x,letter='T',num=str(i),put="Jumuah")
    n=n+1
  f1.close()
  f2.close()
  #########
  f3 = open(path_data+"output.html","w")
  f3.write(x)
  f3.close()
##############################
#exit the file if the device is not a monitor device
if(device_type=='mic'):
    sys.exit() 
    
    
import time
'''
import socket
REMOTE_SERVER = "www.google.com"
def is_connected():
  socket.setdefaulttimeout(10)
  try:
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
    #pass
    return False
'''
#########################
import requests
def is_connected():
  r= False
  try:
    req = requests.request('GET', 'https://www.google.com',timeout=(10))
    r= True
  except:
    r= False
  return r
#########################
time.sleep(15)
tx = time.asctime( time.localtime(time.time()) )
print("Starting ",tx)
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
  ##print("Loop")
  #ppx="loop"
  #os.system("echo \""+ppx+"\" >> /home/pi/rpiMasjidDisplay/sh/internet_status.txt")
  time.sleep(2)
  nextx0=is_connected()
  time.sleep(15)
  nextx1=is_connected()
  if nextx0!=nextx1:
    #time.sleep(2)
    nextx=True #is_connected()
  else:
    nextx=nextx0

  #ppx="S(0)="+ str(nextx0)+ " S(1)=" + str(nextx1)+ " S(Final)=" + str(nextx)+ " "+tx
  #os.system("echo \""+ppx+"\" >> /home/pi/rpiMasjidDisplay/sh/internet_status.txt")
  #print(ppx)
  if nextx!=inix:
    tx = time.asctime( time.localtime(time.time()) )

    print("From=", inix, " To=" , nextx, " ", tx)
    ppx="From="+ str(inix)+ " To=" + str(nextx)+ " "+tx
    os_system("echo \""+ppx+"\" >> "+path_data+"internet_status.txt")
    if nextx == True:
      pass_ini=1
      tx = time.asctime( time.localtime(time.time()) )
      print("Wake", tx)
      ppx="Wake "+tx
      os_system("echo \""+ppx+"\" >> "+path_data+"internet_status.txt")
      os_system("sh "+dir_local+'Chromium_Close.sh &')
      time.sleep(1.0)
      ##do_it(1,file_chrome)
      os_system("sh "+dir_local+'Chromium_Open.sh &')
      time.sleep(15)
    else:
      pass_ini=0
      tx = time.asctime( time.localtime(time.time()) )
      print("Sleep", tx)
      ppx="Sleep "+tx
      os_system("echo \""+ppx+"\" >> "+path_data+"internet_status.txt")
      os_system("sh "+dir_local+'Chromium_Close.sh &')
      time.sleep(1.0)
      ##do_it(1,file_chrome)
      update_local()
      os_system("sh "+dir_local+'Chromium_Open_Local.sh &')
      time.sleep(60)
  else:
    if nextx==inix:
      if nextx==False:
        if pass_ini==1:
          tx = time.asctime( time.localtime(time.time()) )
          print("Down=[", pass_ini, "] ", tx)
          ppx="Down=["+str(pass_ini)+"] "+tx
          os_system("echo \""+ppx+"\" >> "+path_data+"internet_status.txt")
          os_system("sh "+dir_local+'Chromium_Close.sh &')
          time.sleep(1.0)
          ##do_it(1,file_chrome)
          update_local()
          os_system("sh "+dir_local+'Chromium_Open_Local.sh &')
          time.sleep(60)
        pass_ini=0
      else:
        pass_ini=1
  inix=nextx
