import argparse
import time
import logging
from timeloop import Timeloop
from datetime import timedelta, datetime
from PIL import Image, ImageOps
import os
import sys
import platform
import pwd
from mss import mss
import mss.tools

# utility functions
def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

def py_minor():
    return sys.version_info[1]


def platform_is_osx():
    return sys.platform == "darwin"


def platform_is_win():
    return sys.platform == "win32"


def platform_is_linux():
    return sys.platform.startswith("linux")

def use_x_display():
    if platform_is_win():
        return False
    if platform_is_osx():
        return False
    DISPLAY = os.environ.get("DISPLAY")
    XDG_SESSION_TYPE = os.environ.get("XDG_SESSION_TYPE")
    # Xwayland can not be used for screenshot
    return DISPLAY and XDG_SESSION_TYPE != "wayland"

def using_multiple_displays():
    with mss.mss() as mss_instance:
        print(mss_instance.monitors)
        return len(mss_instance.monitors) > 1

# check if running under linux
if platform_is_linux():
    print("running under linux")

    # if in a tty session (i.e. not in an actual graphical desktop), exit script
    if os.environ.get("XDG_SESSION_TYPE") == "tty":
        print("screenshots cannot be taken in a terminal (tty) session!  Please run inside a graphical session")
        sys.exit()
    else:
        if use_x_display():
            print("Running under X11: Proceeding as normal")
        else:
            print("Running under Wayland needs more work")
            sys.exit()

#parser = argparse.ArgumentParser()
#parser.add_argument('imagedir', help='directory to store image files')

logging.getLogger("timeloop").setLevel(logging.CRITICAL)
# obtain metadata on host
user_id = get_username()
host = platform.node()
op_system = platform.system()


print(using_multiple_displays())


# define image quality param
img_quality = 20

tl = Timeloop()

with mss.mss() as mss_instance:
    @tl.job(interval=timedelta(seconds=3))
    def sample_job_every_3s():
        print("Begin compressed picture saving : {}".format(time.ctime()))
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
        output_filename_smaller_png = "screenshots/" + user_id + "_" + host + "_" + dt_string + "_smaller.png"
        output_filename_jpg = "screenshots/" + user_id + "_" + host + "_" + dt_string + "_smaller.jpg"
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
        output_filename_smaller_png = "screenshots/" + user_id + "_" + host + "_" + dt_string + "_smaller.png"
        monitor_1 = mss_instance.monitors[1]
        screenshot1 = mss_instance.grab(monitor_1)
        img1 = Image.frombytes("RGB", screenshot1.size, screenshot1.bgra, "raw", "BGRX")  # Convert to PIL.Image
        img11 = img1.resize((1920, 1080))
        img11.save(output_filename_smaller_png)
        print("End png picture saving : {}".format(time.ctime()))

tl.start(block=True)