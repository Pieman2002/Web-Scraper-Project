from twilio.rest import Client

sender = input("Please enter your trial number here.")
yournumber = input("Please enter your phone number here.")
account_sid = input("Please enter your Account SID here.")
auth_token = input("Please enter your Authorization Token here.")
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='WIP',
         from_=sender,
         to=yournumber
     )

print(message.sid)
