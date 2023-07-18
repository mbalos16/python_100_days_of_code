import requests
from datetime import datetime
import smtplib
import time

MY_LAT = ["insert your latitude here"]
MY_LON = ["insert your longitude here"]
FROM_EMAIL = "socmariabalos@gmail.com"
PERSONAL_API_PASSWORD = "[insert your password here]"
TO_EMAIL = "socmariabalos@gmail.com"


# If the ISS is close to my current possition
def check_position():
    # Iss api access
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        MY_LAT - 5 <= iss_latitude >= MY_LAT + 5
        and MY_LON - 5 <= iss_longitude <= MY_LON + 5
    ):
        return True


# 1. and it is currently dark
def check_night():
    # Sunshine/sunset api access
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0,
    }

    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters
    )
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour < sunrise and time_now.hour > sunset:
        return True
    else:
        return False


def send_email():
    my_email = FROM_EMAIL
    my_password = PERSONAL_API_PASSWORD
    destination = TO_EMAIL
    msg = f"Subject: ISS is up\n\n Get out and look up to the sky"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=destination,
            msg=msg.encode("utf-8"),
        )


while True:
    time.sleep(60)
    if check_position() and check_night():
        send_email()
    else:
        print("Sorry, is not time yet.")
