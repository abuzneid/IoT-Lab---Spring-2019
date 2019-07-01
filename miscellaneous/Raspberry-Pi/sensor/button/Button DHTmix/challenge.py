import tkinter as tk
import numpy as np
import random
import time
import datetime
import threading
import Adafruit_DHT

from time import sleep # Library will let us put in delays
import RPi.GPIO as GPIO

pin = 4
sensor = Adafruit_DHT.DHT22

button1_pin=12 # Button 1 is connected to physical pin 12

GPIO.setmode(GPIO.BOARD) # Use Physical Pin Numbering Scheme

GPIO.setup(button1_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
# Make button1_pin an input, Activate Pull UP Resistor




def tick():
    time2=time.strftime('%H:%M:%S')
    clock.config(text=time2)
    clock.after(200,tick)
    

def button_pressed_mech():
    threading.Timer(1,button_pressed_mech).start()
    input1=GPIO.input(button1_pin)
    if input1==0:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            l_display.config(text = temperature)
            l_display1.config(text = humidity)

        else:
            print('Failed to get reading. Try again!')

mainwindow = tk.Tk()
mainwindow.geometry('640x340')
mainwindow.title("Sensor Data Live Feed ")

clock=tk.Label(mainwindow,font=("Arial",30), bg='green',fg="white")
clock.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

l_m=tk.Label(mainwindow,text="Sensor Data ",font=("Arial",30),fg="Black")
l_m.grid(row=0,column=1, padx=10, pady=10, sticky="nsew")

l_t=tk.Label(mainwindow, text="Temperature C",font=("Arial",25))
l_t.grid(row=1,column=0, padx=10, pady=10, sticky="nsew")


l_display=tk.Label(mainwindow,font=("Arial",25),fg="red")
l_display.grid(row=1,column=1, padx=10, pady=10, sticky="nsew")


l_h=tk.Label(mainwindow, text="Humidity C",font=("Arial",25))
l_h.grid(row=2,column=0, padx=10, pady=10, sticky="nsew")


l_display1=tk.Label(mainwindow,font=("Arial",25),fg="red")
l_display1.grid(row=2,column=1, padx=10, pady=10, sticky="nsew")

tick()

button_pressed_mech()

mainwindow.mainloop()

