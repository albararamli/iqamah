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

echo "0" > "$DATA_PATH"chrome_status.txt
# Close Chromium Browser Instance, if the device is not mic
if [ "$(sed '3q;d' "$CONFIG_FILE")" != 'mic' ]; then
  pkill chromium
fi
