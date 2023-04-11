#!/usr/bin/env python3
import os
import string

def valueOfKey(str, handle):
    while line := handle.readline():
        if str in line:
            res = line.split('\t').pop().split('/')[0].rstrip()
            return res
    return ""

directories = []
with os.scandir('/proc') as entries:
    for entry in entries:
        if(entry.name.isdigit()):
            directories.append(entry.path)


valid_pids = []
for process in directories:
    with open(process + "/" + "status", 'r') as status, open(process + "/" + "cmdline", 'r') as cmdline:
        cmdlineName = cmdline.read() #if name from status file is found in cmdlineName then it's ok
        statusName = valueOfKey("Name", status)
        ppid = valueOfKey("PPid", status)
        
        if cmdlineName:
            if statusName not in cmdlineName:
                print("\nhmm... suspicious --> For process: "+process+": status file: '"+statusName+"' but the cmdline file shows: "+cmdlineName)

        # if not int(ppid):
        #         #if the process has ppid 0 leave it alone
        #     valid_pids.append(process.split('/').pop())
        #     continue
        # elif statusName in cmdlineName:
        #    # if __debug__:
        #      #   print(statusName + " - " + cmdlineName)
        #     valid_pids.append(process.split('/').pop())
        #     continue
        # #elif ppid in valid_pids:
        #   #  valid_pids.append(process.split('/').pop())
        #    # continue
        # else :
        #     print("hmm... suspicious "+statusName +" "+ppid+ " "+ process)
        

