# Documentation

This file consists of things I have found useful.

## Actual Twilio message sending code:
```
message = client.messages \
.create(
        body = "Text to send to user's number",
        from_=twilio_phone_number,
        to=my_phone_number
```
