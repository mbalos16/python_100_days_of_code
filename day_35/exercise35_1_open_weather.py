# Exercise 35.1. Open Weather using key APIs

import requests
from twilio.rest import Client

OPEN_WEATHER_APPID = "[INSERT YOUR WEATHER APPI HERE]"
ACCOUNT_SID = "[YOUR ACCOUNT SID]"
AUTH_TOKEN = "[YOUR AUTH TOKEN]"
FROM_PHONE_NUMBER = "[A PHONE NUMBER HERE]"
TO_PHONE_NUMBER = "[ANOTHER PHONE NUMBER HERE]"

response = requests.get(
    url=f"http://api.openweathermap.org/data/2.5/weather?q=Cambridge,uk&APPID={OPEN_WEATHER_APPID}"
)
response.raise_for_status()
data = response.json()

if int(data["weather"][0]["id"]) < 700:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️.",
        from_=FROM_PHONE_NUMBER,
        to=TO_PHONE_NUMBER,
    )
    print(message.status)
