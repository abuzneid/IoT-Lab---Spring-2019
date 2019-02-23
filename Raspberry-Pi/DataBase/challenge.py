import Adafruit_DHT
import sqlite3
import threading


def my_database(x, y):

    """

    :return: Nothing
    """

    # define the connection
    conn = sqlite3.connect("sensor.db")

    #define the cursor
    cursor = conn.cursor()

    # create Tables
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     temperature  TEXT, 
     humidity TEXT)""")

    # Add data to database
    cursor.execute("""
    INSERT INTO my_table (temperature,humidity) VALUES (?, ?)""",(x, y))

    # perform 3C
    #COMMIT, CLOSE CLOSE

    conn.commit()
    cursor.close()
    conn.close()


def main():
    threading.timer(10,main).start()

    pin = 4
    sensor = Adafruit_DHT.DHT22

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:

        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        my_database(temperature, humidity)
        print("data was written on database T{} H{}".format(temperature,humidity))

    else:
        print('Failed to get reading. Try again!')


if __name__ == '__mmain__':
    while 1:
        main()


