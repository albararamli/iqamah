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

echo "0" > "$DATA_PATH"screen_status.txt
if [ "$(sed '3q;d' "$CONFIG_FILE")" != 'mic' ]; then
vcgencmd display_power 0
sudo echo 1 > /sys/class/backlight/rpi_backlight/bl_power # LCD 7'' turn off with 1 tag
fi


#vcgencmd display_power 0

###### Old Way ######
#tvservice --off > /dev/null
