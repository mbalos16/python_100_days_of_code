# Exercise 32.2. Motivational Monday Quote

import smtplib
import datetime as dt
import pandas as pd
import random as rd

my_email = "socmariabalos@gmail.com"
my_password = "[INSERT API PASSWORD HERE]"
destination = "socmariabalos@yahoo.com"

with open("day_32/exercise32_2_motivational_monday_quotes.txt", mode="r") as file:
    quotes_list = file.readlines()
    random_number = rd.randint(0, len(quotes_list))
    quote = quotes_list[random_number]
    message = quote

now = dt.datetime.now()
day = now.day

if day == 13:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=destination,
            msg=f"Subject: Monday Motivation\n\nHi, \n\n {message}",
        )
