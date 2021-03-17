import os
import platform
import pwd
import mss
import mss.tools
from PIL import Image, ImageOps
from datetime import datetime

# utility functions
def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

# obtain metadata on host
my_id = get_username()
my_host = platform.node()
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")

# define image quality param
img_quality = 50

# generate output file name
output_filename_full_png = "screenshots/" + my_id + "_" + my_host + "_" + dt_string + "_full.png"
output_filename_smaller_png = "screenshots/" + my_id + "_" + my_host + "_" + dt_string + "_smaller.png"

output_filename_jpg = "screenshots/" + my_id + "_" + my_host + "_" + dt_string + "_smaller.jpg"
#print(output_filename)

with mss.mss() as mss_instance:  # Create a new mss.mss instance
    #print(mss_instance.monitors)
    #print(len(mss_instance.monitors))
    #print(mss_instance.monitors[0])
    #print(mss_instance.monitors[1])
    #print(mss_instance.monitors[2])
    monitor_1 = mss_instance.monitors[1]  # Identify the display to capture
    monitor_2 = mss_instance.monitors[2]

    # create file
    #mss_instance.shot(output=output_filename_png)

    screenshot1 = mss_instance.grab(monitor_1)  # Take the screenshot
    #print(screenshot1.size)
    screenshot2 = mss_instance.grab(monitor_2)  # Take the screenshot
    img1 = Image.frombytes("RGB", screenshot1.size, screenshot1.bgra, "raw", "BGRX")  # Convert to PIL.Image
    img1 = Image.frombytes("RGB", screenshot1.size, screenshot1.bgra, "raw", "BGRX")  # Convert to PIL.Image
    img2 = Image.frombytes("RGB", screenshot2.size, screenshot2.bgra, "raw", "BGRX")  # Convert to PIL.Image

    img11 = img1.resize((1920, 1080))

    img1.save(output_filename_full_png)
    img11.save(output_filename_smaller_png)
    img11.save(output_filename_jpg, quality = img_quality)

    #img2.show()  # Show the image using the default image viewer

#print("Hello world")