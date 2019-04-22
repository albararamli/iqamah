
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


#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "####Script Star####" > mycron
echo "#Update parsedIqamah.csv File Once Every Day 15 min after Midnight" >> mycron
echo "00 03 * * * "$SH_PATH"iqamahTimeParser.sh" >> mycron
echo "#Run screenTimeCheck.py Script Every 5 min" >> mycron
echo "*/5 * * * * sudo python "$PY_PATH"screenTimeCheck.py" >> mycron
echo "#Restart RPi Everyday at 2:15AM" >> mycron
echo "15 02 * * * reboot" >> mycron
echo "#Download Local HTML" >> mycron
echo "15 03 * * * "$SH_PATH"local.sh" >> mycron
echo "#Move Mouse Location" >> mycron
echo "#00 * * * * "$SH_PATH"MouseMove.sh" >> mycron
#install new cron file
crontab mycron
rm mycron

AUTO_FILE=~/.config/lxsession/LXDE-pi/autostart
echo "@lxpanel --profile LXDE-pi" > $AUTO_FILE
echo "@pcmanfm --desktop --profile LXDE-pi" >> $AUTO_FILE
echo "@xscreensaver -no-splash" >> $AUTO_FILE
echo "@point-rpi" >> $AUTO_FILE
echo "sudo sh "$SH_PATH"MouseMove.sh" >> $AUTO_FILE
echo "sudo sh "$SH_PATH"screen_on.sh" >> $AUTO_FILE
echo "sudo sh "$SH_PATH"Chromium_Open.sh" >> $AUTO_FILE  # in the 3.5 screen remove "sudo" cuz chrome requires that
echo "sudo sh "$SH_PATH"iqamahTimeParser.sh" >> $AUTO_FILE
echo "sudo python "$PY_PATH"screenTimeCheck.py" >> $AUTO_FILE
echo "sudo python "$PY_PATH"mic_ini.py" >> $AUTO_FILE
echo "sudo python "$PY_PATH"mic_listen_online.py" >> $AUTO_FILE
echo "sudo python "$PY_PATH"internet.py" >> $AUTO_FILE
echo "sudo python "$PY_PATH"sensor.py" >> $AUTO_FILE

