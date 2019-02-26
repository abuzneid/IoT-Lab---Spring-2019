import geocoder
import threading
import datetime

def get_geolocations():
    try:
        g = geocoder.ip('me')
        my_string=g.latlng
        longitude=my_string[0]
        latitude=my_string[1]

        return longitude,latitude
    except:
        print('Could Not Get the  Co-ordinates!')


def get_time():
    my=datetime.datetime.now()
    data_time = '{}:{}:{}'.format(my.hour,my.minute,my.second)
    data_date='{}/{}/{}'.format(my.day,my.month,my.year)
    return  data_date,data_time

def main():
    threading.Timer(10,main,args=None).start()
    longitude,latitude = get_geolocations()
    data_date,data_time = get_time()
    print("lat",latitude)



if __name__ == '__main__':
    main()