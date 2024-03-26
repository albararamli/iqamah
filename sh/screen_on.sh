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

echo "1" > "$DATA_PATH"screen_status.txt
#if [ "$(sed '3q;d' "$CONFIG_FILE")" != 'mic' ]; then
vcgencmd display_power 1
sudo echo 0 > /sys/class/backlight/rpi_backlight/bl_power # LCD 7'' turn on with 0 tag


xrandr --output HDMI-1 --auto --rotate right
xrandr --output HDMI-1 --mode 1920x1080

xrandr --output HDMI-2 --auto --rotate right
xrandr --output HDMI-2 --mode 1920x1080

if [ "$(sed '5q;d' "$CONFIG_FILE")" = '0' ]; then
xinput set-prop 'raspberrypi-ts' 'Coordinate Transformation Matrix' -1 0 1 0 -1 1 0 0 1
fi

###### Old Way ######
#tvservice --preferred > /dev/null
#fbset -depth 8; fbset -depth 16; xrefresh
