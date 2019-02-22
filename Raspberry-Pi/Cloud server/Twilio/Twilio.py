from twilio.rest import Client


def send_sms_alert():

    # Define your body
    my_body='Yo'
    # define client
    client = Client('AC437b2ebb5b00389b17e14990012090ec','4a0cb31f36c5a3beb46b537a9568cdc6')
    client.messages.create(to='+16462045957',
                               from_= '+19738603855',
                               body=my_body)


send_sms_alert()