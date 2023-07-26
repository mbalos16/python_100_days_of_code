# Exercise 36.1. Stock news monitoring

# IMPORTS
import requests
import datetime as dt
from twilio.rest import Client

# Please insert the autorization data to the constats to make it work
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc."
ALPHAVENTAGE_KEY = "[INSERT ALPHAVENTAGE KEY]"
AYLIEN_ID = "[INSERT ALPHAVENTAGE ID]"
AYLIEN_KEY = "[INSERT AYLIEN KEY]"
FROM_PHONE_NUMBER = "[INSERT FROM PHONE NUMBER]"
TO_PHONE_NUMBER = "[INSERT TO PHONE NUMBER]"
TWILIO_ACCOUNT_SID = "[INSERT TWILIO ACCOUNT SID]"
TWILIO_TOKEN = "[INSERT TWILIO TOKEN]"


def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        if current > previous:
            return (abs(current - previous) / previous) * 100.0
        else:
            return (abs(previous - current) / current) * 100.0
    except ZeroDivisionError:
        return 0


def get_news():
    news_content = []
    headers = {
        "X-AYLIEN-NewsAPI-Application-ID": AYLIEN_ID,
        "X-AYLIEN-NewsAPI-Application-Key": AYLIEN_KEY,
    }
    news_url = 'https://api.aylien.com/news/stories?aql=industries:({{id:in.motor}}) AND language:(en) AND categories:({{taxonomy:aylien AND id:ay.fin}}) AND entities:({{surface_forms.text:"AMZN" AND overall_prominence:>=0.65}}) AND sentiment.title.polarity:(negative neutral positive)&cursor=*&published_at.end=NOW&published_at.start=NOW-7DAYS/DAY'
    r = requests.get(news_url, headers=headers)
    data = r.json()
    for x in range(0, 3):
        news_content.append(data["stories"][x]["summary"]["sentences"][x + 1])
    return news_content


## S When STOCK price increase by 5% between yesterday and the day before yesterday then print("Get News").
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&interval=3min&apikey={ALPHAVENTAGE_KEY}"
r = requests.get(url)
data = r.json()["Time Series (Daily)"]
data_list = [values for key, values in data.items()]
yesterday = data_list[0]
yesterday_closing_price = yesterday["4. close"]

before_yesterday = data_list[1]
before_yesterday_closing_price = before_yesterday["4. close"]

percentage = int(
    get_change(float(yesterday_closing_price), float(before_yesterday_closing_price))
)
message_body = get_news()

if percentage >= 5:
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"TSLA: 🔺{percentage}% \n{message_body[0]} \n{message_body[1]} \n{message_body[2]}",
        from_=FROM_PHONE_NUMBER,
        to=TO_PHONE_NUMBER,
    )
    print(message.status)
else:
    print(f"The percentage is: {percentage}%")
