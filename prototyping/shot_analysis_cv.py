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

img = cv2.imread(image_path)
img = cv2.resize(img,(1920,1080))

#im = image_file.crop((870, 20, 1100, 300))

crop = img[20:300, 870:1100]

crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

img = cv2.threshold(crop, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

cv2.imshow('img', crop)
cv2.waitKey(2500)

# Destroying present windows on screen

cv2.destroyAllWindows()

