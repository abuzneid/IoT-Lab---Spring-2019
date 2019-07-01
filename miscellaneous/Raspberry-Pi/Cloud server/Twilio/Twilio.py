from twilio.rest import Client


def send_sms_alert():

    # Define your body
    my_body='Yo'
    # define client
    client = Client('XXXXXXXX','XXXXXXXXXX')
    client.messages.create(to='+1TO NUM',
                               from_= '+1TWILIO NO',
                               body=my_body)


send_sms_alert()
