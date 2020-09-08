"""A dynamic wallpaper changing program to replicate macOS' dynamic wallpapers on Windows
"""


__author__ = 'Amlan Saha Kundu'
__github__ = 'https://github.com/yoursamlan/WallpaperChanger.git'
__version__ = '2.1.1'
__contributors__ = {
    'SFM61319': 'https://github.com/SFM61319'
}


import ctypes

import time
import random

import getpass

print('', '='*32, '\n', 'Welcome to WALLPAPER CHANGER', __version__[:-2], '\n', 'by Amlan'.rjust(20), '\n', '='*32, '\n')
print("Enter 'r' for random choice OR any other key for systematic change")

username = getpass.getuser()

uinp = input('Enter your choice: ')
val = int(eval(input('Enter no. of wallpapers: ')))
num = int(eval(input('Enter time interval (sec): ')))

if uinp.casefold() == 'r':
    while True:
        path = f'C:\\Users\\{username}\\Desktop\\WallpaperChanger\\wp{random.randint(1, val)}.png'  # 'wp' => 'WallpaperChanger'
        
        print(path) # print debugging
        
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
        
        time.sleep(num)

else:
    n = 1
    
    while n <= val:
        path = f'C:\\Users\\{username}\\Desktop\\WallpaperChanger\\wp{n}.png'
        
        print(path) # print debugging
        
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
        
        time.sleep(num)
        
        n += 1
        
        if n == val + 1:
            n = 1
