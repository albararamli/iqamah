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

if [ "$(sed '3q;d' "$CONFIG_FILE")" != 'mic' ]; then
curl -L -o "$LOCAL_PATH" "$(sed '4q;d' "$CONFIG_FILE")local.php?city=$(sed '1q;d' "$CONFIG_FILE")&icdx=1&note_show=0&remain_show=0&time_show=0&refresh_stop=1&arrow_show=0&date_show=0&current_show=0"
fi
