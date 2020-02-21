import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

#Inputs for Twilio
sender = input("Please enter your trial number here.")
yournumber = input("Please enter your phone number here.")
account_sid = input("Please enter your Account SID here.")
auth_token = input("Please enter your Authorization Token here.")

#Actual scraper bit
url = "https://katu.com/resources/ftptransfer/katu/traffic/traffic.html"
page  = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
text = soup.findAll(text=True)

output = ''
blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head',
	'input',
	'script',
	'meta',
	'style',
]

for t in text:
	if t.parent.name not in blacklist:
		output += '{} '.format(t)

#print(output)

#Twilio Communication System
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body=output,
         from_=sender,
         to=yournumber
     )

print(message.sid)
