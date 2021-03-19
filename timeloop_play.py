import time
import logging
from timeloop import Timeloop
from datetime import timedelta

logging.getLogger("timeloop").setLevel(logging.CRITICAL)

tl = Timeloop()

@tl.job(interval=timedelta(seconds=3))
def sample_job_every_3s():
    print("3s job current time : {}".format(time.ctime()))

# @tl.job(interval=timedelta(seconds=5))
# def sample_job_every_5s():
#     print("5s job current time : {}".format(time.ctime()))


# @tl.job(interval=timedelta(seconds=10))
# def sample_job_every_10s():
#     print("10s job current time : {}".format(time.ctime()))

tl.start(block=True)