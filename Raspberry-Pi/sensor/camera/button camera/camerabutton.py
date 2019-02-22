import time
from picamera import PiCamera

from time import sleep # Library will let us put in delays
import RPi.GPIO as GPIO # Import the RPi Library for GPIO pin control

button1_pin=12 # Button 1 is connected to physical pin 12
GPIO.setmode(GPIO.BOARD) # Use Physical Pin Numbering Scheme

GPIO.setup(button1_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
# Make button1_pin an input, Activate Pull UP Resistor

while(1): # Create an infinite Loop
    input1=GPIO.input(button1_pin)
    if input1==0:
        sleep(.1)
        print ('Button 1 Pressed')
        # Look for button 1 press # Delay
        # Notify User
        camera=PiCamera()
        #camera.start_preview()
        time.sleep(2)
        camera.capture("soumil.jpg")
