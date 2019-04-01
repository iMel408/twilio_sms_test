import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Melissa testing out this Twilio stuff :).",
                     from_=os.environ['TWILIO_NUMBER'],
                     to=os.environ['MY_PHONE_NUMBER']
                 )

print(message.sid)
