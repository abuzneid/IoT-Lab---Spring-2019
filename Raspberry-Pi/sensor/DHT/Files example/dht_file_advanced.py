import Adafruit_DHT
import time
import datetime


# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.

pin = 4
sensor = Adafruit_DHT.DHT22



def get_date_time():
    v = datetime.datetime.now()
    my_date='{}/{}/{}'.format(v.month,v.day,v.year)
    my_time = '{}:{}:{}'.format(v.hour,v.minute,v.second)

    return my_date, my_time


def write_data_dht():

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        
        my_date,my_time= get_date_time()
        

        
        with open("sample.txt", 'w') as file:
                   
            data="{},{},{},{}".format(my_date,my_time,temperature,humidity)
            print(data)
            file.write(data)
            file.write("/n")
        file.close()
        
    else:
        print('Failed to get reading. Try again!')
        

        
if __name__ == '__main__':
    for x in range(1,4):
        time.sleep(2)
        write_data_dht()
 

