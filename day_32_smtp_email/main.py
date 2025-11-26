##################### Extra Hard Starting Project ####################

import smtplib
import datetime as dt
import pandas as pd
import os
from random import choice

my_email = "somebody@email.com"
password = "password"


data = pd.read_csv("day_32_smtp_email/birthdays.csv")

now = dt.datetime.now()
year = now.year
day = now.day
month = now.month

birthday = data[(data.Month == month) & (data.Day == day)]
if not birthday.empty:
    files = os.listdir("day_32_smtp_email/letter_templates")
    filename = choice(files)
    with open(f"day_32_smtp_email/letter_templates/{filename}") as f:
        chosen_letter = f.read()

    for _, row in birthday.iterrows():
        name = row["Name"]
        email = row["Email"]
    
        send_letter = chosen_letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject: Happy Birthday\n\n{send_letter}")


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




