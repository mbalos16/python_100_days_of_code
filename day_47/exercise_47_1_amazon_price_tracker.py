import smtplib
import requests
from bs4 import BeautifulSoup


PRODUCT_LINK = "https://www.amazon.co.uk/Thames-Kosmos-Calendar-Solving-Strategy/dp/B0BSHRYPFB/ref=sr_1_1?"
PRICE_GOAL = 30
MY_EMAIL = "[socmariabalos@gmail.com]"
MY_PASSWORD = "[INSERT GOOGLE API PASSWORD HERE]"
EMAIL_DESTINATION = "socmariabalos@yahoo.com"


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=EMAIL_DESTINATION,
            msg=(
                f"Subject: 💸 Amazon Price Alert! \n\nBuy it, baby! \n\n {message}"
            ).encode("utf-8"),
        )


# Use of my HTTP Header to pass to amazon
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
}
response = requests.get(url=PRODUCT_LINK, headers=headers)
azn_website = response.text

# with open("day_47/azn.html", "w") as file:
#     file.write(azn_website)


# Using soup to find item
soup = BeautifulSoup(azn_website, "html.parser")
find_price = soup.find(class_="a-price-whole")
# price = float((find_price.getText()).replace(".", ""))
price = 10
product_name = soup.find(
    class_="_p13n-desktop-sims-fbt_fbt-mobile_title-component-overflow3__3p-Qn"
)
name = (product_name.getText()).replace("This item:  ", "")


# If the proce is below send an email
if price <= PRICE_GOAL:
    message = f"The new price for the product {name} is: {price}."
    send_email(message)
else:
    print("Tomorrow is the day!")
