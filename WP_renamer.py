import os

# Import *getpass* for function *getuser* to get username
import getpass

path = f'C:\\Users\\{getpass.getuser()}\\Desktop\\WallpaperChanger'

if not os.path.exists(path):    # Create the folder *WallpaperChanger* if it doesn't exist
    os.makedirs(path)

files = os.listdir(path)

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(('wp', str(index), '.png'))))
