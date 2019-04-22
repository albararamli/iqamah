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
TMP1_PATH="$DATA_PATH"tmp.txt
TMP2_PATH="$DATA_PATH"tmp2.txt
CSV_PATH="$DATA_PATH"parsedIqamah.csv

#This sh runs every day once to parse Athan and Iqamah times from server, work only in monitor
if [ "$(sed '3q;d' "$CONFIG_FILE")" != 'mic' ]; then
#Download Iqamah Times for Davis from Server
wget -q "$(sed '4q;d' "$CONFIG_FILE")api.php?city=$(sed '1q;d' "$CONFIG_FILE")&id=0" -O "$TMP1_PATH"

#Extract Salat Name and Time from Text File
awk -F'<BR>' '{for (i=1;i<=NF;i++) print $i}' "$TMP1_PATH" > "$TMP2_PATH"

#Check Number of Ljnes in Temp File
lineCheck=$(wc -l < "$TMP2_PATH")

if [ $lineCheck = "19" ]
    then
	#Remove ':' Symbol from the Extracted Time (for comparison purpose)
	sed 's/://' "$TMP2_PATH" > "$CSV_PATH"
fi

#Delete all Temp. Files
rm "$TMP1_PATH"
rm "$TMP2_PATH"

#################### Other Functions/Ways that Didn't work ####################
#Another way to remove : from the times
# gawk -F':' '{for (i=1;i<=NF;i++) print $i}' tmp2.txt > tmp3.csv
#
#Convert Strings to Integers
# sed -E 's/\:([0-9])([0-9])\..*"/\:\1\2"/g' tmp3.csv > tmp4.csv
#
# Another way to read each column form the csv file
# while IFS=, read -r col1; do echo $col1  ; done < tmp.csv
#
# Declaring an array variable
# declare -a var
#
# Another way to read the contents of the csv file
# for=$(while IFS=, read -r col1; do echo $col1  ; done < tmp.csv)
#
# Another way to read the contents of the csv file
# declare -a var=$(gawk -F':' '{for (i=1;i<=NF;i++) print $i, var[$i]=$i}' tmp2.txt)
#
# Another way to read the contents of the csv file
# gawk -F':' '{for (i=1;i<=NF;i++) print $i, var[$i]=$i}' tmp3.csv
#
# Another way to read the contents of the csv file
# declare -a nvar
# for (( i = 0; i < NF; i++ )); do
#   nvar[i]=sed -n "$i"p tmp3.csv
# done

fi
