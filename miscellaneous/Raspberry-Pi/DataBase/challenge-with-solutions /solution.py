import Adafruit_DHT
import sqlite3
import threading
import datetime



def get_time():
    my=datetime.datetime.now()
    data_time = '{}:{}:{}'.format(my.hour,my.minute,my.second)
    data_date='{}/{}/{}'.format(my.day,my.month,my.year)
    return  data_date,data_time


def my_database(x, y,my_time, my_date):

    """

    :return: Nothing
    """

    # define the connection
    conn = sqlite3.connect("xyz.db")

    #define the cursor
    cursor = conn.cursor()

    # create Tables
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     temperature  TEXT, 
     humidity TEXT,
     m_date TEXT,
     m_time TEXT)""")

    # Add data to database
    cursor.execute("""
    INSERT INTO my_table (temperature,humidity,m_date,m_time) VALUES (?, ?, ?, ?)""",(x, y,my_time, my_date))

    # perform 3C
    #COMMIT, CLOSE CLOSE

    conn.commit()
    cursor.close()
    conn.close()


def main():
    threading.Timer(10, main).start()

    pin = 4
    sensor = Adafruit_DHT.DHT22

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:

        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

        data_date,data_time = get_time()
        print('Date',data_date)



        my_database(temperature, humidity,data_time,data_date)


        print("data was written on database T{} H{}".format(temperature,humidity))

    else:
        print('Failed to get reading. Try again!')


if __name__ == '__main__':
    while 1:
        main()


