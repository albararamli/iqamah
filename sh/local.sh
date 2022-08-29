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
LOCAL_PATH="$DATA_PATH"local.html
LOCAL_PATH_BLOCK="$DATA_PATH"block.html
#LOCAL_IMG="$DATA_PATH"internet.png
#LOCAL_IMG2="$DATA_PATH"all.png
###
IFACE_E="eth0"
read MAC_E </sys/class/net/$IFACE_E/address
IFACE_W="wlan0"
read MAC_W </sys/class/net/$IFACE_W/address
MACX=${IFACE_E}${MAC_E}${IFACE_W}${MAC_W}
#MACX2="${MACX//:}"
MACX2=$(echo $MACX | sed 's/[:"]//g')
#echo ${MACX2}
### 
if [ "$(sed '3q;d' "$CONFIG_FILE")" != 'mic' ]; then
curl -kLo "$LOCAL_PATH" "$(sed '4q;d' "$CONFIG_FILE")local.php?size=$(sed '5q;d' "$CONFIG_FILE")&city=$(sed '1q;d' "$CONFIG_FILE")&icdx=1&note_show=0&remain_show=0&time_show=0&refresh_stop=1&arrow_show=0&date_show=0&current_show=0&mac=${MACX2}"
curl -kLo "$LOCAL_PATH_BLOCK" "$(sed '4q;d' "$CONFIG_FILE")local.php?size=$(sed '5q;d' "$CONFIG_FILE")&city=$(sed '1q;d' "$CONFIG_FILE")&icdx=1&note_show=0&remain_show=0&time_show=0&refresh_stop=1&arrow_show=0&date_show=0&current_show=0&mac=111"
#curl -kLo "$LOCAL_IMG" "$(sed '4q;d' "$CONFIG_FILE")internet.png"
#curl -kLo "$LOCAL_IMG2" "$(sed '4q;d' "$CONFIG_FILE")all.png"
###############
###############
for VARIABLE in 0 1 2 3 4 5 6 7 8 9 10    
do
#Liunx
LOCAL_PATH_EXPORT_YEAR=$(date --date=$VARIABLE" year" +%Y)
#MACOS
#LOCAL_PATH_EXPORT_YEAR=$(date -v+"$VARIABLE""y" +%Y)
LOCAL_PATH_EXPORT="$DATA_PATH""$LOCAL_PATH_EXPORT_YEAR".json
curl -kLo "$LOCAL_PATH_EXPORT" "$(sed '4q;d' "$CONFIG_FILE")export.php?city=$(sed '1q;d' "$CONFIG_FILE")&year=$LOCAL_PATH_EXPORT_YEAR&typex=json"
done
###############
###############
fi
