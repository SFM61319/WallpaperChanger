import datetime
import time

import ctypes

import getpass


val = 510
num = 169.4

currtime = datetime.datetime.now()  # Get the current time

# Separate the *currtime* into different units of time
CH = int(currtime.strftime("%H"))
CM = int(currtime.strftime("%M"))
CS = int(currtime.strftime("%S"))
CMonth = int(currtime.strftime("%m"))

startH = 2 if CMonth <=3 or CMonth >= 9 else 3
calH = CH - startH

if CH < startH:
    calH += 24

upSec = calH * 3600 + CM * 60 + CS
startSec = int(upSec//num)

print(startSec) # print debugging

n = startSec % val
username = getpass.getuser()
num = int(num)

while n <= val:
    path = f'C:\\Users\\{username}\\Desktop\\WallpaperChanger\\wp{n}.png'
    
    y = datetime.datetime.now()
    
    print(path, y)  # print debugging
    
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    
    time.sleep(num)
    
    n += 1
    
    if n == val + 1:
        n = 1
