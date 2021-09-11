import os
import platform
import pwd
import mss
import mss.tools
import cv2
from PIL import Image, ImageOps
from datetime import datetime
import time
import numpy

# utility functions
def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

def screen_record_efficient():
    # 800x600 windowed mode
    #mon = {"top": 40, "left": 0, "width": 800, "height": 640}

    title = "[MSS] FPS benchmark"
    fps = 0
    sct = mss.mss()
    last_time = time.time()

    mon = sct.monitors[1]  # Identify the display to capture

    while(True):
        try:
            img = numpy.asarray(sct.grab(mon))
            img = cv2.resize(img,(1920,1080))
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            #fps += 1
            out.write(img)
            StopIteration(1)
        except KeyboardInterrupt:
            break
    
    out.release()
    cv2.destroyAllWindows()

def video_record(my_id, my_host):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
    output_filename = "videos/" + my_id + "_" + my_host + "_" + dt_string + ".png"
    
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = sct.monitors[1]

        while "Screen capturing":
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            #img = numpy.array(sct.grab(monitor))
            img = sct.grab(monitor)

            #img.save(output_filename)
            mss.tools.to_png(img, size = (1920, 1080), output = output_filename)

            # Display the picture
            cv2.imshow("OpenCV/Numpy normal", img)

            # Display the picture in grayscale
            # cv2.imshow('OpenCV/Numpy grayscale',
            #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

            #print("fps: {}".format(1 / (time.time() - last_time)))

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

# obtain metadata on host
my_id = get_username()
my_host = platform.node()
# now = datetime.now()
# dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")

# # generate output file name
# output_filename = "videos/" + my_id + "_" + my_host + "_" + dt_string + ".mp4"
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# frame_width = 1920
# frame_height = 1080
# frame_rate = 1.0
# out = cv2.VideoWriter(output_filename, fourcc, frame_rate, (frame_width, frame_height))






#print("MSS:", screen_record_efficient())
video_record(my_id, my_host)