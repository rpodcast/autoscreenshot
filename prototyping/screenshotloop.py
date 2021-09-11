"""Automatically take screenshots"""
# Standard library imports
from datetime import timedelta, datetime

# autoscreenshot imports
from mss import mss
import mss.tools
from timeloop import Timeloop
from autoscreenshot import getscreenshot

def screenshotloop(image_dir=None, monitor_id = 1, highres_interval=30, lowres_interval=3, quality=20):
    tl = Timeloop()

    with mss.mss() as mss_instance:
        @tl.job(interval=timedelta(seconds=lowres_interval))
        def lowres_job():
            getscreenshot(mss_instance, image_type = "jpg", image_dir=image_dir, monitor_id=monitor_id, quality=quality)

        @tl.job(interval=timedelta(seconds=highres_interval))
        def highres_job():
            getscreenshot(mss_instance, image_type = "png", image_dir=image_dir, monitor_id=monitor_id, quality=quality)

    tl.start(block=True)
