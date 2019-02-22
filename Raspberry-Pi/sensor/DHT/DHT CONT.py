import Adafruit_DHT

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.

pin = 4
sensor = Adafruit_DHT.DHT22

while 1:

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	if humidity is not None and temperature is not None:
		print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
		if humidity >34:
			print("Alert ")
	else:
		print('Failed to get reading. Try again!')
		
