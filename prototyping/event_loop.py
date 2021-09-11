from threading import Event # Needed for the  wait() method
from time import sleep     
import mss
import mss.tools

#print("\n Live long and prosper!")
#sleep(1)               # Conventional sleep() Method.
#print("\n Just let that soak in..")   
#Event().wait(3.0) # wait() Method, useable sans thread.
#print("\n Make it So! = )\n")

with mss.mss() as sct:
    try:
        while True:
            print("\n Live long and prosper!")
            Event().wait(3.0)
    except KeyboardInterrupt:
        pass

print("\nI am done")
