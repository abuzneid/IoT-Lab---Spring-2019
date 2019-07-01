import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

GPIO.output(3,GPIO.LOW)
print("off")
time.sleep(1)

GPIO.output(3,GPIO.HIGH)
print("on ")
time.sleep(1)

GPIO.output(3,GPIO.LOW)
print("off")
time.sleep(1)

GPIO.output(3,GPIO.HIGH)
print("on ")
time.sleep(1)

GPIO.cleanup()

