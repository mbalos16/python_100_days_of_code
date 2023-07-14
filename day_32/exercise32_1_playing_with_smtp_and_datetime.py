# Testion the SMTP module and DATETIME module

# SMTP module

import smtplib

my_email = "socmariabalos@gmail.com"
my_password = "[INSERT API PASSWORD HERE]"
destination = "socmariabalos@yahoo.com"


# Connect with server clossing the connection:
# connection = smtplib.SMTP("smtp.gmail.com")
# adding: connection.close() on the end or:

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=destination,
        msg="Subject: I'm automatic\n\n Hi, here is a message.\n And here is another message :D.",
    )


# Datetime module
import datetime as dt

now = dt.datetime.now()
day = now.day
month = now.month
year = now.year
