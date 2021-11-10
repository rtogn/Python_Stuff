"""
You needs to get up and stretch every 20 minutes.
This script displays a console dialog with a 20min countdown
and will open a file at the end. I have it set to an mp3 here,
replace with anything or type in a path to the file. 

"""

import os, time, sys

clock =1200 #sets var for time of 20 min

os.system('mode con: cols=33 lines=2')
print("Press Ctrl+C to reset counter!")

while True: 
    clock = clock - 1  
    m , s = divmod (clock, 60)   #divmod takes a remainder of x / 60 resulting in a 60 sec minute (m) where (s) is seconds remaining
    
   
    try: 
        sys.stdout.write("\r")  #move to front of line every tick
        print("Time until stretch: %02d:%02d" % (m ,s), end='', flush =True) #print time references m & s from above
        
        time.sleep(1)  
        sys.stdout.flush() #clear line for new print?

    except KeyboardInterrupt:
        clock = 1200  #keyboard int resets clock to 20 min
        pass

    if clock == 0:  #play sound @ 0 sec & reset
    
        os.system ("alarm.mp3") 
        clock = 1200
        time.sleep(60)
        pass

    x = "cat"
    x.upper()
    

