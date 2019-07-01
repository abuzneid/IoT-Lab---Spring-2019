import Adafruit_DHT

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.

pin = 4
sensor = Adafruit_DHT.DHT22

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    with open("data.txt", 'w') as file:
        file.write("Temperature {}, Humidity {}".format(temperature,humidity))
else:
    print('Failed to get reading. Try again!')
