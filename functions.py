# initialise twililo
from twilio.rest import Client
from constants import *

def send_sms(phone, message, image_url=None):
    # print(message)
    # declare initial values for twililo
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    # send whatsapp message
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=phone,
        media_url=image_url
    )

    print(message.sid)


def send_sms1(phone, message):
    print(message)