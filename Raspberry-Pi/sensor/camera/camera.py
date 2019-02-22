import time
from picamera import PiCamera

camera=PiCamera()
#camera.start_preview()
time.sleep(2)
camera.capture("yo.jpg")
