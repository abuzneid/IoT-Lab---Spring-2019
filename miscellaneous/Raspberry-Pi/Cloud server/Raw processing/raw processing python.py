""""
---------------------------------------------------------------------------------------------------------
Code is developed by Soumil shah
this example will teach you how to process data using python and how to analyze data using live graph
we are using tkinter module from python and using animation  function from it
we are also using the concept of database and urlib module

this is perfect example that shows raw processing power of python

soumil shah
Bachelor in Electronic Engineering
Master i Electrical Engineering
Master in Computer Engineering

soushah@my.bridgeport.edu

---------------------------------------------------------------------------------------------------------
"""


try:                                            # import the library using try block
    import tkinter
    import numpy as np
    import matplotlib.pyplot as plt
    import datetime
    import time
    import pandas as pd
    import matplotlib.animation as animation
    from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2Tk
    from os import system
    import sqlite3
    import requests
    from urllib.request import urlopen
    from urllib import request
    import ssl
    import threading
    import twilio

except:                                         # of that fails print error message

    print("Cannot import the library ")


my_sensor_v = []                                # creating  list to Hold the data
x1 = []                                         # Temperature T
y1 = []                                         # Humidity Value

fig = plt.figure()                              # define the Figure
ax1 = fig.add_subplot(111)                        #define the axis

global counter
counter = 0

def sensor_random_value():

    x = np.random.randint(0, 20, None)              # create random value which resenble to sensor data Live
    y = np.random.randint(0, 20, None)              # create a another random variable to store Data Sensor 2

    my_sensor = "{},{}".format(x, y)                # create a Fake Data which represent the hardware data

    my_sensor_v.append(my_sensor)                   # append the data to the list for further processing
    #print(my_sensor_v)
    # Think this of hardware is sending serial data with , seperated
    # and we need to process that from a list


for x in range(0, 10):                              # this loop will generate aa random value or i must say 10 sample
    sensor_random_value()


def process_data():                                 # this Loop is represents processing power of python
    sensor_random_value()

    for data in my_sensor_v:
        # print("Data Reveived {}".format(data))
        # print(type(data))
        x,y=data.split(",")                         # split the data which Microcontoller is sending
        # print("X is : {} ".format(x))
        # print("Y is : {}".format(y))
        x1.append(x)                                # append the Temperature to the  data
        y1.append(y)                                # appand the humidity to the Listt

    return x,y


def plot_data(i):                                    # plot the Graph
    global counter
    counter += 1
    x, y = process_data()
    ax1.clear()
    ax1.plot(x1, y1)
    my_text("Temperature is  is {}".format(x))
    my_database(x,y)
    # post_cloud(x, y)


def my_text(text):                  # create a function to execute Text to Speech
    system("say {}".format(text))


def my_database(x, y):              # database  to store the data

    conn = sqlite3.connect("Test.db")
    cursor = conn.cursor()

    cursor.execute("""
     CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     temperature  TEXT, 
     humidity TEXT)""")

    cursor.execute("""
    INSERT INTO my_table (temperature,humidity) VALUES (?,?)""", (x, y))

    conn.commit()
    cursor.close()
    conn.close()


def post_cloud(x,y):                      # create a function to post on cloud server

    threading.Timer(15,post_cloud).start()

    URL='https://api.thingspeak.com/update?api_key='
    KEYS='54ESHV8Z5ZF0TPX4'
    HEADER='&field1={}&field2={}'.format(x, y)

    NEW_URL = URL+KEYS+HEADERS
    context = ssl._create_unverified_context()

    data = request.urlopen(NEW_URL,context=context)
    print(data)


def ifttt_send():                           # IFTTT notification
    # define payload thats a dictionary
    payload={'value1':'hello',
             'value2':11}

    # define Keys
    KEYS='Q-V9NBxTu3-7Xo98chRB_'

    # define URL
    URL='https://maker.ifttt.com/trigger/suhas/with/key/' # replace XX event name

    # Generate a new Url
    NEW_URL=URL+KEYS

    print(NEW_URL)
    requests.post(NEW_URL, data=payload)


def send_email(x,y):                        # sms module
    # Define your body
    my_body='Sensor data'
    # define client
    client = Client('AC437b2ebb5b00389b17e14990012090ec','4a0cb31f36c5a3beb46b537a9568cdc6')
    client.messages.create(to='+16462045957',
                           from_= '+19738603855',
                           body=my_body)


def get_weather_data():                     # weather module
    city='Bridgeport'
    key='ce45a4d1079e68c410cd42a3054d00e1'
    URL='http://api.openweathermap.org/data/2.5/weather?appid={}&q={}'.format(key,city)
    print(URL)

    data=requests.get(URL).json()
    print(data)

    long = data['coord']['lon']
    lat = data['coord']['lat']
    humidity=data['main']['humidity']
    wind_speed=data['wind']['speed']

    print(long,",",lat)
    print("Humidity", humidity)
    print("Windspeed", wind_speed)


if __name__ == "__main__":                                               # run the code
    ani = animation.FuncAnimation(fig, plot_data, interval = 2000)
    plt.show()



