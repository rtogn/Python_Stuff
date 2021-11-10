import time
import os

"""
* Script that starts and stops a process depending of time of day
* The process will run when time is outside of the range determined by the
* startShift:endshift. So if start is at 9am and end is at 8pm (uses military time) the process
* will run after 8 and end again when 9 rolls around.
* Simple as: plug this into windows startup folder and set your references for the file
* you want to use (startFilePath) and the name of the exe that runs (exeName) so the OS can close it.
* Please note: Windows will close EVERYTHING with that name. So if you crush py.exe it will also
* drop this script from running... 
"""
def main():

    SECONDS_IN_HOUR = 3600
    curHour = updateTime()
    startShift = 22 #off after 8am
    endShift = 23 #back on at 8pm
    startFilePath = "notepad"
    exeName = "notepad.exe"
    
    while(1):
        processCheck(startShift, endShift, startFilePath, exeName)
        time.sleep(5)

def updateTime():
    return int(time.strftime("%M"))

def processCheck(start, end, startFilePath, exeName):
    #function takes ints pls  
    curHour = updateTime()
    print(start)
    print(end)
    if ((curHour >= start) or (curHour <= end)):
        #start your program, direct FP to location
        os.system(startFilePath)
    else:
        #kills your program based on the specific exe name in the tasklist (type tasklist into CMD to check)
        os.system(f"Taskkill /IM \"{exeName}\" /F")

if __name__ == '__main__':
    main()
