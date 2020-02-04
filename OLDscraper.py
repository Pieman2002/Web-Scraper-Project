from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import html2text
from varsScrape import *
import time
import filecmp

# Getting client info and the soup
client = Client(account_sid, auth_token)
url = input("Enter a URL:")
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

# Save initial soup to a text document
f = open("initSoup.txt","w+")
f.write(str(soup))
f.close

# Get time intervals
getWaitTime = input("Number of seconds between searches:")
waitTime = int(getWaitTime)

# Will it spam the server too much?
if(waitTime < 3):
    waitTime = 3
    print("Number of seconds too low. Three seconds chosen.")

getTimesChecked = input("Number of searches:")
timesChecked = int(getTimesChecked)
if(timesChecked > 30):
    timesChecked = 30
    print("Times serched is too high. 30 checks chosen.")
while (timesChecked > 0):

    # Grab the page again
    r = requests.get(url)
    data = r.text
    newSoup = BeautifulSoup(data, 'html.parser')
#-------------------------------------------------------------------------------------------------------
    # Copy newSoup to new file
    f = open("newSoup.txt","w+")
    f.write(str(soup))
    f.close

    # DOESN'T WORK!
    if filecmp.cmp("newSoup.txt", "initSoup.txt", shallow=True) == False:
        print("Change!")
        message = client.messages \
        .create(
            body = "Something changed!",
            from_=twilio_phone_number,
            to=my_phone_number
        )
    else:
        print("No changes detected.")
    timesChecked -= 1
    if (timesChecked > 0):
        time.sleep(waitTime)
    else:
        # Added a small delay
        time.sleep(2)
        print("Done.")
        message = client.messages \
        .create(
            body = "Done",
            from_=twilio_phone_number,
            to=my_phone_number
        )
