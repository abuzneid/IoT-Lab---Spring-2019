try:
    from urllib import request
    from urllib.request import urlopen
    import threading                    # import threadding
    import json                         # import json
    import random                       # import random
    import requests                     # import requests
    import ssl
except:
    print("No Library Found")


def thingspeak_post():

    threading.Timer(15, thingspeak_post).start()
    val=random.randint(1, 30)

    URL=' '
    KEY='54ESHV8Z5ZF0TPX4'
    HEADER='&field1={}&field2={}'.format(val, val)

    NEW_URL = URL + KEY + HEADER
    print(NEW_URL)

    context = ssl._create_unverified_context()

    data=request.urlopen(NEW_URL,context=context)
    print(data)


def read_data_thingspeak():
    t_data=[]

    URL='http://api.thingspeak.com/channels/103357/feeds.json?api_key='
    KEYS='G9SQN8G512L8SQMS'
    HEADER='&results=2'                                                 # modify here to get data

    NEW_URL = URL + KEYS + HEADER
    print(NEW_URL)

    data=requests.get(NEW_URL).json()
    #print(data)

    channel_id=data['channel']['id']
    #print(channel_id)

    x_label=data['channel']["field1"]

    field1=data['feeds']

    for x in field1:

        #print(x)
        #print(x['field1'])

        t_data.append(x['field1'])

    print(t_data)


if __name__ == "__main__":
    read_data_thingspeak()
