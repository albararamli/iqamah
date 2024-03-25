
#!/bin/bash

MY_PATH="`dirname \"$0\"`"              # relative
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"  # absolutized and normalized
if [ -z "$MY_PATH" ] ; then
  # error; for some reason, the path is not accessible
  # to the script (e.g. permissions re-evaled after suid)
  exit 1  # fail
fi
#echo "$MY_PATH"
CONFIG_FILE="$MY_PATH/../"config.txt
DATA_PATH="$MY_PATH/../data/"
PY_PATH="$MY_PATH/../py/"
SH_PATH="$MY_PATH/"

cd $SH_PATH
chmod +x *.sh
cd $PY_PATH
chmod +x *.py

#write out current crontab
##crontab -l > mycron
#echo new cron into cron file
##echo "00 09 * * * echo hello" >> mycron
#install new cron file
##crontab mycron
##rm mycron

AUTO_FILE=/etc/xdg/lxsession/LXDE-pi/autostart # official Raspbian Buster with desktop and recommended software

if [ -z "$1" ] 
then
ooo="new"
#echo "new"
else
if [ $1 = "old" ] 
then
#echo "old"
ooo="old"
AUTO_FILE=/home/pi/.config/lxsession/LXDE-pi/autostart # the old RPI
else 
#echo "keep the new"
ooo="keep the new"
fi
fi

##AUTO_FILE=/etc/xdg/lxsession/LXDE-pi/autostart # official Raspbian Buster with desktop and recommended software
##AUTO_FILE=/home/pi/.config/lxsession/LXDE-pi/autostart # the old RPI // remove sudo from the command
echo "@lxpanel --profile LXDE-pi" > $AUTO_FILE
echo "@pcmanfm --desktop --profile LXDE-pi" >> $AUTO_FILE
echo "@xscreensaver -no-splash" >> $AUTO_FILE
echo "@point-rpi" >> $AUTO_FILE
echo "@xrandr --output HDMI-1 --auto --rotate right" >> $AUTO_FILE
echo "@xrandr --output HDMI-2 --auto --rotate right" >> $AUTO_FILE
echo "xhost +" >> $AUTO_FILE
echo "sudo sh "$SH_PATH"MouseMove.sh" >> $AUTO_FILE
echo "sudo sh "$SH_PATH"screen_on.sh" >> $AUTO_FILE
echo "sudo sh "$SH_PATH"local.sh" >> $AUTO_FILE
#echo "sudo sh "$SH_PATH"iqamahTimeParser.sh" >> $AUTO_FILE
#echo "sudo python "$PY_PATH"screenTimeCheck.py" >> $AUTO_FILE
echo "sudo python "$PY_PATH"mic_ini.py" >> $AUTO_FILE
echo "sudo python "$PY_PATH"mic_listen_online.py" >> $AUTO_FILE
echo "sudo python "$PY_PATH"internet.py" >> $AUTO_FILE # in my 7 inch last time works only when there is no sudo here
#echo "sudo python "$PY_PATH"sensor.py" >> $AUTO_FILE
echo "sudo python "$PY_PATH"tf-mini_plus-new.py" >> $AUTO_FILE
echo "python "$PY_PATH"switch.py" >> $AUTO_FILE
echo "python "$PY_PATH"light.py" >> $AUTO_FILE
echo "sudo sh "$SH_PATH"Chromium_Open.sh" >> $AUTO_FILE  # in the 3.5 and 7 screen remove "sudo" cuz chrome requires that
echo "python "$PY_PATH"door.py" >> $AUTO_FILE
