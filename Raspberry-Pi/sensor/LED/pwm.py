import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) # BCM
GPIO.setup(19,GPIO.OUT)

p=GPIO.PWM(19,50) # freq 100 hz
p.start(0)
while 1:
	for x in range(50):
		p.ChangeDutyCycle(x)
		time.sleep(0.1)
		print(x)
	for x in range(50):
		p.	ChangeDutyCycle(50-x)
		time.sleep(0.1)
		print(x)
