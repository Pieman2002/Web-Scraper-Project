import requests 
import re
from twilio.rest import Client
from bs4 import BeautifulSoup

#Twilio Inputs
sender = input("Please enter your trial number here.")
yournumber = input("Please enter your phone number here.")
account_sid = input("Please enter your Account SID here.")
auth_token = input("Please enter your Authorization Token here.")

#Scraper Bit
page = requests.get("https://weather.com/weather/today/l/97202:4:US")
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='today_nowcard-temp')
RawTemp = str(results.find('span'))

if len(RawTemp) == 35:
  temp = RawTemp[15:16]

if len(RawTemp) == 36:
  temp = RawTemp[15:17]

if len(RawTemp) == 37:
  temp = RawTemp[15:18]
  
#Twilio Communication
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='The temperature is now ' + temp,
         from_=sender,
         to=yournumber
     )

print(message.sid)
