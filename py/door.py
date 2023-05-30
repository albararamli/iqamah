#===========================================================================================
#===========================================================================================
#===========================================================================================
#===========================================================================================
ROOTX='/home/pi/iqamah/data/'
FILEX=ROOTX+'doorStatus.json'
side="men"#women
urlx="https://albara.ramli.net/iqamah/pi/davis/door/api.php"
import json
from datetime import date, datetime, time, timedelta
import time
import os
import os.path
import sys
import json
import requests
#import pyrebase
import json
#####################################################
#####################################################
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
########
#####################################################
#####################################################
def add_to_time(time_str,add_time):
  #time_str = '09:00:00' # Time strings
  time_tmp = datetime.strptime(time_str, '%H:%M:%S').time() # Convert time string to time object
  #print(time_str,"===========",time_tmp)
  time_obj = (datetime.combine(datetime.today(), time_tmp) + timedelta(minutes=add_time)).time()# Add 20 minutes to start_time_obj
  #print(time_str,add_time,time_obj)
  return time_obj
#####################################################
#####################################################
def today_is():
  return datetime.now().strftime('%A')
#####################################################
#####################################################
def current_time():
  formatted_time_str = datetime.now().strftime('%H:%M:%S')
  formatted_time = datetime.strptime(formatted_time_str, '%H:%M:%S').time()
  return formatted_time#time.fromisoformat(datetime.now().strftime('%H:%M:%S'))# Get the current time
#####################################################
#####################################################
def give_me(X_WHEN,X_AT,X_BY,data):
  global day_of_year
  INDEX=data[0].index(X_WHEN)
  #print(data[0][INDEX],end=" ")
  if X_AT=="Athan":
    N=0
  elif X_AT=="Iqamah":
    N=1
  ###################
  #print(X_AT,data[day_of_year][INDEX+N])
  return add_to_time(data[day_of_year][INDEX+N],int(X_BY))
#####################################################
def get_data_json():
  global day_of_year
  try:
    #####################################################
    date_string = datetime.today().strftime('%Y-%m-%d')
    #####
    ##datex = date.fromisoformat(date_string)
    datex = datetime.strptime(date_string, '%Y-%m-%d').date()
    ####
    first_day = datex.replace(month=1, day=1)
    day_of_year = (datex - first_day).days + 1
    #################
    YEAR=datetime.today().strftime('%Y')
    filename=ROOTX+YEAR+'.json'
    if os.path.isfile(filename):
      with open(filename, 'r') as f:
        data = json.load(f)
    #####################################################
    #####################################################
    for i in range(0,len(data[day_of_year])):
      target=data[day_of_year][i].strip()
      if i>=4:
        target+=":00"
      out=target
      if i>=8:
        if add_to_time(target,0) < add_to_time("12:00:00",0):
          time_12 = datetime.strptime(target+" pm", '%I:%M:%S %p')
          time_24 = time_12.strftime('%H:%M:%S')
          out=time_24
      data[day_of_year][i]=out
  except:
    return ''
  return data
#####################################################
#===============================================================================
#===========================================================================================
#===========================================================================================
#===========================================================================================
###########################################
# Initialize GPIO
###########################################
red_led_pin = 16  # brown wire
green_led_pin = 18  # white wire
relay_pin = 22  # blue wire
GPIO.setup(red_led_pin, GPIO.OUT, initial=GPIO.LOW)  # External Red LED
GPIO.setup(green_led_pin, GPIO.OUT, initial=GPIO.HIGH)  # External Green LED
GPIO.setup(relay_pin, GPIO.OUT, initial=GPIO.HIGH)  # Relay
###########################################
# Write JSON file
###########################################
def writeDoorStatusJSON(status):
  global FILEX
  try:
    with open(FILEX, 'w') as f:
      json.dump(status, f)
  except:
    pass
############################################
def ReadDoorStatusJSON():
  global FILEX
  status=''
  try:
    with open(FILEX, 'r') as f:
      status=json.load(f)["doorStatus"]
  except:
    pass
  return status
###########################################
# Open Door Function
###########################################
def openDoor():
  print("Door opend now")
  GPIO.output(relay_pin, GPIO.LOW)
  GPIO.output(green_led_pin, GPIO.LOW)
  GPIO.output(red_led_pin, GPIO.HIGH)
  writeDoorStatusJSON({'doorStatus': 'open'})
###########################################
# Close Door Function
###########################################
def closeDoor():
  print("Door closed now")
  GPIO.output(relay_pin, GPIO.HIGH)
  GPIO.output(green_led_pin, GPIO.HIGH)
  GPIO.output(red_led_pin, GPIO.LOW)
  writeDoorStatusJSON({'doorStatus': 'closed'})
###########################################
# OpenX Function
###########################################
def openx(s):
  timeout = time.time() + 10   # 5 sec from now
  while True:
    if s=="open":
      openDoor()
    elif s=="close":
      closeDoor()
    print(round(time.time()-timeout),"Door: ",s)
    if time.time() > timeout:
      print("break")
      #closeDoor()
      break
###########################################
# Main Function
###########################################
print("START")
while True:
  try:
    doornow=ReadDoorStatusJSON()
    ################
    try:
      r=requests.get(urlx,params = {"request": "1","doornow": doornow, "side": side},timeout=10)
      h=r.text.strip()
    except:
      h='none'
      pass
    #################
    if h=="open" or h=="close":
      openx(h)
    elif h!="none":
      print("no recognized")
    ##########################################
    ##########################################
    #####################################################
    CC = current_time()
    acx=0
    data=get_data_json()
    if data!='':
      ########
      ST=give_me("Fajr","Athan","-30",data)
      EN=give_me("Sunrise","Iqamah","30",data)
      if ST<=CC<=EN:
        acx=1
      ########
      ST=give_me("Dhuhar","Athan","-30",data)
      EN=give_me("Dhuhar","Iqamah","30",data)
      if ST<=CC<=EN:
        acx=1
      #########
      ST=give_me("Asr","Athan","-30",data)
      EN=give_me("Asr","Iqamah","30",data)
      if ST<=CC<=EN:
        acx=1
      ##########
      ST=give_me("Maghrib","Athan","-30",data)
      EN=give_me("Maghrib","Iqamah","30",data)
      if ST<=CC<=EN:
        acx=1
      ##########
      ST=give_me("Maghrib","Iqamah","30",data)
      EN=give_me("Isha","Iqamah","30",data)
      if ST<=CC<=EN:
        acx=1
      #print(ST,CC,EN)
      #######
    #ST=add_to_time('02:30:00',0)
    #EN=add_to_time('05:30:00',0)
    #if ST<=CC<=EN:
    #  acx=1
    #print(ST,CC,EN)
    ##############
    if today_is()=="Friday":
      ST=add_to_time('12:30:00',0)
      EN=add_to_time('14:30:00',0)
      if ST<=CC<=EN:
        acx=1
      #print(ST,CC,EN)
    ##############
    if today_is()=="Friday":
      ST=add_to_time('15:00:00',0)
      EN=add_to_time('17:30:00',0)
      if ST<=CC<=EN:
        acx=1
      #print(ST,CC,EN)
    ##############
    if today_is()=="Sunday":
      ST=add_to_time('09:30:00',0)
      EN=add_to_time('14:30:00',0)
      if ST<=CC<=EN:
        acx=1
      #print(ST,CC,EN)
    ##############
    if acx==1:
      openDoor()
    else:
      closeDoor()
    #######################################################
    ##########################################
    ##########################################
    time.sleep(2)
  except Exception as eee:
    pass####print("error")
