import os
import mss
import mss.tools
from PIL import Image, ImageOps
from datetime import datetime

# see here for example analysis https://github.com/ymauray/hotshotpy/blob/main/src/hotshotpy/observer.py
# example analysis race in progress
image_path = "game_screenshots/race_lap1_inprogress.png"
image_file = Image.open(image_path)

