from twilio.rest import Client

sender = raw_input("Please enter your trial number here.")
yournumber = raw_input("Please enter your phone number here."
account_sid = raw_input("Please enter your Accound SID here.")
auth_token = raw_input("Please enter your Authorization Token here.")
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="WIP",
                     from_='sender',
                     to='yournumber'
                )
                
print(message.sid)
