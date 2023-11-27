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
###
IFACE_E="eth0"
read MAC_E </sys/class/net/$IFACE_E/address
IFACE_W="wlan0"
read MAC_W </sys/class/net/$IFACE_W/address
MACX=${IFACE_E}${MAC_E}${IFACE_W}${MAC_W}
#MACX2="${MACX//:}"
MACX2=$(echo $MACX | sed 's/[:"]//g')
#echo ${MACX2}

LOCAL_FILE_sbr="$DATA_PATH"sbr2.sbr

LOCAL_FILE="$DATA_PATH"output.html
if [ "$(echo ${MACX2}"PASSED" | base64)" != "$(sed '1q;d' "$LOCAL_FILE_sbr")" ]; then
LOCAL_FILE="$DATA_PATH"block.html
fi
###

echo "1" > "$DATA_PATH"chrome_status.txt
# Open Chromium Browser Instance, if the device is not mic
if [ "$(sed '3q;d' "$CONFIG_FILE")" = 'monitor' ]; then
  chromium-browser --kiosk --disable-gpu --incognito --no-sandbox --noerrdialogs -disable-session-crashed-bubble --disable-infobars --test-type "$LOCAL_FILE" #(for 3.5 screen to run as root)--user-data-dir=/home/pi
fi

