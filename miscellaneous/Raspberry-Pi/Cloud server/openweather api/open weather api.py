import urllib
import requests
from urllib import request
from urllib.request import urlopen
import json

def get_weather_data():
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


if __name__ == "__main__":
    get_weather_data()
