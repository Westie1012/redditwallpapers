import ctypes
import os
import random, urllib.request, json

drive = "C:\\"
folder = "images"
f = open("url.txt")
urls = []
for line in f:
    urls.append(line.strip())
f.close()

image = "test.jpg"
image_path = os.path.join(drive, folder, image)
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
subreddit = "https://www.reddit.com/r/
