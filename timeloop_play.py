import time
import logging
from timeloop import Timeloop
from datetime import timedelta, datetime
from PIL import Image, ImageOps
import os
import platform
import pwd
from mss import mss
import mss.tools

# utility functions
def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]


logging.getLogger("timeloop").setLevel(logging.CRITICAL)
# obtain metadata on host
my_id = get_username()
my_host = platform.node()

# define image quality param
img_quality = 20

tl = Timeloop()

with mss.mss() as mss_instance:
    @tl.job(interval=timedelta(seconds=3))
    def sample_job_every_3s():
        print("Begin compressed picture saving : {}".format(time.ctime()))
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
        output_filename_smaller_png = "screenshots/" + my_id + "_" + my_host + "_" + dt_string + "_smaller.png"
        output_filename_jpg = "screenshots/" + my_id + "_" + my_host + "_" + dt_string + "_smaller.jpg"
        monitor_1 = mss_instance.monitors[1]
        screenshot1 = mss_instance.grab(monitor_1)
        img1 = Image.frombytes("RGB", screenshot1.size, screenshot1.bgra, "raw", "BGRX")  # Convert to PIL.Image
        img11 = img1.resize((1920, 1080))
        #img11.save(output_filename_smaller_png)
        img11.save(output_filename_jpg, quality = img_quality)
        print("End compressed picture saving : {}".format(time.ctime()))

    @tl.job(interval=timedelta(seconds=30))
    def sample_job_every_30s():
        print("Begin png picture saving : {}".format(time.ctime()))
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
        output_filename_smaller_png = "screenshots/" + my_id + "_" + my_host + "_" + dt_string + "_smaller.png"
        monitor_1 = mss_instance.monitors[1]
        screenshot1 = mss_instance.grab(monitor_1)
        img1 = Image.frombytes("RGB", screenshot1.size, screenshot1.bgra, "raw", "BGRX")  # Convert to PIL.Image
        img11 = img1.resize((1920, 1080))
        img11.save(output_filename_smaller_png)
        print("End png picture saving : {}".format(time.ctime()))

tl.start(block=True)