import ctypes
import os
import random, urllib.request, json
global drive, folder, image

drive = "C:\\"
folder = "images"
image = "test.jpg"
f = open("url.txt")
urls = []
# "https://www.reddit.com/r/MinimalWallpaper/.json"
subreddit = "http://pastebin.com/raw/DLNYEhNw"


def setImage(image):
    image_path = os.path.join(drive, folder, image)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(
        SPI_SETDESKWALLPAPER, 0, image_path,)


def validate(url):
    pass


url = urllib.request.urlopen(subreddit)
content = url.read()
data = json.loads(content.decode("utf-8"))
for i in data["data"]["children"]:
    urls.append(i["data"]["url"] + "\n")

for item in urls:
    validate(item)
