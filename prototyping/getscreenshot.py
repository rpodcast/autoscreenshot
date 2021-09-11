"""Take a screenshot"""
# Standard library imports
import os
import platform
import pwd
import sys
import time
import logging
from datetime import timedelta, datetime

# autoscreenshot imports
from mss import mss
import mss.tools
from PIL import Image, ImageOps

# utility functions
def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

def res_gt_1080p(monitor_dict):
    width = monitor_dict['width']
    height = monitor_dict['height']
    #print(f"width is {width}")
    #print(f"height is {height}")
    return width > 1920 or height > 1080


def getscreenshot(image_type, image_dir=None, monitor_id = 1, quality=20):

    user_id = get_username()
    host = platform.node()
    op_system = platform.system()
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")

    if image_type == "jpg":
        image_ext = ".jpg"
    elif image_type == "png":
        image_ext = ".png"
    else:
        print(f"Error: file type {image_type} is not supported")
        sys.exit()
    
    output_filename = user_id + "_" + host + "_" + "monitor" + monitor_id + "_" + dt_string + image_ext

    with mss.mss() as mss_instance:
        monitor_1 = mss_instance.monitors[monitor_id]
        screenshot1 = mss_instance.grab(monitor_1)
        img1 = Image.frombytes("RGB", screenshot1.size, screenshot1.bgra, "raw", "BGRX")  # Convert to PIL.Image

        if res_gt_1080p(monitor_1):
            #print("resizing screenshot to 1080p")
            img1 = img1.resize((1920, 1080))

        if image_dir is None:
            image_dir=os.getcwd()

        final_path = os.path.join(image_dir, output_filename)
        
        img1.save(final_path, quality = quality)
    
    return final_path



    

