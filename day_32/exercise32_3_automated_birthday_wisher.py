# Exercise 32.3. Automate Birthday Wisher

##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random as rd

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
# Access the data where the birthdays are in csv and create a list of dictionaries.
df = pd.read_csv("day_32/exercise32_3_automated_birthday_wisher_birthdays.csv")
birthday_data = df.to_dict(orient="records")


# Access the day and month of the data and check if they are any bithdays today.
now = dt.datetime.now()

birthdays_today = [birthday for birthday in birthday_data if birthday["month"]== now.month and birthday["day"]== now.day]

def pick_random_letter():
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        # Pick a letter randomly
        first_letter = "day_32/exercise32_3_automated_birthday_wisher_letter_1.txt"
        second_letter = "day_32/exercise32_3_automated_birthday_wisher_letter_2.txt"
        third_letter = "day_32/exercise32_3_automated_birthday_wisher_letter_3.txt"

        random_letter = rd.randint(1, 3)
        if random_letter == 1:
            letter = first_letter
        elif random_letter == 2:
            letter = second_letter
        else:
            letter = third_letter
        return letter


if len(birthdays_today) > 0:
    for person in birthdays_today:
        
        letter = pick_random_letter()

        # Get the letter text from the string_letter document and add it into a list
        final_letter = open(letter, mode="r")
        final_letter_list = final_letter.readlines()

        # 2. sustitute the [NAME] with the person who's birthday is today
        
        birthday_name = person["name"].strip()
        add_name = final_letter_list[0].replace("[NAME]", birthday_name)

        letter_content = final_letter_list[1:]
        clear_letter = "".join(letter_content)
        letter_to_send = add_name + clear_letter
        
        
        # Send the letter out to he user getting the email from the main line.
        my_email = "socmariabalos@gmail.com"
        my_password = "[INSERT API PASSWORD HERE]"
        # !!!!!!!!!!!!!!!!!!!!!!ADD DESTINATION BASED ON BIRTHDAY WHO'S BIRTHDAY TODAY
        destination = person["email"]
        msg = f"Subject: Happy Birthday\n\n {letter_to_send}"
        # print("---------------------")  
        # print(f"Subject: Happy Birthday\n\n {letter_to_send}")
        # print("---------------------")
        # print(f"Subject: Happy Birthday\n\n {letter_to_send}"[30:40])
        # print(type(f"Subject: Happy Birthday\n\n {letter_to_send}"[30:40].encode("utf-8")))

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=destination,
                msg=msg.encode('utf-8'),
            )
else:
    print("Sorry, today you have nothing to celebrate!")