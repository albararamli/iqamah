#!/usr/bin/python
import os
import sys
import time as timeSleep

# cd to Script Directory
scriptDirectory = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(scriptDirectory)

while True:
    try:
        # Download New Iqamah Time
        os.system(scriptDirectory+'/../sh/iqamahTimeParser.sh')
        # Download New Local HTML Page
        os.system(scriptDirectory+'/../sh/local.sh')
    except:
        pass

    # Sleep for 6 hours before rerunning the loop
    timeSleep.sleep(21600)
