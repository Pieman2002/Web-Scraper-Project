# Documentation

This file is for both using the scraper and building the scraper. I am not an expert with these sorts of things.
## Table of Contents
- [Title](https://github.com/Pieman2002/Web-Scraper-Project/blob/Liam/documentation.md#documentation)
- [Table of Contents](https://github.com/Pieman2002/Web-Scraper-Project/blob/Liam/documentation.md#table-of-contents)
- [Twilio](https://github.com/Pieman2002/Web-Scraper-Project/blob/Liam/documentation.md#twilio)

## Strings in Python


## Twilio
Twilio is a great resource for getting actual feedback from your code. Here are some things that might help Twilio beginners:

**DO NOT** release your trial number! You never know when it will come in handy.

Here is the code that Twilio gives its users:
```
client = Client(account_sid, auth_token)

message = client.messages \
.create(
        body = "Text to send to user's number",
        from_=twilio_phone_number,
        to=my_phone_number
```
You need four variables for the code to work. Three of the four are Twilio related (and can be found on your Twilio page), with the last one being your phone number.
