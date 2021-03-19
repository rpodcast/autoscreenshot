# import required libraries
import os
import platform
import pwd
from vidgear.gears import ScreenGear
from vidgear.gears import WriteGear
import cv2
from datetime import datetime
import time

# obtain metadata on host
#my_id = get_username()
#my_host = platform.node()

# define suitable (Codec,CRF,preset) FFmpeg parameters for writer
#output_params = {"-vcodec": "libx264", "-crf": 0, "-preset": "fast"}
frame_rate = 1
output_params = {"-vcodec": "libx264", "-r": frame_rate, "-preset": "fast"}
#output_params = {"-input_framerate": 1}

# open video stream with default parameters
stream = ScreenGear(monitor=1, logging=True).start()

# Define writer with defined parameters and suitable output filename for e.g. `Output.mp4`
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
out_file = "videos/output_" + dt_string + ".mp4"

writer = WriteGear(output_filename=out_file, logging=True, **output_params)
#writer = WriteGear(output_filename="videos/myimage_%04d.png", logging=True, **output_params)
#starttime = time.time()


# loop over
while True:

    #now = datetime.now()
    #dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")

    #output_filename_full_png = "videos/" + my_id + "_" + my_host + "_" + dt_string + "_full.png"

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    frame = cv2.resize(frame,(1920,1080))

    # {do something with the frame here}
    # write gray frame to writer
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    writer.write(frame)


    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break



# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close writer
writer.close()
