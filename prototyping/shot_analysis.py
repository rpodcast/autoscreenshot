import os
import mss
import mss.tools
import numpy as np
from PIL import Image, ImageOps, ImageDraw
from datetime import datetime
from tesserocr import PyTessBaseAPI, RIL
import cv2
import pytesseract

#import tesserocr

# see here for example analysis https://github.com/ymauray/hotshotpy/blob/main/src/hotshotpy/observer.py
# example analysis race in progress
image_path = "game_screenshots/race_lap1_inprogress.png"
image_file = Image.open(image_path)

#print(image_file.size)

image_file = image_file.resize((1920, 1080))
#image_file2.show()

# obtain time remaining before DNF

im = image_file.crop((870, 20, 1100, 300))

im = ImageOps.invert(im)
im = im.convert('LA')
im = im.convert('RGBA')
#im.show()
print(im.mode)

data = np.array(im)

#print(data)

red, blue, green, alpha = data.T

source_color = (red >= 46)
data[..., :-1][source_color.T] = (255, 255, 255)
im2 = Image.fromarray(data)

im2.show()
with PyTessBaseAPI() as api:
    api.SetImage(im2)
    text = api.GetUTF8Text()
    print(text)